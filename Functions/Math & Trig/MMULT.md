---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Matrix
purpose:
  - Matrix Math
use-case:
  - Ingredient Requirements
  - Store Sales Totals
  - Weighted Scoring
related:
  - MDETERM
  - MINVERSE
  - MUNIT
  - SUMPRODUCT
  - TRANSPOSE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/mmult-function
  - https://support.google.com/docs/answer/3094292
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Matrix Product
  - Matrix Multiply
tags:
  - excel
  - linear-algebra
  - matrix
  - sheets
---

# MMULT

## Description

**MMULT** returns the matrix product of two arrays. Each cell in the result is the sum of products formed by one row of the first array and one column of the second array. The result has as many rows as the first array and as many columns as the second array.

The rule that makes MMULT work is dimensional. The first array must have as many columns as the second array has rows. A 2 by 3 array can be multiplied by a 3 by 1 array, which returns a 2 by 1 result, but it cannot be multiplied by a 2 by 3 array.

Use MMULT when a calculation is a sum of products across rows and columns, such as weighted scores, ingredient totals from a recipe grid, or the solution of a linear system using MINVERSE. For a single weighted total, SUMPRODUCT is simpler. MMULT is the right choice when many rows need the same weights at once.

## Syntax

```excel
=MMULT(array1, array2)
```

<!-- Image 1: Row and Column Matching. See Images/Math & Trig/MMULT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first array or range. Its number of columns must equal the number of rows in `array2`. |
| `array2` | Yes | The second array or range. Its number of rows must equal the number of columns in `array1`. |

### Return Value

An array with the same number of rows as `array1` and the same number of columns as `array2`. MMULT returns `#VALUE!` when the inner dimensions do not match, and when any cell in either array is empty or contains text.

## Examples

### Example 1: Product of Two 2 by 2 Ranges

With `A1:B2` containing `1`, `2`, `3`, and `4`, and `D1:E2` containing `5`, `6`, `7`, and `8`:

```excel
=MMULT(A1:B2, D1:E2)
```

**Result:** `19` and `22` in the first row, `43` and `50` in the second row

Row 1 times column 1 is 1 x 5 + 2 x 7 = 19, and the other three cells follow the same pattern.

### Example 2: Row Totals Through a Column of Ones

```excel
=MMULT({1,2,3;4,5,6}, {1;1;1})
```

**Result:** `6` and `15`

A 2 by 3 array times a 3 by 1 array returns a 2 by 1 result. Multiplying by a column of ones adds each row, so the totals are 1 + 2 + 3 = 6 and 4 + 5 + 6 = 15.

### Example 3: Weighted Test Scores

With the scores for two students in `B2:D3` (80, 90, 70 for the first student and 60, 75, 95 for the second) and the weights in `F2:F4` (0.2, 0.3, and 0.5):

```excel
=MMULT(B2:D3, F2:F4)
```

**Result:** `78` and `82`

Each student score is the weighted sum of the three tests. The first student scores 80 x 0.2 + 90 x 0.3 + 70 x 0.5 = 78.

### Example 4: Mismatched Dimensions

```excel
=MMULT(A1:B2, D1:D3)
```

**Result:** `#VALUE!`

The first array has 2 columns, but the second array has 3 rows, so the product is undefined.

<!-- Image 2: Matching Inner Dimensions. See Images/Math & Trig/MMULT.md -->

## Story Problems

### Problem 1: Store Sales From Item Counts

A cafe has two locations. Each row of `B2:D3` lists the number of coffees, teas, and pastries sold at one store, and the unit prices sit in `F2:F4` in the same order: coffee 2.50, tea 4.00, and pastry 1.25.

| Store | Coffee | Tea | Pastry |
| --- | --- | --- | --- |
| Harbor | 12 | 5 | 8 |
| Market | 7 | 10 | 3 |

**Task:** Calculate the sales total for each store.

**Solution:**

```excel
=MMULT(B2:D3, F2:F4)
```

**Answer:** Harbor sold `60.00` and Market sold `61.25`. Harbor is 12 x 2.50 + 5 x 4.00 + 8 x 1.25 = 60, and Market is 7 x 2.50 + 10 x 4.00 + 3 x 1.25 = 61.25.

<!-- Image 3: Store Totals Result Panel. See Images/Math & Trig/MMULT.md -->

### Problem 2: Ingredients for a Bake Order

A bakery sells two cakes. The recipe grid in `B2:C4` lists eggs, cups of flour, and cups of sugar needed for one cake of each type. The order for the day is 4 of cake one and 3 of cake two, stored in `E2:E3`.

| Ingredient | Cake One | Cake Two |
| --- | --- | --- |
| Eggs | 2 | 1 |
| Flour Cups | 1 | 3 |
| Sugar Cups | 0 | 2 |

**Task:** Calculate the total of each ingredient the bakery must buy.

**Solution:**

```excel
=MMULT(B2:C4, E2:E3)
```

**Answer:** 11 eggs, 13 cups of flour, and 6 cups of sugar. Eggs are 2 x 4 + 1 x 3 = 11, flour is 1 x 4 + 3 x 3 = 13, and sugar is 0 x 4 + 2 x 3 = 6.

## Use Cases

### Weighted Scoring Across Many Candidates

**Scenario:** A hiring panel scores each candidate on several criteria and applies the same weights to every candidate.

```excel
=MMULT(Scores, Weights)
```

**Why It Works:** Each row of Scores is one candidate and the Weights column applies the same percentages to every row, so one formula ranks the whole list. The weights must sum to 1 for the result to be a true average.

### Ingredient Requirements From a Recipe Grid

**Scenario:** A catering team converts a menu order into the total quantity of each ingredient.

```excel
=MMULT(RecipeGrid, OrderQuantities)
```

**Why It Works:** Rows of the recipe grid are ingredients and columns are dishes, so the product adds each dish's ingredient needs across the order.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The columns of the first array do not match the rows of the second. | Transpose one array with TRANSPOSE or select a range with matching dimensions. |
| `#VALUE!` | A cell is empty or contains text. | Replace the blank or text cell with a number. |
| Only one value appears | The output range was not entered as an array formula in legacy Excel. | Select the full output range and press Ctrl+Shift+Enter. |
| Result is the wrong shape | The output range is larger or smaller than the product. | Select a range with the number of rows of the first array and the columns of the second. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, 2019, 2021, 2024, Microsoft 365, and Excel for the web | Works as a dynamic array in Microsoft 365; legacy versions need Ctrl+Shift+Enter. |
| Google Sheets | Available | Same dimension rule. The help page does not describe the error for mismatched dimensions, so check the sizes before you rely on the output. |

## Tips and Best Practices

- Write down the dimensions of each array before you multiply, and confirm that the inner numbers match.
- Use TRANSPOSE to turn a row of weights into a column when the layout does not fit.
- Use SUMPRODUCT for a single weighted total, and use MMULT when many rows share the same weights.
- Keep inputs numeric; a blank cell inside the range returns `#VALUE!`.
- Name the ranges, such as Scores and Weights, so the formula describes the business meaning.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MINVERSE](MINVERSE.md) | Produces the inverse matrix that is commonly multiplied with a vector of totals. |
| [MDETERM](MDETERM.md) | Returns the determinant, which tells you whether a matrix can be inverted. |
| [MUNIT](MUNIT.md) | Creates an identity matrix; multiplying any matrix by it returns the original matrix. |
| [SUMPRODUCT](SUMPRODUCT.md) | Sums products of a single pair of ranges, the simpler choice for one weighted total. |
| [TRANSPOSE](../Lookup%20%26%20Reference/TRANSPOSE.md) | Swaps rows and columns so the dimensions match. |

## Official Documentation

- [Microsoft Support: MMULT function](https://support.microsoft.com/en-us/excel/functions/mmult-function)
- [Google Docs Editors Help: MMULT](https://support.google.com/docs/answer/3094292)
