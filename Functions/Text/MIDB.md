---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Text Manipulation
use-case:
  - Double-Byte Field Limits
  - Japanese Label Formatting
related:
  - LEFTB
  - LENB
  - MID
  - REPLACEB
  - RIGHTB
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/mid-function
  - https://support.google.com/docs/answer/9367691
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Byte Substring
  - Middle Bytes
tags:
  - byte-count
  - double-byte
  - excel
  - sheets
  - text
---

# MIDB

## Description

**MIDB** returns a set number of bytes from the middle of a text string, starting at a given character. It works like MID, except that the length is counted in bytes rather than characters. For single-byte characters, such as English letters, digits and common punctuation, one character is one byte, so MIDB and MID return the same result.

Double-byte languages such as Japanese, Chinese and Korean store many characters in two bytes. When a field has a byte limit, such as a label, a fixed-width export or a database column, MIDB cuts the text to fit that limit. MID would cut by character and could produce a value that is too long for the field.

Microsoft lists MIDB as deprecated, and its help page does not describe how to choose a double-byte locale. Google Sheets documents MIDB as a working function. For new work, check the output in the target system before you rely on it, and use MID when the field limit is measured in characters.

## Syntax

```excel
=MIDB(text, start_num, num_bytes)
```

<!-- Image 1: MIDB Byte Counting. See Images/Text/MIDB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to read from. Enter it in quotation marks, reference a cell, or use a formula that returns text. |
| `start_num` | Yes | The character position where extraction begins. Position 1 is the first character, and the value must be 1 or greater. |
| `num_bytes` | Yes | The number of bytes to return. The value must be 0 or greater. |

### Return Value

A text string that holds up to `num_bytes` bytes, beginning at the character position `start_num`. The result is text. When the byte count ends in the middle of a double-byte character, the result depends on the platform, so choose a byte count that falls on a character boundary.

## Examples

### Example 1: Single-Byte Text Matches MID

```excel
=MIDB("ABCDEFG", 3, 2)
```

**Result:** `CD`

Every letter here takes one byte, so MIDB counts two bytes from position 3 and returns the same value as MID.

### Example 2: Comparing MID and MIDB on Kanji

```excel
=MID("東京都庁舎", 2, 4)
```

**Result:** `京都庁舎`

```excel
=MIDB("東京都庁舎", 2, 4)
```

**Result:** `京都`

MID returns four characters from position 2. MIDB starts at the same character but stops after four bytes. Each kanji takes two bytes, so only two kanji fit.

<!-- Image 2: Character Count Versus Byte Count. See Images/Text/MIDB.md -->

### Example 3: Measuring the Bytes First

```excel
=LENB("東京都庁舎")
```

**Result:** `10`

Five kanji at two bytes each make 10 bytes. Check the byte count with LENB before choosing the length for MIDB.

### Example 4: Cutting at a Byte Limit

```excel
=MIDB("ABC東京", 4, 4)
```

**Result:** `東京`

Position 4 is the first kanji, and the two kanji take four bytes together, so MIDB returns both of them.

## Story Problems

### Problem 1: Checking Product Names Against a Label Limit

A café prints product names on shelf labels. The label printer accepts up to 8 bytes per name when the names use double-byte characters, and each kanji or katakana character counts as two bytes.

| Product Name |
| --- |
| 抹茶ラテ |
| ミルクティー |
| Cola |
| 黒豆茶 |

**Task:** Count how many names are too long for the label.

**Solution:**

```excel
=SUMPRODUCT(--(LENB(A2:A5)>8))
```

**Answer:** `1`. 抹茶ラテ takes exactly 8 bytes and fits. ミルクティー takes 12 bytes and does not fit. Cola takes 4 bytes and 黒豆茶 takes 6 bytes.

### Problem 2: Shortening a Name to Fit the Label

The same café needs the shortened form of ミルクティー that fits in 8 bytes.

**Task:** Return the part of the name that fits in the first 8 bytes, starting at the first character.

**Solution:**

```excel
=MIDB(A2, 1, 8)
```

**Answer:** `ミルクテ`. Four katakana characters take 8 bytes, so the fifth character, ィ, is cut. The café can print the shortened name or choose a shorter product name.

## Use Cases

### Double-Byte Field Limits

**Scenario:** A Japanese order system stores the customer name in a column that accepts 20 bytes. Longer names must be shortened before they are exported.

```excel
=MIDB(A2, 1, 20)
```

**Why It Works:** The byte limit is applied directly, so the exported name never exceeds the column size. Check the cut with LENB to confirm that no character is split.

### Japanese Label Formatting

**Scenario:** A label template prints a product code, followed by a short name, in a fixed-width field.

```excel
=MIDB(B2, 1, 12)
```

**Why It Works:** MIDB keeps the label inside its byte width whether the name contains Latin letters or double-byte characters, which MID cannot guarantee.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `start_num` is less than 1. | Start at position 1 or greater. |
| `#VALUE!` | `num_bytes` is negative. | Use a zero or positive byte count, wrapped in MAX(0, ...) if it is calculated. |
| Cut character looks wrong | The byte count ends in the middle of a double-byte character. | Use LENB to find the byte count of each character and adjust the length. |
| Result is shorter than expected | The text contains double-byte characters, so fewer characters fit. | Expect fewer characters in a byte-limited field. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, deprecated | Microsoft lists MIDB as deprecated and does not describe its double-byte rules on the same page. Use MID or a newer approach in new workbooks. |
| Google Sheets | Available | Counts bytes for double-byte text. The documentation shows that each kanji in the example takes two bytes. |

## Tips and Best Practices

- Use LENB to measure a value before you cut it with MIDB.
- Test with real double-byte data, because byte rules depend on the character set.
- Keep Latin-only data on MID, since the two functions return the same result and MID is easier to read.
- Document the byte limit of each target field next to the formula that enforces it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LENB](LENB.md) | Returns the length of text in bytes, to measure before cutting. |
| [MID](MID.md) | Extracts by characters, the usual choice for character limits. |
| [LEFTB](LEFTB.md) | Returns a byte count from the start of the text. |
| [RIGHTB](RIGHTB.md) | Returns a byte count from the end of the text. |
| [REPLACEB](REPLACEB.md) | Replaces a byte count of text, for double-byte fields. |

## Official Documentation

- [Microsoft Support: MID and MIDB functions](https://support.microsoft.com/en-us/excel/functions/mid-function)
- [Google Docs Editors Help: MIDB](https://support.google.com/docs/answer/9367691)
