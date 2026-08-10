# Projects INT 1.0 — one product, six months

## Product mission

All work in this folder contributes to one real-world product: the **Team Management Platform**. Teams rotate monthly, but the product backlog, contracts, design language, environments, test strategy, and release history remain shared.

## Six-month project roadmap

| Month | Product stage | Combined deliverable |
| --- | --- | --- |
| M-01 | Discover | Product brief, personas, journeys, backlog, risks, local setup |
| M-02 | Define foundations | Design system, data model, API contract, test strategy, architecture decision |
| M-03 | Build vertical slice | Authentication plus task flow in development |
| M-04 | Expand features | Teams, roles, task CRUD, search, filters, pagination, notifications |
| M-05 | Harden and stage | CI, automated regression, staging deployment, security, observability, performance |
| M-06 | Release and handoff | Release candidate, final release, runbook, case studies, portfolio demo |

## Track contribution map

| Track | Product responsibility |
| --- | --- |
| UI/UX | Research, flows, screens, components, prototypes, design QA |
| Frontend | Responsive accessible interface and client-side integration |
| Backend | Secure API, data model, business rules, auth, permissions |
| QA | Risk model, test strategy, manual/API/E2E evidence, release recommendation |
| DevOps | CI/CD, packaging, environments, automation, observability |
| Cloud | Runtime architecture, identity, networking, backups, cost, deployment |
| AI/ML | Measured, responsible AI experiment or decision-support feature |
| Pre-sales | Discovery, acceptance criteria, scope, demos, proposals, handoff |

## Monthly folders

- [M-01 — Discovery](./M-01/README.md)
- [M-02 — Foundations](./M-02/README.md)
- [M-03 — Vertical slice](./M-03/README.md)
- [M-04 — Feature delivery](./M-04/README.md)
- [M-05 — Reliability and staging](./M-05/README.md)
- [M-06 — Release and handoff](./M-06/README.md)

Each month contains the four weekly product outcomes from [WEEKLY_WORKPLAN.md](../WEEKLY_WORKPLAN.md). The team’s implementation, design, tests, operations evidence, and case studies should link back to this project index.

## Definition of done for the shared product

The product is ready for the final handoff when a new person can run it from documented instructions, complete a protected login-to-task flow, understand the API and data model, see test evidence for critical paths, deploy to the documented environment, and find the known limitations and rollback steps.
