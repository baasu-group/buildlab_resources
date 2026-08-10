# Case-study operating guide

## Required volume

Every team produces **two case studies per month**. With four teams and six months, the program produces **48 case studies**:

```text
6 months × 4 teams × 2 case studies = 48 case studies
```

Case studies are stored under [case_study_INT_1.0](./case_study_INT_1.0/) using this exact hierarchy:

```text
case_study_INT_1.0/
└── M-01/
    ├── team_x/
    │   ├── Case-01/README.md
    │   └── Case-02/README.md
    ├── team_y/
    ├── team_z/
    └── team_xyz/
```

## Case-study types

- **Case-01 — Product/technical outcome:** what the team built, the problem, architecture/design decisions, evidence, and result.
- **Case-02 — Quality/learning outcome:** a failure, experiment, usability insight, performance improvement, process improvement, or important decision.

## Required Markdown sections

Every case study must contain:

1. Title and team/month.
2. Contributors and roles.
3. Problem or hypothesis.
4. Context and constraints.
5. Approach and alternatives considered.
6. Artifact links or screenshots.
7. Validation evidence and measurable result.
8. What failed or changed.
9. Lessons learned.
10. Follow-up owner and next action.

## Review flow

| Step | Owner | Timing |
| --- | --- | --- |
| Draft | Quality & Documentation Owner | Thursday of Week 4 |
| Team review | All three members | Friday of Week 4 |
| Track review | Relevant mentor | First three working days of next month |
| Publish | Program Operations Manager | By the fifth working day of next month |

Never write a case study as a tutorial summary. It must show a team decision and evidence from the shared product.
