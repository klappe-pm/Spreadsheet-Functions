# markdown-style

## binding

Headings are lowercase kebab-case; a reserved filename's H1 keeps its literal, uppercase, with extension. Frontmatter opens on row 1 with `---` in canonical key order (domain, category, sub-category, topics, types, date-created, date-revised, status, aliases, tags, then file-specific keys sorted A to Z). `date-created` never changes; `date-revised` updates on content changes. Array values are deduped, sorted case-insensitively; an empty array is `key: []`. Unordered lists use `-`, nested two spaces, one blank line around the block, none between items. Code fences carry a language tag. Tables are pipe-style, `&#124;` for a literal pipe. Links and frontmatter relations use paths relative to the file, relations one direction only; wikilinks get converted; broken links flagged. One blank line follows frontmatter and separates sections.

Full rule: `$HOME/projects/active/0-llm-root/rules/markdown-style.md`.
