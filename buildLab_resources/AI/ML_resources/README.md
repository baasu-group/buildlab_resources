# AI/ML and responsible AI track

## Mission

Use AI/ML only where it improves a real product decision or user task. Start with a measurable problem, a safe data boundary, and a non-AI baseline. The track emphasizes applied AI literacy, evaluation, and responsible integration rather than trying to train a large model in six months.

## Six-month progression

| Month | Learn and practice | Product deliverable | Validation |
| --- | --- | --- | --- |
| 1 — Problem and data literacy | Python, statistics vocabulary, problem framing, data ownership, privacy, bias | AI opportunity brief and data inventory | Mentor rejects vague “add AI” proposals; metric is measurable |
| 2 — Baselines | Data cleaning, exploratory analysis, train/test split, simple rules and classical models | Baseline notebook or rule-based feature | Reproducible data preparation and baseline metric |
| 3 — Applied AI slice | Model/API selection, prompt design, structured outputs, validation, human review | Small assistant, classifier, or recommendation experiment | Compare AI result to baseline; record failure cases |
| 4 — Evaluation | Precision/recall or task metrics, hallucination tests, safety cases, cost/latency | Evaluation set and scorecard | At least 20 representative cases; thresholds and stop conditions |
| 5 — Integration and operations | API boundaries, caching, rate limits, privacy, monitoring, fallback behavior | Backend-integrated AI feature or ML service | Failure, abuse, timeout, and fallback tests |
| 6 — Responsible release | Documentation, model card/decision record, user disclosure, feedback loop | Release-ready feature or recommendation not to ship | Risk review, reproducible demo, and clear limitations |

## Suggested product experiments

- Task-description summarizer with user confirmation.
- Duplicate-task suggestion with a visible confidence score.
- Natural-language task search with a deterministic fallback.
- Team workload insight using transparent aggregation before ML.

Do not use real private intern data. Use synthetic or approved data, document retention, and avoid automated decisions about people without explicit review.

## Required outputs

1. Problem statement, success metric, and non-AI baseline.
2. Data inventory and privacy/risk assessment.
3. Reproducible notebook or service prototype.
4. Evaluation dataset, scorecard, and failure log.
5. Integration, fallback, and monitoring plan.
6. Responsible AI decision record and final demo.

## Validated free resources

- [AI Engineer roadmap](https://roadmap.sh/ai-engineer)
- [Machine Learning roadmap](https://roadmap.sh/machine-learning)
- [AI and Data Scientist roadmap](https://roadmap.sh/ai-data-scientist)
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)
- [StatQuest](https://www.youtube.com/@statquest)
- [3Blue1Brown](https://www.youtube.com/@3blue1brown)
- [Python for Absolute Beginners](https://www.udemy.com/course/free-python/) — free when validated; prerequisite only

See the [central resource catalog](../../RESOURCE_CATALOG.md) for fallback resources.

## Final assessment

Present both the feature and the reasons it might fail. A strong submission can recommend not shipping when the baseline is safer, cheaper, or more accurate.
