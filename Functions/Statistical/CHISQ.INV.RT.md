---
domain: Spreadsheet Functions
category: Statistical
subcategory: Hypothesis Tests
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - Critical Value Lookup
  - Goodness of Fit Cutoffs
  - Test Threshold Dashboards
related:
  - CHIINV
  - CHISQ.DIST
  - CHISQ.DIST.RT
  - CHISQ.INV
  - CHISQ.TEST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/chisq-inv-rt-function
  - https://support.google.com/docs/answer/7003348
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Chi Squared Critical Value
  - Chi Squared Right Tail Inverse
tags:
  - chi-squared
  - distribution
  - excel
  - hypothesis-testing
  - sheets
---

# CHISQ.INV.RT

## Description

**CHISQ.INV.RT** returns the critical value on the right side of a chi-squared distribution. You give it a probability (the right-tail area) and the degrees of freedom, and it returns the value x where the chance of a chi-squared result at least that large equals the probability. Analysts use it to find the cutoff for a chi-squared test at a chosen significance level, such as 0.05.

The function is the inverse of CHISQ.DIST.RT. If CHISQ.DIST.RT(x, df) returns 0.2, then CHISQ.INV.RT(0.2, df) returns x again. Use CHISQ.INV.RT when you start from a significance level and need the threshold. Use CHISQ.DIST.RT when you start from a test statistic and need its p-value.

Do not confuse it with CHISQ.INV, which works on the left tail. Using CHISQ.INV with a right-tail probability returns a different value and makes a test look significant or not significant for the wrong reason. Google Sheets documents CHISQ.INV.RT as synonymous with CHIINV.

## Syntax

```excel
=CHISQ.INV.RT(probability, deg_freedom)
```

<!-- Image 1: Right Tail Critical Value. See Images/Statistical/CHISQ.INV.RT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `probability` | Yes | The right-tail probability, the area to the right of the critical value. It must be between 0 and 1. Values below 0 or above 1 return `#NUM!`. |
| `deg_freedom` | Yes | The degrees of freedom. A value that is not an integer is truncated. A value below 1 returns `#NUM!`. |

In Google Sheets the second argument is named `degrees_freedom`. The arguments work in the same order.

### Return Value

A number greater than or equal to 0: the chi-squared value whose right-tail area equals `probability`. The result grows as the probability gets smaller, because a smaller tail area needs a larger cutoff.

## Examples

### Example 1: Critical Value for a Probability and Degrees of Freedom

```excel
=CHISQ.INV.RT(0.1, 3)
```

**Result:** `6.251389`

A chi-squared value of 6.251389 with 3 degrees of freedom leaves 10 percent of the distribution to its right.

### Example 2: Probability and Degrees of Freedom From Cells

Cell `A2` holds `0.01` and cell `A3` holds `6`.

```excel
=CHISQ.INV.RT(A2, A3)
```

**Result:** `16.811894`

Keeping the inputs in cells lets a reviewer change the significance level or the group count without editing the formula.

### Example 3: Compare a Test Statistic With the Cutoff

Cell `B2` holds the test statistic `12.4`. Cell `B3` holds the degrees of freedom, `5`.

```excel
=IF(B2>CHISQ.INV.RT(0.05, B3), "Reject", "Keep")
```

**Result:** `Reject`

The cutoff at the 0.05 level with 5 degrees of freedom is 11.070498. The statistic 12.4 is larger, so the result falls in the rejection area.

<!-- Image 2: Statistic Against the Cutoff. See Images/Statistical/CHISQ.INV.RT.md -->

### Example 4: Fractional Degrees of Freedom

```excel
=CHISQ.INV.RT(0.1, 3.8)
```

**Result:** `6.251389`

The degrees of freedom 3.8 is truncated to 3, so the result matches Example 1. Do not rely on fractional degrees of freedom to mean anything; supply the integer you mean.

### Example 5: Round Trip With CHISQ.DIST.RT

```excel
=CHISQ.DIST.RT(CHISQ.INV.RT(0.2, 5), 5)
```

**Result:** `0.2`

Feeding the cutoff back into the right-tail function returns the original probability. This check confirms that the two functions use the same distribution.

## Story Problems

### Problem 1: Packaging Defect Test

A plant checks defects across five defect types. The team uses a significance level of 0.02. The test statistic for the week is in `E2`.

| Defect Type | Units Inspected |
| --- | --- |
| Torn Seal | 140 |
| Crooked Label | 95 |
| Short Fill | 120 |
| Dented Corner | 88 |
| Wrong Barcode | 102 |

Test statistic in `E2`: `10.8`. Degrees of freedom in `E3`: `4` (five categories minus one).

**Task:** Find the critical value at the 0.02 level and decide whether the test statistic is in the rejection area.

**Solution:**

```excel
=CHISQ.INV.RT(0.02, E3)
```

**Answer:** `11.667843`. The test statistic 10.8 is below the cutoff, so the defect pattern does not reject the assumed mix at this level.

### Problem 2: Call Center Routing Check

A call center routes calls into seven categories and tests the routing against a plan at a significance level of 0.025. Seven categories give 6 degrees of freedom. The test statistic is in `C2`, and it equals `15.2`.

**Task:** Compute the cutoff and decide whether to reject the routing plan.

**Solution:**

```excel
=IF(C2>CHISQ.INV.RT(0.025, 6), "Reject", "Keep")
```

**Answer:** `Reject`. The cutoff is 14.449375, and 15.2 is larger, so the routing differs from the plan at this level.

## Use Cases

### Goodness of Fit Threshold in a Report

**Scenario:** A quality team reviews a monthly report that checks whether defect counts follow the expected mix. The significance level is set in a single cell so the reviewer can change it.

```excel
=CHISQ.INV.RT(Alpha, Categories - 1)
```

**Why It Works:** The named cells `Alpha` and `Categories` hold the inputs. The result is the cutoff that every row of the report compares its statistic against.

### Critical Value Table for Several Levels

**Scenario:** An analyst builds a small table that shows the cutoff for common significance levels at a fixed degrees of freedom, so readers can pick a level without recalculating.

```excel
=CHISQ.INV.RT(B2, $E$1)
```

**Why It Works:** Each row in column B holds one level (0.10, 0.05, 0.01). The header cell `E1` holds the degrees of freedom and stays fixed with absolute references.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | One argument is text or blank. | Convert the value with `VALUE` or check the cell that feeds the argument. |
| `#NUM!` | `probability` is below 0 or above 1. | Enter a probability between 0 and 1. |
| `#NUM!` | `deg_freedom` is below 1. | Use at least 1 degree of freedom. |
| `#N/A` | The iterative search did not converge after 64 iterations. | Check the inputs for extreme values, such as a very small probability with a very large degree of freedom. |
| Wrong decision | `CHISQ.INV` was used where a right-tail value was needed. | Use `CHISQ.INV.RT` for a right-tail cutoff. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed for Excel 2016, Excel 2019, Excel 2021, Excel 2024 and Microsoft 365 | Returns `#N/A` when the internal search fails to converge. |
| Google Sheets | Available | The help page states that the function is synonymous with CHIINV. The argument is named `degrees_freedom`. |

## Tips and Best Practices

- Store the significance level in a labeled cell so the cutoff updates when the policy changes.
- Pair the function with CHISQ.DIST.RT when you need both the cutoff and the p-value for the same test.
- Round the displayed cutoff for reports, but keep the full value in calculations to avoid decisions that flip on rounding.
- Check the degrees of freedom before you use the result: for a goodness of fit test it is the number of categories minus one.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHIINV](CHIINV.md) | Earlier name for the same right-tail inverse. |
| [CHISQ.DIST](CHISQ.DIST.md) | Left-tail and density values for the chi-squared distribution. |
| [CHISQ.DIST.RT](CHISQ.DIST.RT.md) | Right-tail probability for a given statistic, the inverse of this function. |
| [CHISQ.INV](CHISQ.INV.md) | Left-tail inverse, used when the probability is measured from the left. |
| [CHISQ.TEST](CHISQ.TEST.md) | Runs the full independence test on a table of counts. |

## Official Documentation

- [Microsoft Support: CHISQ.INV.RT function](https://support.microsoft.com/en-us/excel/functions/chisq-inv-rt-function)
- [Google Docs Editors Help: CHISQ.INV.RT](https://support.google.com/docs/answer/7003348)
