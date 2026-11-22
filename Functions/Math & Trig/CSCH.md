---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Hyperbolic
purpose:
  - Trigonometry
use-case:
  - Hanging Cable Shapes
  - Hyperbolic Curve Analysis
  - Symmetry Checks
related:
  - COSH
  - COTH
  - CSC
  - SECH
  - SINH
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/csch-function
  - https://support.google.com/docs/answer/9116336
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Hyperbolic Cosecant
tags:
  - excel
  - hyperbolic
  - reciprocal-trig
  - sheets
---

# CSCH

## Description

**CSCH** returns the hyperbolic cosecant of a real number. The hyperbolic cosecant is the reciprocal of the hyperbolic sine, so `CSCH(x)` gives the same result as `1/SINH(x)`. Use it in formulas built from hyperbolic functions, where the reciprocal of SINH appears in the model.

The Microsoft page describes the input as an angle in radians, but the function returns the hyperbolic value of the number, not a circular trig value. For circular angles, use CSC instead. An input of 0 has no defined value, and Google Sheets returns `#DIV/0!` for it. In Excel, an input whose absolute value is 2^27 or greater returns `#NUM!`.

## Syntax

```excel
=CSCH(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/CSCH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A real number, other than 0, whose absolute value is less than 2^27. Google Sheets names this argument `value`. |

### Return Value

A number: the hyperbolic cosecant of the input. The function returns `#NUM!` when the absolute value of the input is 2^27 or greater, and `#VALUE!` when the input is not numeric.

## Examples

### Example 1: Hyperbolic Cosecant of One and a Half

```excel
=CSCH(1.5)
```

**Result:** `0.46964`

The value is 1 divided by the hyperbolic sine of 1.5.

### Example 2: Value From a Cell

Cell A2 holds `1`.

```excel
=CSCH(A2)
```

**Result:** `0.85092`

### Example 3: Larger Input

```excel
=CSCH(4)
```

**Result:** `0.03664`

As the input grows, the hyperbolic cosecant falls toward 0 because the hyperbolic sine grows quickly.

### Example 4: Small Input

```excel
=CSCH(0.5)
```

**Result:** `1.91903`

Small inputs give large results, which is why an input near 0 needs a guard in a model.

<!-- Image 2: Odd Symmetry of CSCH. See Images/Math & Trig/CSCH.md -->

### Example 5: Reciprocal of the Hyperbolic Sine

```excel
=1/SINH(1.5)
```

**Result:** `0.46964`

This matches Example 1 and shows the reciprocal relationship with SINH.

## Story Problems

### Problem 1: Hanging Cable Shape Index

An engineer records three index values in column B. The report needs the total of their hyperbolic cosecants.

| Sample | Index |
| --- | --- |
| Sample A | 0.5 |
| Sample B | 1 |
| Sample C | 2 |

**Task:** Add the hyperbolic cosecants of the three index values in one formula.

**Solution:**

```excel
=SUMPRODUCT(CSCH(B2:B4))
```

**Answer:** `3.04567`. The three values are 1.91903, 0.85092 and 0.27572, which add to 3.04567.

### Problem 2: Symmetry Check

A reviewer tests a negative input and a positive input of similar size to see how the signs compare.

| Test | Input |
| --- | --- |
| Negative test | -1 |
| Positive test | 4 |

**Task:** Add the hyperbolic cosecants of both test inputs in one formula.

**Solution:**

```excel
=SUMPRODUCT(CSCH(B2:B3))
```

**Answer:** `-0.81427`. The hyperbolic cosecant of -1 is -0.85092 and that of 4 is 0.03664, and the total at full precision is -0.81427. The negative input dominates the total because its result is larger in size.

## Use Cases

### Hanging Cable Shape Index

**Scenario:** A cable design sheet stores several index values in a table named Samples. The total of their hyperbolic cosecants feeds a summary cell.

```excel
=SUMPRODUCT(CSCH(Samples[Index]))
```

**Why It Works:** SUMPRODUCT evaluates CSCH across the whole column. Keep each index away from 0, because the result grows without limit as the input approaches 0.

### Hyperbolic Curve Analysis

**Scenario:** An analyst compares the hyperbolic cosecant of two parameters in adjacent cells.

```excel
=CSCH(B2)-CSCH(C2)
```

**Why It Works:** The difference shows how sensitive the model is to the change between the two parameters. Confirm that neither parameter is 0.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | The input is 0 in Google Sheets. | Use `=IF(A2=0,"",CSCH(A2))` to skip zero inputs. |
| `#NUM!` | The absolute value of the input is 2^27 or greater in Excel. | Check the source value for a data entry mistake. |
| `#VALUE!` | The input is text or another non-numeric value. | Check the source cell, or convert the text to a number. |
| Unexpected result | A circular angle was used where a hyperbolic input was intended. | Use CSC for circular angles. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in the Math and trigonometry group. | The argument is named `number`. |
| Google Sheets | Available | The argument is named `value`. Google Sheets documents a zero input as returning `#DIV/0!`. |

## Tips and Best Practices

- Use CSCH only for hyperbolic models. Circular angles belong in CSC.
- Guard against zero inputs with IF when zero can occur.
- Add a check column with `1/SINH` when a workbook must confirm the reciprocal relationship.
- Expect large results for inputs close to 0.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COSH](COSH.md) | The hyperbolic cosine, used alongside SINH in hyperbolic formulas. |
| [COTH](COTH.md) | The hyperbolic cotangent, built from the hyperbolic tangent. |
| [CSC](CSC.md) | The circular cosecant, for angles in radians. |
| [SECH](SECH.md) | The hyperbolic secant, the reciprocal of COSH. |
| [SINH](SINH.md) | The hyperbolic sine, whose reciprocal CSCH returns. |

## Official Documentation

- [Microsoft Support: CSCH function](https://support.microsoft.com/en-us/excel/functions/csch-function)
- [Google Docs Editors Help: CSCH](https://support.google.com/docs/answer/9116336)
