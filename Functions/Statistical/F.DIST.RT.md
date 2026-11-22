---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - Process Variance Review
  - Significance Testing
  - Test Score Comparison
related:
  - CHISQ.DIST.RT
  - F.DIST
  - F.INV.RT
  - F.TEST
  - FDIST
  - T.DIST.RT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/f-dist-rt-function
  - https://support.google.com/docs/answer/6055799
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Right Tailed F Probability
tags:
  - distribution
  - excel
  - hypothesis-testing
  - p-value
  - sheets
---

# F.DIST.RT

## Description

**F.DIST.RT** returns the right-tailed F probability, which is the chance of seeing an F value greater than `x` when both samples come from populations with the same variance. In other words, it returns P(F > x). This is the number most people need when they test whether two variances differ, because a small result means the observed ratio would be unusual if the variances were equal.

F.DIST.RT and F.DIST are two views of the same curve. Mathematically, F.DIST.RT(x, df1, df2) equals 1 minus F.DIST(x, df1, df2, TRUE). Use F.DIST.RT when the question is "how unusual is this result," and use F.DIST when the question is "how much of the curve lies below this result."

The degrees of freedom are each sample size minus 1, and non-integer values are truncated. Microsoft documents FDIST as the same right-tail calculation under the older name. New workbooks should use F.DIST.RT.

## Syntax

```excel
=F.DIST.RT(x, deg_freedom1, deg_freedom2)
```

<!-- Image 1: Right Tail Area Under the F Curve. See Images/Statistical/F.DIST.RT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The F value to test. It must not be negative. |
| `deg_freedom1` | Yes | The numerator degrees of freedom, which is the numerator sample size minus 1. |
| `deg_freedom2` | Yes | The denominator degrees of freedom, which is the denominator sample size minus 1. |

### Return Value

A probability from 0 to 1. A larger `x` gives a smaller probability. Excel returns `#VALUE!` when an argument is not numeric and `#NUM!` when `x` is negative or a degrees-of-freedom value is less than 1.

## Examples

### Example 1: Right-Tail Probability

```excel
=F.DIST.RT(3.8, 4, 20)
```

**Result:** `0.0186` (rounded to four decimal places)

Only about 1.9 percent of variance ratios with these degrees of freedom would be 3.8 or larger if the two variances were equal.

### Example 2: A Larger Threshold Gives a Smaller Tail

```excel
=F.DIST.RT(2.9, 4, 20)
```

**Result:** `0.0482` (rounded to four decimal places)

The same degrees of freedom with a smaller `x` leave more of the curve in the right tail. The result is larger than in Example 1.

<!-- Image 2: Tail Area at Two Thresholds. See Images/Statistical/F.DIST.RT.md -->

### Example 3: Flagging a Significant Result

```excel
=IF(F.DIST.RT(3.8, 4, 20)<0.05, "Significant", "Not significant")
```

**Result:** `Significant`

The probability in Example 1 is below 0.05, so the test flags the variance difference at the 5 percent level.

## Story Problems

### Problem 1: Teaching Methods Comparison

A school compares the spread of test scores for two teaching methods. Method A has 5 students and Method B has 21 students. The variance of Method A divided by the variance of Method B is 3.1.

| Group | Students |
| --- | --- |
| Method A | 5 |
| Method B | 21 |

**Task:** Find the right-tail probability for a variance ratio of 3.1, using the student counts in `B2:B3`.

**Solution:**

```excel
=F.DIST.RT(3.1, B2-1, B3-1)
```

**Answer:** `0.0388`. The degrees of freedom are 4 and 20. Because 0.0388 is below 0.05, the score spread differs between the methods at the 5 percent level.

### Problem 2: Warehouse Picking Times

A warehouse compares picking times on a day shift and a night shift. The day shift has 4 pickers and the night shift has 31 pickers. The variance ratio of day to night is 2.6.

| Shift | Pickers |
| --- | --- |
| Day | 4 |
| Night | 31 |

**Task:** Find the right-tail probability for the ratio 2.6, using the picker counts in `B2:B3`.

**Solution:**

```excel
=F.DIST.RT(2.6, B2-1, B3-1)
```

**Answer:** `0.0705`. The degrees of freedom are 3 and 30. Because 0.0705 is above 0.05, the evidence is not strong enough to call the spreads different.

## Use Cases

### Process Variance Review

**Scenario:** A quality engineer checks whether a new filling process is more consistent than the old one, using the variance ratio from two sample runs.

```excel
=F.DIST.RT(VarOld/VarNew, NOld-1, NNew-1)
```

**Why It Works:** The ratio of old variance to new variance is the test statistic. A small p-value means the old process is unusually more variable than the new one. Check that the larger variance is in the numerator when you expect the old process to be worse.

### Test Score Comparison

**Scenario:** A department head reviews whether two classes show different spreads in exam scores before comparing their averages.

```excel
=IF(F.DIST.RT(VarRatio, B2-1, B3-1)<0.05, "Spread differs", "No clear difference")
```

**Why It Works:** The IF wrapper turns the p-value into a label that a reader can act on. It does not replace judgment about sample size, so keep the raw p-value visible in an adjacent cell.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative, or a degrees-of-freedom value is less than 1. | Check that `x` is zero or positive and that each sample has at least two values. |
| `#VALUE!` | An argument is text. | Convert the value or fix the reference. |
| Unexpectedly large p-value | The variances were swapped, so the ratio is below 1 when a large value was expected. | Confirm which variance is in the numerator. |
| Result looks reversed | The sample size was entered instead of sample size minus 1. | Subtract 1 from each sample size. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel, including Excel for the web | Microsoft documents FDIST as the same calculation under the older name. |
| Google Sheets | Available | Requires `x` to be positive. Both degrees-of-freedom values must be greater than 1 and no more than 10^10. |

## Tips and Best Practices

- Compare the p-value with a threshold you chose before looking at the data, such as 0.05 or 0.01.
- Use F.DIST.RT instead of FDIST in new work, because the dotted names match the rest of the F function family.
- Check the variance ratio direction before you read the result, since swapping the variances changes the answer.
- Keep the sample sizes in their own cells so the degrees of freedom are visible to reviewers.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHISQ.DIST.RT](CHISQ.DIST.RT.md) | Right-tail probability for the chi square distribution, used for single-variance tests. |
| [F.DIST](F.DIST.md) | Left-tail probability. F.DIST and F.DIST.RT sum to 1. |
| [F.INV.RT](F.INV.RT.md) | Returns the critical F value for a right-tail probability, the inverse of this function. |
| [F.TEST](F.TEST.md) | Runs a two-tailed variance test directly from two ranges. |
| [FDIST](FDIST.md) | The legacy name for the same right-tail calculation. |
| [T.DIST.RT](T.DIST.RT.md) | Right-tail probability for the t distribution, used for mean comparisons. |

## Official Documentation

- [Microsoft Support: F.DIST.RT function](https://support.microsoft.com/en-us/excel/functions/f-dist-rt-function)
- [Google Docs Editors Help: F.DIST.RT](https://support.google.com/docs/answer/6055799)
