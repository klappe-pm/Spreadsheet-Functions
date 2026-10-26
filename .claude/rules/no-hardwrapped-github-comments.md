# no-hardwrapped-github-comments

## binding

Never hard-wrap prose in anything posted to GitHub: pull request, issue and review comments, inline review comments, pull request and issue bodies, release notes, and session handoff comments. Write each paragraph and each list item on one line; GitHub soft-wraps it. What counts as a wrap, and which line breaks are structure, is defined once in `no-hardwrapped-writing`. HTML lines such as `<details>` and `<summary>` are structure as well.

When a body is wrapped, remove the wraps before posting: write it to a file, reflow it with `python3 $HOME/projects/active/0-llm-root/hooks/lib/prose-detect.py unwrap <file>`, and post it with `--body-file <file>`.

Global tier: AGENTS.md's authority-order preamble names it as overriding every project's own instruction files, and `scripts/sync-projects.py` carries its guard into every active project.

Full rule: `$HOME/projects/active/0-llm-root/rules/no-hardwrapped-github-comments.md`.
