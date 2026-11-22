---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Logarithms and Powers
purpose:
  - Arithmetic Operations
use-case:
  - Continuous Growth Projection
  - Decay Modeling
related:
  - LN
  - LOG
  - LOG10
  - POWER
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/exp-function
  - https://support.google.com/docs/answer/3093411
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Natural Exponential
tags:
  - excel
  - exponential
  - natural-log
  - sheets
---

# EXP

## Description

**EXP** returns Euler's number, e (about 2.718282), raised to a power. Use it in continuous growth and decay formulas, where the rate applies continuously rather than in fixed periods. The function is the inverse of LN, the natural logarithm, so `EXP(LN(x))` returns x.

EXP always uses base e. For any other base, use the exponentiation operator, so 2 to the power of 3 is written `=2^3`. EXP is the function to use when the exponent is a rate multiplied by a time, as in continuous compounding.

## Syntax

```excel
=EXP(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/EXP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The exponent applied to e. Google Sheets names this argument `exponent`. A non-numeric value returns `#VALUE!`. |

### Return Value

A number: e raised to the power of the input. A positive result is always returned for a numeric input, because e raised to any real power is greater than 0.

## Examples

### Example 1: Euler's Number

```excel
=EXP(1)
```

**Result:** `2.71828`

This is an approximation of e, the base of the natural logarithm.

### Example 2: Power of Two

```excel
=EXP(2)
```

**Result:** `7.38906`

e squared is about 7.38906.

### Example 3: Zero Exponent

```excel
=EXP(0)
```

**Result:** `1`

Any base raised to the power of 0 is 1.

### Example 4: Negative Exponent

```excel
=EXP(-1)
```

**Result:** `0.36788`

A negative exponent gives the reciprocal of e, which is 1 divided by 2.71828.

<!-- Image 2: EXP Inverse of LN. See Images/Math & Trig/EXP.md -->

### Example 5: Inverse of the Natural Logarithm

```excel
=EXP(LN(10))
```

**Result:** `10`

EXP undoes LN, so the result is the original value. A spreadsheet may display a tiny rounding difference in some cells.

## Story Problems

### Problem 1: Continuous Growth

An investor deposits 1000 in an account that earns a continuous annual rate. The inputs are stored in column B, and the task is to find the balance after three years.

| Input | Value |
| --- | --- |
| Principal | 1000 |
| Annual Rate | 0.05 |
| Years | 3 |

**Task:** Calculate the balance as the principal times e raised to the rate times the years.

**Solution:**

```excel
=B2*EXP(B3*B4)
```

**Answer:** `1161.83`. The exponent is 0.05 times 3, which is 0.15, and 1000 times e to the power of 0.15 is 1161.83.

### Problem 2: Decay Check

A sample loses value continuously. After two periods of a decay rate of 1, the analyst wants the fraction that remains.

| Input | Value |
| --- | --- |
| Elapsed Periods | 2 |

**Task:** Calculate e raised to the negative of the elapsed periods in B2.

**Solution:**

```excel
=EXP(-B2)
```

**Answer:** `0.13534`. The remaining fraction is e to the power of -2, which is about 13.5 percent of the original amount.

## Use Cases

### Continuous Growth Projection

**Scenario:** A planning sheet projects a balance for each year using the same principal and rate, with each year in a separate row.

```excel
=B2*EXP(B3*C2)
```

**Why It Works:** The principal in B2 is multiplied by e raised to the rate in B3 times the years in C2. Fill the formula down to project each year.

### Decay Modeling

**Scenario:** A table stores a decay rate and the elapsed time for several samples, and the report needs the remaining fraction for each row.

```excel
=EXP(-Decay[Rate]*Decay[Periods])
```

**Why It Works:** The negative sign makes the exponent negative, so the result falls below 1 as time increases. Check that the rate and periods use the same time unit.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The input is text or another non-numeric value. | Check the source cell, or convert the text to a number. |
| Result is very large | The exponent is large and positive. | Check the rate and time units, because the result grows quickly. |
| Result is very small | The exponent is large and negative. | Confirm the sign of the exponent is intended. |
| Wrong result for a base other than e | EXP was used where a different base was needed. | Use the `^` operator, such as `=2^3`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in the Math and trigonometry group. | The argument is named `number`. |
| Google Sheets | Available | The argument is named `exponent`. Sample formulas match Excel. |

## Tips and Best Practices

- Keep the rate and the time in the same units, such as annual rate and years, before multiplying them in the exponent.
- Use the `^` operator for bases other than e.
- Pair EXP with LN when a model moves between logarithmic and exponential forms.
- Format the result with a fixed number of decimal places when it feeds a financial report.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LN](LN.md) | The natural logarithm, the inverse of EXP. |
| [LOG](LOG.md) | Logarithm with a chosen base, for models that do not use base e. |
| [LOG10](LOG10.md) | Base 10 logarithm, the inverse of raising 10 to a power. |
| [POWER](POWER.md) | Raises a number to any power, for bases other than e. |

## Official Documentation

- [Microsoft Support: EXP function](https://support.microsoft.com/en-us/excel/functions/exp-function)
- [Google Docs Editors Help: EXP](https://support.google.com/docs/answer/3093411)
