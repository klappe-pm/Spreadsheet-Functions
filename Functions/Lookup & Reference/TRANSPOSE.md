---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
use-case:
  - Chart Series From Rows
  - Rotating Imported Data
  - Vertical Report Lists
related:
  - CHOOSEROWS
  - HSTACK
  - TOCOL
  - TOROW
  - VSTACK
  - WRAPCOLS
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/transpose-function
  - https://support.google.com/docs/answer/3094262
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Flip Rows and Columns
  - Swap Rows and Columns
tags:
  - array-shaping
  - excel
  - lookup-reference
  - sheets
---

# TRANSPOSE

## Description

**TRANSPOSE** swaps the rows and columns of a range or array. The first row becomes the first column, the second row becomes the second column, and so on. A range of 3 rows by 2 columns becomes a range of 2 rows by 3 columns.

Use TRANSPOSE when data arrives in the wrong orientation. A monthly report with months across the top can be turned into months down the side, or a vertical list can be laid out as a header row. Because TRANSPOSE is a formula, the result stays linked to the source, unlike Paste Special with Transpose, which copies the values once and does not update.

In Microsoft 365, TRANSPOSE works as a normal formula that spills into the cells beside it. In older Excel versions, the formula must be entered as an array formula across the full output range. Google Sheets treats TRANSPOSE the same way as a normal formula, so no special entry is needed.

## Syntax

```excel
=TRANSPOSE(array)
```

<!-- Image 1: Rows Becoming Columns. See Images/Lookup & Reference/TRANSPOSE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array to transpose. Its first row becomes the first column of the result. |

### Return Value

An array with the rows and columns swapped. A range of m rows and n columns returns a result of n rows and m columns. A value in row n, column m moves to row m, column n.

## Examples

### Example 1: Swap a Square Block

Data is in `A1:C3`:

| Column A | Column B | Column C |
| --- | --- | --- |
| 5 | 3 | 8 |
| 2 | 7 | 4 |
| 6 | 1 | 9 |

```excel
=TRANSPOSE(A1:C3)
```

**Result:** Row 1 becomes `5, 2, 6`, row 2 becomes `3, 7, 1`, and row 3 becomes `8, 4, 9`.

The block is 3 by 3, so the result is also 3 by 3.

### Example 2: Swap a Rectangular Block

```excel
=TRANSPOSE(A1:B3)
```

**Result:** Two rows of three values: `5, 2, 6` and `3, 7, 1`

The source has 3 rows and 2 columns, so the result has 2 rows and 3 columns.

### Example 3: Turn a Column Into a Row

Months are listed down `D1:D4` as Jan, Feb, Mar and Apr.

```excel
=TRANSPOSE(D1:D4)
```

**Result:** Jan, Feb, Mar and Apr across four columns of one row

A single column of four cells becomes a single row of four cells.

### Example 4: Transpose and Take the Largest Value

```excel
=MAX(TRANSPOSE(A1:C3))
```

**Result:** `9`

TRANSPOSE does not change which values exist, so MAX still finds the largest value in the block.

<!-- Image 2: Column Becomes Row. See Images/Lookup & Reference/TRANSPOSE.md -->

## Story Problems

### Problem 1: Invoice Numbers for a Report Header

A clerk lists five invoice numbers down `E1:E5`: INV-2041, INV-2042, INV-2043, INV-2044 and INV-2045.

**Task:** Place the invoice numbers across one row so they can be used as a report header, and name the first and last items.

**Solution:**

```excel
=TRANSPOSE(E1:E5)
```

**Answer:** Five values in one row, starting with `INV-2041` and ending with `INV-2045`.

### Problem 2: Quarterly Revenue as a Column

A finance sheet shows quarterly revenue across one row in `B2:E2`, with Q1 to Q4 in `B1:E1`.

| Quarter | Q1 | Q2 | Q3 | Q4 |
| --- | --- | --- | --- | --- |
| Revenue | 42000 | 45500 | 39800 | 51200 |

**Task:** Turn the four revenue figures into a column for a chart, and identify the highest quarter.

**Solution:**

```excel
=TRANSPOSE(B2:E2)
```

**Answer:** The four values run down a column. The highest is 51200, in the fourth row, which is Q4.

## Use Cases

### Chart Series From Rows

**Scenario:** A summary sheet stores monthly totals across a row, but the chart needs them down a column.

```excel
=TRANSPOSE(Summary!B2:M2)
```

**Why It Works:** The formula rebuilds the series in the orientation the chart expects, and it updates when the monthly totals change.

### Rotating Imported Data

**Scenario:** A system export places each record in a column, and the report needs each record in a row.

```excel
=TRANSPOSE(Export!A1:A40)
```

**Why It Works:** Each value moves from the column to the row in the same order, so the export does not need manual copying.

### Vertical Report Lists

**Scenario:** A list of approved regions is stored in a row, and a printed report needs them stacked vertically.

```excel
=TRANSPOSE(Settings!B1:F1)
```

**Why It Works:** The regions remain linked to the settings row, so a change to the setting appears in the report automatically.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Only one value appears (Excel 2019 and earlier) | The formula was entered in one cell without an array entry. | Select the full output range, enter the formula, and press Ctrl+Shift+Enter. |
| `#SPILL!` | The cells the result needs are not empty. | Clear the cells that the result would fill. |
| Values appear in the wrong positions | The output was sized for the original orientation. | Size the output range as n rows by m columns for an m by n source. |
| Pasted copy stops updating | Paste Special with Transpose copies values, not formulas. | Use TRANSPOSE in a formula to keep the link. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel 2016, Excel 2019, Excel 2021, Excel 2024, Microsoft 365 and Excel for the web | Microsoft 365 spills the result. Older versions need an array entry across the full output range. |
| Google Sheets | Available | Works as a normal formula, with no Ctrl+Shift+Enter. |

## Tips and Best Practices

- Check the dimensions before you enter the formula: a block of m rows and n columns needs n rows and m columns of empty cells.
- Use TRANSPOSE inside another function, such as SUM or MAX, when you need the result in a different shape without placing it on the sheet.
- Use CHOOSEROWS or HSTACK when you only need some of the rows or columns from the transposed result.
- Keep the source and the output on the same sheet when possible, so the formula is easy to find.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TOCOL](TOCOL.md) | Flattens a block into one column, skipping blanks if needed. |
| [TOROW](TOROW.md) | Flattens a block into one row, skipping blanks if needed. |
| [WRAPROWS](WRAPROWS.md) | Builds rows of a set width from a single list. |
| [WRAPCOLS](WRAPCOLS.md) | Builds columns of a set height from a single list. |
| [HSTACK](HSTACK.md) | Places ranges side by side without changing their orientation. |
| [VSTACK](VSTACK.md) | Stacks ranges one above another. |

## Official Documentation

- [Microsoft Support: TRANSPOSE function](https://support.microsoft.com/en-us/excel/functions/transpose-function)
- [Google Docs Editors Help: TRANSPOSE](https://support.google.com/docs/answer/3094262)
