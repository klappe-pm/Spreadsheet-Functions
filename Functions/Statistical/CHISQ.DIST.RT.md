---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Hypothesis Testing
  - Probability
  - Statistical Analysis
use-case:
  - Goodness Of Fit P Values
  - Independence Test Results
  - Variance Test P Values
related:
  - CHIDIST
  - CHISQ.DIST
  - CHISQ.INV.RT
  - CHISQ.TEST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/chisq-dist-rt-function
  - https://support.google.com/docs/answer/7003199
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Chi Squared Right Tail
  - Chi Squared P Value
tags:
  - chi-squared
  - distributions
  - excel
  - hypothesis-testing
  - sheets
---

# CHISQ.DIST.RT

## Description

**CHISQ.DIST.RT** returns the right-tailed probability of the chi-squared distribution. For a statistic x and a given number of degrees of freedom, it gives the chance of seeing a value at least as large as x. In a hypothesis test, that chance is the p-value: a small result means the observed statistic is unusual if the null hypothesis holds.

Most chi-squared tests in spreadsheets end with this calculation. A goodness-of-fit test, a test of independence and a test of a variance all compare a statistic with the right tail, so CHISQ.DIST.RT is the function that returns the p-value directly.

CHISQ.DIST.RT replaced CHIDIST in Excel. The two functions return the same values with the same arguments. Microsoft recommends CHISQ.DIST.RT for new work, and Google Sheets lists it as synonymous with CHIDIST.

## Syntax

```excel
=CHISQ.DIST.RT(x, deg_freedom)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/CHISQ.DIST.RT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The statistic at which to evaluate the distribution. It must not be negative. |
| `deg_freedom` | Yes | The number of degrees of freedom. It must be from 1 to 10^10. Non-integers are truncated. |

### Return Value

A probability from 0 to 1. The function returns `#VALUE!` when an argument is not numeric. It returns `#NUM!` when `x` is negative, or when `deg_freedom` is below 1 or above 10^10.

## Examples

### Example 1: P-Value for a Statistic

```excel
=CHISQ.DIST.RT(7.5, 3)
```

**Result:** `0.0576`

A statistic of 7.5 with 3 degrees of freedom has a p-value of about 5.8 percent. That is above 5 percent but below 10 percent.

### Example 2: Cell References

Row 2 holds the statistic 4.2 in `A2` and 6 degrees of freedom in `B2`.

```excel
=CHISQ.DIST.RT(A2, B2)
```

**Result:** `0.6496`

A high p-value like this one means the statistic is consistent with the expected pattern, so the test gives no reason to reject it.

<!-- Image 2: Right Tail Versus Left Tail. See Images/Statistical/CHISQ.DIST.RT.md -->

### Example 3: A Second Statistic

```excel
=CHISQ.DIST.RT(12.1, 4)
```

**Result:** `0.0166`

With 4 degrees of freedom, a statistic of 12.1 is in the upper tail, so the p-value is small enough to flag for review at the 5 percent level.

### Example 4: Tails Add to One

```excel
=CHISQ.DIST.RT(7.5, 3) + CHISQ.DIST(7.5, 3, TRUE)
```

**Result:** `1`

The right-tail value and the left-tail value for the same statistic always sum to 1. The check confirms that the two functions are reading the same distribution.

## Story Problems

### Problem 1: Regional Sales Spread

A chain expects sales to spread evenly across 9 stores. The test has 8 degrees of freedom, and the team computes a chi-squared statistic of 14.2 from the observed sales.

| Input | Value |
| --- | --- |
| Statistic | 14.2 |
| Degrees of Freedom | 8 |

**Task:** Find the p-value for the statistic using the inputs in `B1:B2`.

**Solution:**

```excel
=CHISQ.DIST.RT(B1, B2)
```

**Answer:** `0.0767`. The result is below 10 percent but above 5 percent, so the spread is unusual at one level and ordinary at the other.

### Problem 2: Survey Question Independence

A survey cross-tabulates answers against age groups, which gives 6 degrees of freedom. The statistic from the table is 10.6.

| Input | Value |
| --- | --- |
| Statistic | 10.6 |
| Degrees of Freedom | 6 |

**Task:** Find the p-value using the inputs in `B1:B2`.

**Solution:**

```excel
=CHISQ.DIST.RT(B1, B2)
```

**Answer:** `0.1016`. A p-value of about 10 percent does not reach the 5 percent threshold, so the answers are not clearly related to age.

## Use Cases

### Goodness Of Fit P Values

**Scenario:** A call center compares the number of calls per weekday with an expected even split across five days, which gives 4 degrees of freedom.

```excel
=CHISQ.DIST.RT(B12, 4)
```

**Why It Works:** The statistic in `B12` comes from the test table. Keep the degrees of freedom tied to the category count so the p-value stays correct when a category is added.

### Independence Test Results

**Scenario:** A researcher checks whether preferred channel depends on region in a table with 2 rows and 3 columns.

```excel
=CHISQ.DIST.RT(F4, (2 - 1) * (3 - 1))
```

**Why It Works:** The degrees of freedom for a contingency table are (rows minus 1) times (columns minus 1), which the formula shows in plain terms.

### Variance Test P Values

**Scenario:** A lab tests whether a measurement process is more variable than its target. The statistic in `C6` uses 14 degrees of freedom.

```excel
=CHISQ.DIST.RT(C6, 14)
```

**Why It Works:** For a variance test, the right tail is the region that supports the claim of excess variation, so the p-value comes from this function rather than the left tail.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative. | Check the statistic formula. Chi-squared statistics are sums of squares. |
| `#NUM!` | `deg_freedom` is below 1 or above 10^10. | Enter the number of categories minus 1, or the table degrees of freedom. |
| `#VALUE!` | An argument is text. | Convert the inputs to numbers. |
| p-value looks reversed | The left tail was expected. | CHISQ.DIST.RT is the right tail. Use CHISQ.DIST with TRUE for the left tail. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Replaces CHIDIST. Microsoft recommends it for new work. |
| Google Sheets | Available | Synonymous with CHIDIST. The value x must be positive, and degrees of freedom must be from 1 to 10^10. |

## Tips and Best Practices

- Use this function to get the p-value of a chi-squared test, and compare it with the significance level you chose before the test.
- Use CHISQ.TEST when you have observed and expected ranges and want the p-value from the table directly.
- Use CHISQ.INV.RT to find the critical value for a chosen p-value.
- Check that the degrees of freedom come from the test design, not from the number of data rows.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHIDIST](CHIDIST.md) | The legacy function that returns the same right-tail value. |
| [CHISQ.DIST](CHISQ.DIST.md) | Returns the left-tail probability or the density. |
| [CHISQ.INV.RT](CHISQ.INV.RT.md) | Returns the critical value for a right-tail probability, the reverse of this function. |
| [CHISQ.TEST](CHISQ.TEST.md) | Returns the p-value directly from observed and expected ranges. |

## Official Documentation

- [Microsoft Support: CHISQ.DIST.RT function](https://support.microsoft.com/en-us/excel/functions/chisq-dist-rt-function)
- [Google Docs Editors Help: CHISQ.DIST.RT](https://support.google.com/docs/answer/7003199)
