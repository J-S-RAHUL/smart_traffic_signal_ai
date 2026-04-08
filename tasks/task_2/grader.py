# tasks/task_2/grader.py

def grade(output=None, expected_output=None, observation=None, **kwargs):
    """
    Task 2: Peak Hour Congestion
    Returns a float strictly between 0 and 1.
    """
    epsilon = 1e-6  # validator-safe margin

    try:
        action = int(str(output).strip())

        # observation contains [N, S, E, W] traffic densities
        if observation and isinstance(observation, list):
            max_road = observation.index(max(observation))
            raw_score = 0.99 if action == max_road else 0.01
        else:
            raw_score = 0.99 if action in [0, 1, 2, 3] else 0.01

        # Clip strictly inside (0,1)
        final_score = max(epsilon, min(1 - epsilon, float(raw_score)))
        return final_score

    except Exception:
        return float(epsilon)
