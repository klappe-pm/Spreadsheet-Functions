---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Committee Selection Odds
  - Defect Sampling Without Replacement
related:
  - BINOM.DIST
  - COMBIN
  - HYPGEOM.DIST
  - NEGBINOM.DIST
  - POISSON.DIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/hypgeomdist-function
  - https://support.google.com/docs/answer/3094004
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Hypergeometric Probability
tags:
  - compatibility
  - distribution
  - probability
  - sampling
  - sheets
---

# HYPGEOMDIST

## Description

**HYPGEOMDIST** returns the probability of drawing a given number of successes in a sample taken without replacement from a finite population. A success is any item with the attribute you count, such as a defective part, a manager on a committee or a marked card. Each item drawn is removed from the population, so the probability changes with every draw.

In Excel, HYPGEOMDIST is a compatibility function. It returns the probability of exactly `sample_s` successes and takes four arguments. Microsoft replaced it with HYPGEOM.DIST, which adds a `cumulative` argument so one formula can return either the exact probability or the probability of that many successes or fewer. HYPGEOMDIST still works in current versions of Excel, but Microsoft says it may not be available in future versions, so use HYPGEOM.DIST for new work.

Google Sheets documents HYPGEOMDIST with five arguments, the last being `cumulative`. A formula written for Sheets with that fifth argument will not work in Excel, which accepts four. Check the function signature in the program where the file will be opened.

## Syntax

```excel
=HYPGEOMDIST(sample_s, number_sample, population_s, number_pop)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/HYPGEOMDIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `sample_s` | Yes | The number of successes in the sample. Must be between 0 and the smaller of `number_sample` and `population_s`. |
| `number_sample` | Yes | The size of the sample. Must be greater than 0 and no more than `number_pop`. |
| `population_s` | Yes | The number of successes in the population. Must be greater than 0 and no more than `number_pop`. |
| `number_pop` | Yes | The size of the population. Must be greater than 0. |

### Return Value

A probability between 0 and 1 for exactly `sample_s` successes. The function truncates all numeric arguments to whole numbers. It returns `#NUM!` when an argument breaks one of the rules above and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Two Managers on a Committee

```excel
=HYPGEOMDIST(2, 5, 4, 12)
```

**Result:** `0.424242`

Choosing 5 people from 12, where 4 are managers, gives exactly 2 managers about 42 percent of the time.

### Example 2: No Successes in the Sample

```excel
=HYPGEOMDIST(0, 3, 6, 15)
```

**Result:** `0.184615`

The chance that all 3 draws are non-successes is 84 out of 455 possible samples.

### Example 3: At Least One Success

```excel
=1 - HYPGEOMDIST(0, 3, 6, 15)
```

**Result:** `0.815385`

Subtracting the probability of zero successes from 1 gives the chance of at least one success.

### Example 4: Guarding Against Invalid Arguments

```excel
=IFERROR(HYPGEOMDIST(4, 3, 6, 15), "Check arguments")
```

**Result:** `Check arguments`

A sample cannot contain more successes than its size, so the function returns `#NUM!` and IFERROR shows a message.

<!-- Image 2: Successes in a Sample Without Replacement. See Images/Statistical/HYPGEOMDIST.md -->

## Story Problems

### Problem 1: Committee Composition

A firm has 12 staff members, and 4 of them are managers. A committee of 5 is chosen at random.

| Measure | Value |
| --- | --- |
| Total staff | 12 |
| Managers | 4 |
| Committee size | 5 |

**Task:** Find the probability that the committee has exactly 2 managers. The values are in `B2` (total staff), `B3` (managers) and `B4` (committee size).

**Solution:**

```excel
=HYPGEOMDIST(2, B4, B3, B2)
```

**Answer:** `0.4242`, about a 42 percent chance of exactly two managers.

### Problem 2: No Managers at All

Using the same firm, the board wants to know how likely it is that a random committee of 5 has no managers.

**Task:** Find the probability of zero managers on the committee, using the cells from Problem 1.

**Solution:**

```excel
=HYPGEOMDIST(0, B4, B3, B2)
```

**Answer:** `0.0707`, which is 56 possible committees out of 792.

## Use Cases

### Committee Selection Odds

**Scenario:** An HR analyst checks how often a random panel will include a required number of people from a specific group.

```excel
=HYPGEOMDIST(GroupMembers, PanelSize, GroupTotal, StaffTotal)
```

**Why It Works:** Each person is selected once, so the probability depends on the remaining pool. Put the counts in labeled cells so the formula updates with the staff list.

### Defect Sampling Without Replacement

**Scenario:** A quality technician estimates the chance that a sample of parts contains a given number of defects.

```excel
=HYPGEOMDIST(DefectsInSample, SampleSize, DefectsInLot, LotSize)
```

**Why It Works:** Parts are inspected once and set aside, so the draws are without replacement. For a sample that is tiny compared with the lot, BINOM.DIST gives a close approximation.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `sample_s` is outside the allowed range, or another population rule is broken. | Check each argument against the parameter table. |
| `#VALUE!` | An argument is text or an empty reference. | Enter numbers in every argument. |
| Argument count error | A formula written for Sheets includes a fifth `cumulative` argument. | Remove the fifth argument, or use HYPGEOM.DIST with TRUE for cumulative results. |
| Wrong result | The arguments were entered in another order. | Use sample successes, sample size, population successes, population size. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available as a compatibility function | Four arguments and exact probability only. Microsoft names HYPGEOM.DIST as the replacement. |
| Google Sheets | Available | The help page documents five arguments: num_successes, num_draws, successes_in_pop, pop_size and cumulative. |

## Tips and Best Practices

- Use HYPGEOM.DIST in new Excel workbooks because it covers both exact and cumulative probabilities.
- Use `1 - HYPGEOMDIST(...)` for "at least one" questions in Excel.
- Put the four counts in labeled cells so the formula can be checked by eye.
- Keep the argument order consistent with the syntax before copying formulas between Excel and Sheets.

## Related Functions

| Function | Relationship |
| --- | --- |
| [HYPGEOM.DIST](HYPGEOM.DIST.md) | The current replacement, with a cumulative option. |
| [BINOM.DIST](BINOM.DIST.md) | Binomial model for draws with replacement, or a very large population. |
| [COMBIN](../Math%20%26%20Trig/COMBIN.md) | Counts the combinations used in the hypergeometric formula. |
| [POISSON.DIST](POISSON.DIST.md) | Counts rare events over time or area. |
| [NEGBINOM.DIST](NEGBINOM.DIST.md) | Counts failures before a fixed number of successes. |

## Official Documentation

- [Microsoft Support: HYPGEOMDIST function](https://support.microsoft.com/en-us/excel/functions/hypgeomdist-function)
- [Google Docs Editors Help: HYPGEOMDIST](https://support.google.com/docs/answer/3094004)
