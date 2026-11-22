---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
purpose:
  - Reference Building
use-case:
  - Cross Sheet Reference Labels
  - Dynamic Cell References
  - Formula Audit Notes
related:
  - CELL
  - COLUMN
  - FORMULATEXT
  - INDIRECT
  - OFFSET
  - ROW
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/address-function
  - https://support.google.com/docs/answer/3093308
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cell Address Text
  - Cell Reference Text
tags:
  - excel
  - r1c1-notation
  - reference-building
  - sheets
---

# ADDRESS

## Description

**ADDRESS** builds a cell reference as text from a row number and a column number. Give it row 4 and column 3, and it returns `$C$4`. Use it when the position is calculated, for example by MATCH, and you need the address as text: to pass into INDIRECT, to label a result, or to record which cell a figure came from.

The result is text, not a live reference. If you insert a row above `C4` later, the text `$C$4` does not change, so it no longer follows the cell that moved. When a formula must read the value that follows the cell, use INDEX with the row and column numbers, or wrap the address in INDIRECT.

The third argument sets which parts of the address are absolute. The fourth argument chooses between A1 style, the default, and R1C1 style. The fifth argument adds a sheet name in front of the address, so the result reads `Budget!$C$4`.

## Syntax

```excel
=ADDRESS(row_num, column_num, [abs_num], [a1], [sheet_text])
```

<!-- Image 1: Address Argument Anatomy. See Images/Lookup & Reference/ADDRESS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `row_num` | Yes | The row number, where row 1 is 1. Use a whole number. |
| `column_num` | Yes | The column number, not the column letter. Column A is 1 and column C is 3. |
| `abs_num` | No | The reference type. 1 (default) makes row and column absolute, 2 makes the row absolute and the column relative, 3 makes the row relative and the column absolute, and 4 makes both relative. |
| `a1` | No | TRUE (default) returns A1 style. FALSE returns R1C1 style. |
| `sheet_text` | No | The sheet name to place in front of the address. Leave it out for the current sheet. |

### Return Value

A text string that holds the cell address, such as `$C$4`. The function returns text and never a reference, so use INDIRECT when a formula must read the cell itself.

## Examples

### Example 1: Absolute Address by Default

```excel
=ADDRESS(4, 3)
```

**Result:** `$C$4`

Row 4 and column 3 (column C). With no abs_num, both the column and the row are absolute.

### Example 2: Row Absolute and Column Relative

```excel
=ADDRESS(4, 3, 2)
```

**Result:** `C$4`

The dollar sign stays in front of the row number only. This form is common when a reference should keep a fixed row while the column changes.

### Example 3: R1C1 Style

```excel
=ADDRESS(4, 3, 1, FALSE)
```

**Result:** `R4C3`

Setting a1 to FALSE returns the row and column as numbers, which is the style used by R1C1 notation.

<!-- Image 2: Reference Style Grid. See Images/Lookup & Reference/ADDRESS.md -->

### Example 4: Sheet Name Prefix

```excel
=ADDRESS(4, 3, 1, TRUE, "Budget")
```

**Result:** `Budget!$C$4`

The fifth argument adds the sheet name and an exclamation mark. If the sheet name contains spaces, the name needs quotation marks in any formula built from this text.

### Example 5: Reading the Cell With INDIRECT

```excel
=INDIRECT(ADDRESS(4, 3))
```

**Result:** the value stored in cell C4 of the current sheet

ADDRESS creates the text `$C$4` and INDIRECT turns that text into a live reference. The formula returns whatever C4 holds.

## Story Problems

### Problem 1: Finding the Peak Sales Month

A shop records monthly sales in `A1:B6`. The header row is row 1 and the data starts in row 2.

| Month | Sales |
| --- | --- |
| Jan | 4200 |
| Feb | 5100 |
| Mar | 3900 |
| Apr | 6100 |
| May | 4800 |

**Task:** Return the address of the cell that holds the highest sales figure as text.

**Solution:**

```excel
=ADDRESS(MATCH(MAX(B2:B6), B2:B6, 0) + 1, 2)
```

**Answer:** `$B$5`. MATCH finds the highest value in position 4 of `B2:B6`. Adding 1 converts that position to the sheet row, because the data starts in row 2, and column 2 is column B.

<!-- Image 3: Peak Lookup Result. See Images/Lookup & Reference/ADDRESS.md -->

### Problem 2: Labeling Budget Cells

A planner keeps a list of budget items in `A1:C4`. Columns B and C hold the row and column number of each item's amount cell on the Budget sheet.

| Item | Row | Column |
| --- | --- | --- |
| Rent | 3 | 2 |
| Utilities | 4 | 2 |
| Insurance | 5 | 3 |

**Task:** Create the absolute address of each amount cell in column D.

**Solution:**

```excel
=ADDRESS(B2, C2)
```

Copy the formula down to `D4`.

**Answer:** `$B$3` for Rent, `$B$4` for Utilities and `$C$5` for Insurance. Each address follows the row and column numbers in the same line.

## Use Cases

### Cross Sheet Reference Labels

**Scenario:** A summary sheet lists where each reported figure comes from so that a reviewer can find it on the Inputs sheet.

```excel
=ADDRESS(2, 3, 1, TRUE, "Inputs")
```

**Why It Works:** The sheet name in the fifth argument produces `Inputs!$C$2`, which the reviewer can paste into the Go To box. The label stays correct as long as the input stays in the same cell.

### Dynamic Cell References

**Scenario:** A dashboard picks a row from a list with MATCH, and a helper cell must read the value in that row without a fixed reference.

```excel
=INDIRECT(ADDRESS(MATCH(F1, A2:A13, 0) + 1, 4, 4))
```

**Why It Works:** ADDRESS builds a relative address in column D from the matched row, and INDIRECT reads it. If the match fails, the formula returns an error, so wrap it in IFERROR when a blank is better.

### Formula Audit Notes

**Scenario:** An analyst writes a check line that names the cell being tested, so the note stays correct when someone copies it.

```excel
="Check the value at "&ADDRESS(ROW(B7), COLUMN(B7), 4)
```

**Why It Works:** ROW and COLUMN supply the numbers for B7, and abs_num 4 gives the relative form `B7`. The note reads "Check the value at B7".

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Wrong address | The column is given as a letter, such as `"C"`. | Use the column number, 3 for column C, or write COLUMN(C1). |
| Address does not follow a moved cell | The result is text, so inserted rows do not update it. | Use INDEX with the row and column numbers, or read the cell through INDIRECT. |
| Address in R1C1 form | The a1 argument is FALSE. | Omit a1 or set it to TRUE for A1 style. |
| Reference to the wrong sheet | The sheet name in sheet_text is misspelled or missing. | Check the spelling against the tab name, or leave the argument out for the current sheet. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Argument names are row_num, column_num, abs_num, a1 and sheet_text. |
| Google Sheets | Available | The arguments are named row, column, absolute_relative_mode, use_a1_notation and sheet, in the same order. |

## Tips and Best Practices

- Leave abs_num out when the address should lock both the row and the column, and use 4 when the address should move with the formula.
- Use COLUMN(C1) instead of a typed 3 when a reviewer must see which column the formula means.
- Pair ADDRESS with INDIRECT only when the position is calculated; for a fixed cell, a plain reference is simpler and easier to audit.
- Remember that the result is text, so it does not change when rows or columns are inserted.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CELL](../Information/CELL.md) | Returns an address with the `"address"` info type, without building text. |
| [COLUMN](COLUMN.md) | Returns the column number that ADDRESS needs for its column_num argument. |
| [FORMULATEXT](FORMULATEXT.md) | Returns the formula in a cell as text, which helps when auditing ADDRESS formulas. |
| [INDIRECT](INDIRECT.md) | Turns an address string into a live reference. |
| [OFFSET](OFFSET.md) | Returns a reference that is a set number of rows and columns from a start cell. |
| [ROW](ROW.md) | Returns the row number that ADDRESS needs for its row_num argument. |

## Official Documentation

- [Microsoft Support: ADDRESS function](https://support.microsoft.com/en-us/excel/functions/address-function)
- [Google Docs Editors Help: ADDRESS](https://support.google.com/docs/answer/3093308)
