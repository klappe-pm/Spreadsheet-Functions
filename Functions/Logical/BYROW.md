---
domain: Spreadsheet Functions
category: Logical
subcategory: Lambda Helpers
purpose:
  - Array Shaping
use-case:
  - Batch Peak Scores
  - Weekly Hour Totals
related:
  - BYCOL
  - LAMBDA
  - MAKEARRAY
  - MAP
  - REDUCE
  - SCAN
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/byrow-function
  - https://support.google.com/docs/answer/12570930
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - By Row
  - Row Lambda
tags:
  - dynamic-array
  - excel
  - lambda
  - sheets
---

# BYROW

## Description

**BYROW** splits an array or range into its rows, applies a LAMBDA to each row, and returns one result per row in a single column. Each LAMBDA receives an entire row as one value, so a calculation such as a sum or a maximum works across that row at once.

Use BYROW when the same calculation belongs to every row, such as the total hours for each employee or the best score for each batch. Without it, you would write one formula per row and copy it down. Keeping the LAMBDA inline means the whole rule lives in one formula.

The column-based counterpart is [BYCOL](BYCOL.md), which does the same job for each column. [MAP](MAP.md) works on each cell, and [REDUCE](REDUCE.md) and [SCAN](SCAN.md) combine values into one result or a running result. [LAMBDA](LAMBDA.md) defines the custom calculation that BYROW applies.

Each row must produce a single value. A LAMBDA that returns a nested array is not supported. In Microsoft Excel, BYROW is available in Microsoft 365, Excel for the web, Excel 2024, and Excel 2024 for Mac. In Google Sheets, the LAMBDA takes a name for the current row in the form `LAMBDA(name, expression)`.

## Syntax

```excel
=BYROW(array, LAMBDA(row, formula))
```

<!-- Image 1: Row Grouping Diagram. See Images/Logical/BYROW.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array whose rows are processed, such as `B2:D4`. In Google Sheets this argument is named array_or_range. |
| `LAMBDA` | Yes | A LAMBDA that receives one row and returns a single value for it. |
| `row` | Yes | The parameter name you give inside the LAMBDA. It stands for the current row. The name is your choice, such as `values`. |

### Return Value

A column array with one value for each row of the input. A three-row input returns three values. Excel spills the column into the cells below the formula, so those cells must be empty.

## Examples

All examples use this table in B2:D4, where each row is a store and each column is a month.

| Store | January | February | March |
| --- | --- | --- | --- |
| North | 12 | 15 | 9 |
| South | 7 | 11 | 14 |
| West | 20 | 4 | 6 |

### Example 1: Total for Each Store

```excel
=BYROW(B2:D4, LAMBDA(values, SUM(values)))
```

**Result:** `36`, `32`, `30` down three cells

Each row is added up separately. North totals 36, South totals 32, and West totals 30.

### Example 2: Best Month for Each Store

```excel
=BYROW(B2:D4, LAMBDA(values, MAX(values)))
```

**Result:** `15`, `14`, `20`

The formula returns the highest monthly value for each store. North peaked in February, South in March, and West in January.

<!-- Image 2: Rows Passed to the LAMBDA. See Images/Logical/BYROW.md -->

### Example 3: Counting Strong Months

```excel
=BYROW(B2:D4, LAMBDA(values, COUNTIF(values, ">10")))
```

**Result:** `2`, `2`, `1`

COUNTIF runs on each row and counts the months above 10. North has 12 and 15, South has 11 and 14, and West has only 20.

### Example 4: Google Sheets Form

```excel
=BYROW(B2:D4,LAMBDA(row,SUM(row)))
```

**Result:** `36`, `32`, `30`

The Sheets version names the current row `row` and gives the same totals as Example 1. Use the form that matches the platform where the sheet will be opened.

## Story Problems

### Problem 1: Weekly Hours per Employee

A team lead records hours worked by four employees over three weeks. She needs each person's total.

| Employee | Week 1 | Week 2 | Week 3 |
| --- | --- | --- | --- |
| Ana | 6 | 8 | 7 |
| Ben | 5 | 5 | 6 |
| Cora | 8 | 7 | 9 |
| Dev | 4 | 6 | 5 |

**Task:** Enter the formula in E2 so it spills down E2:E5 with one total for each employee. Then find the employee with the most hours.

**Solution:**

```excel
=BYROW(B2:D5, LAMBDA(values, SUM(values)))
```

**Answer:** `21`, `16`, `24`, and `15` hours. Cora logged the most at 24 hours. The four totals add up to 76.

<!-- Image 3: Weekly Hour Totals. See Images/Logical/BYROW.md -->

### Problem 2: Best Score per Batch

A quality team tests four product batches on three measures. The team wants the best result for each batch.

| Batch | Test 1 | Test 2 | Test 3 |
| --- | --- | --- | --- |
| B1 | 88 | 92 | 79 |
| B2 | 75 | 81 | 90 |
| B3 | 94 | 86 | 97 |
| B4 | 68 | 72 | 80 |

**Task:** Enter the formula in E2 so it spills down E2:E5, then identify the batch with the highest best score.

**Solution:**

```excel
=BYROW(B2:D5, LAMBDA(values, MAX(values)))
```

**Answer:** `92`, `90`, `97`, and `80`. Batch B3 has the highest best score at 97.

## Use Cases

### Batch Peak Scores

**Scenario:** A quality report lists several tests for each batch. Managers want one best score per batch without adding a formula to each row.

```excel
=BYROW(BatchScores, LAMBDA(values, MAX(values)))
```

**Why It Works:** The LAMBDA runs once for each batch row, so new batches are included when the range grows. Name the range `BatchScores` to keep the formula readable.

### Weekly Hour Totals

**Scenario:** A timesheet has one row per employee and one column per week. Payroll needs total hours for each person.

```excel
=BYROW(Timesheet, LAMBDA(values, SUM(values)))
```

**Why It Works:** One formula totals every row. If a week is added as a new column inside the named range, the total updates on its own.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` (Incorrect Parameters) | The LAMBDA has the wrong number of parameters. | Give the LAMBDA exactly one parameter for the row. |
| `#CALC!` | The LAMBDA is missing, or it returns more than one value for a row. | Make the LAMBDA return a single value, such as a SUM or MAX. |
| `#SPILL!` | The cells below the formula already hold data. | Clear the output cells so the column can spill. |
| Nested array result | The LAMBDA returns an array instead of one value. | Reduce the row to one value, for example with SUM or MAX. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel for the web, Excel 2024, and Excel 2024 for Mac | Returns a spilled column. The LAMBDA is written as `LAMBDA(row, formula)`. |
| Google Sheets | Available | Written as `BYROW(array_or_range, LAMBDA)`. The LAMBDA is written as `LAMBDA(name, formula)`, where the name stands for the current row. |

## Tips and Best Practices

- Use a parameter name such as `values` so the LAMBDA explains its purpose.
- Name the input range so the formula keeps working when rows are added.
- Test the LAMBDA on one row first, then copy the logic into BYROW.
- Use BYCOL when the calculation belongs to each column rather than each row.
- Keep the cells below the formula empty, because a spilled result cannot overwrite data.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BYCOL](BYCOL.md) | Applies the same kind of LAMBDA to each column. |
| [LAMBDA](LAMBDA.md) | Defines the custom calculation that BYROW runs on each row. |
| [MAKEARRAY](MAKEARRAY.md) | Builds an array from a LAMBDA that receives row and column numbers. |
| [MAP](MAP.md) | Applies a LAMBDA to each value separately. |
| [REDUCE](REDUCE.md) | Combines all values into one accumulated result. |
| [SCAN](SCAN.md) | Returns each step of an accumulation, such as a running total. |

## Official Documentation

- [Microsoft Support: BYROW function](https://support.microsoft.com/en-us/excel/functions/byrow-function)
- [Google Docs Editors Help: BYROW](https://support.google.com/docs/answer/12570930)
