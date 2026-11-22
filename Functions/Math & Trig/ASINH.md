---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Hyperbolic
purpose:
  - Special Functions
  - Trigonometry
use-case:
  - Inverse Model Checks
  - Signal Normalization
  - Wide Range Data Scaling
related:
  - ACOSH
  - ASIN
  - ATANH
  - COSH
  - SINH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/asinh-function
  - https://support.google.com/docs/answer/3093393
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Arcsinh
  - Inverse Hyperbolic Sine
tags:
  - excel
  - hyperbolic
  - inverse-trig
  - sheets
---

# ASINH

## Description

**ASINH** returns the inverse hyperbolic sine of a number. It finds the value whose hyperbolic sine equals the input, so `ASINH(SINH(x))` returns `x` again. Unlike ACOSH and ATANH, ASINH accepts any real number, positive or negative, and it always returns a real result.

ASINH has a useful property for data. For small inputs it stays close to the input itself, and for large positive or negative inputs it grows slowly, like a logarithm. Analysts use it to compress values that span several orders of magnitude while keeping their sign. Zero stays zero.

Google Sheets does not support imaginary or complex numbers in hyperbolic functions, so in that application the input and result are always real.

## Syntax

```excel
=ASINH(number)
```

<!-- Image 1: Inverse Hyperbolic Sine Curve. See Images/Math & Trig/ASINH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | Any real number. A cell reference or a formula result is allowed. |

### Return Value

A real number: the value whose hyperbolic sine equals `number`. The result has the same sign as the input, and an input of 0 returns 0. Non-numeric input returns `#VALUE!`.

## Examples

### Example 1: Large Positive Input

```excel
=ASINH(10)
```

**Result:** `2.998223`

A value of 10 compresses to about 3, which shows how the function reduces large inputs.

### Example 2: Negative Input

```excel
=ASINH(-2.5)
```

**Result:** `-1.647231`

The sign is preserved, so a negative input gives a negative result.

### Example 3: Zero Input

```excel
=ASINH(0)
```

**Result:** `0`

Zero is the only input that returns zero, so the sign is unchanged.

### Example 4: Input From a Cell

Reading in `A2` is 4.

```excel
=ASINH(A2)
```

**Result:** `2.094713`

The transformed value is easier to compare with other readings that differ in size.

### Example 5: Round Trip Through SINH

Input in `A2` is 1.25.

```excel
=ASINH(SINH(A2))
```

**Result:** `1.25`

Applying `SINH` and then `ASINH` returns the original value, which confirms the inverse is set up correctly.

## Story Problems

### Problem 1: Transforming Sensor Readings

A vibration sensor reports three readings that range from small to large. The analyst applies ASINH to compress the range while keeping each sign.

| Sample | Reading |
| --- | --- |
| S-1 | 4 |
| S-2 | -2.5 |
| S-3 | 0.5 |

**Task:** Transform each reading with ASINH.

**Solution:**

```excel
=ASINH(B2)
```

Fill the formula down from `C2` to `C4`.

**Answer:** S-1 is `2.094713`, S-2 is `-1.647231` and S-3 is `0.481212`. The largest reading is now about 2.1 and the smallest positive reading is still close to its original size.

<!-- Image 2: Readings Before and After ASINH. See Images/Math & Trig/ASINH.md -->

### Problem 2: Counting Negative Transforms

After the transformation in Problem 1, the analyst needs to know how many samples remain negative.

**Task:** Count the transformed values in `C2:C4` that are below zero.

**Solution:**

```excel
=COUNTIF(C2:C4,"<0")
```

**Answer:** `1`. Only S-2 is negative, because ASINH keeps the sign of the reading it transforms.

## Use Cases

### Signal Normalization

**Scenario:** A monitoring team compares signals that vary from tiny to very large, and the report needs a scale that treats both ends fairly.

```excel
=ASINH(Signal)
```

**Why It Works:** Large values are reduced in size while small values stay close to their original numbers, so one chart can show the full range.

### Wide Range Data Scaling

**Scenario:** A research group has measurements that include negative and positive values across several orders of magnitude, and it needs them scaled before a regression.

```excel
=ASINH(Measurement/Scale)
```

**Why It Works:** Dividing by a scale value sets the units first, and ASINH then compresses the spread while the signs stay correct.

### Inverse Model Checks

**Scenario:** An analyst checks a model that applies SINH to its inputs and needs to confirm the original inputs come back.

```excel
=ROUND(ASINH(SINH(Input))-Input,10)
```

**Why It Works:** A result of 0 confirms the round trip, and `ROUND` hides tiny floating point differences.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The input is text that cannot be read as a number. | Convert the cell to a number. |
| Result has an unexpected sign | The input had a sign that was not expected. | Check the source data. ASINH keeps the sign of the input. |
| Result looks too small | The input was expected to be an angle in degrees. | ASINH is not an angle function. Use `ASIN` for circular angles. |
| `#NAME?` | The function name is misspelled. | Type `ASINH`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Accepts any real number. The Microsoft page gives the examples ASINH(10) = 2.99822295 and ASINH(-2.5) = -1.647231146. |
| Google Sheets | Available | Same argument. Imaginary and complex numbers are not supported. |

## Tips and Best Practices

- Use ASINH when data includes both positive and negative values across a wide range, because it keeps the sign while compressing large values.
- Test an inverse model with `ASINH(SINH(x))` to confirm that the model and its inverse agree.
- Label transformed columns clearly, so a reader knows the values are not in the original units.
- Use `ASIN` for circular angles, which accept inputs from -1 to 1.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SINH](SINH.md) | Hyperbolic sine. ASINH is its inverse. |
| [COSH](COSH.md) | Hyperbolic cosine. Pair it with ACOSH when a model uses cosine. |
| [ACOSH](ACOSH.md) | Inverse hyperbolic cosine. Accepts values of 1 or more. |
| [ATANH](ATANH.md) | Inverse hyperbolic tangent. Accepts values between -1 and 1. |
| [ASIN](ASIN.md) | Inverse sine for circular angles. Accepts values between -1 and 1. |

## Official Documentation

- [Microsoft Support: ASINH function](https://support.microsoft.com/en-us/excel/functions/asinh-function)
- [Google Docs Editors Help: ASINH](https://support.google.com/docs/answer/3093393)
