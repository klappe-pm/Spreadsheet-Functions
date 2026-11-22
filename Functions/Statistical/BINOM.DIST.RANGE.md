---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Acceptance Testing Ranges
  - Customer Call Outcomes
  - Shipment Timeliness
related:
  - BINOM.DIST
  - BINOM.INV
  - COMBIN
  - CRITBINOM
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/binom-dist-range-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Binomial Range Probability
tags:
  - binomial
  - distributions
  - excel
  - probability
---

# BINOM.DIST.RANGE

## Description

**BINOM.DIST.RANGE** returns the probability of a trial result using a binomial distribution. It works with the same kind of problem as BINOM.DIST: a fixed number of independent trials, each with the same chance of success. The difference is that it can return the probability of one exact count or of every count from a lower value to an upper value, in one formula.

Leave out the last argument to get the probability of exactly one count. Supply it to get the probability that the number of successes falls between the two counts, inclusive. This is the cleanest way to answer "between 6 and 9 successes" in Excel, because you do not need to subtract two cumulative results.

BINOM.DIST.RANGE is available in Excel only. Google Sheets does not offer it, so workbooks that use it will show errors in Sheets. Where a file must work in both programs, build the range from two cumulative calls as shown in Platform Differences.

## Syntax

```excel
=BINOM.DIST.RANGE(trials, probability_s, number_s, [number_s2])
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/BINOM.DIST.RANGE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `trials` | Yes | The number of independent trials. It must be 0 or greater. Non-integers are truncated. |
| `probability_s` | Yes | The probability of success on each trial. It must be from 0 to 1. |
| `number_s` | Yes | The number of successes. It must be from 0 to `trials`. When `number_s2` is omitted, this is the exact count. |
| `number_s2` | No | The upper end of the range. It must be at least `number_s` and no greater than `trials`. When provided, the function returns the probability of every count from `number_s` to `number_s2`. |

### Return Value

A probability from 0 to 1. The function returns `#NUM!` when an argument falls outside its limits, and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: One Exact Count

```excel
=BINOM.DIST.RANGE(40, 0.2, 8)
```

**Result:** `0.1560`

With 40 trials at a 20 percent chance each, the probability of exactly 8 successes is about 15.6 percent. No upper argument is supplied, so the function returns a single count.

### Example 2: A Range of Counts

```excel
=BINOM.DIST.RANGE(40, 0.2, 6, 9)
```

**Result:** `0.5704`

The probability of 6, 7, 8 or 9 successes is about 57 percent. The four individual probabilities are added inside the function.

<!-- Image 2: Range Shading Across Counts. See Images/Statistical/BINOM.DIST.RANGE.md -->

### Example 3: Reading Inputs From Cells

Row 2 holds 40 trials in `B2`, a probability of 0.2 in `C2`, a lower count of 6 in `D2` and an upper count of 9 in `E2`.

```excel
=BINOM.DIST.RANGE(B2, C2, D2, E2)
```

**Result:** `0.5704`

Storing the counts in cells lets a planner test a different target range without editing the formula.

### Example 4: Equivalent Cumulative Calculation

```excel
=BINOM.DIST(9, 40, 0.2, TRUE) - BINOM.DIST(5, 40, 0.2, TRUE)
```

**Result:** `0.5704`

This is the same range written with two cumulative calls. It matches Example 2 and shows why the range function is shorter.

## Story Problems

### Problem 1: Reply Count Target

A sales team emails 25 prospects. Each prospect replies with a 60 percent chance, independently. The team counts a campaign as a success when between 15 and 18 prospects reply.

| Input | Value |
| --- | --- |
| Emails Sent | 25 |
| Reply Chance | 0.6 |
| Lowest Replies | 15 |
| Highest Replies | 18 |

**Task:** Enter the inputs in `B1:B4` and find the probability that the number of replies falls between 15 and 18.

**Solution:**

```excel
=BINOM.DIST.RANGE(B1, B2, B3, B4)
```

**Answer:** `0.5122`. A campaign meets the target about 51 percent of the time.

### Problem 2: On-Time Shipments

A warehouse ships 30 orders a day. Each order arrives on time with a 90 percent chance. The operations manager wants the probability that at least 27 orders are on time, which is every count from 27 to 30.

| Input | Value |
| --- | --- |
| Orders | 30 |
| On-Time Chance | 0.9 |
| Lowest On Time | 27 |
| Highest On Time | 30 |

**Task:** Find the probability that 27 to 30 orders arrive on time, using the inputs in `B1:B4`.

**Solution:**

```excel
=BINOM.DIST.RANGE(B1, B2, B3, B4)
```

**Answer:** `0.6474`. The target of at least 27 on-time orders is met on about 65 percent of days.

## Use Cases

### Acceptance Testing Ranges

**Scenario:** A test lab accepts a batch when it finds between 0 and 2 defective units out of 50, with a 2 percent defect rate.

```excel
=BINOM.DIST.RANGE(50, 0.02, 0, 2)
```

**Why It Works:** The lower bound of 0 includes the case of no defects. Compare the result with the acceptance rule used by the lab before relying on it.

### Customer Call Outcomes

**Scenario:** A support center expects a 25 percent resolution rate on first contact and wants the chance that 5 to 8 of 30 calls are resolved.

```excel
=BINOM.DIST.RANGE(30, 0.25, 5, 8)
```

**Why It Works:** One formula covers the whole band, so the staffing report can show a range rather than a single count.

### Shipment Timeliness

**Scenario:** A carrier reports on-time delivery for 14 stops on a route with an 85 percent on-time rate and asks for the chance that 10 to 12 stops arrive on time.

```excel
=BINOM.DIST.RANGE(14, 0.85, 10, 12)
```

**Why It Works:** The upper count of 12 keeps the band below the total of 14, so the range stays valid.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `number_s2` is smaller than `number_s`. | Put the lower count first. |
| `#NUM!` | `number_s2` is greater than `trials`. | Keep the upper count at or below the number of trials. |
| `#NUM!` | `probability_s` is outside 0 to 1. | Enter a decimal probability, not a percentage. |
| `#VALUE!` | An argument is text. | Convert the input cells to numbers. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns the probability for one count or for a range of counts. |
| Google Sheets | Not available | Use two cumulative calls instead, such as `=BINOMDIST(9, 40, 0.2, TRUE) - BINOMDIST(5, 40, 0.2, TRUE)`. This is the closest alternative. |

## Tips and Best Practices

- Use the range form in Excel workbooks that stay in Excel, and the cumulative form in files shared with Sheets users.
- Check that `number_s2` is at least `number_s`. Swapped counts return `#NUM!` rather than a silent wrong answer.
- Enter the probability as a decimal, not as 25 for 25 percent.
- Use BINOM.DIST when you only need a cumulative result, because it is easier to read.
- Store the trial count, probability and range limits in labeled cells so the reviewer can see the assumptions.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BINOM.DIST](BINOM.DIST.md) | Returns the probability for one count or the cumulative probability, and works in Sheets. |
| [BINOM.INV](BINOM.INV.md) | Finds the smallest count that reaches a target cumulative probability. |
| [COMBIN](../Math%20%26%20Trig/COMBIN.md) | Counts the ways to choose successes, the building block of the binomial formula. |
| [CRITBINOM](CRITBINOM.md) | Returns the smallest count for a target probability, the Sheets counterpart of BINOM.INV. |

## Official Documentation

- [Microsoft Support: BINOM.DIST.RANGE function](https://support.microsoft.com/en-us/excel/functions/binom-dist-range-function)
