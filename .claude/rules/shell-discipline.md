# shell-discipline

## binding

One command per Bash call. Real work goes into committed scripts. Read and write files through the Read, Edit, and Write tools, not shell. The prose guard instruments only Write, Edit, and NotebookEdit; a write made through Bash, a heredoc, or an interpreter invocation never passes through it. The attribution guard runs on every tool call, Bash included, but checks attribution only. Keeping file changes on the editor tools is what keeps a change both guarded and reviewable. See `enforcement` below for what a hook actually checks in this rule.

Full rule: `$HOME/projects/active/0-llm-root/rules/shell-discipline.md`.
