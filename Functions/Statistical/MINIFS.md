---
domain: Spreadsheet Functions
category: Statistical
subcategory: Conditional Extremes
purpose:
  - Aggregation
  - Conditional Logic
use-case:
  - Cheapest Approved Quote
  - Shortest Express Lead Time
related:
  - AVERAGEIFS
  - COUNTIFS
  - MAXIFS
  - MIN
  - SUMIFS
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/minifs-function
  - https://support.google.com/docs/answer/7014063
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Conditional Minimum
  - Minimum If Condition
tags:
  - aggregation
  - conditional
  - excel
  - minimum
  - sheets
---

# MINIFS

## Description

**MINIFS** returns the smallest value in one range, but only for the rows that meet one or more conditions. It answers questions such as "What is the lowest quote from an approved vendor?" or "What is the shortest express lead time?" Without MINIFS, the same answer needs MIN with an array formula.

The first argument is the range that holds the values to compare. Each condition then takes a pair: a criteria range and a criterion. Every condition must be true for a row to count, so the conditions work as an AND test. A criterion can be a number, text, a cell reference, a comparison such as `"<50"`, or a wildcard pattern such as `"Express*"`. Text matching is not case sensitive.

MINIFS returns 0 when no row meets every condition. For a minimum, a 0 is easy to misread as a real low value, so confirm that matches exist with COUNTIFS first. If zeros in the data mean missing values, add a condition such as `">0"` to the same range. For OR logic, combine separate MINIFS results with MIN. For the largest matching value, use MAXIFS. MINIFS requires Excel 2019, Excel 2021, Excel 2024, or Microsoft 365 in Excel, so it does not work in Excel 2016 or earlier.

## Syntax

```excel
=MINIFS(min_range, criteria_range1, criterion1, [criteria_range2, criterion2], ...)
```

<!-- Image 1: Min Range and Criteria Pairs. See Images/Statistical/MINIFS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `min_range` | Yes | The range of values to compare, such as `C2:C8`. Must contain numbers for the result to be meaningful. |
| `criteria_range1` | Yes | The range tested against `criterion1`. It must be the same size and shape as `min_range`. |
| `criterion1` | Yes | The test applied to `criteria_range1`, such as `"East"`, `"<1000"`, or a cell reference. |
| `criteria_range2, criterion2, ...` | No | Additional range and criterion pairs. Every row must meet all of them. Excel allows up to 126 pairs. |

### Return Value

A single number: the smallest value in `min_range` among rows that meet every condition. It returns 0 when no row meets all conditions. It returns `#VALUE!` when the ranges are not the same size.

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
=MINIFS(C2:C8, A2:A8, "East")
```

**Result:** `410`

Only the four East rows are considered (1200, 640, 410, and 1010), and 410 is the smallest.

### Example 2: Two Conditions

```excel
=MINIFS(C2:C8, A2:A8, "East", B2:B8, "Gadgets")
```

**Result:** `640`

Only rows that are both East and Gadgets qualify: 640 and 1010. The smaller of the two is 640.

<!-- Image 2: Two Conditions Filtering Rows. See Images/Statistical/MINIFS.md -->

### Example 3: Numeric Comparison

```excel
=MINIFS(C2:C8, C2:C8, ">1000")
```

**Result:** `1010`

The criteria range is the same as the values range. Sales above 1000 are 1200, 1530, and 1010, so 1010 is the smallest.

### Example 4: Criterion From a Cell

Assume cell `G1` contains `West`.

```excel
=MINIFS(C2:C8, A2:A8, G1)
```

**Result:** `850`

The West rows hold 850 and 1530, so 850 is returned. Changing `G1` updates the result.

### Example 5: No Match Returns Zero

```excel
=MINIFS(C2:C8, A2:A8, "South")
```

**Result:** `0`

No row has the region South, so the result is 0. A 0 here means no match, not a free item, so check the match count with COUNTIFS.

## Story Problems

### Problem 1: Cheapest Quote From an Approved Vendor

A purchasing team records quotes from six vendors in `A1:C7`.

| Vendor | Status | Quote |
| --- | --- | --- |
| Alpha | Approved | 540 |
| Beta | Pending | 410 |
| Gamma | Approved | 515 |
| Delta | Approved | 585 |
| Echo | Pending | 380 |
| Foxtrot | Approved | 498 |

**Task:** Find the lowest quote from a vendor whose status is Approved.

**Solution:**

```excel
=MINIFS(C2:C7, B2:B7, "Approved")
```

**Answer:** `498`, the quote from Foxtrot. The lower pending quotes from Beta and Echo are excluded by the condition.

### Problem 2: Shortest Express Lead Time

A warehouse logs the lead time in days for five shipments in `A1:C6`.

| Shipment | Service | Days |
| --- | --- | --- |
| S1 | Express | 2 |
| S2 | Standard | 5 |
| S3 | Express | 3 |
| S4 | Standard | 1 |
| S5 | Express | 4 |

**Task:** Find the shortest lead time for any Express shipment.

**Solution:**

```excel
=MINIFS(C2:C6, B2:B6, "Express")
```

**Answer:** `2` days, from shipment S1. The one-day Standard shipment is excluded because it does not use the Express service.

<!-- Image 3: Story Problem Result. See Images/Statistical/MINIFS.md -->

## Use Cases

### Cheapest Approved Quote

**Scenario:** A procurement manager wants the lowest price for a part from suppliers who have passed approval.

```excel
=MINIFS(Quotes[Price], Quotes[Part], "Bearing", Quotes[Approved], TRUE)
```

**Why It Works:** Both conditions must match, so unapproved suppliers are excluded. Wrap the formula with COUNTIFS to show a message when no approved quote exists.

### Shortest Express Lead Time

**Scenario:** A customer service team needs the fastest delivery time offered to a specific destination.

```excel
=MINIFS(Orders[LeadDays], Orders[Carrier], "Express", Orders[Destination], "Chicago")
```

**Why It Works:** The formula returns the smallest lead time among Express orders to Chicago. Use MAXIFS with the same criteria to show the range of delivery times.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The criteria ranges are not the same size as `min_range`. | Make every range cover the same rows, for example `C2:C8` and `A2:A8`. |
| `0` | No row meets every condition. | Check the match count with COUNTIFS. A 0 here usually means no match, not a real low value. |
| `0` | Zeros in the data represent missing values. | Add a condition such as `">0"` to the same range. |
| `#NAME?` | The function is not available in the version of Excel in use. | Use Excel 2019, Excel 2021, Excel 2024, or Microsoft 365, or use MIN with IF as an array formula. |
| Wrong result | A number is stored as text, so the numeric criterion does not match it. | Convert the cells to numbers before calculating. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2019, Excel 2021, Excel 2024, Microsoft 365, Excel for the web, and Office for iPhone | Up to 126 range and criterion pairs. Returns 0 when no row matches. |
| Google Sheets | Available | The help page describes the same syntax and returns 0 when no row matches. It lists no version requirement. |

## Tips and Best Practices

- Keep the value range and every criteria range the same size so the rows line up.
- Put criteria in labeled cells and reference them, so users can change the question without editing the formula.
- Exclude zeros with a condition such as `">0"` when zero means missing data.
- Check the match count with COUNTIFS whenever a 0 result could be mistaken for a real value.
- Use a table reference such as `Quotes[Price]` so new rows are included automatically.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MIN](MIN.md) | Returns the smallest value with no conditions. |
| [MAXIFS](MAXIFS.md) | Returns the largest value that meets the same kind of conditions. |
| [COUNTIFS](COUNTIFS.md) | Counts the rows that meet the conditions, to confirm that matches exist. |
| [AVERAGEIFS](AVERAGEIFS.md) | Averages the rows that meet the conditions. |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Adds the values that meet the same kind of conditions. |

## Official Documentation

- [Microsoft Support: MINIFS function](https://support.microsoft.com/en-us/excel/functions/minifs-function)
- [Google Docs Editors Help: MINIFS](https://support.google.com/docs/answer/7014063)
