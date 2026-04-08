# tasks/task_3/grader.py

def grade(output=None, expected_output=None, observation=None, **kwargs):
    """
    Task 3: Emergency Vehicle Priority
    Returns a float strictly between 0 and 1.
    Applies catastrophic penalties and bonuses for smart behavior.
    """
    epsilon = 1e-6  # validator-safe margin

    try:
        action = int(str(output).strip())

        # observation = [N, S, E, W] traffic densities
        if observation and isinstance(observation, list):
            max_road = observation.index(max(observation))

            # Raw score logic
            if action == max_road:
                raw_score = 0.90  # perfect
            elif action in [0, 1, 2, 3]:
                raw_score = 0.70  # partial credit
            else:
                raw_score = 0.15  # false positive / ignored emergency

        else:
            raw_score = 0.50 if action in [0, 1, 2, 3] else 0.10

        # Catastrophic penalty: ignore emergency vehicle
        catastrophic_penalty = 0.0
        if raw_score <= 0.10:
            catastrophic_penalty = 0.50

        # Consistency bonus: reliable selection
        consistency_bonus = 0.0
        if raw_score >= 0.70:
            consistency_bonus = 0.10

        # Explanation bonus: perfect actions + reasoning
        explanation_bonus = 0.0
        if raw_score >= 0.90:
            explanation_bonus = 0.05

        # Final score computation
        final_score = raw_score + consistency_bonus + explanation_bonus - catastrophic_penalty

        # Clip strictly inside (0,1) for validator
        final_score = max(epsilon, min(1 - epsilon, final_score))
        return float(final_score)

    except Exception:
        return float(epsilon)
