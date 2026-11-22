---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Arithmetic Operations
  - Statistical Analysis
use-case:
  - Force Magnitude
  - Sum of Squared Residuals
related:
  - MMULT
  - SQRT
  - SUM
  - SUMPRODUCT
  - SUMXMY2
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/sumsq-function
  - https://support.google.com/docs/answer/3093714
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sum of Squares
tags:
  - arithmetic
  - excel
  - sheets
  - statistics
---

# SUMSQ

## Description

**SUMSQ** squares each number and adds the squares. It accepts single numbers, cell references, ranges and arrays, and it returns one total. Use it when the squares of values are needed, such as the sum of squared errors in a regression or the squared length of a vector.

Squaring makes negative and positive values count the same way. A residual of -4 contributes 16, just as a residual of 4 does. For that reason SUMSQ appears in error measures and in the length of a vector.

Inside a range or a reference, SUMSQ ignores text, logical values and empty cells. Text typed directly into the argument list causes an error, and an error value in any argument passes through to the result. To get the length of a vector, take the square root of the SUMSQ result.

## Syntax

```excel
=SUMSQ(number1, [number2], ...)
```

<!-- Image 1: Squared Values in a Range. See Images/Math & Trig/SUMSQ.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, reference, range or array to square and add. |
| `number2, ...` | No | Additional numbers, references or ranges. Excel accepts up to 255 arguments in total. A single array or range can replace the list. |

### Return Value

A single number equal to the sum of the squares of the numeric values. The function returns an error when an argument is an error value or text that cannot be read as a number.

## Examples

All examples use these values. Column B holds residuals in `B2:B6`: 2, -1, 3, -4 and 0.5. Column C holds readings in `C2:C5`: 2, the text "n/a", 3 and an empty cell.

### Example 1: Squares of Two Numbers

```excel
=SUMSQ(3, 4)
```

**Result:** `25`

The squares are 9 and 16, and their sum is 25.

### Example 2: Sum of Squared Residuals

```excel
=SUMSQ(B2:B6)
```

**Result:** `30.25`

The squares are 4, 1, 9, 16 and 0.25. Their total is 30.25, and the negative values count as positive.

### Example 3: Mix a Range With a Number

Cells A2, A3 and A4 contain 1, 2 and 3.

```excel
=SUMSQ(A2:A4, 10)
```

**Result:** `114`

The range gives 1 + 4 + 9 = 14, and the extra argument 10 adds 100.

<!-- Image 2: Text Ignored in a Range. See Images/Math & Trig/SUMSQ.md -->

### Example 4: Text and Blanks in a Range

```excel
=SUMSQ(C2:C5)
```

**Result:** `13`

The text "n/a" and the empty cell are ignored, so only 2 and 3 are squared: 4 + 9 = 13.

## Story Problems

### Problem 1: Squared Residuals of a Forecast

A planner compares forecast values with actual sales. The difference for each month is the residual. The planner needs the total of the squared residuals to measure the fit.

| Month | Residual |
| --- | --- |
| January | 1.5 |
| February | -2 |
| March | 0.5 |
| April | 3 |

**Task:** Total the squared residuals.

**Solution:**

```excel
=SUMSQ(B2:B5)
```

**Answer:** `15.5`, from 2.25 + 4 + 0.25 + 9.

<!-- Image 3: Residual Table. See Images/Math & Trig/SUMSQ.md -->

### Problem 2: Length of a Force Vector

An engineer records three force components on a bracket: 6 units along x, 8 units along y, and 0 units along z. The overall force size is the length of the vector.

| Component | Force |
| --- | --- |
| Fx | 6 |
| Fy | 8 |
| Fz | 0 |

**Task:** Calculate the length of the force vector.

**Solution:**

```excel
=SQRT(SUMSQ(B2:B4))
```

**Answer:** `10`, because 6 squared plus 8 squared plus 0 squared is 100, and its square root is 10.

## Use Cases

### Force Magnitude

**Scenario:** A design team checks the size of a force from its three components.

```excel
=SQRT(SUMSQ(Forces[Fx], Forces[Fy], Forces[Fz]))
```

**Why It Works:** SUMSQ adds the squares of all three components in one step, and SQRT returns the length. The result does not depend on the direction of the force.

### Sum of Squared Residuals

**Scenario:** An analyst compares the errors of two forecasting models by their squared residuals.

```excel
=SUMSQ(Model_A[Residual])
```

**Why It Works:** The model with the smaller total has smaller errors overall. Large misses count more than small ones because each error is squared before the total.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A text value typed directly into the argument list cannot be read as a number. | Enter a number, or place the value in a cell and reference it. |
| Error passes through | A referenced cell contains an error value, which SUMSQ returns. | Fix the source cell before summing. |
| Result looks like a square | The function returns the sum of squares, not the root. | Wrap the result in SQRT to get the length of a vector. |
| Text values missing | Text in a range is ignored without a warning. | Confirm that numeric data is stored as numbers. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Excel for the web | Accepts up to 255 arguments, or a single array or reference. Text in a range is ignored. |
| Google Sheets | Available | The arguments are named `value1` and `value2`, with more values optional. The help page describes the function for numbers and ranges. Use a range rather than a long list of arguments. |

## Tips and Best Practices

- Use SUMSQ with SQRT for a vector length, and use SUMSQ alone for an error total.
- Keep residuals in a column so the total updates when a value changes.
- Divide the result by the count of values when you need a mean squared error.
- Check for text values in the source range, because they are skipped silently.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MMULT](MMULT.md) | Multiplies matrices, which some vector calculations need. |
| [SQRT](SQRT.md) | Returns the square root, which turns a sum of squares into a length. |
| [SUM](SUM.md) | Adds the values themselves without squaring them. |
| [SUMPRODUCT](SUMPRODUCT.md) | Multiplies pairs of arrays, which SUMSQ does when both arrays are the same. |
| [SUMXMY2](SUMXMY2.md) | Sums the squared differences between two arrays. |

## Official Documentation

- [Microsoft Support: SUMSQ function](https://support.microsoft.com/en-us/excel/functions/sumsq-function)
- [Google Docs Editors Help: SUMSQ](https://support.google.com/docs/answer/3093714)
