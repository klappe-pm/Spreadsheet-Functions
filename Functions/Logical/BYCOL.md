---
domain: Spreadsheet Functions
category: Logical
subcategory: Lambda Helpers
purpose:
  - Array Shaping
use-case:
  - Column Maximums
  - Monthly Column Totals
related:
  - BYROW
  - LAMBDA
  - MAKEARRAY
  - MAP
  - REDUCE
  - SCAN
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/bycol-function
  - https://support.google.com/docs/answer/12571032
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - By Column
  - Column Lambda
tags:
  - dynamic-array
  - excel
  - lambda
  - sheets
---

# BYCOL

## Description

**BYCOL** splits an array or range into its columns, applies a LAMBDA to each column, and returns one result per column in a single row. Each LAMBDA receives an entire column as one value, so a calculation such as a sum or a maximum works on the whole column at once.

Use BYCOL when the same calculation belongs to every column, such as the monthly total of each cost center or the peak reading of each sensor. Without it, you would write one formula per column and copy them across. Because the LAMBDA is written inline, the logic stays in one formula.

The row-based counterpart is [BYROW](BYROW.md), which runs the same kind of LAMBDA on each row. [MAP](MAP.md) works cell by cell, and [REDUCE](REDUCE.md) and [SCAN](SCAN.md) combine values into a single result or a running result. [LAMBDA](LAMBDA.md) defines the custom calculation that BYCOL applies.

BYCOL is a dynamic array function. In Microsoft Excel it is available in Microsoft 365, Excel for the web, Excel 2024, and Excel 2024 for Mac. In Google Sheets it is available with the same purpose, but the LAMBDA takes a name for the current column in the form `LAMBDA(name, expression)`.

## Syntax

```excel
=BYCOL(array, LAMBDA(column, formula))
```

<!-- Image 1: Column Grouping Diagram. See Images/Logical/BYCOL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array to split into columns, such as `B2:D4`. In Google Sheets this argument is named array_or_range. |
| `LAMBDA` | Yes | A LAMBDA that receives one column and returns a single value. Both Excel and Sheets require it to return one value per column. |
| `column` | Yes | The parameter name you give inside the LAMBDA. It stands for the current column. The name is your choice, such as `values` or `column`. |

### Return Value

A row array with one value for each column of the input. A three-column input returns three values. Excel spills the row into the cells to the right of the formula, so those cells must be empty.

## Examples

All examples use this table in B2:D4, where each row is a call center and each column is a day.

| Center | Monday | Tuesday | Wednesday |
| --- | --- | --- | --- |
| A | 40 | 35 | 52 |
| B | 28 | 31 | 25 |
| C | 19 | 44 | 38 |

### Example 1: Total for Each Day

```excel
=BYCOL(B2:D4, LAMBDA(values, SUM(values)))
```

**Result:** `87`, `110`, `115` across three cells

Each column is added up separately. Monday totals 87, Tuesday totals 110, and Wednesday totals 115.

### Example 2: Busiest Center Each Day

```excel
=BYCOL(B2:D4, LAMBDA(values, MAX(values)))
```

**Result:** `40`, `44`, `52`

The formula returns the highest call count on each day. Center A had the most calls on Monday and Wednesday, and Center C had the most on Tuesday.

<!-- Image 2: Columns Passed to the LAMBDA. See Images/Logical/BYCOL.md -->

### Example 3: Counting Days Over a Limit

```excel
=BYCOL(B2:D4, LAMBDA(values, COUNTIF(values, ">30")))
```

**Result:** `1`, `3`, `2`

COUNTIF runs inside the LAMBDA on each column and counts the values above 30. Monday has one (40), Tuesday has three (35, 31, and 44), and Wednesday has two (52 and 38).

### Example 4: Google Sheets Form

```excel
=BYCOL(B2:D4,LAMBDA(column,MAX(column)))
```

**Result:** `40`, `44`, `52`

The Sheets version uses a named parameter, here `column`, and the same result as Example 2. Use the form that matches the platform where the sheet will be opened.

## Story Problems

### Problem 1: Daily Call Volume

A support manager reviews calls handled by three call centers from Monday to Wednesday. She wants the total calls for each day, not each center.

| Center | Monday | Tuesday | Wednesday |
| --- | --- | --- | --- |
| North | 22 | 18 | 30 |
| South | 14 | 27 | 19 |
| West | 25 | 16 | 21 |

**Task:** Enter the formula in B6 and let it spill across B6:D6 to show the total calls for each day.

**Solution:**

```excel
=BYCOL(B2:D4, LAMBDA(values, SUM(values)))
```

**Answer:** `61`, `61`, and `70` calls. Together they add up to 192, the same total as summing all nine cells.

<!-- Image 3: Call Volume Totals. See Images/Logical/BYCOL.md -->

### Problem 2: Peak Sensor Readings

A lab records temperatures from three sensors at four hours. Each column is one sensor. The lab wants the highest reading for each sensor.

| Hour | Sensor A | Sensor B | Sensor C |
| --- | --- | --- | --- |
| 1 | 21 | 19 | 23 |
| 2 | 24 | 22 | 20 |
| 3 | 26 | 18 | 25 |
| 4 | 22 | 21 | 24 |

**Task:** Enter the formula in B7 and let it spill across B7:D7 to show the peak reading for each sensor.

**Solution:**

```excel
=BYCOL(B2:D5, LAMBDA(values, MAX(values)))
```

**Answer:** `26`, `22`, and `25`. Sensor A peaks at 26 in hour 3, Sensor B at 22 in hour 2, and Sensor C at 25 in hour 3.

## Use Cases

### Monthly Column Totals

**Scenario:** A budget sheet has one column for each cost center and one row for each expense. The controller needs the total spend for every cost center without changing the layout.

```excel
=BYCOL(Budget, LAMBDA(column, SUM(column)))
```

**Why It Works:** The LAMBDA runs once per cost center, so new expense rows are included when the range grows. Name the range `Budget` to keep the formula readable.

### Column Maximums for Quality Checks

**Scenario:** A production log stores one measurement per column for each batch. Quality control needs the highest value each measurement reached.

```excel
=BYCOL(Measurements, LAMBDA(column, MAX(column)))
```

**Why It Works:** One formula checks every measurement column. If the maximum for a column exceeds its limit, the value is visible in the output row without a separate formula per column.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` (Incorrect Parameters) | The LAMBDA has the wrong number of parameters. | Give the LAMBDA exactly one parameter for the column. |
| `#CALC!` | The LAMBDA is missing, or it returns more than one value. | Make the LAMBDA return a single value, such as a SUM or MAX. |
| `#SPILL!` | The cells below or beside the result already hold data. | Clear the output cells so the row can spill. |
| Wrong values | The formula inside the LAMBDA refers to a cell instead of the column parameter. | Use the parameter name, such as `values`, inside the LAMBDA. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel for the web, Excel 2024, and Excel 2024 for Mac | Returns a spilled row. The LAMBDA is written as `LAMBDA(column, formula)`. |
| Google Sheets | Available | Written as `BYCOL(array_or_range, LAMBDA)`. The LAMBDA is written as `LAMBDA(name, formula)`, where the name stands for the current column. |

## Tips and Best Practices

- Use descriptive parameter names, such as `values`, so the LAMBDA reads like a sentence.
- Name the input range, so the formula keeps working when rows are added.
- Test the LAMBDA on one column with a simple function before you add complexity.
- Use BYROW when the calculation belongs to each row rather than each column.
- Keep the output range empty, because a spilled result cannot write over existing cells.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BYROW](BYROW.md) | Applies the same kind of LAMBDA to each row. |
| [LAMBDA](LAMBDA.md) | Defines the custom calculation that BYCOL runs on each column. |
| [MAKEARRAY](MAKEARRAY.md) | Builds an array from a LAMBDA that receives row and column numbers. |
| [MAP](MAP.md) | Applies a LAMBDA to each value separately. |
| [REDUCE](REDUCE.md) | Combines all values into one accumulated result. |
| [SCAN](SCAN.md) | Returns each step of an accumulation, such as a running total. |

## Official Documentation

- [Microsoft Support: BYCOL function](https://support.microsoft.com/en-us/excel/functions/bycol-function)
- [Google Docs Editors Help: BYCOL](https://support.google.com/docs/answer/12571032)
