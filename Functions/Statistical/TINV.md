---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - Legacy Workbook Maintenance
  - Two-Tailed Confidence Multipliers
related:
  - T.DIST.2T
  - T.INV
  - T.INV.2T
  - TDIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/tinv-function
  - https://support.google.com/docs/answer/6055811
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Two-Tailed Student T Critical Value
tags:
  - compatibility
  - distribution
  - excel
  - hypothesis-test
  - sheets
---

# TINV

## Description

**TINV** returns the two-tailed inverse of the Student t-distribution. You give it a probability that sits in both tails combined, and it returns the positive t-value that cuts off that probability, half in each tail. For example, a probability of 0.05 gives the critical value for a two-sided 5 percent test, or the multiplier for a 95 percent two-sided interval.

Microsoft lists TINV as a compatibility function. It is kept for older workbooks, and Microsoft states that T.INV.2T and T.INV have replaced it and that it may not be supported in future versions. In new work, use T.INV.2T, which returns the same two-tailed value. Use T.INV for a one-tailed cutoff.

TINV finds its answer by an iterative search, so it can fail to converge in rare cases. It truncates the degrees of freedom to a whole number, and it requires a probability greater than 0 and no more than 1. For a one-tailed value with TINV, double the one-tailed probability before you enter it.

## Syntax

```excel
=TINV(probability, deg_freedom)
```

<!-- Image 1: Probability and Degrees of Freedom. See Images/Statistical/TINV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The total two-tailed probability, such as 0.05. Must be greater than 0 and no more than 1. |
| `deg_freedom` | Yes | The degrees of freedom, truncated to a whole number. Must be at least 1. |

### Return Value

A positive t-value. Excel returns `#NUM!` when `probability` is 0 or less, greater than 1, or `deg_freedom` is less than 1. It returns `#VALUE!` when an argument is not numeric and `#N/A` when the search does not converge after 100 iterations.

## Examples

### Example 1: Two-Tailed 5 Percent Critical Value

```excel
=TINV(0.05, 10)
```

**Result:** `2.228139`

The critical value for a two-sided 5 percent test with 10 degrees of freedom.

### Example 2: Ninety Percent Interval Multiplier

```excel
=TINV(0.1, 20)
```

**Result:** `1.724718`

A 90 percent two-sided interval with 20 degrees of freedom uses this multiplier on the standard error.

### Example 3: Same Result as T.INV.2T

```excel
=T.INV.2T(0.05, 10)
```

**Result:** `2.228139`

T.INV.2T returns the same value as TINV for the same two-tailed probability and degrees of freedom.

### Example 4: Invalid Probability

```excel
=TINV(0, 10)
```

**Result:** `#NUM!`

A probability of 0 is outside the allowed range, so the function returns an error.

<!-- Image 2: Replacement Check. See Images/Statistical/TINV.md -->

## Story Problems

### Problem 1: Critical Value in an Old Model

An older model sets its critical value with TINV for 10 degrees of freedom and a two-sided 5 percent level. The team wants to confirm the value before they rebuild the model with a newer function.

**Task:** Find the two-tailed critical value with TINV, then confirm it with T.INV.2T.

**Solution:**

```excel
=TINV(0.05, 10)
```

**Answer:** `2.228139`. The replacement `=T.INV.2T(0.05, 10)` returns the same value.

### Problem 2: Ninety Percent Interval for a Mean

A quality analyst measured 21 parts, which gives 20 degrees of freedom. The old template uses a two-sided 90 percent interval, so it needs the 10 percent two-tailed multiplier.

**Task:** Find the multiplier for the 90 percent interval.

**Solution:**

```excel
=TINV(0.1, 20)
```

**Answer:** `1.724718`. The interval for the mean is the sample mean plus or minus this value times the standard error.

## Use Cases

### Legacy Workbook Maintenance

**Scenario:** A finance team inherits a model that uses TINV for its critical values and needs the results to stay identical while the model is updated.

```excel
=TINV(B2, C2)
```

**Why It Works:** `B2` holds the two-tailed probability and `C2` holds the degrees of freedom. The result matches T.INV.2T, so the team can switch functions and compare the two columns to confirm the change.

### Two-Tailed Confidence Multipliers

**Scenario:** A survey template needs a 95 percent margin of error for each reported mean.

```excel
=TINV(0.05, B2 - 1) * C2 / SQRT(B2)
```

**Why It Works:** `B2` is the sample size and `C2` is the standard deviation. The multiplier times the standard error gives the half-width of the interval.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The probability is 0 or less, or greater than 1. | Enter a two-tailed probability between 0 and 1. |
| `#NUM!` | `deg_freedom` is less than 1. | Check the sample size. |
| `#N/A` | The iterative search did not converge. | Check the inputs, or switch to T.INV.2T, which does not use a search. |
| Value too large | A one-tailed probability was entered without doubling it. | Double the one-tailed probability, or use T.INV for one tail. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, kept for compatibility | Replaced by T.INV.2T. Uses an iterative search that can return `#N/A`. |
| Google Sheets | Available | Described as the same function as T.INV.2T. Use the newer name in new work. |

## Tips and Best Practices

- Use T.INV.2T in new work, since it returns the same two-tailed value with a clearer name.
- Keep TINV in older workbooks and compare its results with T.INV.2T before replacing it.
- Double a one-tailed probability before you enter it into TINV, and say so in the sheet notes.
- Store the probability in a labeled cell so the confidence level is easy to change.

## Related Functions

| Function | Relationship |
| --- | --- |
| [T.INV.2T](T.INV.2T.md) | Modern replacement that returns the same two-tailed value. |
| [T.INV](T.INV.md) | Returns the left-tail value for a single-tail probability. |
| [T.DIST.2T](T.DIST.2T.md) | Returns the two-tailed probability, the reverse of this function. |
| [TDIST](TDIST.md) | Legacy companion that returns the probability for a t-value. |

## Official Documentation

- [Microsoft Support: TINV function](https://support.microsoft.com/en-us/excel/functions/tinv-function)
- [Google Docs Editors Help: TINV (listed on the T.INV.2T page)](https://support.google.com/docs/answer/6055811)
