---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Hyperbolic
purpose:
  - Special Functions
  - Trigonometry
use-case:
  - Calibration Curves
  - Input Validation Checks
  - Model Inversion
related:
  - ACOTH
  - ASINH
  - ATANH
  - COSH
  - SINH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/acosh-function
  - https://support.google.com/docs/answer/3093391
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Arccosh
  - Inverse Hyperbolic Cosine
tags:
  - excel
  - hyperbolic
  - inverse-trig
  - sheets
---

# ACOSH

## Description

**ACOSH** returns the inverse hyperbolic cosine of a number. It finds the value whose hyperbolic cosine equals the input, so `ACOSH(COSH(x))` returns `x` again. The input must be greater than or equal to 1. Inputs below 1 fall outside the function's domain and return an error.

Hyperbolic functions appear in models of hanging cables, some signal and sensor curves, and certain growth and decay formulas. Use ACOSH when a model gives you the hyperbolic cosine and you need the underlying variable. For circular angles, use `ACOS` instead, which takes inputs from -1 to 1.

Google Sheets and Excel both support real inputs only. Imaginary and complex results are not available in either platform.

## Syntax

```excel
=ACOSH(number)
```

<!-- Image 1: Hyperbolic Cosine Curve and Its Inverse. See Images/Math & Trig/ACOSH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A real number greater than or equal to 1. A cell reference or a formula result is allowed. |

### Return Value

A real number: the value whose hyperbolic cosine equals `number`. An input of exactly 1 returns 0. An input below 1 returns `#NUM!` in Excel. A non-numeric input returns `#VALUE!`.

## Examples

### Example 1: Lower Boundary

```excel
=ACOSH(1)
```

**Result:** `0`

The hyperbolic cosine of 0 is 1, so this is the smallest valid input and its inverse is zero.

### Example 2: A Typical Value

```excel
=ACOSH(10)
```

**Result:** `2.993223`

The result is rounded to six decimal places for display.

### Example 3: Input From a Cell

Calibration reading in `A2` is 2.5.

```excel
=ACOSH(A2)
```

**Result:** `1.566799`

The formula returns the model input that produces the reading in `A2`.

### Example 4: Round Trip Through COSH

Input in `A2` is 0.75.

```excel
=ACOSH(COSH(A2))
```

**Result:** `0.75`

Applying `COSH` and then `ACOSH` returns the original value, which is a quick check that the inverse is set up correctly.

### Example 5: Guarding the Domain

Reading in `B2` is 0.5.

```excel
=IFERROR(ACOSH(B2),"Below 1")
```

**Result:** `Below 1`

An input below 1 is outside the domain, so `IFERROR` returns a label instead of an error.

## Story Problems

### Problem 1: Sensor Calibration Inversion

A sensor's output follows a hyperbolic cosine curve. The three readings below must be converted back to the model input.

| Sensor | Reading |
| --- | --- |
| S-1 | 1.0 |
| S-2 | 2.5 |
| S-3 | 5.0 |

**Task:** Convert each reading to the model input.

**Solution:**

```excel
=ACOSH(B2)
```

Fill the formula down from `C2`.

**Answer:** S-1 returns `0`, S-2 returns `1.566799` and S-3 returns `2.292432`. Each value is the input that produces the reading in column B.

<!-- Image 2: Readings and Recovered Inputs. See Images/Math & Trig/ACOSH.md -->

### Problem 2: Checking Readings Before Conversion

A quality team receives three readings. Only readings of 1 or more can be converted.

| Reading |
| --- |
| 0.8 |
| 1.2 |
| 3.0 |

**Task:** Count how many readings can be passed to ACOSH.

**Solution:**

```excel
=COUNTIF(A2:A4,">=1")
```

**Answer:** `2`. The readings 1.2 and 3.0 are valid. The reading 0.8 is below the domain and must be corrected or excluded.

## Use Cases

### Calibration Curves

**Scenario:** A lab records a hyperbolic response from a sensor and needs the input that produced each measurement.

```excel
=ACOSH(Reading)
```

**Why It Works:** The sensor model is inverted cell by cell. Keep the readings at 1 or above, because lower values have no real inverse.

### Input Validation Checks

**Scenario:** A data import includes readings that may fall below the valid range, and the workbook must flag them before conversion.

```excel
=IF(B2>=1,ACOSH(B2),"Check reading")
```

**Why It Works:** The `IF` test stops invalid values from reaching ACOSH, so the column stays free of errors.

### Model Inversion

**Scenario:** A planning model gives a hyperbolic ratio, and the analyst needs the matching input for a scenario table.

```excel
=ROUND(ACOSH(Ratio),3)
```

**Why It Works:** `ROUND` keeps the scenario table readable without changing the calculation.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is less than 1. | Check the input and keep values at 1 or above. |
| `#VALUE!` | The input is text that cannot be read as a number. | Convert the cell to a number. |
| Result looks like a circular angle | The user expected a value from `ACOS`. | Use `ACOS` for angles and `ACOSH` for hyperbolic inputs. |
| `#NAME?` | The function name is misspelled. | Type `ACOSH`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Real inputs only. The return value is a real number. |
| Google Sheets | Available | Same argument. Imaginary and complex numbers are not supported. |

## Tips and Best Practices

- Validate inputs before calling ACOSH, because a single value below 1 produces an error in a whole column of results.
- Use `ACOSH(COSH(x))` to test that a model and its inverse agree.
- Use `ACOS` for circular angles, which accept inputs from -1 to 1.
- Document the domain in a note next to the input column so future editors do not enter values below 1.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COSH](COSH.md) | Hyperbolic cosine. ACOSH is its inverse for values of 1 or more. |
| [SINH](SINH.md) | Hyperbolic sine. Pair it with ASINH when the same model uses sine. |
| [ASINH](ASINH.md) | Inverse hyperbolic sine. Accepts any real number. |
| [ATANH](ATANH.md) | Inverse hyperbolic tangent. Accepts inputs between -1 and 1. |
| [ACOTH](ACOTH.md) | Inverse hyperbolic cotangent. Accepts values with an absolute value above 1. |

## Official Documentation

- [Microsoft Support: ACOSH function](https://support.microsoft.com/en-us/excel/functions/acosh-function)
- [Google Docs Editors Help: ACOSH](https://support.google.com/docs/answer/3093391)
