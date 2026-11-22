---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - Legacy Workbook Maintenance
  - Two-Tailed Probability Checks
related:
  - T.DIST
  - T.DIST.2T
  - T.DIST.RT
  - T.TEST
  - TINV
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/tdist-function
  - https://support.google.com/docs/answer/3295914
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Student T Probability
tags:
  - compatibility
  - distribution
  - excel
  - hypothesis-test
  - sheets
---

# TDIST

## Description

**TDIST** returns the probability of a Student t-value from a t-distribution, with the number of tails chosen by the `tails` argument. With `tails` set to `1`, it returns the one-tailed probability that a t-value exceeds `x`. With `tails` set to `2`, it returns the two-tailed probability that the absolute t-value exceeds `x`.

Microsoft lists TDIST as a compatibility function. It remains available for older workbooks, but Microsoft states that newer functions have replaced it and that it may not be supported in future versions. Use T.DIST.RT for the one-tailed case and T.DIST.2T for the two-tailed case in new work. T.DIST.RT accepts negative `x` values, which TDIST does not, while T.DIST.2T, like TDIST, requires a non-negative `x`.

TDIST truncates `deg_freedom` and `tails` to whole numbers. The value of `x` must be zero or greater in Excel, and the degrees of freedom must be at least 1. Keep TDIST in place when a workbook already depends on it, and replace it when the workbook is being rebuilt.

## Syntax

```excel
=TDIST(x, deg_freedom, tails)
```

<!-- Image 1: Tails Argument Choices. See Images/Statistical/TDIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The t-value to evaluate. Must be zero or greater in Excel. |
| `deg_freedom` | Yes | The degrees of freedom, truncated to a whole number. Must be at least 1. |
| `tails` | Yes | `1` for the one-tailed probability or `2` for the two-tailed probability. Other values return `#NUM!`. |

### Return Value

A probability between 0 and 1. Excel returns `#VALUE!` when an argument is not numeric, `#NUM!` when `deg_freedom` is less than 1, `tails` is not 1 or 2, or `x` is negative.

## Examples

### Example 1: Two-Tailed Probability

```excel
=TDIST(2.2, 14, 2)
```

**Result:** `0.045100`

The two-tailed probability for a t-value of 2.2 with 14 degrees of freedom.

### Example 2: One-Tailed Probability

```excel
=TDIST(2.2, 14, 1)
```

**Result:** `0.022550`

The one-tailed result is half the two-tailed result for the same inputs.

### Example 3: Large Sample Two-Tailed Value

```excel
=TDIST(1.96, 60, 2)
```

**Result:** `0.054645`

With 60 degrees of freedom, a t-value of 1.96 produces a two-tailed probability close to the familiar 5 percent level.

### Example 4: Negative Input

```excel
=TDIST(-1, 10, 2)
```

**Result:** `#NUM!`

TDIST rejects a negative `x`. Wrap the value in ABS, which gives the same two-tailed result, or use T.DIST.2T.

<!-- Image 2: Replacement Formulas. See Images/Statistical/TDIST.md -->

## Story Problems

### Problem 1: Maintaining an Old Quality Report

A legacy quality report calculates a two-tailed p-value from a t-statistic of 2.2 with 14 degrees of freedom. The team wants to confirm that the replacement function gives the same answer before they update the report.

| Statistic | Degrees of Freedom |
| --- | --- |
| 2.2 | 14 |

**Task:** Find the two-tailed probability with TDIST, then check it against T.DIST.2T.

**Solution:**

```excel
=TDIST(B2, C2, 2)
```

**Answer:** `0.045100`. The replacement `=T.DIST.2T(B2, C2)` returns the same value, so the report can move to the newer function without changing its numbers.

### Problem 2: One-Tailed Growth Check

A sales lead tested whether a campaign lifted sales in one direction only. The statistic is 1.8 with 20 degrees of freedom.

**Task:** Find the one-tailed probability.

**Solution:**

```excel
=TDIST(1.8, 20, 1)
```

**Answer:** `0.043482`. The same result comes from `=T.DIST.RT(1.8, 20)`.

## Use Cases

### Legacy Workbook Maintenance

**Scenario:** An analyst inherits a workbook from several years ago that uses TDIST in many cells and needs to keep it working while the team plans a rebuild.

```excel
=TDIST(ABS(B2), C2, 2)
```

**Why It Works:** `B2` holds the statistic and `C2` holds the degrees of freedom. The formula keeps the original two-tailed behavior, and ABS protects it from a negative statistic that would otherwise return `#NUM!`.

### Two-Tailed Probability Checks

**Scenario:** A review sheet flags any test whose two-tailed probability falls below 5 percent.

```excel
=IF(TDIST(ABS(B2), C2, 2) < 0.05, "Significant", "Not Significant")
```

**Why It Works:** ABS makes the check work for negative statistics, and the tails argument of 2 keeps the test two-sided.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is negative. | Wrap the statistic in ABS for a two-tailed check. |
| `#NUM!` | `tails` is not 1 or 2. | Enter 1 or 2. |
| `#NUM!` | `deg_freedom` is less than 1. | Check the sample size. |
| `#VALUE!` | An argument is text. | Confirm each argument is a number. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, kept for compatibility | Replaced by T.DIST.RT and T.DIST.2T. Returns `#NUM!` for negative `x`. |
| Google Sheets | Available | Accepts `tails` values of 1 and 2. The documentation does not describe error conditions. |

## Tips and Best Practices

- Use T.DIST.2T or T.DIST.RT in new work, because they accept more inputs and are named for the tail they return.
- Keep TDIST in older workbooks and check the results against the replacement before changing formulas.
- Note that TDIST truncates degrees of freedom, so enter a whole number to avoid surprises.
- Document the tails value beside each formula so the one-tailed and two-tailed results are not confused.

## Related Functions

| Function | Relationship |
| --- | --- |
| [T.DIST.2T](T.DIST.2T.md) | Modern replacement for the two-tailed case, with the same result for a non-negative `x`. |
| [T.DIST.RT](T.DIST.RT.md) | Modern replacement for the one-tailed case, with the same result for a non-negative `x`. |
| [T.DIST](T.DIST.md) | Returns the cumulative or density value rather than a tail probability. |
| [T.TEST](T.TEST.md) | Runs a complete t-test and returns its p-value. |
| [TINV](TINV.md) | Legacy companion that returns the two-tailed critical value. |

## Official Documentation

- [Microsoft Support: TDIST function](https://support.microsoft.com/en-us/excel/functions/tdist-function)
- [Google Docs Editors Help: TDIST](https://support.google.com/docs/answer/3295914)
