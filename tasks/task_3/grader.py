def grade(output=None, expected_output=None, observation=None, **kwargs):
    try:
        action = int(str(output).strip())

        if observation and isinstance(observation, dict):
            traffic = observation.get("traffic", [])
            emergency = observation.get("emergency", [])

            if emergency and 1 in emergency:
                emergency_road = emergency.index(1)
                return 0.99 if action == emergency_road else 0.01

            if traffic:
                max_road = traffic.index(max(traffic))
                return 0.99 if action == max_road else 0.01

        return 0.99 if action in [0, 1, 2, 3] else 0.01

    except Exception:
        return 0.01
