---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
purpose:
  - Counting
use-case:
  - Checking Import Width
  - Sizing Lookup Ranges
  - Validating Table Layout
related:
  - CHOOSECOLS
  - COLUMN
  - INDEX
  - ROWS
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/columns-function
  - https://support.google.com/docs/answer/3093374
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Column Count
  - Width Count
tags:
  - column-count
  - dimensions
  - excel
  - sheets
---

# COLUMNS

## Description

**COLUMNS** returns the number of columns in a range or array. The range `C1:E4` covers columns C, D and E, so `COLUMNS(C1:E4)` returns 3. The function counts columns only, so the height of the range does not change the result. A single-column range always returns 1.

Use COLUMNS to size a formula, to check the width of an imported table, or to pass the last column number to a function such as INDEX or VLOOKUP. It also counts the columns of an array constant. In `{1,2,3;4,5,6}`, rows are separated by semicolons and columns by commas, so the constant has three columns.

COLUMNS is the width counterpart of ROWS. Use the two together to find the size of a range in cells, or use COLUMN when you need the position of one column rather than a count.

## Syntax

```excel
=COLUMNS(array)
```

<!-- Image 1: Width Count Anatomy. See Images/Lookup & Reference/COLUMNS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | An array, an array formula or a reference to a range of cells. |

### Return Value

A whole number: the count of columns in the array or range. The page does not describe any error values for this function.

## Examples

### Example 1: Columns in a Range

```excel
=COLUMNS(C1:E4)
```

**Result:** `3`

The range runs across columns C, D and E. Its four rows do not affect the count.

### Example 2: Columns in an Array Constant

```excel
=COLUMNS({1,2,3,4,5})
```

**Result:** `5`

The commas separate five values in one row, so the array has five columns.

### Example 3: Width of a Header Row

```excel
=COLUMNS(A2:H2)
```

**Result:** `8`

A header row that spans columns A to H has eight columns.

### Example 4: A Single Column

```excel
=COLUMNS(A1:A100)
```

**Result:** `1`

A column of 100 cells is still one column wide.

<!-- Image 2: Columns Versus Rows. See Images/Lookup & Reference/COLUMNS.md -->

### Example 5: Last Value in a Row

```excel
=INDEX(B2:H2, COLUMNS(B2:H2))
```

**Result:** the last value in row 2 between columns B and H

COLUMNS returns 7 for B2:H2, and INDEX returns the seventh value of that range, which is the value in H2.

## Story Problems

### Problem 1: Average Monthly Sales

A shop records monthly sales for one store in row 2. The months run from January to June across columns B to G.

| Store | Jan | Feb | Mar | Apr | May | Jun |
| --- | --- | --- | --- | --- | --- | --- |
| Harbor | 40 | 50 | 45 | 60 | 55 | 50 |

**Task:** Find the average monthly sales for Harbor without typing the number of months.

**Solution:**

```excel
=SUM(B2:G2) / COLUMNS(B2:G2)
```

**Answer:** `50`. The six months total 300, and 300 divided by 6 is 50.

### Problem 2: Last Value in a Stock Row

A parts list holds one part per row in `A1:D2`. The stock count is always the last column.

| Code | Name | Price | Stock |
| --- | --- | --- | --- |
| P-10 | Hinge | 4 | 120 |

**Task:** Return the stock count from row 2, using COLUMNS to find the last column.

**Solution:**

```excel
=INDEX(A2:D2, COLUMNS(A2:D2))
```

**Answer:** `120`. The range has four columns, so INDEX returns the fourth value in row 2.

## Use Cases

### Checking Import Width

**Scenario:** A weekly export from a billing system must have exactly 12 columns. A check cell warns the user when the export changes shape.

```excel
=IF(COLUMNS(ImportData) = 12, "Width OK", "Check the export columns")
```

**Why It Works:** COLUMNS counts the columns of the named range, so a new or missing column changes the result and triggers the warning.

### Sizing Lookup Ranges

**Scenario:** A price table has a product code in the first column, and the price sits in the last of its columns. The lookup should use the last column automatically when columns are added.

```excel
=VLOOKUP(A2, Prices, COLUMNS(Prices), FALSE)
```

**Why It Works:** The column index is always the width of the table, so the lookup returns the last column even after the table grows.

### Validating Table Layout

**Scenario:** A reporting template expects the same number of headers as the summary sheet. A check confirms that both header rows match before the data is copied.

```excel
=COLUMNS(Summary!A1:H1) = COLUMNS(Template!A1:H1)
```

**Why It Works:** The formula returns TRUE when both header rows have the same width and FALSE when they differ.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Count of 1 for a block | COLUMNS counts columns, not cells, so a single-column block returns 1. | Use ROWS for the height, and multiply the two for the cell count. |
| Unexpected width after an edit | Inserted or deleted columns changed the range. | Recheck the range after structural edits. |
| Wrong width for a constant | Rows and columns were confused in an array constant. | Use commas between values in the same row and semicolons between rows. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019, Excel 2016, Microsoft Office and Office for iPhone | Counts columns in an array, array formula or range. |
| Google Sheets | Available | Same single argument. The page describes the range as the input. |

## Tips and Best Practices

- Use COLUMNS to set the column index of VLOOKUP or INDEX so the formula still works when the table grows.
- Multiply COLUMNS by ROWS to count the cells in a block.
- Check the width after an export, because a single extra column can shift every lookup.
- Use commas for columns and semicolons for rows when you type an array constant.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSECOLS](CHOOSECOLS.md) | Returns chosen columns from an array, so COLUMNS can size the result. |
| [COLUMN](COLUMN.md) | Returns the position of one column rather than the count of columns. |
| [INDEX](INDEX.md) | Returns a value by position, often with COLUMNS supplying the last column. |
| [ROWS](ROWS.md) | Counts the rows in a range, the height counterpart of this function. |

## Official Documentation

- [Microsoft Support: COLUMNS function](https://support.microsoft.com/en-us/excel/functions/columns-function)
- [Google Docs Editors Help: COLUMNS](https://support.google.com/docs/answer/3093374)
