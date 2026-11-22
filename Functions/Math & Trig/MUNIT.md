---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Matrix
purpose:
  - Matrix Math
use-case:
  - Identity Matrix Checks
  - Inventory Stay Rules
  - Matrix Verification
related:
  - MDETERM
  - MINVERSE
  - MMULT
  - TRANSPOSE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/munit-function
  - https://support.google.com/docs/answer/9368156
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Identity Matrix
  - Unit Matrix
tags:
  - excel
  - linear-algebra
  - matrix
  - sheets
---

# MUNIT

## Description

**MUNIT** returns a unit matrix, also called an identity matrix. A unit matrix is square, has 1s along its main diagonal from top left to bottom right, and has 0s in every other cell. The size of the result is set by the one argument, so MUNIT(3) returns a 3 by 3 matrix.

The unit matrix plays the role that the number 1 plays in ordinary multiplication. Multiplying any matrix by a unit matrix of the right size returns the original matrix unchanged. That makes MUNIT useful for checking matrix formulas, for starting a calculation from a neutral state, and for building transition rules in which some values stay as they are.

MUNIT returns an array, so it fills a square output range. In Microsoft 365 and Google Sheets, enter the formula once in the top-left cell. In older Excel versions, select the full output range and confirm with Ctrl+Shift+Enter.

## Syntax

```excel
=MUNIT(dimension)
```

<!-- Image 1: Identity Matrix Layout. See Images/Math & Trig/MUNIT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `dimension` | Yes | The size of the square matrix to return. It must be an integer greater than zero. A value of 1 returns a single cell containing 1. |

### Return Value

A square array with `dimension` rows and `dimension` columns. The diagonal cells hold 1 and all other cells hold 0. MUNIT returns `#VALUE!` when `dimension` is zero or negative. The Microsoft documentation does not describe the result for a non-integer dimension, so use whole numbers.

## Examples

### Example 1: Three by Three Identity Matrix

```excel
=MUNIT(3)
```

**Result:** A 3 by 3 array with `1`, `0`, `0` in the first row, `0`, `1`, `0` in the second, and `0`, `0`, `1` in the third

Enter the formula in the top-left cell of a 3 by 3 output range in Microsoft 365, or select the range first in older Excel.

<!-- Image 2: Identity Matrix Grid. See Images/Math & Trig/MUNIT.md -->

### Example 2: Single Cell

```excel
=MUNIT(1)
```

**Result:** `1`

A 1 by 1 unit matrix contains only the value 1.

### Example 3: Multiplying a Matrix by the Identity

With `A1:C3` containing the numbers 1 through 9 in order by row:

```excel
=MMULT(A1:C3, MUNIT(3))
```

**Result:** The same nine values as `A1:C3`

Multiplying by the identity leaves the matrix unchanged. This is the standard check that a matrix product is working.

### Example 4: Invalid Dimension

```excel
=MUNIT(0)
```

**Result:** `#VALUE!`

The dimension must be greater than zero, so a zero size is rejected.

## Story Problems

### Problem 1: Checking a Matrix Pipeline

A forecasting team stores a 3 by 3 transition table in `B2:D4`. Before the table feeds a model, the analyst multiplies it by an identity matrix to confirm that the multiplication step does not alter any value.

| Row | Column 1 | Column 2 | Column 3 |
| --- | --- | --- | --- |
| Row A | 2 | 5 | 1 |
| Row B | 0 | 3 | 4 |
| Row C | 6 | 1 | 2 |

**Task:** Multiply `B2:D4` by a 3 by 3 unit matrix and compare the output with the original table.

**Solution:**

```excel
=MMULT(B2:D4, MUNIT(3))
```

**Answer:** The output matches the original table value for value, so the multiplication step is safe to use. The table holds 2, 5, 1, 0, 3, 4, 6, 1, and 2 in both places.

### Problem 2: Holding Stock Steady

Four warehouses each start the week with a stock count in `B2:B5`: 120, 85, 40, and 200 units. A planner uses a stay rule in which no stock moves between warehouses, so the transfer matrix is the identity.

| Warehouse | Units |
| --- | --- |
| North | 120 |
| South | 85 |
| East | 40 |
| West | 200 |

**Task:** Apply the stay rule to the stock counts and report the result.

**Solution:**

```excel
=MMULT(MUNIT(4), B2:B5)
```

**Answer:** 120, 85, 40, and 200 units, the same as the starting counts. Because no stock moves, every warehouse keeps its original total.

<!-- Image 3: Stay Rule Stock Panel. See Images/Math & Trig/MUNIT.md -->

## Use Cases

### Identity Matrix Checks

**Scenario:** A modeler builds a formula that multiplies matrices and needs a quick test that the formula returns valid results.

```excel
=MMULT(Model, MUNIT(3))
```

**Why It Works:** If the output matches Model cell for cell, the multiplication formula is working. Any difference points to a layout or dimension problem.

### Inventory Stay Rules

**Scenario:** A planning sheet describes how stock moves between sites each week, and some sites keep all their stock.

```excel
=MMULT(MUNIT(4), StockCounts)
```

**Why It Works:** Each site's count is multiplied by 1 on the diagonal and 0 elsewhere, so the stock stays where it is. Replace the identity with a transfer matrix when stock does move.

### Starting Point for Matrix Inversion Checks

**Scenario:** An analyst inverts a matrix and wants to confirm the result.

```excel
=MMULT(Coefficients, MINVERSE(Coefficients))
```

**Why It Works:** The product should equal MUNIT of the same size, with 1s on the diagonal and 0s elsewhere. Small rounding differences such as 0.9999999999 are normal.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The dimension is zero or negative. | Use a whole number greater than zero. |
| `#VALUE!` | The dimension is text, such as a cell that holds a label. | Point the formula at a cell that holds a number. |
| Only one value appears | The output range was not entered as an array formula in legacy Excel. | Select the full square output range and press Ctrl+Shift+Enter. |
| Values near 1 or 0 instead of exact | Floating-point rounding after a chain of calculations. | Wrap the check in ROUND, such as ROUND(value, 10). |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, 2019, 2021, 2024, Microsoft 365, and Excel for the web | Returns an array. Legacy versions need Ctrl+Shift+Enter. |
| Google Sheets | Available | Returns a square array of the given size. The help page calls the dimension required to be an integer greater than zero. |

## Tips and Best Practices

- Use MUNIT with the same size as the matrix you are checking, because a size mismatch returns `#VALUE!` in MMULT.
- Keep the dimension in a labeled cell so the size of the model is easy to change.
- Combine MUNIT with MMULT and MINVERSE to confirm that an inverse is correct.
- Treat results that differ from the identity only by rounding noise as correct, and round them for display.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MMULT](MMULT.md) | Multiplies matrices; multiplying by MUNIT returns the original matrix. |
| [MINVERSE](MINVERSE.md) | Returns the inverse, which multiplied by the original gives MUNIT. |
| [MDETERM](MDETERM.md) | Confirms that a matrix is square and non-singular before inversion. |
| [TRANSPOSE](../Lookup%20%26%20Reference/TRANSPOSE.md) | Reorients a matrix so its dimensions match MUNIT's size. |

## Official Documentation

- [Microsoft Support: MUNIT function](https://support.microsoft.com/en-us/excel/functions/munit-function)
- [Google Docs Editors Help: MUNIT](https://support.google.com/docs/answer/9368156)
