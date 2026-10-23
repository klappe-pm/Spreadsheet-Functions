# agents

`llm-root` is the shared configuration repository for agent runtimes; owns instructions, rules, hooks, skills, commands, agents, permissions, project configuration sources, synchronization code, and documentation; runtime directories are generated outputs.

## intake

llm-root needs a git remote (`klappe-pm/llm-root` on GitHub), the runtimes it configures (Claude Code, Codex, Gemini CLI, Cursor, OpenCode), the operator's GitHub CLI session, and the secrets resolved through `scripts/credentials.py` and 1Password for the accounts and services it orchestrates (GitHub, freellmapi provider keys, Railway). It needs no inference model of its own to run its generators and hooks; the models it invokes are the ones it configures for other sessions.

Free tiers: on, no opt-out. llm-root's own work is orchestration, generation and validation of configuration text, none of it proprietary or customer facing, so the default of `docs/adr/2026-09-25-resolve-a-model-route-by-precedence.md` applies unchanged.

## data-strategy

llm-root produces: generated runtime configuration, deployed to `~/.claude/`, `~/.codex/`, `~/.gemini/`, `~/.cursor/` and `~/.config/opencode/`, disposable and rebuilt by `sync.py`; guard, budget and session telemetry under `~/.agent-hooks/telemetry/` and `~/.agent-hooks/state/`, local only and never committed; prompt captures under `.docs/prompts/`, committed and redacted before persisting; and its own source history in git.

Where it lives: the source tree and `docs/` live in the private `klappe-pm/llm-root` repository; telemetry and state live on the local filesystem outside git.

Retention: telemetry and state accumulate locally with no automatic purge; committed docs are kept indefinitely as project history; generated runtime output has no retention concern, since it is replaced on every `sync.py` run.

Sensitivity: the repository is private. Captured content is redacted before it is written (`rules/captured-content-redaction.md`), and no literal secret is ever committed (`rules/secrets-out-of-git.md`) or printed (`rules/no-secret-exposure.md`).

Never reaches a free tier: any literal secret or credential, any unredacted capture, any environment dump, and any bulk export of this repository's private source or telemetry to a third party beyond what a specific routed task requires.

## source-and-output-boundary

Edit only the source tree under `$HOME/projects/active/0-llm-root/`: `AGENTS.md`, `README.md`, `permissions.json`, `components.json`, `control-plane.md`, `loadouts/`, `models/`, `rules/`, `hooks/`, `skills/`, `commands/`, `agents/`, `projects-root/`, `scripts/`, and `docs/`.

Generated runtime output lives under `~/.claude/`, `~/.codex/`, `~/.gemini/`, `~/.cursor/`, and `~/.config/opencode/`. A later synchronization overwrites those locations. Change the source, not the generated copy.

## session-start

At the start of a session in a managed project, run `python3 $HOME/projects/active/0-llm-root/scripts/reconcile-control-plane.py`, then read `.docs/llm-root-control-plane.md` in the project before acting. Reconciliation records source additions, project additions, moves, and removals, then refreshes the local snapshot for active projects.

## editing-and-sync

`control-plane.md` is generated inventory with preserved opt-in decisions. Do not hand-add source rows. Add, move, or remove the source file or project, then run the reconciler.

Hook registration belongs only in `hooks/hooks.json`. Permissions belong only in `permissions.json`. External components (MCP servers, plugins, foreign hooks, third-party skills, services, dependencies) and the user-level budget defaults belong only in `components.json`. A work item's session loadout belongs only in `loadouts/<work-item>.json`. An inference provider and the models it serves belong only in `models/providers/<provider>.json`; `models/index.json` and the pages under `docs/models/` and `docs/providers/` are generated from them by `scripts/build-model-catalog.py`. Project-local configuration belongs only in `projects-root/<project>/`.

After a source edit, run `python3 $HOME/projects/active/0-llm-root/scripts/sync.py`. The runtime PostToolUse reconciliation hook keeps the control plane current after agent-authored source changes, but synchronization remains the step that deploys content to runtime outputs.

When a hook or gate blocks an action, surface the block verbatim and fix the underlying condition. Do not bypass it without explicit approval in the current session.

## extraction-efforts

The flow for extracting a component from this repository and publishing it under MIT is `docs/adr/adr-0003-2026-10-08-extract-and-publish-core-components.md`; the first component is the runtime engine, published as `klappe-pm/agentrc`. A session working on an extraction effort reads the local, uncommitted log `.docs/COMMENTS-PROCESS.md` at the repository root before acting, appends one dated entry of one or two lines there for each process observation as it occurs, and ends every commit message with a `Process observations:` section carrying the entries recorded during that commit's work. The log file is never committed and entries are never rewritten. Nothing crossing into a public repository carries `models`, `providers` or `session-link` keys, a session permalink, or a tokens comment.

## intent-delivery-design-integration

For intent-to-delivery and ADR integration, resolve `docs/plans/INTENT-DELIVERY-PLAN.pointer` and read `PLAN.md` section `intent-delivery-integration`. It owns WS-23 through WS-26 and WI-134 through WI-154. Existing work-item status, loadouts, provider catalogs, dispatcher, launcher, permissions and hook registration remain authoritative. Read the assigned work order and `docs/plans/intent-delivery/worker-contract.md` completely; load only the named source slices afterward.

This phase writes design records only inside llm-root. Do not build starters, implementation code or operational schemas, enable hooks, create execution loadouts, change model defaults, run reconciliation or synchronization, or edit generated runtime/instruction copies. The coordinator alone updates PLAN status and integrates shared research. The assigned worker owns only its work order's declared output and evidence paths.

Before an autonomous pivot, verify dependency evidence, exact source revision, current claim, approved scope, real budget, compatible launcher/loadout support and native confinement. A QUEUED row or accepted ADR does not prove enforcement or grant deployment authority. Independent review covers correctness, adversarial cases, performance methodology, conformance and clarity. Keep owner choices explicit and implementation disabled where required authority or capability is missing.

## documentation

Use [README.md](README.md) for the repository overview, [SCRIPTS.md](SCRIPTS.md) for automation, [docs/adapters/README.md](docs/adapters/README.md) for runtime translators, [docs/runtimes/README.md](docs/runtimes/README.md) for delivered runtime behavior, and [docs/scripts/README.md](docs/scripts/README.md) for operational scripts and hooks.

## authority-order

Inside a project, apply project validators and CI first, project instruction files second, and this user-scope configuration third. Read a plan document whole before acting on it.

The global tier (captured-content-redaction, guard-bypass-approval, irreversible-external-actions, manual-changes-authoritative, no-agent-attribution, no-client-named-features, no-external-repo-publishing, no-hardwrapped-github-comments, no-secret-exposure, repo-scope, secret-exposure-response, secret-resolution, secrets-out-of-git, token-shaped-values) overrides a project's own instruction files; everything else in this configuration yields to the project.

<!-- The block below is generated by scripts/gen-rules-digest.py. Do not edit it directly. -->

<!-- BEGIN RULES-DIGEST generated by scripts/gen-rules-digest.py -- do not hand-edit between markers -->

## user-scope-rules-digest

Rendered from the canonical rule tree (`rules/` in llm-root) per `rules/tiers.json`: each rule's binding section and a pointer to its full text. These rules are binding on every agent surface; read the full rule when a task turns on its detail. Edit the source rules and re-run `scripts/gen-rules-digest.py`; hand-edits between the markers are overwritten.

### captured-content-redaction

Tier: global.

Content captured from external sources (crawls, exports, scraped pages, API responses) is scanned with the `token-shaped-values` detector before persisting. Replace each match with `[REDACTED:<kind>]`. Drop the record if redaction leaves it meaningless. Reports and indexes built from captured content inherit this: nothing token-shaped reaches a generated file.

Full rule: `$HOME/projects/active/0-llm-root/rules/captured-content-redaction.md`

### guard-bypass-approval

Tier: global.

When a hook, guard, permission check, or safety gate blocks an action, stop. The block is a required checkpoint, not an obstacle to optimize. AGENTS.md's authority-order preamble names the global tier, this rule included, as overriding every project's own instruction files, which is the standing basis for calling this rule absolute rather than a default a project can narrow.

Full rule: `$HOME/projects/active/0-llm-root/rules/guard-bypass-approval.md`

### irreversible-external-actions

Tier: global.

An irreversible external action is any action taken outside the local environment that cannot be fully retracted: sending a message or email, submitting an application, posting to a platform, placing an order, or initiating contact on behalf of the user or a third party.

Never take an irreversible external action without explicit instruction naming the action in the same turn. Approval is spent when used. It covers exactly the action named, nothing adjacent, nothing implied, nothing that follows from it.

Full rule: `$HOME/projects/active/0-llm-root/rules/irreversible-external-actions.md`

### manual-changes-authoritative

Tier: global.

A change the user makes by hand is tracked, intentional, and accurate. It is the current state of record, not an anomaly to investigate. This applies to edits, deletions, renames, moves, reverts, and manual overrides of anything an agent generated.

Treat the manual change as settled and proceed to the next action. Do not re-verify that it was intended. Do not audit whether it was complete, consistent, or correct. Do not surface it as a discrepancy, a regression, or an unexplained difference. Never offer, propose, or move toward undoing, restoring, or reverting it.

Full rule: `$HOME/projects/active/0-llm-root/rules/manual-changes-authoritative.md`

### no-agent-attribution

Tier: global.

Nothing authored on the user's behalf credits a coding agent, an assistant, a model, a model provider, or an agent runtime as creator or contributor. Commit messages, pull request titles and bodies, issue bodies and comments, code comments, documentation, generated files, notes, release notes, footers, banners, metadata, and generated reports carry the human author and nothing else. This holds for every current and future runtime, agent, and subagent, in conversation output and in every authored artifact. AGENTS.md's authority-order preamble names the global tier, this rule included, as overriding every project's own instruction files, which is the standing basis for calling this rule absolute rather than a default a project can narrow.

Full rule: `$HOME/projects/active/0-llm-root/rules/no-agent-attribution.md`

### no-client-named-features

Tier: global.

A feature, component, capability, package, module or skill is never named after a client, a client's business, or a client contact. Name it for what it does: `wallpaper-estimating-agent-skills`, not a client's name. This holds in file names, ids, H1 titles, aliases, branch names and generated catalogs, and for work that came from a client's repository. A client name may appear only as a reference to where something came from (a repository path, a file path, an evidence line), never as the thing's name. When a feature carries a client name today, rename it to its function before it is published or catalogued.

Full rule: `$HOME/projects/active/0-llm-root/rules/no-client-named-features.md`

### no-external-repo-publishing

Tier: global.

Never publish anything to a repository the user does not own. No pull requests, no pushes, no branches, no forks, no issues, no comments, no reviews, no releases. This holds for every repository whose owner is not the user, including one the user has cloned, contributes to, or has an open PR against.

The rule is absolute and standing. It is not satisfied by the work being finished, tested, reviewed, or obviously useful, and not by the task appearing to call for it. AGENTS.md's authority-order preamble names the global tier, this rule included, as overriding every project's own instruction files, which is the standing basis for calling this rule absolute rather than a default a project can narrow.

Full rule: `$HOME/projects/active/0-llm-root/rules/no-external-repo-publishing.md`

### no-hardwrapped-github-comments

Tier: global.

Never hard-wrap prose in anything posted to GitHub: pull request, issue and review comments, inline review comments, pull request and issue bodies, release notes, and session handoff comments. Write each paragraph and each list item on one line; GitHub soft-wraps it. What counts as a wrap, and which line breaks are structure, is defined once in `no-hardwrapped-writing`. HTML lines such as `<details>` and `<summary>` are structure as well.

When a body is wrapped, remove the wraps before posting: write it to a file, reflow it with `python3 $HOME/projects/active/0-llm-root/hooks/lib/prose-detect.py unwrap <file>`, and post it with `--body-file <file>`.

Global tier: AGENTS.md's authority-order preamble names it as overriding every project's own instruction files, and `scripts/sync-projects.py` carries its guard into every active project.

Full rule: `$HOME/projects/active/0-llm-root/rules/no-hardwrapped-github-comments.md`

### no-secret-exposure

Tier: global.

Never place a literal token-shaped value (see `token-shaped-values`) in any file, command, log, stdout, generated artifact, or the conversation. Never read `.env`, `settings.local.json`, credential files, or raw `env`/`printenv` output into context. Never pass a secret as a command argument or capture one with `$(op read …)`; both land in shell history and the transcript. To verify a secret resolved, check existence, length, or the first four characters only. If a value is exposed anyway, follow `secret-exposure-response`.

Full rule: `$HOME/projects/active/0-llm-root/rules/no-secret-exposure.md`

### repo-scope

Tier: global.

Every session operates inside exactly one repo at a time. That repo is the blast radius for reads, writes, commits, and commands.

Full rule: `$HOME/projects/active/0-llm-root/rules/repo-scope.md`

### secret-exposure-response

Tier: global.

When a literal secret has landed anywhere (file, commit, log, transcript, generated artifact): stop the current task, report the exposure to the user in the same turn, treat the secret as burned and rotate it, and purge it from git history if committed. Redaction after exposure is cleanup, not remediation; rotation is the remediation.

Full rule: `$HOME/projects/active/0-llm-root/rules/secret-exposure-response.md`

### secret-resolution

Tier: global.

Use GitHub CLI's native macOS Keychain login for local GitHub operations across projects. Do not require 1Password enrollment, export the token, or request repeated sign-ins when a session cannot access Keychain. Verify through an authenticated endpoint in a permitted execution context; report access failures explicitly. Read the full rule before troubleshooting.

Other managed secrets use secrets-v1 (`secret://<namespace>/<key>`) and configured providers. Never hardcode credentials or print them. `${VAR}` references in files require a documented injector. Literals are covered by `no-secret-exposure`.

Full rule: `$HOME/projects/active/0-llm-root/rules/secret-resolution.md`

### secrets-out-of-git

Tier: global.

`settings.local.json`, env files, credentials, private keys, and OAuth artifacts are gitignored and never staged. `.env.example` with placeholder values is allowed. The pre-commit scan (`scripts/git-hooks/check-staged-secrets.sh`) runs the `token-shaped-values` detector on staged content and blocks matches. If a secret was already committed, follow `secret-exposure-response`.

Full rule: `$HOME/projects/active/0-llm-root/rules/secrets-out-of-git.md`

### token-shaped-values

Tier: global.

A value is token-shaped when the pattern set in `hooks/lib/guard-utils.sh` matches it: cloud and API key prefixes, JWTs, PEM blocks, long hex or base64 runs adjacent to key/token/secret. That detector is the single definition. Every rule that says "secret" or "token-shaped" means this; do not reason about whether something looks like a secret, run the detector.

Full rule: `$HOME/projects/active/0-llm-root/rules/token-shaped-values.md`

### command-cwd-scoping

Tier: common.

Every terminal command an agent hands to the user must carry its own working directory. A command printed in a turn, a doc, a PR body, or a runbook is read and run somewhere else: a fresh shell, a new Claude Code or Codex session, a different tab, or a different machine. That reader does not inherit this session's current directory and cannot be told to "run this from the repo root" reliably. An unscoped command is therefore a defect, not a shorthand.

Full rule: `$HOME/projects/active/0-llm-root/rules/command-cwd-scoping.md`

### delegated-quality-passes

Tier: common.

Match verification and review to the change's consequences. Default to one builder, the smallest relevant checks, and completion when the requested behavior works. Additional review needs a named risk or an explicit request.

Full rule: `$HOME/projects/active/0-llm-root/rules/delegated-quality-passes.md`

### docs-provenance-frontmatter

Tier: common.

In a private repository, every Markdown file an agent creates or content-revises under a `.docs/` or `docs/` directory carries three frontmatter keys recording the agent session that produced it: `models`, `providers`, and `session-link`. The agent populates them from the session it is running in, on every content write, without being asked. A public repository never carries them.

Full rule: `$HOME/projects/active/0-llm-root/rules/docs-provenance-frontmatter.md`

### find-fix-document

Tier: common.

Verify defects with concrete evidence, fix causes within the requested scope, and keep a concise record where useful. Match the record and verification to the defect's consequences.

Full rule: `$HOME/projects/active/0-llm-root/rules/find-fix-document.md`

### finish-or-record-scope-change

Tier: common.

Work an agent decided not to do is a scope change. It is finished in the same cycle, or it is recorded as a scope change with its reason and its cost. It is never handed back as a closing list of things that were within reach and were skipped.

The failure this prevents has a recognisable shape: a report that ends "two things I did not do", naming work the agent understood, had the access to complete, and left undone because the turn felt finished. Nobody decided to drop that work. It was dropped, then described. Describing it is not the same as deciding it, and a list in a final message is where it stops being tracked.

Full rule: `$HOME/projects/active/0-llm-root/rules/finish-or-record-scope-change.md`

### human-facing-writing

Tier: common.

Human-facing documents use plain, direct language appropriate to their reader. Strategy documents, resumes, candidate positioning, plans, and other reader-ready artifacts state the useful conclusion, priority, experience, or decision in finished prose.

Full rule: `$HOME/projects/active/0-llm-root/rules/human-facing-writing.md`

### markdown-style

Tier: common.

Headings are lowercase kebab-case; a reserved filename's H1 keeps its literal, uppercase, with extension. Frontmatter opens on row 1 with `---` in canonical key order (domain, category, sub-category, topics, types, date-created, date-revised, status, aliases, tags, then file-specific keys sorted A to Z). `date-created` never changes; `date-revised` updates on content changes. Array values are deduped, sorted case-insensitively; an empty array is `key: []`. Unordered lists use `-`, nested two spaces, one blank line around the block, none between items. Code fences carry a language tag. Tables are pipe-style, `&#124;` for a literal pipe. Links and frontmatter relations use paths relative to the file, relations one direction only; wikilinks get converted; broken links flagged. One blank line follows frontmatter and separates sections.

Full rule: `$HOME/projects/active/0-llm-root/rules/markdown-style.md`

### memory-criteria

Tier: common.

Applies to `~/.claude/projects/<project>/memory/` auto-memory and to any analogous per-project memory store written across sessions. Write only facts the next session needs: toolchain conventions, past gotchas with their resolutions, the user's style conventions, external constraints, and in-progress task state that must survive a session boundary. Never write session work logs, the story of what a session did to the workstation, one-off research findings, duplicates of CLAUDE.md or the rule tree, or unverified hypotheses. Keep MEMORY.md under 200 lines by moving topics into linked files. Never report an absent or unwritable store; drop the attempt silently.

Full rule: `$HOME/projects/active/0-llm-root/rules/memory-criteria.md`

### naming-conventions

Tier: common.

Filenames are lowercase kebab-case, never underscores. Directories follow the same convention. Reserved uppercase names (`README.md`, `CLAUDE.md`, `MEMORY.md`, `CODEX.md`, `GEMINI.md`, `AGENTS.md`, `PLAN.md`, `COMMENTS-PROCESS.md`, `*.pointer`) stay literal.

`.docs/` is the reserved directory for internal work product in every project; `docs/` and `developer-docs/` hold external documentation for users and contributors.

A file's identity is its path, not its filename. Filenames are not required to be unique across a repository or vault. In a folder-per-entity layout (`skills/<name>/SKILL.md`) the folder names the entity and the reserved filename names the file's role. Links and relations therefore address files by path; `markdown-style` defines the form.

Full rule: `$HOME/projects/active/0-llm-root/rules/naming-conventions.md`

### no-em-dash

Tier: common.

Never use a dash as punctuation in authored prose. This prohibits em dashes, en dashes, spaced hyphens (` - `), and double hyphens (`--`). Use a comma, period, colon, semicolon, or parentheses instead. Applies to notes, docs, plans, commit messages, PR and issue bodies, generated reports, and conversation output.

Hyphens remain valid inside compound words (`pre-commit`, `read-only`) and in code, paths, flags, and identifiers. HTML comment markers (`<!--` and `-->`) are syntax, not punctuation, and every checker that enforces this rule ignores them. Numeric ranges use "to" (`3 to 5`), not a dash. A list item marker at line start (`- item`) is structure, not punctuation.

Full rule: `$HOME/projects/active/0-llm-root/rules/no-em-dash.md`

### no-hardwrapped-writing

Tier: common.

Never hard-wrap prose in authored Markdown. Write each paragraph and each list item as one line and let the editor soft-wrap. Never insert breaks at a fixed column. Applies to notes, docs, plans, PR and issue bodies, runbooks, and any generated Markdown artifact.

Break lines only for structure: blank lines between blocks, headings, list items, table rows, code fences, blockquotes, frontmatter, and intentional line breaks (trailing two spaces or backslash).

Full rule: `$HOME/projects/active/0-llm-root/rules/no-hardwrapped-writing.md`

### no-redundant-labels

Tier: common.

- A table cell never opens with a label that repeats or paraphrases its column header.
- A list item never opens with its section heading's noun as a label.
- A heading is never restated as the first sentence of its section.
- A fact, figure or sentence appears once per file; a later mention refers to the first instead of repeating it.
- No preamble that announces the body, no closing summary that repeats it, no "as noted above", and no "in other words" followed by the same point.
- Shorter wins when nothing is lost. Delete words before rewording.

Full rule: `$HOME/projects/active/0-llm-root/rules/no-redundant-labels.md`

### open-decision-elicitation

Tier: common.

An open decision is a choice that blocks forward progress on a turn or session and that only the user can resolve: a fork in approach with no clearly correct default, a fact only the user holds, or a tradeoff between named options that changes the outcome materially.

When a turn or session would otherwise end with one unresolved, prompt the user directly for an answer through the surface's structured elicitation tool, or with a single direct question in prose where none exists, instead of burying a passive question or proceeding on a silent default.

Full rule: `$HOME/projects/active/0-llm-root/rules/open-decision-elicitation.md`

### output-format-contract

Tier: common.

When a file, prior session, or explicit instruction defines an output format for a task, that format is the contract. Do not re-derive, simplify, or improve it without instruction.

Full rule: `$HOME/projects/active/0-llm-root/rules/output-format-contract.md`

### session-handoff-on-pr

Tier: common.

Every session ends by writing a handoff where the next session will find it: a comment on the pull request that carries the session's work. The next session reads that comment before it does anything else.

A transcript is not a system of record. It ends with the session, it is not attached to the code it describes, and nobody reads it. A pull request comment is attached to the diff, timestamped, durable, and visible to anyone reviewing the change, which is what makes the handoff provenance rather than a note.

A cloud session also posts its token count beside the handoff, as a separate `## session tokens` comment, on a private repository only.

Full rule: `$HOME/projects/active/0-llm-root/rules/session-handoff-on-pr.md`

### shell-discipline

Tier: common.

One command per Bash call. Real work goes into committed scripts. Read and write files through the Read, Edit, and Write tools, not shell. The prose guard instruments only Write, Edit, and NotebookEdit; a write made through Bash, a heredoc, or an interpreter invocation never passes through it. The attribution guard runs on every tool call, Bash included, but checks attribution only. Keeping file changes on the editor tools is what keeps a change both guarded and reviewable. See `enforcement` below for what a hook actually checks in this rule.

Full rule: `$HOME/projects/active/0-llm-root/rules/shell-discipline.md`

<!-- END RULES-DIGEST -->
