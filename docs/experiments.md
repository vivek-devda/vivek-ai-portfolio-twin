# Experiments — Vivek AI Portfolio Twin

This document records experiments performed during development.

Only actual experiments with observed results should be marked completed.

---

## Experiment Status

| Status | Meaning |
|---|---|
| Planned | Experiment is proposed but not started |
| In Progress | Experiment is being conducted |
| Completed | Experiment has been executed and results recorded |
| Rejected | Approach was tested and not selected |

---

## EXP-001: LLM Provider Comparison

**Status:** Planned

**Objective:** Identify a suitable LLM provider for the portfolio assistant.

**Candidates:** Gemini, OpenAI, and Anthropic.

**Evaluation criteria:**
- Answer quality.
- Instruction following.
- Tool-calling reliability.
- Response latency.
- Token consumption and cost.
- Privacy and data retention policies.

**Methodology:**

Use the same set of professional portfolio questions across candidate models.

**Results:** Pending.

**Conclusion:** Pending.

---

## EXP-002: Embedding Model Comparison

**Status:** Planned

**Objective:** Identify an embedding model suitable for retrieving relevant professional knowledge.

**Candidates:** To be selected during implementation.

**Evaluation criteria:**
- Retrieval precision.
- Retrieval recall.
- Mean Reciprocal Rank (MRR).
- Semantic relevance.
- Embedding generation latency.
- Computational cost.

**Methodology:**

Use the same knowledge documents and evaluation queries for each candidate model.

**Results:** Pending.

**Conclusion:** Pending.

---

## EXP-003: Document Chunking Strategy

**Status:** Planned

**Objective:** Determine how document chunk size and overlap affect retrieval quality.

**Variables:**
- Chunk size.
- Chunk overlap.
- Document structure.
- Metadata preservation.

**Evaluation criteria:**
- Retrieval relevance.
- Context completeness.
- Precision and recall.
- Answer groundedness.

**Methodology:**

Compare multiple chunking configurations using an identical evaluation dataset.

**Results:** Pending.

**Conclusion:** Pending.

---

## EXP-004: Retrieval Strategy Comparison

**Status:** Planned

**Objective:** Compare retrieval approaches for professional knowledge.

**Candidates:**
- Semantic vector search.
- Keyword search.
- Hybrid retrieval.

**Evaluation criteria:**
- Retrieval precision and recall.
- MRR.
- Retrieval latency.
- Relevance of retrieved context.

**Results:** Pending.

**Conclusion:** Pending.

---

## EXP-005: RAG Answer Quality Evaluation

**Status:** Planned

**Objective:** Measure whether the assistant generates accurate, grounded answers using retrieved knowledge.

**Evaluation criteria:**
- Answer relevance.
- Groundedness.
- Hallucination rate.
- Citation correctness.
- Completeness.

**Methodology:**

Create a dataset of questions with expected answers and supporting source documents. Evaluate model responses against those references.

**Results:** Pending.

**Conclusion:** Pending.

---

## Experiment Recording Template

Use this template for future experiments.

### Experiment ID and Name

**Status:**

**Objective:**

**Hypothesis:**

**Configuration:**

**Dataset:**

**Methodology:**

**Metrics:**

**Observed Results:**

**Limitations:**

**Conclusion:**

**Engineering Decision:**

---

## Important Rules

1. Record actual measurements, not estimates presented as results.
2. Keep experimental conditions consistent when comparing alternatives.
3. Record failed experiments as well as successful ones.
4. Do not claim performance improvements without measurements.
5. Link important findings to engineering decisions.
6. Preserve enough detail to reproduce an experiment.

*This document is initially a plan. No experiments have been conducted yet.*