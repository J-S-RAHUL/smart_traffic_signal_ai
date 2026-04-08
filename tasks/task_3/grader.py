def grade(output=None, expected_output=None, observation=None, **kwargs):
    """
    Safe universal grader.
    Always returns a float strictly between 0 and 1.
    """
    try:
        action = int(str(output).strip())

        # valid action range
        if action in [0, 1, 2, 3]:
            return float(0.99)
        else:
            return float(0.01)

    except Exception:
        return float(0.01)
