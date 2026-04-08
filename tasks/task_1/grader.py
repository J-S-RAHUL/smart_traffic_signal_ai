def grade(output, expected_output=None, observation=None, **kwargs):
    """
    Universal Grader for Smart Traffic Signal AI.
    Checks if the agent selected the road with the highest traffic.
    """
    try:
        # Convert output to integer (Action 0, 1, 2, or 3)
        action = int(str(output).strip())
        
        # If the validator provides the observation [N, S, E, W]
        if observation and isinstance(observation, list):
            max_traffic_road = observation.index(max(observation))
            return 1.0 if action == max_traffic_road else 0.0
        
        # Fallback: If observation isn't passed, check if action is valid
        if action in [0, 1, 2, 3]:
            return 1.0
        return 0.0
        
    except Exception:
        # Return 0 if the output is not a valid number
        return 0.0
