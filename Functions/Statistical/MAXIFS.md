---
domain: Spreadsheet Functions
category: Statistical
subcategory: Conditional Extremes
purpose:
  - Aggregation
  - Conditional Logic
use-case:
  - Best Sale by Region and Year
  - Highest Price in a Category
related:
  - AVERAGEIFS
  - COUNTIFS
  - MAX
  - MINIFS
  - SUMIFS
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/maxifs-function
  - https://support.google.com/docs/answer/7013817
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Conditional Maximum
  - Maximum If Condition
tags:
  - aggregation
  - conditional
  - excel
  - maximum
  - sheets
---

# MAXIFS

## Description

**MAXIFS** returns the largest value in one range, but only for the rows that meet one or more conditions. It answers questions such as "What was the highest sale in the East region?" or "What was the longest wait for a high priority ticket?" Without MAXIFS, the same answer needs MAX with an array formula, which is harder to read and maintain.

The first argument is the range that holds the values to compare. Each condition then takes a pair: a criteria range and a criterion. Every condition must be true for a row to count, so the conditions work as an AND test. A criterion can be a number, text, a cell reference, a comparison such as `">1000"`, or a wildcard pattern such as `"North*"`. Text matching is not case sensitive.

MAXIFS returns 0 when no row meets every condition. A 0 can be a real maximum, so check the match count with COUNTIFS when a zero would be misleading. For OR logic, add separate MAXIFS results together with MAX. For the smallest matching value, use MINIFS. MAXIFS requires Excel 2019, Excel 2021, Excel 2024, or Microsoft 365 in Excel, so it does not work in Excel 2016 or earlier.

## Syntax

```excel
=MAXIFS(max_range, criteria_range1, criterion1, [criteria_range2, criterion2], ...)
```

<!-- Image 1: Max Range and Criteria Pairs. See Images/Statistical/MAXIFS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `max_range` | Yes | The range of values to compare, such as `C2:C8`. Must contain numbers for the result to be meaningful. |
| `criteria_range1` | Yes | The range tested against `criterion1`. It must be the same size and shape as `max_range`. |
| `criterion1` | Yes | The test applied to `criteria_range1`, such as `"East"`, `">1000"`, or a cell reference. |
| `criteria_range2, criterion2, ...` | No | Additional range and criterion pairs. Every row must meet all of them. Excel allows up to 126 pairs. |

### Return Value

A single number: the largest value in `max_range` among rows that meet every condition. It returns 0 when no row meets all conditions. It returns `#VALUE!` when the ranges are not the same size.

## Examples

All examples use the sales list below in `A1:C8`, with the header in row 1.

| Region | Product | Sales |
| --- | --- | --- |
| East | Widgets | 1200 |
| West | Gadgets | 850 |
| East | Gadgets | 640 |
| North | Widgets | 975 |
| East | Widgets | 410 |
| West | Widgets | 1530 |
| East | Gadgets | 1010 |

### Example 1: One Condition

```excel
=MAXIFS(C2:C8, A2:A8, "East")
```

**Result:** `1200`

Only the four East rows are considered (1200, 640, 410, and 1010), and 1200 is the largest.

### Example 2: Two Conditions

```excel
=MAXIFS(C2:C8, A2:A8, "East", B2:B8, "Gadgets")
```

**Result:** `1010`

Only rows that are both East and Gadgets qualify: 640 and 1010. The larger of the two is 1010.

<!-- Image 2: Two Conditions Filtering Rows. See Images/Statistical/MAXIFS.md -->

### Example 3: Numeric Comparison

```excel
=MAXIFS(C2:C8, C2:C8, "<1000")
```

**Result:** `975`

The criteria range is the same as the values range. Sales below 1000 are 850, 640, 975, and 410, so 975 is the largest.

### Example 4: Criterion From a Cell

Assume cell `G1` contains `North`.

```excel
=MAXIFS(C2:C8, A2:A8, G1)
```

**Result:** `975`

Changing the text in `G1` updates the result, which suits a report where users choose the region.

### Example 5: No Match Returns Zero

```excel
=MAXIFS(C2:C8, A2:A8, "South")
```

**Result:** `0`

No row has the region South, so the result is 0. Use COUNTIFS to confirm that matches exist before you show this value.

## Story Problems

### Problem 1: Best Month for Riverside

A retail chain records monthly revenue for two stores in `A1:C7`.

| Month | Store | Revenue |
| --- | --- | --- |
| Jan | Riverside | 18400 |
| Jan | Hillcrest | 15200 |
| Feb | Riverside | 21950 |
| Feb | Hillcrest | 14800 |
| Mar | Riverside | 19875 |
| Mar | Hillcrest | 16300 |

**Task:** Find the highest monthly revenue for the Riverside store.

**Solution:**

```excel
=MAXIFS(C2:C7, B2:B7, "Riverside")
```

**Answer:** `21950`, the February revenue at Riverside. The Hillcrest rows are excluded by the condition.

### Problem 2: Longest Wait for High Priority Tickets

A help desk logs the wait time in minutes for each ticket in `A1:C7`.

| Ticket | Priority | Wait |
| --- | --- | --- |
| T1 | High | 42 |
| T2 | Low | 15 |
| T3 | High | 67 |
| T4 | Medium | 30 |
| T5 | High | 55 |
| T6 | Low | 90 |

**Task:** Find the longest wait for any high priority ticket.

**Solution:**

```excel
=MAXIFS(C2:C7, B2:B7, "High")
```

**Answer:** `67` minutes, from ticket T3. The 90-minute wait on T6 is a low priority ticket, so it is excluded.

<!-- Image 3: Story Problem Result. See Images/Statistical/MAXIFS.md -->

## Use Cases

### Best Sale by Region and Year

**Scenario:** A regional manager wants the largest single sale for the Northeast region in 2025.

```excel
=MAXIFS(Sales[Amount], Sales[Region], "Northeast", Sales[Year], 2025)
```

**Why It Works:** Both conditions must match, so sales from other regions or years are ignored. Combine the result with INDEX and MATCH to find the rep who made the sale.

### Highest Price in a Category

**Scenario:** A buyer wants the most expensive item in a product category that is still in stock.

```excel
=MAXIFS(Catalog[Price], Catalog[Category], "Premium", Catalog[InStock], TRUE)
```

**Why It Works:** The logical TRUE is accepted as a criterion, so only in-stock rows count. Use COUNTIFS with the same criteria to check that matches exist.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The criteria ranges are not the same size as `max_range`. | Make every range cover the same rows, for example `C2:C8` and `A2:A8`. |
| `0` | No row meets every condition. | Check the match count with COUNTIFS before you rely on the result. |
| `#NAME?` | The function is not available in the version of Excel in use. | Use Excel 2019, Excel 2021, Excel 2024, or Microsoft 365, or use MAX with IF as an array formula. |
| Wrong result | A number is stored as text, so `">1000"` or `1000` does not match it. | Convert the cells to numbers before calculating. |
| Wrong result | Trailing spaces in the data prevent an exact text match. | Clean the data with TRIM, or use a wildcard such as `"East*"`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2019, Excel 2021, Excel 2024, Microsoft 365, Excel for the web, and Office for iPhone | Up to 126 range and criterion pairs. Returns 0 when no row matches. |
| Google Sheets | Available | The help page describes the same syntax and returns 0 when no row matches. It lists no version requirement. |

## Tips and Best Practices

- Keep the value range and every criteria range the same size so the rows line up.
- Put criteria in labeled cells and reference them, so users can change the question without editing the formula.
- Check the match count with COUNTIFS whenever a 0 result could be a real value.
- For the top N matches rather than the single largest, use FILTER with LARGE.
- Use a table reference such as `Sales[Amount]` so new rows are included automatically.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MAX](MAX.md) | Returns the largest value with no conditions. |
| [MINIFS](MINIFS.md) | Returns the smallest value that meets the same kind of conditions. |
| [COUNTIFS](COUNTIFS.md) | Counts the rows that meet the conditions, to confirm that matches exist. |
| [AVERAGEIFS](AVERAGEIFS.md) | Averages the rows that meet the conditions. |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Adds the values that meet the same kind of conditions. |

## Official Documentation

- [Microsoft Support: MAXIFS function](https://support.microsoft.com/en-us/excel/functions/maxifs-function)
- [Google Docs Editors Help: MAXIFS](https://support.google.com/docs/answer/7013817)
