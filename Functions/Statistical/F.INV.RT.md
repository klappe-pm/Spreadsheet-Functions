---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Hypothesis Testing
  - Statistical Analysis
use-case:
  - Critical Value Lookup
  - Significance Thresholds
related:
  - CHISQ.INV.RT
  - F.DIST.RT
  - F.INV
  - F.TEST
  - FINV
  - T.INV.2T
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/f-inv-rt-function
  - https://support.google.com/docs/answer/7003960
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Right Tailed F Critical Value
tags:
  - critical-value
  - distribution
  - excel
  - hypothesis-testing
  - sheets
---

# F.INV.RT

## Description

**F.INV.RT** returns the F value whose right-tail probability equals the `probability` you supply. In other words, it returns the x for which F.DIST.RT(x, df1, df2) equals `probability`. This value is the critical value for an F test: an observed variance ratio above it is significant at that probability level.

The usual inputs are 0.05 for a 5 percent test and 0.01 for a 1 percent test. A smaller probability gives a larger critical value, because the test then demands stronger evidence before it declares a difference.

Use F.INV.RT when you know the significance level and need the cutoff. Use F.DIST.RT when you know the observed ratio and need its p-value. The two functions are inverses of each other, so you can check one against the other.

Excel requires the probability to be from 0 to 1, and Google Sheets requires a value strictly between 0 and 1. The degrees of freedom are each sample size minus 1, and non-integer values are truncated.

## Syntax

```excel
=F.INV.RT(probability, deg_freedom1, deg_freedom2)
```

<!-- Image 1: Critical Value at the Right Tail. See Images/Statistical/F.INV.RT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The right-tail probability, such as 0.05 or 0.01. |
| `deg_freedom1` | Yes | The numerator degrees of freedom, which is the numerator sample size minus 1. |
| `deg_freedom2` | Yes | The denominator degrees of freedom, which is the denominator sample size minus 1. |

### Return Value

The critical F value for the given right-tail probability. Excel returns `#VALUE!` when an argument is not numeric, and `#NUM!` when the probability is outside 0 to 1, a degrees-of-freedom value is less than 1, or the denominator degrees of freedom are 10^10 or more. Excel returns `#N/A` when its iterative search does not converge.

## Examples

### Example 1: Critical Value at 5 Percent

```excel
=F.INV.RT(0.05, 3, 12)
```

**Result:** `3.4903` (rounded to four decimal places)

An observed variance ratio above 3.4903 is significant at the 5 percent level with 3 and 12 degrees of freedom.

### Example 2: Critical Value at 1 Percent

```excel
=F.INV.RT(0.01, 3, 12)
```

**Result:** `5.9525` (rounded to four decimal places)

The same degrees of freedom at the stricter 1 percent level need a larger ratio, so the cutoff rises to 5.9525.

<!-- Image 2: Critical Values at Two Significance Levels. See Images/Statistical/F.INV.RT.md -->

### Example 3: Critical Value for a Different Design

```excel
=F.INV.RT(0.05, 4, 20)
```

**Result:** `2.8661` (rounded to four decimal places)

With 4 numerator and 20 denominator degrees of freedom, the 5 percent critical value is 2.8661.

## Story Problems

### Problem 1: Critical Value for a Control Group Test

A clinic compares the spread of recovery times for a control group and a treatment group. The control group has 4 patients and the treatment group has 13. The team tests at the 5 percent level.

| Group | Sample Size |
| --- | --- |
| Control | 4 |
| Treatment | 13 |

**Task:** Find the critical value for a 5 percent test, using the sample sizes in `B2:B3`.

**Solution:**

```excel
=F.INV.RT(0.05, B2-1, B3-1)
```

**Answer:** `3.4903`. The degrees of freedom are 3 and 12. If the variance ratio is above this value, the spread differs at the 5 percent level.

### Problem 2: Stricter Test for Two Teams

Two sales teams are compared for variation in weekly deal sizes. Team X has 5 weeks of data and Team Y has 21 weeks. Management wants a 1 percent test before it changes any targets.

| Team | Weeks of Data |
| --- | --- |
| Team X | 5 |
| Team Y | 21 |

**Task:** Find the critical value for a 1 percent test, using the week counts in `B2:B3`.

**Solution:**

```excel
=F.INV.RT(0.01, B2-1, B3-1)
```

**Answer:** `4.4307`. The degrees of freedom are 4 and 20. An observed ratio must exceed 4.4307 before management treats the difference as significant.

## Use Cases

### Critical Value Lookup

**Scenario:** A statistics instructor builds a table of critical values for common sample sizes so students can run F tests by hand.

```excel
=F.INV.RT(0.05, n1-1, n2-1)
```

**Why It Works:** Each row of the table holds the sample sizes for one scenario, and the formula returns the cutoff for that row. The table stays correct when the instructor changes the significance level in one cell.

### Significance Thresholds

**Scenario:** A quality team sets an alarm line so that a process review starts only when the variance ratio exceeds the 1 percent critical value.

```excel
=IF(VarRatio>F.INV.RT(0.01, DaysA-1, DaysB-1), "Review", "Within limits")
```

**Why It Works:** The formula compares the observed ratio with the critical value in one step. Keep the significance level in a labeled cell if several teams use the same threshold.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is outside the allowed range, for example a percentage typed as 5 instead of 0.05. | Enter a probability between 0 and 1, such as 0.05. |
| `#NUM!` | A degrees-of-freedom value is less than 1. | Check that each sample has at least two values. |
| `#N/A` | The iterative search did not converge. | Check the probability and degrees of freedom for unusual values. |
| `#VALUE!` | An argument is text. | Convert the value or fix the reference. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel, including Excel for the web | Uses an iterative search, so an unusual input can return `#N/A`. |
| Google Sheets | Available | Requires the probability to be greater than 0 and less than 1. Both degrees-of-freedom values must be at least 1. |

## Tips and Best Practices

- Store the significance level in one labeled cell and reference it, so every critical value updates together.
- Check the result against F.DIST.RT with the same inputs to confirm the two tails match.
- Use the critical value when you want a yes or no answer, and use F.DIST.RT when you want to report the exact p-value.
- Keep the degrees of freedom visible next to the critical value, since the same probability gives different cutoffs for different sample sizes.

## Related Functions

| Function | Relationship |
| --- | --- |
| [F.DIST.RT](F.DIST.RT.md) | Returns the right-tail p-value for an observed ratio, the inverse of this function. |
| [F.INV](F.INV.md) | Returns the left-tail value for a probability. |
| [F.TEST](F.TEST.md) | Runs a two-tailed variance test directly from two ranges. |
| [FINV](FINV.md) | The legacy name for the same right-tail calculation. |
| [T.INV.2T](T.INV.2T.md) | Two-tailed critical value for the t distribution, used for mean comparisons. |

## Official Documentation

- [Microsoft Support: F.INV.RT function](https://support.microsoft.com/en-us/excel/functions/f-inv-rt-function)
- [Google Docs Editors Help: F.INV.RT](https://support.google.com/docs/answer/7003960)
