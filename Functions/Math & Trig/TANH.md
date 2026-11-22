---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Hyperbolic
purpose:
  - Trigonometry
use-case:
  - Bounded Score Scaling
  - Gauge Display Scaling
related:
  - ATANH
  - COSH
  - SINH
  - TAN
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/tanh-function
  - https://support.google.com/docs/answer/3093755
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Hyperbolic Tangent
tags:
  - excel
  - hyperbolic
  - sheets
  - trigonometry
---

# TANH

## Description

**TANH** returns the hyperbolic tangent of any real number. The result always falls between -1 and 1. An input of 0 returns 0, positive inputs return values between 0 and 1, and negative inputs return values between -1 and 0. As the input grows in size, the result approaches 1 or -1 but never reaches it.

Use TANH when you need to squeeze numbers of any size into a fixed band, such as turning a large change into a score that cannot exceed 1 in either direction. Values beyond 3 are already above 0.99 or below -0.99, so large inputs add little detail once they pass that point.

Do not confuse TANH with TAN. TAN takes an angle in radians and returns the trigonometric tangent, which is not limited to a band. TANH takes a plain number and uses the exponential curve instead of the unit circle. The hyperbolic tangent is defined as:

```text
tanh(x) = (e^x - e^-x) / (e^x + e^-x)
```

Google Sheets does not accept or return complex numbers, so TANH only works with real inputs there.

## Syntax

```excel
=TANH(number)
```

<!-- Image 1: Hyperbolic Tangent Curve. See Images/Math & Trig/TANH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | Any real number. Google Sheets calls this argument `value`. Text that cannot be read as a number returns `#VALUE!`. |

### Return Value

A number between -1 and 1. The result has the same sign as the input. Text that cannot be read as a number returns `#VALUE!`.

## Examples

### Example 1: Zero Input

```excel
=TANH(0)
```

**Result:** `0`

The curve passes through the origin, so an input of 0 returns 0.

### Example 2: Positive Input

```excel
=TANH(0.5)
```

**Result:** `0.462117`

A positive input gives a positive result below 1.

### Example 3: Negative Input

```excel
=TANH(-2)
```

**Result:** `-0.964028`

The sign of the result matches the sign of the input, and the size stays below 1.

<!-- Image 2: Percentage Scale Mapping. See Images/Math & Trig/TANH.md -->

### Example 4: Percentage Scale

```excel
=ROUND(100*TANH(0.8),1)
```

**Result:** `66.4`

Multiplying by 100 maps the -1 to 1 range onto a -100 to 100 scale, and ROUND limits the result to one decimal place.

## Story Problems

### Problem 1: Bounded Sales Momentum

A sales manager compares monthly change scores for three representatives. A raw change of 1.2 is not twice as meaningful as 0.6, so the manager squeezes each score into the -1 to 1 band before totaling them.

| Representative | Change Score |
| --- | --- |
| Ines | -0.5 |
| Jonas | 0.25 |
| Kira | 1.2 |

**Task:** Find the total of the three scores after TANH has been applied to each one.

**Solution:**

```excel
=SUMPRODUCT(TANH(B2:B4))
```

**Answer:** `0.6165`. The three results are -0.4621, 0.2449 and 0.8337, and they add up to 0.6165.

### Problem 2: Pump Gauge Reading

A plant displays signal strength on a gauge that reads from -100 to 100. Each sensor sends a raw signal, and the gauge shows 100 times the TANH of that signal, rounded to one decimal place.

| Sensor | Raw Signal |
| --- | --- |
| Pump A | 0.8 |
| Pump B | 2.5 |

**Task:** Find the gauge reading for Pump A, which is in row 2.

**Solution:**

```excel
=ROUND(100*TANH(B2),1)
```

**Answer:** `66.4`. Pump B would read 98.7 on the same gauge, which shows how the curve flattens near the top of the scale.

<!-- Image 3: Gauge Dial Reading. See Images/Math & Trig/TANH.md -->

## Use Cases

### Bounded Score Scaling

**Scenario:** A performance dashboard shows each team's change score between -1 and 1 so that one extreme month does not dominate the chart.

```excel
=TANH(Scores[Change])
```

**Why It Works:** TANH keeps the order of the scores and the sign of each change, but compresses the extremes. Ranking is unchanged, so the sort order of the table stays the same.

### Gauge Display Scaling

**Scenario:** A control panel shows each pump's signal on a dial that reads from -100 to 100.

```excel
=ROUND(100*TANH(Signal),1)
```

**Why It Works:** The formula scales the output to the dial range in one step. Keep the signal values in a named range so that the same formula works as new sensors are added.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text that cannot be read as a number. | Convert the value to a number. |
| Results always near 1 or -1 | The input is a large value such as a percent written as 80, not 0.8. | Scale the input down first, or divide percentages by 100. |
| Differences look too small | Two large inputs, such as 5 and 10, return almost the same value. | Compare the raw inputs when the size of the gap matters. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Argument named `number`. Accepts any real number. |
| Google Sheets | Available | Argument named `value`. Complex numbers are not supported. |

## Tips and Best Practices

- Use `SUMPRODUCT(TANH(range))` to total a range without entering the formula as an array in older versions of Excel.
- Scale large inputs down before applying TANH, because values beyond about 3 are already very close to 1 or -1.
- Multiply the result by 100 to show a value on a percentage-style scale.
- Use `TAN` when the input is an angle in radians, and `TANH` when the input is a plain number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ATANH](ATANH.md) | The inverse of TANH. It returns the input that produces a given TANH result. |
| [COSH](COSH.md) | Hyperbolic cosine, which is the other common hyperbolic function. |
| [SINH](SINH.md) | Hyperbolic sine, the numerator in the hyperbolic tangent definition. |
| [TAN](TAN.md) | Trigonometric tangent of an angle in radians, not limited to the -1 to 1 band. |

## Official Documentation

- [Microsoft Support: TANH function](https://support.microsoft.com/en-us/excel/functions/tanh-function)
- [Google Docs Editors Help: TANH](https://support.google.com/docs/answer/3093755)
