# BuildLab six-month internship guide

## Program outcome

By the end of six months, each intern should be able to contribute safely to a real product team, explain their decisions, show a portfolio of evidence, and complete one meaningful release of the Team Management Platform.

This is a shared product program, not eight isolated courses. Each specialist owns a track but works from the same requirements, backlog, environments, design language, and release plan.

## Six-month calendar

| Month | Shared theme | Product milestone | Evidence required |
| --- | --- | --- | --- |
| 1 | Foundations and discovery | Product brief, personas, user journeys, repo conventions, local development setup | Baseline assessment, glossary, first small exercise, working local setup |
| 2 | Core skills and design system | Approved information architecture, design tokens, database model, API contract, test strategy | Design review, schema/endpoint review, test plan, first pull request |
| 3 | Vertical slice | Login plus one complete task flow works end to end in a development environment | Demo, API documentation, automated smoke tests, accessibility notes |
| 4 | Feature delivery | Teams, roles, task management, search/filtering, and responsive states | Two reviewed features per team, regression suite, changelog |
| 5 | Reliability and release readiness | Staging environment with CI, security checks, observability, and production-like data | Risk report, deployment rehearsal, incident exercise, rollback plan |
| 6 | Ship and present | Release candidate, final release, portfolio case study, and technical/product demo | Release notes, runbook, demo recording, individual reflection, final review |

## Weekly rhythm

1. **Learn:** complete one focused lesson, roadmap section, or documentation chapter.
2. **Practice:** solve a small exercise without copying the tutorial solution.
3. **Apply:** make a small change to the shared product or its project artifacts.
4. **Review:** open a pull request or design review and request specific feedback.
5. **Reflect:** record what was learned, what failed, and what will change next week.

Recommended weekly allocation: 3 hours guided learning, 2 hours practice, 4–5 hours product work, and 1–2 hours review/documentation.

## Weeks 1–24

| Week | Cross-functional focus | Definition of done |
| ---: | --- | --- |
| 1 | Orientation, tools, Git/GitHub, product problem | Local tools work; each intern can clone, branch, commit, and open a draft review |
| 2 | Users, stakeholders, accessibility, and success metrics | Shared product brief, personas, assumptions, and risks |
| 3 | User journeys and information architecture | Login and task-management journeys reviewed by the whole team |
| 4 | First discipline exercise | One small, independently completed artifact per intern |
| 5 | Design tokens, coding standards, and test language | Shared conventions documented and accepted |
| 6 | Data model, API contract, wireframes, and test plan | Design/API/schema/test reviews complete |
| 7 | Implementation foundations | App shell, project structure, seed data, and first automated check |
| 8 | Authentication flow | Login/logout/protected-route design and implementation plan ready |
| 9 | Vertical slice build | One user can complete a narrow task flow end to end |
| 10 | Vertical slice test and accessibility | Happy path, failure paths, keyboard path, and API checks pass |
| 11 | Vertical slice review | Feedback addressed; demo can be repeated by another intern |
| 12 | Month-three checkpoint | Release a development milestone and document lessons learned |
| 13 | Team and role management | Role behavior is visible in UI, API, and tests |
| 14 | Task creation and assignment | Validated task form and API with useful errors |
| 15 | Status, priority, search, filter, pagination | State transitions and edge cases covered |
| 16 | Notifications and responsive states | Loading, empty, error, success, and mobile states are reviewed |
| 17 | CI and code quality | Every change runs format/lint/unit checks automatically |
| 18 | Integration and regression | Critical user journeys have regression coverage |
| 19 | Deployment rehearsal | Staging deployment is repeatable from documented steps |
| 20 | Security and observability | Secrets are protected; logs and health checks answer basic incidents |
| 21 | Performance and reliability | Risks measured; at least one improvement is demonstrated |
| 22 | Release candidate | Release checklist, rollback plan, accessibility pass, and known issues list |
| 23 | Final release and portfolio evidence | Product is released or release-ready; evidence is organized |
| 24 | Demo, handoff, and retrospective | Public-quality demo, runbook, case study, and individual reflection |

## Required team ceremonies

- Weekly planning: choose work that can be finished in one week.
- Two short async updates per week: progress, blocker, next action.
- Weekly review/demo: show working evidence, not only slides.
- Weekly retro: keep one practice, stop one practice, try one practice.
- Monthly checkpoint: mentor scores outcomes using the rubric below.

## Assessment rubric

Score each category from 1 to 4 at the end of months 1, 3, and 6.

| Category | 1 — starting | 2 — developing | 3 — dependable | 4 — strong |
| --- | --- | --- | --- | --- |
| Fundamentals | Can follow a tutorial | Can reproduce a small example | Can apply the concept independently | Can explain trade-offs and coach someone |
| Product contribution | Artifact is incomplete | Small contribution with help | Feature/artifact is useful and reviewed | Contribution improves the team’s system |
| Quality | Happy path only | Some checks exist | Risks and failure paths are covered | Evidence is systematic and repeatable |
| Collaboration | Status is unclear | Responds when asked | Communicates early and reviews peers | Unblocks others and improves team practice |
| Documentation | Notes are fragmentary | Basic steps are recorded | Another person can use the artifact | Documentation is concise, current, and reusable |

An intern passes the final checkpoint by reaching at least level 3 in every category and presenting evidence for one complete product outcome.

## Evidence folder convention

Keep one folder or issue per week containing:

```text
week-XX/
├── outcome.md
├── links.md
├── screenshots-or-recording.md
├── review-feedback.md
└── reflection.md
```

Do not store secrets, private user data, or paid course downloads in this repository.
