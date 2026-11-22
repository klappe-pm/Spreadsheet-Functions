---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Statistical Analysis
use-case:
  - Delivery Time Targets
  - Order Value Benchmarks
related:
  - MEDIAN
  - PERCENTILE.EXC
  - PERCENTILE.INC
  - PERCENTRANK
  - QUARTILE.INC
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/percentile-function
  - https://support.google.com/docs/answer/3094093
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - compatibility
  - excel
  - interpolation
  - percentile
  - sheets
---

# PERCENTILE

## Description

**PERCENTILE** returns the k-th percentile of the values in a range, where k is a number from 0 to 1 inclusive. A k of 0.5 returns the middle value, and a k of 0.9 returns a value near the top of the range. When k falls between two ranked values, the function interpolates and may return a number that does not appear in the data.

PERCENTILE is a compatibility function. Microsoft keeps it so older workbooks still calculate, and it has been replaced by PERCENTILE.INC and PERCENTILE.EXC. For new work, use PERCENTILE.INC, which uses the same inclusive 0 to 1 range and interpolation. Use PERCENTILE.EXC when a rule requires a range that excludes 0 and 1.

Keep PERCENTILE in existing files that depend on it, because replacing it changes the formula text and can confuse people who read the workbook later.

## Syntax

```excel
=PERCENTILE(array, k)
```

<!-- Image 1: Percentile Arguments Diagram. See Images/Statistical/PERCENTILE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array of values that defines the distribution, for example `A2:A10`. |
| `k` | Yes | The percentile to return, as a decimal from 0 to 1. Enter 0.25 for the 25th percentile. |

### Return Value

The k-th percentile as a number. The function returns `#VALUE!` when k is not numeric and `#NUM!` when k is less than 0 or greater than 1.

## Examples

All examples use these nine values in `A2:A10`: 14, 22, 27, 31, 35, 40, 46, 52 and 60.

### Example 1: Lower Quartile

```excel
=PERCENTILE(A2:A10, 0.25)
```

**Result:** `27`

The rank for k = 0.25 is 0.25 × 8 + 1 = 3, which is the third value, 27.

### Example 2: Interpolated Percentile

```excel
=PERCENTILE(A2:A10, 0.9)
```

**Result:** `53.6`

The rank is 0.9 × 8 + 1 = 8.2, which falls 20 percent of the way from 52 to 60.

### Example 3: The Median

```excel
=PERCENTILE(A2:A10, 0.5)
```

**Result:** `35`

A k of 0.5 returns the same value as `=MEDIAN(A2:A10)`.

### Example 4: Guarding Against a Bad Percentile

```excel
=IFERROR(PERCENTILE(A2:A10, 1.2), "Out of Range")
```

**Result:** `Out of Range`

A k above 1 returns `#NUM!`, so IFERROR shows a readable message instead.

## Story Problems

### Problem 1: Order Values and the Median Order

A shop lists nine orders in `A1:B10` with the order value in column B.

| Order | Value |
| --- | --- |
| 1001 | 120 |
| 1002 | 180 |
| 1003 | 210 |
| 1004 | 240 |
| 1005 | 275 |
| 1006 | 300 |
| 1007 | 340 |
| 1008 | 390 |
| 1009 | 450 |

**Task:** Find the value that splits the orders in half, using PERCENTILE with k set to 0.5.

**Solution:**

```excel
=PERCENTILE(B2:B10, 0.5)
```

**Answer:** `275`. With nine values the middle position is the fifth, and 275 is the fifth value. The result equals `MEDIAN(B2:B10)`.

### Problem 2: Delivery Times and a Promise Window

A courier records nine delivery times in minutes in `A2:A10`: 12, 18, 21, 25, 26, 30, 34, 41 and 55.

**Task:** Find the time that 80 percent of deliveries are at or below, so the company can promise it to customers.

**Solution:**

```excel
=PERCENTILE(A2:A10, 0.8)
```

**Answer:** `36.8` minutes. The rank is 0.8 × 8 + 1 = 7.4, which is 40 percent of the way from 34 to 41.

<!-- Image 2: Order Values Percentile Marker. See Images/Statistical/PERCENTILE.md -->

## Use Cases

### Delivery Time Targets

**Scenario:** An operations manager sets a service promise based on the delivery time that most orders beat.

```excel
=PERCENTILE(Deliveries[Minutes], 0.8)
```

**Why It Works:** The formula updates when new deliveries are added to the table. In a new workbook, switch to PERCENTILE.INC to keep the same result with a current function name.

### Order Value Benchmarks

**Scenario:** A sales lead marks the top quarter of orders so the team can review large deals first.

```excel
=PERCENTILE(Orders[Value], 0.75)
```

**Why It Works:** Orders at or above the result form the top quarter. Because the value is interpolated, a few orders can sit right at the boundary, so check the nearest rows before assigning them to a band.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The k argument is text or a blank cell. | Enter k as a number or reference a cell that holds a number. |
| `#NUM!` | The k argument is below 0 or above 1. | Enter a decimal from 0 to 1, such as 0.9 rather than 90. |
| Value not in the data | The percentile falls between two ranked values, so the function interpolates. | Expect decimals, and round the result with ROUND if the display needs whole numbers. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available as a compatibility function in current versions | Kept for older workbooks. Use PERCENTILE.INC or PERCENTILE.EXC for new formulas. |
| Google Sheets | Available | Arguments are named `data` and `percentile`. A percentile of 0.5 returns the same value as MEDIAN. The official page does not document error values for out-of-range input. |

## Tips and Best Practices

- Use PERCENTILE.INC in new workbooks and keep PERCENTILE only where an existing file depends on it.
- Store k in its own cell so the threshold can change without editing the formula.
- Wrap user-entered k values in IFERROR, or validate them with data validation that allows only 0 to 1.
- Remember that results can fall between data points, so format the output to the precision the reader needs.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Current replacement that uses the same inclusive 0 to 1 range. |
| [PERCENTILE.EXC](PERCENTILE.EXC.md) | Replacement that excludes 0 and 1 for k. |
| [MEDIAN](MEDIAN.md) | Returns the same result as PERCENTILE when k is 0.5. |
| [PERCENTRANK](PERCENTRANK.md) | Reverses the lookup: it returns the rank of a given value. |
| [QUARTILE.INC](QUARTILE.INC.md) | Returns the quartile cut points of the same data. |

## Official Documentation

- [Microsoft Support: PERCENTILE function](https://support.microsoft.com/en-us/excel/functions/percentile-function)
- [Google Docs Editors Help: PERCENTILE](https://support.google.com/docs/answer/3094093)
