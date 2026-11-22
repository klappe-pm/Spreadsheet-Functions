---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Defect Counts In Samples
  - Delivery Damage Counts
  - Raffle Win Odds
related:
  - BINOM.DIST
  - BINOM.DIST.RANGE
  - BINOM.INV
  - COMBIN
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/binomdist-function
  - https://support.google.com/docs/answer/3093987
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Binomial Probability
  - Binomial Mass Function
tags:
  - binomial
  - compatibility
  - distributions
  - excel
  - sheets
---

# BINOMDIST

## Description

**BINOMDIST** returns the probability of a given number of successes in a fixed number of independent trials. It calculates the same values as BINOM.DIST and takes the same arguments in the same order. Microsoft replaced it with BINOM.DIST, so Excel keeps it only for backward compatibility.

Set the last argument to FALSE for the probability of exactly that many successes. Set it to TRUE for the probability of that many successes or fewer. The two forms answer different questions, so confirm which one a workbook needs before copying the formula.

Use BINOMDIST when you maintain a workbook that already contains it or when you need its exact behavior in Google Sheets. For new Excel work, use BINOM.DIST. Microsoft warns that BINOMDIST may not be available in future versions of Excel.

## Syntax

```excel
=BINOMDIST(number_s, trials, probability_s, cumulative)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/BINOMDIST.md -->

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

### Example 1: Exactly Two Successes

```excel
=BINOMDIST(2, 8, 0.3, FALSE)
```

**Result:** `0.2965`

Eight trials at a 30 percent chance produce exactly two successes about 29.7 percent of the time.

### Example 2: Two Successes or Fewer

```excel
=BINOMDIST(2, 8, 0.3, TRUE)
```

**Result:** `0.5518`

The cumulative form adds the probabilities for 0, 1 and 2 successes. It is the only change from Example 1.

<!-- Image 2: Exact Versus Cumulative Results. See Images/Statistical/BINOMDIST.md -->

### Example 3: Reading Inputs From Cells

Row 2 holds 4 successes in `B2`, 15 trials in `B3` and a probability of 0.6 in `B4`.

```excel
=BINOMDIST(B2, B3, B4, TRUE)
```

**Result:** `0.0093`

The chance of four or fewer successes in this case is under 1 percent, which suggests the success rate of 60 percent is higher than the sample supports.

### Example 4: The Same Result With BINOM.DIST

```excel
=BINOM.DIST(2, 8, 0.3, FALSE)
```

**Result:** `0.2965`

BINOM.DIST returns the same value as Example 1 with the same arguments. Use it in new Excel workbooks.

## Story Problems

### Problem 1: Damaged Deliveries

A courier handles 12 parcels on a route. Each parcel arrives damaged with a 15 percent chance, independently of the others. The dispatcher wants the chance that exactly 2 parcels arrive damaged.

| Input | Value |
| --- | --- |
| Parcels | 12 |
| Damage Chance | 0.15 |
| Damaged | 2 |

**Task:** Enter the inputs in `B1:B3` and find the probability of exactly 2 damaged parcels.

**Solution:**

```excel
=BINOMDIST(B3, B1, B2, FALSE)
```

**Answer:** `0.2924`. Exactly two damaged parcels happens on about 29 percent of routes.

### Problem 2: Raffle Wins

A member plays 10 independent draws in a raffle. Each draw has a 5 percent chance of winning. The member wants the chance of winning at most once.

| Input | Value |
| --- | --- |
| Draws | 10 |
| Win Chance | 0.05 |
| Maximum Wins | 1 |

**Task:** Find the probability of at most one win using the inputs in `B1:B3`.

**Solution:**

```excel
=BINOMDIST(B3, B1, B2, TRUE)
```

**Answer:** `0.9139`. The member wins at most once about 91 percent of the time.

## Use Cases

### Defect Counts In Samples

**Scenario:** A legacy quality workbook checks whether a sample of 20 parts shows at most one defect when the defect rate is 3 percent.

```excel
=BINOMDIST(1, 20, 0.03, TRUE)
```

**Why It Works:** The formula keeps the legacy function that the workbook already uses. Replacing it with BINOM.DIST gives the same result and is safer for future Excel versions.

### Delivery Damage Counts

**Scenario:** A logistics sheet lists the parcel count and damage rate in cells and calculates the exact probability of no damage.

```excel
=BINOMDIST(0, B2, B3, FALSE)
```

**Why It Works:** Referencing the count and rate in cells means the sheet updates when the route changes, and the zero count shows the no-damage case directly.

### Raffle Win Odds

**Scenario:** A club shows members the chance of winning no prizes across six draws with a 2 percent win rate per draw.

```excel
=BINOMDIST(0, 6, 0.02, FALSE)
```

**Why It Works:** A zero success count is the simplest case, and it reads clearly in a member-facing sheet.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `number_s` is below 0 or above `trials`. | Keep the success count between 0 and the number of trials. |
| `#NUM!` | `probability_s` is below 0 or above 1. | Enter a decimal probability, not a percentage. |
| `#VALUE!` | An argument is text. | Convert the input cells to numbers. |
| Result looks too large | `cumulative` is TRUE when an exact count was wanted. | Use FALSE for the probability of exactly `number_s`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available for backward compatibility | Replaced by BINOM.DIST. Microsoft warns it may not be available in future versions. |
| Google Sheets | Available | Documented under this name with the same argument order. The cumulative argument defaults to FALSE. |

## Tips and Best Practices

- Use BINOM.DIST in new Excel work, and keep BINOMDIST only where a workbook or a Sheets file depends on it.
- Pass the cumulative argument explicitly. Excel requires it, and omitting it in Sheets falls back to FALSE, which is easy to miss.
- Enter probabilities as decimals from 0 to 1.
- Replace legacy formulas in a workbook in one pass and recheck a few results against the original values.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BINOM.DIST](BINOM.DIST.md) | The modern replacement with the same arguments. |
| [BINOM.DIST.RANGE](BINOM.DIST.RANGE.md) | Returns the probability for a range of counts in Excel. |
| [BINOM.INV](BINOM.INV.md) | Finds the smallest count that reaches a target cumulative probability. |
| [COMBIN](../Math%20%26%20Trig/COMBIN.md) | Counts the ways to choose successes, the core of the probability formula. |

## Official Documentation

- [Microsoft Support: BINOMDIST function](https://support.microsoft.com/en-us/excel/functions/binomdist-function)
- [Google Docs Editors Help: BINOMDIST](https://support.google.com/docs/answer/3093987)
