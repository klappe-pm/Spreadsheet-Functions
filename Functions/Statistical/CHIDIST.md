---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Hypothesis Testing
  - Probability
  - Statistical Analysis
use-case:
  - Ad Click Independence
  - Goodness Of Fit Reviews
  - Survey Answer Patterns
related:
  - CHIINV
  - CHISQ.DIST
  - CHISQ.DIST.RT
  - CHISQ.TEST
  - CHITEST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/chidist-function
  - https://support.google.com/docs/answer/7003346
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Right Tail Chi Squared
  - Chi Squared Right Tail
tags:
  - chi-squared
  - compatibility
  - excel
  - hypothesis-testing
  - sheets
---

# CHIDIST

## Description

**CHIDIST** returns the right-tailed probability of the chi-squared distribution. In a hypothesis test, that probability is the p-value: the chance of seeing a statistic at least as large as the one you calculated if the null hypothesis were true. A small result suggests the observed pattern is unlikely to be chance alone.

The function takes the chi-squared statistic (x) and the degrees of freedom. The degrees of freedom usually equal the number of categories minus one for a goodness-of-fit test, or (rows minus one) times (columns minus one) for a test of independence.

Microsoft replaced CHIDIST with CHISQ.DIST.RT, which returns the same right-tailed value. CHISQ.DIST returns the left-tailed cumulative probability. CHIDIST remains available for backward compatibility, but Microsoft warns it may not be available in future versions. Use CHISQ.DIST.RT in new work.

## Syntax

```excel
=CHIDIST(x, deg_freedom)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/CHIDIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the distribution, usually a chi-squared statistic. It must not be negative. |
| `deg_freedom` | Yes | The number of degrees of freedom. It must be from 1 to 10^10. Non-integers are truncated. |

### Return Value

A probability from 0 to 1. The function returns `#VALUE!` when an argument is not numeric. It returns `#NUM!` when `x` is negative, or when `deg_freedom` is below 1 or above 10^10.

## Examples

### Example 1: Right-Tail Probability

```excel
=CHIDIST(7.5, 3)
```

**Result:** `0.0576`

A statistic of 7.5 with 3 degrees of freedom has a right-tail probability of about 5.8 percent. The result is the area of the distribution at or beyond 7.5.

### Example 2: A Second Statistic

```excel
=CHIDIST(4.2, 6)
```

**Result:** `0.6496`

With 6 degrees of freedom, a statistic of 4.2 is well within the typical range, so the tail probability is high.

<!-- Image 2: Right Tail Shading. See Images/Statistical/CHIDIST.md -->

### Example 3: Reading Inputs From Cells

Row 2 holds the statistic 12.1 in `B2` and 4 degrees of freedom in `C2`.

```excel
=CHIDIST(B2, C2)
```

**Result:** `0.0166`

Keeping the statistic and the degrees of freedom in cells lets the test update when the observed counts change.

### Example 4: The Modern Equivalent

```excel
=CHISQ.DIST.RT(7.5, 3)
```

**Result:** `0.0576`

CHISQ.DIST.RT returns the same value as Example 1 with the same arguments.

## Story Problems

### Problem 1: Mobile Users By Region

A team checks whether mobile app use varies by region. The chi-squared statistic from its table is 5.4, and the test has 2 degrees of freedom.

| Input | Value |
| --- | --- |
| Chi-Squared Statistic | 5.4 |
| Degrees of Freedom | 2 |

**Task:** Find the right-tail probability for the statistic and degrees of freedom in `B1:B2`.

**Solution:**

```excel
=CHIDIST(B1, B2)
```

**Answer:** `0.0672`. A pattern this uneven would appear by chance about 6.7 percent of the time, so the team does not reach the 5 percent significance level.

### Problem 2: Support Ticket Categories

A help desk expects tickets to split evenly across four categories, which gives 3 degrees of freedom. The observed split produces a chi-squared statistic of 9.5.

| Input | Value |
| --- | --- |
| Chi-Squared Statistic | 9.5 |
| Degrees of Freedom | 3 |

**Task:** Find the p-value for the split using the inputs in `B1:B2`.

**Solution:**

```excel
=CHIDIST(B1, B2)
```

**Answer:** `0.0233`. The result is below 0.05, which suggests the ticket split is not even.

## Use Cases

### Ad Click Independence

**Scenario:** A marketer compares clicks on two ad versions in a 2 by 2 table, which has 1 degree of freedom.

```excel
=CHIDIST(C5, 1)
```

**Why It Works:** The statistic sits in cell `C5` from the test table, so the p-value updates whenever the counts change. Confirm the table size before choosing the degrees of freedom.

### Goodness Of Fit Reviews

**Scenario:** A warehouse checks whether the number of orders per shift fits an expected pattern across six shifts.

```excel
=CHIDIST(B9, 5)
```

**Why It Works:** Six categories give 5 degrees of freedom. The formula reads the statistic from `B9` so the reviewer can see where it came from.

### Survey Answer Patterns

**Scenario:** A researcher compares answer patterns across seven question groups and needs the tail probability for 6 degrees of freedom.

```excel
=CHIDIST(A2, 6)
```

**Why It Works:** The degrees of freedom are fixed by the number of groups, so only the statistic changes from one survey wave to the next.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative. | Chi-squared statistics are sums of squares, so check the calculation that produced the statistic. |
| `#NUM!` | `deg_freedom` is below 1 or above 10^10. | Use the number of categories minus one, or the table formula. |
| `#VALUE!` | An argument is text. | Convert the inputs to numbers. |
| Unexpected p-value | A left-tail result was expected. | CHIDIST is right-tailed. Use CHISQ.DIST for the left tail. |
| Unexpected p-value | Degrees of freedom were entered as a decimal, which is truncated. | Enter whole numbers of degrees of freedom. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available for backward compatibility | Replaced by CHISQ.DIST.RT for the right tail. Microsoft warns it may not be available in future versions. |
| Google Sheets | Available | Documented under this name. It is synonymous with CHISQ.DIST.RT. The statistic must be positive, and degrees of freedom must be from 1 to 10^10. |

## Tips and Best Practices

- Use CHISQ.DIST.RT in new Excel work, because the results match and the name says which tail it returns.
- Confirm the degrees of freedom from the test table, not from the number of rows or columns alone.
- Use CHISQ.TEST when you have observed and expected ranges and want the p-value directly.
- Compare the p-value with your significance level before concluding anything, and report it with the statistic.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHIINV](CHIINV.md) | Returns the statistic for a given right-tail probability, the reverse of this function. |
| [CHISQ.DIST](CHISQ.DIST.md) | Returns the left-tail cumulative probability or the density. |
| [CHISQ.DIST.RT](CHISQ.DIST.RT.md) | The modern right-tail replacement with the same arguments. |
| [CHISQ.TEST](CHISQ.TEST.md) | Returns the p-value directly from observed and expected ranges. |
| [CHITEST](CHITEST.md) | The legacy version of CHISQ.TEST. |

## Official Documentation

- [Microsoft Support: CHIDIST function](https://support.microsoft.com/en-us/excel/functions/chidist-function)
- [Google Docs Editors Help: CHIDIST](https://support.google.com/docs/answer/7003346)
