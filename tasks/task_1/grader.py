# grader.py for Easy Task

def grade(raw_scores, consistency_bonus=0.05, explanation_bonus=0.05, catastrophic_penalty=0.4):
    """
    Easy task validator-safe grader
    """
    # Step 1: Compute mean of raw_scores
    mean_score = sum(raw_scores) / len(raw_scores)

    # Step 2: Apply bonuses and catastrophic penalty
    final_score = mean_score + consistency_bonus + explanation_bonus - catastrophic_penalty

    # Step 3: Clip strictly between 0 and 1
    epsilon = 1e-6
    final_score = max(epsilon, min(1 - epsilon, final_score))

    # Step 4: Return float
    return float(final_score)
