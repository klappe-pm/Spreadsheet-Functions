---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Hyperbolic
purpose:
  - Trigonometry
use-case:
  - Cable Sag Modeling
  - Hyperbolic Curve Analysis
  - Symmetry Checks
related:
  - COSH
  - COT
  - CSCH
  - SECH
  - SINH
  - TANH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/coth-function
  - https://support.google.com/docs/answer/9084102
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Hyperbolic Cotangent
tags:
  - excel
  - hyperbolic
  - reciprocal-trig
  - sheets
---

# COTH

## Description

**COTH** returns the hyperbolic cotangent of a real number. The hyperbolic cotangent is the reciprocal of the hyperbolic tangent, so `COTH(x)` gives the same result as `1/TANH(x)`. Use it in formulas built from hyperbolic functions, rather than in formulas that use ordinary angles.

The input is a plain number. It is not an angle, so no conversion to radians or degrees applies. Microsoft limits the absolute value of the input to less than 2^27, and returns `#NUM!` for larger values. Google Sheets returns `#DIV/0!` when the input is 0, so guard that case in workbooks that can produce a zero.

For circular angles, use COT instead.

## Syntax

```excel
=COTH(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/COTH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | Any real number whose absolute value is less than 2^27. Google Sheets names this argument `value`. |

### Return Value

A number: the hyperbolic cotangent of the input. The function returns `#NUM!` when the absolute value of the input is 2^27 or greater, and `#VALUE!` when the input is not numeric.

## Examples

### Example 1: Hyperbolic Cotangent of Two

```excel
=COTH(2)
```

**Result:** `1.03731`

The value is 1 divided by the hyperbolic tangent of 2.

### Example 2: Value From a Cell

Cell A2 holds `1`.

```excel
=COTH(A2)
```

**Result:** `1.31304`

The result is rounded here to five decimal places.

### Example 3: Negative Input

```excel
=COTH(-1)
```

**Result:** `-1.31304`

The hyperbolic cotangent is an odd function, so the result for -1 is the negative of the result for 1.

<!-- Image 2: Odd Symmetry of COTH. See Images/Math & Trig/COTH.md -->

### Example 4: Larger Input

```excel
=COTH(4)
```

**Result:** `1.00067`

As the input grows, the hyperbolic cotangent approaches 1.

### Example 5: Reciprocal of the Hyperbolic Tangent

```excel
=1/TANH(2)
```

**Result:** `1.03731`

This matches Example 1, which shows the reciprocal relationship with TANH.

## Story Problems

### Problem 1: Cable Sag Index

An engineer records three sample index values in column B. The report needs the total of their hyperbolic cotangents.

| Sample | Index |
| --- | --- |
| Sample A | 1 |
| Sample B | 2 |
| Sample C | 4 |

**Task:** Add the hyperbolic cotangents of the three index values in one formula.

**Solution:**

```excel
=SUMPRODUCT(COTH(B2:B4))
```

**Answer:** `3.35102`. The three values are 1.31304, 1.03731 and 1.00067, which add to 3.35102.

### Problem 2: Symmetry Check

A reviewer enters a negative test input and wants to know how its result compares with the positive input of the same size.

| Test | Input |
| --- | --- |
| Negative test | -2 |

**Task:** Compute the hyperbolic cotangent of the input in B2 and explain the sign.

**Solution:**

```excel
=COTH(B2)
```

**Answer:** `-1.03731`. The result is negative because the hyperbolic cotangent of -2 equals the negative of the hyperbolic cotangent of 2.

## Use Cases

### Cable Sag Modeling

**Scenario:** A cable design sheet stores several index values in a table named Samples. The total of their hyperbolic cotangents feeds a summary cell.

```excel
=SUMPRODUCT(COTH(Samples[Index]))
```

**Why It Works:** SUMPRODUCT evaluates COTH across the whole column. Keep the index values within the valid range, because a value of 2^27 or greater returns `#NUM!`.

### Hyperbolic Curve Analysis

**Scenario:** An analyst compares two hyperbolic curve parameters in adjacent cells and needs the difference between their hyperbolic cotangents.

```excel
=COTH(B2)-COTH(C2)
```

**Why It Works:** Both values are calculated from the same function, so the difference shows how sensitive the curve is to the parameter change. Confirm that neither input is 0.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | The input is 0 in Google Sheets. | Use `=IF(A2=0,"",COTH(A2))` to skip zero inputs. |
| `#NUM!` | The absolute value of the input is 2^27 or greater. | Check the source value for a data entry mistake. |
| `#VALUE!` | The input is text or another non-numeric value. | Check the source cell, or convert the text to a number. |
| Unexpected result | The formula uses an angle in degrees. | COTH is for hyperbolic inputs. Use COT for circular angles. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in the Math and trigonometry group. | The argument is named `number`. |
| Google Sheets | Available | The argument is named `value`. Google Sheets documents a zero input as returning `#DIV/0!`. |

## Tips and Best Practices

- Use COTH only for hyperbolic models. Circular angles belong in COT.
- Guard against zero inputs with IF when zero can occur.
- Add a check column with `1/TANH` when a workbook must confirm the reciprocal relationship.
- Keep the input in its natural units, because hyperbolic functions do not take degree conversions.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COSH](COSH.md) | The hyperbolic cosine, used with SINH and TANH in hyperbolic formulas. |
| [COT](COT.md) | The circular cotangent, for angles in radians. |
| [CSCH](CSCH.md) | The hyperbolic cosecant, the reciprocal of SINH. |
| [SECH](SECH.md) | The hyperbolic secant, the reciprocal of COSH. |
| [SINH](SINH.md) | The hyperbolic sine, the function used in the cosecant ratio. |
| [TANH](TANH.md) | The hyperbolic tangent, whose reciprocal COTH returns. |

## Official Documentation

- [Microsoft Support: COTH function](https://support.microsoft.com/en-us/excel/functions/coth-function)
- [Google Docs Editors Help: COTH](https://support.google.com/docs/answer/9084102)
