---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Matrix
purpose:
  - Matrix Math
use-case:
  - Linear Equation Systems
  - Production Mix Planning
  - Undoing Linear Transformations
related:
  - MDETERM
  - MMULT
  - MUNIT
  - TRANSPOSE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/minverse-function
  - https://support.google.com/docs/answer/3094253
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Matrix Inverse
tags:
  - excel
  - linear-algebra
  - matrix
  - sheets
---

# MINVERSE

## Description

**MINVERSE** returns the inverse of a square matrix. The inverse is the matrix that, when multiplied by the original with MMULT, produces the identity matrix (1s on the diagonal and 0s elsewhere). Inverses are the standard way to solve a system of linear equations: if A holds the coefficients and b holds the constants, the solution is the inverse of A multiplied by b.

A matrix has an inverse only when its determinant is not zero. A singular matrix, where one row or column is a multiple of another, has no inverse, and MINVERSE returns `#NUM!`. Check the determinant with MDETERM first when the input might be singular.

MINVERSE returns an array, so it fills several cells. In Microsoft 365 and Google Sheets, enter the formula once in the top-left cell of the output range. In older Excel versions, select the whole output range, enter the formula, and confirm with Ctrl+Shift+Enter; otherwise only the first value appears.

## Syntax

```excel
=MINVERSE(array)
```

<!-- Image 1: Inverse Output Range. See Images/Math & Trig/MINVERSE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | A square numeric range, array constant, or named range with an equal number of rows and columns. Every cell must contain a number. |

### Return Value

An array with the same number of rows and columns as the input. MINVERSE returns `#NUM!` when the matrix is singular and `#VALUE!` when the array is not square or contains an empty or text cell.

## Examples

### Example 1: Inverse of a 2 by 2 Matrix

With `A1:B2` containing `4`, `7`, `2`, and `6`, select a 2 by 2 output range, type this formula, and confirm:

```excel
=MINVERSE(A1:B2)
```

**Result:** `0.6` and `-0.7` in the first row, `-0.2` and `0.4` in the second row

The determinant is 10, so each entry is the adjugate divided by 10. Check the answer by multiplying the original and the inverse with MMULT; the product is the identity matrix.

### Example 2: Diagonal Matrix

```excel
=MINVERSE({2,0;0,4})
```

**Result:** `0.5`, `0`, `0`, and `0.25` in a 2 by 2 output

The inverse of a diagonal matrix holds the reciprocal of each diagonal value.

### Example 3: Solving a Two Variable System

With the coefficients in `B2:C3` (4 and 7 in row 2, 2 and 6 in row 3) and the totals in `D2:D3` (18 and 14):

```excel
=MMULT(MINVERSE(B2:C3), D2:D3)
```

**Result:** `1` and `2`

The system 4x + 7y = 18 and 2x + 6y = 14 has the solution x = 1 and y = 2. Enter this formula in a two row output range in legacy Excel.

<!-- Image 2: Coefficient, Total and Solution Ranges. See Images/Math & Trig/MINVERSE.md -->

### Example 4: Singular Matrix

```excel
=MINVERSE({1,2;2,4})
```

**Result:** `#NUM!`

The second row is twice the first, so the determinant is zero and no inverse exists.

## Story Problems

### Problem 1: Two Products Through Two Machines

A workshop makes two products, X and Y. Each product uses cutting and finishing time. The table lists the hours per unit and the total hours used last week.

| Operation | Product X | Product Y | Total Hours |
| --- | --- | --- | --- |
| Cutting | 4 | 7 | 18 |
| Finishing | 2 | 6 | 14 |

**Task:** Find how many units of each product were made.

**Solution:**

```excel
=MMULT(MINVERSE(B2:C3), D2:D3)
```

**Answer:** 1 unit of Product X and 2 units of Product Y. Check: 4 x 1 + 7 x 2 = 18 cutting hours, and 2 x 1 + 6 x 2 = 14 finishing hours.

<!-- Image 3: Workshop Hours Result Panel. See Images/Math & Trig/MINVERSE.md -->

### Problem 2: A Rate Table That Cannot Be Inverted

A procurement analyst records two supplier rate combinations in `B2:C3`: 3 and 2 in row 2, and 6 and 4 in row 3. The analyst wants to recover the unit costs from these rates.

| Combination | Rate One | Rate Two |
| --- | --- | --- |
| Pair A | 3 | 2 |
| Pair B | 6 | 4 |

**Task:** Enter MINVERSE on the rate table and report what the result means.

**Solution:**

```excel
=MINVERSE(B2:C3)
```

**Answer:** `#NUM!`. Pair B is exactly twice Pair A, so the table has no inverse and the unit costs cannot be recovered from it. Ask for a different pair of rates.

## Use Cases

### Solving Linear Equation Systems

**Scenario:** An analyst has coefficients and totals for several related quantities and needs the unknown values.

```excel
=MMULT(MINVERSE(Coefficients), Totals)
```

**Why It Works:** Multiplying the inverse by the totals gives the unknowns directly. Named ranges keep the formula readable when the model grows.

### Production Mix Planning

**Scenario:** A plant wants to know how many units of each product to schedule when hours are fixed on two machines.

```excel
=MMULT(MINVERSE(HoursPerUnit), HoursAvailable)
```

**Why It Works:** Each row of HoursPerUnit is one machine and each column is one product, so the result gives the units that use every available hour exactly.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The matrix is singular, so its determinant is zero. | Check MDETERM first and revise the matrix or the data that produced it. |
| `#VALUE!` | The range is not square, or a cell is empty or contains text. | Select a square range with a number in every cell. |
| Only one value appears | The output range was not entered as an array formula in legacy Excel. | Select the full output range and press Ctrl+Shift+Enter. |
| Tiny values such as `1E-16` in place of 0 | Floating-point rounding in the calculation. | Wrap results in ROUND to the number of places you need. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, 2019, 2021, 2024, Microsoft 365, and Excel for the web | Returns an array; legacy versions need Ctrl+Shift+Enter. |
| Google Sheets | Available | Requires a square range or inline array. The help page does not list the error for a singular matrix, so test your inputs. |

## Tips and Best Practices

- Run MDETERM on the matrix first and only call MINVERSE when the determinant is not zero.
- Verify solutions by multiplying the original matrix with the result and checking for MUNIT.
- Prefer MMULT with MINVERSE over typing each element of the inverse, because the formula updates when the data changes.
- Name the coefficient and total ranges so the formula documents what it solves.
- Use MINVERSE for small systems, and use a dedicated solver for very large systems.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MDETERM](MDETERM.md) | Tests whether the inverse exists by returning the determinant. |
| [MMULT](MMULT.md) | Multiplies the inverse by the totals to solve the system. |
| [MUNIT](MUNIT.md) | Provides the identity matrix that a matrix times its inverse should match. |
| [TRANSPOSE](../Lookup%20%26%20Reference/TRANSPOSE.md) | Reorients a matrix before inversion when the data is stored in rows. |

## Official Documentation

- [Microsoft Support: MINVERSE function](https://support.microsoft.com/en-us/excel/functions/minverse-function)
- [Google Docs Editors Help: MINVERSE](https://support.google.com/docs/answer/3094253)
