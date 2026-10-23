# session-handoff-on-pr

## binding

Every session ends by writing a handoff where the next session will find it: a comment on the pull request that carries the session's work. The next session reads that comment before it does anything else.

A transcript is not a system of record. It ends with the session, it is not attached to the code it describes, and nobody reads it. A pull request comment is attached to the diff, timestamped, durable, and visible to anyone reviewing the change, which is what makes the handoff provenance rather than a note.

A cloud session also posts its token count beside the handoff, as a separate `## session tokens` comment, on a private repository only.

Full rule: `$HOME/projects/active/0-llm-root/rules/session-handoff-on-pr.md`.
