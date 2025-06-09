import streamlit as st
import json
from agents.extraction import extract_profile
from agents.scoring    import score_profile
from agents.decision   import decide_profile

st.set_page_config(page_title="Untapped Agentic VC Demo", layout="centered")
st.title("Untapped Agentic VC Demo")

# --- Input Section ---
uploaded_file = st.file_uploader("Upload founder submission (JSON)", type=["json"])
use_sample    = st.button("Use Sample Submission")

if uploaded_file:
    data = json.load(uploaded_file)
elif use_sample:
    try:
        with open("data/sample_submission.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        st.error("Sample file not found in data/sample_submission.json")
        st.stop()
else:
    st.info("Please upload a JSON file or click ‘Use Sample Submission’ to proceed.")
    st.stop()

# --- Extraction Step ---
st.header("1. Extraction Results")
profile, extraction_cot = extract_profile(data)
st.json(profile)
with st.expander("Chain of Thought (Extraction)"):
    for step in extraction_cot:
        st.write("•", step)

# --- Scoring Step ---
st.header("2. Scoring Breakdown")
scores, scoring_details = score_profile(profile)
for metric, score in scores.items():
    detail = scoring_details.get(metric, "")
    st.write(f"**{metric}:** {score}")
    if detail:
        st.write(f"_Detail:_ {detail}")

# --- Decision Step ---
st.header("3. Recommendation")
decision, rationale, decision_cot = decide_profile(profile, scores)
st.subheader(decision)
st.write(rationale)
with st.expander("Chain of Thought (Decision)"):
    for step in decision_cot:
        st.write("•", step)

# --- Download Report ---
report = {
    "profile": profile,
    "scores": scores,
    "decision": decision,
    "rationale": rationale
}
st.download_button(
    label="Download Full Report as JSON",
    data=json.dumps(report, indent=2),
    file_name="untapped_vc_report.json",
    mime="application/json"
)
