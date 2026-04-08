def grade(output, expected_output=None, observation=None, **kwargs):
    """
    Grader for Emergency Vehicle Priority.
    Emergency vehicle road must be selected first.
    """
    try:
        action = int(str(output).strip())

        if observation and isinstance(observation, dict):
            traffic = observation.get("traffic", [])
            emergency = observation.get("emergency", [])

            # Priority to emergency vehicle
            if 1 in emergency:
                emergency_road = emergency.index(1)
                return 1.0 if action == emergency_road else 0.0

            # Otherwise choose max traffic
            if traffic:
                max_road = traffic.index(max(traffic))
                return 1.0 if action == max_road else 0.0

        return 1.0 if action in [0, 1, 2, 3] else 0.0

    except Exception:
        return 0.0
