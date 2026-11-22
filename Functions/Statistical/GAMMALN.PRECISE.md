---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Special Functions
  - Statistical Analysis
use-case:
  - Factorial Counts for Large Numbers
  - Log Storage for Large Batches
related:
  - COMBIN
  - EXP
  - FACT
  - GAMMA
  - GAMMA.DIST
  - GAMMALN
  - LN
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/gammaln-precise-function
  - https://support.google.com/docs/answer/3093416
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Precise Log Gamma
tags:
  - distribution
  - excel
  - logarithm
  - sheets
  - special-functions
---

# GAMMALN.PRECISE

## Description

**GAMMALN.PRECISE** returns the natural logarithm of the gamma function, ln(Γ(x)). It calculates the same quantity as GAMMALN, which Microsoft documents separately in Excel. Both return the log of a gamma value, which stays in a manageable range for large inputs, so a sheet can add logs where multiplying the raw gamma values would overflow.

For a positive whole number `i`, EXP(GAMMALN.PRECISE(`i`)) returns (`i` minus 1) factorial, so the function is a practical way to work with large factorials. For fractional inputs, the result is the log of a value that has no factorial equivalent.

Use GAMMALN.PRECISE in Excel when a workbook will stay in Excel. The Google Sheets help page for GAMMALN does not describe GAMMALN.PRECISE, so a file that must open in Google Sheets should use GAMMALN.

## Syntax

```excel
=GAMMALN.PRECISE(x)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/GAMMALN.PRECISE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value for which to calculate ln(Γ(x)). Must be greater than 0. |

### Return Value

A number: the natural logarithm of the gamma function at `x`. The function returns `#NUM!` when `x` is 0 or less, and `#VALUE!` when `x` is not a number.

## Examples

### Example 1: Log of a Gamma Value

```excel
=GAMMALN.PRECISE(6)
```

**Result:** `4.787492`

This is ln(120), because Γ(6) equals 5! = 120.

### Example 2: Recovering a Factorial

```excel
=EXP(GAMMALN.PRECISE(9))
```

**Result:** `40320`

Γ(9) equals 8!, so EXP returns 40320.

<!-- Image 2: Log Scale Versus Factorial Growth. See Images/Statistical/GAMMALN.PRECISE.md -->

### Example 3: A Fractional Input

```excel
=GAMMALN.PRECISE(0.5)
```

**Result:** `0.572365`

Γ(0.5) equals the square root of π, so the result is ln(√π).

### Example 4: Handling Negative Input

```excel
=IFERROR(GAMMALN.PRECISE(-2), "Enter a positive number")
```

**Result:** `Enter a positive number`

Zero and negative inputs return `#NUM!`, so IFERROR replaces the error with a message.

## Story Problems

### Problem 1: Logging Large Batch Sizes

A quality lab tracks how many possible sequences exist for each batch. Batch B has 12 items, and the team stores the log of 12! to keep the column readable.

| Batch | Items |
| --- | --- |
| Batch A | 10 |
| Batch B | 12 |

**Task:** Find ln(12!) for Batch B (row 3) using GAMMALN.PRECISE.

**Solution:**

```excel
=GAMMALN.PRECISE(B3 + 1)
```

**Answer:** `19.9872`, because Γ(13) equals 12!, which is 479,001,600, and its natural log is 19.9872.

### Problem 2: Gamma Shape Adjustment

A simulation needs ln(Γ(2.5)) as a constant. The shape value 2.5 is not a whole number, so the team uses the gamma function.

**Task:** Find ln(Γ(2.5)).

**Solution:**

```excel
=GAMMALN.PRECISE(2.5)
```

**Answer:** `0.2847`, because Γ(2.5) equals 0.75 × √π, about 1.3293.

## Use Cases

### Factorial Counts for Large Numbers

**Scenario:** A planner estimates the number of possible arrangements for a large set of items and needs the result in a log column.

```excel
=GAMMALN.PRECISE(Items + 1)
```

**Why It Works:** The log stays small enough to store and compare. Convert with EXP only when the final value is small enough to display.

### Stable Log Likelihood Terms

**Scenario:** An analyst sums gamma terms for each observed count in a likelihood calculation.

```excel
=SUMPRODUCT(GAMMALN.PRECISE(CountRange + 1))
```

**Why It Works:** Adding logs is the same as multiplying the gamma values. The sum avoids overflow for large counts.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is 0 or negative. | Use a positive value, or handle zero with IF. |
| `#VALUE!` | `x` is text. | Convert the cell to a number. |
| `#NUM!` after EXP | The log value is too large to convert back. | Keep the result as a log. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Returns ln(Γ(x)). `x` must be greater than 0. |
| Google Sheets | Not documented on the GAMMALN help page | Use GAMMALN, which takes the same argument and returns the same kind of result. |

## Tips and Best Practices

- Use GAMMALN when the workbook must open in Google Sheets.
- Keep logs in one column and convert with EXP only in the final report.
- Use FACT for small whole numbers when an exact factorial is easier to read.
- Test the formula with a known value, such as 6 returning 4.787492, before you trust it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GAMMALN](GAMMALN.md) | The older name for the same calculation, documented in Google Sheets. |
| [FACT](../Math%20%26%20Trig/FACT.md) | Exact factorial for whole numbers. |
| [GAMMA](GAMMA.md) | The gamma function itself, before taking the log. |
| [GAMMA.DIST](GAMMA.DIST.md) | Gamma distribution that uses gamma values in its formula. |
| [COMBIN](../Math%20%26%20Trig/COMBIN.md) | Counts combinations, which can be computed from gamma values. |
| [LN](../Math%20%26%20Trig/LN.md) | Natural logarithm of ordinary numbers. |

## Official Documentation

- [Microsoft Support: GAMMALN.PRECISE function](https://support.microsoft.com/en-us/excel/functions/gammaln-precise-function)
- [Google Docs Editors Help: GAMMALN](https://support.google.com/docs/answer/3093416)
