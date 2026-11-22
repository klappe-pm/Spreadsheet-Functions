---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Hyperbolic
purpose:
  - Special Functions
  - Trigonometry
use-case:
  - Hyperbolic Model Inversion
  - Input Domain Checks
  - Signal Decay Models
related:
  - ACOSH
  - ACOT
  - ASINH
  - ATANH
  - COTH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/acoth-function
  - https://support.google.com/docs/answer/9084097
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Arccoth
  - Inverse Hyperbolic Cotangent
tags:
  - excel
  - hyperbolic
  - inverse-trig
  - sheets
---

# ACOTH

## Description

**ACOTH** returns the inverse hyperbolic cotangent of a number. It finds the value whose hyperbolic cotangent equals the input. The result equals one half of the natural logarithm of `(x + 1) / (x - 1)`, which is why the input must lie outside the range from -1 to 1.

The valid inputs are numbers whose absolute value is greater than 1. Values of exactly 1, exactly -1, and any value between them have no real inverse, and the function returns an error for them. Negative inputs below -1 return negative results.

Use ACOTH when a hyperbolic model gives you the cotangent and you need the underlying variable. For the circular version, use `ACOT`, which accepts any real number and returns an angle.

## Syntax

```excel
=ACOTH(number)
```

<!-- Image 1: Valid and Invalid Input Ranges. See Images/Math & Trig/ACOTH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A real number whose absolute value is greater than 1. A cell reference or a formula result is allowed. |

### Return Value

A real number. For inputs above 1 the result is positive, and for inputs below -1 the result is negative. Inputs between -1 and 1, inclusive, return `#NUM!`. A non-numeric input returns `#VALUE!`.

## Examples

### Example 1: Positive Input

```excel
=ACOTH(6)
```

**Result:** `0.168236`

This equals one half of the natural log of 7 divided by 5.

### Example 2: Negative Input Below -1

```excel
=ACOTH(-4)
```

**Result:** `-0.255413`

The absolute value is 4, which is greater than 1, so the result is valid and negative.

### Example 3: Input From a Cell

Model output in `A2` is 3.

```excel
=ACOTH(A2)
```

**Result:** `0.346574`

The result is one half of the natural log of 2.

### Example 4: Input Close to 1

Model output in `A2` is 1.1.

```excel
=ACOTH(A2)
```

**Result:** `1.522261`

Values close to 1 produce much larger results, because the function grows without limit as the input approaches 1 from above.

### Example 5: Guarding the Domain

Reading in `B2` is 0.5.

```excel
=IFERROR(ACOTH(B2),"Out of domain")
```

**Result:** `Out of domain`

A value of 0.5 lies between -1 and 1, so `IFERROR` returns a label instead of an error.

## Story Problems

### Problem 1: Hyperbolic Calibration Values

A test rig reports three hyperbolic cotangent values for a material. The model needs the underlying variable for each.

| Test | Coth Reading |
| --- | --- |
| T-1 | 6 |
| T-2 | -4 |
| T-3 | 3 |

**Task:** Convert each reading with ACOTH.

**Solution:**

```excel
=ACOTH(B2)
```

Fill the formula down from `C2`.

**Answer:** T-1 is `0.168236`, T-2 is `-0.255413` and T-3 is `0.346574`. Each reading lies outside the range from -1 to 1, so each has a valid result.

### Problem 2: Counting Valid Readings

A lab receives four readings. Only readings whose absolute value exceeds 1 can be converted.

| Reading |
| --- |
| 0.5 |
| 2 |
| -1.5 |
| 0.9 |

**Task:** Count the readings that ACOTH can convert.

**Solution:**

```excel
=SUMPRODUCT(--(ABS(A2:A5)>1))
```

**Answer:** `2`. The readings 2 and -1.5 are valid. The readings 0.5 and 0.9 lie between -1 and 1 and must be reviewed.

<!-- Image 2: Hyperbolic Cotangent Curve. See Images/Math & Trig/ACOTH.md -->

## Use Cases

### Hyperbolic Model Inversion

**Scenario:** A materials team has a model that reports a hyperbolic cotangent, and it needs the matching variable for each sample.

```excel
=ACOTH(Sample)
```

**Why It Works:** Each sample is inverted in its own row. Confirm that every sample is outside the range from -1 to 1 before the column is used.

### Input Domain Checks

**Scenario:** An import contains model outputs that may fall inside the invalid range, and the workbook must flag them before any conversion.

```excel
=IF(ABS(B2)>1,ACOTH(B2),"Review input")
```

**Why It Works:** The `IF` test checks the absolute value, so negative valid inputs pass and inputs between -1 and 1 are flagged.

### Signal Decay Models

**Scenario:** An engineer estimates a decay parameter from a measured hyperbolic ratio and needs the parameter rounded for a report.

```excel
=ROUND(ACOTH(Ratio),4)
```

**Why It Works:** `ROUND` fixes the number of decimal places in the report without changing the calculation.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The absolute value of the input is 1 or less. | Check the input range and keep the absolute value above 1. |
| `#VALUE!` | The input is text that cannot be read as a number. | Convert the cell to a number. |
| Result looks like an angle | The user expected a value from `ACOT`. | Use `ACOT` for circular angles and `ACOTH` for hyperbolic inputs. |
| `#NAME?` | The function name is misspelled. | Type `ACOTH`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Inputs must satisfy an absolute value above 1. The Microsoft page gives both `#NUM!` and `#VALUE!` for inputs between -1 and 1, so test that case in your version of Excel. |
| Google Sheets | Available | Inputs between -1 and 1 return `#NUM!`. Imaginary and complex numbers are not supported. |

## Tips and Best Practices

- Validate the input before calling ACOTH, because a single value between -1 and 1 creates an error in its row.
- Use `ABS(x)>1` as the validation test, since it accepts negative inputs below -1.
- Confirm that a result is correct by applying `COTH` to it and checking that the original input returns.
- Label the input column with its valid range so future editors do not enter values inside the invalid band.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COTH](COTH.md) | Hyperbolic cotangent. ACOTH is its inverse. |
| [ACOT](ACOT.md) | Circular inverse cotangent. Accepts any real number and returns an angle. |
| [ACOSH](ACOSH.md) | Inverse hyperbolic cosine. Accepts values of 1 or more. |
| [ATANH](ATANH.md) | Inverse hyperbolic tangent. Accepts values between -1 and 1. |
| [ASINH](ASINH.md) | Inverse hyperbolic sine. Accepts any real number. |

## Official Documentation

- [Microsoft Support: ACOTH function](https://support.microsoft.com/en-us/excel/functions/acoth-function)
- [Google Docs Editors Help: ACOTH](https://support.google.com/docs/answer/9084097)
