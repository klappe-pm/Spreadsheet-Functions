---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
purpose:
  - Statistical Analysis
use-case:
  - Battery Life Benchmarks
  - Small Sample Quartiles
  - Website Traffic Cutoffs
related:
  - MEDIAN
  - PERCENTILE.EXC
  - PERCENTRANK.EXC
  - QUARTILE
  - QUARTILE.INC
  - SMALL
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/quartile-exc-function
  - https://support.google.com/docs/answer/9368240
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Exclusive Quartile
tags:
  - descriptive-statistics
  - excel
  - sheets
---

# QUARTILE.EXC

## Description

**QUARTILE.EXC** returns the first, second or third quartile of a dataset using the exclusive method. The quartile position is based on the number of values plus one, so the result stays inside the data and does not use the minimum (quartile 0) or the maximum (quartile 4). Use it when you want quartile cutoffs that are not pulled toward the extremes of a small sample.

The exclusive method can give a different answer from QUARTILE.INC for the same numbers. Choose one method for each report and state which one you used, because a reader who compares the two results may see a difference even when both are correct for their method.

QUARTILE.EXC is the current Excel version of the exclusive quartile. Quartile 0 and quartile 4 are not supported, and the function returns `#NUM!` for them. Use MIN and MAX for the extremes.

## Syntax

```excel
=QUARTILE.EXC(array, quart)
```

<!-- Image 1: QUARTILE.EXC Syntax Anatomy. See Images/Statistical/QUARTILE.EXC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The numeric values or cell range to evaluate, such as `A2:A8`. Text and blank cells are ignored. |
| `quart` | Yes | `1` for the first quartile, `2` for the median and `3` for the third quartile. Non-integer values are truncated. Values of 0 or less, or 4 or more, return an error. |

### Return Value

A number from the dataset or interpolated between two values. The function returns `#NUM!` when the array is empty or when `quart` is 0 or less, or 4 or more.

## Examples

Examples use the values 12, 15, 18, 22, 25, 30 and 34 in `A2:A8`.

### Example 1: First Quartile, Exclusive Method

```excel
=QUARTILE.EXC(A2:A8, 1)
```

**Result:** `15`

With seven values, the first quartile sits at position 2 of 8, which is the value 15.

### Example 2: Median

```excel
=QUARTILE.EXC(A2:A8, 2)
```

**Result:** `22`

The median is the same under both methods for this dataset.

### Example 3: Third Quartile

```excel
=QUARTILE.EXC(A2:A8, 3)
```

**Result:** `30`

Position 6 of 8 holds the value 30.

### Example 4: Quartile 4 Is Not Supported

```excel
=IFERROR(QUARTILE.EXC(A2:A8, 4), "Use MAX")
```

**Result:** `Use MAX`

Quartile 4 is excluded by definition, so the formula returns the error message instead.

## Story Problems

### Problem 1: Battery Life Benchmarks

A laptop team tests seven batteries and records the hours of use in `B2:B8`: 4.2, 5.0, 5.5, 6.1, 6.8, 7.4 and 8.0. The team wants a first-quartile benchmark that uses only values from the test.

| Battery | Hours |
| --- | --- |
| 1 | 4.2 |
| 2 | 5.0 |
| 3 | 5.5 |
| 4 | 6.1 |
| 5 | 6.8 |
| 6 | 7.4 |
| 7 | 8.0 |

**Task:** Find the exclusive first quartile of the battery life.

**Solution:**

```excel
=QUARTILE.EXC(B2:B8, 1)
```

**Answer:** `5` hours. The position is (7 + 1) × 0.25 = 2, which is the second value.

### Problem 2: Website Traffic Cutoffs

A site records monthly visits in thousands for five months in `C2:C6`: 120, 135, 150, 170 and 210. The marketing team wants the exclusive third quartile as the cutoff for high-traffic months.

**Task:** Find the third quartile using the exclusive method.

**Solution:**

```excel
=QUARTILE.EXC(C2:C6, 3)
```

**Answer:** `190` thousand visits. The position is (5 + 1) × 0.75 = 4.5, which falls halfway between 170 and 210.

## Use Cases

### Battery Life Benchmarks

**Scenario:** A hardware team wants a benchmark that uses only values measured in its own tests, not the best and worst results.

```excel
=QUARTILE.EXC(BatteryHours, 3)
```

**Why It Works:** The exclusive method keeps the cutoff between measured values in small samples. Use a named range so new tests update the benchmark.

### Small Sample Quartiles

**Scenario:** A quality team reviews a batch of 9 measurements and needs quartile cutoffs for a control chart.

```excel
=QUARTILE.EXC(Measurements, 1)
```

**Why It Works:** Excluding the extremes avoids giving the minimum more influence than it deserves in a short list. Compare the result with QUARTILE.INC to confirm the method your chart uses.

### Website Traffic Cutoffs

**Scenario:** A marketing analyst groups months into three traffic tiers using exclusive quartiles.

```excel
=QUARTILE.EXC(TrafficThousands, 1)
```

**Why It Works:** The first and third quartiles form the lower and upper cutoffs. Keep the method consistent across reports so tier changes reflect real traffic shifts.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The array is empty or `quart` is 0 or less, or 4 or more. | Check the range and use 1, 2 or 3. |
| Unexpected value | The result differs from QUARTILE.INC for the same range. | Both methods are valid. Use the method your report states. |
| Unexpected value | Text in the range is ignored, so fewer values are counted. | Convert numbers stored as text to numeric values. |
| `#VALUE!` | The range contains an error value. | Fix the error in the source cells first. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns `#NUM!` for quartile 0 or 4. |
| Google Sheets | Available | Same arguments. The documentation describes quartiles 1 to 3 as exclusive of 0 and 4. |

## Tips and Best Practices

- Write the method name in your report, because QUARTILE.EXC and QUARTILE.INC can return different values.
- Use MIN and MAX for the extremes, which QUARTILE.EXC does not return.
- Use `1`, `2` or `3` as the quartile number and store it in a labeled cell so the same formula works for each cutoff.
- Check that the range has enough values for the exclusive method. Small lists give cutoffs that sit very close to the data.

## Related Functions

| Function | Relationship |
| --- | --- |
| [QUARTILE.INC](QUARTILE.INC.md) | The inclusive method, which can return the minimum and maximum. |
| [QUARTILE](QUARTILE.md) | The older inclusive function kept for compatibility. |
| [PERCENTILE.EXC](PERCENTILE.EXC.md) | Returns any exclusive percentile, not only the quartiles. |
| [PERCENTRANK.EXC](PERCENTRANK.EXC.md) | Finds the exclusive percentile rank of a value in the dataset. |
| [MEDIAN](MEDIAN.md) | Returns the same value as quartile 2. |
| [SMALL](SMALL.md) | Returns the kth smallest value directly. |

## Official Documentation

- [Microsoft Support: QUARTILE.EXC function](https://support.microsoft.com/en-us/excel/functions/quartile-exc-function)
- [Google Docs Editors Help: QUARTILE.EXC](https://support.google.com/docs/answer/9368240)
