# memory-criteria

## binding

Applies to `~/.claude/projects/<project>/memory/` auto-memory and to any analogous per-project memory store written across sessions. Write only facts the next session needs: toolchain conventions, past gotchas with their resolutions, the user's style conventions, external constraints, and in-progress task state that must survive a session boundary. Never write session work logs, the story of what a session did to the workstation, one-off research findings, duplicates of CLAUDE.md or the rule tree, or unverified hypotheses. Keep MEMORY.md under 200 lines by moving topics into linked files. Never report an absent or unwritable store; drop the attempt silently.

Full rule: `$HOME/projects/active/0-llm-root/rules/memory-criteria.md`.
