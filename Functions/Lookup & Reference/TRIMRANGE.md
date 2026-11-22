---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
  - Data Cleaning
use-case:
  - Cleaning Imported Blocks
  - Dynamic Report Ranges
  - Trimming Form Exports
related:
  - CHOOSECOLS
  - DROP
  - FILTER
  - ROWS
  - TAKE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/trimrange-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Trim Range
  - Trim Blank Edges
tags:
  - array-shaping
  - data-cleaning
  - excel
---

# TRIMRANGE

## Description

**TRIMRANGE** removes blank rows and columns from the outer edges of a range or array. It scans inward from each edge until it reaches a cell that contains a value, and it excludes the blank rows and columns it passed. It is useful when a block of data has empty rows above, below, or beside it, such as an export that pads its result with blank lines.

TRIMRANGE trims only the outer edges. Blank rows that sit between data rows stay where they are. To remove blank rows from anywhere in the block, use FILTER with a condition on a key column instead.

The two optional arguments control which edges to trim. `trim_rows` and `trim_cols` each take a code: 0 trims nothing, 1 trims the leading (top or left) blanks, 2 trims the trailing (bottom or right) blanks, and 3 trims both. The default for both is 3.

TRIMRANGE is available only in Microsoft 365. It is not listed for Excel 2024 or earlier versions, and Google Sheets does not have it.

## Syntax

```excel
=TRIMRANGE(range, [trim_rows], [trim_cols])
```

<!-- Image 1: TRIMRANGE Edge Codes. See Images/Lookup & Reference/TRIMRANGE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `range` | Yes | The range or array to trim. |
| `trim_rows` | No | Which blank rows to remove: `0` for none, `1` for leading blank rows, `2` for trailing blank rows, and `3` for both (the default). |
| `trim_cols` | No | Which blank columns to remove, using the same codes. The default is `3`. |

### Return Value

The range or array with the blank outer rows and columns removed. Blank rows and columns between data cells remain in the result. The result spills into the cells below and to the right of the formula.

## Examples

All examples use this block in `C1:E7`. Row 1 is blank, row 2 is the header, rows 3 to 5 hold the data, and rows 6 and 7 are blank.

| Column C | Column D | Column E |
| --- | --- | --- |
| (blank) | (blank) | (blank) |
| Item | Qty | Price |
| Pens | 12 | 0.50 |
| Paper | 5 | 4.00 |
| Tape | 3 | 2.50 |
| (blank) | (blank) | (blank) |
| (blank) | (blank) | (blank) |

### Example 1: Trim Both Edges

```excel
=TRIMRANGE(C1:E7)
```

**Result:** Four rows and three columns, from `C2:E5`: the header row and the three data rows.

The default trims both the leading and trailing blank rows.

### Example 2: Trim Only the Leading Blanks

```excel
=TRIMRANGE(C1:E7, 1)
```

**Result:** Six rows and three columns, from `C2:E7`

The blank row above the header is removed, but the two blank rows at the bottom stay.

### Example 3: Trim Only the Trailing Blanks

```excel
=TRIMRANGE(C1:E7, 2)
```

**Result:** Five rows and three columns, from `C1:E5`

The two blank rows at the bottom are removed, and the blank row at the top stays.

### Example 4: Sum a Column After Trimming

```excel
=SUM(TRIMRANGE(D1:D7))
```

**Result:** `20`

The trimmed range is `D2:D5`. SUM ignores the header text, so it adds 12, 5 and 3.

### Example 5: Count the Rows After Trimming

```excel
=ROWS(TRIMRANGE(C1:E7))
```

**Result:** `4`

The trimmed range holds the header and three data rows.

<!-- Image 2: Trim Before and After. See Images/Lookup & Reference/TRIMRANGE.md -->

## Story Problems

### Problem 1: Counting Survey Responses

A form export in `A1:B12` has a header in row 1 and six responses in rows 2 to 7. Rows 8 to 12 are blank padding from the export.

**Task:** Count the responses, leaving out the header row.

**Solution:**

```excel
=ROWS(TRIMRANGE(A1:B12))-1
```

**Answer:** `6`. Trimming the bottom blanks leaves seven rows, and subtracting the header gives six responses.

### Problem 2: Data Starting Below Blank Rows

A column in `E3:E10` has two blank rows at the top, then values in `E5` to `E8`, then two blank rows at the bottom.

**Task:** Find how many rows the block holds once the blank rows at the top are removed.

**Solution:**

```excel
=ROWS(TRIMRANGE(E3:E10, 1))
```

**Answer:** `6`. Removing the leading blanks leaves rows 5 to 10, which is six rows, including the two trailing blanks.

## Use Cases

### Trimming Form Exports

**Scenario:** A form tool exports responses into a fixed block that is padded with blank rows, and a report needs only the filled rows.

```excel
=TRIMRANGE(Export!A1:H1000)
```

**Why It Works:** The padding at the top and bottom is removed, so the report sizes itself to the real responses.

### Dynamic Report Ranges

**Scenario:** A summary needs the number of rows in a table that is pre-formatted to 500 rows.

```excel
=ROWS(TRIMRANGE(Data!A1:D500))
```

**Why It Works:** Trailing blank rows are excluded, so the count reflects the rows that contain data.

### Cleaning Imported Blocks

**Scenario:** An imported block has blank columns on the left, and the report needs only the columns that contain values.

```excel
=TRIMRANGE(Import!A1:Z50, 0, 3)
```

**Why It Works:** Setting `trim_rows` to 0 keeps every row, and `trim_cols` to 3 removes the blank columns at both edges.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The Excel version is earlier than Microsoft 365. | Use TAKE or DROP with a fixed row count, or upgrade to Microsoft 365. |
| Blank rows remain in the middle | TRIMRANGE trims only outer edges. | Use FILTER with a condition on a key column. |
| Blank rows still appear at the bottom | `trim_rows` is set to 1 or 0. | Use 2 or 3 to trim the trailing blanks. |
| `#SPILL!` | The cells the result needs are not empty. | Clear the spill range, or move the formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 only | Not listed for Excel 2024 or earlier. Trims outer edges only. |
| Google Sheets | Not available | Use FILTER with a condition on a key column to remove blank rows, for example `=FILTER(A1:B12, A1:A12<>"")`. |

## Tips and Best Practices

- Use TRIMRANGE on exports and imports, where padding rows and columns are common at the edges.
- Pair TRIMRANGE with ROWS to size a report without counting the padding.
- Use FILTER instead when blank rows may sit in the middle of the data.
- Check the edge codes when the result looks too large: a default of 3 trims both sides, which is not always what you want.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TAKE](TAKE.md) | Keeps a fixed number of rows from the start or end. |
| [DROP](DROP.md) | Removes a fixed number of rows or columns from the start or end. |
| [FILTER](FILTER.md) | Removes blank rows from anywhere in the block, not only the edges. |
| [ROWS](ROWS.md) | Counts the rows that remain after trimming. |
| [CHOOSECOLS](CHOOSECOLS.md) | Selects specific columns from the trimmed block. |

## Official Documentation

- [Microsoft Support: TRIMRANGE function](https://support.microsoft.com/en-us/excel/functions/trimrange-function)
