---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Arithmetic Operations
use-case:
  - Gamma Function Inputs
  - Scaled Statistical Constants
related:
  - GAMMA
  - PI
  - POWER
  - ROUND
  - SQRT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/sqrtpi-function
  - https://support.google.com/docs/answer/3093579
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Square Root of Pi
tags:
  - arithmetic
  - constants
  - excel
  - sheets
---

# SQRTPI

## Description

**SQRTPI** returns the square root of a number multiplied by pi (about 3.14159). The formula it computes is the square root of (number × π). For example, SQRTPI(1) returns 1.772454, which is the square root of pi.

Use SQRTPI when a calculation needs the square root of a pi-scaled term. This shows up in some statistical formulas and in approximations of the gamma function. When you need the same result inside a longer formula, `SQRT(A2*PI())` returns identical values, but SQRTPI is shorter and states the intent.

SQRTPI returns the `#NUM!` error when the input is negative, because the square root of a negative product is not a real number. Zero returns zero. To get the negative root, multiply the result by -1.

## Syntax

```excel
=SQRTPI(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/SQRTPI.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value that pi is multiplied by. Enter zero or a positive number. A negative value returns `#NUM!`. Text that looks like a number, such as `"4"`, is converted when it is typed directly in the formula. |

### Return Value

A decimal number equal to the square root of `number` multiplied by pi. The result is always zero or positive. The function returns `#NUM!` when `number` is negative.

## Examples

### Example 1: Scale Pi by a Cell Value

Cell A2 contains `4`.

```excel
=SQRTPI(A2)
```

**Result:** `3.544908`

The function multiplies 4 by pi (12.566371) and returns its square root. The same value comes from `SQRT(A2*PI())`.

### Example 2: Round the Result for Display

Cell A2 contains `9`.

```excel
=ROUND(SQRTPI(A2), 2)
```

**Result:** `5.32`

SQRTPI(9) equals 5.317362. ROUND trims the value to two decimal places for a report column.

<!-- Image 2: Sample Inputs and Results. See Images/Math & Trig/SQRTPI.md -->

### Example 3: Flag Negative Inputs

Cell A2 contains `-1`.

```excel
=IFERROR(SQRTPI(A2), "Enter zero or more")
```

**Result:** `Enter zero or more`

IFERROR replaces the `#NUM!` error with a message, so a column of inputs stays readable when one entry is invalid.

### Example 4: Check Agreement With SQRT and PI

Cell A2 contains `7`.

```excel
=ROUND(SQRTPI(A2) - SQRT(A2*PI()), 10)
```

**Result:** `0`

Both routes calculate the same value, so the difference rounds to zero. This check is useful when a workbook mixes the two styles.

## Story Problems

### Problem 1: Scaling Factors for Sample Sizes

A quality analyst records four sample sizes in column A and needs a scaling factor for each one. The factor for each row is the square root of pi times the sample size.

| Sample Size | Scaling Factor |
| --- | --- |
| 1 | |
| 4 | |
| 6 | |
| 10 | |

**Task:** Fill column B with SQRTPI for each sample size, then total the factors.

**Solution:**

```excel
=SUM(B2:B5)
```

**Answer:** `15.264`, from 1.772 + 3.545 + 4.342 + 5.605 (rounded to three decimals on each term).

<!-- Image 3: Scaling Factors Table. See Images/Math & Trig/SQRTPI.md -->

### Problem 2: Validating a Column of Inputs

A lab technician enters four readings in column A. One entry was typed with a minus sign by mistake. The technician wants a scaled value for each valid reading and a clear flag for the bad one.

| Reading | Scaled Value |
| --- | --- |
| 2 | |
| 5 | |
| -3 | |

**Task:** Fill column B with a formula that returns SQRTPI for each reading and returns `Check` when the reading is negative.

**Solution:**

```excel
=IFERROR(SQRTPI(A2), "Check")
```

**Answer:** Row values are `2.506628` (for 2), `3.963327` (for 5) and `Check` (for -3).

## Use Cases

### Gamma Function Inputs

**Scenario:** A modeling workbook estimates gamma function values for small positive inputs and needs the pi-scaled square root as a separate building block.

```excel
=SQRTPI(B2)
```

**Why It Works:** Keeping the SQRTPI term in its own column makes the approximation formula in the next column short and easy to audit. Check the input column for negatives first, because they return `#NUM!`.

### Scaled Statistical Constants

**Scenario:** A research team compares normalizing constants from several experiments. Each constant is scaled by the square root of pi before the comparison.

```excel
=SQRTPI(C2)
```

**Why It Works:** The function returns the scaled value in one step, so each experiment row uses the same definition. Wrap the formula in IFERROR only when negative inputs are expected, so real data problems still surface.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is negative. | Enter zero or a positive number, or flag the row with IFERROR. |
| `#VALUE!` | The input is text that cannot be read as a number. | Convert the cell to a number or correct the source entry. |
| `#NAME?` | The function name is misspelled. | Check the spelling as `SQRTPI`. |
| Result looks too large | The formula multiplied by pi when a plain square root was intended. | Use `SQRT(number)` instead when pi should not be part of the calculation. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | The argument is named `number`. A negative input returns `#NUM!`. |
| Google Sheets | Available | The argument is named `value`. A negative input returns `#NUM!`. The help page describes the function as the positive square root of pi times a positive number. |

## Tips and Best Practices

- Use SQRTPI rather than repeating `SQRT(A2*PI())` in many cells, so the intent stays visible.
- Keep inputs numeric. Text values that look like numbers can produce errors when they come from imports.
- Validate negative inputs before the formula runs, so `#NUM!` does not hide in totals.
- Round only for display. Keep full precision in intermediate cells.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SQRT](SQRT.md) | Square root of a number without the pi multiplication. |
| [PI](PI.md) | Returns the value of pi used inside SQRTPI. |
| [POWER](POWER.md) | Raises a number to any power, such as 0.5 for a square root. |
| [ROUND](ROUND.md) | Trims SQRTPI results to a fixed number of decimal places. |
| [GAMMA](../Statistical/GAMMA.md) | Gamma function, where SQRTPI often appears in approximations. |

## Official Documentation

- [Microsoft Support: SQRTPI function](https://support.microsoft.com/en-us/excel/functions/sqrtpi-function)
- [Google Docs Editors Help: SQRTPI](https://support.google.com/docs/answer/3093579)
