---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bessel Functions
purpose:
  - Special Functions
use-case:
  - Stress Field Analysis
  - Wave Boundary Modeling
related:
  - BESSELI
  - BESSELJ
  - BESSELK
  - ERF
  - ERFC
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/bessely-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Weber Function
  - Neumann Function
tags:
  - bessel-function
  - engineering
  - excel
  - special-functions
---

# BESSELY

## Description

**BESSELY** returns the Bessel function of the second kind, Yn(x), for a number x and an integer order n.
The function is also called the Weber or Neumann function. It is singular at zero and oscillates for larger x, with negative values as well as positive ones.
It appears in models of circular and cylindrical boundary problems, where it is combined with the first-kind function.

Use BESSELY when a model needs the ordinary Bessel function of the second kind at a known order.
For the ordinary function of the first kind, use BESSELJ. For the modified functions, use BESSELI or BESSELK.

The order n is truncated to an integer, so a fraction is cut off rather than rounded. A negative order returns `#NUM!`.
BESSELY is an Excel function. Google Sheets does not list it, so workbooks shared with Sheets users need another method.

## Syntax

```excel
=BESSELY(x, n)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/BESSELY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The number at which the function is evaluated. Use a positive value, because the function is not defined at zero. |
| `n` | Yes | The order of the function, 0 or greater. Any fraction is cut off rather than rounded. |

### Return Value

A number: the Bessel function Yn(x), which can be negative. The function returns `#VALUE!` when x or n is not numeric and `#NUM!` when n is less than 0.

## Examples

### Example 1: Order Zero at a Point

```excel
=BESSELY(3, 0)
```

**Result:** `0.376850`

This is the zero-order function at x equal to 3, rounded to six decimal places.
The positive result shows that Yn can change sign, so a model should never assume the value is always positive.

### Example 2: Negative Result

```excel
=BESSELY(1.5, 1)
```

**Result:** `-0.412309`

The first-order function is negative at x equal to 1.5, rounded to six decimal places.
Check the sign of the result before using it as a magnitude.

### Example 3: Filled Down a Column

Radii in `A2:A4` are 0.5, 4 and 5, and the order is 0.

```excel
=BESSELY(A2, 0)
```

Fill the formula down to `B4`.

**Result:** `-0.444519` (A2), `-0.016941` (A3), `-0.308518` (A4)

All three values are negative, so the sign pattern in a table is worth reviewing before it is charted.

<!-- Image 2: Second Kind Curves. See Images/Engineering/BESSELY.md -->

### Example 4: Non-Integer Order Is Truncated

```excel
=BESSELY(2, 0.7)
```

**Result:** `0.510376`

The order 0.7 is cut to 0, so the result equals `=BESSELY(2, 0)`.
Enter integer orders directly in shared models so the truncation is visible.

## Story Problems

### Problem 1: Stress Readings in a Cylinder

A materials lab records a zero-order factor at three radii in a cylindrical test piece. The radii are in column A, and the lab needs the total of the three readings.

| Position | Radius |
| --- | --- |
| T1 | 1 |
| T2 | 2 |
| T3 | 2.5 |

**Task:** Put `=BESSELY(B2, 0)` in `C2`, fill it down to `C4`, then add the three values.

**Solution:**

```excel
=SUM(C2:C4)
```

**Answer:** `1.0967`, from 0.088257 + 0.510376 + 0.498070 = 1.096703, rounded to four decimal places.

<!-- Image 3: Results Panel for the Story Problems. See Images/Engineering/BESSELY.md -->

### Problem 2: Which Reading Is Negative

A reviewer has two readings, one of the second-order function at x equal to 3 and one of the first-order function at x equal to 4, and must report the one that is negative.

| Reading | x | Order |
| --- | --- | --- |
| Reading A | 3 | 2 |
| Reading B | 4 | 1 |

**Task:** Calculate both values and identify the negative one.

**Solution:**

```excel
=BESSELY(B2, C2)
```

**Answer:** `-0.160400` for Reading A. Reading B is positive, at about 0.397926, so Reading A is the negative value.

## Use Cases

### Stress Field Analysis

**Scenario:** An engineer tabulates the zero-order second-kind factor at several radii to check where the field changes sign.

```excel
=BESSELY(Table1[Radius], 0)
```

**Why It Works:** The function returns one value per radius, so the sign change is visible down the column.
Use a conditional format on negative values to make the crossing easy to spot.

### Wave Boundary Modeling

**Scenario:** A modeler compares the first-order second-kind term with the first-order first-kind term at the same radius.

```excel
=BESSELY(B2, 1) - BESSELJ(B2, 1)
```

**Why It Works:** Placing both terms in one formula shows the combined boundary contribution in a single cell.
Confirm that the two functions use the same radius units before subtracting.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `x` or `n` is text, blank or a formula that returns text. | Convert the input to a number or reference a numeric cell. |
| `#NUM!` | The order `n` is less than 0, or `x` is not a valid positive input. | Use an order of 0 or greater and a positive x. |
| Unexpected sign | A negative result was read as a magnitude. | Keep the sign in the calculation and interpret it in context. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019, Excel 2016 and Excel 2019 for Mac | Order is truncated, not rounded. Dynamic array behavior applies in current versions. |
| Google Sheets | Not available | Closest alternative: write an Apps Script custom function, or compute the value in a separate tool and paste it into the sheet. |

## Tips and Best Practices

- Enter the order as an integer in a labeled input cell so the model is easy to audit.
- Check the function against a known value such as `=BESSELY(3, 0)` before trusting a new table.
- Keep radii positive and add a validation rule that rejects zero and negative values.
- Read the sign of each result before rounding or formatting, because a display format can hide negative values.
- Pair BESSELY with BESSELJ when a model needs both ordinary solutions.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BESSELI](BESSELI.md) | Modified Bessel function of the first kind. |
| [BESSELJ](BESSELJ.md) | Ordinary Bessel function of the first kind, the companion to BESSELY. |
| [BESSELK](BESSELK.md) | Modified Bessel function of the second kind. |
| [ERF](ERF.md) | Error function, another special function used in the same kinds of models. |
| [ERFC](ERFC.md) | Complementary error function, the companion to ERF. |

## Official Documentation

- [Microsoft Support: BESSELY function](https://support.microsoft.com/en-us/excel/functions/bessely-function)
