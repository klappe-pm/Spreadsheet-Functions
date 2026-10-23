# docs-provenance-frontmatter

## binding

In a private repository, every Markdown file an agent creates or content-revises under a `.docs/` or `docs/` directory carries three frontmatter keys recording the agent session that produced it: `models`, `providers`, and `session-link`. The agent populates them from the session it is running in, on every content write, without being asked. A public repository never carries them.

Full rule: `$HOME/projects/active/0-llm-root/rules/docs-provenance-frontmatter.md`.
