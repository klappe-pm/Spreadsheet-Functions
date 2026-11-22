---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Hypothesis Testing
  - Statistical Analysis
use-case:
  - Critical Value Lookups
  - Quality Test Thresholds
  - Survey Significance Cutoffs
related:
  - CHIDIST
  - CHISQ.DIST.RT
  - CHISQ.INV
  - CHISQ.INV.RT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/chiinv-function
  - https://support.google.com/docs/answer/7003198
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Chi Squared Critical Value
  - Chi Squared Inverse Right Tail
tags:
  - chi-squared
  - compatibility
  - excel
  - hypothesis-testing
  - sheets
---

# CHIINV

## Description

**CHIINV** returns the chi-squared value whose right-tail probability equals the probability you supply. It is the reverse of CHIDIST. In a hypothesis test, you pass the significance level, such as 0.05, and the degrees of freedom, and receive the critical value. A test statistic larger than that value is significant at the chosen level.

Use it to set a cutoff before you run a test, or to check whether an observed statistic clears the cutoff. The probability is a right-tail value, so 0.05 means the area in the upper 5 percent of the distribution.

Microsoft replaced CHIINV with CHISQ.INV.RT, which returns the same right-tail value. CHISQ.INV returns the left-tail value. CHIINV remains available for backward compatibility, but Microsoft warns it may not be available in future versions. Use CHISQ.INV.RT in new work.

## Syntax

```excel
=CHIINV(probability, deg_freedom)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/CHIINV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The right-tail probability, the significance level in most tests. It must be greater than 0 and less than 1. |
| `deg_freedom` | Yes | The number of degrees of freedom. It must be at least 1. Non-integers are truncated. |

### Return Value

The chi-squared value whose right-tail probability equals `probability`. The function returns `#VALUE!` when an argument is not numeric. It returns `#NUM!` when `probability` is below 0 or above 1, or when `deg_freedom` is less than 1. It returns `#N/A` when the search does not converge within 100 iterations.

## Examples

### Example 1: Critical Value at the 5 Percent Level

```excel
=CHIINV(0.05, 3)
```

**Result:** `7.8147`

For 3 degrees of freedom, a statistic above 7.8147 is significant at the 5 percent level.

### Example 2: A Stricter Cutoff

```excel
=CHIINV(0.01, 6)
```

**Result:** `16.8119`

Lowering the significance level to 1 percent raises the cutoff. With 6 degrees of freedom, the statistic must exceed 16.8119.

<!-- Image 2: Critical Value Cutoff. See Images/Statistical/CHIINV.md -->

### Example 3: Reading Inputs From Cells

Row 2 holds the probability 0.1 in `B2` and 4 degrees of freedom in `C2`.

```excel
=CHIINV(B2, C2)
```

**Result:** `7.7794`

Storing the level and degrees of freedom in cells lets the cutoff update when the test design changes.

### Example 4: The Modern Equivalent

```excel
=CHISQ.INV.RT(0.05, 3)
```

**Result:** `7.8147`

CHISQ.INV.RT returns the same critical value as Example 1 with the same arguments.

## Story Problems

### Problem 1: Four Store Regions

A chain tests whether sales are spread evenly across four regions. The test has 4 degrees of freedom, and the team uses a 5 percent significance level.

| Input | Value |
| --- | --- |
| Significance Level | 0.05 |
| Degrees of Freedom | 4 |

**Task:** Find the critical value that the test statistic must exceed, using the inputs in `B1:B2`.

**Solution:**

```excel
=CHIINV(B1, B2)
```

**Answer:** `9.4877`. A statistic above 9.4877 means the regional spread is unlikely to be even.

### Problem 2: Packaging Line Checks

A packaging line samples six machine settings and uses a 2.5 percent significance level, which gives 5 degrees of freedom. The engineer wants the cutoff for a statistic that would trigger a line review.

| Input | Value |
| --- | --- |
| Significance Level | 0.025 |
| Degrees of Freedom | 5 |

**Task:** Find the critical value using the inputs in `B1:B2`.

**Solution:**

```excel
=CHIINV(B1, B2)
```

**Answer:** `12.8325`. A statistic above this value triggers a review of the line.

## Use Cases

### Critical Value Lookups

**Scenario:** A student project needs the 10 percent cutoff for a test with 2 degrees of freedom and wants the formula to show its source.

```excel
=CHIINV(0.1, 2)
```

**Why It Works:** The formula returns the cutoff directly, so the assumptions are visible in the cell rather than hidden in a printed table.

### Quality Test Thresholds

**Scenario:** A lab sets a review threshold at the 5 percent level for a test with 6 degrees of freedom.

```excel
=CHIINV(0.05, 6)
```

**Why It Works:** The threshold is recalculated if the level changes, so the review rule stays consistent with the documented policy.

### Survey Significance Cutoffs

**Scenario:** An analyst compares a statistic in cell `D4` against a cutoff built from the number of answer groups in `B4` minus one.

```excel
=IF(D4 > CHIINV(0.05, B4 - 1), "Significant", "Not Significant")
```

**Why It Works:** Subtracting 1 from the group count gives the degrees of freedom for a goodness-of-fit test, and the comparison turns the cutoff into a readable label.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `probability` is 0 or less, or 1 or more. | Enter a significance level strictly between 0 and 1. |
| `#NUM!` | `deg_freedom` is below 1. | Check the category count and subtract 1 for a goodness-of-fit test. |
| `#N/A` | The search did not converge within 100 iterations. | Check the inputs and try the CHISQ.INV.RT replacement. |
| `#VALUE!` | An argument is text. | Convert the inputs to numbers. |
| Cutoff seems too high or too low | The level was entered as 5 instead of 0.05. | Enter the probability as a decimal. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available for backward compatibility | Replaced by CHISQ.INV.RT. Microsoft warns it may not be available in future versions. |
| Google Sheets | Available | Documented under this name and synonymous with CHISQ.INV.RT. The probability must be greater than 0 and less than 1, and the degrees of freedom must be at least 1. |

## Tips and Best Practices

- Use CHISQ.INV.RT in new Excel work, because it takes the same arguments and matches the right-tail meaning of this function.
- Choose the significance level before you look at the data, so the cutoff is not adjusted to fit the result.
- Compare the statistic with the critical value, or use CHIDIST to get the p-value for the statistic directly.
- Enter degrees of freedom as a whole number, because decimals are truncated without warning.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHIDIST](CHIDIST.md) | Returns the right-tail probability for a statistic, the reverse of this function. |
| [CHISQ.DIST.RT](CHISQ.DIST.RT.md) | The right-tail probability function, the modern counterpart of CHIDIST. |
| [CHISQ.INV](CHISQ.INV.md) | Returns the left-tail inverse for a probability. |
| [CHISQ.INV.RT](CHISQ.INV.RT.md) | The modern replacement for this function. |

## Official Documentation

- [Microsoft Support: CHIINV function](https://support.microsoft.com/en-us/excel/functions/chiinv-function)
- [Google Docs Editors Help: CHIINV](https://support.google.com/docs/answer/7003198)
