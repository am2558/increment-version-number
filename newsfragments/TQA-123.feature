Added a workflow that creates PR notes from files in `newsfragments` and a check that `newsfragments` is not empty. Integrated towncrier into the workflow and requirements.txt for generating release notes. 

- New CI check runs on opened, synchronized, and reopened PRs to ensure `newsfragments` is not empty.
- On merges to the base branch, generates release notes from `newsfragments` and appends them to `NEWS.rst`.

JIRA Ticket: [TQA-123](https://aliro.atlassian.net/browse/TQA-123)
