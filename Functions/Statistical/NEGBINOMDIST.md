---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Quality Inspection Counts
  - Sales Call Outcomes
  - Trial Offer Conversions
related:
  - BINOM.DIST
  - HYPGEOM.DIST
  - NEGBINOM.DIST
  - POISSON.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/negbinomdist-function
  - https://support.google.com/docs/answer/3094031
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Negative Binomial Probability
tags:
  - compatibility
  - discrete
  - distribution
  - excel
  - probability
  - sheets
---

# NEGBINOMDIST

## Description

**NEGBINOMDIST** returns the probability of seeing a given number of failures before a set number of successes, when every trial has the same chance of success and the trials are independent. It answers the same question as the binomial distribution family, but it fixes the number of successes and counts the failures.

Microsoft has replaced this function with NEGBINOM.DIST. The newer function gives the same exact probability and adds a cumulative option in Excel. Microsoft keeps NEGBINOMDIST for backward compatibility and warns that it may not be available in future versions of Excel, so use NEGBINOM.DIST for new work and keep NEGBINOMDIST only in workbooks that already rely on it.

Google Sheets documents this calculation under the NEGBINOMDIST name and includes a cumulative argument, so the arguments differ between the two platforms. The Platform Differences section shows the details.

## Syntax

```excel
=NEGBINOMDIST(number_f, number_s, probability_s)
```

<!-- Image 1: Failures, Successes and Probability Inputs. See Images/Statistical/NEGBINOMDIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number_f` | Yes | The number of failures. Decimals are truncated to whole numbers. A negative value returns `#NUM!`. |
| `number_s` | Yes | The number of successes the process must reach. Decimals are truncated to whole numbers. A value below 1 returns `#NUM!`. |
| `probability_s` | Yes | The chance of success on each trial, as a decimal from 0 to 1. A value below 0 or above 1 returns `#NUM!`. |

### Return Value

The probability of exactly `number_f` failures occurring before the `number_s`th success. The function returns `#VALUE!` when an argument is not a number and `#NUM!` when an argument falls outside the limits in the table above.

## Examples

The examples use 6 failures in `A2`, 4 successes in `B1` and a success probability of 0.3 in `B2`.

### Example 1: Exact Probability

```excel
=NEGBINOMDIST(6, 4, 0.3)
```

**Result:** `0.080048`

The probability of exactly six failures before the fourth success when each trial succeeds 30 percent of the time.

### Example 2: Matching NEGBINOM.DIST

```excel
=NEGBINOM.DIST(6, 4, 0.3, FALSE)
```

**Result:** `0.080048`, the same as Example 1

Both functions return the same exact probability when cumulative is FALSE. Use NEGBINOM.DIST when the workbook needs the cumulative option.

### Example 3: Probability Table Across Failure Counts

Place failure counts in `A2:A6`, keep the success count in `B1` and the probability in `B2`, then fill this formula down from `C2`.

```excel
=NEGBINOMDIST(A2, $B$1, $B$2)
```

**Result:** `0.02268` in `C3`, where `A3` holds 1 failure

The absolute references lock the success count and probability while each row tests a different failure count.

### Example 4: Rounded Output

```excel
=ROUND(NEGBINOMDIST(6, 4, 0.3), 4)
```

**Result:** `0.08`

Rounding to four decimal places gives `0.0800`, which displays as `0.08` when the cell uses a general number format.

### Example 5: Cumulative Chance Built From Exact Values

Excel's NEGBINOMDIST has no cumulative option, so add the exact probabilities for the counts you need.

```excel
=NEGBINOMDIST(0, 4, 0.3) + NEGBINOMDIST(1, 4, 0.3) + NEGBINOMDIST(2, 4, 0.3)
```

**Result:** `0.07047`

The result is the chance of at most two failures before the fourth success. With NEGBINOM.DIST the same answer comes from a single call with TRUE as the last argument.

<!-- Image 2: Summing Exact Probabilities. See Images/Statistical/NEGBINOMDIST.md -->

## Story Problems

### Problem 1: Rejected Parts Before Four Good Parts

A machine shop passes 70 percent of parts from a new fixture. The inspector wants the chance that exactly two rejected parts appear before the fourth good part.

| Input | Value |
| --- | --- |
| Rejected parts (failures) | 2 |
| Good parts needed (successes) | 4 |
| Chance a part passes | 0.7 |

**Task:** Enter the inputs in `E2:E4`, then calculate the probability of exactly two rejects before the fourth pass.

**Solution:**

```excel
=NEGBINOMDIST(E2, E3, E4)
```

**Answer:** `0.21609`, or about 21.6 percent.

### Problem 2: Trial Offer Sign-Ups

A software company needs three paying customers from a trial program. About 20 percent of trial users convert. The marketing lead wants the chance that at most one trial user fails to convert before the third conversion.

| Input | Value |
| --- | --- |
| Non-converting users allowed (failures) | 1 |
| Conversions needed (successes) | 3 |
| Conversion rate | 0.2 |

**Task:** Enter the inputs in `E2:E4`, then add the exact probabilities for zero and one failures.

**Solution:**

```excel
=NEGBINOMDIST(0, E3, E4) + NEGBINOMDIST(1, E3, E4)
```

**Answer:** `0.0272`, or about 2.7 percent. Reaching three conversions with at most one non-converting user is unlikely at a 20 percent conversion rate.

## Use Cases

### Legacy Quality Workbook

**Scenario:** A plant maintains a workbook built years ago that already uses NEGBINOMDIST in several reports. The team wants the reports to keep working while new sheets use the current function.

```excel
=NEGBINOMDIST(C2, $F$2, $F$3)
```

**Why It Works:** The formula keeps its original form, so the existing reports do not change. New analysis can use NEGBINOM.DIST with the same three inputs plus a FALSE or TRUE for the last argument.

### Trial Conversion Tracking

**Scenario:** A growth team tracks how many non-converting trial users appear before a target number of paying customers.

```excel
=NEGBINOMDIST(B5, $F$2, $F$3)
```

**Why It Works:** `B5` holds the observed number of non-converting users, while `F2` and `F3` hold the target and the conversion rate. The result gives the exact chance of that specific count.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `number_f` is negative, `number_s` is below 1, or `probability_s` is outside 0 to 1. | Correct the input cell. Enter probabilities as decimals. |
| `#VALUE!` | An argument holds text or another nonnumeric value. | Re-enter the value as a number. |
| Formula error in Excel | A fourth argument such as `cumulative` is included. | Remove the fourth argument, or switch to NEGBINOM.DIST. |
| Result looks like a cumulative total | The exact probabilities were added but the wrong counts were included. | List every failure count from 0 up to the threshold, with no gaps. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available, listed in the compatibility group | Three arguments and no cumulative option. Microsoft recommends NEGBINOM.DIST. |
| Google Sheets | Available | Four arguments. The last argument, `cumulative`, returns the cumulative distribution when TRUE and the exact probability when FALSE. |

## Tips and Best Practices

- Use NEGBINOM.DIST in new workbooks, because it adds the cumulative option and Microsoft recommends it.
- Keep NEGBINOMDIST in older files only when changing the formula would change the reports.
- Enter probabilities as decimals. A value of 30 is outside the allowed range and returns `#NUM!`.
- Build cumulative totals from exact values only when the list of counts is short and complete.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NEGBINOM.DIST](NEGBINOM.DIST.md) | The current replacement, with a cumulative option in Excel. |
| [BINOM.DIST](BINOM.DIST.md) | Fixes the number of trials and counts successes. |
| [HYPGEOM.DIST](HYPGEOM.DIST.md) | Counts successes when items are drawn without replacement. |
| [POISSON.DIST](POISSON.DIST.md) | Counts events in a fixed interval rather than trials until a target count. |

## Official Documentation

- [Microsoft Support: NEGBINOMDIST function](https://support.microsoft.com/en-us/excel/functions/negbinomdist-function)
- [Google Docs Editors Help: NEGBINOMDIST](https://support.google.com/docs/answer/3094031)
