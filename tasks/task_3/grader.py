# grader.py for Hard Task

def grade(raw_scores, consistency_bonus=0.15, explanation_bonus=0.15, catastrophic_penalty=0.6):
    """
    Hard task validator-safe grader
    """
    mean_score = sum(raw_scores) / len(raw_scores)
    final_score = mean_score + consistency_bonus + explanation_bonus - catastrophic_penalty

    epsilon = 1e-6
    final_score = max(epsilon, min(1 - epsilon, final_score))

    return float(final_score)
