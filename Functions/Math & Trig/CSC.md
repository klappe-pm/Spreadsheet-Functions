---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Trigonometry
purpose:
  - Trigonometry
use-case:
  - Trig Table Audits
  - Wave Phase Analysis
related:
  - COT
  - CSCH
  - RADIANS
  - SEC
  - SIN
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/csc-function
  - https://support.google.com/docs/answer/9084103
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cosecant
tags:
  - excel
  - reciprocal-trig
  - sheets
  - trigonometry
---

# CSC

## Description

**CSC** returns the cosecant of an angle that you supply in radians. The cosecant is the reciprocal of the sine, so `CSC(angle)` gives the same result as `1/SIN(angle)`. Use CSC when a calculation is written in cosecant terms, such as a wave phase relationship or a trig identity that uses the reciprocal of the sine.

CSC expects radians, not degrees. Convert degree values with RADIANS first. An input of 0 has no defined cosecant, and Google Sheets returns `#DIV/0!` for it. An input whose absolute value is 2^27 or greater returns `#NUM!` in Excel.

## Syntax

```excel
=CSC(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/CSC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The angle in radians. Google Sheets names this argument `angle`. A non-numeric value returns `#VALUE!`. |

### Return Value

A number: the cosecant of the angle. The function returns `#NUM!` when the absolute value of the input is 2^27 or greater, and `#VALUE!` when the input is not numeric.

## Examples

### Example 1: Cosecant of Fifteen Radians

```excel
=CSC(15)
```

**Result:** `1.53778`

The angle is read as 15 radians, which gives 1 divided by sin(15).

### Example 2: Cosecant of One Radian

```excel
=CSC(1)
```

**Result:** `1.18840`

### Example 3: Cosecant of Pi Over Two

```excel
=CSC(PI()/2)
```

**Result:** `1`

The sine of pi over two is 1, so its reciprocal is 1.

### Example 4: Reciprocal of the Sine

```excel
=1/SIN(4)
```

**Result:** `-1.32135`

This matches the cosecant of 4 radians. Because sin(4) is negative, the cosecant is negative.

<!-- Image 2: Cosecant Versus Reciprocal Sine. See Images/Math & Trig/CSC.md -->

### Example 5: Negative Input

Cell A2 holds `-1`.

```excel
=CSC(A2)
```

**Result:** `-1.18840`

The cosecant is an odd function, so the result for -1 is the negative of the result for 1.

## Story Problems

### Problem 1: Wave Phase Readings

A test rig logs three phase readings in radians in column B. The analyst wants the total of their cosecants for a combined index.

| Reading | Phase (radians) |
| --- | --- |
| W1 | 1 |
| W2 | 4 |
| W3 | 15 |

**Task:** Add the cosecants of the three phase readings in one formula.

**Solution:**

```excel
=SUMPRODUCT(CSC(B2:B4))
```

**Answer:** `1.40483`. The three cosecants are 1.18840, -1.32135 and 1.53778, which add to 1.40483.

### Problem 2: Reciprocal Check

An auditor wants to confirm that the CSC function gives the same answer as dividing 1 by the sine for a test angle.

| Test | Angle (radians) |
| --- | --- |
| Sine check | 1 |

**Task:** Subtract `1/SIN` from `CSC` for the angle in B2. The difference shows whether the two methods agree.

**Solution:**

```excel
=CSC(B2)-1/SIN(B2)
```

**Answer:** `0`. Both methods give 1.18840, so the difference is zero, apart from any tiny rounding noise that a spreadsheet may display.

## Use Cases

### Wave Phase Analysis

**Scenario:** A lab stores phase readings in a table named Waves. The report needs the total of the cosecants across all readings.

```excel
=SUMPRODUCT(CSC(Waves[Phase]))
```

**Why It Works:** SUMPRODUCT evaluates CSC across the whole column in one step. Keep the phase values in radians so that the result matches the angle definition.

### Trig Table Audits

**Scenario:** A reviewer checks a trig table that mixes CSC and 1/SIN formulas and needs a quick test for any row that disagrees.

```excel
=ABS(CSC(B2)-1/SIN(B2))
```

**Why It Works:** Any row where the absolute difference is larger than a rounding tolerance needs review. Filter the column for large values to find the rows.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | The input is 0 in Google Sheets. | Use `=IF(A2=0,"",CSC(A2))` to skip zero inputs. |
| `#NUM!` | The absolute value of the input is 2^27 or greater in Excel. | Check the source value for a data entry mistake. |
| `#VALUE!` | The input is text or another non-numeric value. | Check the source cell, or convert the text to a number. |
| Unexpected result | The angle is in degrees, not radians. | Wrap the input in RADIANS. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in the Math and trigonometry group. | The argument is named `number` and is read in radians. |
| Google Sheets | Available | The argument is named `angle` and is read in radians. Sample results match Excel. |

## Tips and Best Practices

- Convert degree values with RADIANS before calling CSC.
- Use `1/SIN` in an audit column when you need to prove that the two methods agree.
- Guard against zero inputs with IF when zero can appear in the data.
- Remember that the result is negative wherever the sine is negative.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COT](COT.md) | The cotangent, built from the same radian input. |
| [CSCH](CSCH.md) | The hyperbolic cosecant, for hyperbolic inputs. |
| [RADIANS](RADIANS.md) | Converts degrees to radians before CSC is applied. |
| [SEC](SEC.md) | The secant, the reciprocal of COS. |
| [SIN](SIN.md) | The sine, whose reciprocal CSC returns. |

## Official Documentation

- [Microsoft Support: CSC function](https://support.microsoft.com/en-us/excel/functions/csc-function)
- [Google Docs Editors Help: CSC](https://support.google.com/docs/answer/9084103)
