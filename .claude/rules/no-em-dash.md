# no-em-dash

## binding

Never use a dash as punctuation in authored prose. This prohibits em dashes, en dashes, spaced hyphens (` - `), and double hyphens (`--`). Use a comma, period, colon, semicolon, or parentheses instead. Applies to notes, docs, plans, commit messages, PR and issue bodies, generated reports, and conversation output.

Hyphens remain valid inside compound words (`pre-commit`, `read-only`) and in code, paths, flags, and identifiers. HTML comment markers (`<!--` and `-->`) are syntax, not punctuation, and every checker that enforces this rule ignores them. Numeric ranges use "to" (`3 to 5`), not a dash. A list item marker at line start (`- item`) is structure, not punctuation.

Full rule: `$HOME/projects/active/0-llm-root/rules/no-em-dash.md`.
