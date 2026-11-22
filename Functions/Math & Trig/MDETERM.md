---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Matrix
purpose:
  - Matrix Math
use-case:
  - Garden Plot Area
  - Invertibility Checks
  - Linear Equation Systems
related:
  - MINVERSE
  - MMULT
  - MUNIT
  - SUMPRODUCT
  - TRANSPOSE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/mdeterm-function
  - https://support.google.com/docs/answer/3094290
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Matrix Determinant
tags:
  - excel
  - linear-algebra
  - matrix
  - sheets
---

# MDETERM

## Description

**MDETERM** returns the determinant of a square matrix, a single number calculated from all the values in the matrix. The matrix must have the same number of rows and columns. A 2 by 2 range, for example, has a determinant of `a x d - b x c`, where a, b, c, and d are its four values.

The determinant tells you two things about a matrix. First, a determinant of zero means the matrix has no inverse, so MINVERSE cannot return a usable result and linear equations built from that matrix may have no unique solution. Second, the absolute value of the determinant measures how much the matrix stretches or shrinks space, which is why it gives the area of a triangle when the matrix holds coordinates.

Use MDETERM when you need to test whether a matrix can be inverted, when you need an area from coordinates, or when you need a scaling factor for a linear transformation. Most day-to-day spreadsheet work does not need it. For a single pair of equations, a direct calculation with the values is often easier to audit.

## Syntax

```excel
=MDETERM(array)
```

<!-- Image 1: Square Array Requirement. See Images/Math & Trig/MDETERM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | A numeric range, array constant, or named range with an equal number of rows and columns, such as `A1:B2` or `{4,7;2,6}`. Every cell must contain a number. |

### Return Value

A single number. MDETERM returns `#VALUE!` when the array is not square, or when any cell in the array is empty or contains text. Because Excel calculates to about 16 digits, a singular matrix can return a value such as `1E-16` instead of exactly 0.

## Examples

### Example 1: Determinant of a 2 by 2 Range

With `A1:B2` containing `4`, `7`, `2`, and `6`:

```excel
=MDETERM(A1:B2)
```

**Result:** `10`

The calculation is 4 x 6 minus 7 x 2, which equals 24 minus 14.

### Example 2: Inline Array Constant

```excel
=MDETERM({2,0;0,5})
```

**Result:** `10`

The semicolon starts a new row. A diagonal matrix has a determinant equal to the product of its diagonal values, so 2 x 5 = 10.

### Example 3: Singular Matrix

```excel
=MDETERM({1,2;2,4})
```

**Result:** `0`

The second row is exactly twice the first, so the matrix has no inverse and its determinant is zero.

### Example 4: 3 by 3 Matrix

With `A1:C3` containing `2`, `0`, `1` in row 1, `1`, `3`, `2` in row 2, and `1`, `1`, `4` in row 3:

```excel
=MDETERM(A1:C3)
```

**Result:** `18`

The expansion is 2 x (3 x 4 minus 2 x 1) minus 0 x (1 x 4 minus 2 x 1) plus 1 x (1 x 1 minus 3 x 1), which gives 20 minus 0 minus 2.

### Example 5: Non-Square Input

```excel
=MDETERM(A1:B3)
```

**Result:** `#VALUE!`

A 3 by 2 range has no determinant because the matrix is not square.

## Story Problems

### Problem 1: Area of a Garden Plot

A landscaper marks three corner stakes of a triangular bed. The x and y coordinates are in `B2:C4` in meters, and column `D` holds the value 1 for each stake, as the area method requires.

| Stake | X | Y | Constant |
| --- | --- | --- | --- |
| North | 1 | 1 | 1 |
| East | 5 | 2 | 1 |
| South | 2 | 6 | 1 |

**Task:** Calculate the area of the bed in square meters.

**Solution:**

```excel
=ABS(MDETERM(B2:D4))/2
```

**Answer:** `9.5`. The determinant is 19, and half its absolute value is 9.5 square meters.

<!-- Image 2: Garden Plot Triangle Layout. See Images/Math & Trig/MDETERM.md -->

### Problem 2: Can Two Recipes Be Solved Together

A bakery writes two ingredient ratios in `B2:C3`: row 2 holds 3 and 2, and row 3 holds 6 and 4. The owner wants to know whether the two ratios can be solved for a unique set of batch sizes.

| Ratio | Flour Units | Sugar Units |
| --- | --- | --- |
| Batch A | 3 | 2 |
| Batch B | 6 | 4 |

**Task:** Find the determinant of the ratio matrix.

**Solution:**

```excel
=MDETERM(B2:C3)
```

**Answer:** `0`. Batch B is exactly twice Batch A, so the two ratios do not determine a unique answer.

<!-- Image 3: Ratio Table With Zero Determinant. See Images/Math & Trig/MDETERM.md -->

## Use Cases

### Triangle Area From Coordinates

**Scenario:** A surveyor records three boundary points and needs the area of a parcel without drawing it.

```excel
=ABS(MDETERM(B2:D4))/2
```

**Why It Works:** Each row holds x, y, and 1. The absolute value makes the result independent of the order of the points, and dividing by 2 gives the area of the triangle.

### Invertibility Check Before Solving

**Scenario:** A planning model uses a two by two coefficient table. Before calling MINVERSE, the analyst confirms that the table can be inverted.

```excel
=IF(ABS(MDETERM(A2:B3)) < 0.000000000001, "Not invertible", "Invertible")
```

**Why It Works:** Comparing against a tiny tolerance avoids false results caused by floating-point rounding, which can turn an exact zero into a very small number.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The range has a different number of rows and columns. | Select a range with the same number of rows and columns. |
| `#VALUE!` | A cell in the range is empty or contains text. | Fill the blank cell with a number or correct the text value. |
| Tiny value such as `1E-16` | A singular matrix gives a determinant that is almost zero. | Test with ABS and a small tolerance rather than an exact zero. |
| Negative result | The order of rows or the sign of the values reverses orientation. | Use ABS when only the magnitude matters, such as for areas. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, 2019, 2021, 2024, Microsoft 365, and Excel for the web | Returns `#VALUE!` for non-square arrays or for empty or text cells. |
| Google Sheets | Available | Requires a square matrix, given as a range or an inline array with `;` between rows. |

## Tips and Best Practices

- Check the determinant before MINVERSE, because a zero result means the inverse does not exist.
- Use ABS with the determinant when you need an area, since the sign depends on the order of the points.
- Test for zero with a small tolerance instead of an exact equal sign.
- Keep the matrix on its own range or named range so inserting a row does not break the calculation.
- Use MMULT to check results: multiplying a matrix by its inverse should return MUNIT.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MINVERSE](MINVERSE.md) | Returns the inverse of a matrix that has a non-zero determinant. |
| [MMULT](MMULT.md) | Multiplies matrices, used with MINVERSE to solve linear systems. |
| [MUNIT](MUNIT.md) | Creates the identity matrix that a matrix times its inverse should equal. |
| [SUMPRODUCT](SUMPRODUCT.md) | Multiplies and sums ranges, useful for simple weighted totals without matrices. |
| [TRANSPOSE](../Lookup%20%26%20Reference/TRANSPOSE.md) | Swaps rows and columns before a matrix calculation. |

## Official Documentation

- [Microsoft Support: MDETERM function](https://support.microsoft.com/en-us/excel/functions/mdeterm-function)
- [Google Docs Editors Help: MDETERM](https://support.google.com/docs/answer/3094290)
