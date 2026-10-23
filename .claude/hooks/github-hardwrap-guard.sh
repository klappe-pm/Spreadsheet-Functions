#!/usr/bin/env bash
# PreToolUse hook. Removes hard wraps from prose posted to GitHub, and stops
# the post when they cannot be removed: a pull request, issue or review
# comment, a pull request or issue body, or release notes
# (rules/no-hardwrapped-github-comments.md).
#
# Registered in hooks/hooks.json with no matcher, so it sees Bash and any
# MCP server's GitHub writer. Bash is judged on gh only: the --body,
# --comment and --notes values, their body files, and a gh api call's body
# field, inline, as @file, or inside --input JSON. Titles, graphql queries,
# --jq expressions and git commit messages are never judged. The bodies come
# from hooks/lib/attribution-detect.py (github_body_sources), whose gh parser
# the attribution guard already relies on, so one parser decides what a
# command posts. The wrap test is prose-detect.py's, the one prose-guard.sh
# applies to Markdown files, with HTML lines (<details>, <summary>)
# structural.
#
# A wrapped body is fixed and the call allowed on every runtime, by the
# operator's decision of 2026-10-14: prose-detect.py github-hardwrap-fix
# reflows a body file in place, a body written in the command in the command
# text, or a GitHub tool's body fields, judges the result again, and the hook
# returns the rewrite in the shape each runtime documents (checked
# 2026-10-14 against learn.chatgpt.com/docs/hooks for Codex,
# geminicli.com/docs/hooks/reference for Gemini CLI and cursor.com/docs/hooks
# for Cursor; OpenCode through hooks/opencode-runtime-hooks.ts). A body it
# cannot reach (built at run time, escaped in a form it cannot match) is
# denied, and the deny names the reflow command, prose-detect.py unwrap
# <file>. The runtime is read from where the script is installed, as
# hooks/prompt-capture.sh does. The shell tool is Bash, run_shell_command
# (Gemini CLI) or Shell (Cursor).
#
# Carried into every active project's .claude/hooks/ by
# scripts/sync-projects.py (global tier). The carried copy stands down when
# the identical user-level guard is registered, as no-attribution-guard.sh
# does, so one call is never rewritten twice.
#
# Escape hatch: ALLOW_HARDWRAP=1, shared with prose-guard.sh, only to quote
# hard-wrapped source text verbatim.
#
# Emits a single JSON object on stdout per Claude Code's hook protocol.

set -u
trap 'exit 0' ERR
[ "${RUNTIME_HOOKS_DISABLE:-0}" = "1" ] && exit 0
[ "${ALLOW_HARDWRAP:-0}" = "1" ] && exit 0

HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

_carried_copy_defers() {
  [ -n "${CLAUDE_PROJECT_DIR:-}" ] && [ -n "${HOME:-}" ] || return 1
  local here project_hooks user_hooks rel
  here="$(cd "$HOOK_DIR" && pwd -P)" || return 1
  project_hooks="$(cd "$CLAUDE_PROJECT_DIR/.claude/hooks" 2>/dev/null && pwd -P)" || return 1
  [ "$here" = "$project_hooks" ] || return 1
  user_hooks="$(cd "$HOME/.claude/hooks" 2>/dev/null && pwd -P)" || return 1
  [ "$user_hooks" != "$here" ] || return 1
  [ -x "$user_hooks/github-hardwrap-guard.sh" ] || return 1
  grep -q '/.claude/hooks/github-hardwrap-guard.sh' "$HOME/.claude/settings.json" 2>/dev/null || return 1
  for rel in github-hardwrap-guard.sh lib/log.sh lib/guard-utils.sh lib/guard-log.sh lib/prose-detect.py lib/attribution-detect.py; do
    cmp -s "$here/$rel" "$user_hooks/$rel" || return 1
  done
  return 0
}
_carried_copy_defers && exit 0

# shellcheck source=lib/log.sh
source "$HOOK_DIR/lib/log.sh"
# shellcheck source=lib/guard-log.sh
[ -f "$HOOK_DIR/lib/guard-log.sh" ] && source "$HOOK_DIR/lib/guard-log.sh"
command -v guard_log_event >/dev/null 2>&1 || guard_log_event() { :; }

payload="$(cat 2>/dev/null || true)"
[ -n "$payload" ] || exit 0

# Cheap prefilter: only a gh command or a GitHub tool can post a body.
case "$payload" in
  *gh*|*github*|*GitHub*) ;;
  *) exit 0 ;;
esac

runtime="${GITHUB_HARDWRAP_RUNTIME:-}"
if [ -z "$runtime" ]; then
  case "$HOOK_DIR" in
    */.codex/*) runtime=codex ;;
    */.gemini/*) runtime=gemini ;;
    */.cursor/*) runtime=cursor ;;
    */.config/opencode/*) runtime=opencode ;;
    *) runtime=claude ;;
  esac
fi

result="$(printf '%s' "$payload" | python3 "$HOOK_DIR/lib/prose-detect.py" github-hardwrap-fix 2>/dev/null || true)"
[ -n "$result" ] || exit 0
# The rewrite, in the shape the runtime documents. claude, codex and the
# OpenCode bridge (which applies updatedInput to output.args) read
# hookSpecificOutput.updatedInput with permissionDecision allow; Gemini CLI
# merges hookSpecificOutput.tool_input into the call; Cursor's preToolUse
# reads updated_input with permission allow.
allow="$(printf '%s' "$result" | python3 -c '
import json, sys
r = json.loads(sys.stdin.read())
fixed = r.get("tool_input")
if fixed is None:
    sys.exit(1)
note = "Removed hard wraps from the GitHub body (rules/no-hardwrapped-github-comments.md)."
runtime = sys.argv[1]
if runtime == "gemini":
    out = {"decision": "allow", "hookSpecificOutput": {"hookEventName": "BeforeTool", "tool_input": fixed}}
elif runtime == "cursor":
    out = {"permission": "allow", "updated_input": fixed}
else:
    out = {"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "permissionDecisionReason": note,
        "updatedInput": fixed,
    }}
print(json.dumps(out))
' "$runtime" 2>/dev/null)" && {
  reason="$(printf '%s' "$result" | python3 -c 'import json,sys;print(json.loads(sys.stdin.read())["reason"])' 2>/dev/null || true)"
  # Not a guard event: guard-events records denies, which the budget
  # counters read as a call that never ran, and this call runs.
  log_warn "github-hardwrap-guard: reflowed post on $runtime (wrapped: $reason)"
  printf '%s\n' "$allow"
  exit 0
}
reason="$(printf '%s' "$result" | python3 -c 'import json,sys;print(json.loads(sys.stdin.read())["reason"])' 2>/dev/null || true)"
[ -n "$reason" ] || exit 0

msg="Hard-wrapped prose in a GitHub comment or body (line starting \"$reason\"). rules/no-hardwrapped-github-comments.md: write each paragraph and list item on one line; GitHub soft-wraps it. Remove the wraps and post again: write the body to a file, run python3 $HOOK_DIR/lib/prose-detect.py unwrap <file> to reflow it in place, and pass it with --body-file <file>. Code fences, tables, headings, quotes, separate list items and HTML lines are kept as they are. Set ALLOW_HARDWRAP=1 only to quote source text verbatim."

log_warn "github-hardwrap-guard: denied post (wrapped: $reason)"
guard_log_event github-hardwrap-guard no-hardwrapped-github-comments deny "wrapped: $reason" "$payload"
printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":%s}}\n' \
  "$(printf '%s' "$msg" | python3 -c 'import json,sys;print(json.dumps(sys.stdin.read()))')"
exit 0
