# Agentic Investment Decision Prototype

A lightweight public prototype illustrating an agent-based workflow for turning heterogeneous founder submissions into structured investment evaluations.

This repository is **not the full production system or proprietary internal code** from Untapped Ventures. It is a compact public implementation of the core workflow patterns: extraction, scoring, decision generation, and reviewable rationale.

## Problem

Early-stage investment review often requires combining information scattered across pitch decks, founder submissions, and structured application fields. The challenge is not simply text classification; the system has to normalize heterogeneous evidence, apply stage-specific evaluation criteria, and produce a decision that can still be inspected by a human analyst.

## Workflow

```text
Founder submission
      |
      v
Data extraction
      |
      v
Structured scoring
      |
      v
Decision agent
      |
      v
Reviewable recommendation
```

The repository separates these responsibilities into modular agents so that extraction, scoring, and decision logic can be tested independently.

## Core components

- **Extraction agent** - converts incoming submission data into a structured startup profile.
- **Scoring agent** - evaluates the profile against defined criteria using a hybrid rule + language-model workflow.
- **Decision agent** - converts the structured profile and scores into a recommendation with supporting rationale.
- **Pipeline runner** - executes the end-to-end workflow from the command line.
- **Streamlit demo** - provides a simple interface for uploading an input and reviewing the resulting report.
- **Tests** - exercise the individual agent components.

## Repository structure

```text
.
├── agents/                 # Extraction, scoring, and decision modules
├── data/                   # Sample founder submissions
├── tests/                  # Unit tests
├── app.py                  # Streamlit demo
├── pipeline.py             # End-to-end CLI pipeline
├── graph.py                # Workflow / system diagram definition
├── requirements.txt
└── README.md
```

## Running the prototype

Install the dependencies:

```bash
pip install streamlit transformers torch pytest
```

Run the Streamlit interface:

```bash
streamlit run app.py
```

or execute the pipeline directly:

```bash
python pipeline.py
```

## What this repo demonstrates

The value of this project for my broader work is the **decision pipeline**, not the investment domain itself. It required coordinating multiple model-assisted stages over heterogeneous evidence while preserving structured outputs and a human-reviewable rationale.

The production work at Untapped Ventures extended these ideas to richer founder materials, stage-specific evaluation workflows, confidence-based routing, and operational review processes.

## Background

Developed from work associated with my **AI Research Analyst** experience at Untapped Ventures.
