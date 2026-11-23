# Engineering Decisions — Vivek AI Portfolio Twin

This document records important technical decisions, their rationale, alternatives, and implementation status.

Decisions are provisional until validated through implementation and testing.

---

## ED-001: Modular Application Architecture

**Status:** Proposed

**Decision:** Use separate modules for the UI, API, AI provider, conversation management, RAG, integrations, and database.

**Reasoning:**
- Improves maintainability.
- Separates responsibilities.
- Makes individual components easier to test.
- Allows components to evolve independently.

**Alternative considered:** A single Python application containing all logic.

**Trade-off:** More initial organization and module boundaries, but better long-term maintainability.

---

## ED-002: Gradio as the Initial Frontend

**Status:** Proposed

**Decision:** Use Gradio to build the initial chat interface.

**Reasoning:**
- Rapid prototyping.
- Native Python integration.
- Less frontend development overhead.
- Suitable for demonstrating an AI application.

**Alternative considered:** React with a custom frontend.

**Trade-off:** Faster initial development, but less UI flexibility. A custom frontend can be introduced later.

---

## ED-003: FastAPI as an Independent Backend

**Status:** Proposed

**Decision:** Use FastAPI for backend APIs and application orchestration.

**Reasoning:**
- Clear API boundaries.
- Pydantic-based validation.
- Support for asynchronous operations.
- Easier integration with future frontend clients.
- Good testing and documentation support.

**Alternative considered:** Implementing all backend logic directly inside Gradio.

**Trade-off:** Additional development complexity, but stronger separation between UI and backend.

---

## ED-004: Provider-Independent AI Integration

**Status:** Proposed

**Decision:** Create a common interface for LLM providers.

**Reasoning:**
- Avoid locking the application into one provider.
- Compare models using consistent evaluation tasks.
- Make future provider changes easier.
- Keep business logic independent of provider-specific SDKs.

**Alternatives considered:** Directly integrating one provider throughout the application.

**Trade-off:** Requires an abstraction layer and some additional implementation effort.

**Provider selection criteria:**
- Response quality.
- Latency.
- Cost.
- Tool-calling reliability.
- Privacy and data retention policies.

The final provider has not yet been selected.

---

## ED-005: Implement a Real RAG Pipeline

**Status:** Proposed

**Decision:** Build an actual document ingestion, embedding, retrieval, and generation pipeline.

**Reasoning:**
- Answers should be grounded in verified professional information.
- Knowledge should be updateable without rewriting prompts.
- Relevant sources should be retrievable and traceable.
- Retrieval quality should be measurable.

**Alternatives considered:**
- Hardcoding all profile information into a system prompt.
- Using a simple keyword search.

**Trade-off:** More implementation and evaluation work, but better knowledge management and source grounding.

---

## ED-006: PostgreSQL with pgvector

**Status:** Proposed

**Decision:** Use PostgreSQL as the primary database and pgvector for vector storage and similarity search.

**Reasoning:**
- Relational and vector data can coexist.
- Supports persistent storage.
- Reduces the need for a separate vector database initially.
- Provides SQL-based data management.

**Alternative considered:** Using a separate vector database such as FAISS or ChromaDB.

**Trade-off:** Requires PostgreSQL setup and management, but simplifies the initial production architecture.

---

## ED-007: Backend-Controlled Lead Capture

**Status:** Proposed

**Decision:** Let the AI identify lead intent, but let backend services validate, store, and notify.

**Reasoning:**
- LLM-generated text is not a reliable authorization mechanism.
- Contact information requires validation.
- Database persistence must be verified.
- Notifications should only follow successful lead storage.

**Alternative considered:** Allowing the model to declare that a lead has been captured.

**Trade-off:** Additional backend logic, but substantially better reliability and control.

---

## ED-008: Telegram for Lead Notifications

**Status:** Proposed

**Decision:** Use the Telegram Bot API for private lead notifications.

**Reasoning:**
- Suitable for lightweight notifications.
- Can be integrated using HTTP requests.
- Avoids building a separate notification dashboard initially.

**Alternative considered:** Discord or WhatsApp integration.

**Trade-off:** Requires bot configuration and secure token management.

---

## ED-009: Evaluate Before Optimizing

**Status:** Proposed

**Decision:** Maintain a repeatable evaluation dataset and compare alternatives using measurable results.

**Reasoning:**
- Avoid choosing models based only on popularity.
- Measure retrieval quality and answer groundedness.
- Track latency and token usage.
- Make technical improvements evidence-based.

**Planned evaluation metrics:**
- Precision and recall.
- Mean Reciprocal Rank.
- Answer relevance.
- Groundedness.
- Citation correctness.
- Hallucination rate.
- Latency and token consumption.

---

## ED-010: Incremental Development

**Status:** Active development principle

**Decision:** Build a functional MVP before adding advanced features.

**Reasoning:**
- Reduces unnecessary complexity.
- Produces demonstrable progress early.
- Makes debugging easier.
- Allows design assumptions to be validated.

**Trade-off:** Some advanced features will be postponed, but the initial product becomes usable sooner.

---

## Decision Update Policy

For every major engineering decision:

1. Record the problem.
2. Identify possible alternatives.
3. Explain the selected approach.
4. Document the trade-offs.
5. Test the implementation.
6. Update the decision status based on evidence.

Do not describe a proposed decision as implemented or experimentally validated until it actually is.
