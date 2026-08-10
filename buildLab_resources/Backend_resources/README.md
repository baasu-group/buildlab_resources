# Backend engineering track

## Mission

Build a secure, documented, testable backend for the Team Management Platform. Backend work includes data modeling, APIs, authentication, authorization, validation, error handling, performance, and maintainability—not just endpoint creation.

## Recommended stack

Python, Django, Django REST Framework, PostgreSQL, pytest/Django tests, Git, Docker, and OpenAPI-compatible API documentation.

## Six-month progression

| Month | Learn and practice | Product deliverable | Validation |
| --- | --- | --- | --- |
| 1 — Python and web basics | Python syntax, functions, modules, exceptions, HTTP, Git, virtual environments | Small CLI/data-processing project and local Django hello-world app | Tests for normal and invalid input; explain request/response basics |
| 2 — Data and Django | Models, migrations, relationships, SQL, admin, serializers, views, URLs | User/team/task schema and first CRUD API | Schema review, migration test, representative API examples |
| 3 — Secure vertical slice | Authentication, permissions, validation, status codes, pagination, filtering | Login plus task API consumed by the frontend | API contract review, negative tests, permission matrix, documented errors |
| 4 — Business features | Role-based access, assignments, notifications, transactions, query optimization | Team, role, task, search, filter, and pagination endpoints | Unit/API tests, query review, authorization tests for every role |
| 5 — Reliability | Logging, configuration, secrets, security headers, rate limits, background work, performance | Staging-ready API with health checks and observability | Failure drill, basic load/risk test, security checklist, rollback notes |
| 6 — Release and handoff | Deployment, API versioning, OpenAPI, runbooks, maintenance, portfolio explanation | Release candidate and backend case study | Reproducible setup, release demo, API documentation, known issues |

## Weekly practice

- Weeks 1–4: write Python exercises and a small testable CLI.
- Weeks 5–8: model the domain and expose simple CRUD endpoints.
- Weeks 9–12: implement the first secure vertical slice with API documentation.
- Weeks 13–16: add roles, task behavior, filters, pagination, and notifications.
- Weeks 17–20: improve observability, security, performance, and deployment readiness.
- Weeks 21–24: stabilize, release, document, and present the backend.

## Required outputs

1. Python practice project with tests.
2. Entity relationship diagram and migration history.
3. REST API contract and example requests.
4. Authentication and permission matrix.
5. Validated CRUD endpoints with useful errors.
6. Unit and integration/API tests.
7. Health check, structured logs, and configuration guide.
8. API documentation, release notes, and case study.

## Backend quality gate

- Every endpoint has an owner, purpose, request shape, response shape, and error behavior.
- Authentication and authorization are separate concepts and are tested separately.
- Validation rejects invalid data without exposing internal details.
- Database constraints protect important invariants.
- List endpoints define pagination, filtering, ordering, and maximum page size.
- Secrets are loaded from environment/configuration, never committed.
- Tests cover permissions, invalid input, not-found behavior, and important business rules.
- Logs are useful without leaking passwords, tokens, or private data.

## Validated free resources

- [Backend roadmap](https://roadmap.sh/backend) and [Django roadmap](https://roadmap.sh/django)
- [Django tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django REST Framework quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [freeCodeCamp YouTube](https://www.youtube.com/@freecodecamp) for Python, SQL, and API videos
- [Python for Absolute Beginners](https://www.udemy.com/course/free-python/) — free when validated; prerequisite only
- [Django REST Framework course](https://www.udemy.com/course/django-rest-framework/) — optional; check price before enrollment

See the [central resource catalog](../RESOURCE_CATALOG.md) for the source-validation policy.

## Final assessment

A reviewer should be able to run the API, inspect the schema, authenticate as different roles, reproduce documented requests, and understand why the main data and permission decisions were made.
