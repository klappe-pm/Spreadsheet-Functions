---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Statistical Analysis
use-case:
  - Complete Year Reviews
  - Monthly Defect Patterns
  - Weekly Order Volumes
related:
  - AVERAGE
  - KURT
  - MEDIAN
  - SKEW
  - STDEV.P
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/skew-p-function
  - https://support.google.com/docs/answer/9368569
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Population Skewness
tags:
  - distribution
  - excel
  - sheets
  - skewness
---

# SKEW.P

## Description

**SKEW.P** returns the skewness of a population, which describes how asymmetric a set of values is around its mean. A value near 0 means the distribution is roughly symmetrical. A positive value means the long tail stretches toward larger numbers, and a negative value means the long tail stretches toward smaller numbers.

Use SKEW.P when your values are the complete group you care about, such as every month in a year, every machine on a line or every order in a week. If your values are only a sample taken from a larger group, use SKEW instead. The two functions answer the same question with different assumptions about the data, so they give different numbers for the same list.

SKEW.P uses the population standard deviation in its calculation. Excel needs at least three values and returns `#DIV/0!` when fewer are supplied or when the standard deviation is zero. Text and empty cells inside a range are ignored.

## Syntax

```excel
=SKEW.P(number1, [number2], ...)
```

<!-- Image 1: Population Skewness Syntax. See Images/Statistical/SKEW.P.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, range, array or reference that contains numbers. |
| `number2, ...` | No | Additional numbers or ranges. Excel accepts up to 254 arguments in total. |

### Return Value

A number. Logical values, text and empty cells inside a range or array are ignored, while cells that contain zero are counted. The function returns `#NUM!` for invalid values and `#VALUE!` for invalid data types. It returns `#DIV/0!` with fewer than three values or when the standard deviation is zero.

## Examples

All examples use the values 2, 4, 4, 4, 5, 5, 7 and 9 in `A1:A8`.

### Example 1: Population Skewness

```excel
=SKEW.P(A1:A8)
```

**Result:** `0.65625`

The population result is smaller than the sample result from SKEW for the same values, because SKEW.P does not apply the small-sample correction.

### Example 2: Comparing With SKEW

```excel
=SKEW(A1:A8)
```

**Result:** `0.8185` (rounded to four decimals)

Placing SKEW next to SKEW.P on the same list shows the effect of the sample assumption. Use the function that matches how the list was collected.

<!-- Image 2: Population Versus Sample Comparison. See Images/Statistical/SKEW.P.md -->

### Example 3: Blank Cells and Text Are Ignored

With `A9` empty and `A10` containing the text `n/a`:

```excel
=SKEW.P(A1:A10)
```

**Result:** `0.65625`

Excel skips the blank cell and the text, so the result is the same as Example 1.

### Example 4: Too Few Values

```excel
=SKEW.P(A1:A2)
```

**Result:** `#DIV/0!`

Two values are not enough for Excel to measure skewness, so the formula returns an error. Check the number of values before you rely on the result.

## Story Problems

### Problem 1: Monthly Defects for a Plant

A plant records the number of defective parts found in each month of 2026. The list covers the entire year, so the population function fits.

| Month | Defects |
| --- | --- |
| Jan | 14 |
| Feb | 15 |
| Mar | 16 |
| Apr | 16 |
| May | 17 |
| Jun | 18 |
| Jul | 18 |
| Aug | 19 |
| Sep | 20 |
| Oct | 21 |
| Nov | 22 |
| Dec | 38 |

**Task:** Measure how strongly the defect counts lean toward high months.

**Solution:**

```excel
=SKEW.P(B2:B13)
```

**Answer:** `2.2695`. The December spike of 38 defects creates a long tail on the right, so the skewness is strongly positive. The median of 18 defects is much lower than the mean of 19.5.

### Problem 2: Orders Placed in One Week

A small shop counts the orders it received on each day of one week. The full week is the complete group being studied.

| Day | Orders |
| --- | --- |
| Mon | 12 |
| Tue | 14 |
| Wed | 15 |
| Thu | 15 |
| Fri | 16 |
| Sat | 18 |
| Sun | 31 |

**Task:** Find the population skewness of the daily order counts.

**Solution:**

```excel
=SKEW.P(B2:B8)
```

**Answer:** `1.6930`. The Sunday peak of 31 orders pulls the tail to the right. The mean is about 17.29 orders per day.

<!-- Image 3: Story Problem Results. See Images/Statistical/SKEW.P.md -->

## Use Cases

### Reviewing a Complete Year of Defects

**Scenario:** A quality manager checks whether a few bad months dominate the yearly defect pattern.

```excel
=SKEW.P(DefectsByMonth)
```

**Why It Works:** Because the twelve months are the whole year, the population version is the right choice. A strong positive result points to a spike that deserves a root-cause review.

### Weekly Order Shape

**Scenario:** A store manager compares a week of daily orders to decide whether staffing should follow a steady pattern or a peak pattern.

```excel
=IF(SKEW.P(OrderCounts)>1,"Peak Pattern","Steady Pattern")
```

**Why It Works:** The threshold of 1 is a planning choice, not a statistical rule. Adjust it to match how sensitive the staffing decision should be.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | Fewer than three values, or every value is the same. | Include more data points or check the range. |
| `#VALUE!` | An argument contains a value that cannot be read as a number. | Use cells that contain numbers, and remove text labels from the range. |
| `#NUM!` | An argument contains an invalid numeric value. | Check the range for errors and replace them. |
| Result differs from SKEW | The list was treated as a population when it is a sample. | Use SKEW when the values come from a larger group. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web | Needs at least three values. Logical values and empty cells inside a range are ignored. |
| Google Sheets | Available | Uses the same name and population assumption. Text in the value arguments is ignored. |

## Tips and Best Practices

- Choose SKEW.P only when the list is the complete group; a sample of that group needs SKEW.
- Compare the result with MEDIAN to see whether the average is pulled toward a tail.
- Use SKEW.P with STDEV.P when both the shape and the spread of a complete group matter.
- Keep the data range free of headings and notes, because stray text can shift which cells are counted.
- Recalculate after adding a new period so the population includes every value.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SKEW](SKEW.md) | Skewness for a sample, with a small-sample correction. |
| [KURT](KURT.md) | Measures how heavy the tails are. |
| [AVERAGE](AVERAGE.md) | The mean that skewness is measured around. |
| [MEDIAN](MEDIAN.md) | The middle value, used to compare against the mean. |
| [STDEV.P](STDEV.P.md) | Population standard deviation, which measures spread. |

## Official Documentation

- [Microsoft Support: SKEW.P function](https://support.microsoft.com/en-us/excel/functions/skew-p-function)
- [Google Docs Editors Help: SKEW.P](https://support.google.com/docs/answer/9368569)
