# DevOps and platform track

## Mission

Make delivery repeatable, safe, observable, and collaborative. DevOps is a team practice: developers, QA, cloud, and product people all contribute to reliable delivery.

## Six-month progression

| Month | Learn and practice | Product deliverable | Validation |
| --- | --- | --- | --- |
| 1 — Delivery foundations | Linux shell, Git workflows, environments, processes, networking basics | Local developer setup and runbook | A new teammate can start the project using the guide |
| 2 — Containers and quality | Docker images, Compose, environment variables, lint/format/test commands | Local multi-service stack and quality scripts | Clean rebuild from scratch; no secrets in image or repo |
| 3 — CI vertical slice | GitHub Actions, pull-request checks, artifacts, branch protection concepts | CI pipeline for frontend/backend/QA checks | Intentional failing commit produces useful feedback |
| 4 — Deployment | Staging workflow, deployment strategies, migrations, backups, rollback | Repeatable staging deployment | Deployment rehearsal and rollback exercise |
| 5 — Operations | Logs, metrics, health checks, alerts, security scanning, cost awareness | Basic observability and incident runbook | Simulated outage with timeline and recovery steps |
| 6 — Release engineering | Release automation, change management, documentation, handoff | Release pipeline, runbook, post-release review | Final release is repeatable by another person |

## Required outputs

- Local setup and troubleshooting guide.
- Dockerfile/Compose configuration with documented decisions.
- CI workflow for lint, tests, and build artifacts.
- Staging deployment procedure and rollback plan.
- Health checks, structured logs, and a basic dashboard/alert plan.
- Security and cost checklist.
- Incident report and final release runbook.

## Quality gate

- Builds are reproducible from a clean checkout.
- Environment-specific values are configured outside source control.
- CI fails fast on formatting, linting, tests, or build errors.
- Deployment has a rollback or forward-fix plan.
- Every service exposes a useful health signal.
- Logs include correlation context and exclude secrets.
- The team can answer who owns a failure and how to recover.

## Validated free resources

- [DevOps roadmap](https://roadmap.sh/devops)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [TechWorld with Nana](https://www.youtube.com/@TechWorldwithNana)
- [AWS Developers](https://www.youtube.com/@amazonwebservices)
- [DevOps for Beginners](https://www.udemy.com/course/devops-for-beginners-github-docker-cicd-from-scratch/) — free when validated

See the [central resource catalog](../RESOURCE_CATALOG.md) for current options.

## Final assessment

Run a deployment in front of a reviewer, deliberately cause one recoverable failure, and explain the evidence used to detect and recover from it.
