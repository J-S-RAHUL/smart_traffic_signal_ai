import os
from openai import OpenAI


def call_llm(task_id):
    try:
        client = OpenAI(
            base_url=os.environ["API_BASE_URL"],
            api_key=os.environ["API_KEY"]
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"Choose the best traffic signal action for {task_id}. Return only 0, 1, 2, or 3."
                }
            ]
        )

        result = response.choices[0].message.content.strip()

        # safety check
        if result not in ["0", "1", "2", "3"]:
            print("[WARN] Invalid LLM response, using fallback")
            return "0"

        return result

    except Exception as e:
        print(f"[ERROR] API call failed: {e}")
        return "0"


def run_task(task_id):
    try:
        print(f"[START] task={task_id}")

        output = call_llm(task_id)

        print(output)
        return output

    except Exception as e:
        print(f"[ERROR] run_task failed: {e}")
        print("0")
        return "0"


if __name__ == "__main__":
    tasks = ["task_1", "task_2", "task_3"]

    for task in tasks:
        try:
            run_task(task)
        except Exception as e:
            print(f"[FATAL] {e}")
            print("0")
