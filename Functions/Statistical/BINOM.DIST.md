---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Quality Sampling Plans
  - Sales Conversion Odds
  - Survey Response Counts
related:
  - BINOM.DIST.RANGE
  - BINOM.INV
  - BINOMDIST
  - COMBIN
  - CRITBINOM
  - NEGBINOM.DIST
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/binom-dist-function
  - https://support.google.com/docs/answer/3093987
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Binomial Probability
  - Binomial Distribution
tags:
  - binomial
  - distributions
  - excel
  - probability
  - sheets
---

# BINOM.DIST

## Description

**BINOM.DIST** returns the probability of a given number of successes in a fixed number of independent trials, where each trial has the same chance of success. Use it when every trial is a yes or no outcome: a product passes or fails inspection, a customer opens an email or does not, a seed germinates or does not.

The **cumulative** argument selects the form. FALSE returns the probability of exactly that many successes. TRUE returns the probability of that many successes or fewer. Most questions about "at least" or "between" are built from the cumulative form by subtracting or taking the complement.

BINOM.DIST replaced BINOMDIST in Excel. Both return the same values with the same arguments, but Microsoft recommends BINOM.DIST for new work and warns that BINOMDIST may not be available in future versions. For a range of successes, BINOM.DIST.RANGE is simpler than subtracting two cumulative results.

## Syntax

```excel
=BINOM.DIST(number_s, trials, probability_s, cumulative)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/BINOM.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number_s` | Yes | The number of successes in the trials. It must be from 0 to `trials`. Non-integers are truncated. |
| `trials` | Yes | The number of independent trials. Non-integers are truncated. |
| `probability_s` | Yes | The probability of success on each trial. It must be from 0 to 1. |
| `cumulative` | Yes | TRUE returns the probability of `number_s` or fewer successes. FALSE returns the probability of exactly `number_s` successes. |

### Return Value

A probability from 0 to 1. The function returns `#VALUE!` when an argument is not numeric. It returns `#NUM!` when `number_s` is below 0 or above `trials`, or when `probability_s` is below 0 or above 1.

## Examples

### Example 1: Exactly Three Defects

```excel
=BINOM.DIST(3, 10, 0.1, FALSE)
```

**Result:** `0.0574`

A batch of 10 items with a 10 percent defect rate has about a 5.7 percent chance of containing exactly three defects.

### Example 2: Three Defects or Fewer

```excel
=BINOM.DIST(3, 10, 0.1, TRUE)
```

**Result:** `0.9872`

The cumulative form adds the probabilities for 0, 1, 2 and 3 defects. Changing FALSE to TRUE is the only difference from Example 1.

<!-- Image 2: Exact Versus Cumulative Results. See Images/Statistical/BINOM.DIST.md -->

### Example 3: Reading Inputs From Cells

Row 2 holds 7 successes in `B2`, 12 trials in `B3` and a success probability of 0.4 in `B4`.

```excel
=BINOM.DIST(B2, B3, B4, TRUE)
```

**Result:** `0.9427`

Keeping the counts and probability in cells lets a report recalculate when the sample size changes.

### Example 4: Probability Between Two Counts

```excel
=BINOM.DIST(4, 10, 0.1, TRUE) - BINOM.DIST(1, 10, 0.1, TRUE)
```

**Result:** `0.2623`

Subtracting the cumulative probability at 1 from the cumulative probability at 4 leaves the probability of 2, 3 or 4 successes.

## Story Problems

### Problem 1: Newsletter Open Count

A publisher sends a newsletter to 20 subscribers. Past issues show that each subscriber opens a given issue with a 30 percent chance, independently of the others. The editor wants the chance that exactly 5 subscribers open the next issue.

| Input | Value |
| --- | --- |
| Subscribers | 20 |
| Open Chance | 0.3 |
| Opens | 5 |

**Task:** Enter the inputs in `B1:B3` and find the probability of exactly 5 opens.

**Solution:**

```excel
=BINOM.DIST(B3, B1, B2, FALSE)
```

**Answer:** `0.1789`. Exactly five opens happens in about 17.9 percent of issues.

### Problem 2: Seedling Germination Target

A nursery plants 8 seeds. Each seed germinates with a 75 percent chance. The nursery needs at least 6 seedlings to fill a tray.

| Input | Value |
| --- | --- |
| Seeds | 8 |
| Germination Chance | 0.75 |
| Minimum Germinated | 6 |

**Task:** Find the probability that 6 or more seeds germinate, using the inputs in `B1:B3`.

**Solution:**

```excel
=1 - BINOM.DIST(B3 - 1, B1, B2, TRUE)
```

**Answer:** `0.6785`. The tray fills in about two of every three plantings. Subtracting the cumulative probability from 1 gives "at least," because "at least 6" is the complement of "5 or fewer."

<!-- Image 3: Seedling Germination Tail. See Images/Statistical/BINOM.DIST.md -->

## Use Cases

### Quality Sampling Plans

**Scenario:** A quality team pulls 25 parts from each lot and needs the chance of seeing at most one defect when the true defect rate is 2 percent.

```excel
=BINOM.DIST(1, 25, 0.02, TRUE)
```

**Why It Works:** The cumulative form answers an "at most" question in one step. Compare the result with the acceptance rule in the sampling plan before using it.

### Sales Conversion Odds

**Scenario:** A sales manager wants the chance that a rep closes exactly 4 of 15 calls when each call has a 20 percent close rate.

```excel
=BINOM.DIST(4, 15, 0.2, FALSE)
```

**Why It Works:** Each call is treated as an independent trial. The result is most useful for comparing a rep's actual results with the expected spread rather than for judging a single week.

### Survey Response Counts

**Scenario:** A research team expects 40 percent of invitations to produce a response and wants the chance of getting at least 30 responses from 70 invitations.

```excel
=1 - BINOM.DIST(29, 70, 0.4, TRUE)
```

**Why It Works:** The complement of "29 or fewer" is "30 or more." Keep the invitation count in a cell so the target can be updated when the list changes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `number_s` is below 0 or above `trials`. | Keep the success count between 0 and the number of trials. |
| `#NUM!` | `probability_s` is below 0 or above 1. | Enter a probability from 0 to 1, not a percentage such as 30. |
| `#VALUE!` | An argument is text. | Remove text from the input cells or convert them to numbers. |
| Result looks too large | `cumulative` is TRUE when an exact count was wanted. | Use FALSE for the probability of exactly `number_s`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Replaces BINOMDIST. Microsoft recommends BINOM.DIST for new work. |
| Google Sheets | Available | Google's help page documents the calculation as BINOMDIST, with arguments num_successes, num_trials, prob_success and cumulative. Its cumulative argument defaults to FALSE. |

## Tips and Best Practices

- Enter the probability as a decimal from 0 to 1. A value of 30 is rejected with `#NUM!`.
- Use TRUE for "at most" questions and 1 minus the TRUE result for "more than" questions.
- Use BINOM.DIST.RANGE when you need a range of successes in Excel, because it avoids subtracting two results.
- Non-integer counts are truncated, so round the inputs yourself before the formula if the rounding rule matters.
- Use BINOM.INV when you know the probability you need and want the count that produces it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BINOM.DIST.RANGE](BINOM.DIST.RANGE.md) | Returns the probability for a range of successes in one formula. Excel only. |
| [BINOM.INV](BINOM.INV.md) | Finds the smallest success count that reaches a target cumulative probability. |
| [BINOMDIST](BINOMDIST.md) | The legacy version of this function with the same results. |
| [COMBIN](../Math%20%26%20Trig/COMBIN.md) | Calculates the number of ways to choose successes, the core of the probability formula. |
| [CRITBINOM](CRITBINOM.md) | The Sheets name for the inverse of the binomial distribution. |
| [NEGBINOM.DIST](NEGBINOM.DIST.md) | Models the number of failures before a set number of successes. |

## Official Documentation

- [Microsoft Support: BINOM.DIST function](https://support.microsoft.com/en-us/excel/functions/binom-dist-function)
- [Google Docs Editors Help: BINOMDIST](https://support.google.com/docs/answer/3093987)
