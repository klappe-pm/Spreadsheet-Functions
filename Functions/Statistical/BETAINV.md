---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Conversion Rate Floors
  - Delivery Window Planning
  - Repair Time Estimates
related:
  - BETA.DIST
  - BETA.INV
  - BETADIST
  - PERCENTILE.EXC
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/betainv-function
  - https://support.google.com/docs/answer/9061377
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Beta Inverse
  - Inverse Beta Distribution
tags:
  - beta-distribution
  - compatibility
  - excel
  - probability
  - sheets
---

# BETAINV

## Description

**BETAINV** returns the value x at which the cumulative beta distribution reaches a given probability. It is the reverse of BETADIST: if BETADIST(x, alpha, beta) returns 0.6, then BETAINV(0.6, alpha, beta) returns x. Use it to turn a target probability into a threshold, such as the number of hours that 90 percent of jobs finish within.

The beta distribution describes values that fall between two bounds, which makes it useful for shares, percentages and durations with a known minimum and maximum. The optional arguments **A** and **B** set those bounds. When they are omitted, the distribution runs from 0 to 1.

Microsoft replaced BETAINV with **BETA.INV**, which takes the same arguments in the same order. BETAINV remains in Excel for backward compatibility, but Microsoft warns that it may not be available in future versions. Use BETA.INV in new workbooks and keep BETAINV only in files that already depend on it.

## Syntax

```excel
=BETAINV(probability, alpha, beta, [A], [B])
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/BETAINV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The cumulative probability to invert. It must be greater than 0 and no greater than 1. |
| `alpha` | Yes | The first shape parameter of the distribution. It must be greater than 0. |
| `beta` | Yes | The second shape parameter of the distribution. It must be greater than 0. |
| `A` | No | The lower bound of the x interval. The default is 0. |
| `B` | No | The upper bound of the x interval. The default is 1. |

### Return Value

A number between A and B. The function returns `#VALUE!` when any argument is not numeric. It returns `#NUM!` when probability is 0 or less, when probability is greater than 1, or when alpha or beta is 0 or less.

## Examples

### Example 1: Median Estimate With Default Bounds

```excel
=BETAINV(0.6, 2, 5)
```

**Result:** `0.3094`

With A and B omitted, the search runs over 0 to 1. The value returned is the point below which 60 percent of the distribution falls.

### Example 2: Quantile With Custom Bounds

```excel
=BETAINV(0.25, 2, 5, 10, 50)
```

**Result:** `16.4465`

The same shape parameters now stretch across 10 to 50. The probability stays the same, so the result moves from the 0 to 1 scale into the 10 to 50 scale.

<!-- Image 2: Bounds Versus Default Range. See Images/Statistical/BETAINV.md -->

### Example 3: Reading Inputs From Cells

Row 2 holds the probability in `B2`, alpha in `C2`, beta in `D2`, the lower bound in `E2` and the upper bound in `F2`.

```excel
=BETAINV(B2, C2, D2, E2, F2)
```

**Result:** `34.2976` with the values 0.9, 3, 2, 0 and 40

Keeping the inputs in cells lets you change the probability or bounds without editing the formula.

### Example 4: Round Trip Check

```excel
=BETADIST(BETAINV(0.6, 2, 5), 2, 5)
```

**Result:** `0.6`

BETADIST undoes BETAINV, so the probability returns to its starting value. Use this pattern to confirm that the shape parameters and bounds match the ones you intended.

## Story Problems

### Problem 1: Repair Time Commitment

A field service team records how long each repair takes. The times follow a beta distribution with alpha 3 and beta 2 across a scope of 0 to 40 hours. The manager wants to promise a time that 90 percent of jobs finish within.

| Input | Value |
| --- | --- |
| Probability | 0.9 |
| Alpha | 3 |
| Beta | 2 |
| Lower Bound | 0 |
| Upper Bound | 40 |

**Task:** Enter the inputs in `B2:B6` and find the hour limit that 90 percent of jobs meet.

**Solution:**

```excel
=BETAINV(B2, B3, B4, B5, B6)
```

**Answer:** `34.2976` hours. Nine of every ten repairs finish within about 34.3 hours.

### Problem 2: Conversion Rate Floor

A marketing team models the monthly trial-to-paid conversion rate with a beta distribution using alpha 4 and beta 4 on the 0 to 1 scale. The team wants the rate that only the weakest 10 percent of months fall below.

| Input | Value |
| --- | --- |
| Probability | 0.1 |
| Alpha | 4 |
| Beta | 4 |

**Task:** Find the rate at the 10th percentile of the distribution.

**Solution:**

```excel
=BETAINV(B2, B3, B4)
```

**Answer:** `0.2786`. Ten percent of months convert at or below about 27.9 percent.

## Use Cases

### Repair Time Estimates

**Scenario:** A dispatcher promises customers a repair window that will be met on most visits.

```excel
=BETAINV(0.9, 3, 2, 0, 40)
```

**Why It Works:** The bounds stay inside the job scope, so the estimate never exceeds the longest possible repair. Changing 0.9 to 0.95 widens the promise.

### Delivery Window Planning

**Scenario:** A logistics planner estimates the share of a route's length covered by the first delivery of the day, with the route measured in kilometers.

```excel
=BETAINV(0.5, 2, 3, 0, 12)
```

**Why It Works:** Setting A and B to the route length keeps the result on the same scale as the input data, so the planner does not need a separate conversion step.

### Conversion Rate Floors

**Scenario:** A growth team wants a floor below which it investigates a campaign.

```excel
=BETAINV(0.05, 8, 12)
```

**Why It Works:** A low probability such as 0.05 sets the floor near the bottom of the distribution. Review the floor after each quarter, because shape parameters drift as the data changes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | Probability is 0 or less, or greater than 1. | Enter a probability above 0 and no greater than 1. |
| `#NUM!` | Alpha or beta is 0 or less. | Use positive shape parameters. |
| `#VALUE!` | An argument is text or a blank that does not evaluate to a number. | Check that each input cell holds a number. |
| Result outside the expected range | A and B are omitted for data that is not on the 0 to 1 scale. | Pass A and B explicitly. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available for backward compatibility | Replaced by BETA.INV. Microsoft warns it may not be available in future versions. |
| Google Sheets | Not documented under this name | Use BETA.INV with the same argument order. Google's help page lists the default for both bounds as 1, so pass both bounds explicitly. |

## Tips and Best Practices

- Use BETA.INV in new workbooks, because it takes the same arguments and is the current Microsoft function.
- Always pass A and B when the data is not on the 0 to 1 scale. Omitting them silently changes the answer.
- Check each result with BETADIST using the same shape parameters and bounds. The probability should return unchanged.
- Keep alpha and beta as inputs in labeled cells so a reviewer can see which distribution the formula assumes.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BETA.DIST](BETA.DIST.md) | Returns the beta probability for a given x, the forward direction of this function. |
| [BETA.INV](BETA.INV.md) | The current replacement with the same arguments. |
| [BETADIST](BETADIST.md) | The legacy cumulative beta function that BETAINV inverts. |
| [PERCENTILE.EXC](PERCENTILE.EXC.md) | Returns a percentile from observed data rather than from a fitted distribution. |

## Official Documentation

- [Microsoft Support: BETAINV function](https://support.microsoft.com/en-us/excel/functions/betainv-function)
- [Google Docs Editors Help: BETA.INV](https://support.google.com/docs/answer/9061377)
