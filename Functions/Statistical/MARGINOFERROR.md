---
domain: Spreadsheet Functions
category: Statistical
subcategory: Hypothesis Tests
purpose:
  - Hypothesis Testing
  - Statistical Analysis
use-case:
  - Customer Survey Precision
  - Quality Audit Sampling
  - Sample Mean Reporting
related:
  - AVERAGE
  - CONFIDENCE.NORM
  - CONFIDENCE.T
  - STDEV.S
  - T.INV.2T
level: 4
source:
  - https://support.google.com/docs/answer/12487850
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Confidence Interval Half Width
  - Sampling Error
tags:
  - confidence-interval
  - sampling
  - sheets
  - statistical
---

# MARGINOFERROR

## Description

**MARGINOFERROR** returns the margin of error for the mean of a sample at a chosen confidence level. The margin of error is the amount you add to and subtract from the sample mean to form a confidence interval. If the confidence level is 0.95, the true population mean is expected to lie within that distance of the sample mean in 95 percent of repeated samples.

The function takes a range of sample values and a confidence level written as a decimal between 0 and 1, such as 0.95 or 0.99. It uses the sample standard deviation and the number of values, and it applies a t-based calculation. Google's help page describes the result as `CONFIDENCE.T(1 - confidence, STDEV(range), COUNT(range))`.

The page says the calculation suits normally distributed continuous data and surveys with reasonably large samples. With very few values or heavily skewed data, the interval can be misleading. MARGINOFERROR is available in Google Sheets only. Excel does not have this function, and CONFIDENCE.T is the closest equivalent.

## Syntax

```excel
=MARGINOFERROR(range, confidence)
```

<!-- Image 1: Sample Mean Plus or Minus the Margin. See Images/Statistical/MARGINOFERROR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `range` | Yes | The cells that hold the sample values. |
| `confidence` | Yes | The confidence level as a decimal greater than 0 and less than 1. Use 0.95 for 95 percent and 0.99 for 99 percent. |

### Return Value

A number: the margin of error in the same unit as the data. Add it to and subtract it from the sample mean to get the confidence interval. A larger sample or a smaller spread gives a smaller margin.

## Examples

The examples use six measurements in `A2:A7`: 72, 68, 75, 70, 74 and 69. The mean is 71.33.

### Example 1: Margin at 95 Percent Confidence

```excel
=MARGINOFERROR(A2:A7, 0.95)
```

**Result:** `2.9434`

The sample mean is 71.33 and the interval is about 68.39 to 74.28.

### Example 2: Margin at 99 Percent Confidence

```excel
=MARGINOFERROR(A2:A7, 0.99)
```

**Result:** `4.6170`

A higher confidence level needs a wider margin, so the same data gives a larger value here than in Example 1.

### Example 3: Lower Bound of the Interval

```excel
=AVERAGE(A2:A7) - MARGINOFERROR(A2:A7, 0.95)
```

**Result:** `68.39`

Subtracting the margin from the mean gives the lower end of the 95 percent confidence interval.

### Example 4: Guarding the Confidence Level

Cell `D2` holds the confidence level 0.95.

```excel
=IF(AND(D2 > 0, D2 < 1), MARGINOFERROR(A2:A7, D2), "Enter a decimal between 0 and 1")
```

**Result:** `2.9434`

A value such as 95 typed as a whole number falls outside the allowed range, and the test returns the message instead of a misleading margin. Use a check like this one whenever the confidence level comes from an input cell.

## Story Problems

### Problem 1: Daily Order Counts

An online store records the orders received on each of 10 days in `B2:B11`.

| Day | Orders |
| --- | --- |
| 1 | 18 |
| 2 | 22 |
| 3 | 25 |
| 4 | 31 |
| 5 | 27 |
| 6 | 40 |
| 7 | 20 |
| 8 | 24 |
| 9 | 29 |
| 10 | 21 |

**Task:** Find the margin of error at 95 percent confidence for the average daily order count, so the team can report the range it believes the true average falls in.

**Solution:**

```excel
=MARGINOFERROR(B2:B11, 0.95)
```

**Answer:** `4.62`. The mean is 25.7 orders, so the interval runs from about 21.08 to 30.32 orders per day.

<!-- Image 2: Daily Orders Interval Worksheet. See Images/Statistical/MARGINOFERROR.md -->

### Problem 2: Customer Satisfaction Scores

A survey asks eight customers to rate their experience from 1 to 10. The ratings are in `C2:C9`.

| Customer | Rating |
| --- | --- |
| 1 | 6.5 |
| 2 | 7.0 |
| 3 | 7.5 |
| 4 | 6.0 |
| 5 | 8.0 |
| 6 | 7.0 |
| 7 | 6.5 |
| 8 | 7.5 |

**Task:** Find the margin of error at 99 percent confidence for the average rating.

**Solution:**

```excel
=MARGINOFERROR(C2:C9, 0.99)
```

**Answer:** `0.81`. The mean rating is 7.0, so the 99 percent interval runs from about 6.19 to 7.81. With only eight responses, the interval is wide.

## Use Cases

### Customer Survey Precision

**Scenario:** A research team reports the average satisfaction score and needs to show how precise it is.

```excel
=AVERAGE(Survey!C2:C500) & " plus or minus " & ROUND(MARGINOFERROR(Survey!C2:C500, 0.95), 2)
```

**Why It Works:** Reporting the margin next to the mean shows readers how much the average could move with a different sample.

### Quality Audit Sampling

**Scenario:** An auditor checks the weight of sampled packages and reports the precision of the average.

```excel
=MARGINOFERROR(Audit!D2:D41, 0.95)
```

**Why It Works:** Forty sampled packages give a tighter margin than eight, which helps the auditor decide whether the sample is large enough.

### Sample Mean Reporting

**Scenario:** A manager shares the mean wait time for a month and wants a precision figure with it.

```excel
=ROUND(AVERAGE(Waits!B2:B60), 1) & " minutes (margin " & ROUND(MARGINOFERROR(Waits!B2:B60, 0.95), 1) & ")"
```

**Why It Works:** Presenting the mean and its margin together gives the figure context without requiring the reader to run statistics.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Wrong margin | The confidence level was typed as a percentage, such as 95, instead of a decimal. | Enter 0.95 for 95 percent confidence. |
| Very wide interval | The sample is small or the values vary widely. | Collect more observations, or check the data for outliers. |
| Misleading interval | The data is strongly skewed or the sample is tiny. | Review the distribution first and consider a different method. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use `=CONFIDENCE.T(1-0.95, STDEV.S(range), COUNT(range))` as the closest equivalent. |
| Google Sheets | Available | Google-specific function. The help page defines the result as `CONFIDENCE.T(1 - confidence, STDEV(range), COUNT(range))`. |

## Tips and Best Practices

- Report the margin with the mean so readers can see the precision of the estimate.
- Enter the confidence level in its own labeled cell as a decimal, so the report can change it without editing the formula.
- Check for outliers before calculating, because one extreme value widens the margin considerably.
- Remember that the margin describes the mean only. It does not describe the spread of individual values.
- Use a larger sample when a narrower margin is needed, since the margin shrinks as the number of values grows.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Returns the sample mean that the margin is added to and subtracted from. |
| [CONFIDENCE.T](CONFIDENCE.T.md) | The Excel equivalent, which takes the alpha value and the standard deviation directly. |
| [CONFIDENCE.NORM](CONFIDENCE.NORM.md) | Gives a margin based on the normal distribution, for large samples. |
| [STDEV.S](STDEV.S.md) | Returns the sample standard deviation that the margin depends on. |
| [T.INV.2T](T.INV.2T.md) | Returns the two-tailed t value used in the margin calculation. |

## Official Documentation

- [Google Docs Editors Help: MARGINOFERROR](https://support.google.com/docs/answer/12487850)
