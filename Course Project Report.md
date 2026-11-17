# Meeting Organizer Agent

## Course Project Report

**Course:** Agentic AI Systems  
**School:** School of Computer Science and Engineering, KLE Technological University  
**Report date:** 17 November 2026  
**Submission deadline:** 19 November 2026  
**Repository:** https://github.com/aniiiket08/meeting-workflow-engine

## 1. Project Summary

Meeting Organizer Agent is a full-stack system for coordinating the lifecycle of a meeting. It proposes times, books an available room or meeting link, prepares an agenda using prior meeting context, processes transcripts into draft minutes, tracks approved actions, and supports distribution and reminders. A person reviews the agenda and minutes at explicit approval points before the workflow continues.

The project is intended to reduce repetitive coordination work while keeping scheduling decisions, extracted meeting records, and outbound communication reviewable. It combines a web interface, a FastAPI backend, a LangGraph workflow, a relational database, and a Model Context Protocol (MCP) tool server.

## 2. Problem and Objectives

Meeting coordination spans calendars, facilities, agendas, transcripts, decisions, action items, and follow-up. When these tasks are handled in separate tools, conflicts and unassigned actions can be missed. This project addresses that coordination gap with a traceable workflow.

The main objectives are to:

- rank available meeting slots and explain the ranking;
- match room capacity and equipment while preventing double booking;
- prepare time-boxed agendas using open actions and previous meeting context;
- generate transcript-grounded minutes and action candidates;
- pause for human approval before agendas and minutes move forward;
- assign and monitor action items, deadlines, and reminders; and
- retain workflow traces and evaluation evidence for review.

## 3. System Design

The application separates the user interface, API, orchestration, tools, and data. The React and Vite frontend calls the FastAPI routes. The backend authenticates the user and starts or resumes workflow work. LangGraph carries the meeting state through agent nodes and approval gates. MCP exposes calendar, room, and Zoom capabilities through structured tools. SQLAlchemy and Alembic manage persistent records; local development can use SQLite, while Docker Compose configures a local PostgreSQL service.

### Meeting workflow

| Stage | Purpose |
|---|---|
| Scheduling | Find and rank candidate times using attendee availability and slot scoring. |
| Room booking | Select an appropriate room or meeting link and reject conflicts. |
| Agenda | Draft a structured agenda using meeting context and prior records. |
| Agenda approval | Pause until an authorized user approves or requests changes. |
| Minutes | Process a transcript into a summary, decisions, and action candidates. |
| Minutes approval | Pause until an authorized user reviews and approves the draft. |
| Action tracking | Create or update assigned actions with owners, dates, and status. |
| Distribution | Prepare approved outputs for distribution and record delivery attempts. |
| Reminders | Check open or overdue actions and apply follow-up rules. |

The graph and API are designed to persist state across approval pauses. Long-running operations use database-backed jobs so a request can return a job identifier while the worker handles transcript processing, LLM calls, or document generation.

## 4. Agents, Tools, and Memory

The agent modules cover scheduling, room booking, agenda preparation, minutes generation, action tracking, distribution, follow-up, and reminders. The graph passes shared state between stages and records agent runs for inspection.

MCP tools provide scoped interfaces for calendar, room, and Zoom operations. Tool inputs are validated and the server returns structured results. Room booking checks for overlapping reservations. Scheduling uses a mock calendar dataset for local development; external integrations require credentials and configuration.

Meeting memory retrieves relevant prior records to inform agendas and memory-chat answers. The repository includes a BM25-style retrieval implementation and seed meeting data. Retrieval is used as context; answers should remain tied to the retrieved records rather than presenting unsupported information as a stored decision.

## 5. Human Review, Security, and Reliability

The workflow includes approval gates before an agenda is accepted and before minutes are approved for downstream use. Role-based access control distinguishes administrative, approver, staff, and guest capabilities.

Transcript processing includes PII scrubbing before external model calls. Extracted decisions and actions are checked against source transcript text; unsupported quotes are dropped and logged. This makes source evidence visible for review, although it does not guarantee that every semantic interpretation is correct.

Distribution and reminders use idempotency keys to reduce duplicate actions during retries. Email delivery is disabled until valid SMTP settings are configured. The application uses environment-based configuration for credentials and security keys; the source snapshot includes a template file rather than local credentials.

## 6. Evaluation Evidence

The repository contains unit tests, API and workflow benchmarks, memory and MCP evaluations, frontend build evidence, and load-test records. The results below are reported from the existing project evaluation files; they were not rerun while preparing this submission.

| Area | Recorded result | Interpretation |
|---|---|---|
| Backend suite | 194 passed, 1 skipped in the final local verification recorded by the evaluation report. | The skipped sample regression depends on transcript and gold-data fixtures that are absent. |
| Frontend build | Production build passed in the recorded verification. | This is local build evidence, not a deployment check. |
| Full 10-meeting extraction benchmark | Actions: precision 0.4286, recall 0.8571, F1 0.5714. Decisions: precision 0.3333, recall 1.0000, F1 0.5000. | The complete benchmark did not meet the configured quality target. The false positives are documented for follow-up. |
| Follow-up benchmark after precision changes | 9 of 10 meetings completed; the remaining case returned a Gemini HTTP 503. The completed subset scored 1.0000 for action and decision precision, recall, and F1. | This is a partial result and must not be presented as a complete 10-meeting score. |
| Load profile | The saved evaluation record reports 306 requests at 20 users with zero errors over the measured run. | This is local load-test evidence; no hosted performance was measured. |

The benchmark indicates that reducing false positives and improving external model availability remain important. In particular, the incomplete second run cannot replace a successful full-set evaluation.

## 7. Limitations and Future Work

No hosted deployment or production environment was verified in the available project record. Real calendar, Zoom, and email operations depend on provider credentials and configuration. The sample transcript and gold-data files required for one regression case are not present, so that case remains skipped. The complete live-model benchmark has shown both false positives and a provider-side 503 response.

The next steps are to add the missing regression fixtures, repeat the full benchmark with stable provider availability, review false-positive examples, and verify the worker and persistent-storage configuration in the intended deployment environment. External actions should continue to require explicit human approval where policy calls for it.

## 8. Running the Project

The source-code snapshot includes a README, dependency declarations, Docker configuration, backend, frontend, migration files, and evaluation scripts. For local setup:

1. Install Docker and Docker Compose, or install the Python and Node versions declared by the project.
2. Copy `.env.example` to `.env` and configure only the credentials required for the feature being exercised.
3. Start the services with `docker compose up --build`, or follow the backend and frontend run instructions in the project README.
4. Use the seeded local data and mock calendar for a credential-free workflow demonstration.
5. Run the relevant backend or evaluation commands documented in `evaluation/README.md` after installing the dependencies.

Email, Zoom, and external calendar features remain unavailable until their credentials are supplied and the corresponding integrations are configured.

## 9. Project References

Project basis: README.md, the PRD and architecture documents, evaluation_report.md, and test_results.md.
