# Program management hierarchy

## Reporting hierarchy

```text
Program Director / Technical Mentor
│
├── Program Operations Manager
│   ├── Product and Pre-sales Mentor
│   ├── UI/UX Mentor
│   ├── Frontend Mentor
│   ├── Backend Mentor
│   ├── QA Mentor
│   ├── DevOps Mentor
│   ├── Cloud Mentor
│   └── AI/ML Mentor
│
└── Four monthly delivery teams
    ├── team_x
    ├── team_y
    ├── team_z
    └── team_xyz
```

Mentors provide standards and review. Team members own delivery. Mentors must not silently complete intern work; they clarify, review, and unblock.

## Team-level hierarchy

Each team has three people. Their responsibilities are explicit for each week:

| Role | Responsibility | Evidence |
| --- | --- | --- |
| Team Lead | Plans the week, maintains scope, runs the Friday demo, escalates blockers | Team update, demo, decision log |
| Delivery Owner | Coordinates the feature implementation across relevant tracks | Working artifact, integration notes, pull requests |
| Quality & Documentation Owner | Checks acceptance criteria, risk, test evidence, and case-study notes | Test/review record, weekly notes, case-study draft |

The three roles rotate weekly inside the team. The roster order in [TEAM_ROSTER_AND_ROTATION.md](./TEAM_ROSTER_AND_ROTATION.md) is used as the starting order:

| Week of month | Team Lead | Delivery Owner | Quality & Documentation Owner |
| ---: | --- | --- | --- |
| Week 1 | Member 1 | Member 2 | Member 3 |
| Week 2 | Member 2 | Member 3 | Member 1 |
| Week 3 | Member 3 | Member 1 | Member 2 |
| Week 4 | Member 1 | Member 3 | Member 2 |

## Decision rights

- **Team Lead:** daily sequencing, meeting facilitation, blocker escalation.
- **Delivery Owner:** implementation coordination and integration readiness.
- **Quality & Documentation Owner:** evidence quality, acceptance criteria, and case-study completeness.
- **Track Mentor:** technical approval within a discipline.
- **Program Director:** scope, risk, release, or staffing decisions affecting multiple teams.

No intern changes the shared API, database schema, deployment configuration, or product scope without a review from the relevant mentor and a written decision.

## Operating rules

1. Every task has one accountable owner, one reviewer, a due week, and a definition of done.
2. Every team updates its weekly Markdown file by Friday.
3. Every team demonstrates one working or reviewable outcome each Friday.
4. Case studies are written from evidence, not claims.
5. A team may carry work forward only with a written reason and a new owner/date.
6. Secrets, personal data, and private customer material never enter this repository.
