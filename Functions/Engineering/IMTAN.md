---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
purpose:
  - Complex Numbers
use-case:
  - Filter Response Checks
  - Phase Angle Modeling
related:
  - COMPLEX
  - IMCOS
  - IMCOT
  - IMSIN
  - IMTANH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/imtan-function
  - https://support.google.com/docs/answer/9203334
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Complex Tangent
tags:
  - complex-numbers
  - excel
  - sheets
  - trigonometry
---

# IMTAN

## Description

**IMTAN** returns the tangent of a complex number as text in `x+yi` or `x+yj` form. For an input `x+yi`, it computes tan(x+yi), which is a complex result with its own real and imaginary parts. A real number is treated as a complex number whose imaginary part is zero, so `IMTAN(0.25)` gives the ordinary tangent of 0.25.

Use IMTAN in engineering models where a phase angle or a sampled value is stored as a complex number and the tangent of that value is needed, such as filter or control calculations. For ordinary angles measured in radians, the regular TAN function is simpler. IMTAN is the complex-number counterpart, and IMSIN and IMCOS give the sine and cosine of the same kind of input, so the three can be combined into checks.

The tangent of a complex number is undefined at some points, and IMTAN returns an error there. Inputs that are not valid complex text also return an error. Excel documents `#NUM!` for invalid text and `#VALUE!` for a logical value, while Google Sheets describes the errors in general terms.

## Syntax

```excel
=IMTAN(inumber)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/IMTAN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `inumber` | Yes | The complex number whose tangent you want. Use text in `x+yi` or `x+yj` form, a COMPLEX result, or a real number. Google Sheets calls this argument `number`. |

### Return Value

A text string in `x+yi` or `x+yj` form that holds the tangent. The function returns `#NUM!` when the input is not in `x+yi` or `x+yj` form in Excel, and `#VALUE!` when the input is a logical value. Google Sheets returns an error for any input that is not a valid complex number.

## Examples

Results are shown rounded to ten decimal places, which is how many digits the reader needs to check the values.

### Example 1: Tangent of Complex Text

```excel
=IMTAN("1+1i")
```

**Result:** `0.2717525853+1.0839233273i`

The function evaluates tan(1+1i). The real part of the result is 0.2717525853 and the imaginary part is 1.0839233273.

### Example 2: Tangent of a Real Number

```excel
=IMTAN(0.25)
```

**Result:** `0.2553419212`

A real input has an imaginary part of zero, so the result is the ordinary tangent of 0.25 with no imaginary part shown.

### Example 3: Tangent of a COMPLEX Result

```excel
=IMTAN(COMPLEX(0.5,0.25))
```

**Result:** `0.5045007027+0.3124206925i`

COMPLEX(0.5,0.25) builds the number 0.5+0.25i, and IMTAN returns its tangent. Use COMPLEX when the real and imaginary parts sit in separate cells.

<!-- Image 2: Real and Imaginary Parts in Separate Cells. See Images/Engineering/IMTAN.md -->

### Example 4: Tangent From a Cell Reference

```excel
=IMTAN(B2)
```

**Result:** `0.0338128261-1.0147936161i` (with B2 holding `1-2i`)

Pointing to a cell lets the same formula be copied down a column of complex values. The cell must hold text in `x+yi` form or a valid complex number.

## Story Problems

### Problem 1: Phase Angle in a Filter Model

A signal engineer stores a sampled complex phase value for a filter stage in cell `B2`. The value is `2-1i`.

| Sample | Phase Value |
| --- | --- |
| Stage Input | 2-1i |

**Task:** Find the tangent of the stage phase value so the engineer can compare it with the model output.

**Solution:**

```excel
=IMTAN(B2)
```

**Answer:** `-0.2434582012-1.1667362572i`, rounded to ten decimal places.

### Problem 2: Tangent of a Real Test Angle

A calibration sheet lists one real test angle of 0.5 radians in `B2`. The technician needs the tangent of that angle to compare with a bench reading.

| Test | Angle (radians) |
| --- | --- |
| Bench Check | 0.5 |

**Task:** Find the tangent of the test angle.

**Solution:**

```excel
=IMTAN(B2)
```

**Answer:** `0.5463024898`, rounded to ten decimal places. Because the input is real, the result has no imaginary part.

## Use Cases

### Filter Response Checks

**Scenario:** A design team checks the complex response of a filter at several sample points stored in a column.

```excel
=IMTAN(FilterPoints)
```

**Why It Works:** Copy the formula down the column so each point gets its own result. Each result keeps both parts, so the team can see the real and imaginary shifts together.

### Phase Angle Modeling

**Scenario:** A control engineer models a phase value that is written as complex text in a configuration table.

```excel
=IMTAN(COMPLEX(PhaseReal, PhaseImag))
```

**Why It Works:** COMPLEX builds the value from two numeric columns, so the model can change the real and imaginary parts independently without editing text strings.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is not in `x+yi` or `x+yj` form. | Rewrite the input as text such as `2-1i`, or build it with COMPLEX. |
| Error value | The tangent is undefined for that complex value. | Check the input values and wrap the formula in IFERROR where such points can occur. |
| `#VALUE!` | The input is a logical value such as TRUE. | Enter a numeric or complex value instead. |
| Unexpected result | A radian angle was given in degrees. | Convert degrees to radians first, for example with RADIANS. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Argument name is inumber. Returns `#NUM!` for invalid text and `#VALUE!` for logical values. |
| Google Sheets | Available | Argument name is number. Accepts a COMPLEX result, a real number, or text in `x+yi` form. |

## Tips and Best Practices

- Use COMPLEX when the real and imaginary parts are separate values in the model.
- Compare IMTAN with IMSIN and IMCOS on the same input when a check is needed, because tan equals sin divided by cos.
- Set the number of decimal places with the cell format rather than rounding inside the formula, so the full value stays available.
- Wrap the formula in IFERROR to catch points where the tangent is undefined.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMPLEX](COMPLEX.md) | Builds the complex input from real and imaginary coefficients. |
| [IMCOS](IMCOS.md) | Returns the cosine of the same complex input, used in tan equals sin over cos checks. |
| [IMCOT](IMCOT.md) | Returns the cotangent, the reciprocal of IMTAN. |
| [IMSIN](IMSIN.md) | Returns the sine of the same complex input. |
| [IMTANH](IMTANH.md) | Returns the hyperbolic tangent, which uses the hyperbolic form instead of the circular one. |

## Official Documentation

- [Microsoft Support: IMTAN function](https://support.microsoft.com/en-us/excel/functions/imtan-function)
- [Google Docs Editors Help: IMTAN](https://support.google.com/docs/answer/9203334)
