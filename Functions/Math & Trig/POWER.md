---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Logarithms and Powers
purpose:
  - Arithmetic Operations
  - Financial Modeling
use-case:
  - Compound Growth Projections
  - Savings Balance Forecasts
  - Scaling Factor Calculations
related:
  - EXP
  - LN
  - LOG
  - LOG10
  - SQRT
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/power-function
  - https://support.google.com/docs/answer/3093433
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Exponent Function
  - Raise to Power
tags:
  - arithmetic
  - excel
  - exponents
  - sheets
---

# POWER

## Description

**POWER** raises a number to a power. The first argument is the base and the second is the exponent, so `=POWER(5,2)` returns 25, which is 5 squared. The function accepts any real number as the base, and the exponent can be a whole number, a fraction or a decimal. A fractional exponent works as a root: `POWER(8,1/3)` returns 2, the cube root of 8.

Use POWER when the exponent is a value in a cell or a formula, such as a number of years in a growth calculation. The caret operator (`^`) does the same job, and the official Excel page notes that you can use either. POWER reads more clearly when the base or exponent is itself a long expression, because each argument is separated by a comma.

POWER is the right choice for compound growth, scaling and area or volume calculations. For the exponential function with base e, use EXP. For logarithms, which reverse this operation, use LN, LOG or LOG10.

## Syntax

```excel
=POWER(number, power)
```

<!-- Image 1: Base and Exponent Layout. See Images/Math & Trig/POWER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The base. Any real number, including negative numbers and decimals. A cell reference or formula works. |
| `power` | Yes | The exponent that the base is raised to. Use a whole number, a fraction such as `1/3`, or a decimal. |

### Return Value

A number equal to `number` raised to the `power`. POWER returns `#VALUE!` when either argument is text that cannot be read as a number.

<!-- Image 2: Compound Growth Table. See Images/Math & Trig/POWER.md -->

## Examples

### Example 1: Square a Number

```excel
=POWER(5,2)
```

**Result:** `25`

The base 5 is raised to the exponent 2, which is the same as 5 times 5.

### Example 2: Powers of Two

```excel
=POWER(2,10)
```

**Result:** `1024`

Ten doublings of 2 produce 1024, a common value in binary and storage calculations.

### Example 3: Growth Factor for Ten Periods

```excel
=ROUND(POWER(1.05,10), 4)
```

**Result:** `1.6289`

A 5 percent growth rate applied for 10 periods multiplies the starting amount by 1.05 raised to the 10th power. The exact factor is 1.628894626777442.

### Example 4: Cube Root With a Fractional Exponent

```excel
=ROUND(POWER(8,1/3), 6)
```

**Result:** `2`

An exponent of 1/3 returns the cube root. ROUND removes any tiny floating-point difference from the displayed value.

### Example 5: Compound Balance After Four Years

The principal is in cell `B2`, the annual rate is in `B3` and the number of years is in `B4`.

```excel
=ROUND(B2*POWER(1+B3,B4), 2)
```

**Result:** `6312.38` (with 5000, 0.06 and 4 in the cells)

The formula multiplies the principal by 1 plus the rate, raised to the number of years. Interest compounds on earlier interest, which is why the balance grows faster than a simple percentage each year.

## Story Problems

### Problem 1: Savings Balance After Four Years

A family deposits $5,000 in a savings account that earns 6 percent a year, compounded annually. They want the balance after four years.

| Item | Value |
| --- | --- |
| Principal | 5000 |
| Annual Rate | 0.06 |
| Years | 4 |

**Task:** Calculate the balance at the end of four years, rounded to cents.

**Solution:**

```excel
=ROUND(B2*POWER(1+B3,B4), 2)
```

**Answer:** `6312.38`. The factor is 1.06 raised to the 4th power, which is 1.26248, and 5000 times that factor is 6312.38.

### Problem 2: Volume of a Storage Cube

A shipping crate is a cube with sides of 2.5 feet. The volume is needed to plan pallet space.

| Item | Length (feet) |
| --- | --- |
| Storage Cube | 2.5 |

**Task:** Calculate the cubic volume of the crate.

**Solution:**

```excel
=POWER(B2,3)
```

**Answer:** `15.625` cubic feet. A cube's volume is its side length raised to the 3rd power, and 2.5 cubed is 15.625.

## Use Cases

### Compound Growth Projections

**Scenario:** A finance analyst projects revenue that grows by a fixed percentage each year.

```excel
=ROUND(B2*POWER(1+C2,D2), 0)
```

**Why It Works:** The starting revenue in `B2` is multiplied by the growth factor, `1+C2`, raised to the number of years in `D2`. Keep the rate in one cell so that a scenario change updates every year.

### Savings Balance Forecasts

**Scenario:** A planner compares deposit schedules for a retirement account at different rates.

```excel
=ROUND(B2*POWER(1+B3/12,B4*12), 2)
```

**Why It Works:** Monthly compounding divides the annual rate by 12 and multiplies the number of years by 12. The formula returns the balance after the number of months in `B4 * 12`.

### Scaling Factor Calculations

**Scenario:** A designer resizes a square artwork and needs the area multiplier for printing costs.

```excel
=POWER(B2/C2, 2)
```

**Why It Works:** When a square is scaled by the ratio of the new side to the old side, its area changes by that ratio squared. Use the same units in both sides.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text, such as a number stored as text. | Convert the cell to a number, or re-enter the value. |
| `#NAME?` | The function name is misspelled. | Check the spelling of POWER. |
| Result is too large or too small | A percentage was typed as a whole number, such as 6 instead of 0.06. | Enter the rate as a decimal, or format the cell as a percentage. |
| Unexpected result | The base and exponent are swapped. | Put the base first and the exponent second, for example `POWER(3,4)` for 3 to the 4th power. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Same two arguments. The caret operator gives the same result. |
| Google Sheets | Available | Same two arguments. The official page links POWER to SQRT, EXP, LN and LOG. |

## Tips and Best Practices

- Use POWER when the exponent comes from a cell, because a cell reference is easier to audit than a caret inside a long formula.
- Enter rates as decimals or formatted percentages, never as whole numbers.
- Use ROUND on money results at the end of the formula, not on each factor.
- Write a root as `POWER(x,1/n)`, for example `POWER(27,1/3)` for a cube root.
- Use the same time unit for the rate and the exponent, such as monthly rates with a number of months.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EXP](EXP.md) | Raises the constant e to a power, a special case of exponential growth. |
| [LN](LN.md) | Natural logarithm, the inverse of EXP. |
| [LOG](LOG.md) | Logarithm to any base you specify, the inverse of POWER. |
| [LOG10](LOG10.md) | Base 10 logarithm, the inverse of raising 10 to a power. |
| [SQRT](SQRT.md) | Square root, the same as POWER with an exponent of 1/2. |

## Official Documentation

- [Microsoft Support: POWER function](https://support.microsoft.com/en-us/excel/functions/power-function)
- [Google Docs Editors Help: POWER](https://support.google.com/docs/answer/3093433)
