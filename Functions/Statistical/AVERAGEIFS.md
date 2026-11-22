---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Aggregation
  - Conditional Logic
use-case:
  - Regional Product Averages
  - Shift Productivity Reports
  - Warranty Claim Costs
related:
  - AVERAGE
  - AVERAGEIF
  - COUNTIFS
  - DAVERAGE
  - SUMIFS
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/averageifs-function
  - https://support.google.com/docs/answer/3256534
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Multiple Criteria Average
tags:
  - averages
  - conditional
  - criteria
  - excel
  - sheets
---

# AVERAGEIFS

## Description

**AVERAGEIFS** averages the cells in one range that meet every condition in a set of conditions. Each condition pairs a range with a criterion. A cell is included only when it satisfies all of the pairs at once, so the function answers questions such as "What is the average tickets handled by the day shift in the billing team?"

The function takes the average range first, followed by one or more criteria range and criterion pairs. Excel allows up to 127 pairs. Every criteria range must be the same size and shape as the average range, which is the main difference from AVERAGEIF, where the average range is optional and can be resized.

Use AVERAGEIFS when two or more conditions must hold together. For a single condition, AVERAGEIF is shorter. For conditions that join with OR, add the separate averages with a formula or use a single condition that lists the choices. The criteria accept the same comparison operators, wildcards and cell references as AVERAGEIF. Excel and Google Sheets both support this function with the same argument order.

## Syntax

```excel
=AVERAGEIFS(average_range, criteria_range1, criterion1, [criteria_range2, criterion2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/AVERAGEIFS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `average_range` | Yes | The numbers to average. Blank and text cells in this range are not averaged. |
| `criteria_range1` | Yes | The first range to test. It must be the same size and shape as `average_range`. |
| `criterion1` | Yes | The condition applied to `criteria_range1`, such as `"Billing"`, `">30"` or a cell reference. |
| `criteria_range2, criterion2, ...` | No | Additional range and condition pairs. Excel accepts up to 127 pairs. Every range must match the size and shape of `average_range`. |

### Return Value

A number: the arithmetic mean of the cells in `average_range` whose matching cells satisfy every condition. Excel returns `#DIV/0!` when no cell meets all of the conditions, and when the average range is blank or contains text that cannot be averaged.

## Examples

All examples use this list in `A1:C7`. Department is in column A, shift in column B, and tickets handled in column C.

| Department | Shift | Tickets |
| --- | --- | --- |
| Billing | Day | 40 |
| Billing | Night | 35 |
| Claims | Day | 52 |
| Billing | Day | 48 |
| Claims | Night | 30 |
| Billing | Day | 44 |

### Example 1: Two Text Conditions

```excel
=AVERAGEIFS(C2:C7, A2:A7, "Billing", B2:B7, "Day")
```

**Result:** `44`

Three rows are Billing on the day shift, with 40, 48 and 44 tickets. Their total is 132, and dividing by three gives 44.

### Example 2: One Condition Among Two Rows

```excel
=AVERAGEIFS(C2:C7, A2:A7, "Claims")
```

**Result:** `41`

Only one condition is needed here, so the formula uses one pair. The two Claims rows hold 52 and 30, which average to 41.

### Example 3: A Numeric Condition Combined With a Text Condition

```excel
=AVERAGEIFS(C2:C7, B2:B7, "Night", C2:C7, ">30")
```

**Result:** `35`

Night rows are 35 and 30. The second condition keeps only values greater than 30, which leaves 35 alone.

<!-- Image 2: Every Condition Must Hold. See Images/Statistical/AVERAGEIFS.md -->

### Example 4: Conditions From Cells

Cell `F1` holds `Billing`, and cell `F2` holds `Night`.

```excel
=AVERAGEIFS(C2:C7, A2:A7, F1, B2:B7, F2)
```

**Result:** `35`

The criteria come from cells, so a manager can change the question by typing a different department or shift.

## Story Problems

### Problem 1: Coffee Sales at the North Store

A chain records each sale by store and product in `A1:C7`.

| Store | Product | Sales |
| --- | --- | --- |
| North | Coffee | 420 |
| South | Coffee | 380 |
| North | Tea | 150 |
| North | Coffee | 480 |
| South | Tea | 210 |
| North | Coffee | 360 |

**Task:** Find the average sale for coffee at the North store only.

**Solution:**

```excel
=AVERAGEIFS(C2:C7, A2:A7, "North", B2:B7, "Coffee")
```

**Answer:** `420`. The three North coffee sales are 420, 480 and 360. They total 1260, and dividing by three gives 420.

### Problem 2: Commute Times on Line 4 at Peak

A transit analyst logs each trip's line, whether it ran at peak time, and its minutes in `A1:C7`.

| Line | Peak | Minutes |
| --- | --- | --- |
| Line 4 | Yes | 34 |
| Line 2 | Yes | 28 |
| Line 4 | No | 22 |
| Line 4 | Yes | 40 |
| Line 4 | Yes | 31 |
| Line 2 | No | 19 |

**Task:** Find the average trip time on Line 4 during peak hours.

**Solution:**

```excel
=AVERAGEIFS(C2:C7, A2:A7, "Line 4", B2:B7, "Yes")
```

**Answer:** `35` minutes. The three qualifying trips take 34, 40 and 31 minutes. They total 105, and dividing by three gives 35.

<!-- Image 3: Results Panel for the Commute Problem. See Images/Statistical/AVERAGEIFS.md -->

## Use Cases

### Regional Product Averages

**Scenario:** A regional manager reports the average unit price of one product in one region, using a sales table that is updated every day.

```excel
=AVERAGEIFS(Sales[Price], Sales[Region], "West", Sales[Product], "Widget")
```

**Why It Works:** The structured references keep the three columns aligned as rows are added. Each extra condition narrows the average to a more specific group.

### Shift Productivity Reports

**Scenario:** A warehouse supervisor wants the average picks per hour for night-shift workers who worked at least a full shift.

```excel
=AVERAGEIFS(Picks[PerHour], Picks[Shift], "Night", Picks[Hours], ">=8")
```

**Why It Works:** The second condition removes partial shifts before the average is taken. Keep the threshold in a labeled cell if the supervisor needs to change it.

### Warranty Claim Costs

**Scenario:** A service manager compares average repair cost for one product model that was claimed in one year.

```excel
=IFERROR(AVERAGEIFS(Claims[Cost], Claims[Model], $B2, Claims[Year], 2025), "No claims")
```

**Why It Works:** IFERROR shows a readable label when no claims match the model and year, which is common for newer models.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | No row meets every condition. | Check each criterion for spelling and case, or wrap the formula in IFERROR. |
| `#VALUE!` | A criteria range is a different size or shape from the average range. | Make every range the same number of rows and columns. |
| Unexpected result | An empty criteria cell is treated as 0, so it matches only zeros. | Fill or remove blank criteria cells before averaging. |
| Unexpected result | A text number in the average range is not averaged. | Convert the values to numbers first. |
| Unexpected result | A wildcard in a criterion matches more rows than intended. | Use a tilde before `*` or `?` to match the character itself. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2007 and later, including Excel for the web | Up to 127 criteria range and criterion pairs. Wildcards and comparison operators work in criteria. |
| Google Sheets | Available | Uses the same argument order. The help page does not describe the no-match result, so check it in your file. |

## Tips and Best Practices

- Start with the most selective condition, then add others until the result matches the question.
- Put criteria in labeled cells so the report can be filtered without editing the formula.
- Check that every range covers the same rows; a mismatch is a common source of errors.
- Use COUNTIFS beside AVERAGEIFS to show how many rows the average is based on.
- Use DAVERAGE when the criteria already live in a database-style block on the sheet.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Averages every numeric value with no conditions. |
| [AVERAGEIF](AVERAGEIF.md) | Averages cells that meet one condition, with an optional resizable average range. |
| [COUNTIFS](COUNTIFS.md) | Counts the rows that meet the same conditions, for the sample size. |
| [DAVERAGE](../Database/DAVERAGE.md) | Averages a database field for rows that match a criteria block. |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Adds the matching values instead of averaging them. |

## Official Documentation

- [Microsoft Support: AVERAGEIFS function](https://support.microsoft.com/en-us/excel/functions/averageifs-function)
- [Google Docs Editors Help: AVERAGEIFS](https://support.google.com/docs/answer/3256534)
