---
domain: Spreadsheet Functions
category: Text
subcategory: Text Joining and Splitting
purpose:
  - Array Shaping
  - Text Manipulation
use-case:
  - Array Debugging
  - Dynamic Label Building
  - Report Summary Cells
related:
  - CONCAT
  - TEXTJOIN
  - TEXTSPLIT
  - TOCOL
  - TOROW
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/arraytotext-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - array
  - dynamic-array
  - excel
  - text-conversion
---

# ARRAYTOTEXT

## Description

**ARRAYTOTEXT** converts an array or range of any shape into text. It reads the values row by row and returns them in one cell, so a two-column block of prices and names becomes a single readable string or a single formula-style string. It is available only in Excel, where it works with dynamic arrays.

The function has two output styles, set by the optional format argument. Format 0, the default, returns a concise list of values separated by commas, which suits labels, messages and quick summaries. Format 1 returns a strict version with quotes around strings, row delimiters and the same shape as the input, which suits checking exactly what an array contains.

Use ARRAYTOTEXT when a dynamic array result must appear as text in one cell. It does not join values with a chosen separator. For that, use TEXTJOIN, which accepts a delimiter and can skip empty values. Use CONCAT when you only need the values placed next to each other with no separator.

<!-- Image 1: Array Input and Output Formats. See Images/Text/ARRAYTOTEXT.md -->

## Syntax

```excel
=ARRAYTOTEXT(array, [format])
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range, array or formula result to convert. Values are read row by row. |
| `format` | No | `0` returns concise text (the default when omitted). `1` returns strict text with quotes and row delimiters. Any other value returns `#VALUE!`. |

### Return Value

A single text value. Format 0 returns comma-separated values in one cell. Format 1 returns a string in array notation with the same number of rows and columns as the input. The function returns `#VALUE!` when the format is not 0 or 1.

## Examples

All examples use this price list in `A2:B4`:

| Item | Detail |
| --- | --- |
| Mugs | Blue |
| Bowls | 7 |
| Plates | Green |

### Example 1: Concise Output of a Two-Column Block

```excel
=ARRAYTOTEXT(A2:B4)
```

**Result:** `Mugs, Blue, Bowls, 7, Plates, Green`

The function reads the first row (Mugs, Blue), then the second, then the third. The format argument is omitted, so the default format 0 applies.

<!-- Image 2: Format 0 Versus Format 1. See Images/Text/ARRAYTOTEXT.md -->

### Example 2: Strict Output for Checking Shape

```excel
=ARRAYTOTEXT(A2:B4, 1)
```

**Result:** `{"Mugs","Blue";"Bowls",7;"Plates","Green"}`

Strings are wrapped in quotes, the number 7 is not, semicolons separate rows and commas separate columns. Use this output to confirm that the array has the expected layout before you build on it.

### Example 3: Single Column as a List

```excel
=ARRAYTOTEXT(A2:A4)
```

**Result:** `Mugs, Bowls, Plates`

A single column produces one value per row, so the result is the list of items in order.

### Example 4: Guarding Against an Invalid Format

```excel
=IFERROR(ARRAYTOTEXT(A2:B4, 2), "Unsupported format")
```

**Result:** `Unsupported format`

Format 2 is not documented, so the function returns `#VALUE!` and IFERROR replaces the error with a readable message.

### Example 5: Building a Label From a List

```excel
="Items: " & ARRAYTOTEXT(A2:A4)
```

**Result:** `Items: Mugs, Bowls, Plates`

The ampersand joins the fixed label text to the converted array.

## Story Problems

### Problem 1: Staff Shifts for an Email Header

A manager keeps a shift list in `A1:B5`.

| Name | Shift |
| --- | --- |
| Ana | Morning |
| Ben | Evening |
| Cruz | Night |
| Dee | Morning |

**Task:** Put the whole shift list into one cell, `D2`, so it can be pasted into an email header.

**Solution:**

```excel
=ARRAYTOTEXT(A2:B5)
```

**Answer:** `Ana, Morning, Ben, Evening, Cruz, Night, Dee, Morning`, because the rows are read in order and each name is followed by its shift.

### Problem 2: Items That Are Out of Stock

A shop keeps stock counts in `D1:E5`.

| Item | On Hand |
| --- | --- |
| Pens | 0 |
| Glue | 3 |
| Tape | 0 |
| Stapler | 5 |

**Task:** List the items with zero stock in one cell, `G2`.

**Solution:**

```excel
=ARRAYTOTEXT(FILTER(D2:D5, E2:E5=0))
```

**Answer:** `Pens, Tape`, because FILTER keeps only the rows where the count is 0, and ARRAYTOTEXT turns those names into one string.

## Use Cases

### Warehouse Reorder Alert

**Scenario:** A reorder message must list every product below its reorder level, and the list changes daily.

```excel
="Reorder now: " & ARRAYTOTEXT(FILTER(Stock[SKU], Stock[Qty] < Stock[Reorder]))
```

**Why It Works:** FILTER returns the matching SKUs as a dynamic array, and ARRAYTOTEXT turns them into one line that the message can show. If nothing matches, FILTER returns an error, so wrap it in IFERROR when the list can be empty.

### Checking What a Dynamic Array Holds

**Scenario:** A formula spills a block of results, and the analyst needs to confirm the exact layout before copying it.

```excel
=ARRAYTOTEXT(B2:D4, 1)
```

**Why It Works:** Format 1 shows row delimiters, quotes and the shape of the block, so mistakes in the spill range are easy to see. Switch back to format 0 for the final label.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The format argument is not 0 or 1. | Use 0, 1 or leave the argument out. |
| `#VALUE!` shown inside the text | A source cell in the array contains an error. | Fix or wrap the source values before converting. |
| Numbers look unformatted | Format 0 uses general formatting, so currency or date formats are not kept. | Convert formatted values with TEXT before the array is built. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021 and Microsoft Office | Format 0 and format 1 only. Works with dynamic array results. |
| Google Sheets | Not available | Closest alternative: TEXTJOIN with a delimiter, which joins a range of any shape but does not add row delimiters or quotes. |

## Tips and Best Practices

- Use format 1 while you build a formula, then switch to format 0 for the final text.
- Fix error values in the source range first, because they appear as `#VALUE!` inside the output.
- Pair the function with FILTER or SORT to convert only the rows you need.
- Use TEXTJOIN when you need a separator other than the default comma and space.
- Keep the output in one cell only when it is short, since long lists become hard to read.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CONCAT](CONCAT.md) | Joins values in order with no separator. |
| [TEXTJOIN](TEXTJOIN.md) | Joins values with a chosen delimiter and can skip blanks. |
| [TEXTSPLIT](TEXTSPLIT.md) | Does the reverse: splits text into an array. |
| [TOCOL](../Lookup%20%26%20Reference/TOCOL.md) | Reshapes any array into one column before conversion. |
| [TOROW](../Lookup%20%26%20Reference/TOROW.md) | Reshapes any array into one row before conversion. |

## Official Documentation

- [Microsoft Support: ARRAYTOTEXT function](https://support.microsoft.com/en-us/excel/functions/arraytotext-function)
