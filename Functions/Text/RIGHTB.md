---
domain: Spreadsheet Functions
category: Text
subcategory: Double Byte Text
purpose:
  - Text Manipulation
use-case:
  - Byte Limited Field Extracts
  - Fixed Width Record Edits
  - Japanese Customer Names
related:
  - LEFTB
  - LENB
  - MIDB
  - REPLACEB
  - RIGHT
  - SEARCHB
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/right-function
  - https://support.google.com/docs/answer/9367697
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Right Bytes
tags:
  - byte-based
  - double-byte
  - excel
  - sheets
---

# RIGHTB

## Description

**RIGHTB** returns a set number of bytes from the end of a text string. It works like [RIGHT](RIGHT.md), except that it counts bytes rather than characters. With single-byte text such as English letters and digits, RIGHTB and RIGHT return the same result. With double-byte characters, such as Japanese kanji, each character counts as two bytes, so RIGHTB returns fewer characters for the same count.

Use RIGHTB when a fixed-width file or a legacy system defines the width of a field in bytes, typically for Japanese, Chinese or Korean data. For ordinary text, RIGHT is the better choice. The Microsoft RIGHT page lists RIGHTB as deprecated, so new Excel work should use RIGHT and keep RIGHTB only for existing byte-based layouts.

If the byte count falls in the middle of a double-byte character, the page does not explain what happens. Check boundary cases on real data before relying on the result.

## Syntax

```excel
=RIGHTB(string, num_of_bytes)
```

<!-- Image 1: Byte Count From the Right. See Images/Text/RIGHTB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `string` | Yes | The text to extract from. It can be a literal string in quotes, a cell reference, or a formula that returns text. |
| `num_of_bytes` | No | The number of bytes to return from the right end. Must be zero or greater. The default is 1, and a count larger than the byte length returns the whole string. |

### Return Value

Text containing the rightmost bytes of `string`. A double-byte character is returned only when all of its bytes fit within the count.

## Examples

### Example 1: Single-Byte Text Behaves Like RIGHT

```excel
=RIGHTB("ABCDEF", 3)
```

**Result:** `DEF`

Each letter is one byte, so the three rightmost bytes are the three rightmost characters. RIGHT returns the same answer.

### Example 2: Double-Byte Characters Count as Two Bytes

```excel
=RIGHTB("東京都", 2)
```

**Result:** `都`

Each kanji takes two bytes, so two bytes are exactly one character, the last one. RIGHT with a count of 2 would return two characters, `京都`.

### Example 3: Four Bytes Hold Two Double-Byte Characters

```excel
=RIGHTB("東京都", 4)
```

**Result:** `京都`

Four bytes cover the last two kanji. This shows how the byte count, not the character count, sets the length of the result.

### Example 4: Compare With RIGHT

```excel
=RIGHT("東京都", 2)
```

**Result:** `京都`

RIGHT counts characters, so two characters are the last two kanji. Those same two kanji take four bytes, which is why RIGHTB with a count of 4 in Example 3 returns the same text.

<!-- Image 2: Byte Boundary in a Branch Code. See Images/Text/RIGHTB.md -->

## Story Problems

### Problem 1: Read a Fixed-Width Branch Code

A logistics system stores branch codes in a fixed-width field. The last four bytes of each code are the branch number. The branch names are in Japanese, so the number of characters differs from the number of bytes.

| Branch Code |
| --- |
| TK001東京都 |
| OS002大阪府 |

**Task:** Extract the last four bytes of the first branch code, and state the result.

**Solution:**

```excel
=RIGHTB(A2, 4)
```

**Answer:** `京都`. Each kanji takes two bytes, so four bytes hold the final two kanji.

### Problem 2: Confirm That ASCII Data Matches RIGHT

An analyst checks whether a column of product codes needs RIGHTB. All codes use letters and digits only.

| Product Code |
| --- |
| WX-7741 |

**Task:** Extract the last four bytes of the code.

**Solution:**

```excel
=RIGHTB(A2, 4)
```

**Answer:** `7741`. Every character is one byte, so RIGHTB returns the same result as RIGHT, and RIGHT is the simpler choice for this column.

<!-- Image 3: Fixed Width Suffix Layout. See Images/Text/RIGHTB.md -->

## Use Cases

### Byte Limited Field Extracts

**Scenario:** A legacy export reads the last ten bytes of a reference as a second key.

```excel
=RIGHTB(A2, 10)
```

**Why It Works:** The byte count matches the field definition, so the extract fits the layout the system expects. Check the result length with LENB.

### Fixed Width Record Edits

**Scenario:** A warehouse file stores a site code in the last six bytes of each record, and the code must be copied to a new column.

```excel
=RIGHTB(A2, 6)
```

**Why It Works:** The site code is always at the end of the field, so counting bytes from the right keeps the extract aligned even when the earlier fields vary.

### Name Suffixes in Byte Fields

**Scenario:** A mailing system keeps a four-byte name suffix in a fixed field, and the suffix must be copied to a separate column.

```excel
=RIGHTB(A2, 4)
```

**Why It Works:** The suffix width is set by the field definition, so counting bytes from the right returns the same portion the legacy system reads. Review names where the boundary falls inside a double-byte character.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Fewer characters than expected | Double-byte characters use two bytes each. | Use the byte count from the field definition, or use RIGHT for character counts. |
| Unexpected partial text | The byte count stops inside a double-byte character. | Adjust the count so the range ends on a character boundary, and check the boundary on sample rows. |
| Formula fails | `num_of_bytes` is negative. | Keep the count at zero or greater. |
| Deprecation warning | RIGHTB is deprecated in Excel. | Use RIGHT for new work, and keep RIGHTB only for existing byte-based files. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Deprecated | The Microsoft RIGHT page lists RIGHTB as deprecated. Use RIGHT for new work. |
| Google Sheets | Available | Counts double-byte characters as two bytes, as the page's examples show. Same argument order as Excel. |

## Tips and Best Practices

- Use RIGHTB only when the source system defines fields by bytes.
- Check the byte length of sample values with LENB before changing a full column.
- Confirm the encoding of the source file, because the byte count depends on it.
- Prefer RIGHT for English and other single-byte text.
- Test values where the byte boundary falls inside a double-byte character.

## Related Functions

| Function | Relationship |
| --- | --- |
| [RIGHT](RIGHT.md) | The character-based version and the recommended choice for ordinary text. |
| [LEFTB](LEFTB.md) | Returns bytes from the start of the text. |
| [MIDB](MIDB.md) | Returns a byte-based section from any position. |
| [LENB](LENB.md) | Counts the bytes in text, used to check field widths. |
| [REPLACEB](REPLACEB.md) | Replaces a byte-based section of text. |
| [SEARCHB](SEARCHB.md) | Finds a position counted in bytes. |

## Official Documentation

- [Microsoft Support: RIGHT function](https://support.microsoft.com/en-us/excel/functions/right-function)
- [Google Docs Editors Help: RIGHTB](https://support.google.com/docs/answer/9367697)
