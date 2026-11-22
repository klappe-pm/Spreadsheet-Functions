---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Committee Selection Odds
  - Lot Inspection Sampling
related:
  - BINOM.DIST
  - COMBIN
  - HYPGEOMDIST
  - NEGBINOM.DIST
  - POISSON.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/hypgeom-dist-function
  - https://support.google.com/docs/answer/3094004
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Hypergeometric Distribution
tags:
  - distribution
  - excel
  - probability
  - sampling
  - sheets
---

# HYPGEOM.DIST

## Description

**HYPGEOM.DIST** returns the hypergeometric distribution: the probability of drawing a given number of successes in a sample taken without replacement from a finite population. A success is any item with the attribute you are counting, such as a defective part, a manager on a committee or a red marble. Because each draw changes the remaining population, the chances change with every item removed.

With `cumulative` set to FALSE, the function returns the probability of exactly `sample_s` successes. With TRUE, it returns the probability of `sample_s` successes or fewer. Use the cumulative form to answer questions such as "at most one defective item" or "at least one defective item," by subtracting from 1.

HYPGEOM.DIST is the Excel version of the hypergeometric function. It has the same purpose as HYPGEOMDIST, but it adds the cumulative argument as a fifth parameter, which the older function did not have in Excel. Google's help page for this family documents HYPGEOMDIST, not HYPGEOM.DIST, so workbooks that must open in Sheets should use HYPGEOMDIST with its own argument order.

## Syntax

```excel
=HYPGEOM.DIST(sample_s, number_sample, population_s, number_pop, cumulative)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/HYPGEOM.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `sample_s` | Yes | The number of successes in the sample. Must be between 0 and the smaller of `number_sample` and `population_s`. |
| `number_sample` | Yes | The size of the sample. Must be greater than 0 and no more than `number_pop`. |
| `population_s` | Yes | The number of successes in the population. Must be greater than 0 and no more than `number_pop`. |
| `number_pop` | Yes | The size of the population. Must be greater than 0. |
| `cumulative` | Yes | TRUE returns the probability of `sample_s` successes or fewer. FALSE returns the probability of exactly `sample_s` successes. |

### Return Value

A probability between 0 and 1. The function truncates all numeric arguments to whole numbers. It returns `#NUM!` when `sample_s` falls outside its allowed range or when another argument breaks a rule in the table above, and `#VALUE!` when any argument is not numeric.

## Examples

### Example 1: Exact Probability

```excel
=HYPGEOM.DIST(2, 5, 10, 30, FALSE)
```

**Result:** `0.359985`

Drawing 5 items from 30, where 10 are successes, gives exactly 2 successes about 36 percent of the time.

### Example 2: Cumulative Probability

```excel
=HYPGEOM.DIST(2, 5, 10, 30, TRUE)
```

**Result:** `0.808766`

This is the chance of 0, 1 or 2 successes in the same sample.

### Example 3: At Least One Success

```excel
=1 - HYPGEOM.DIST(0, 5, 10, 30, TRUE)
```

**Result:** `0.891205`

The probability of zero successes is subtracted from 1, which gives the chance of at least one success.

### Example 4: Guarding Against Invalid Arguments

```excel
=IFERROR(HYPGEOM.DIST(6, 5, 10, 30, FALSE), "Check arguments")
```

**Result:** `Check arguments`

A sample cannot contain more successes than the sample size, so the function returns `#NUM!` and IFERROR shows a message.

<!-- Image 2: Sample Draws Without Replacement. See Images/Statistical/HYPGEOM.DIST.md -->

## Story Problems

### Problem 1: Defective Items in a Sample

A lot holds 40 parts, and 6 of them are defective. An inspector draws 8 parts without replacement.

| Measure | Value |
| --- | --- |
| Lot size | 40 |
| Defective parts | 6 |
| Sample size | 8 |

**Task:** Find the probability that the sample contains exactly 2 defective parts. Keep the values in the table in `B2` (lot size), `B3` (defective parts) and `B4` (sample size).

**Solution:**

```excel
=HYPGEOM.DIST(2, B4, B3, B2, FALSE)
```

**Answer:** `0.2623`, which means about 26 percent of samples will contain exactly two defective parts.

### Problem 2: Acceptance Rule

Using the same lot of 40 parts with 6 defective items and a sample of 8, the buyer accepts the lot only when the sample holds one defective part or none.

**Task:** Find the probability that the lot passes the rule.

**Solution:**

```excel
=HYPGEOM.DIST(1, 8, 6, 40, TRUE)
```

**Answer:** `0.6558`, so about 66 percent of lots pass with this rule.

## Use Cases

### Committee Selection Odds

**Scenario:** A board wants to know how likely it is that a random committee contains a specific number of managers.

```excel
=HYPGEOM.DIST(ManagersOnCommittee, CommitteeSize, Managers, Staff, FALSE)
```

**Why It Works:** Each person is picked once, so the function models the draws without replacement. The formula updates when the staff list changes.

### Lot Inspection Sampling

**Scenario:** A quality team sets an acceptance rule and checks how often a lot with a known defect count passes.

```excel
=HYPGEOM.DIST(MaxDefects, SampleSize, DefectsInLot, LotSize, TRUE)
```

**Why It Works:** The cumulative form returns the chance of passing the rule. Compare results for several defect counts to see how sensitive the rule is.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `sample_s` is larger than the sample size or the population successes, or another range rule is broken. | Check each argument against the rules in the parameter table. |
| `#VALUE!` | An argument is text or an empty reference. | Enter numbers in every argument. |
| Unexpectedly small result | Cumulative was set to FALSE when a range of outcomes was needed. | Set `cumulative` to TRUE for "or fewer" questions. |
| Wrong order | The arguments were entered in the HYPGEOMDIST order. | Use sample successes, sample size, population successes, population size. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed on the Microsoft page for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Five arguments, with `cumulative` as the last. Replaces HYPGEOMDIST for new work. |
| Google Sheets | Not documented on the Sheets help page for this name | Use HYPGEOMDIST, which Google documents with a `cumulative` argument and the arguments num_successes, num_draws, successes_in_pop and pop_size. |

## Tips and Best Practices

- Use `1 - HYPGEOM.DIST(..., TRUE)` for "at least" questions.
- Put the population and sample sizes in labeled cells so the formula stays readable.
- Use BINOM.DIST only when draws are with replacement, because it gives a different answer for small populations.
- Check the argument order against the syntax before copying a formula from an older workbook.

## Related Functions

| Function | Relationship |
| --- | --- |
| [HYPGEOMDIST](HYPGEOMDIST.md) | The older version with four arguments in Excel. |
| [BINOM.DIST](BINOM.DIST.md) | Binomial model for draws with replacement, or a very large population. |
| [COMBIN](../Math%20%26%20Trig/COMBIN.md) | Counts the combinations used in the hypergeometric formula. |
| [POISSON.DIST](POISSON.DIST.md) | Counts events over time or area when the events are rare. |
| [NEGBINOM.DIST](NEGBINOM.DIST.md) | Counts failures before a fixed number of successes. |

## Official Documentation

- [Microsoft Support: HYPGEOM.DIST function](https://support.microsoft.com/en-us/excel/functions/hypgeom-dist-function)
- [Google Docs Editors Help: HYPGEOMDIST](https://support.google.com/docs/answer/3094004)
