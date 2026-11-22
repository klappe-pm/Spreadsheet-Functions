---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Statistical Analysis
use-case:
  - Delivery Time Variability
  - Order Size Outliers
  - Score Distribution Review
related:
  - AVERAGE
  - KURT
  - MEDIAN
  - SKEW.P
  - STDEV.S
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/skew-function
  - https://support.google.com/docs/answer/3094101
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sample Skewness
tags:
  - distribution
  - excel
  - sheets
  - skewness
---

# SKEW

## Description

**SKEW** returns the skewness of a sample, a number that shows how lopsided a set of values is around its average. A value near 0 means the data is roughly symmetrical. A positive value means the long tail stretches toward larger numbers, and a negative value means the long tail stretches toward smaller numbers.

Use SKEW when a few unusually large or small values might be pulling the distribution out of shape, for example in delivery times, order sizes or response times. The average alone can hide this, because a handful of extreme values can move the average far away from where most of the data sits.

SKEW treats its values as a sample of a larger group. When your list is the complete group, such as every order placed in one month, use SKEW.P instead. Excel needs at least three values and returns `#DIV/0!` when fewer are supplied or when the standard deviation of the values is zero. Google Sheets requires at least two values.

## Syntax

```excel
=SKEW(number1, [number2], ...)
```

<!-- Image 1: Skewness Syntax and Arguments. See Images/Statistical/SKEW.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, range, array or reference that contains numbers. |
| `number2, ...` | No | Additional numbers or ranges. Excel accepts up to 255 arguments in total. |

### Return Value

A number. Logical values, text and empty cells inside a range or array are ignored, but cells that contain zero are included. Error values, and text that cannot be converted to a number when typed directly into the argument list, cause an error. The function returns `#DIV/0!` with fewer than three values in Excel, or when the sample standard deviation is zero.

## Examples

All examples use the values 2, 4, 4, 4, 5, 5, 7 and 9 in `A1:A8`.

### Example 1: Basic Skewness

```excel
=SKEW(A1:A8)
```

**Result:** `0.8185` (rounded to four decimals)

The value is positive, so the tail on the right side is longer. The 9 is the largest value and sits well above the average of 5.

### Example 2: Blank Cells and Text Are Ignored

With `A9` empty and `A10` containing the text `n/a`:

```excel
=SKEW(A1:A10)
```

**Result:** `0.8185` (rounded to four decimals)

Excel skips the empty cell and the text inside a range, so the result matches Example 1.

<!-- Image 2: Reading the Sign of the Result. See Images/Statistical/SKEW.md -->

### Example 3: Flagging Lopsided Data

```excel
=IF(SKEW(A1:A8)>1,"Strong Right Tail","Roughly Symmetric")
```

**Result:** `Roughly Symmetric`

The skewness of 0.8185 is below the threshold of 1, so the formula reports the data as roughly symmetric. Change the threshold to suit your own data.

### Example 4: Too Few Values

```excel
=SKEW(A1:A2)
```

**Result:** `#DIV/0!`

Two values are not enough to measure skewness in Excel, so the function returns an error. Wrap the formula in `IFERROR` when a short list is possible.

## Story Problems

### Problem 1: Delivery Days for Eight Orders

A shop records the number of days each of eight orders took to arrive.

| Order | Days |
| --- | --- |
| 1 | 3 |
| 2 | 4 |
| 3 | 4 |
| 4 | 5 |
| 5 | 6 |
| 6 | 6 |
| 7 | 7 |
| 8 | 15 |

**Task:** Measure how lopsided the delivery times are.

**Solution:**

```excel
=SKEW(B2:B9)
```

**Answer:** `2.1726`. The 15-day order stretches the tail to the right, so the skewness is strongly positive. The average of 6.25 days is pulled above the typical delivery of about 5 to 6 days.

### Problem 2: Test Scores for a Small Class

A teacher lists the scores of ten students on a quiz.

| Student | Score |
| --- | --- |
| 1 | 62 |
| 2 | 71 |
| 3 | 74 |
| 4 | 78 |
| 5 | 80 |
| 6 | 83 |
| 7 | 85 |
| 8 | 88 |
| 9 | 94 |
| 10 | 97 |

**Task:** Decide whether the scores lean toward high or low results.

**Solution:**

```excel
=SKEW(B2:B11)
```

**Answer:** `-0.2475`. The value is slightly negative, so a few low scores stretch the left tail. The mean of 81.2 sits a little below the median of 81.5, which matches that small lean.

<!-- Image 3: Story Problem Results. See Images/Statistical/SKEW.md -->

## Use Cases

### Spotting Delivery Outliers

**Scenario:** An operations lead reviews whether a few very slow deliveries are distorting the average delivery time for a month.

```excel
=SKEW(Deliveries[Days])
```

**Why It Works:** A strongly positive result signals that a few long delivery times dominate the average. Investigate those orders before changing the target.

### Checking Score Balance

**Scenario:** A training team wants to know whether a course test is mostly easy, with a few hard cases, or mostly hard.

```excel
=IF(SKEW(ScoreRange)<0,"Few Low Scores","Few High Scores")
```

**Why It Works:** A negative result means the long tail is on the low side. The label tells readers which direction to examine, although the sign alone does not prove the cause.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | Fewer than three values in Excel, or all values are identical. | Add more data points, or check that the values vary. |
| `#VALUE!` | A text value was typed directly into the argument list. | Put the numbers in cells and reference the range. |
| Unexpected sign | A few extreme values appear on one side of the data. | Sort the list and review the largest and smallest values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web | Needs at least three values. Logical values and empty cells inside a range are ignored. |
| Google Sheets | Available | Needs at least two values. Text in the value arguments is ignored. |

## Tips and Best Practices

- Use SKEW together with AVERAGE and MEDIAN; a large gap between the average and the median hints at skewness before you calculate it.
- Use SKEW.P when the list is the complete group rather than a sample.
- Sort the data before reviewing a result, so the extreme values are easy to find.
- Pair SKEW with STDEV.S to judge how much the values spread, since skewness alone says nothing about spread.
- Remember that small lists give unstable skewness values, so treat results from fewer than about ten values with caution.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SKEW.P](SKEW.P.md) | Skewness for a complete population instead of a sample. |
| [KURT](KURT.md) | Measures how heavy the tails are, not which side they lean toward. |
| [AVERAGE](AVERAGE.md) | The mean, which skewness compares against the middle of the data. |
| [MEDIAN](MEDIAN.md) | The middle value; a gap from the mean suggests skewness. |
| [STDEV.S](STDEV.S.md) | Sample standard deviation, which measures spread. |

## Official Documentation

- [Microsoft Support: SKEW function](https://support.microsoft.com/en-us/excel/functions/skew-function)
- [Google Docs Editors Help: SKEW](https://support.google.com/docs/answer/3094101)
