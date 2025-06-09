# Untapped Agentic VC Demo

This project implements a lightweight prototype of an **Agentic Investment Decision System**, simulating how an automated VC pipeline might operate. It extracts structured profiles from founder submissions, computes rule + LLM-based scores, and generates investment decisions with rationale and transparency.

## 🗂️ Folder Structure

```
.
├── agents/                 # Modular agent scripts (extraction, scoring, decision)
├── data/                   # Sample JSON submissions
├── tests/                  # Unit tests for each agent
├── app.py                  # Streamlit frontend demo
├── pipeline.py             # CLI script to run full pipeline
├── graph.py                # (Optional) Workflow DAG logic
├── requirements.txt        # (Not required for setup)
└── README.md               # You're here!
```

---

## 🚀 How to Run

### 1. Install Dependencies (Without `requirements.txt`)
You can install only what’s needed using pip:

```bash
pip install streamlit transformers torch
```

Optionally, if you're running tests:
```bash
pip install pytest
```

### 2. Run Streamlit App (GUI)
```bash
streamlit run app.py
```
- Upload a custom JSON or use the sample to trigger extraction, scoring, and decision.
- Download the full report after processing.

### 3. Run from CLI (Headless)
```bash
python pipeline.py
```
This runs the same pipeline but prints output to terminal. Useful for debugging or batch processing.

---

## ✅ Features

- Agent-based modular design: `extract → score → decide`
- Rule + LLM hybrid scoring (using Flan-T5 from Hugging Face)
- Chain-of-thought trace for transparency
- Downloadable decision report via UI
- Easily extensible (e.g., plug in vector DB, new agents, admin overrides)

---

## 🔍 Testing

To run tests:

```bash
pytest tests/
```

---

## 📁 Sample Inputs

Use any file from the `/data` directory to simulate startup submissions. Structure should match `sample_submission.json`.

---

## 🤝 Acknowledgments

Developed as part of the **Untapped Ventures AI Technical Analyst Assignment**. Combines agentic design patterns with practical AI engineering for investment decision systems.