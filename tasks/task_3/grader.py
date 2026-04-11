import math

def grade(*args, **kwargs):
    raw_scores = args[0] if args else kwargs.get("raw_scores", None)
    EPSILON = 1e-6
    try:
        if not raw_scores:
            return 0.5
        scores = [float(s) for s in raw_scores if math.isfinite(float(s))]
        if not scores:
            return 0.5
        mean = sum(scores) / len(scores)
        if kwargs.get("consistency_bonus") is True:
            mean += 0.15
        if kwargs.get("explanation_bonus") is True:
            mean += 0.15
        if kwargs.get("catastrophic") is True:
            mean -= 0.60
        return float(max(EPSILON, min(1.0 - EPSILON, mean)))
    except Exception:
        return 0.5
