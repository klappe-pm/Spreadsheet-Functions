# naming-conventions

## binding

Filenames are lowercase kebab-case, never underscores. Directories follow the same convention. Reserved uppercase names (`README.md`, `CLAUDE.md`, `MEMORY.md`, `CODEX.md`, `GEMINI.md`, `AGENTS.md`, `PLAN.md`, `COMMENTS-PROCESS.md`, `*.pointer`) stay literal.

`.docs/` is the reserved directory for internal work product in every project; `docs/` and `developer-docs/` hold external documentation for users and contributors.

A file's identity is its path, not its filename. Filenames are not required to be unique across a repository or vault. In a folder-per-entity layout (`skills/<name>/SKILL.md`) the folder names the entity and the reserved filename names the file's role. Links and relations therefore address files by path; `markdown-style` defines the form.

Full rule: `$HOME/projects/active/0-llm-root/rules/naming-conventions.md`.
