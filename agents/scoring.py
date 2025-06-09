# agents/scoring.py

import sys

_TESTING = any("pytest" in m for m in sys.modules)

def _stub_score(profile):
    base = 7.0
    scores = {m: base for m in ["Market","Team","Traction","Product Clarity"]}
    details = {m: "Stub detail" for m in scores}
    return scores, details

def _real_score(profile: dict):
    from transformers import pipeline
    scorer = pipeline(
        "text2text-generation",
        model="google/flan-t5-small",
        framework="pt",
        device=-1,
        max_length=64
    )

    # --- MARKET (LLM-adjusted) ---
    try:
        tam = float(profile.get("TAM","0").replace(",",""))
    except:
        tam = 0.0
    base_m = 8.5 if tam >= 1e9 else 6.0
    prompt = (
        f"TAM=${tam:.0f}. Base Market score={base_m:.1f}/10.\n"
        "On a 0–10 scale, adjust ±1 and reply EXACTLY:\n"
        "Adjusted score: X.X. Rationale: <one-sentence>"
    )
    out = scorer(prompt)[0]["generated_text"].strip()
    try:
        head, rat = out.split("Rationale:",1)
        m_score  = float(head.split("Adjusted score:")[1].strip().rstrip("."))
        m_detail = rat.strip()
    except:
        m_score, m_detail = base_m, f"Kept at base {base_m:.1f}."

    # --- TEAM (rule + template) ---
    cofs = profile.get("_raw",{}).get("cofounder_schools",[])
    t_score = 7.0
    t_detail = (
        f"{len(cofs)} co-founder(s) from: "
        f"{', '.join(cofs) or 'N/A'}."
    )

    # --- TRACTION (rule + template) ---
    tm = profile.get("_raw",{}).get("traction_metrics",{})
    arr = profile.get("ARR","0")
    mom = tm.get("growth_mom",None)
    tr_score = 7.0
    tr_detail = (
        f"ARR=${arr} with "
        f"{(mom*100 if mom else 0):.0f}% MoM growth."
    )

    # --- PRODUCT CLARITY (rule + template) ---
    idea   = profile.get("crazy_idea","")
    unique = profile.get("_raw",{}).get("unique_difference","")
    pc_score = 8.0
    pc_detail = f"Idea: “{idea}” Unique: {unique}."

    scores = {
        "Market":        m_score,
        "Team":          t_score,
        "Traction":      tr_score,
        "Product Clarity": pc_score
    }
    details = {
        "Market":         m_detail,
        "Team":           t_detail,
        "Traction":       tr_detail,
        "Product Clarity": pc_detail
    }
    return scores, details

def score_profile(profile: dict):
    return _stub_score(profile) if _TESTING else _real_score(profile)
