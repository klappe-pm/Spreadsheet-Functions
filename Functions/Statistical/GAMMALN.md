---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Special Functions
  - Statistical Analysis
use-case:
  - Factorial Counts for Large Numbers
  - Gamma Values for Fractional Inputs
related:
  - COMBIN
  - EXP
  - FACT
  - GAMMA
  - GAMMA.DIST
  - GAMMALN.PRECISE
  - LN
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/gammaln-function
  - https://support.google.com/docs/answer/3093416
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Log Gamma Function
  - Natural Log of Gamma
tags:
  - distribution
  - excel
  - logarithm
  - sheets
  - special-functions
---

# GAMMALN

## Description

**GAMMALN** returns the natural logarithm of the gamma function, written as ln(Γ(x)). The gamma function extends factorials to non-integer numbers: for a whole number `n`, Γ(n) equals `(n - 1)!`. Because gamma values grow very quickly, a spreadsheet often stores the logarithm instead, which stays within a normal range even for large inputs.

Use GAMMALN when a formula needs the log of a gamma value, such as a log-likelihood, a distribution constant, or a count of arrangements too large to multiply out. Google describes it as a helper used inside other analysis, and it is rarely needed on its own.

The argument must be greater than zero. Microsoft also documents GAMMALN.PRECISE, which returns the same kind of result. The Google Sheets help page for GAMMALN does not describe a separate GAMMALN.PRECISE, so use GAMMALN for workbooks that must open in both programs.

## Syntax

```excel
=GAMMALN(x)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/GAMMALN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value for which to calculate ln(Γ(x)). Must be greater than 0. |

### Return Value

A number: the natural logarithm of the gamma function at `x`. Use EXP to convert the result back to the gamma value. The function returns `#NUM!` when `x` is 0 or less, and `#VALUE!` when `x` is not a number.

## Examples

### Example 1: Log of a Gamma Value

```excel
=GAMMALN(6)
```

**Result:** `4.787492`

This is ln(120), because Γ(6) equals 5! = 120.

### Example 2: Converting Back to a Factorial

```excel
=EXP(GAMMALN(7))
```

**Result:** `720`

EXP reverses the logarithm, and Γ(7) equals 6! = 720.

<!-- Image 2: Log Scale Versus Factorial Growth. See Images/Statistical/GAMMALN.md -->

### Example 3: A Fractional Input

```excel
=GAMMALN(0.5)
```

**Result:** `0.572365`

Γ(0.5) equals the square root of π, so the result is ln(√π). A fractional input has no factorial equivalent, which is why the gamma function is needed.

### Example 4: Handling Zero

```excel
=IFERROR(GAMMALN(0), "Enter a positive number")
```

**Result:** `Enter a positive number`

A zero input returns `#NUM!`, so the formula shows a message instead.

## Story Problems

### Problem 1: Staff Line Ups

A company wants to know how many different orders a crew can line up in for a photo. The team sizes are in the table below.

| Team | Staff |
| --- | --- |
| Front Desk | 3 |
| Kitchen | 5 |
| Warehouse | 8 |

**Task:** Find the number of ways to order the 8 warehouse staff, using GAMMALN so the calculation stays small.

**Solution:**

```excel
=EXP(GAMMALN(B4 + 1))
```

**Answer:** `40320`, because Γ(9) equals 8!, which is 40320.

### Problem 2: Gamma Value for a Scale Factor

A researcher needs Γ(4.5) to scale a fitted curve. The value is not a whole factorial, so the team uses the gamma function.

**Task:** Find Γ(4.5) with GAMMALN.

**Solution:**

```excel
=EXP(GAMMALN(4.5))
```

**Answer:** `11.631728`, because Γ(4.5) = 3.5 × 2.5 × 1.5 × 0.5 × √π.

## Use Cases

### Factorial Counts for Large Numbers

**Scenario:** An analyst counts the ways to choose and order items in a process where the totals exceed the largest number a spreadsheet can multiply.

```excel
=GAMMALN(N + 1) - GAMMALN(K + 1)
```

**Why It Works:** Subtracting logs divides the factorials. Convert the result with EXP only when the final number is small enough to display.

### Log Likelihood Components

**Scenario:** A modeler adds a constant term to a log-likelihood that depends on the gamma function of the observed counts.

```excel
=SUM(GAMMALN(CountRange + 1))
```

**Why It Works:** Summing the logs is the same as multiplying the gamma values, and the sum stays stable for large counts.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `x` is 0 or negative. | Use a positive value, or handle zero with IF. |
| `#VALUE!` | `x` is text. | Convert the cell to a number. |
| `#NUM!` after EXP | The log value is too large to convert back. | Keep the result as a log, or use a ratio of logs. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions | Documented with a single argument. `x` must be greater than 0. |
| Google Sheets | Available | The help page documents one argument, `value`, which must be positive. |

## Tips and Best Practices

- Use EXP only at the end of a calculation, so the working numbers stay in log form.
- Use FACT for small whole numbers when you need an exact factorial.
- Subtract logs instead of dividing large gamma values.
- Use GAMMALN.PRECISE in Excel when your file does not need to open in Google Sheets.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FACT](../Math%20%26%20Trig/FACT.md) | Exact factorial for whole numbers. |
| [GAMMA](GAMMA.md) | The gamma function itself, not its logarithm. |
| [GAMMA.DIST](GAMMA.DIST.md) | Gamma probability distribution that uses gamma values in its formula. |
| [GAMMALN.PRECISE](GAMMALN.PRECISE.md) | The Excel version with the same result. |
| [COMBIN](../Math%20%26%20Trig/COMBIN.md) | Counts combinations, which can be computed from gamma values. |
| [LN](../Math%20%26%20Trig/LN.md) | Natural logarithm of ordinary numbers. |

## Official Documentation

- [Microsoft Support: GAMMALN function](https://support.microsoft.com/en-us/excel/functions/gammaln-function)
- [Google Docs Editors Help: GAMMALN](https://support.google.com/docs/answer/3093416)
