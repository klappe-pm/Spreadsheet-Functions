---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bessel Functions
purpose:
  - Special Functions
use-case:
  - Vibration Analysis
  - Wave Pattern Modeling
related:
  - BESSELI
  - BESSELK
  - BESSELY
  - ERF
  - ERFC
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/besselj-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bessel Function of the First Kind
tags:
  - bessel-function
  - engineering
  - excel
  - special-functions
---

# BESSELJ

## Description

**BESSELJ** returns the Bessel function of the first kind, Jn(x), for a number x and an integer order n.
Unlike its modified cousins, the ordinary function oscillates: it rises, crosses zero, and falls again as x increases.
That pattern shows up in the vibration of circular membranes, in wave propagation in cylindrical geometry and in diffraction problems.

Use BESSELJ when a model needs the ordinary Bessel function of the first kind at a known order.
For the modified function of the first kind, use BESSELI. For the second kind, use BESSELY (ordinary) or BESSELK (modified).

The order n is truncated to an integer, so a fractional order such as 2.8 is treated as 2. A negative order returns `#NUM!`.
BESSELJ is an Excel function. Google Sheets does not list it, so workbooks shared with Sheets users need another method for these values.

## Syntax

```excel
=BESSELJ(x, n)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/BESSELJ.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The number at which the function is evaluated. Zero and negative values are allowed. |
| `n` | Yes | The order of the function, 0 or greater. Any fraction is cut off rather than rounded. |

### Return Value

A number: the Bessel function Jn(x). The function returns `#VALUE!` when x or n is not numeric and `#NUM!` when n is less than 0.

## Examples

### Example 1: Order Zero at a Single Point

```excel
=BESSELJ(3, 0)
```

**Result:** `-0.260052`

This is the zero-order function at x equal to 3, rounded to six decimal places.
A negative result is normal for the ordinary function, which is why the sign matters when a model compares values.

### Example 2: Value at Zero

```excel
=BESSELJ(0, 2)
```

**Result:** `0`

For any order above 0, the function equals 0 at x equal to 0.
For order 0, the same input returns 1, so the order argument is easy to check with this input.

### Example 3: Filled Down a Column

Radii in `A2:A4` are 0.5, 1 and 1.5.

```excel
=BESSELJ(A2, 1)
```

Fill the formula down to `B4`.

**Result:** `0.242268` (A2), `0.440051` (A3), `0.557937` (A4)

Each row is evaluated on its own, so one formula covers a whole list of inputs.

<!-- Image 2: Ordinary Bessel Curves. See Images/Engineering/BESSELJ.md -->

### Example 4: Non-Integer Order Is Truncated

```excel
=BESSELJ(2.2, 2.9)
```

**Result:** `0.395059`

The order 2.9 is cut to 2, so the result equals `=BESSELJ(2.2, 2)`.
Write the integer order directly in shared models so the truncation does not surprise a later reader.

## Story Problems

### Problem 1: Drum Head Response

A workshop records a first-order response for a circular drum head at three radial positions. The radii are in column A, and the team needs the total of the three readings.

| Position | Radius |
| --- | --- |
| R1 | 2 |
| R2 | 3 |
| R3 | 4 |

**Task:** Put `=BESSELJ(B2, 1)` in `C2`, fill it down to `C4`, then add the three values.

**Solution:**

```excel
=SUM(C2:C4)
```

**Answer:** `0.8497`, from 0.576725 + 0.339059 + (-0.066043) = 0.849740, rounded to four decimal places. The value at radius 4 is negative, which is the first sign change in the list.

<!-- Image 3: Results Panel for the Story Problems. See Images/Engineering/BESSELJ.md -->

### Problem 2: Finding the Zero Crossing

An analyst wants to know where the zero-order response changes sign near x equal to 2.5. Two readings are taken, one at x equal to 2.4 and one at x equal to 2.6.

| Reading | x |
| --- | --- |
| Before | 2.4 |
| After | 2.6 |

**Task:** Calculate the zero-order value at the second reading and state whether it is positive or negative.

**Solution:**

```excel
=BESSELJ(B3, 0)
```

**Answer:** `-0.096805`. The value at 2.4 is about 0.002508, which is positive, so the sign changes between the two readings.

## Use Cases

### Vibration Analysis

**Scenario:** A design team models the radial mode of a circular plate and needs the first-order response at a list of radii.

```excel
=BESSELJ(Table1[Radius], 1)
```

**Why It Works:** The function returns one value per radius in a dynamic array, so the table stays aligned with the inputs.
Scale the radius to the dimensionless form the model uses before the call, because the function does not convert units.

### Wave Pattern Modeling

**Scenario:** A modeler wants to compare the zero-order response at two frequencies stored on the same sheet.

```excel
=BESSELJ(B2, 0) - BESSELJ(C2, 0)
```

**Why It Works:** Subtracting the two results gives the difference between the responses, which is easier to read than two separate columns.
Confirm that both inputs use the same scaling before the subtraction.

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
| Google Sheets | Not available | Closest alternative: sum the power series with SUMPRODUCT and FACT for a fixed number of terms, or write an Apps Script custom function. |

## Tips and Best Practices

- Enter the order as an integer in a labeled input cell so the model is easy to audit.
- Check the function against a known point such as `=BESSELJ(0, 2)`, which should return 0, before trusting a new table.
- Expect negative values for the ordinary function, and do not wrap results in ABS unless the sign is truly irrelevant.
- Use BESSELI when the model describes growth rather than oscillation.
- Keep the units of `x` consistent with the rest of the model because the function works on the bare number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BESSELI](BESSELI.md) | Modified Bessel function of the first kind, which grows instead of oscillating. |
| [BESSELK](BESSELK.md) | Modified Bessel function of the second kind. |
| [BESSELY](BESSELY.md) | Ordinary Bessel function of the second kind, the companion to BESSELJ. |
| [ERF](ERF.md) | Error function, another special function used in the same kinds of models. |
| [ERFC](ERFC.md) | Complementary error function, the companion to ERF. |

## Official Documentation

- [Microsoft Support: BESSELJ function](https://support.microsoft.com/en-us/excel/functions/besselj-function)
