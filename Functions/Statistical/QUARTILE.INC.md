---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
purpose:
  - Statistical Analysis
use-case:
  - Employee Tenure Bands
  - Fast Lane Cutoffs
  - Interquartile Range Reporting
related:
  - MEDIAN
  - PERCENTILE.INC
  - PERCENTRANK.INC
  - QUARTILE
  - QUARTILE.EXC
  - SMALL
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/quartile-inc-function
  - https://support.google.com/docs/answer/3094041
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Inclusive Quartile
tags:
  - descriptive-statistics
  - excel
  - sheets
---

# QUARTILE.INC

## Description

**QUARTILE.INC** returns a quartile of a dataset using the inclusive method, based on percentile values from 0 to 1. It returns the minimum for quartile 0, the first quartile for 1, the median for 2, the third quartile for 3 and the maximum for 4. Use it to split a list into four equal-sized groups, such as tenure bands, cutoffs for a service tier or the interquartile range.

QUARTILE.INC is the current name for the function that Excel previously called QUARTILE. Both return the same results. Use QUARTILE.EXC when your method excludes the minimum and maximum, and state which method a report uses so readers can compare figures.

When the quartile falls between two values, the function interpolates. For example, the first quartile of 12, 15 and 18 is 13.5, not one of the listed numbers.

## Syntax

```excel
=QUARTILE.INC(array, quart)
```

<!-- Image 1: QUARTILE.INC Syntax Anatomy. See Images/Statistical/QUARTILE.INC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The numeric values or cell range to evaluate, such as `A2:A8`. Text and blank cells are ignored. |
| `quart` | Yes | `0` for the minimum, `1` for the first quartile, `2` for the median, `3` for the third quartile and `4` for the maximum. Non-integer values are truncated. |

### Return Value

A number from the dataset or interpolated between two values. The function returns `#NUM!` when the array is empty or when `quart` is less than 0 or greater than 4.

## Examples

Examples use the values 12, 15, 18, 22, 25, 30 and 34 in `A2:A8`.

### Example 1: First Quartile

```excel
=QUARTILE.INC(A2:A8, 1)
```

**Result:** `16.5`

The inclusive method places the first quartile halfway between 15 and 18.

### Example 2: Minimum Through Quartile Zero

```excel
=QUARTILE.INC(A2:A8, 0)
```

**Result:** `12`

Quartile 0 returns the smallest value, the same result as MIN.

### Example 3: Interquartile Range

```excel
=QUARTILE.INC(A2:A8, 3)-QUARTILE.INC(A2:A8, 1)
```

**Result:** `11`

The third quartile is 27.5 and the first is 16.5, so the middle half of the values spans 11 units.

### Example 4: Maximum Through Quartile Four

```excel
=QUARTILE.INC(A2:A8, 4)
```

**Result:** `34`

Quartile 4 returns the largest value, the same result as MAX.

## Story Problems

### Problem 1: Employee Tenure Bands

HR records the years of service for eight employees in `B2:B9`: 1, 2, 2, 3, 5, 8, 10 and 12. The top band starts at the third quartile.

| Employee | Years |
| --- | --- |
| A | 1 |
| B | 2 |
| C | 2 |
| D | 3 |
| E | 5 |
| F | 8 |
| G | 10 |
| H | 12 |

**Task:** Find the third quartile of years of service.

**Solution:**

```excel
=QUARTILE.INC(B2:B9, 3)
```

**Answer:** `8.5` years. The position is 0.75 times 7 (the eight values count from 0), which is 5.25, so the result falls a quarter of the way from 8 to 10.

### Problem 2: Fast Lane Cutoff

A service desk records processing times for five tickets in `C2:C6`: 14, 18, 21, 25 and 30 minutes. Tickets at or below the first quartile go to a fast lane.

**Task:** Find the first quartile of the processing times.

**Solution:**

```excel
=QUARTILE.INC(C2:C6, 1)
```

**Answer:** `18` minutes. The position is 0.25 times 4 (the five values count from 0), which is 1, so the result is exactly the second value.

## Use Cases

### Employee Tenure Bands

**Scenario:** An HR analyst groups staff into four tenure bands using the quartiles of years of service.

```excel
=QUARTILE.INC(TenureYears, 1)
```

**Why It Works:** Each quartile marks a boundary between bands. Use a named range so the bands update when staff join or leave.

### Fast Lane Cutoffs

**Scenario:** An operations lead sends the quickest quarter of tickets to a fast lane.

```excel
=QUARTILE.INC(ProcessingMinutes, 1)
```

**Why It Works:** The first quartile is the cutoff below which 25 percent of tickets fall. Compare each ticket against this value with a simple IF formula.

### Interquartile Range Reporting

**Scenario:** A finance analyst reports the spread of monthly expenses without the influence of extreme months.

```excel
=QUARTILE.INC(Expenses, 3)-QUARTILE.INC(Expenses, 1)
```

**Why It Works:** The interquartile range covers the middle half of the values, so a single unusual month has less effect on it than on the full range.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The array is empty or `quart` is less than 0 or greater than 4. | Check the range and use 0, 1, 2, 3 or 4. |
| Unexpected value | The quartile number is a percentage, such as 75, not 3. | Use 0 to 4 for quartiles or PERCENTILE.INC for percentages. |
| Unexpected value | Text in the range is ignored, so fewer values are counted. | Convert numbers stored as text to numeric values. |
| `#VALUE!` | The range contains an error value. | Fix the error in the source cells first. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Replaces QUARTILE for new work. Interpolates between values when the quartile falls between two of them. |
| Google Sheets | Available | The documentation covers QUARTILE.INC together with QUARTILE and describes the result as the value nearest to the requested quartile. |

## Tips and Best Practices

- Use QUARTILE.INC in new workbooks and use QUARTILE only in files that already depend on it.
- Keep the quartile number in a labeled cell so one formula returns any quartile.
- Check that the range holds numbers rather than text before you read the result.
- Use the same method across a report, and name it in the text, so the cutoffs match readers' expectations.

## Related Functions

| Function | Relationship |
| --- | --- |
| [QUARTILE](QUARTILE.md) | The older name for this function, kept for compatibility. |
| [QUARTILE.EXC](QUARTILE.EXC.md) | The exclusive method, which does not return the minimum or maximum. |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Returns any inclusive percentile, not only the four quartiles. |
| [PERCENTRANK.INC](PERCENTRANK.INC.md) | Finds the percentile rank of a value within the dataset. |
| [MEDIAN](MEDIAN.md) | Returns the same value as quartile 2. |
| [SMALL](SMALL.md) | Returns the kth smallest value directly. |

## Official Documentation

- [Microsoft Support: QUARTILE.INC function](https://support.microsoft.com/en-us/excel/functions/quartile-inc-function)
- [Google Docs Editors Help: QUARTILE](https://support.google.com/docs/answer/3094041)
