---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bessel Functions
purpose:
  - Special Functions
use-case:
  - Cylindrical Heat Flow
  - Radial Field Modeling
related:
  - BESSELJ
  - BESSELK
  - BESSELY
  - ERF
  - ERFC
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/besseli-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Modified Bessel Function
tags:
  - bessel-function
  - engineering
  - excel
  - special-functions
---

# BESSELI

## Description

**BESSELI** returns the modified Bessel function of the first kind, In(x), for a number x and an integer order n.
The modified function equals the ordinary Bessel function evaluated at purely imaginary arguments, so its values grow as x increases instead of oscillating.
Engineers and physicists use it in models of heat conduction in cylinders and of fields that vary with distance from a center line.

Use BESSELI when a model calls for the modified function of the first kind at a known order.
For the ordinary Bessel function of the first kind, use BESSELJ. For the modified function of the second kind, use BESSELK.

The order n is truncated to an integer, not rounded, so 1.9 behaves as 1. A negative order returns `#NUM!`.
BESSELI is an Excel function. Google Sheets does not offer it, so workbooks that must open in both products need a different approach for these values.

## Syntax

```excel
=BESSELI(x, n)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/BESSELI.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The number at which the function is evaluated. It can be negative, zero or positive. |
| `n` | Yes | The order of the function. A value of 0 or greater. Any fraction is cut off, so 2.7 is treated as 2. |

### Return Value

A number: the modified Bessel function In(x). The function returns `#VALUE!` when x or n is not numeric and `#NUM!` when n is less than 0.

## Examples

### Example 1: Value at a Single Point

```excel
=BESSELI(2, 0)
```

**Result:** `2.279585`

This is the order 0 modified function at x equal to 2, rounded to six decimal places.
Order 0 is the most common case in practice, so it is a good first check when a model is built.

### Example 2: Value at Zero

```excel
=BESSELI(0, 0)
```

**Result:** `1`

For order 0, the function equals 1 at x equal to 0.
For any order above 0, the same input returns 0, which is a quick way to confirm the order argument is set as intended.

### Example 3: Filled Down a Column

Radii in `A2:A4` are 0.5, 1 and 2.

```excel
=BESSELI(A2, 0)
```

Fill the formula down to `B4`.

**Result:** `1.063483` (A2), `1.266066` (A3), `2.279585` (A4)

Each row is evaluated separately, so the same formula serves a whole table of inputs.

<!-- Image 2: Modified Bessel Curves. See Images/Engineering/BESSELI.md -->

### Example 4: Non-Integer Order Is Truncated

```excel
=BESSELI(1.5, 1.9)
```

**Result:** `0.981666`

The order 1.9 is cut to 1, so the result equals `=BESSELI(1.5, 1)`.
Enter integer orders directly when the model is shared with others, so the truncation is not a surprise to the next reader.

## Story Problems

### Problem 1: Radial Readings From a Test Coil

A lab records a dimensionless factor at three distances from the center of a cylindrical test coil. The distances are in column A, and the lab needs the sum of the zero-order modified Bessel values at those points.

| Position | Radius |
| --- | --- |
| P1 | 1.5 |
| P2 | 2.5 |
| P3 | 3 |

**Task:** Put `=BESSELI(B2, 0)` in `C2`, fill it down to `C4`, then total the three values.

**Solution:**

```excel
=SUM(C2:C4)
```

**Answer:** `9.8174`, from 1.646723 + 3.289839 + 4.880793 = 9.817355, rounded to four decimal places.

<!-- Image 3: Results Panel for the Story Problems. See Images/Engineering/BESSELI.md -->

### Problem 2: Comparing Two Orders at the Same Point

A technician needs the first-order modified value at x equal to 2 and must report whether it is larger than the zero-order value at the same point.

| Quantity | Value |
| --- | --- |
| x | 2 |
| Order | 1 |

**Task:** Calculate the first-order value, then state whether the zero-order value at x equal to 2 (about 2.279585) is larger.

**Solution:**

```excel
=BESSELI(2, 1)
```

**Answer:** `1.590637`. The zero-order value at the same point is larger, at about 2.2796, so the order 0 curve sits above the order 1 curve at x equal to 2.

## Use Cases

### Cylindrical Heat Flow

**Scenario:** A thermal analyst estimates how a radial temperature term changes across the rows of a table that lists radii for a heated rod.

```excel
=BESSELI(Table1[Radius], 0)
```

**Why It Works:** Excel returns one value per row in a dynamic array, so the whole column is evaluated without copying the formula.
Keep the radii in the same units as the model, because the function does not scale them.

### Radial Field Modeling

**Scenario:** A field model needs the first-order modified value at several radii, and the modeler wants the results beside the inputs for review.

```excel
=BESSELI(B2:B20, 1)
```

**Why It Works:** Placing the formula in the first output cell spills the results downward when the workbook uses dynamic arrays.
In older Excel versions, fill the formula down to each row instead.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `x` or `n` is text, blank or a formula that returns text. | Convert the input to a number or reference a numeric cell. |
| `#NUM!` | The order `n` is less than 0. | Use an order of 0 or greater. |
| Unexpected value | A fractional order was entered and quietly cut to an integer. | Enter the integer order the model needs. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Order is truncated, not rounded. Dynamic array behavior applies in current versions. |
| Google Sheets | Not available | Closest alternative: build the series sum with SUMPRODUCT and FACT, or write an Apps Script custom function. |

## Tips and Best Practices

- Enter the order as an integer in a labeled input cell so the model is easy to audit.
- Compare results against a known value such as `=BESSELI(0, 0)`, which should return 1, before trusting a new table.
- Keep the units of `x` consistent with the rest of the model, because the function works on the number alone.
- Use BESSELK for the decaying companion solution when a model needs both kinds of modified function.
- Wrap the formula in `IFERROR` only after the inputs are validated, so a negative order is not hidden.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BESSELJ](BESSELJ.md) | Ordinary Bessel function of the first kind, which oscillates. |
| [BESSELK](BESSELK.md) | Modified Bessel function of the second kind, which decays as x grows. |
| [BESSELY](BESSELY.md) | Ordinary Bessel function of the second kind. |
| [ERF](ERF.md) | Error function, another special function used in the same kinds of models. |
| [ERFC](ERFC.md) | Complementary error function, the companion to ERF. |

## Official Documentation

- [Microsoft Support: BESSELI function](https://support.microsoft.com/en-us/excel/functions/besseli-function)
