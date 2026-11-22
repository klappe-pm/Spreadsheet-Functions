---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - Critical Value Cutoffs
  - Lower Tail Thresholds
  - Small Sample Confidence Bounds
related:
  - NORM.S.INV
  - T.DIST
  - T.INV.2T
  - TINV
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/t-inv-function
  - https://support.google.com/docs/answer/6055809
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Inverse Student T
tags:
  - distribution
  - excel
  - probability
  - sheets
  - statistical
---

# T.INV

## Description

**T.INV** returns the t-value whose left-tail probability equals the `probability` you supply, for a Student t-distribution with the given degrees of freedom. It runs the calculation in reverse: T.DIST takes a t-value and returns a probability, while T.INV takes a probability and returns the t-value.

Use T.INV to set a cutoff. For a lower-tail threshold, enter the probability of the low outcome you want to flag, such as 0.05 for the lowest 5 percent. For an upper-tail cutoff, enter 1 minus the tail probability, such as 0.95 for a one-sided 5 percent test, because T.INV works from the left side of the distribution.

The probability must be greater than 0 and less than 1. The degrees of freedom must be at least 1, and a fractional value is truncated to a whole number. For a two-tailed cutoff, use T.INV.2T, which takes the total probability in both tails.

## Syntax

```excel
=T.INV(probability, deg_freedom)
```

<!-- Image 1: Probability and Degrees of Freedom. See Images/Statistical/T.INV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The left-tail probability. Must be greater than 0 and less than 1. |
| `deg_freedom` | Yes | The degrees of freedom. A fractional value is truncated. Must be at least 1. |

### Return Value

A t-value. Negative results occur when the probability is below 0.5, and positive results when it is above 0.5. Excel returns `#NUM!` when `probability` is 0 or less, 1 or more, or `deg_freedom` is less than 1, and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Upper Cutoff for a Small Sample

```excel
=T.INV(0.9, 15)
```

**Result:** `1.340606`

Ninety percent of t-values with 15 degrees of freedom fall at or below 1.340606.

### Example 2: One-Sided 5 Percent Test

```excel
=T.INV(0.95, 24)
```

**Result:** `1.710882`

A one-sided test at the 5 percent level with 24 degrees of freedom rejects results above this value.

### Example 3: Lower Cutoff

```excel
=T.INV(0.05, 12)
```

**Result:** `-1.782288`

The lowest 5 percent of t-values with 12 degrees of freedom sit below -1.782288. The sign is negative because the probability is below 0.5.

### Example 4: Median Is Zero

```excel
=T.INV(0.5, 10)
```

**Result:** `0`

The distribution is symmetric, so half of all t-values fall below zero.

<!-- Image 2: Lower and Upper Cutoffs. See Images/Statistical/T.INV.md -->

## Story Problems

### Problem 1: Maximum Allowed Lift

A marketing team ran a one-sided test on 25 weeks of data, which gives 24 degrees of freedom. They accept a lift only if the statistic clears the 95 percent point of the distribution.

**Task:** Find the t-value that the statistic must exceed for a one-sided 5 percent test.

**Solution:**

```excel
=T.INV(0.95, 24)
```

**Answer:** `1.710882`. A lift statistic above this value is significant at the 5 percent level in one direction.

### Problem 2: Lowest Five Percent of Returns

A portfolio manager reviewed 13 monthly returns, which gives 12 degrees of freedom. She wants the t-value that marks the worst 5 percent of outcomes.

**Task:** Find the lower 5 percent cutoff.

**Solution:**

```excel
=T.INV(0.05, 12)
```

**Answer:** `-1.782288`. Any standardized return below this value falls in the lowest 5 percent.

## Use Cases

### Critical Value Cutoffs

**Scenario:** A lab sets its alert threshold for a small-sample test before the samples arrive, so every result is judged against the same cutoff.

```excel
=T.INV(B2, C2 - 1)
```

**Why It Works:** `B2` holds the confidence level as a probability and `C2` holds the sample count, so the degrees of freedom are one less than the count. Each formula returns a fixed cutoff for that confidence level and sample size, which avoids typing the cutoff by hand.

### Lower Tail Thresholds

**Scenario:** A logistics team flags weeks whose on-time ratio falls in the lowest 5 percent of the historical t-distribution.

```excel
=IF(B2 < T.INV(0.05, C2), "Flag Week", "Normal")
```

**Why It Works:** `B2` holds the standardized weekly score and `C2` holds the degrees of freedom. Comparing the score with the lower cutoff gives a simple flag rule.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is 0 or less, or 1 or more. | Enter a probability strictly between 0 and 1. |
| `#NUM!` | `deg_freedom` is less than 1. | Check the sample size. |
| Wrong sign | The probability is below 0.5, so the result is negative. | Use the sign as given, or switch to the upper-tail probability on purpose. |
| Wrong cutoff for a two-sided test | This function uses one tail, but the test needs both tails. | Use T.INV.2T for a two-sided cutoff. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2010 and later, including Microsoft 365 | Returns a left-tailed inverse. The older TINV is two-tailed and remains for compatibility. |
| Google Sheets | Available | Same arguments and order. Fractional degrees of freedom are truncated. |

## Tips and Best Practices

- Store probabilities in labeled cells so the confidence level is visible and easy to change.
- Use T.INV.2T for a two-sided test, and avoid doubling the probability by hand.
- Check the sign of the result against the probability before you compare it with a statistic.
- Pair the cutoff with T.DIST.RT or T.DIST to show the probability behind it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NORM.S.INV](NORM.S.INV.md) | Inverse of the standard normal distribution, the large-sample counterpart. |
| [T.DIST](T.DIST.md) | Returns the probability for a t-value, the reverse of this function. |
| [T.INV.2T](T.INV.2T.md) | Returns the two-tailed critical value, with both tails counted. |
| [TINV](TINV.md) | Older two-tailed inverse kept for compatibility. |

## Official Documentation

- [Microsoft Support: T.INV function](https://support.microsoft.com/en-us/excel/functions/t-inv-function)
- [Google Docs Editors Help: T.INV](https://support.google.com/docs/answer/6055809)
