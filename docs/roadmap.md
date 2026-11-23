# Vivek AI Portfolio Twin — Project Roadmap

## 1. Project Vision

Build an AI-powered professional portfolio assistant that represents Vivek's technical background, projects, skills, and professional interests.

The assistant will help recruiters and potential freelance clients explore his work, ask technical questions, understand his experience, and initiate professional contact.

It will identify itself as an AI assistant rather than pretending to be Vivek.

## 2. Primary Objectives

- Build a functional AI-powered portfolio assistant.
- Implement Retrieval-Augmented Generation (RAG).
- Provide accurate, source-grounded answers about projects and skills.
- Integrate GitHub to retrieve public project information.
- Implement isolated conversational memory.
- Capture genuine professional leads with user consent.
- Send lead notifications through Telegram.
- Deploy an accessible web application.
- Evaluate answer quality, retrieval performance, and reliability.

## 3. Target Users

1. Recruiters evaluating technical skills and projects.
2. Freelance clients exploring potential collaboration.
3. Developers and visitors interested in the projects.

## 4. Planned Technology Stack

| Component | Planned technology |
|---|---|
| Programming language | Python |
| Initial UI | Gradio |
| Backend API | FastAPI |
| Data validation | Pydantic |
| LLM | Provider selected after evaluation |
| Embeddings | Sentence Transformers or evaluated alternative |
| Database | PostgreSQL |
| Vector search | pgvector |
| Notifications | Telegram Bot API |
| Version control | Git and GitHub |
| Testing | pytest |
| Deployment | Hugging Face Spaces initially |
| Containerization | Docker |
| CI/CD | GitHub Actions |

Technology choices may change when experiments demonstrate a better alternative.

## 5. Development Roadmap

### Phase 1 — Project Foundation

- [x] Create public GitHub repository.
- [x] Clone repository locally.
- [x] Open project in VS Code.
- [x] Create documentation structure.
- [x] Document system architecture.
- [x] Document engineering decisions.
- [x] Document experiment strategy.
- [x] Document interview stories.
- [x] Document deployment strategy.
- [x] Establish initial application structure.
- [x] Configure Python environment and dependencies.
- [x] Implement initial health check.
### Phase 2 — Core Application

- [ ] Build Gradio chat interface.
- [ ] Implement FastAPI backend.
- [ ] Create modular AI provider interface.
- [ ] Integrate selected LLM provider.
- [ ] Implement prompt management.
- [ ] Add conversation history.
- [ ] Add input validation and error handling.

### Phase 3 — Knowledge and RAG

- [ ] Prepare profile, skills, experience, and project documents.
- [ ] Implement document ingestion.
- [ ] Implement text extraction and cleaning.
- [ ] Implement chunking and metadata.
- [ ] Generate embeddings.
- [ ] Configure PostgreSQL and pgvector.
- [ ] Implement semantic retrieval.
- [ ] Add source-grounded responses and citations.
- [ ] Evaluate retrieval quality and answer groundedness.

### Phase 4 — Intelligence and Integrations

- [ ] Implement isolated conversational memory.
- [ ] Integrate GitHub API.
- [ ] Retrieve and display public repositories.
- [ ] Implement professional lead detection.
- [ ] Validate lead information.
- [ ] Persist leads in the database.
- [ ] Integrate Telegram notifications.
- [ ] Add rate limiting and abuse protection.

### Phase 5 — Testing and Reliability

- [ ] Write unit tests.
- [ ] Write API integration tests.
- [ ] Test memory isolation.
- [ ] Test lead capture and duplicate handling.
- [ ] Evaluate hallucination and citation accuracy.
- [ ] Measure latency and token usage.
- [ ] Test failure and recovery scenarios.
- [ ] Document engineering experiments.

### Phase 6 — Deployment and Presentation

- [ ] Configure production environment variables.
- [ ] Prepare Docker configuration.
- [ ] Deploy the application.
- [ ] Configure persistent database storage.
- [ ] Add logging and basic monitoring.
- [ ] Test deployed application.
- [ ] Prepare project documentation.
- [ ] Create portfolio demonstration.

## 6. Engineering Principles

- Prefer modular, maintainable architecture.
- Keep the AI provider independent of application logic.
- Never trust LLM-generated text as authorization for external actions.
- Validate user inputs on the backend.
- Keep visitor conversations isolated.
- Never expose API keys or private information.
- Ground professional claims in verified project information.
- Measure performance rather than assuming improvements.
- Avoid unnecessary frameworks and infrastructure.
- Document important engineering decisions and trade-offs.

## 7. Evaluation Metrics

The following metrics will be considered during testing:

- Retrieval precision and recall.
- Mean Reciprocal Rank (MRR).
- Answer relevance.
- Answer groundedness.
- Citation correctness.
- Hallucination rate.
- Response latency.
- Token consumption and estimated cost.
- Lead capture success rate.

Actual results will be recorded in `docs/experiments.md`.

## 8. Future Enhancements

These are not part of the initial MVP:

- Custom React frontend.
- Voice-based interaction.
- Advanced agent workflows.
- Job opportunity discovery.
- Freelance opportunity assistance.
- Human-approved outreach generation.
- More advanced observability and analytics.

## 9. Project Status

**Current stage:** Project foundation.

**Completed:** GitHub repository setup, local clone, VS