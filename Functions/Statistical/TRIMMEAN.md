---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Aggregation
  - Statistical Analysis
use-case:
  - Customer Review Averages
  - Delivery Time Reporting
  - Lab Reaction Time Averages
related:
  - AVERAGE
  - MEDIAN
  - PERCENTILE.INC
  - STDEV.S
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/trimmean-function
  - https://support.google.com/docs/answer/3094061
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Trimmed Mean
tags:
  - averages
  - excel
  - outliers
  - sheets
  - trimmed-mean
---

# TRIMMEAN

## Description

**TRIMMEAN** returns the mean of a data set after removing a share of its lowest and highest values. The function drops the same number of values from each end, so a few extreme readings cannot pull the average far off. It is useful when a data set contains occasional outliers such as a failed sensor reading, a one-off very long delivery, or a rating left by a single unhappy customer.

The `percent` argument sets the total share of values to exclude, split evenly between the two ends. With 10 values and a percent of 0.2, the function removes the single lowest and single highest value and averages the eight that remain. The average of all values is available from AVERAGE, which is the right choice when no value is suspect.

Pick the percent with care. A small share leaves the outliers in place, and a large share discards real information. When the excluded count is less than 2, nothing is removed and the result equals the plain mean. TRIMMEAN has no criteria argument, so for conditional trimmed averages you must first extract the qualifying values into a helper range.

## Syntax

```excel
=TRIMMEAN(array,percent)
```

<!-- Image 1: Trimmed Values at Both Ends. See Images/Statistical/TRIMMEAN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array of values to trim and average, such as `A2:A11`. |
| `percent` | Yes | The fraction of data points to exclude, from 0 to 1. For example, 0.2 excludes 20 percent of the points, half from the top and half from the bottom. |

### Return Value

A number: the mean of the values that remain after the trimming. The function returns `#NUM!` when `percent` is less than 0 or greater than 1. The number of excluded values is rounded down to the nearest even number, so a percent that removes an odd count removes one fewer value.

## Examples

All examples use these ten customer ratings in `A2:A11`: 72, 88, 91, 85, 40, 90, 87, 83, 99, 86. The lowest rating is 40 and the highest is 99.

### Example 1: Exclude Twenty Percent

```excel
=TRIMMEAN(A2:A11,0.2)
```

**Result:** `85.25`

Ten values at 20 percent exclude two values, one from each end: 40 and 99. The remaining eight values average to 85.25.

### Example 2: Exclude Nothing

```excel
=TRIMMEAN(A2:A11,0)
```

**Result:** `82.1`

A percent of 0 excludes no values, so the result is the ordinary mean of all ten ratings. The 40 rating pulls the average down compared with the trimmed result in Example 1.

### Example 3: A Small Percent Excludes Nothing

```excel
=TRIMMEAN(A2:A11,0.1)
```

**Result:** `82.1`

Ten values at 10 percent would exclude one value, but the count is rounded down to an even number, which is zero. The result therefore matches Example 2. Use at least 20 percent with ten values to remove any values.

### Example 4: Round the Trimmed Mean for a Report

```excel
=ROUND(TRIMMEAN(A2:A11,0.2),1)
```

**Result:** `85.3`

Wrapping TRIMMEAN in ROUND keeps the report to one decimal place. The underlying value is 85.25, which rounds up to 85.3.

## Story Problems

### Problem 1: Delivery Times Report

A courier company logs the minutes each of ten deliveries took in `A2:A11`. One delivery took 75 minutes because of a road closure, and another took 27 minutes because it was a short hop. The operations manager wants an average that ignores both extremes.

| Delivery | Minutes |
| --- | --- |
| D1 | 34 |
| D2 | 41 |
| D3 | 29 |
| D4 | 38 |
| D5 | 75 |
| D6 | 36 |
| D7 | 40 |
| D8 | 33 |
| D9 | 27 |
| D10 | 44 |

**Task:** Compute the average delivery time after excluding the lowest and highest 20 percent of values.

**Solution:**

```excel
=TRIMMEAN(A2:A11,0.2)
```

**Answer:** `36.875`. Two values are excluded (27 and 75), and the eight remaining values sum to 295, so 295 / 8 = 36.875. The plain mean of 39.7 is pulled up by the 75-minute delivery.

<!-- Image 2: Delivery Times Trimmed Average. See Images/Statistical/TRIMMEAN.md -->

### Problem 2: Reaction Time Readings

A lab measures the reaction time of a sensor in milliseconds for ten trials in `A2:A11`. Two trials were disturbed by a power surge and produced very high or very low readings. The lab wants the trimmed average using a 40 percent exclusion, which removes two values from each end.

| Trial | Milliseconds |
| --- | --- |
| T1 | 212 |
| T2 | 198 |
| T3 | 205 |
| T4 | 260 |
| T5 | 201 |
| T6 | 207 |
| T7 | 199 |
| T8 | 240 |
| T9 | 204 |
| T10 | 210 |

**Task:** Compute the trimmed average reaction time with 40 percent of the values excluded.

**Solution:**

```excel
=TRIMMEAN(A2:A11,0.4)
```

**Answer:** `206.5`. Ten values at 40 percent exclude four values: 198 and 199 at the low end, and 240 and 260 at the high end. The six remaining values sum to 1,239, so 1,239 / 6 = 206.5.

## Use Cases

### Delivery Time Reporting

**Scenario:** A logistics team reports average delivery time each week, and one blocked road can distort the figure for the whole fleet.

```excel
=TRIMMEAN(Deliveries[Minutes],0.1)
```

**Why It Works:** A 10 percent trim removes the single most extreme value at each end of a sample of about 20 deliveries. Check the sample size first, because very small samples lose too many values.

### Customer Review Averages

**Scenario:** A product page shows an average rating, and a few reviews left by bots or spammers skew it.

```excel
=ROUND(TRIMMEAN(Reviews[Score],0.2),2)
```

**Why It Works:** Excluding 20 percent of the scores from both ends limits the effect of extreme ratings, and ROUND keeps the display to two decimals.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `percent` is less than 0 or greater than 1. | Enter a value from 0 up to 1, such as 0.2. |
| Unexpected average | `percent` times the count of values is below 2, so nothing is removed. | Increase `percent`, or accept that the result is the plain mean. |
| Unexpected average | The range includes a blank or non-numeric cell that the average should skip. | Confirm that the range contains only the values to trim. |
| Unexpected average | The excluded count rounds down to an even number, so one fewer value is removed than the percent suggests. | Choose a percent that gives an even count, such as 0.2 with ten values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows and Mac), Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Returns `#NUM!` when `percent` is outside 0 to 1. Excludes an even number of values, split between the two ends. |
| Google Sheets | Available | Named `data` and `exclude_proportion`. The official page requires `exclude_proportion` to be at least 0 and less than 1, but it does not describe how the excluded count is rounded. Check results against Excel when a workbook is shared between the two. |

## Tips and Best Practices

- Look at the data first to confirm that the extreme values are errors or one-off events before trimming them.
- Use AVERAGE when every value is valid, because trimming discards real observations.
- Remember that the excluded count rounds down to an even number, so small percentages can remove nothing.
- Use MEDIAN as a quick alternative when you only need the middle value.
- Document the percent used in the report so readers know how much of the data was excluded.
- Use PERCENTILE.INC to find the cut-off values that a trim would remove.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Mean of all values, with no trimming. |
| [MEDIAN](MEDIAN.md) | Middle value, which resists outliers without a percent setting. |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Finds the cut-off values at a given percentile. |
| [STDEV.S](STDEV.S.md) | Measures spread, useful for judging whether trimming is needed. |

## Official Documentation

- [Microsoft Support: TRIMMEAN function](https://support.microsoft.com/en-us/excel/functions/trimmean-function)
- [Google Docs Editors Help: TRIMMEAN](https://support.google.com/docs/answer/3094061)
