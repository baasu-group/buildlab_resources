# Contributing to BuildLab

## Repository ownership model

`buildLab_resources/` is the protected curriculum source. Only `basan-ta` may approve and merge changes there.

`buildLab_INT_1.0/` contains intern work. Contributors may update their own GitHub-username folder and prepare shared project or case-study artifacts. The default branch remains protected and all changes go through pull requests.

## Branch naming

Use one of these patterns:

```text
intern/<github-username>/W-<week>
team/<team-name>/M-<month>-<purpose>
owner/<purpose>
```

Examples:

```text
intern/code-himal/W-07
team/team_x/M-03-auth-flow
owner/update-resources
```

## Personal-folder rule

An intern may change only:

```text
buildLab_INT_1.0/<TRACK>_INT_1.0/<their-github-username>/**
```

Interns may also prepare shared project and case-study changes. The path-ownership workflow checks these rules on pull requests, and `CODEOWNERS` requests the required reviewer.

## Pull request process

1. Create a branch from the latest `main`.
2. Make one focused weekly or team change.
3. Update the relevant weekly Markdown record.
4. Run local checks and inspect the changed-file list.
5. Open a pull request and complete the template.
6. Wait for the required code-owner review.
7. Merge only after required checks and approvals pass.

Never commit secrets, tokens, private customer data, or paid course downloads.
