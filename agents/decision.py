# agents/decision.py
def decide_profile(profile: dict, scores: dict):
    overall_score = sum(scores.values()) / len(scores)
    threshold = 7.0
    decision = "INVEST" if overall_score >= threshold else "PASS"
    rationale = (
        f"The weighted average score is {overall_score:.1f}/10. "
        f"Market scored {scores['Market']}, Team scored {scores['Team']}, "
        f"Traction scored {scores['Traction']}, and Product Clarity scored {scores['Product Clarity']}. "
        f"Based on this analysis, we recommend {decision}."
    )
    chain_of_thought = [
        f"Sub-scores: {scores}",
        f"Computed overall_score = {overall_score:.1f}",
        f"Threshold = {threshold} → Decision = {decision}"
    ]
    return decision, rationale, chain_of_thought
