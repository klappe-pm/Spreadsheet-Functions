---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Hypothesis Testing
  - Probability
use-case:
  - One-Sided Growth Tests
  - Upper Tail Risk Limits
related:
  - T.DIST
  - T.DIST.2T
  - T.INV
  - T.TEST
  - TDIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/t-dist-rt-function
  - https://support.google.com/docs/answer/9369017
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Right Tail Student T Probability
tags:
  - distribution
  - excel
  - hypothesis-test
  - sheets
  - statistical
---

# T.DIST.RT

## Description

**T.DIST.RT** returns the right-tail probability of a Student t-distribution at `x`. That is the chance of a t-value greater than or equal to `x` for the given degrees of freedom. It answers one-sided questions, such as whether a new process is better than the old one in one direction only.

The function accepts negative values of `x`. When `x` is negative, the result is greater than 0.5, because most of the distribution then lies to the right. The degrees of freedom must be at least 1.

For a positive `x`, the right-tail result is exactly half the two-tailed probability from T.DIST.2T. Use T.DIST.RT when the hypothesis points one way and T.DIST.2T when it does not. T.DIST.RT replaces the one-tailed case of the older TDIST function, which is the form most older workbooks used.

## Syntax

```excel
=T.DIST.RT(x, deg_freedom)
```

<!-- Image 1: Right Tail Area. See Images/Statistical/T.DIST.RT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The t-value at which to evaluate the right tail. Negative values are allowed. |
| `deg_freedom` | Yes | The degrees of freedom, usually the sample size minus one for a single sample. Must be at least 1. |

### Return Value

A probability between 0 and 1. Excel returns `#NUM!` when `deg_freedom` is less than 1 and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Right-Tail Probability for a Positive Statistic

```excel
=T.DIST.RT(1.96, 60)
```

**Result:** `0.027322`

About 2.7 percent of results with 60 degrees of freedom are at least 1.96.

### Example 2: Negative Statistic

```excel
=T.DIST.RT(-1.98, 2)
```

**Result:** `0.906874`

A negative `x` is valid. The result is high because most of the distribution sits above -1.98.

### Example 3: Half of the Two-Tailed Result

```excel
=T.DIST.RT(2.5, 20)
```

**Result:** `0.010617`

This is half of the T.DIST.2T result for the same inputs, 0.021234, because the distribution is symmetric.

### Example 4: One-Sided Decision

```excel
=IF(T.DIST.RT(B2, 24) < 0.05, "Improvement Confirmed", "Not Confirmed")
```

**Result:** `Not Confirmed` when `B2` is 1.5, because T.DIST.RT(1.5, 24) is 0.073328, above 0.05

The test passes only when the right-tail probability falls below 5 percent, which keeps the decision rule in one visible formula.

<!-- Image 2: One-Sided Decision Rule. See Images/Statistical/T.DIST.RT.md -->

## Story Problems

### Problem 1: Conversion Lift

A web team ran a one-sided test on a new checkout page across 21 days, which gives 20 degrees of freedom. The statistic for the lift is 1.8, and the team only cares whether the new page does better.

| Days | Degrees of Freedom | Test Statistic |
| --- | --- | --- |
| 21 | 20 | 1.8 |

**Task:** Find the right-tail probability for the lift.

**Solution:**

```excel
=T.DIST.RT(1.8, 20)
```

**Answer:** `0.043482`. A lift this large would show up by chance about 4.3 percent of the time.

### Problem 2: Negative Drift Check

A warehouse tracks weekly stock drift, and a control test gives a statistic of -0.6 with 9 degrees of freedom. The manager asks how likely a drift at least that high is.

**Task:** Find the right-tail probability at -0.6 with 9 degrees of freedom.

**Solution:**

```excel
=T.DIST.RT(-0.6, 9)
```

**Answer:** `0.718347`. A negative statistic leaves most of the distribution above it, so the chance is high.

## Use Cases

### One-Sided Growth Tests

**Scenario:** A subscription team wants to confirm that a new onboarding flow raises activation, not just changes it.

```excel
=T.DIST.RT(B2, C2)
```

**Why It Works:** `B2` holds the lift statistic and `C2` holds the degrees of freedom. The right tail matches a claim that the new flow is better, so use this layout only when that claim was set before the data was collected.

### Upper Tail Risk Limits

**Scenario:** A risk team wants an alert when the observed spike in late payments has a small chance of arising by chance.

```excel
=IF(T.DIST.RT(B2, C2) < 0.01, "Escalate", "Monitor")
```

**Why It Works:** Comparing the right-tail probability with a fixed limit gives a clear escalation rule. `B2` holds the statistic and `C2` holds the degrees of freedom.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `deg_freedom` is less than 1. | Check the sample size. |
| `#VALUE!` | An argument is text or blank. | Confirm both inputs are numbers. |
| Result above 0.5 | `x` is negative, so most of the distribution lies to the right. | This is expected. Check the sign of the statistic. |
| Result is half the expected value | The test was meant to be two-tailed. | Use T.DIST.2T for a two-sided question. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2010 and later, including Microsoft 365 | Accepts negative `x`. Returns `#NUM!` for `deg_freedom` less than 1. |
| Google Sheets | Available | Same arguments and order, with the same examples for positive and negative `x`. |

## Tips and Best Practices

- Decide on the tail before the test runs, because switching after seeing the data inflates the chance of a false result.
- Name the tail in the sheet label, such as "Right tail, one-sided", so readers do not confuse it with a two-tailed value.
- Keep the probability threshold in its own cell so the decision rule is easy to audit.
- Use T.INV for the matching critical value when a fixed cutoff is more useful than a probability.

## Related Functions

| Function | Relationship |
| --- | --- |
| [T.DIST](T.DIST.md) | Returns the left-tail cumulative value or the density. |
| [T.DIST.2T](T.DIST.2T.md) | Two-tailed probability, equal to twice this result for a positive `x`. |
| [T.INV](T.INV.md) | Returns the t-value for a left-tail probability, which helps set a cutoff. |
| [T.TEST](T.TEST.md) | Runs a complete t-test and returns its p-value. |
| [TDIST](TDIST.md) | Older function whose one-tailed form (`tails` set to 1) this function replaces. |

## Official Documentation

- [Microsoft Support: T.DIST.RT function](https://support.microsoft.com/en-us/excel/functions/t-dist-rt-function)
- [Google Docs Editors Help: T.DIST.RT](https://support.google.com/docs/answer/9369017)
