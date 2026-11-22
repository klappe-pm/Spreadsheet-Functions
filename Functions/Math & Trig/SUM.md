---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Aggregation
  - Arithmetic Operations
use-case:
  - Monthly Budget Totals
  - Multi-Range Budget Totals
  - Timesheet Totals
related:
  - SUBTOTAL
  - SUMIF
  - SUMIFS
  - SUMPRODUCT
  - SUMSQ
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/sum-function
  - https://support.google.com/docs/answer/3093669
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Add Numbers
  - Total
tags:
  - aggregation
  - arithmetic
  - excel
  - sheets
  - totals
---

# SUM

## Description

**SUM** adds numbers. You give it single values, cell references or ranges, and it returns the total. It is the most common aggregation function in spreadsheets and the first choice for totals that include every row.

SUM ignores text and empty cells inside a range, so headers and blank rows do not break a total. Error values are not ignored. If any cell in the range shows an error such as `#REF!`, the SUM returns that error.

Use SUM when every value should count. For totals that depend on conditions, use SUMIF or SUMIFS. For totals that must respect filters, use SUBTOTAL. A plus sign chain such as `=A1+A2+A3` gives the same answer for three cells, but it returns `#VALUE!` when a referenced cell contains text, and it does not grow when rows are inserted into the range.

## Syntax

```excel
=SUM(number1, [number2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/SUM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, cell, or range to add. It can be a value such as `5`, a cell such as `A1`, a range such as `A1:A100`, or a named range such as `MonthlySales`. |
| `number2, ...` | No | Additional numbers, cells or ranges. Excel accepts up to 255 arguments in total. Arguments can mix values, cells and ranges. |

### Return Value

A single number equal to the total of the numeric values in the arguments. Text and empty cells inside ranges are ignored. The function returns the first error value found in its arguments.

## Examples

All examples use these monthly expenses in `A2:A6`: 25, "N/A", 40, 60 and 10.

### Example 1: Sum a Range

```excel
=SUM(A2:A6)
```

**Result:** `135`

The text entry "N/A" is skipped, so the total is 25 + 40 + 60 + 10.

### Example 2: Sum Ranges From Two Columns

```excel
=SUM(A2:A6, C2:C6)
```

**Result:** The combined total of column A and column C

Column C holds the same kind of expense for a second branch. SUM adds both ranges in one formula, so the totals stay in one place.

### Example 3: Mix Ranges With Numbers

```excel
=SUM(A2:A6, 100, -25)
```

**Result:** `210`

The range total is 135. Adding 100 gives 235, and the negative 25 subtracts to give 210. A negative number inside SUM works as a subtraction.

<!-- Image 2: Text Skipped in a Range. See Images/Math & Trig/SUM.md -->

### Example 4: Sum a Whole Column

```excel
=SUM(A:A)
```

**Result:** The total of every number in column A

A full-column reference includes rows added later, but it also includes a header row if that row contains a number. Use `=SUM(A2:A500)` when the header must stay out of the total.

## Story Problems

### Problem 1: Quarterly Fuel Costs

A delivery company records monthly fuel costs for the first quarter in `A1:B4`.

| Month | Fuel Cost |
| --- | --- |
| January | 412.50 |
| February | 388.75 |
| March | 430.00 |

**Task:** Total the fuel cost for the first quarter.

**Solution:**

```excel
=SUM(B2:B4)
```

**Answer:** `1231.25`, from 412.50 + 388.75 + 430.00.

<!-- Image 3: Quarterly Fuel Table. See Images/Math & Trig/SUM.md -->

### Problem 2: Weekly Hours With Blank Days

A freelancer logs hours per day in column B. Holidays and days off contain text or are left empty.

| Day | Hours |
| --- | --- |
| Monday | 7.5 |
| Tuesday | Holiday |
| Wednesday | 8 |
| Thursday | 6.25 |
| Friday | |
| Saturday | 8 |

**Task:** Total the hours worked during the week.

**Solution:**

```excel
=SUM(B2:B7)
```

**Answer:** `29.75`, from 7.5 + 8 + 6.25 + 8. The text "Holiday" and the empty cell are skipped.

## Use Cases

### Monthly Budget Totals

**Scenario:** A household tracks expense categories in a column and needs the monthly spending total.

```excel
=SUM(C5:C15)
```

**Why It Works:** The range covers every expense row, and text labels in the range are ignored. Add a category by inserting a row inside the range so the total updates.

### Timesheet Totals

**Scenario:** A team enters daily hours in a grid, with text notes such as "Leave" in some cells.

```excel
=SUM(B2:F40)
```

**Why It Works:** SUM skips the text notes, so the notes can stay in the grid without distorting the total of worked hours.

### Multi-Range Budget Totals

**Scenario:** A finance team totals budget figures from three regional blocks on one sheet.

```excel
=SUM(B3:B12, B16:B25, B29:B38)
```

**Why It Works:** Each block is a separate range, so SUM adds them in one formula. The header rows between blocks are skipped as text.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#REF!` | A referenced cell was deleted. | Restore the cell or rewrite the reference. |
| `#NAME?` | The function name is misspelled or a named range is missing. | Check the spelling and the Name Manager. |
| Total is too high | The range includes a header row with a number, or a total row. | Start the range below the header and exclude total rows. |
| Total is zero | The cells contain numbers stored as text. | Convert the cells to numbers with VALUE or Paste Special. |
| Circular reference warning | The SUM range includes the cell that holds the formula. | Move the formula outside the summed range. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Excel for the web | Up to 255 arguments. Supports three-dimensional references across sheets, such as `=SUM(Jan:Mar!B2)`. |
| Google Sheets | Available | The arguments are named `value1` and `value2` onward. Long lists of arguments are rarely needed, because ranges cover most cases. Three-dimensional references are not supported, so each sheet must be listed. |

## Tips and Best Practices

- Use a range such as `=SUM(A2:A100)` instead of a chain of plus signs, so the formula grows with the data.
- Start full-column references below the header row when the header might contain a number.
- Use SUBTOTAL instead of SUM when the list is filtered and the total should follow the visible rows.
- Name important ranges, such as `=SUM(MonthlySales)`, so the formula explains itself.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SUBTOTAL](SUBTOTAL.md) | Totals only visible rows and ignores nested subtotals. |
| [SUMIF](SUMIF.md) | Totals rows that match one condition. |
| [SUMIFS](SUMIFS.md) | Totals rows that match several conditions. |
| [SUMPRODUCT](SUMPRODUCT.md) | Multiplies arrays before summing, for example quantity times price. |
| [SUMSQ](SUMSQ.md) | Sums the squares of the values instead of the values themselves. |

## Official Documentation

- [Microsoft Support: SUM function](https://support.microsoft.com/en-us/excel/functions/sum-function)
- [Google Docs Editors Help: SUM](https://support.google.com/docs/answer/3093669)
