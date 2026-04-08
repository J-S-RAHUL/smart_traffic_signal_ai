import os
import random
from openai import OpenAI

# ── Grader imports ───────────────────────────────────────────────────────────
from tasks.task_1.grader import grade as grade_task1
from tasks.task_2.grader import grade as grade_task2
from tasks.task_3.grader import grade as grade_task3

ROADS = ["North", "South", "East", "West"]

# ── Traffic state generators ─────────────────────────────────────────────────

def generate_state_task1():
    """Easy: simple random traffic counts, no emergency."""
    counts = {r: random.randint(0, 100) for r in ROADS}
    correct = max(counts, key=counts.get)
    return counts, None, correct

def generate_state_task2():
    """Medium: peak-hour multipliers on two roads."""
    counts = {r: random.randint(10, 80) for r in ROADS}
    peak_road = random.choice(ROADS)
    counts[peak_road] = int(counts[peak_road] * 1.8)   # peak hour surge
    correct = max(counts, key=counts.get)
    return counts, None, correct

def generate_state_task3():
    """Hard: one road has an emergency vehicle — must be prioritised."""
    counts = {r: random.randint(10, 80) for r in ROADS}
    emergency_road = random.choice(ROADS)
    correct = emergency_road   # emergency always wins
    return counts, emergency_road, correct

# ── Score a single LLM decision ──────────────────────────────────────────────

def score_decision(chosen: str, correct: str, emergency_road) -> float:
    """Return a per-step reward in (0, 1) based on decision quality."""
    if emergency_road and chosen != emergency_road:
        return 0.10   # catastrophic: ignored emergency vehicle

    if chosen == correct:
        return 0.90   # perfect

    # Partial credit — wrong road but at least responded
    return 0.50

# ── LLM call ─────────────────────────────────────────────────────────────────

def call_llm(task_id: str, counts: dict, emergency_road) -> str:
    """Ask the LLM which road to prioritise. Returns road name."""
    traffic_summary = "\n".join(
        f"  {road}: {count} vehicles" + (" [EMERGENCY VEHICLE]" if road == emergency_road else "")
        for road, count in counts.items()
    )

    prompt = (
        f"You are a smart traffic signal controller.\n"
        f"Task: {task_id}\n\n"
        f"Current traffic state:\n{traffic_summary}\n\n"
        f"Which road should get the GREEN signal right now?\n"
        f"Reply with ONLY one word — the road name: North, South, East, or West."
    )

    try:
        client = OpenAI(
            base_url=os.environ["API_BASE_URL"],
            api_key=os.environ["API_KEY"]
        )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content.strip().capitalize()
        if result not in ROADS:
            print(f"[WARN] LLM returned unexpected road '{result}', using fallback")
            return random.choice(ROADS)
        return result

    except Exception as e:
        print(f"[ERROR] LLM call failed: {e}")
        return random.choice(ROADS)   # fallback: random valid road

# ── Run a single task over N steps ───────────────────────────────────────────

def run_task(task_id: str, steps: int = 5) -> float:
    """
    Simulate `steps` traffic decisions, collect per-step scores,
    then call the appropriate grader and return a final score in (0, 1).
    """
    print(f"\n[START] {task_id} — {steps} steps")

    if task_id == "task_1":
        generate_state = generate_state_task1
        grader = grade_task1
    elif task_id == "task_2":
        generate_state = generate_state_task2
        grader = grade_task2
    elif task_id == "task_3":
        generate_state = generate_state_task3
        grader = grade_task3
    else:
        raise ValueError(f"Unknown task_id: {task_id}")

    raw_scores = []
    had_catastrophic = False

    for step in range(1, steps + 1):
        counts, emergency_road, correct = generate_state()
        chosen = call_llm(task_id, counts, emergency_road)
        step_score = score_decision(chosen, correct, emergency_road)

        print(f"  Step {step}: correct={correct}, chosen={chosen}, score={step_score:.2f}")
        raw_scores.append(step_score)

        if emergency_road and chosen != emergency_road:
            had_catastrophic = True

    # Determine trajectory bonuses
    consistency_bonus = len(set(raw_scores)) == 1          # all steps identical = fully consistent
    explanation_bonus = all(s >= 0.70 for s in raw_scores)  # all steps high quality

    final_score = grader(
        raw_scores,
        consistency_bonus=consistency_bonus,
        explanation_bonus=explanation_bonus,
        catastrophic=had_catastrophic
    )

    print(f"[RESULT] {task_id}: raw_scores={raw_scores}, final_score={final_score:.6f}")
    return final_score


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    results = {}
    for task in ["task_1", "task_2", "task_3"]:
        try:
            score = run_task(task)
            results[task] = score
        except Exception as e:
            print(f"[FATAL] {task} failed: {e}")
            results[task] = 1e-6   # safe fallback — strictly > 0

    print("\n=== FINAL SCORES ===")
    for task, score in results.items():
        status = "✅ VALID" if 0 < score < 1 else "❌ INVALID"
        print(f"  {task}: {score:.6f}  {status}")
