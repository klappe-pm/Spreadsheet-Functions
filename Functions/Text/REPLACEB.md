---
domain: Spreadsheet Functions
category: Text
subcategory: Double Byte Text
purpose:
  - Text Manipulation
use-case:
  - Byte Limited Field Updates
  - Fixed Width Record Edits
  - Japanese Customer Names
related:
  - LENB
  - MIDB
  - REPLACE
  - RIGHTB
  - SEARCHB
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/replace-function
  - https://support.google.com/docs/answer/9367752
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Replace By Bytes
tags:
  - byte-based
  - double-byte
  - excel
  - sheets
---

# REPLACEB

## Description

**REPLACEB** replaces part of a text string, but it counts the start position and the number of characters to replace in bytes instead of characters. When the text contains only single-byte characters such as English letters, digits and common punctuation, REPLACEB gives the same result as [REPLACE](REPLACE.md). The difference appears with double-byte characters, which take two bytes each in the byte count.

Use REPLACEB when a file format or legacy system defines fields by byte length, typically in Japanese, Chinese or Korean data. Use REPLACE for ordinary text. The Microsoft REPLACE page lists REPLACEB as deprecated, so new work in Excel should use REPLACE. Google Sheets documents REPLACEB as a current function.

The Google Sheets page does not explain how the num_bytes argument behaves when a double-byte character sits on the boundary of the replaced range. Test with real data before relying on REPLACEB for mixed-width text.

## Syntax

```excel
=REPLACEB(text, position, num_bytes, new_text)
```

<!-- Image 1: Byte Positions in a Mixed Text String. See Images/Text/REPLACEB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text, or a cell reference that holds the text, to change. |
| `position` | Yes | The byte position where the replacement begins. Counting starts at 1. |
| `num_bytes` | Yes | The number of bytes in `text` to replace. The Google Sheets page gives no further detail. |
| `new_text` | Yes | The text inserted in place of the replaced bytes. |

### Return Value

Text. Wrap the formula in VALUE to convert a numeric result to a number.

## Examples

### Example 1: Single-Byte Text Behaves Like REPLACE

```excel
=REPLACEB("Order-2024", 7, 4, "2025")
```

**Result:** `Order-2025`

Every character in this text is one byte, so the four bytes starting at position 7 are the four digits of the year. The result matches what REPLACE returns for the same arguments.

### Example 2: Replace a Code Inside a Longer Label

```excel
=REPLACEB("Invoice-2024", 9, 4, "2025")
```

**Result:** `Invoice-2025`

The invoice number starts at byte 9 and occupies four bytes. Replacing those bytes updates the year without touching the prefix.

### Example 3: Return a Numeric Value

```excel
=VALUE(REPLACEB("1009", 1, 2, "20"))
```

**Result:** `2009`

The first two bytes of the text are replaced, and VALUE converts the resulting digits to a number. VALUE only works when the final text contains a valid number.

### Example 4: Compare With REPLACE on ASCII Text

```excel
=REPLACE("Order-2024", 7, 4, "2025")
```

**Result:** `Order-2025`

Using REPLACE on the same single-byte text gives the same answer. The comparison shows that the byte rule changes results only when double-byte characters are present.

<!-- Image 2: Byte Positions in an Invoice Reference. See Images/Text/REPLACEB.md -->

## Story Problems

### Problem 1: Update Fixed-Width Invoice Records

A finance team exports invoices to a system that reads a fixed-width record. The invoice reference holds the billing year in bytes 9 to 12. All references in this list use single-byte characters, so the byte positions match character positions.

| Invoice Reference |
| --- |
| Invoice-2024 |
| Invoice-2024 |

**Task:** Replace the billing year in the first reference with `2025`.

**Solution:**

```excel
=REPLACEB(A2, 9, 4, "2025")
```

**Answer:** `Invoice-2025`. The year occupies bytes 9 to 12, and the prefix `Invoice-` is unchanged.

### Problem 2: Confirm That Single-Byte Data Matches REPLACE

A data analyst is unsure whether a column needs REPLACEB. The column holds product codes made only of English letters and digits.

| Product Code |
| --- |
| WX-7741 |

**Task:** Decide whether REPLACEB and REPLACE return the same result for the code when the characters from position 4 to 5 are replaced with `99`.

**Solution:**

```excel
=REPLACE(A2, 4, 2, "99")
```

**Answer:** `WX-9941` for both functions. Positions 4 and 5 hold `77`, which becomes `99`, and the last two characters `41` stay. Every character in the code is one byte, so REPLACE is the simpler choice.

<!-- Image 3: Fixed Width Record Layout. See Images/Text/REPLACEB.md -->

## Use Cases

### Byte Limited Field Updates

**Scenario:** A legacy system accepts a fixed number of bytes for each field. A code must be updated without changing its total byte length.

```excel
=REPLACEB(A2, 1, 6, "ABCDEF")
```

**Why It Works:** REPLACEB measures the replaced section in bytes, so the replacement width matches the field definition. Check the output length with LENB before exporting.

### Fixed Width Record Edits

**Scenario:** A warehouse file stores records in fixed columns, and one code in each record must be changed.

```excel
=REPLACEB(A2, 11, 3, "007")
```

**Why It Works:** The position and width come from the record layout, so REPLACEB keeps every other field aligned.

### Byte Width Placeholders

**Scenario:** A mailing export stores a placeholder code of fixed byte width at the start of each name field, and the code must be swapped for a new one.

```excel
=REPLACEB(A2, 1, 4, "N001")
```

**Why It Works:** Because the old code and the new code both occupy four bytes, the rest of the field stays aligned. Double-byte names are safe only when the replaced range starts and ends on a character boundary, so check those rows before exporting.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result differs from REPLACE | The text contains double-byte characters, and REPLACEB counts them as two bytes. | Use the byte positions from the record layout, or use REPLACE if the layout is character based. |
| Replacement splits a character | The byte range starts or ends inside a double-byte character. | Adjust `position` or `num_bytes` so the range ends on a character boundary. |
| Unexpected number | REPLACEB returns text. | Wrap the formula in VALUE when the result feeds a calculation. |
| Excel warns about deprecation | REPLACEB is deprecated in Excel. | Use REPLACE for new work, and keep REPLACEB only for existing byte-based files. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Deprecated | The Microsoft REPLACE page lists REPLACEB as deprecated. Use REPLACE for new work. |
| Google Sheets | Available | Same four arguments, counting bytes instead of characters. The page does not say how a partial double-byte character is handled. |

## Tips and Best Practices

- Use REPLACEB only when the source system defines fields by bytes.
- Measure a sample with LENB to confirm the byte counts before changing a full column.
- Keep a note of the encoding of the source file, because the byte count depends on it.
- Prefer REPLACE for English and other single-byte text.
- Test the output on a few rows that contain double-byte characters at the edges of the replaced range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [REPLACE](REPLACE.md) | The character-based version and the recommended choice for ordinary text. |
| [LENB](LENB.md) | Counts the bytes in text, used to check field widths. |
| [MIDB](MIDB.md) | Extracts a byte-based section of text. |
| [RIGHTB](RIGHTB.md) | Returns the rightmost bytes of text. |
| [SEARCHB](SEARCHB.md) | Finds a position counted in bytes, to use as `position`. |

## Official Documentation

- [Microsoft Support: REPLACE function](https://support.microsoft.com/en-us/excel/functions/replace-function)
- [Google Docs Editors Help: REPLACEB](https://support.google.com/docs/answer/9367752)
