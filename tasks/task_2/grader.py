# grader.py for Medium Task

import math

def grade(raw_scores, consistency_bonus=False, explanation_bonus=False, catastrophic=False):
    """
    Medium task validator-safe grader.

    Args:
        raw_scores (list): Per-step reward scores from the trajectory.
        consistency_bonus (bool): Set True only if the agent was consistent throughout.
        explanation_bonus (bool): Set True only if the agent provided good explanations.
        catastrophic (bool): Set True only if a catastrophic event occurred.

    Returns:
        float: Final score strictly in (0, 1).
    """
    epsilon = 1e-6

    # Guard: empty trajectory
    if not raw_scores:
        return float(epsilon)

    mean_score = sum(raw_scores) / len(raw_scores)

    # Guard: NaN or Inf bypasses clipping — catch it explicitly
    if not math.isfinite(mean_score):
        return float(epsilon)

    # Apply modifiers only when actually triggered
    final_score = mean_score
    if consistency_bonus:
        final_score += 0.10
    if explanation_bonus:
        final_score += 0.10
    if catastrophic:
        final_score -= 0.50

    # Strict open-interval clip: 0 < score < 1
    final_score = max(epsilon, min(1 - epsilon, final_score))
    return float(final_score)
