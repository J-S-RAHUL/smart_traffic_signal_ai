import math

def grade(raw_scores=None, **kwargs):
    """
    Medium Task grader — Peak Hour Congestion.
    Returns a float STRICTLY between 0 and 1 (never 0.0, never 1.0).
    """
    EPSILON = 1e-6
    LOW     = EPSILON
    HIGH    = 1.0 - EPSILON

    try:
        if not raw_scores:
            return 0.5
        scores = [float(s) for s in raw_scores if math.isfinite(float(s))]
        if not scores:
            return 0.5
        mean = sum(scores) / len(scores)
        if kwargs.get("consistency_bonus") is True:
            mean += 0.10
        if kwargs.get("explanation_bonus") is True:
            mean += 0.10
        if kwargs.get("catastrophic") is True:
            mean -= 0.50
        return float(max(LOW, min(HIGH, mean)))
    except Exception:
        return 0.5
