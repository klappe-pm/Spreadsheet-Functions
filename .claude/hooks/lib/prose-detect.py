#!/usr/bin/env python3
"""Shared detection for the em-dash, hard-wrap and redundant-label prose rules.

Backs rules/no-em-dash.md, rules/no-hardwrapped-writing.md and
rules/no-redundant-labels.md (the redundant-label check runs only in the
PreToolUse guard). The forbidden-dash rule and the
no-hard-wrap rule are absolute, and this module is the single detection
implementation behind both enforcement points:

  * the PreToolUse guard hooks/prose-guard.sh, which stops a violation
    authored through Claude Code before the write lands, and
  * the git pre-commit backstop scripts/git-hooks/check-staged-prose.sh,
    which catches a violation staged directly with plain git (bypassing
    Claude Code) at commit time.

Keeping one detector means the two paths can never drift.

Public functions:
  detect_emdash(text) -> str    reason ("em-dash" / "en-dash-connector") or ""
  detect_hardwrap(text) -> str  offending line snippet or ""
  detect_hardwrap_in_context(before, text) -> str
                                same, with fence, Templater, and frontmatter
                                state carried over from the file text that
                                precedes the edit
  hardwrap_reason_for_payload(payload) -> str
                                the hook path: reads a PreToolUse Write or
                                Edit payload and scans the authored text in
                                the context of the target file
  detect_labels(text) -> str    a table cell or list item that opens with a
                                label repeating its column header or heading
  labels_reason_for_payload(payload) -> str
                                the same, for a PreToolUse payload in context

CLI: prose-detect.py emdash|hardwrap|labels   reads text on stdin, prints the
reason (one line) when a violation is found, prints nothing when clean, always
exits 0. prose-detect.py hardwrap-payload|labels-payload reads the PreToolUse
JSON payload on stdin instead of bare text. A nonzero exit signals a usage error, never a detection
result, so callers distinguish "clean" from "broke" by output, not exit status.

Determinism: pure Python stdlib, no network, no model calls.
"""

import json
import os
import re
import sys

# Em-dash (U+2014) and horizontal bar (U+2015) are forbidden unconditionally.
# En-dash (U+2013) is forbidden only as a connector (a space on either side);
# a bare numeric range such as "2" U+2013 "3" is allowed. The glyphs are built
# from codepoints with chr() so this source stays pure ASCII and carries no
# literal forbidden dash for its own guard to trip on.
_EMDASH = chr(0x2014)
_HBAR = chr(0x2015)
_ENDASH = chr(0x2013)
_ENDASH_CONNECTOR = re.compile("(?:\\s" + _ENDASH + "|" + _ENDASH + "\\s)")


def _strip_code(text):
    """Remove fenced blocks and inline code spans, leaving the prose.

    rules/no-em-dash.md ends with "Quote source text that contains dashes
    verbatim only inside a code fence", which grants an exemption the detector
    never implemented: it tested the raw string, so a dash inside a fence or a
    backtick span was flagged exactly like one in a sentence. That made the
    documented escape hatch unusable and left ALLOW_EMDASH, a bypass needing
    approval, as the only way to record a literal. A product watermark string
    and a vendored code sample both hit it.

    Code is not prose. The dash rule is about punctuation an author chose, not
    about bytes inside a quotation, so both block fences and inline spans are
    removed before the scan.
    """
    out = []
    in_fence = None
    for line in text.split("\n"):
        fence = _FENCE_RE.match(line)
        if in_fence:
            marker, width = in_fence
            stripped = line.strip()
            if len(stripped) >= width and set(stripped) == {marker}:
                in_fence = None
            continue
        if fence:
            token = fence.group(1)
            in_fence = (token[0], len(token))
            continue
        out.append(_INLINE_CODE_RE.sub(" ", line))
    return "\n".join(out)


def _strip_frontmatter(text):
    """Remove a leading YAML frontmatter block (--- ... ---), if present.

    detect_hardwrap already treats frontmatter as not prose (_scan skips it
    the same way below); detect_emdash never did, so a title or alias quoted
    verbatim into a frontmatter field, such as the one make_title in
    hooks/lib/prompt-capture.py writes into aliases:, could still trip the
    rule even though rules/no-em-dash.md is about punctuation an author
    chose in prose, not a value carried into a structured metadata field
    (docs/bugs/prompt-capture-notes-fail-the-prose-gate-on-a-dashed-title.md).
    Mirrors _scan's own frontmatter skip: an unterminated opening fence
    leaves nothing after it to scan, exactly as it does there.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return text
    i = 1
    n = len(lines)
    while i < n and lines[i].strip() != "---":
        i += 1
    return "\n".join(lines[i + 1 :])


def detect_emdash(text):
    """Return a reason string if text carries a forbidden dash, else ""."""
    if not text:
        return ""
    prose = _strip_code(_strip_frontmatter(text))
    if _EMDASH in prose or _HBAR in prose:
        return "em-dash"
    if _ENDASH_CONNECTOR.search(prose):
        return "en-dash-connector"
    return ""


_FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
# An inline code span: a run of backticks, content, a closing run. Used by
# _strip_code to lift quoted literals out before the dash scan.
_INLINE_CODE_RE = re.compile(r"`+[^`]*`+")
# Obsidian Templater delimiters. A Templater template is a *.md note whose
# <% ... %> blocks hold JavaScript, so its body is code that happens to live in
# a Markdown file. Ordinary source is nothing but adjacent non-blank lines, so
# without this the hard-wrap detector rejects every possible Templater script.
# Treated exactly like a fenced code block: contents skipped, boundaries reset
# the paragraph. Prose outside the block is still checked normally.
_TEMPLATER_OPEN_RE = re.compile(r"<%")
_TEMPLATER_CLOSE_RE = re.compile(r"%>")
_HEADING_RE = re.compile(r"^#{1,6}\s")
_TABLE_RE = re.compile(r"^\s*\|")
_HR_RE = re.compile(r"^\s*(-{3,}|\*{3,})\s*$")
_QUOTE_RE = re.compile(r"^\s*>")
# A line that opens with an HTML tag or comment, structural in a GitHub body.
_HTML_LINE_RE = re.compile(r"^\s*<(?:/?[A-Za-z][A-Za-z0-9-]*[\s>/]|!--)")
# Display math. `$$` alone on a line opens or closes a block; `$$ ... $$` on one
# line is a complete equation and opens nothing. Mathematics is not prose, so
# neither form may be read as a wrapped paragraph: without this the equation row
# of a multi-line block looks like a lazy continuation of the `$$` above it, and
# the guard denies a write that follows the vault's own documented note schema.
_MATH_DELIM_RE = re.compile(r"^\s*\$\$\s*$")
_MATH_INLINE_RE = re.compile(r"^\s*\$\$.+\$\$\s*$", re.S)
_LIST_RE = re.compile(r"^(\s*)([-*+]|\d+\.)\s+\S")
# A bold field label opening a line: "**Delivered:** ...". The handoff format
# rules/session-handoff-on-pr.md mandates is one such field per line, and like
# a list item each one opens its own logical line. Review cluster F2: the scan
# read the second field as a lazy continuation of the first and denied the
# mandated format. The label must close with a colon inside the bold run, so
# "**Bold** words" followed by a wrapped line is still a wrap.
_FIELD_RE = re.compile(r"^\s*\*\*[^*\n]+:\*\*(?:\s|$)")
# An intentional line break: two trailing spaces or a trailing backslash.
# rules/no-hardwrapped-writing.md names these as permitted structure, alongside
# headings and table rows, but the scan below never implemented the exemption,
# so it rejected the one break the rule explicitly allows. A line carrying one
# ends its own logical line, exactly as a blank line or a heading does; the
# following line therefore begins a new one and is not a lazy continuation.
_HARD_BREAK_RE = re.compile(r"(  |\\)$")

# A YAML mapping key, at column 0 or indented under a parent key: "status: ACCEPTED",
# "tags:", "id: x", "  enforced-by: x". Deliberately strict (kebab/snake key, colon
# then space or end of line) so ordinary prose that merely contains a colon
# mid-sentence does not match; leading whitespace is allowed so a nested key
# (e.g. metadata.enforced-by) is still recognized as frontmatter.
_YAML_KEY_RE = re.compile(r"^\s*[A-Za-z_][A-Za-z0-9_-]*:(?:\s|$)")
# A block-sequence item under a YAML key ("  - value").
_YAML_SEQ_RE = re.compile(r"^\s+-\s+\S")


def _is_frontmatter_fragment(lines):
    """True when every non-blank line is a YAML mapping key or sequence item.

    An Edit passes only its ``new_string``, so a frontmatter edit arrives as a
    bare fragment that never starts with the ``---`` fence the whole-file skip
    below looks for. Its adjacent ``key: value`` lines then read as a
    hard-wrapped paragraph and the write is denied, which is wrong: YAML
    frontmatter is not prose and is *required* to put one key per line.

    The all-lines-match test is what keeps this from blinding the detector. A
    genuinely hard-wrapped paragraph carries at least one continuation line
    that is not a mapping key, so a mixed fragment still falls through to the
    normal scan below.
    """
    seen = False
    for line in lines:
        if line.strip() == "":
            continue
        seen = True
        if not (_YAML_KEY_RE.match(line) or _YAML_SEQ_RE.match(line)):
            return False
    return seen


def detect_hardwrap(text):
    """Return the offending line snippet if text hard-wraps a paragraph or
    list item across more than one physical line, else "".

    Two adjacent non-blank lines that are neither structural (heading, table
    row, horizontal rule, blockquote) nor the start of a new list item are
    the same CommonMark paragraph (lazy continuation) or the same list-item
    continuation, which the rule always forbids regardless of column width.
    Lines inside fenced code blocks are skipped, as is leading frontmatter.
    """
    if not text:
        return ""
    return _scan(text.split("\n"), first_reportable=1, fragment_check=True)


def detect_hardwrap_in_context(before, text):
    """Scan text as it will sit in its file, with the file text before it as context.

    An Edit's new_string is a fragment. Scanned alone, a fragment that starts
    inside a fenced code block (its opener lies before the edit) reads as
    adjacent prose lines and is denied, which is wrong. Prepending the file
    text before the edit lets fence, Templater, and frontmatter state carry
    over. Only a wrap the new text itself creates is reported: a wrap between
    two lines that both lie inside the new text. A pre-existing wrap in the
    context, or one across the join with the old text, is not the author's.
    """
    if not text:
        return ""
    if not before:
        return detect_hardwrap(text)
    return _scan(
        (before + text).split("\n"),
        first_reportable=before.count("\n") + 1,
        fragment_check=False,
    )


def hardwrap_reason_for_payload(payload):
    """Return the hard-wrap reason for a PreToolUse Write or Edit payload, else "".

    Write content is a whole file and is scanned as is. An Edit's new_string
    is scanned in the context of the target file's text before old_string,
    when the file exists and old_string is found in it; otherwise it is
    scanned alone, which is the behaviour for a new file.
    """
    authored = _payload_text(payload)
    if authored is None:
        return ""
    before, text, whole = authored
    if whole:
        return detect_hardwrap(text)
    return detect_hardwrap_in_context(before, text)


def detect_github_hardwrap(text):
    """detect_hardwrap for a GitHub body, where an HTML line is structural."""
    if not text:
        return ""
    return _scan(text.split("\n"), first_reportable=1, fragment_check=False, html=True)


def unwrap_hardwrap(text, html=True):
    """Return text with every hard-wrapped paragraph and list item joined
    onto one line. The same classification as detect_hardwrap decides what
    is a wrap, so code fences, tables, headings, quotes, separate list items
    and intentional breaks are left as they are."""
    if not text:
        return text
    lines = text.split("\n")
    joins = []
    _scan(lines, first_reportable=1, fragment_check=False, joins=joins, html=html)
    joined = set(joins)
    out = []
    for index, line in enumerate(lines):
        if index in joined and out:
            out[-1] = out[-1].rstrip() + " " + line.strip()
        else:
            out.append(line)
    return "\n".join(out)


def _load_attribution():
    """attribution-detect.py, whose gh parser finds what a command posts."""
    import importlib.util

    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "attribution-detect.py"
    )
    spec = importlib.util.spec_from_file_location("attribution_detect", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def github_hardwrap_reason_for_payload(payload):
    """Return the hard-wrap reason for a body a PreToolUse payload posts to
    GitHub (a comment, review, pull request or issue body, release notes),
    else "". The bodies come from attribution-detect.github_bodies."""
    try:
        bodies = _load_attribution().github_bodies(payload)
    except Exception:
        return ""
    for body in bodies:
        reason = detect_github_hardwrap(body)
        if reason:
            return reason
    return ""


def _unwrap_json_bodies(value, fields):
    """value with every string under a body-shaped key reflowed, at any depth."""
    if isinstance(value, dict):
        return {
            key: unwrap_hardwrap(item)
            if key in fields and isinstance(item, str)
            else _unwrap_json_bodies(item, fields)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_unwrap_json_bodies(item, fields) for item in value]
    return value


def _fix_body_file(path, kind, body, fields):
    """Reflow body in the file it was read from, when the file on disk still
    holds it. True when the file was rewritten."""
    try:
        with open(path, encoding="utf-8") as handle:
            original = handle.read()
    except (OSError, UnicodeDecodeError):
        return False
    if kind == "json":
        try:
            decoded = json.loads(original)
        except ValueError:
            return False
        if (
            body not in json.dumps(decoded, ensure_ascii=False)
            and json.dumps(body)[1:-1] not in original
        ):
            return False
        reflowed = (
            json.dumps(
                _unwrap_json_bodies(decoded, fields), ensure_ascii=False, indent=2
            )
            + "\n"
        )
    else:
        if body.strip("\n") not in original:
            return False
        reflowed = unwrap_hardwrap(original)
    if reflowed != original:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(reflowed)
    return True


def _replace_literal(command, body):
    """command with body reflowed where it is written verbatim: as itself
    (single quotes, a quoted heredoc, plain double quotes) or JSON escaped.
    None when it is written in neither form."""
    for form in (body, body.strip("\n")):
        if "\n" in form and form in command:
            return command.replace(form, unwrap_hardwrap(form))
    escaped = json.dumps(body)[1:-1]
    if "\\n" in escaped and escaped in command:
        return command.replace(escaped, json.dumps(unwrap_hardwrap(body))[1:-1])
    return None


def github_hardwrap_fix_for_payload(payload):
    """Reflow every wrapped GitHub body a PreToolUse payload posts.

    Returns (reason, tool_input): reason is the wrap that was found ("" when
    the payload is clean), and tool_input is the input to run instead, or
    None when some wrapped body could not be reflowed where it lives, in
    which case the caller denies. A body read from a file still holding it
    is reflowed in that file; a body written in the command is reflowed in
    the command text; a GitHub tool's body fields are reflowed in place. The
    result is judged again, so a fix that leaves a wrap is never returned.
    """
    reason = github_hardwrap_reason_for_payload(payload)
    if not reason:
        return "", None
    attribution = _load_attribution()
    fields = attribution._GH_API_BODY_FIELDS
    tool_input = dict(payload.get("tool_input") or {})
    if payload.get("tool_name") not in attribution.SHELL_TOOLS:
        tool_input = _unwrap_json_bodies(
            tool_input, attribution._GITHUB_TOOL_BODY_FIELDS
        )
    else:
        command = tool_input.get("command") or ""
        for body, source in attribution.github_body_sources(payload):
            if not detect_github_hardwrap(body):
                continue
            if source is not None and _fix_body_file(
                source[0], source[1], body, fields
            ):
                continue
            replaced = _replace_literal(command, body)
            if replaced is None:
                return reason, None
            command = replaced
        tool_input["command"] = command
    if github_hardwrap_reason_for_payload({**payload, "tool_input": tool_input}):
        return reason, None
    return reason, tool_input


def labels_reason_for_payload(payload):
    """Return the redundant-label reason for a PreToolUse Write or Edit payload, else "".

    Same context rule as the hard-wrap path: an Edit fragment is read after
    the target file's text before old_string, so the heading or table header
    it sits under is known, and only a line the fragment itself adds is
    reported.
    """
    authored = _payload_text(payload)
    if authored is None:
        return ""
    before, text, _whole = authored
    return detect_labels_in_context(before, text)


def _payload_text(payload):
    """(before, text, whole) for a Write or Edit payload, or None when it carries no text.

    whole is True for Write content, which is a complete file with no context.
    """
    tool_input = payload.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        return None
    content = tool_input.get("content")
    if isinstance(content, str):
        return ("", content, True)
    new_string = tool_input.get("new_string")
    if not isinstance(new_string, str):
        return None
    before = ""
    old_string = tool_input.get("old_string")
    file_path = tool_input.get("file_path")
    if (
        isinstance(old_string, str)
        and old_string
        and isinstance(file_path, str)
        and file_path
    ):
        try:
            with open(file_path, encoding="utf-8") as handle:
                existing = handle.read()
        except (OSError, UnicodeDecodeError):
            existing = ""
        index = existing.find(old_string)
        if index >= 0:
            before = existing[:index]
    return (before, new_string, False)


# rules/no-redundant-labels.md. A label is a short run of words that opens a
# table cell or list item and ends in a colon, bold or not: "Gap:", "**Gap:**".
# It must start with a letter, so a time such as "10:30" is not a label.
_LABEL_RE = re.compile(
    r"^(?:\*\*|__)?([A-Za-z][A-Za-z0-9 '&/]{0,60}?)(?:\*\*|__)?\s*:(?:\*\*|__)?(?:\s|$)"
)
_ITEM_TEXT_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+(.*)$")
_HEADING_TEXT_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
_CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")


def _words(text):
    """Lowercase alphanumeric words, punctuation and kebab hyphens ignored."""
    return re.findall(r"[a-z0-9]+", text.lower())


# A header or heading that joins several things ("inputs-and-outputs",
# "evidence or gap") names alternatives; a label under it says which one
# applies, so it carries information and is not redundant.
_CONJUNCTIONS = {"and", "or", "vs", "versus", "plus"}


def _names_alternatives(words):
    return any(word in _CONJUNCTIONS for word in words)


def _singular(word):
    return (
        word[:-1]
        if len(word) > 3 and word.endswith("s") and not word.endswith("ss")
        else word
    )


def _cells(row):
    """The cells of a pipe-table row, outer pipes removed."""
    inner = row.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|") and not inner.endswith("\\|"):
        inner = inner[:-1]
    return [cell.strip() for cell in _CELL_SPLIT_RE.split(inner)]


def _is_table_rule(line):
    stripped = line.strip()
    return "-" in stripped and set(stripped) <= set("|-: ")


def _cell_repeats_header(cell, header):
    """The cell opens with a label equal to or a prefix of its column header."""
    match = _LABEL_RE.match(cell)
    if not match:
        return False
    label = " ".join(_words(match.group(1)))
    head = " ".join(_words(header))
    if len(label) < 3 or not head or _names_alternatives(head.split()):
        return False
    singular_label = " ".join(_singular(w) for w in label.split())
    singular_head = " ".join(_singular(w) for w in head.split())
    return head.startswith(label) or singular_head.startswith(singular_label)


def _item_label(item):
    """The label an item opens with, as singular words, or None."""
    match = _LABEL_RE.match(item)
    if not match:
        return None
    label = [_singular(w) for w in _words(match.group(1))]
    return label or None


def _repeats_heading(label, heading_words):
    """The label is the heading's noun: its last word or words."""
    if not label or not heading_words or _names_alternatives(heading_words):
        return False
    return heading_words[-len(label) :] == label


def detect_labels(text):
    """Return the offending line if a cell or item repeats its header or heading as a label, else ""."""
    if not text:
        return ""
    return _scan_labels(text.split("\n"), first_reportable=0)


def detect_labels_in_context(before, text):
    """Scan text after the file text that precedes it; report only lines text adds."""
    if not text:
        return ""
    if not before:
        return detect_labels(text)
    return _scan_labels(
        (before + text).split("\n"), first_reportable=before.count("\n")
    )


def _list_run_reason(run, heading_words, first_reportable):
    """The first item in a list run that repeats the heading, unless the run is a record of fields.

    run holds (index, line, label) for each item. When any item carries a
    label other than the heading's noun, the labels name fields of a record
    ("Pattern:", "Evidence:", "Impact:") and none of them is redundant.
    """
    labels = [label for _index, _line, label in run if label]
    if any(not _repeats_heading(label, heading_words) for label in labels):
        return ""
    for index, line, label in run:
        if (
            label
            and index >= first_reportable
            and _repeats_heading(label, heading_words)
        ):
            return line.strip()[:70]
    return ""


def _scan_labels(lines, first_reportable):
    """Track the nearest section heading and the current table header; report the first redundant label."""
    n = len(lines)
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < n and lines[i].strip() != "---":
            i += 1
        i += 1
    in_fence = None
    heading_words = []
    header = None  # column headers of the table being read, or None outside a table
    run = []  # (index, line, label) for the list being read; blank lines do not end it

    def close_run():
        reason = _list_run_reason(run, heading_words, first_reportable)
        run.clear()
        return reason

    while i < n:
        index = i
        line = lines[i]
        i += 1
        fence = _FENCE_RE.match(line)
        if in_fence:
            marker, width = in_fence
            stripped = line.strip()
            if len(stripped) >= width and set(stripped) == {marker}:
                in_fence = None
            continue
        item = None if fence else _ITEM_TEXT_RE.match(line)
        if item:
            run.append((index, line, _item_label(item.group(1))))
            header = None
            continue
        if line.strip() == "":
            continue
        reason = close_run()
        if reason:
            return reason
        if fence:
            token = fence.group(1)
            in_fence = (token[0], len(token))
            header = None
            continue
        heading = _HEADING_TEXT_RE.match(line)
        if heading:
            # The H1 is the file title; only a section heading governs the items under it.
            heading_words = (
                []
                if line.startswith("# ")
                else [_singular(w) for w in _words(heading.group(1))]
            )
            header = None
            continue
        if _TABLE_RE.match(line):
            if header is None:
                following = lines[i] if i < n else ""
                if _is_table_rule(following):
                    header = _cells(line)
                    i += 1
                continue
            if index >= first_reportable:
                for column, cell in enumerate(_cells(line)):
                    if column < len(header) and _cell_repeats_header(
                        cell, header[column]
                    ):
                        return line.strip()[:70]
            continue
        header = None
    return close_run()


def _scan(lines, first_reportable, fragment_check, joins=None, html=False):
    """Run the hard-wrap state machine over lines.

    first_reportable is the smallest line index (0-based) at which a wrap may
    be reported; a wrap is reported at the second of its two lines. With
    fragment_check the pure-YAML-fragment exemption applies, which is only
    right when the lines are a bare Edit fragment with no file context.
    With joins (a list), every wrapped line's index is appended to it and
    the scan runs to the end instead of stopping at the first, which is how
    unwrap_hardwrap reflows text with the same classification. With html, a
    line that opens with a tag (<details>, <summary>, <img>) is structural,
    as GitHub renders it.
    """
    n = len(lines)
    i = 0

    # A pure YAML frontmatter fragment (an Edit's new_string) is not prose.
    if fragment_check and _is_frontmatter_fragment(lines):
        return ""

    # Frontmatter (--- ... ---) is not prose; skip it if present at the top.
    if lines and lines[0].strip() == "---":
        i = 1
        while i < n and lines[i].strip() != "---":
            i += 1
        i += 1

    in_fence = None
    in_templater = False
    in_math = False
    prev = None  # previous non-structural line, or None at a structural/blank boundary

    while i < n:
        line = lines[i]
        i += 1

        if in_templater:
            # Inside a Templater block: skip the code, close on the delimiter.
            if _TEMPLATER_CLOSE_RE.search(line):
                in_templater = False
            prev = None
            continue
        fence = _FENCE_RE.match(line)
        if in_fence:
            marker, width = in_fence
            stripped = line.strip()
            if len(stripped) >= width and set(stripped) == {marker}:
                in_fence = None
            prev = None
            continue
        if fence:
            token = fence.group(1)
            in_fence = (token[0], len(token))
            prev = None
            continue
        if in_math:
            # Inside a display equation: the body is mathematics, not prose.
            if _MATH_DELIM_RE.match(line):
                in_math = False
            prev = None
            continue
        if _MATH_INLINE_RE.match(line):
            # A complete single-line equation. Structural, opens no block.
            prev = None
            continue
        if _MATH_DELIM_RE.match(line):
            in_math = True
            prev = None
            continue
        if _TEMPLATER_OPEN_RE.search(line):
            # An inline <% ... %> closes on its own line and opens no block.
            open_at = line.index("<%")
            if not _TEMPLATER_CLOSE_RE.search(line, open_at):
                in_templater = True
            prev = None
            continue
        if line.strip() == "":
            prev = None
            continue
        if (
            _HEADING_RE.match(line)
            or _TABLE_RE.match(line)
            or _HR_RE.match(line)
            or _QUOTE_RE.match(line)
            or (html and _HTML_LINE_RE.match(line))
        ):
            prev = None
            continue

        is_new_item = bool(_LIST_RE.match(line) or _FIELD_RE.match(line))
        if prev is not None and not is_new_item and i - 1 >= first_reportable:
            if joins is None:
                return line.strip()[:70]
            joins.append(i - 1)
        # A line ending in an intentional break closes its own logical line, so
        # the next line starts a new one rather than continuing this one.
        prev = None if _HARD_BREAK_RE.search(line) else line

    return ""


def _main(argv):
    mode = argv[1] if len(argv) > 1 else ""
    modes = (
        "emdash",
        "hardwrap",
        "hardwrap-payload",
        "labels",
        "labels-payload",
        "github-hardwrap-payload",
        "github-hardwrap-fix",
        "unwrap",
    )
    if mode not in modes:
        sys.stderr.write("usage: prose-detect.py " + "|".join(modes) + " [file]\n")
        return 64
    if mode == "unwrap":
        # Reflow in place when a file is named, else stdin to stdout.
        if len(argv) > 2:
            with open(argv[2], encoding="utf-8") as handle:
                original = handle.read()
            reflowed = unwrap_hardwrap(original)
            if reflowed != original:
                with open(argv[2], "w", encoding="utf-8") as handle:
                    handle.write(reflowed)
            return 0
        sys.stdout.write(
            unwrap_hardwrap(sys.stdin.buffer.read().decode("utf-8", errors="replace"))
        )
        return 0
    # Bytes in. A text-mode stdin raised UnicodeDecodeError on a non-UTF-8
    # Markdown file, and the staged prose gate read that crash as a clean file
    # (review cluster F2). Undecodable bytes become U+FFFD, which is neither a
    # dash nor a line break, so every rule still judges the rest of the text.
    text = sys.stdin.buffer.read().decode("utf-8", errors="replace")
    if mode == "emdash":
        reason = detect_emdash(text)
    elif mode == "hardwrap":
        reason = detect_hardwrap(text)
    elif mode == "labels":
        reason = detect_labels(text)
    else:
        try:
            payload = json.loads(text or "{}")
        except ValueError:
            payload = {}
        payload = payload if isinstance(payload, dict) else {}
        if mode == "labels-payload":
            reason = labels_reason_for_payload(payload)
        elif mode == "github-hardwrap-payload":
            reason = github_hardwrap_reason_for_payload(payload)
        elif mode == "github-hardwrap-fix":
            # One JSON line: the wrap found and the input to run instead
            # (null when it cannot be fixed); nothing when the payload is clean.
            try:
                reason, fixed = github_hardwrap_fix_for_payload(payload)
            except Exception:
                reason, fixed = github_hardwrap_reason_for_payload(payload), None
            if reason:
                print(json.dumps({"reason": reason, "tool_input": fixed}))
            return 0
        else:
            reason = hardwrap_reason_for_payload(payload)
    if reason:
        print(reason)
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv))
