---
domain: Spreadsheet Functions
category: Text
subcategory: Double Byte Text
purpose:
  - Data Retrieval
  - Text Manipulation
use-case:
  - Byte Limited Field Parsing
  - Japanese Branch Names
  - Route Code Positions
related:
  - FINDB
  - LENB
  - MIDB
  - REPLACEB
  - RIGHTB
  - SEARCH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/search-function
  - https://support.google.com/docs/answer/3295923
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Search Bytes
tags:
  - byte-based
  - double-byte
  - excel
  - sheets
---

# SEARCHB

## Description

**SEARCHB** returns the position of one piece of text inside another, but it counts positions in bytes rather than characters. Each double-byte character, such as a Japanese, Chinese or Korean character, takes two bytes. The position of a character that follows a double-byte character is therefore larger than its character position. For single-byte text, SEARCHB and [SEARCH](SEARCH.md) return the same position.

SEARCHB ignores letter case, like SEARCH. Use it when a legacy file or a fixed-width layout defines fields by byte position. For ordinary text, SEARCH is simpler and easier to read.

The Google Sheets page recommends SEARCH for standard character sets and SEARCHB for double-byte sets. The Microsoft SEARCH page lists SEARCHB as deprecated, so Excel users should plan to move byte-based formulas to another approach before they are rebuilt.

## Syntax

```excel
=SEARCHB(search_for, text_to_search, [starting_at])
```

<!-- Image 1: Byte Positions Versus Character Positions. See Images/Text/SEARCHB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `search_for` | Yes | The text to locate inside `text_to_search`. |
| `text_to_search` | Yes | The text in which to look for `search_for`. |
| `starting_at` | No | The byte position where the search begins. The default is 1. |

### Return Value

A number giving the byte position where `search_for` first appears in `text_to_search`. If there is no match, the result is `#VALUE!`.

## Examples

### Example 1: Single-Byte Text Matches SEARCH

```excel
=SEARCHB("b", "abc")
```

**Result:** `2`

Each letter is one byte, so the byte position matches the character position. SEARCH returns the same value for this text.

### Example 2: Double-Byte Characters Shift the Position

```excel
=SEARCHB("本", "大阪本社")
```

**Result:** `5`

The two kanji 大 and 阪 take four bytes together, so 本 begins at byte 5. SEARCH returns position 3 for the same text because it counts characters.

### Example 3: Find a Character After Double-Byte Text

```excel
=SEARCHB("社", "大阪本社")
```

**Result:** `7`

The three kanji before 社 take six bytes, so 社 starts at byte 7.

### Example 4: Search From a Byte Position

```excel
=SEARCHB("Route", "Route B-12 Route C-4", 7)
```

**Result:** `12`

The search starts at byte 7 and skips the first `Route`. The second occurrence begins at byte 12 because all of the text is single-byte.

<!-- Image 2: Double-Byte Position Comparison. See Images/Text/SEARCHB.md -->

## Story Problems

### Problem 1: Locate a Branch Marker in a Fixed-Width Name

A logistics system stores branch names in a fixed-width field, and the field layout counts bytes. The branch type marker 本 marks the head office. The team needs its byte position to cut the field.

| Branch Name |
| --- |
| 東京本部 |

**Task:** Find the byte position of 本 in the first branch name, and state the position that SEARCH would return.

**Solution:**

```excel
=SEARCHB("本", A2)
```

**Answer:** `5`. Each of the two kanji before 本 takes two bytes, so 本 begins at byte 5. SEARCH would return `3` for the same text.

### Problem 2: Confirm That ASCII Text Behaves Like SEARCH

An analyst checks a column of route codes that use only English letters, digits and symbols. The question is whether SEARCHB needs to be used.

| Route Code |
| --- |
| Route B-12 |

**Task:** Find the position of the letter `B` in the route code.

**Solution:**

```excel
=SEARCHB("B", A2)
```

**Answer:** `7`. Every character is one byte, so SEARCH would return the same value, and SEARCH is the simpler choice.

<!-- Image 3: Branch Name Byte Positions. See Images/Text/SEARCHB.md -->

## Use Cases

### Byte Limited Field Parsing

**Scenario:** A legacy export stores a reference in a field of fixed byte width. The team must find where a separator sits before splitting the reference.

```excel
=LEFTB(A2, SEARCHB("-", A2) - 1)
```

**Why It Works:** The position is counted in bytes, so it matches the field layout used by the legacy system. LEFTB then returns the bytes before the separator.

### Japanese Branch Names

**Scenario:** A regional report needs to cut each branch name before its office type marker.

```excel
=MIDB(A2, 1, SEARCHB("本", A2) - 1)
```

**Why It Works:** The byte position of 本 tells MIDB where the office type marker starts, so the branch name is cut at the right point even though kanji use two bytes.

### Route Code Positions

**Scenario:** A route code has a hyphen between the route letter and the route number, and the team needs the byte position of the hyphen for a fixed-width import.

```excel
=SEARCHB("-", A2)
```

**Why It Works:** For single-byte route codes, the byte position is the character position. Use the same formula for mixed text only after checking a sample with double-byte characters.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Position is larger than expected | Double-byte characters count as two bytes each. | Read the result as a byte position, or use SEARCH for character positions. |
| `#VALUE!` | The text is not found, or `starting_at` is out of range. | Wrap the formula in IFERROR, and check the starting position. |
| Cut in the middle of a kanji | The byte position falls inside a double-byte character. | Check the boundary on sample values and adjust the position. |
| Deprecation warning | SEARCHB is deprecated in Excel. | Use SEARCH for new work, and keep SEARCHB only for existing byte-based files. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Deprecated | The Microsoft SEARCH page lists SEARCHB as deprecated. Use SEARCH for new work. |
| Google Sheets | Available | Counts each double-byte character as two. The page recommends SEARCH for standard character sets and SEARCHB for double-byte sets. |

## Tips and Best Practices

- Use SEARCHB only when the source data or the target system counts fields in bytes.
- Check a sample of values with LENB before relying on byte positions.
- Use SEARCH for ordinary text, and convert the layout to characters before a formula is rebuilt.
- Confirm the encoding of the source file, because the byte count depends on it.
- Pair SEARCHB with LEFTB, MIDB or RIGHTB when you need to cut the text at the position it returns.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SEARCH](SEARCH.md) | The character-based version and the recommended choice for ordinary text. |
| [FINDB](FINDB.md) | The byte-based version of FIND, which is case sensitive. |
| [LENB](LENB.md) | Counts the bytes in text, used to check field widths. |
| [MIDB](MIDB.md) | Returns a byte-based section from any position. |
| [REPLACEB](REPLACEB.md) | Replaces a byte-based section, often at a position found by SEARCHB. |
| [RIGHTB](RIGHTB.md) | Returns the rightmost bytes of text. |

## Official Documentation

- [Microsoft Support: SEARCH function](https://support.microsoft.com/en-us/excel/functions/search-function)
- [Google Docs Editors Help: SEARCHB](https://support.google.com/docs/answer/3295923)
