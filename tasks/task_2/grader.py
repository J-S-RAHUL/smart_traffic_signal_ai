def grade(output=None, expected_output=None, observation=None, **kwargs):
    try:
        action = int(str(output).strip())

        if observation and isinstance(observation, list):
            max_road = observation.index(max(observation))
            return 0.99 if action == max_road else 0.01

        return 0.99 if action in [0, 1, 2, 3] else 0.01

    except Exception:
        return 0.01
