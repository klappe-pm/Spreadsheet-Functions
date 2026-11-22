---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bessel Functions
purpose:
  - Special Functions
use-case:
  - Heat Transfer Modeling
  - Radial Decay Analysis
related:
  - BESSELI
  - BESSELJ
  - BESSELY
  - ERF
  - ERFC
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/besselk-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Modified Bessel Function of the Second Kind
tags:
  - bessel-function
  - engineering
  - excel
  - special-functions
---

# BESSELK

## Description

**BESSELK** returns the modified Bessel function of the second kind, Kn(x), for a number x and an integer order n.
It is defined for positive x and decays as x increases, which makes it useful where a quantity must fall away from a source.
In practice it appears in heat flow from thin wires, in radial decay problems and in some diffusion models.

Use BESSELK when a model needs the decaying modified solution at a known order.
For the growing modified solution of the first kind, use BESSELI. For the ordinary function of the second kind, use BESSELY.

The order n is truncated to an integer, so 2.9 behaves as 2. A negative order returns `#NUM!`.
BESSELK is an Excel function. Google Sheets does not list it, so Sheets users need another route to these values.

## Syntax

```excel
=BESSELK(x, n)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/BESSELK.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The number at which the function is evaluated. Use a positive value, because the function is not defined at zero. |
| `n` | Yes | The order of the function, 0 or greater. Any fraction is cut off rather than rounded. |

### Return Value

A number: the modified Bessel function Kn(x). The function returns `#VALUE!` when x or n is not numeric and `#NUM!` when n is less than 0.

## Examples

### Example 1: Order One at a Point

```excel
=BESSELK(0.75, 1)
```

**Result:** `0.949580`

This is the first-order function at x equal to 0.75, rounded to six decimal places.
The value falls toward zero as x grows, which is the decay the function is used to describe.

### Example 2: Higher Order at a Point

```excel
=BESSELK(3, 2)
```

**Result:** `0.061510`

The second-order function is larger than the zero-order function at the same x, because values rise with the order at a fixed x.
Use this check to confirm the order argument when several orders are compared in one sheet.

### Example 3: Filled Down a Column

Radii in `A2:A4` are 1.5, 3 and 0.25, and the order is 0.

```excel
=BESSELK(A2, 0)
```

Fill the formula down to `B4`.

**Result:** `0.213806` (A2), `0.034740` (A3), `1.541507` (A4)

The smallest radius gives the largest value, which matches the decay pattern.

<!-- Image 2: Modified Second Kind Curves. See Images/Engineering/BESSELK.md -->

### Example 4: Non-Integer Order Is Truncated

```excel
=BESSELK(2, 1.8)
```

**Result:** `0.139866`

The order 1.8 is cut to 1, so the result equals `=BESSELK(2, 1)`.
Enter integer orders directly in shared models so the truncation is visible.

## Story Problems

### Problem 1: Heat Shield Around a Thin Wire

A test team records a zero-order decay factor at three distances from a thin heated wire. The distances are in column A, and the team wants the total of the three values.

| Position | Distance |
| --- | --- |
| S1 | 0.5 |
| S2 | 1 |
| S3 | 2 |

**Task:** Put `=BESSELK(B2, 0)` in `C2`, fill it down to `C4`, then add the three results.

**Solution:**

```excel
=SUM(C2:C4)
```

**Answer:** `1.4593`, from 0.924419 + 0.421024 + 0.113894 = 1.459337, rounded to four decimal places.

<!-- Image 3: Results Panel for the Story Problems. See Images/Engineering/BESSELK.md -->

### Problem 2: Two Orders in One Check

An engineer needs the first-order value at x equal to 1.25 and the third-order value at x equal to 2.5, and wants their sum for a single comparison cell.

| Check | x | Order |
| --- | --- | --- |
| Check A | 1.25 | 1 |
| Check B | 2.5 | 3 |

**Task:** Calculate both values with BESSELK and add them.

**Solution:**

```excel
=BESSELK(B2, C2) + BESSELK(B3, C3)
```

**Answer:** `0.6704`, from 0.402124 + 0.268227 = 0.670351, rounded to four decimal places.

## Use Cases

### Heat Transfer Modeling

**Scenario:** A thermal designer tabulates the decaying modified term at several radii for a heated element and reads it beside the geometry.

```excel
=BESSELK(Table1[Radius], 0)
```

**Why It Works:** The function returns one value per radius, so the whole table is evaluated in one formula in dynamic array versions of Excel.
Keep the radii positive, because the function is not defined at zero.

### Radial Decay Analysis

**Scenario:** An analyst compares the first-order decay at two radii, one on each side of a design threshold.

```excel
=BESSELK(B2, 1) / BESSELK(C2, 1)
```

**Why It Works:** The ratio shows how quickly the function falls between the two radii, which is easier to report than two raw values.
Check that the denominator is not zero before using the ratio in a report.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `x` or `n` is text, blank or a formula that returns text. | Convert the input to a number or reference a numeric cell. |
| `#NUM!` | The order `n` is less than 0, or `x` is not a valid positive input. | Use an order of 0 or greater and a positive x. |
| Unexpected value | A fractional order was entered and quietly cut to an integer. | Enter the integer order the model needs. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Order is truncated, not rounded. Dynamic array behavior applies in current versions. |
| Google Sheets | Not available | Closest alternative: approximate the integral form with SUMPRODUCT over a fixed grid, or write an Apps Script custom function. |

## Tips and Best Practices

- Enter the order as an integer in a labeled input cell so the model is easy to audit.
- Check a known point such as `=BESSELK(2, 0)` before trusting a new table.
- Pair BESSELK with BESSELI when a model needs both modified solutions.
- Guard inputs with a positive-value check, because zero and negative x are outside the function's domain.
- Round results only at the presentation layer so the calculation keeps full precision.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BESSELI](BESSELI.md) | Modified Bessel function of the first kind, which grows with x. |
| [BESSELJ](BESSELJ.md) | Ordinary Bessel function of the first kind. |
| [BESSELY](BESSELY.md) | Ordinary Bessel function of the second kind. |
| [ERF](ERF.md) | Error function, another special function used in decay and diffusion models. |
| [ERFC](ERFC.md) | Complementary error function, the companion to ERF. |

## Official Documentation

- [Microsoft Support: BESSELK function](https://support.microsoft.com/en-us/excel/functions/besselk-function)
