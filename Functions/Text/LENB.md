---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Text Manipulation
use-case:
  - Double-Byte Field Limits
  - Japanese Label Formatting
related:
  - LEFTB
  - LEN
  - MIDB
  - REPLACEB
  - RIGHTB
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/len-function
  - https://support.google.com/docs/answer/9367584
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Byte Length
  - Length In Bytes
tags:
  - byte-count
  - double-byte
  - excel
  - sheets
  - text
---

# LENB

## Description

**LENB** returns the length of a text string measured in bytes instead of characters. For text made only of single-byte characters, such as English letters, digits and common punctuation, LENB returns the same number as LEN. The difference appears with double-byte characters such as Japanese kanji and kana, which take more than one byte each.

Use LENB when a field has a byte limit, such as a fixed-width export, a label template or a legacy system that stores text in a double-byte code page. LEN answers the question "how many characters," and LENB answers "how many bytes," so the two functions are used for different limits.

Microsoft lists LENB as deprecated, and its LEN help page does not describe the byte rules for LENB. Google Sheets documents LENB as a working function and shows that the kanji in its example takes two bytes each. For new work, confirm the byte count in the target system before you rely on it.

## Syntax

```excel
=LENB(text)
```

<!-- Image 1: LENB Argument Layout. See Images/Text/LENB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to measure. Enter it in quotation marks, reference a cell, or use a formula that returns text. A number is converted to text before it is measured. |

### Return Value

A whole number: the count of bytes in the text. The result is a number, so it can be used directly in comparisons and sums. An empty string returns 0.

## Examples

### Example 1: Single-Byte Text

```excel
=LENB("Hello")
```

**Result:** `5`

Each letter takes one byte, so LENB returns the same value as LEN.

### Example 2: A Two-Kanji Word

```excel
=LENB("大阪")
```

**Result:** `4`

The two kanji each take two bytes, so the total is four bytes. LEN returns 2 for the same text.

### Example 3: Mixed Latin and Kanji Text

```excel
=LENB("Tokyo 東京")
```

**Result:** `10`

`Tokyo ` takes six bytes, one for each letter and the space, and the two kanji take four bytes together.

<!-- Image 2: LEN and LENB on the Same Text. See Images/Text/LENB.md -->

### Example 4: Comparing Bytes With Characters

```excel
=LENB(A2)-LEN(A2)
```

Cell `A2` contains `大阪`.

**Result:** `2`

The difference is the number of extra bytes in the text. Each kanji adds one extra byte over its character count, so the difference is 2 for two kanji.

## Story Problems

### Problem 1: Choosing Names That Fit a Field

A Japanese shop stores product names in a point-of-sale field that accepts 12 bytes. Double-byte characters use more of the limit than Latin letters.

| Product Name |
| --- |
| 新宿駅前店 |
| Ramen 醤油 |
| Tofu |
| 東京スカイツリー店 |

**Task:** Count the names that fit within 12 bytes.

**Solution:**

```excel
=SUMPRODUCT(--(LENB(A2:A5)<=12))
```

**Answer:** `3`. 新宿駅前店 takes 10 bytes, Ramen 醤油 takes 10 bytes and Tofu takes 4 bytes. 東京スカイツリー店 takes 18 bytes and does not fit.

### Problem 2: Total Bytes for an Export

The same shop exports the four names in one file, and the export format needs the total number of bytes used by all names.

**Task:** Add the byte counts of the four names in `A2:A5`.

**Solution:**

```excel
=SUMPRODUCT(LENB(A2:A5))
```

**Answer:** `42`, because 10 + 10 + 4 + 18 = 42. Using LEN here would give a much smaller total, because it counts characters.

## Use Cases

### Double-Byte Field Limits

**Scenario:** A legacy order system accepts 30 bytes for each delivery note. Staff need a warning before they save a note that is too long.

```excel
=IF(LENB(B2)>30, "Too long", "OK")
```

**Why It Works:** LENB measures the note in the same unit the system uses. A character count would allow longer notes than the system accepts when they contain kanji.

### Japanese Label Formatting

**Scenario:** A label template prints a customer name in a field that is 16 bytes wide. The label office wants a flag on each name that will not fit.

```excel
=IF(LENB(A2)>16, "Shorten", "Fits")
```

**Why It Works:** The flag uses the byte count, so the check matches the printer's field width. Pair it with MIDB to cut names that are too long.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Count is higher than expected | Kanji and kana count as two bytes each. | Use LEN when the limit is in characters. |
| Count is the same as LEN | The text has only single-byte characters. | This is correct, so no change is needed. |
| Count differs between platforms | Each platform applies its own byte rules for double-byte text. | Test with a sample from the target system before you set a limit. |
| Count is unexpected for a number | The number is converted to text first. | Check the digits and any decimal point in the text form. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, deprecated | Microsoft lists LENB as deprecated, and its LEN help page does not describe the byte rules for LENB. Use LEN unless a legacy workbook depends on LENB. |
| Google Sheets | Available | The documentation shows that each kanji in its example takes two bytes, so LENB returns 4 for two kanji. |

## Tips and Best Practices

- Use LEN for character limits and LENB only for byte limits.
- Test with real text from the target system, because the byte count depends on the character set.
- Use LENB before MIDB or LEFTB so the cut fits the byte limit on the first try.
- Record which unit each field uses, characters or bytes, in the data dictionary.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LEN](LEN.md) | Counts characters, the standard length function. |
| [MIDB](MIDB.md) | Extracts a byte count from the middle of text. |
| [LEFTB](LEFTB.md) | Returns a byte count from the start of text. |
| [RIGHTB](RIGHTB.md) | Returns a byte count from the end of text. |
| [REPLACEB](REPLACEB.md) | Replaces a byte count of text. |

## Official Documentation

- [Microsoft Support: LEN function](https://support.microsoft.com/en-us/excel/functions/len-function)
- [Google Docs Editors Help: LENB](https://support.google.com/docs/answer/9367584)
