---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Beta Model Migration
  - Legacy Workbook Updates
related:
  - BETA.DIST
  - BETA.INV
  - BETAINV
  - GAMMA.DIST
  - NORM.DIST
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/betadist-function
  - https://support.google.com/docs/answer/9084099
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Beta Distribution
tags:
  - compatibility
  - distributions
  - excel
  - probability
  - sheets
---

# BETADIST

## Description

**BETADIST** returns the cumulative beta distribution: the probability that a value between two bounds is at or below a given point. It is kept in Excel for compatibility with workbooks created in earlier versions. Microsoft replaced it with **BETA.DIST**, which returns the same cumulative probability and also offers a density option when the `cumulative` argument is FALSE.

Use BETADIST only when you must keep an older workbook working unchanged. In a new formula, use BETA.DIST with `cumulative` set to TRUE. The result is identical for the same inputs, as the examples below show. BETADIST has no cumulative argument, so it never returns a density.

Google's help page for BETADIST refers readers to BETA.DIST, so the Sheets formula should be written with BETA.DIST. The shape parameters must be positive, and the bounds default to 0 and 1 when they are left out.

## Syntax

```excel
=BETADIST(x, alpha, beta, [A], [B])
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/BETADIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value at which to evaluate the function. It must fall between `A` and `B`. |
| `alpha` | Yes | The first shape parameter of the distribution. |
| `beta` | Yes | The second shape parameter of the distribution. |
| `A` | No | The lower bound of the interval. If omitted, it is 0. |
| `B` | No | The upper bound of the interval. If omitted, it is 1. |

### Return Value

A number between 0 and 1: the cumulative beta probability at `x`. Invalid inputs return an error. The error values follow the same rules as BETA.DIST, so check that page for the cases that produce `#NUM!` and `#VALUE!`.

## Examples

### Example 1: Cumulative Probability on the Default Interval

```excel
=BETADIST(0.5, 2, 3)
```

**Result:** `0.6875`

The chance that the value is at or below 0.5 is 68.75 percent when alpha is 2 and beta is 3.

### Example 2: The Same Probability With BETA.DIST

```excel
=BETA.DIST(0.5, 2, 3, TRUE)
```

**Result:** `0.6875`

The replacement function returns the same value. A workbook can move to BETA.DIST without any change to the answer.

### Example 3: Custom Bounds

```excel
=BETADIST(3, 2, 3, 1, 5)
```

**Result:** `0.6875`

The interval from 1 to 5 is rescaled to 0 to 1, so 3 maps to 0.5, the same point as Example 1.

### Example 4: Probability in the Lower Tail

```excel
=BETADIST(0.2, 2, 5)
```

**Result:** `0.3446`

About 34.5 percent of the cumulative probability lies at or below 0.2 when alpha is 2 and beta is 5.

## Story Problems

### Problem 1: Migrating a Legacy Risk Model

A risk team's older workbook uses `=BETADIST(B2, B3, B4)` to estimate the chance that a defect rate stays at or below a threshold. The inputs are in `A1:B4`.

| Input | Value |
| --- | --- |
| Defect rate threshold | 0.2 |
| Alpha | 2 |
| Beta | 5 |

**Task:** Rewrite the formula with the replacement function so the answer stays the same.

**Solution:**

```excel
=BETA.DIST(B2, B3, B4, TRUE)
```

**Answer:** `0.3446`. This matches the legacy formula `=BETADIST(0.2, 2, 5)` from Example 4.

<!-- Image 2: Legacy and Replacement Formulas Side by Side. See Images/Statistical/BETADIST.md -->

### Problem 2: Bounded Legacy Calculation

A workbook models a delivery window from 10 to 20 minutes with alpha 2 and beta 2. The team wants the probability that a delivery takes 12 minutes or less.

**Task:** Find the cumulative probability with the legacy function.

**Solution:**

```excel
=BETADIST(12, 2, 2, 10, 20)
```

**Answer:** `0.104`. The value 12 maps to 0.2 on the 0 to 1 scale, and the cumulative probability at 0.2 for alpha 2 and beta 2 is 0.104.

## Use Cases

### Beta Model Migration

**Scenario:** An analyst inherits a workbook full of BETADIST formulas and must update them before the file is shared with a team that uses current Excel.

```excel
=BETA.DIST(Threshold, Alpha, Beta, TRUE)
```

**Why It Works:** BETA.DIST with `cumulative` set to TRUE returns the same probability, so the migrated formulas keep their results while using the current function name.

### Legacy Workbook Updates

**Scenario:** A finance model uses bounded inputs and must keep its original results while the team adds new scenarios.

```excel
=BETADIST(Score, Alpha, Beta, Lower, Upper)
```

**Why It Works:** The explicit bounds make the rescaling visible in the formula, so reviewers can check each input against the original model.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected result | A density was expected, but BETADIST always returns the cumulative probability. | Use BETA.DIST with `cumulative` set to FALSE for a density. |
| `#NUM!` | `x` is outside the interval, or the shape parameters are not positive. | Check the inputs against the bounds and parameter rules. |
| `#VALUE!` | An argument is text or blank. | Convert the input to a number or reference a numeric cell. |
| Unexpected result | The bounds are omitted, so the interval is 0 to 1. | Pass `A` and `B` explicitly when the model uses another scale. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available as a compatibility function | Microsoft documents BETA.DIST as the replacement. Use BETA.DIST in new work. |
| Google Sheets | Documented by reference to BETA.DIST | The BETADIST help page points to BETA.DIST, so write new formulas with BETA.DIST. |

## Tips and Best Practices

- Replace BETADIST with BETA.DIST in every workbook you maintain, and keep the same inputs so the results can be compared.
- Keep a side-by-side test of the old and new formulas until the migration is confirmed.
- Pass bounds explicitly when the model does not use 0 and 1.
- Use BETA.INV for the reverse calculation, from a probability to a value.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BETA.DIST](BETA.DIST.md) | Replacement function that returns the same cumulative probability and adds a density option. |
| [BETA.INV](BETA.INV.md) | Inverse of the cumulative beta distribution, returning the value for a probability. |
| [BETAINV](BETAINV.md) | Compatibility version of the inverse function. |
| [GAMMA.DIST](GAMMA.DIST.md) | Another continuous distribution for positive values. |
| [NORM.DIST](NORM.DIST.md) | Normal distribution for values that cluster around a mean. |

## Official Documentation

- [Microsoft Support: BETADIST function](https://support.microsoft.com/en-us/excel/functions/betadist-function)
- [Google Docs Editors Help: BETADIST](https://support.google.com/docs/answer/9084099)
