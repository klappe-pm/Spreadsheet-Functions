---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Statistical Analysis
use-case:
  - Bottling Line Consistency
  - Delivery Time Variability
  - Return Distribution Risk
related:
  - AVERAGE
  - DEVSQ
  - SKEW
  - STDEV.S
  - VAR.S
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/kurt-function
  - https://support.google.com/docs/answer/3093634
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Excess Kurtosis
  - Kurtosis Measure
tags:
  - distribution-shape
  - excel
  - kurtosis
  - sheets
  - statistical
---

# KURT

## Description

**KURT** returns the excess kurtosis of a data set. Kurtosis describes the shape of a distribution's tails and peak compared with a normal bell curve. The excess kurtosis subtracts 3 from the raw measure, so a normal distribution scores about 0.

A positive result means the data has heavier tails and a sharper peak than a normal curve, so extreme values appear more often than the average spread would suggest. A negative result means the data is flatter, with fewer extreme values. KURT does not measure the center or the spread of the data. Use AVERAGE and STDEV.S for those values, and read KURT alongside them.

KURT uses the sample standard deviation in its calculation, so it suits a sample of observations. The function needs at least four data points. With fewer, or when all values are identical, it returns `#DIV/0!`. For a symmetry check, use SKEW, which measures lean rather than tail weight.

## Syntax

```excel
=KURT(number1, [number2], ...)
```

<!-- Image 1: Normal Curve Compared With Heavy Tails. See Images/Statistical/KURT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, a range, an array or a reference to values. |
| `number2, ...` | No | Additional numbers or ranges. Up to 255 arguments are allowed. A single array or range can replace the list. |

Logical values and numbers typed directly into the list are counted. In a range or array, text, logical values and empty cells are ignored, but zeros are included.

### Return Value

A number: the excess kurtosis. Zero means the tails match a normal distribution, a positive value means heavier tails, and a negative value means lighter tails. It returns `#DIV/0!` when there are fewer than four numeric values or when the sample standard deviation is zero.

## Examples

### Example 1: Kurtosis of a Small Sample

Data in `A2:A9`: 4, 8, 6, 5, 3, 7, 9, 2.

```excel
=KURT(A2:A9)
```

**Result:** `-1.2`

The result is negative, so the values are spread evenly across the range with few extreme points.

### Example 2: Rounding for a Report

```excel
=ROUND(KURT(A2:A9), 2)
```

**Result:** `-1.2`

ROUND keeps the report to two decimal places without changing the underlying calculation.

### Example 3: Labeling the Shape

```excel
=IF(KURT(A2:A9) > 0, "Heavy tails", "Light or normal tails")
```

**Result:** `Light or normal tails`

The IF test turns the number into a label that a manager can read without knowing the formula.

### Example 4: Guarding Against Too Few Values

```excel
=IFERROR(KURT(B2:B4), "Need at least four values")
```

**Result:** `Need at least four values`

With only three values in `B2:B4`, KURT returns `#DIV/0!`. IFERROR shows a message instead.

## Story Problems

### Problem 1: Delivery Times for One Route

A courier logs the minutes each delivery took on one route in `A1:B7`.

| Stop | Minutes |
| --- | --- |
| 1 | 31 |
| 2 | 35 |
| 3 | 29 |
| 4 | 60 |
| 5 | 33 |
| 6 | 30 |

**Task:** Measure how heavy the tails of the delivery times are. The dispatcher wants to know whether long delays are rare or frequent.

**Solution:**

```excel
=KURT(B2:B7)
```

**Answer:** `5.3021`. The large positive value comes from the single 60-minute delivery, which creates a heavy right tail. The route needs a closer look at that stop.

### Problem 2: Bottle Fill Weights

A bottling line fills bottles to a target of 500 grams. A technician records eight fill weights in `D2:D9`.

| Bottle | Weight (g) |
| --- | --- |
| 1 | 498 |
| 2 | 501 |
| 3 | 500 |
| 4 | 499 |
| 5 | 502 |
| 6 | 500 |
| 7 | 497 |
| 8 | 500 |

**Task:** Decide whether the fill weights behave like a normal process, with few extreme overfills or underfills.

**Solution:**

```excel
=KURT(D2:D9)
```

**Answer:** `-0.1649`. The value is close to zero, so the tails are close to a normal curve. The fill process has no unusual pattern in its extremes.

<!-- Image 2: Bottle Fill Weights Worksheet. See Images/Statistical/KURT.md -->

## Use Cases

### Return Distribution Risk

**Scenario:** An analyst reviews daily percentage returns for a fund and wants to know how often large losses happen beyond what the average and standard deviation suggest.

```excel
=KURT(Returns[Daily Return])
```

**Why It Works:** A strongly positive result warns that extreme days are more common than a normal distribution predicts, so a simple volatility estimate may understate risk.

### Delivery Time Variability

**Scenario:** An operations team compares the delivery time spread across depots.

```excel
=KURT(Depot1!C2:C200)
```

**Why It Works:** Comparing KURT across depots shows which depot has rare but severe delays, even when the average times look similar.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | Fewer than four numeric values were supplied. | Add more observations. KURT needs at least four. |
| `#DIV/0!` | Every value is the same, so the standard deviation is zero. | Check the data for a copy-paste or lookup problem. |
| `#VALUE!` | An error value such as `#N/A` sits inside the range. | Fix or remove the error cell before calculating. |
| Unexpected result | Text or blank cells were expected to count as zeros. | Text and empty cells are ignored in ranges, but zeros count, so replace blanks with a value only when zero is correct. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Accepts up to 255 arguments. Text and empty cells in ranges are ignored. |
| Google Sheets | Available | Same calculation. The help page gives a maximum of 30 arguments, so put larger data sets in a single range. Text in the value arguments is ignored. |

## Tips and Best Practices

- Read KURT with SKEW. Skew shows lean, kurtosis shows tail weight, and both can point to a non-normal process.
- Check for outliers before reading the result, since one unusual value can change the kurtosis a great deal.
- Use at least 20 to 30 observations when the result will drive a decision, because small samples give unstable values.
- Keep a sample and a full population separate. KURT assumes a sample, so describe the data that way in reports.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SKEW](SKEW.md) | Measures symmetry, the companion check to KURT. |
| [STDEV.S](STDEV.S.md) | Provides the sample standard deviation that KURT uses internally. |
| [VAR.S](VAR.S.md) | Returns the sample variance, which describes spread without tail shape. |
| [DEVSQ](DEVSQ.md) | Returns the sum of squared deviations from the mean. |
| [AVERAGE](AVERAGE.md) | Returns the center of the data that KURT is measured around. |

## Official Documentation

- [Microsoft Support: KURT function](https://support.microsoft.com/en-us/excel/functions/kurt-function)
- [Google Docs Editors Help: KURT](https://support.google.com/docs/answer/3093634)
