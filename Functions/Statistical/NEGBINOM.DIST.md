---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Quality Inspection Counts
  - Repeated Trial Planning
  - Sales Call Outcomes
related:
  - BINOM.DIST
  - HYPGEOM.DIST
  - NEGBINOMDIST
  - POISSON.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/negbinom-dist-function
  - https://support.google.com/docs/answer/3094031
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Negative Binomial Distribution
tags:
  - discrete
  - distribution
  - excel
  - probability
  - sheets
---

# NEGBINOM.DIST

## Description

**NEGBINOM.DIST** returns the probability of seeing a given number of failures before a set number of successes, when every trial has the same chance of success and the trials are independent. Use it when you keep trying until you reach a target count of successes and want to know how many misses to expect along the way, such as the number of unsuccessful sales calls before the fifth sale.

The function has two modes. When cumulative is FALSE it returns the chance of exactly that many failures. When cumulative is TRUE it returns the chance of that many failures or fewer, which is the usual form for planning thresholds.

The binomial distribution works the other way around. BINOM.DIST fixes the number of trials and counts the successes, while NEGBINOM.DIST fixes the number of successes and counts the failures. Choose the one that matches how the process stops.

NEGBINOM.DIST replaces the older NEGBINOMDIST function. In Excel it adds the cumulative argument that NEGBINOMDIST does not have.

## Syntax

```excel
=NEGBINOM.DIST(number_f, number_s, probability_s, cumulative)
```

<!-- Image 1: Failures, Successes and Probability Inputs. See Images/Statistical/NEGBINOM.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number_f` | Yes | The number of failures. Decimals are truncated to whole numbers. A negative value returns `#NUM!`. |
| `number_s` | Yes | The number of successes the process must reach. Decimals are truncated to whole numbers. A value below 1 returns `#NUM!`. |
| `probability_s` | Yes | The chance of success on each trial, entered as a decimal from 0 to 1. A value below 0 or above 1 returns `#NUM!`. |
| `cumulative` | Yes | TRUE returns the chance of up to `number_f` failures. FALSE returns the chance of exactly `number_f` failures. |

### Return Value

A probability between 0 and 1. The function returns `#VALUE!` when an argument is not a number and `#NUM!` when an argument falls outside the limits in the table above.

## Examples

The examples use 4 failures in `B2`, 3 successes in `B3` and a success probability of 0.4 in `B4`.

### Example 1: Exactly Four Failures

```excel
=NEGBINOM.DIST(4, 3, 0.4, FALSE)
```

**Result:** `0.124416`

The third success must be the last trial, so the first six trials hold four failures and two successes. Those two successes can fall in any of 15 positions, and each arrangement has a probability of 0.4 cubed times 0.6 to the fourth power.

### Example 2: Four Failures or Fewer

```excel
=NEGBINOM.DIST(4, 3, 0.4, TRUE)
```

**Result:** `0.580096`

The function adds the exact probabilities for 0, 1, 2, 3 and 4 failures. The chance of finishing with at most four failures is a little better than even.

### Example 3: Probability Table Across Failure Counts

Place failure counts 0 to 5 in `A2:A7`, keep the success count in `B1` and the probability in `B2`, then fill this formula down from `C2`.

```excel
=NEGBINOM.DIST(A2, $B$1, $B$2, FALSE)
```

**Result:** `0.13824` in `C4`, where `A4` holds 2 failures

The absolute references keep the success count and probability fixed while each row tests a different failure count.

### Example 4: Rounded Output for a Report

```excel
=ROUND(NEGBINOM.DIST(4, 3, 0.4, FALSE), 4)
```

**Result:** `0.1244`

Rounding keeps a dashboard table readable. The underlying value still drives any further calculation that refers to the unrounded cell.

### Example 5: Chance of More Than Four Failures

```excel
=1-NEGBINOM.DIST(4, 3, 0.4, TRUE)
```

**Result:** `0.419904`

Subtracting the cumulative chance from 1 gives the chance that the run needs at least five failures before the third success.

<!-- Image 2: Trial Sequence for the Third Success. See Images/Statistical/NEGBINOM.DIST.md -->

## Story Problems

### Problem 1: Sales Calls Until Five Deals

A sales team closes about one call in four. The manager wants to know how likely it is that the team makes exactly ten unsuccessful calls before it closes its fifth deal.

| Input | Value |
| --- | --- |
| Unsuccessful calls (failures) | 10 |
| Deals needed (successes) | 5 |
| Chance a call closes | 0.25 |

**Task:** Enter the three inputs in `E2:E4`, then calculate the chance of exactly ten failed calls before the fifth deal.

**Solution:**

```excel
=NEGBINOM.DIST(E2, E3, E4, FALSE)
```

**Answer:** `0.05505`, or about 5.5 percent. The team has roughly a one in eighteen chance of a run this long.

### Problem 2: Survey Responses Before Three Satisfied Customers

A support team needs three satisfied responses from customers. Each response has a 60 percent chance of being satisfied. The team wants the chance that no more than two unsatisfied responses arrive before the third satisfied one.

| Input | Value |
| --- | --- |
| Unsatisfied responses allowed (failures) | 2 |
| Satisfied responses needed (successes) | 3 |
| Chance a response is satisfied | 0.6 |

**Task:** Enter the inputs in `E2:E4`, then calculate the cumulative chance of at most two unsatisfied responses.

**Solution:**

```excel
=NEGBINOM.DIST(E2, E3, E4, TRUE)
```

**Answer:** `0.68256`, or about 68 percent. The cumulative setting adds the chances for zero, one and two unsatisfied responses.

## Use Cases

### Sales Pipeline Planning

**Scenario:** A regional manager needs five new contracts this quarter. The team has a close rate of 25 percent and wants to know the chance of closing the five contracts within 12 failed calls.

```excel
=NEGBINOM.DIST(B2, B3, B4, TRUE)
```

**Why It Works:** `B2` holds the call limit of 12, `B3` holds 5 contracts and `B4` holds 0.25. Changing any input updates the planning figure without rewriting the formula.

### Survey Fielding Risk

**Scenario:** A research team needs four completed interviews. Each call reaches a willing respondent with a 40 percent chance. The team wants the chance that it needs more than seven unanswered calls.

```excel
=1-NEGBINOM.DIST(7, 4, 0.4, TRUE)
```

**Why It Works:** Subtracting the cumulative chance from 1 turns a "seven or fewer" result into a "more than seven" risk. Teams can use the result to decide whether to add more calling shifts.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `number_f` is negative, `number_s` is below 1, or `probability_s` is outside 0 to 1. | Correct the input cell. Enter probabilities as decimals, so 25 percent is 0.25. |
| `#VALUE!` | An argument holds text or another nonnumeric value. | Re-enter the value as a number or convert it with VALUE. |
| Result too small | `cumulative` is TRUE when the exact count is needed. | Set `cumulative` to FALSE for the chance of exactly that many failures. |
| Result too large | `cumulative` is FALSE when a threshold is needed. | Set `cumulative` to TRUE for the chance of that many failures or fewer. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Excel for the web | Four arguments, with `cumulative` as the last argument. |
| Google Sheets | Documented as NEGBINOMDIST | The Google help page lists the calculation under NEGBINOMDIST with four arguments, including a cumulative argument. The page does not show the NEGBINOM.DIST name, so test the name in your sheet before you rely on it. |

## Tips and Best Practices

- Put the failures, successes and probability in labeled cells so the formula reads clearly to other users.
- Enter probabilities as decimals. A value of 25 is outside the allowed range and returns `#NUM!`.
- Use BINOM.DIST instead when the number of trials is fixed in advance.
- Use TRUE for planning thresholds and FALSE for the chance of one specific outcome.
- Check that each trial is independent. A changing success rate makes the result unreliable.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BINOM.DIST](BINOM.DIST.md) | Fixes the number of trials and counts the successes. |
| [HYPGEOM.DIST](HYPGEOM.DIST.md) | Counts successes when items are drawn without replacement. |
| [NEGBINOMDIST](NEGBINOMDIST.md) | The older form of this calculation, kept for compatibility. |
| [POISSON.DIST](POISSON.DIST.md) | Counts events in a fixed interval rather than trials until a target count. |

## Official Documentation

- [Microsoft Support: NEGBINOM.DIST function](https://support.microsoft.com/en-us/excel/functions/negbinom-dist-function)
- [Google Docs Editors Help: NEGBINOMDIST](https://support.google.com/docs/answer/3094031)
