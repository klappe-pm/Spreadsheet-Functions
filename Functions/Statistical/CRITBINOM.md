---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Batch Defect Thresholds
  - Quality Sampling Plans
  - Survey Response Targets
related:
  - BINOM.DIST
  - BINOM.INV
  - BINOMDIST
  - NEGBINOM.DIST
  - POISSON.DIST
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/critbinom-function
  - https://support.google.com/docs/answer/3093623
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Binomial Criterion Value
  - Smallest Binomial Count
tags:
  - binomial
  - compatibility
  - excel
  - sheets
---

# CRITBINOM

## Description

**CRITBINOM** returns the smallest whole number of successes for which the cumulative binomial probability reaches a target. A binomial situation has a fixed number of independent trials, each with the same chance of success. Examples include the number of defective parts in a batch, the number of people who respond to an invitation, or the number of calls that connect.

CRITBINOM answers the question "What is the smallest count that gives at least this much confidence?" For a given number of trials and success probability, it adds the probabilities of 0, 1, 2 and so on until the running total reaches the target alpha. It returns the count at which that happens.

Microsoft lists CRITBINOM as a compatibility function. Its support page says it has been replaced by BINOM.INV, which may offer better accuracy and a clearer name. CRITBINOM remains available for backward compatibility but may not be available in future versions. For new work, use BINOM.INV, which takes the same three inputs.

Google Sheets provides CRITBINOM with the argument names `num_trials`, `prob_success` and `target_prob`.

## Syntax

```excel
=CRITBINOM(trials, probability_s, alpha)
```

<!-- Image 1: CRITBINOM Syntax Anatomy. See Images/Statistical/CRITBINOM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `trials` | Yes | The number of Bernoulli trials. A fractional value is truncated to a whole number. Google Sheets calls it `num_trials`. |
| `probability_s` | Yes | The probability of a success on each trial. It must be greater than 0 and less than 1. Google Sheets calls it `prob_success`. |
| `alpha` | Yes | The criterion value, the cumulative probability the result must reach. It must be greater than 0 and less than 1. Google Sheets calls it `target_prob`. |

### Return Value

A whole number: the smallest count of successes for which the cumulative binomial distribution is greater than or equal to `alpha`. It returns `#VALUE!` when any argument is not numeric. It returns `#NUM!` when `trials` is below 0, when `probability_s` is 0 or 1 or outside that range, or when `alpha` is 0 or 1 or outside that range.

## Examples

Each example uses a fixed number of trials and a success probability. The results are whole numbers of successes.

### Example 1: Ten Trials at 30 Percent

```excel
=CRITBINOM(10, 0.3, 0.9)
```

**Result:** `5`

The cumulative probability of at most 4 successes is about 0.850, which is below 0.9. At most 5 successes has a cumulative probability of about 0.953, which reaches 0.9, so the result is 5.

### Example 2: Values From Cells

Cell `A2` holds `12` trials, cell `A3` holds `0.2` and cell `A4` holds `0.8`.

```excel
=CRITBINOM(A2, A3, A4)
```

**Result:** `4`

Changing any of the three cells recalculates the count, so the same formula works for each new batch or survey.

### Example 3: Fractional Trials Are Truncated

```excel
=CRITBINOM(10.9, 0.3, 0.9)
```

**Result:** `5`

Microsoft truncates the number of trials to a whole number, so 10.9 is treated as 10. The result is the same as in Example 1.

### Example 4: Stricter Target

```excel
=CRITBINOM(20, 0.05, 0.9)
```

**Result:** `2`

With 20 trials and a 5 percent chance on each, at most 1 success has a cumulative probability of about 0.736, which is too low. At most 2 successes reaches about 0.925, so the result is 2.

### Example 5: Invalid Criterion Value

```excel
=CRITBINOM(10, 0.3, 1)
```

**Result:** `#NUM!`

The criterion value must be greater than 0 and less than 1. Microsoft returns `#NUM!` for any value outside that range, so a target of 1 is rejected even though it sounds like certainty.

<!-- Image 2: Cumulative Totals for CRITBINOM. See Images/Statistical/CRITBINOM.md -->

## Story Problems

### Problem 1: Survey Responses to Reach 80 Percent Confidence

A research team sends 25 survey invitations. Each invitation has a 40 percent chance of a response, and the team wants to know how many responses it can count on with at least 80 percent confidence.

| Input | Value |
| --- | --- |
| Invitations sent | 25 |
| Response probability | 0.4 |
| Target confidence | 0.8 |

**Task:** Find the smallest number of responses that the team can expect with at least 80 percent confidence.

**Solution:**

```excel
=CRITBINOM(25, 0.4, 0.8)
```

**Answer:** `12`. The cumulative probability of 11 or fewer responses is about 0.732, which is below 0.8. Twelve or fewer responses reaches about 0.846, so 12 is the smallest count that meets the target.

### Problem 2: Failed Deliveries Under a Service Limit

A courier makes 15 deliveries, and each one has a 10 percent chance of failing. Operations wants the smallest number of failures that is expected with 95 percent confidence, so it can set a service threshold.

| Input | Value |
| --- | --- |
| Deliveries | 15 |
| Failure probability | 0.1 |
| Confidence | 0.95 |

**Task:** Find the smallest number of failed deliveries that reaches 95 percent cumulative probability.

**Solution:**

```excel
=CRITBINOM(15, 0.1, 0.95)
```

**Answer:** `4`. Up to 3 failures has a cumulative probability of about 0.944, which is just below 0.95. Up to 4 failures reaches about 0.987, so the threshold is 4.

## Use Cases

### Batch Defect Thresholds

**Scenario:** A plant accepts a batch of 20 parts with a 5 percent defect rate and wants the number of defects that the batch will stay at or under with 90 percent confidence.

```excel
=CRITBINOM(Batch_Size, Defect_Rate, 0.9)
```

**Why It Works:** The named ranges hold the batch size and defect rate, so the threshold updates for each new batch. The result is the count that a batch reaches with the stated confidence.

### Quality Sampling Plans

**Scenario:** A supplier inspects a sample of parts and needs the maximum number of defects allowed to keep the chance of accepting a bad lot below a set level.

```excel
=CRITBINOM(Sample_Size, Bad_Rate, 1 - Risk_Level)
```

**Why It Works:** Subtracting the risk level from 1 turns the risk into the cumulative probability the criterion requires. Check the plan against the supplier's agreed standards before using it in a contract.

### Survey Response Targets

**Scenario:** A marketing team wants to know how many responses to plan for when it sends a fixed number of invitations.

```excel
=CRITBINOM(Invitations, Response_Rate, 0.8)
```

**Why It Works:** The formula returns a responses count that the team can expect with 80 percent confidence, which is safer for planning than the average response.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The criterion value or the probability is 0 or 1, or outside the range. | Enter a probability and a criterion above 0 and below 1. |
| `#NUM!` | The number of trials is negative. | Use zero or a positive number of trials. |
| `#VALUE!` | One argument is text or a blank cell. | Check that each argument is a number, such as `0.3` rather than `"30%"`. |
| Count is lower than expected | The criterion value is low, so the smallest count that reaches it is small. | Increase the criterion value to set a stricter threshold. |
| `#NUM!` | A percentage was typed as a whole number, such as `30` instead of `0.3`. | Enter probabilities as decimals between 0 and 1. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Compatibility function | Replaced by BINOM.INV. Kept for backward compatibility, and Microsoft notes it may not be available in future versions. |
| Google Sheets | Available | Arguments are `num_trials`, `prob_success` and `target_prob`. The help page shows the syntax and sample formulas without sample results. |

## Tips and Best Practices

- Use BINOM.INV in new workbooks, and keep CRITBINOM only where an older file needs it.
- Enter probabilities as decimals, and check that each value falls between 0 and 1.
- Use a higher criterion value to set a stricter threshold, which raises the count.
- Compare the result with BINOM.DIST to see the cumulative probability behind the count.
- Store trials, probability and criterion in cells, so the threshold can be reviewed and changed without editing the formula.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BINOM.INV](BINOM.INV.md) | The current replacement, with the same three inputs. |
| [BINOM.DIST](BINOM.DIST.md) | Returns the probability or cumulative probability for a given count. |
| [BINOMDIST](BINOMDIST.md) | The older binomial distribution function that BINOM.DIST replaces. |
| [NEGBINOM.DIST](NEGBINOM.DIST.md) | Models the number of failures before a set number of successes. |
| [POISSON.DIST](POISSON.DIST.md) | Models counts of rare events when the number of trials is large. |

## Official Documentation

- [Microsoft Support: CRITBINOM function](https://support.microsoft.com/en-us/excel/functions/critbinom-function)
- [Google Docs Editors Help: CRITBINOM](https://support.google.com/docs/answer/3093623)
