---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Overbooking Limits
  - Spare Parts Planning
  - Warranty Claim Reserves
related:
  - BINOM.DIST
  - BINOM.DIST.RANGE
  - BINOMDIST
  - CRITBINOM
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/binom-inv-function
  - https://support.google.com/docs/answer/3093623
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Binomial Inverse
  - Smallest Count For Probability
tags:
  - binomial
  - distributions
  - excel
  - probability
  - sheets
---

# BINOM.INV

## Description

**BINOM.INV** returns the smallest number of successes for which the cumulative binomial distribution reaches a target probability. Where BINOM.DIST answers "what is the chance of this count?", BINOM.INV answers "how many successes or fewer will I cover with this much confidence?"

Use it for planning. A warehouse can ask how many spare parts cover 90 percent of expected failures, and an airline can ask how many seats to sell so that the flight is full with at least 95 percent probability. The criterion argument must sit strictly between 0 and 1.

Microsoft's function is named BINOM.INV. Google Sheets documents the same calculation under the name CRITBINOM, with the same arguments in the same order, so the formula moves between the two programs with only a name change.

## Syntax

```excel
=BINOM.INV(trials, probability_s, alpha)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/BINOM.INV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `trials` | Yes | The number of Bernoulli trials. It must be 0 or greater. Non-integers are truncated, not rounded. |
| `probability_s` | Yes | The probability of success on each trial. It must be greater than 0 and less than 1. |
| `alpha` | Yes | The criterion value, the cumulative probability the result must reach. It must be greater than 0 and less than 1. |

### Return Value

The smallest whole number of successes whose cumulative probability is greater than or equal to `alpha`. The function returns `#VALUE!` when an argument is not numeric. It returns `#NUM!` when `trials` is negative, when `probability_s` is 0 or less, or 1 or more, or when `alpha` is 0 or less, or 1 or more.

## Examples

### Example 1: Coverage Count

```excel
=BINOM.INV(30, 0.25, 0.9)
```

**Result:** `11`

With 30 trials at a 25 percent chance each, 11 successes or fewer covers at least 90 percent of outcomes. Ten successes falls short of the target.

### Example 2: Reading Inputs From Cells

Row 2 holds 12 trials in `B2`, a probability of 0.4 in `C2` and an alpha of 0.5 in `D2`.

```excel
=BINOM.INV(B2, C2, D2)
```

**Result:** `5`

The median count for these inputs is 5. Half of all outcomes fall at or below this number.

### Example 3: Checking the Result

```excel
=BINOM.DIST(BINOM.INV(30, 0.25, 0.9), 30, 0.25, TRUE)
```

**Result:** `0.9493`

Feeding the result of Example 1 back into BINOM.DIST shows the coverage it actually achieves. The value sits just above the 0.9 target.

<!-- Image 2: Coverage Steps. See Images/Statistical/BINOM.INV.md -->

## Story Problems

### Problem 1: Spare Control Units

A factory uses 50 control units in a machine line. Each unit fails during a year with a 4 percent chance, independently. The maintenance team wants enough spares to cover at least 90 percent of the failures the year could bring.

| Input | Value |
| --- | --- |
| Units | 50 |
| Failure Chance | 0.04 |
| Coverage Target | 0.9 |

**Task:** Enter the inputs in `B1:B3` and find the smallest number of spares that covers the target.

**Solution:**

```excel
=BINOM.INV(B1, B2, B3)
```

**Answer:** `4` spares. Four spares cover about 95.1 percent of outcomes, while three cover about 86.1 percent, so three falls short.

### Problem 2: Ticket No-Shows

A theater sells 200 tickets for a show. Each ticket holder fails to attend with a 2 percent chance, independently of the others. The box office wants the smallest no-show count that it can stay at or below with 95 percent confidence.

| Input | Value |
| --- | --- |
| Tickets | 200 |
| No-Show Chance | 0.02 |
| Confidence | 0.95 |

**Task:** Find the smallest number of no-shows that the box office stays at or below with 95 percent confidence.

**Solution:**

```excel
=BINOM.INV(B1, B2, B3)
```

**Answer:** `7`. With 95 percent confidence, no more than 7 ticket holders stay away.

<!-- Image 3: Problem Two Threshold. See Images/Statistical/BINOM.INV.md -->

## Use Cases

### Overbooking Limits

**Scenario:** An airline sells seats on a flight with 180 tickets, each with a 5 percent chance of a no-show, and wants a no-show count it can plan around at 90 percent confidence.

```excel
=BINOM.INV(180, 0.05, 0.9)
```

**Why It Works:** The result is the no-show count the airline can cover at the chosen confidence. Test the confidence level before using the result to set a sales limit.

### Spare Parts Planning

**Scenario:** A repair depot keeps spares for 120 modules that each fail with a 3 percent chance per year and wants 99 percent coverage.

```excel
=BINOM.INV(120, 0.03, 0.99)
```

**Why It Works:** A high confidence level such as 0.99 raises the count, which trades storage cost for fewer stockouts.

### Warranty Claim Reserves

**Scenario:** A manufacturer sells 400 units with a 1 percent claim rate and sets aside cash for the claims it can cover at 95 percent confidence.

```excel
=BINOM.INV(400, 0.01, 0.95)
```

**Why It Works:** Reserving for the returned count keeps the reserve tied to a stated confidence level, which makes the finance review easier to follow.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `trials` is negative. | Enter a count of trials of 0 or more. |
| `#NUM!` | `probability_s` is 0 or less, or 1 or more. | Use a probability strictly between 0 and 1. |
| `#NUM!` | `alpha` is 0 or less, or 1 or more. | Enter a confidence level such as 0.9, not 90. |
| `#VALUE!` | An argument is text. | Convert the input cells to numbers. |
| Count is lower than expected | Trials were entered as a decimal, which is truncated. | Enter whole numbers of trials. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Named BINOM.INV. Returns the smallest success count that reaches alpha. |
| Google Sheets | Documented as CRITBINOM | Use CRITBINOM(num_trials, prob_success, target_prob). The arguments match BINOM.INV in order. |

## Tips and Best Practices

- Enter alpha as a decimal between 0 and 1, so 0.9 means 90 percent.
- Check the result with BINOM.DIST using TRUE, as in Example 3, to confirm the coverage it achieves.
- Read the result as a count to plan for, not as a forecast of the count you will see.
- Use BINOM.DIST to see individual probabilities and BINOM.INV when you start from a target coverage.
- Keep trials, probability and alpha in labeled cells so the planning assumptions are visible.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BINOM.DIST](BINOM.DIST.md) | Returns the probability of a count, the forward direction of this function. |
| [BINOM.DIST.RANGE](BINOM.DIST.RANGE.md) | Returns the probability for a range of counts in Excel. |
| [BINOMDIST](BINOMDIST.md) | The legacy form of BINOM.DIST with the same results. |
| [CRITBINOM](CRITBINOM.md) | The Sheets name for this calculation, with the same argument order. |

## Official Documentation

- [Microsoft Support: BINOM.INV function](https://support.microsoft.com/en-us/excel/functions/binom-inv-function)
- [Google Docs Editors Help: CRITBINOM](https://support.google.com/docs/answer/3093623)
