# QA engineering track

## Mission

Understand the product, identify risk, test systematically, and communicate evidence clearly. QA is involved from discovery through release; it is not a final button-clicking phase.

## Six-month progression

| Month | Learn and practice | Product deliverable | Validation |
| --- | --- | --- | --- |
| 1 — Quality foundations | SDLC/STLC, Agile, test levels, risk, requirements, bug reports, test design | Product risk map, test charter, login scenarios, bug-report examples | Mentor checks clarity, reproducibility, severity, and priority |
| 2 — Manual and API testing | Equivalence partitions, boundaries, exploratory testing, HTTP, JSON, Postman, SQL basics | Test plan, traceability matrix, Postman collection | Peer executes cases; API collection covers positive and negative paths |
| 3 — Vertical slice confidence | Smoke/regression suites, auth/session risks, accessibility and responsive checks | Vertical-slice test report and release recommendation | Critical path passes; failures have evidence and owner |
| 4 — Feature risk coverage | Teams, roles, tasks, search, filters, pagination, notifications, permissions | Risk-based test suites and regression baseline | Role matrix and edge cases reviewed with backend/frontend |
| 5 — Automation and reliability | Playwright, fixtures, API tests, CI, flaky-test diagnosis, basic performance/security awareness | Automated critical journeys in CI | Stable repeatable runs; failures produce useful artifacts |
| 6 — Release and quality reporting | Release gates, defect trends, incident learning, test metrics, handoff | Final quality report, release checklist, and portfolio case study | Go/no-go recommendation backed by evidence and known risks |

## Weekly practice

- Weeks 1–4: write scenarios, risk questions, and high-quality bug reports.
- Weeks 5–8: test API contracts, data boundaries, permissions, and SQL-backed behavior.
- Weeks 9–12: test and report the first vertical slice across browser and API.
- Weeks 13–16: extend coverage for team, role, task, search, filter, and pagination behavior.
- Weeks 17–20: automate critical paths and run them in CI; remove flaky checks.
- Weeks 21–24: operate the release gate, summarize risk, and present quality evidence.

## Required outputs

1. Risk-based test strategy.
2. Traceability matrix from requirement to test evidence.
3. Manual test cases and exploratory charters.
4. Postman collection with environment documentation.
5. Bug reports with steps, expected/actual results, severity, and evidence.
6. SQL checks for important data behavior.
7. Playwright API/browser checks in CI.
8. Final quality report and release recommendation.

## QA quality gate

- Test cases state preconditions, data, steps, expected results, and cleanup.
- Severity describes impact; priority describes order of work.
- Tests cover valid, invalid, boundary, permission, empty, loading, timeout, and recovery behavior.
- Automation asserts user or API outcomes rather than implementation details.
- Test data is isolated and repeatable.
- A failed test includes enough logs, screenshots, traces, or request data to diagnose it.
- A release recommendation states what was tested, what was not, and the remaining risk.

## Validated free resources

- [QA roadmap](https://roadmap.sh/qa)
- [Postman Learning Center](https://learning.postman.com/)
- [Playwright API testing](https://playwright.dev/docs/api-testing)
- [Webdriver University](https://webdriveruniversity.com/) for practice
- [Test Automation University](https://testautomationu.applitools.com/)
- [Introduction to Software Testing or Software QA](https://www.udemy.com/course/introduction-to-software-testing-or-software-qa/) — free when validated
- [Postman YouTube](https://www.youtube.com/@postman)

See the [central resource catalog](../RESOURCE_CATALOG.md) for current links and fallback resources.

## Final assessment

Give a release-readiness briefing: summarize critical risks, show the evidence, explain one defect that changed the product, and make a justified ship/no-ship recommendation.
