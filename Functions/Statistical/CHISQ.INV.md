---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Hypothesis Testing
  - Probability
  - Statistical Analysis
use-case:
  - Confidence Bound Limits
  - Critical Value Thresholds
  - Process Variance Limits
related:
  - CHIINV
  - CHISQ.DIST
  - CHISQ.INV.RT
  - CHISQ.TEST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/chisq-inv-function
  - https://support.google.com/docs/answer/7004181
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Chi Squared Inverse
  - Chi Squared Left Tail Inverse
tags:
  - chi-squared
  - distributions
  - excel
  - probability
  - sheets
---

# CHISQ.INV

## Description

**CHISQ.INV** returns the chi-squared value whose left-tail cumulative probability equals the probability you supply. It is the reverse of CHISQ.DIST with TRUE: you give a probability and degrees of freedom, and it returns the x value at which that probability is reached.

Use it for values that sit on the lower side of the distribution. A lower confidence bound for a variance, for example, uses a left-tail probability near 0.975. For critical values in a test that uses the upper tail, CHISQ.INV.RT is the matching function.

CHISQ.INV replaced the left-tail portion of the legacy functions. Microsoft points to CHISQ.INV.RT for the right tail, which replaces CHIINV. Google Sheets documents CHISQ.INV with the same arguments.

## Syntax

```excel
=CHISQ.INV(probability, deg_freedom)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/CHISQ.INV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The left-tail cumulative probability. It must be greater than 0 and less than 1. |
| `deg_freedom` | Yes | The number of degrees of freedom. It must be from 1 to 10^10. Non-integers are truncated. |

### Return Value

The x value whose left-tail probability equals `probability`. The function returns `#VALUE!` when an argument is not numeric. It returns `#NUM!` when `probability` is below 0 or above 1, or when `deg_freedom` is below 1 or above 10^10.

## Examples

### Example 1: Inverse for a High Probability

```excel
=CHISQ.INV(0.93, 1)
```

**Result:** `3.2830`

The value 3.2830 is the point with 93 percent of a one-degree-of-freedom chi-squared distribution at or below it.

### Example 2: A Lower Probability

```excel
=CHISQ.INV(0.6, 2)
```

**Result:** `1.8326`

With 2 degrees of freedom, 60 percent of the distribution lies at or below 1.8326.

### Example 3: Reading Inputs From Cells

Row 2 holds the probability 0.95 in `B2` and 4 degrees of freedom in `C2`.

```excel
=CHISQ.INV(B2, C2)
```

**Result:** `9.4877`

Storing the probability in a cell lets the same formula produce the bound for any confidence level.

<!-- Image 2: Inverse Reads the Curve Backward. See Images/Statistical/CHISQ.INV.md -->

### Example 4: Round Trip Check

```excel
=CHISQ.DIST(CHISQ.INV(0.6, 2), 2, TRUE)
```

**Result:** `0.6`

Passing the result of Example 2 back into CHISQ.DIST returns the original probability, which confirms the two functions agree.

## Story Problems

### Problem 1: Lower Bound on Variance

A quality analyst takes a sample of 7 measurements, which gives 6 degrees of freedom. The analyst needs the left-tail value at the 5 percent level to find a lower bound on the variance.

| Input | Value |
| --- | --- |
| Probability | 0.05 |
| Degrees of Freedom | 6 |

**Task:** Find the left-tail chi-squared value using the inputs in `B1:B2`.

**Solution:**

```excel
=CHISQ.INV(B1, B2)
```

**Answer:** `1.6354`. The variance bound uses this value in the denominator, so a smaller value gives a wider bound.

### Problem 2: Mid-Range Cutoff for Ten Readings

A sensor logs 11 readings, which gives 10 degrees of freedom. The engineer needs the value that only 2.5 percent of the distribution falls below.

| Input | Value |
| --- | --- |
| Probability | 0.025 |
| Degrees of Freedom | 10 |

**Task:** Find the value using the inputs in `B1:B2`.

**Solution:**

```excel
=CHISQ.INV(B1, B2)
```

**Answer:** `3.2470`. Only 2.5 percent of the distribution lies below this point.

## Use Cases

### Confidence Bound Limits

**Scenario:** A lab reports a 95 percent lower confidence bound on the variance of 12 measurements, using the sample variance in `C2`.

```excel
=(B2 - 1) * C2 / CHISQ.INV(0.975, B2 - 1)
```

**Why It Works:** The formula uses the 97.5 percent left-tail value, which is the standard choice for the lower bound of a two-sided 95 percent interval. `B2` holds the sample size.

### Critical Value Thresholds

**Scenario:** A reviewer needs the left-tail value at 5 percent for a test with 9 degrees of freedom.

```excel
=CHISQ.INV(0.05, 9)
```

**Why It Works:** The formula returns the lower cutoff directly, which helps when a test or review rule is written on the lower side.

### Process Variance Limits

**Scenario:** A process team sets an upper bound on the variance of 15 samples, using the sample variance in `C5`.

```excel
=(B5 - 1) * C5 / CHISQ.INV(0.025, B5 - 1)
```

**Why It Works:** The 2.5 percent left-tail value gives the upper bound of a two-sided 95 percent interval, so the limit tightens when the sample variance is smaller.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `probability` is below 0 or above 1. | Enter a probability from 0 to 1, not a percentage. |
| `#NUM!` | `deg_freedom` is below 1 or above 10^10. | Enter a whole number of degrees of freedom within the range. |
| `#VALUE!` | An argument is text. | Convert the inputs to numbers. |
| Bound is on the wrong side | The right-tail probability was entered. | CHISQ.INV uses the left tail. Use CHISQ.INV.RT for the right tail. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Left-tail inverse. Use CHISQ.INV.RT for the right-tail inverse that replaces CHIINV. |
| Google Sheets | Available | Same arguments in the same order. The probability must be greater than 0 and less than 1, and the degrees of freedom must be at least 1. |

## Tips and Best Practices

- Convert a two-sided 95 percent interval into left-tail probabilities of 0.025 and 0.975 before you call this function.
- Use CHISQ.INV.RT when the critical value is on the right tail, as in most goodness-of-fit tests.
- Check a result with CHISQ.DIST using TRUE, as in Example 4, to confirm the probability returns.
- Keep the sample size and degrees of freedom in labeled cells, so a reviewer can see how the bound was built.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHIINV](CHIINV.md) | The legacy right-tail inverse that CHISQ.INV.RT replaces. |
| [CHISQ.DIST](CHISQ.DIST.md) | The forward function, which returns the probability for an x value. |
| [CHISQ.INV.RT](CHISQ.INV.RT.md) | The right-tail inverse, used for critical values in upper-tail tests. |
| [CHISQ.TEST](CHISQ.TEST.md) | Returns the p-value for a table of observed and expected counts. |

## Official Documentation

- [Microsoft Support: CHISQ.INV function](https://support.microsoft.com/en-us/excel/functions/chisq-inv-function)
- [Google Docs Editors Help: CHISQ.INV](https://support.google.com/docs/answer/7004181)
