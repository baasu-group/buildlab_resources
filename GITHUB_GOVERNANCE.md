# GitHub governance setup

The repository includes local controls in `.github/CODEOWNERS` and `.github/workflows/path-ownership.yml`. GitHub repository settings must also be configured by an administrator.

## Protect `main`

In GitHub, open **Settings → Rules → Rulesets → New branch ruleset** and target `main`.

Enable:

- Require a pull request before merging.
- Require at least one approving review.
- Require review from Code Owners.
- Dismiss stale approvals when new commits are pushed.
- Require the `Check changed paths` status check.
- Block force pushes.
- Block branch deletion.
- Restrict who can push directly to `main` to `basan-ta` or the maintainer team.

The same controls are available through **Settings → Branches → Branch protection rules** if rulesets are not available for the repository plan.

## Protect direct pushes by path

`CODEOWNERS` protects pull-request merging. It does not, by itself, stop a collaborator with write access from pushing to an unprotected branch.

If the repository plan supports push rulesets, create these rules:

| Path restriction | Bypass users |
| --- | --- |
| `buildLab_resources/**/*` | `basan-ta` |
| Each personal contributor folder | That GitHub user and `basan-ta` |
| `.github/**/*` | `basan-ta` |

If push rulesets are unavailable, the protected `main` branch plus the included path-ownership workflow still prevents unauthorized pull requests from merging.

## Verify the setup

Test with small pull requests:

1. `code-himal` changes `Backend_INT_1.0/code-himal/W-01/README.md` — should pass ownership check.
2. `code-himal` changes `Frontend_INT_1.0/Bivek09/...` — should fail.
3. Any intern changes `buildLab_resources/...` — should fail.
4. `basan-ta` changes any protected path — should pass.

The workflow is a policy check, not a substitute for branch protection. A maintainer must configure the GitHub ruleset before inviting contributors.
