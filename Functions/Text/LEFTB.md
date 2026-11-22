---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Text Manipulation
use-case:
  - Byte Limit Truncation
  - Japanese Label Fields
related:
  - FINDB
  - LEFT
  - LENB
  - MIDB
  - RIGHTB
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/left-function
  - https://support.google.com/docs/answer/9367470
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Byte Left
  - Left Bytes
tags:
  - byte-count
  - dbcs
  - excel
  - sheets
  - text-extraction
---

# LEFTB

## Description

**LEFTB** returns the leftmost part of a text string up to a set number of bytes, not characters. In single-byte text such as Latin letters, digits and punctuation, each character is one byte, so LEFTB and LEFT return the same result. In double-byte text such as Japanese, Chinese and Korean, most characters take 2 bytes, so LEFTB returns fewer characters than LEFT for the same count.

Use LEFTB when the length limit is set in bytes, for example a legacy field, a fixed-width record or a label that holds a set number of bytes. For ordinary text, use LEFT, which counts characters and is easier to read and maintain.

Microsoft documents LEFTB as deprecated. Excel still calculates it, and it appears in older workbooks, but new formulas should use LEFT unless a byte limit must be met. Google Sheets also provides LEFTB, and its help page describes it as counting bytes in the same way.

If the number of bytes is larger than the byte length of the text, the whole text is returned.

## Syntax

```excel
=LEFTB(string, num_of_bytes)
```

<!-- Image 1: LEFTB Bytes Compared With LEFT Characters. See Images/Text/LEFTB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `string` | Yes | The text to take the left portion from. A cell reference or a literal string in quotes works. |
| `num_of_bytes` | No | The number of bytes to return. Must be zero or greater. Defaults to 1 when omitted. Double-byte characters count as 2 bytes each. |

The argument names above follow the Google Sheets help page. The Microsoft LEFT page covers LEFTB as a deprecated function and does not reproduce its argument list, so confirm the argument names in Excel before you build a workbook that depends on them.

### Return Value

A text string containing the leftmost characters whose bytes fit within `num_of_bytes`. The function returns text. It returns the whole string when the byte limit is larger than the string.

## Examples

### Example 1: Single-Byte Text Matches LEFT

```excel
=LEFTB("ABCDEF", 4)
```

**Result:** `"ABCD"`

Each Latin letter takes one byte, so four bytes hold four characters. The result is the same as `LEFT("ABCDEF", 4)`.

### Example 2: Default Single Byte

```excel
=LEFTB("ABCDEF")
```

**Result:** `"A"`

When `num_of_bytes` is omitted, the function returns one byte, which is one Latin letter here.

### Example 3: Two Bytes With a Kanji

```excel
=LEFTB("熊本", 2)
```

**Result:** `"熊"`

The kanji 熊 takes 2 bytes, so two bytes hold exactly one character.

### Example 4: Four Bytes With Two Kanji

```excel
=LEFTB("熊本", 4)
```

**Result:** `"熊本"`

Each kanji takes 2 bytes, so four bytes hold both characters.

### Example 5: LEFT Counts Characters Instead

```excel
=LEFT("熊本", 2)
```

**Result:** `"熊本"`

LEFT counts characters, so two characters return both kanji. This contrasts with Example 3, where LEFTB counted bytes.

### Example 6: Mixed Text With a Byte Limit

```excel
=LEFTB("Aeñ", 2)
```

**Result:** `"Ae"`

The first two bytes hold the letters A and e. The accented letter does not fit in the remaining byte count, so it is not returned.

## Story Problems

### Problem 1: Fitting a Japanese Name in a Label Field

A label system prints the first four bytes of a Japanese place name in a narrow field. The name in A2 is 熊本県, which is three kanji.

| Place Name |
| --- |
| 熊本県 |

**Task:** Return the part of the name that fits in four bytes.

**Solution:**

```excel
=LEFTB(A2, 4)
```

**Answer:** `"熊本"`. Each kanji takes 2 bytes, so 熊 and 本 use all four bytes, and 県 does not fit.

<!-- Image 2: Byte Limit Applied to a Japanese Name. See Images/Text/LEFTB.md -->

### Problem 2: Trimming Latin Codes to a Byte Limit

A legacy import reads a code field that holds only four bytes. Each code in A2 uses only Latin letters and digits.

| Code |
| --- |
| ABCDEFGH |

**Task:** Return the first four bytes of the code in A2.

**Solution:**

```excel
=LEFTB(A2, 4)
```

**Answer:** `"ABCD"`. Each letter takes one byte, so the first four bytes are the first four characters.

## Use Cases

### Byte Limit Truncation

**Scenario:** A legacy system accepts a customer name only up to 12 bytes. Names that are longer must be shortened before export, and the Japanese names must not be cut inside a character.

```excel
=LEFTB(A2, 12)
```

**Why It Works:** LEFTB counts bytes, so the limit matches the field width. Each result is checked against the byte count, so compare the output with the original name for any long entries.

### Japanese Label Fields

**Scenario:** A shipping label has a short product name field, measured in bytes, and the product names are a mix of Japanese and Latin text.

```excel
=LEFTB(B2, 8)
```

**Why It Works:** The byte limit holds regardless of the character mix, so the label always fits the printed field. Pair it with LENB to measure the original length in bytes before truncating.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result is shorter than expected | Double-byte characters take 2 bytes each, so fewer characters fit. | Count bytes, not characters, or switch to LEFT if the limit is in characters. |
| Unexpected output from an old workbook | The workbook was built with LEFTB for a byte limit that no longer applies. | Review whether the byte limit is still required, and replace LEFTB with LEFT if not. |
| `#VALUE!` | A negative byte count is used. | Keep the byte count at zero or above, using MAX(0, ...) for computed values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available. Deprecated. | Designed for double-byte languages. Microsoft recommends LEFT for new work. |
| Google Sheets | Available. | Documented on the help page as counting bytes, with double-byte characters taking 2 bytes. |

## Tips and Best Practices

- Use LEFTB only when the field limit is in bytes.
- Measure the source with LENB before truncating so that you know how much will be lost.
- Test with real double-byte text, because Latin test data hides the difference from LEFT.
- Use LEFT in any new workbook unless a byte limit is required.
- Document the byte limit next to the formula so that later editors understand why LEFTB is used.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LEFT](LEFT.md) | Counts characters instead of bytes, and is the preferred choice for new work. |
| [FINDB](FINDB.md) | Finds a position in bytes, which pairs with LEFTB to split text at a delimiter. |
| [LENB](LENB.md) | Measures the length of the text in bytes. |
| [MIDB](MIDB.md) | Extracts a byte-counted substring from the middle of a string. |
| [RIGHTB](RIGHTB.md) | Extracts a byte-counted substring from the end of a string. |

## Official Documentation

- [Microsoft Support: LEFT and LEFTB functions](https://support.microsoft.com/en-us/excel/functions/left-function)
- [Google Docs Editors Help: LEFTB](https://support.google.com/docs/answer/9367470)
