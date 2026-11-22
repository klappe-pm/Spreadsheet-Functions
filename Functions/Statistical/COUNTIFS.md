---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
purpose:
  - Conditional Logic
  - Counting
use-case:
  - Certification Pass Tracking
  - Late Shipment Reports
  - Stock Reorder Checks
related:
  - AVERAGEIFS
  - COUNTIF
  - COUNTUNIQUEIFS
  - FILTER
  - SUMIFS
  - SUMPRODUCT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/countifs-function
  - https://support.google.com/docs/answer/3256550
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Count If Multiple Conditions
  - Multi Criteria Count
tags:
  - counting
  - criteria
  - excel
  - multi-criteria
  - sheets
---

# COUNTIFS

## Description

**COUNTIFS** counts the rows where every condition in a set of conditions is true at the same time. Each condition pairs a range with a criteria, so the function asks, for each row, "Does this row pass test 1, test 2 and test 3?" Use it for questions such as "How many East orders are Open?" or "How many Support staff passed with a score of 80 or more?"

The conditions combine with AND logic. A row is counted only when its cell in every criteria range meets that range's criteria. For OR logic, add separate COUNTIF or COUNTIFS results, because a single COUNTIFS call cannot express "East or West."

Each criteria accepts the same forms as COUNTIF: a number, text, an expression such as `">=30"`, a cell reference, or a text pattern with the wildcards `*` and `?`. Wildcards apply only to text. The ranges do not need to be next to each other, but every range must have the same number of rows and columns as the first one.

For a total of matching values rather than a count, use SUMIFS. For matching values that sit in more than one column or need arithmetic, use SUMPRODUCT.

## Syntax

```excel
=COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```

<!-- Image 1: COUNTIFS Syntax Anatomy. See Images/Statistical/COUNTIFS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `criteria_range1` | Yes | The first range to test. Its size sets the size every other range must match. |
| `criteria1` | Yes | The condition applied to `criteria_range1`. It can be a number, text, an expression, a cell reference or a wildcard pattern. |
| `criteria_range2, criteria2, ...` | No | Additional pairs of range and condition. Microsoft Excel accepts up to 127 pairs. |

### Return Value

A whole number: the count of rows that satisfy every condition. It returns 0 when no row passes all of them. Every range must match the size of `criteria_range1`, so fix any size mismatch before you read the count.

## Examples

All examples use this order list in `A1:C8`, with headers in row 1.

| Region | Units | Status |
| --- | --- | --- |
| East | 12 | Open |
| West | 45 | Closed |
| East | 30 | Closed |
| North | 8 | Open |
| West | 60 | Open |
| East | 22 | Closed |
| South | 15 | Open |

### Example 1: Two Text Conditions

```excel
=COUNTIFS(A2:A8, "East", C2:C8, "Open")
```

**Result:** `1`

Only row 2 is both East and Open. Row 4 and row 7 are East but Closed, so they do not count.

### Example 2: Text and Numeric Conditions

```excel
=COUNTIFS(A2:A8, "East", B2:B8, ">20")
```

**Result:** `2`

Rows 4 (30 units) and 7 (22 units) are East and above 20 units. Row 2 is East with 12 units, so it is excluded.

### Example 3: Two Conditions on the Same Column

```excel
=COUNTIFS(B2:B8, ">=10", B2:B8, "<=30")
```

**Result:** `4`

Reading the same range twice creates a band. The units 12, 30, 22 and 15 fall between 10 and 30 inclusive.

<!-- Image 2: AND Logic in a COUNTIFS Formula. See Images/Statistical/COUNTIFS.md -->

### Example 4: Wildcard With a Second Condition

```excel
=COUNTIFS(A2:A8, "*th", C2:C8, "Open")
```

**Result:** `2`

Both North and South end with "th". North is Open, and South is Open, so both rows count.

### Example 5: Conditions From Cells

Cell `E2` holds `West` and cell `F2` holds `Closed`.

```excel
=COUNTIFS(A2:A8, E2, C2:C8, F2)
```

**Result:** `1`

Row 3 is the only West order that is Closed. Changing `E2` or `F2` changes the count without editing the formula.

### Example 6: Three Conditions

```excel
=COUNTIFS(A2:A8, "East", B2:B8, ">=20", C2:C8, "Closed")
```

**Result:** `2`

Rows 4 and 7 are East, at least 20 units, and Closed. Row 2 fails the Closed test.

## Story Problems

### Problem 1: Certification Pass Tracking

A training coordinator keeps one row per employee in `A1:D9`.

| Employee | Team | Passed | Score |
| --- | --- | --- | --- |
| Ruiz | Support | Yes | 88 |
| Chen | Support | No | 72 |
| Okafor | Sales | Yes | 91 |
| Patel | Support | Yes | 76 |
| Lindqvist | Sales | Yes | 84 |
| Moreau | Support | Yes | 95 |
| Nakamura | Sales | No | 65 |
| Reyes | Support | Yes | 80 |

**Task:** Count the Support team members who passed and scored 80 or higher.

**Solution:**

```excel
=COUNTIFS(B2:B9, "Support", C2:C9, "Yes", D2:D9, ">=80")
```

**Answer:** `3`. Ruiz (88), Moreau (95) and Reyes (80) meet all three tests. Patel passed but scored 76, and Chen did not pass.

<!-- Image 3: Certification Result. See Images/Statistical/COUNTIFS.md -->

### Problem 2: Late Shipments From the West

A logistics planner tracks shipments in `A1:D9`.

| Shipment | Region | Days Late | Status |
| --- | --- | --- | --- |
| S201 | West | 3 | Late |
| S202 | East | 1 | Late |
| S203 | West | 0 | On Time |
| S204 | West | 5 | Late |
| S205 | North | 4 | Late |
| S206 | West | 2 | Late |
| S207 | West | 4 | On Time |
| S208 | South | 6 | Late |

**Task:** Count the West shipments that are Late and more than 2 days late.

**Solution:**

```excel
=COUNTIFS(B2:B9, "West", C2:C9, ">2", D2:D9, "Late")
```

**Answer:** `2`. Shipments S201 (3 days) and S204 (5 days) qualify. S206 is only 2 days late, and S207 is On Time.

## Use Cases

### Certification Pass Tracking

**Scenario:** A team lead wants the number of Support staff who passed the certification with at least the pass mark kept in cell `H1`.

```excel
=COUNTIFS(Team, "Support", Passed, "Yes", Score, ">="&H1)
```

**Why It Works:** Named ranges make the formula readable. Joining the operator to `H1` keeps the pass mark editable without changing the formula.

### Late Shipment Reports

**Scenario:** An operations manager counts West shipments that are both Late and more than two days behind.

```excel
=COUNTIFS(Shipments[Region], "West", Shipments[Status], "Late", Shipments[Days Late], ">2")
```

**Why It Works:** Structured references follow the table as new shipments are added. Each condition narrows the count, so the result matches only the rows that qualify on all three tests.

### Stock Reorder Checks

**Scenario:** A purchasing clerk counts Electronics items whose on-hand quantity has fallen below the reorder threshold stored in `H1`.

```excel
=COUNTIFS(Stock[Category], "Electronics", Stock[On Hand], "<"&$H$1)
```

**Why It Works:** Comparing a column to a single threshold is a standard COUNTIFS pattern. The threshold lives in one cell, so purchasing can change it in one place.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error or no result | The criteria ranges have different numbers of rows or columns. | Select ranges of the same height and width, such as `A2:A100` and `B2:B100`. |
| `0` or a count that is too low | Conditions use AND logic, and no row passes all of them. | Test each condition with COUNTIF to see which one removes every row. |
| `0` returned unexpectedly | A criteria cell is empty, so the criteria is treated as 0. | Check that every criteria cell contains a value. |
| Count lower than an OR total | COUNTIFS cannot combine alternatives inside one call, so it applies AND. | Add separate COUNTIFS results, one for each alternative. |
| Wildcards have no effect | Wildcards are used with a number comparison. | Use operators such as `">10"` for numbers and wildcards for text. |
| Unexpected count | The comparison is typed without quotation marks, as in `>50`. | Put the whole criteria in quotes: `">50"`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Up to 127 range and criteria pairs. Text criteria are not case-sensitive. Ranges do not need to be adjacent. |
| Google Sheets | Available | Same argument pattern as Excel, with the same rule that every range matches the size of the first. |

## Tips and Best Practices

- Match every range to the first range's row count and column count before you copy the formula.
- Write AND conditions in one formula, and write OR conditions as separate formulas that you add together.
- Use the same range twice with different operators to count values between two limits.
- Put each threshold in its own cell so the question can change without editing the formula.
- Use `"<>"` to exclude blank cells from a count, for example `COUNTIFS(A2:A100, "Sales", B2:B100, "<>")`.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNTIF](COUNTIF.md) | Counts with one condition only. |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Adds values that meet several conditions. |
| [AVERAGEIFS](AVERAGEIFS.md) | Averages values that meet several conditions. |
| [COUNTUNIQUEIFS](../Database/COUNTUNIQUEIFS.md) | Counts unique values that meet several conditions in Google Sheets. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the matching rows instead of a count. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Handles OR logic and arithmetic that COUNTIFS cannot express. |

## Official Documentation

- [Microsoft Support: COUNTIFS function](https://support.microsoft.com/en-us/excel/functions/countifs-function)
- [Google Docs Editors Help: COUNTIFS](https://support.google.com/docs/answer/3256550)
