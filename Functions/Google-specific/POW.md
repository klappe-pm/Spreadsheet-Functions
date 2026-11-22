---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Arithmetic Operations
use-case:
  - Compound Growth Factors
  - Square Area Scaling
related:
  - EXP
  - MULTIPLY
  - POWER
  - PRODUCT
  - SQRT
level: 2
source:
  - https://support.google.com/docs/answer/3093603
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Power Operator
tags:
  - arithmetic
  - exponent
  - sheets
---

# POW

## Description

**POW** raises a base number to an exponent. `=POW(B2, C2)` returns the base in cell B2 raised to the power in cell C2. In Google Sheets, POW is equivalent to the POWER function, so the two return the same result for the same arguments.

Use POW for compound growth factors, area and volume scaling, and any calculation that repeats a multiplication. An exponent of 0.5 gives a square root, and an exponent of 2 gives a square. Fractional exponents work for positive bases.

A negative base needs a whole-number exponent. Sheets cannot return a real number for a negative base raised to a fractional power, so use an integer exponent or take the absolute value of the base first. Microsoft Excel has no POW function, so Excel users write the `^` operator or the POWER function.

## Syntax

```excel
=POW(base, exponent)
```

<!-- Image 1: Operator Syntax Anatomy. See Images/Google-specific/POW.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `base` | Yes | The number to raise to the `exponent` power. If `base` is negative, `exponent` must be an integer. |
| `exponent` | Yes | The power to raise `base` to. A fraction such as 0.5 gives a root. |

### Return Value

A number equal to `base` raised to `exponent`. The function returns an error when `base` is negative and `exponent` is not a whole number, and when either argument is text that cannot be read as a number.

## Examples

All examples use this growth table.

| Rate | Years |
| --- | --- |
| 0.05 | 10 |
| 0.04 | 5 |
| 0.06 | 8 |

### Example 1: Square Root Using a Half Power

```excel
=POW(4, 0.5)
```

**Result:** `2`

Raising 4 to the power 0.5 gives its square root.

### Example 2: Base and Exponent From Cells

```excel
=POW(1 + B3, C3)
```

**Result:** `1.21665`

Row 3 holds a rate of 0.04 over 5 years. Adding 1 to the rate gives the growth base of 1.04, and POW raises it to the fifth power, rounded here to five decimal places.

### Example 3: Whole Number Power

```excel
=POW(2, 5)
```

**Result:** `32`

Two multiplied by itself five times gives 32.

### Example 4: Negative Base With a Whole Number Exponent

```excel
=POW(-2, 3)
```

**Result:** `-8`

A negative base works when the exponent is a whole number, because the result is negative 2 times 2 times 2.

### Example 5: Growth Factor for Ten Years

```excel
=POW(1 + B2, C2)
```

**Result:** `1.62889`

With the rate of 0.05 in B2 and the 10 years in C2, the growth factor is 1.05 raised to the power 10, which is rounded here to five decimal places.

## Story Problems

### Problem 1: Savings Growth Factor

A saver expects an account to earn a fixed annual rate that compounds each year. The rate and the number of years are in columns B and C of `A1:C4`.

| Account | Annual Rate | Years |
| --- | --- | --- |
| Savings A | 0.04 | 5 |
| Savings B | 0.06 | 8 |
| Savings C | 0.05 | 10 |

**Task:** In column D, calculate the growth factor for each account, which is the amount one unit of money becomes after the stated years.

**Solution:**

```excel
=POW(1 + B2, C2)
```

Fill the formula down to D4.

**Answer:** `1.21665` for Savings A, `1.59385` for Savings B and `1.62889` for Savings C, each rounded to five decimal places. Multiplying a starting balance by the factor gives the ending balance.

<!-- Image 2: Growth Factor Worksheet. See Images/Google-specific/POW.md -->

### Problem 2: Scaling the Area of a Garden Plot

A landscaper enlarges square plots by a linear scale factor. Doubling the side length quadruples the area, so the area factor is the scale factor squared. The scale factors are in column B of `A1:B4`.

| Plot | Linear Scale |
| --- | --- |
| North | 2 |
| South | 3 |
| East | 1.5 |

**Task:** In column C, calculate the area scale factor for each plot.

**Solution:**

```excel
=POW(B2, 2)
```

Fill the formula down to C4.

**Answer:** `4`, `9` and `2.25` for North, South and East. A linear scale of 1.5 gives an area scale of 2.25.

## Use Cases

### Compound Growth Factors

**Scenario:** A planning analyst projects how a 6 percent annual increase in subscriptions compounds over eight years.

```excel
=POW(1 + B2, C2)
```

**Why It Works:** The formula returns the total multiplier for the full period. Multiplying the current figure by the factor gives the projected value without a column for each year.

### Square Area Scaling

**Scenario:** A designer scales an artwork's dimensions and needs the change in area for printing costs.

```excel
=POW(B2, 2)
```

**Why It Works:** Area grows with the square of the linear scale, so POW with exponent 2 gives the area multiplier directly.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error with a negative base | The base is negative and the exponent is a fraction. | Use a whole-number exponent, or apply ABS to the base. |
| Error in place of a number | An argument is text, such as a number stored as text. | Convert the text with VALUE or retype the cell as a number. |
| Unexpected large result | The exponent was typed as a percentage, such as 5 instead of 0.05 for a rate. | Enter rates as decimals, or divide by 100 first. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use the `^` operator, for example `=B2^C2`, or the POWER function. |
| Google Sheets | Available | Equivalent to POWER. |

## Tips and Best Practices

- Enter rates as decimals, so 0.05 means 5 percent, and build growth factors as 1 plus the rate.
- Use POW with exponent 0.5 for a square root when a reviewer expects a named function, or SQRT for the same result.
- Round growth factors only at the end of a calculation, so small rounding errors do not compound.
- When the base can be negative, check the sign before choosing a fractional exponent.

## Related Functions

| Function | Relationship |
| --- | --- |
| [POWER](../Math%20%26%20Trig/POWER.md) | Equivalent to POW in Google Sheets. |
| [EXP](../Math%20%26%20Trig/EXP.md) | Raises the constant e to a power. |
| [SQRT](../Math%20%26%20Trig/SQRT.md) | Returns the square root of a number. |
| [MULTIPLY](MULTIPLY.md) | Multiplies two numbers, which is repeated multiplication for a whole-number exponent. |
| [PRODUCT](../Math%20%26%20Trig/PRODUCT.md) | Multiplies a list of numbers together. |

## Official Documentation

- [Google Docs Editors Help: POW](https://support.google.com/docs/answer/3093603)
