# pipeline.py

import json
from agents.extraction import extract_profile
from agents.scoring    import score_profile
from agents.decision   import decide_profile

def main():
    # 1. Ingest input from sample JSON
    try:
        with open("data/sample_submission.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: 'data/sample_submission.json' not found.")
        return

    # 2. Data Extraction
    print("=== Extraction Step ===")
    profile, extraction_cot = extract_profile(data)
    print("Structured Profile:")
    print(json.dumps(profile, indent=2))
    print("\nChain of Thought (Extraction):")
    for step in extraction_cot:
        print(" •", step)

    # 3. Scoring
    print("\n=== Scoring Step ===")
    scores, scoring_details = score_profile(profile)
    for metric, score in scores.items():
        detail = scoring_details.get(metric, "")
        print(f"{metric}: {score}    ({detail})")

    # 4. Decision
    print("\n=== Decision Step ===")
    decision, rationale, decision_cot = decide_profile(profile, scores)
    print(f"Decision: {decision}")
    print("Rationale:")
    print(rationale)
    print("\nChain of Thought (Decision):")
    for step in decision_cot:
        print(" •", step)

if __name__ == "__main__":
    main()
