---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Conditional Sums
purpose:
  - Aggregation
  - Conditional Logic
use-case:
  - Date Range Revenue
  - Paid Invoice Totals
  - Quarterly Regional Sales
related:
  - AVERAGEIFS
  - COUNTIFS
  - DSUM
  - FILTER
  - SUMIF
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/sumifs-function
  - https://support.google.com/docs/answer/3238496
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Multi Criteria Sum
  - Sum If Multiple
tags:
  - aggregation
  - excel
  - multiple-criteria
  - sheets
---

# SUMIFS

## Description

**SUMIFS** adds the values in one range when the matching rows pass two or more tests. Each test is a pair of a criteria range and a criterion. A row is included only when it passes every test, so the conditions work together with AND logic. Use it for totals such as sales for one region in one quarter with at least a set number of units.

The sum range comes first in SUMIFS, which is the reverse of SUMIF. Every criteria range must have the same number of rows and columns as the sum range. Excel allows up to 127 pairs of criteria range and criterion.

Text criteria match case-insensitively. Wildcards, comparison operators, cell references and date comparisons all work as they do in SUMIF. SUMIFS cannot combine conditions with OR. For OR logic, add two SUMIFS results together, or use SUMPRODUCT or FILTER.

## Syntax

```excel
=SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```

<!-- Image 1: Sum Range and Criteria Pairs. See Images/Math & Trig/SUMIFS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `sum_range` | Yes | The cells to add. It comes first in the formula. |
| `criteria_range1` | Yes | The first range to test. It must be the same size as `sum_range`. |
| `criteria1` | Yes | The condition for `criteria_range1`. It can be a number, text in quotes, a comparison such as `">=5"`, a cell reference, or a wildcard pattern. |
| `criteria_range2, criteria2, ...` | No | More pairs of ranges and criteria. Each range must match the size of `sum_range`. Excel allows up to 127 pairs. |

### Return Value

A single number equal to the total of the sum range for rows that pass every test. The function returns 0 when no row passes all of them.

## Examples

All examples use this sales log in `A2:D7`. Column A is the region, column B is the product, column C is units, and column D is revenue.

| Region | Product | Units | Revenue |
| --- | --- | --- | --- |
| East | Widget | 10 | 500 |
| West | Widget | 4 | 200 |
| East | Gadget | 7 | 840 |
| West | Gadget | 12 | 1440 |
| East | Widget | 3 | 150 |
| North | Widget | 8 | 400 |

### Example 1: Two Conditions

```excel
=SUMIFS(D2:D7, A2:A7, "East", B2:B7, "Widget")
```

**Result:** `650`

Only the East Widget rows qualify, with revenue of 500 and 150.

### Example 2: Text and a Numeric Comparison

```excel
=SUMIFS(D2:D7, A2:A7, "East", C2:C7, ">=5")
```

**Result:** `1340`

East rows with at least five units are the first and third rows, with revenue of 500 and 840.

### Example 3: Exclude a Value

```excel
=SUMIFS(D2:D7, A2:A7, "<>North", B2:B7, "Widget")
```

**Result:** `850`

The `<>` operator removes North. The Widget rows that remain are East (500), West (200) and East (150).

<!-- Image 2: Criteria Read From Cells. See Images/Math & Trig/SUMIFS.md -->

### Example 4: Criteria From Cells

Cell G2 contains `West` and cell G3 contains `Gadget`.

```excel
=SUMIFS(D2:D7, A2:A7, G2, B2:B7, G3)
```

**Result:** `1440`

Changing the values in G2 and G3 changes the total, so one formula serves every selection.

### Example 5: Numeric Range Between Two Limits

```excel
=SUMIFS(D2:D7, C2:C7, ">=4", C2:C7, "<=10")
```

**Result:** `1940`

The same range appears twice, once for each limit. The rows with 4, 7, 8 and 10 units qualify, with revenue of 200, 840, 400 and 500.

### Example 6: Wildcard With a Second Condition

```excel
=SUMIFS(D2:D7, B2:B7, "Wid*", A2:A7, "West")
```

**Result:** `200`

The wildcard matches Widget, and the second pair keeps only the West rows.

## Story Problems

### Problem 1: Training Hours for Sales in Quarter One

A training coordinator records hours by department and quarter in `A1:C6`.

| Department | Quarter | Hours |
| --- | --- | --- |
| Sales | Q1 | 12 |
| Operations | Q1 | 30 |
| Sales | Q2 | 18 |
| Sales | Q1 | 7 |
| Operations | Q2 | 22 |

**Task:** Total the Sales hours for Q1.

**Solution:**

```excel
=SUMIFS(C2:C6, A2:A6, "Sales", B2:B6, "Q1")
```

**Answer:** `19`, from the two Sales Q1 rows (12 and 7).

<!-- Image 3: Two Criteria Table. See Images/Math & Trig/SUMIFS.md -->

### Problem 2: Paid Invoices Above a Threshold

A small studio tracks invoice amounts and status in `A1:B6`. The owner wants the total of paid invoices above 1000.

| Status | Amount |
| --- | --- |
| Paid | 1200 |
| Open | 900 |
| Paid | 450 |
| Paid | 2100 |
| Open | 1500 |

**Task:** Sum the Amount values where Status is Paid and Amount is greater than 1000.

**Solution:**

```excel
=SUMIFS(B2:B6, A2:A6, "Paid", B2:B6, ">1000")
```

**Answer:** `3300`, from 1200 and 2100. The paid invoice of 450 is below the threshold, and the open invoices are excluded by status.

## Use Cases

### Quarterly Regional Sales

**Scenario:** A regional manager reports online sales for one region and quarter.

```excel
=SUMIFS(Sales[Amount], Sales[Region], "Northeast", Sales[Quarter], "Q4", Sales[Channel], "Online")
```

**Why It Works:** Each criterion narrows the rows, and a change to any cell in the table updates the total. Put the region and quarter in parameter cells so the same formula serves each report.

### Paid Invoice Totals

**Scenario:** An accounts team totals the paid invoices that fall within a payment window.

```excel
=SUMIFS(Invoices[Amount], Invoices[Status], "Paid", Invoices[Due], ">="&StartDate, Invoices[Due], "<="&EndDate)
```

**Why It Works:** The start and end dates are joined to their operators with `&`, so the window can come from named cells. Dates must be real dates, not text, or the comparison will not match.

### Date Range Revenue

**Scenario:** A finance team compares revenue for the current year with the same period last year.

```excel
=SUMIFS(Revenue[Amount], Revenue[Date], ">="&DATE(2025,1,1), Revenue[Date], "<="&DATE(2025,12,31))
```

**Why It Works:** Using the same date range twice creates an inclusive window. Change the DATE arguments to move the comparison to the prior year.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The sum range and the criteria ranges are different sizes. | Make every range the same number of rows and columns. |
| `0` | A criterion is a text value without quotes, or no row passes every test. | Put text in quotes and test each criterion alone with SUMIF. |
| Argument order error | The SUMIF order was used, with the sum range last. | Place the sum range first, then the criteria pairs. |
| Unexpected total | TRUE and FALSE values in the sum range are counted as 1 and 0. | Keep logical values out of the sum range. |
| No match on text numbers | Numbers stored as text do not match numeric criteria. | Convert the cells to numbers. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available from Excel 2007 onward and in current versions | Up to 127 criteria pairs. In Excel for Microsoft 365, the function works with dynamic array formulas. |
| Google Sheets | Available | The help page does not state a limit on the number of pairs. Wildcards, comparisons and `<>` work as in Excel. |

## Tips and Best Practices

- Keep the sum range first and check the argument order whenever you copy a formula from SUMIF.
- Use named ranges or table references so each formula explains its conditions.
- Create a second range for each limit when you need a numeric window, such as `">=100"` and `"<=200"` on the same column.
- Use SUM with FILTER when the conditions include OR logic.
- Test each criterion alone with SUMIF when the total is zero and you expect matches.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SUMIF](SUMIF.md) | Totals rows that meet one condition. |
| [COUNTIFS](../Statistical/COUNTIFS.md) | Counts rows that meet the same set of conditions. |
| [AVERAGEIFS](../Statistical/AVERAGEIFS.md) | Averages rows that meet the same set of conditions. |
| [DSUM](../Database/DSUM.md) | Totals records that match criteria stored in a block of cells. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the rows that match conditions, including OR logic, for a total. |

## Official Documentation

- [Microsoft Support: SUMIFS function](https://support.microsoft.com/en-us/excel/functions/sumifs-function)
- [Google Docs Editors Help: SUMIFS](https://support.google.com/docs/answer/3238496)
