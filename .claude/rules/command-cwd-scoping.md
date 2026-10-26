# command-cwd-scoping

## binding

Every terminal command an agent hands to the user must carry its own working directory. A command printed in a turn, a doc, a PR body, or a runbook is read and run somewhere else: a fresh shell, a new Claude Code or Codex session, a different tab, or a different machine. That reader does not inherit this session's current directory and cannot be told to "run this from the repo root" reliably. An unscoped command is therefore a defect, not a shorthand.

Full rule: `$HOME/projects/active/0-llm-root/rules/command-cwd-scoping.md`.
