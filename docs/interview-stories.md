# Engineering Interview Stories — Vivek AI Portfolio Twin

This document tracks technical experiences that can later be explained in interviews.

Important: Planned work must never be presented as completed experience. Update stories as implementation and testing happen.

---

## 1. Project Overview

**Project:** Vivek AI Portfolio Twin

**Category:** AI Application Engineering / Backend Engineering

**Objective:**

Build an AI-powered professional portfolio assistant that uses LLMs, retrieval-augmented generation, conversational memory, external integrations, and persistent storage.

**Current status:** Project foundation and documentation completed. Application implementation has not started.

---

## 2. Engineering Stories

### Story 001 — Designing a Modular AI Application

**Problem:**

A portfolio assistant needs multiple independent capabilities, including AI generation, knowledge retrieval, conversation management, external integrations, and data persistence.

**Approach:**

Design separate modules with clearly defined responsibilities and an independent backend API.

**Technical concepts:**
- Separation of concerns.
- Modular architecture.
- API boundaries.
- Maintainability.

**Implementation evidence:** Pending.

**Interview talking point:** Explain how modular architecture reduces coupling and makes individual components easier to test and replace.

### Story 002 — Selecting an AI Provider

**Problem:**

Different LLM providers have different response quality, latency, pricing, and privacy characteristics.

**Approach:**

Design a provider-independent interface and compare candidate models using consistent evaluation questions.

**Technical concepts:**
- Abstraction.
- Provider integration.
- Model evaluation.
- Cost optimization.

**Implementation evidence:** Pending.

**Interview talking point:** Explain why provider abstraction is useful and how you would compare models fairly.

### Story 003 — Implementing RAG

**Problem:**

An LLM alone may produce inaccurate information about a developer's projects and experience.

**Approach:**

Build a retrieval pipeline that retrieves relevant information from verified documents before generating an answer.

**Technical concepts:**
- Embeddings.
- Chunking.
- Vector search.
- PostgreSQL.
- pgvector.
- Grounded generation.

**Implementation evidence:** Pending.

**Interview talking point:** Explain the complete lifecycle of a document through ingestion, embedding, retrieval, and generation.

### Story 004 — Designing Reliable Lead Capture

**Problem:**

LLM-generated messages cannot guarantee that contact information has actually been validated or stored.

**Approach:**

Keep lead validation, database persistence, and notifications under backend control.

**Technical concepts:**
- Input validation.
- Database transactions.
- API integration.
- Error handling.
- Idempotency.

**Implementation evidence:** Pending.

**Interview talking point:** Explain why an AI-generated confirmation is not equivalent to a successful database operation.

### Story 005 — Evaluating Retrieval Quality

**Problem:**

A RAG system can retrieve irrelevant or incomplete context even when its responses sound convincing.

**Approach:**

Create an evaluation dataset and compare retrieval configurations using measurable metrics.

**Technical concepts:**
- Precision.
- Recall.
- Mean Reciprocal Rank.
- Groundedness.
- Evaluation datasets.

**Implementation evidence:** Pending.

**Interview talking point:** Explain how you would measure whether a retrieval system is improving.

---

## 3. Technical Concepts to Master

- Python modular programming.
- REST APIs and HTTP.
- FastAPI and Pydantic.
- SQL and PostgreSQL.
- Database transactions.
- Embeddings and vector similarity.
- RAG architecture.
- LLM prompting and structured outputs.
- Token management.
- Async programming.
- API security.
- Testing with pytest.
- Docker and deployment.
- Logging and monitoring.

---

## 4. Interview Evidence Tracker

For every completed feature, record:

| Evidence | What to document |
|---|---|
| Implementation | What was built |
| Technical reasoning | Why this approach was selected |
| Alternatives | What else was considered |
| Testing | How correctness was verified |
| Metrics | Actual measured results |
| Failure handling | What happens when something goes wrong |
| Trade-offs | What was gained and sacrificed |

---

## 5. Personal Interview Rule

Never memorize impressive-sounding explanations without understanding the implementation.

Be prepared to explain:
1. What problem the feature solves.
2. How the implementation works.
3. Why the technology was selected.
4. What alternatives were considered.
5. What limitations remain.
6. What you would improve next.

*The strongest interview stories will come from real implementation experience, measurable results, and lessons learned.*