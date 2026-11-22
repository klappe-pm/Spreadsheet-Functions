---
domain: Spreadsheet Functions
category: Logical
subcategory: Lambda Helpers
purpose:
  - Array Shaping
use-case:
  - Label Matrix
  - Price Grid Builder
  - Seat Number Grid
related:
  - BYROW
  - LAMBDA
  - MAP
  - REDUCE
  - SCAN
  - SEQUENCE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/makearray-function
  - https://support.google.com/docs/answer/12569202
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Array Builder
  - Grid Generator
tags:
  - array-generation
  - dynamic-array
  - excel
  - lambda
  - sheets
---

# MAKEARRAY

## Description

**MAKEARRAY** builds an array with a set number of rows and columns. A LAMBDA with two parameters calculates each cell from its row number and column number, so the grid comes from a formula rather than from data already in the sheet.

Use MAKEARRAY when the grid follows a rule, such as a multiplication table, a seat numbering scheme or a set of labels. For a grid that repeats existing values, use an array function such as HSTACK or VSTACK. For an array created from a sequence of numbers alone, SEQUENCE is shorter.

Row and column numbers start at 1. The LAMBDA must return a single value for each cell, so a cell formula that itself returns an array causes an error.

## Syntax

```excel
=MAKEARRAY(rows, columns, LAMBDA(row, column, calculation))
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/MAKEARRAY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rows` | Yes | The number of rows in the result. Must be a whole number greater than zero. |
| `columns` | Yes | The number of columns in the result. Must be a whole number greater than zero. |
| `LAMBDA` | Yes | A LAMBDA with exactly two parameters. The first is the row number and the second is the column number. The last argument is the calculation for each cell. |

### Return Value

An array with the given number of rows and columns, where each cell holds the value the LAMBDA calculates for its row and column. A row or column value below 1, or a value that is not a number, returns `#VALUE!`. A LAMBDA with the wrong number of parameters also returns `#VALUE!` in Microsoft Excel.

## Examples

### Example 1: Sum of Row and Column Numbers

```excel
=MAKEARRAY(4,2,LAMBDA(r,c,r+c))
```

**Result:** a 4 by 2 block with the rows `2 3`, `3 4`, `4 5` and `5 6`.

The first row has row number 1, so its cells are 1 + 1 = 2 and 1 + 2 = 3. Each later row adds one to the row above it, which is the pattern the calculation produces.

### Example 2: Identity Matrix From Cell Inputs

```excel
=MAKEARRAY(B1,B2,LAMBDA(r,c,IF(r=c,1,0)))
```

**Result:** a 3 by 3 block of `1 0 0`, `0 1 0` and `0 0 1` when B1 and B2 both hold 3.

The size comes from cells, so the same formula builds a larger or smaller matrix. The diagonal cells, where the row and column numbers match, hold 1.

<!-- Image 2: Row and Column Index Grid. See Images/Logical/MAKEARRAY.md -->

### Example 3: Building Labels From Row and Column

```excel
=MAKEARRAY(2,3,LAMBDA(r,c,"R"&r&"C"&c))
```

**Result:** a 2 by 3 block with the labels `R1C1`, `R1C2`, `R1C3`, `R2C1`, `R2C2` and `R2C3`.

The LAMBDA joins text and numbers to build each label. This is a quick way to create a set of codes for a planning sheet.

### Example 4: A LAMBDA With the Wrong Parameter Count

```excel
=MAKEARRAY(2,2,LAMBDA(r,r*2))
```

**Result:** `#VALUE!`

The LAMBDA takes one parameter, but MAKEARRAY needs two, one for the row and one for the column. Add a second parameter to fix the formula.

## Story Problems

### Problem 1: Seat Numbers in a Hall

A hall has 4 rows of 5 seats. Seats are numbered across each row, so seat number = (row − 1) × 5 + column.

**Task:** Build the full seat grid in MAKEARRAY, then read the seat number in row 3, column 2.

**Solution:**

```excel
=MAKEARRAY(4,5,LAMBDA(r,c,(r-1)*5+c))
```

```excel
=INDEX(MAKEARRAY(4,5,LAMBDA(r,c,(r-1)*5+c)),3,2)
```

**Answer:** `12`. Row 3 starts after 10 seats, so column 2 is seat 12.

<!-- Image 3: Seat Grid Worksheet. See Images/Logical/MAKEARRAY.md -->

### Problem 2: Printing Cost Grid

A print shop charges 2.50 for each page of each copy. A job of r copies and c pages costs r × c × 2.50.

**Task:** Build a grid of 3 copy counts by 4 page counts, then read the cost for 2 copies of 3 pages.

**Solution:**

```excel
=INDEX(MAKEARRAY(3,4,LAMBDA(r,c,r*c*2.5)),2,3)
```

**Answer:** `15`. Two copies of a 3-page job are 2 × 3 × 2.50 = 15.

## Use Cases

### Label Matrix

**Scenario:** A warehouse labels storage bins in a grid of letters and numbers, such as A1, B1 and C1 on the first shelf.

```excel
=MAKEARRAY(4,3,LAMBDA(r,c,CHAR(64+c)&r))
```

**Why It Works:** The column number is turned into a letter with CHAR, and the row number is appended. The grid updates when the number of shelves changes.

### Price Grid Builder

**Scenario:** A price sheet shows a base price for each product in one column and a volume discount for each tier in another.

```excel
=MAKEARRAY(ROWS(Prices),3,LAMBDA(r,c,INDEX(Prices,r)*(1-c*0.05)))
```

**Why It Works:** The number of rows follows the product list, and each column applies a different discount tier to the base price.

### Seat Number Grid

**Scenario:** An event planner needs a numbering scheme for a room layout that changes with the number of rows and seats per row.

```excel
=MAKEARRAY(SeatRows,SeatsPerRow,LAMBDA(r,c,(r-1)*SeatsPerRow+c))
```

**Why It Works:** Changing the two named inputs redraws the whole grid, and the numbering rule stays in one place.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | Rows or columns are zero, negative or not numbers. | Use whole numbers greater than zero. |
| `#VALUE!` (Incorrect Parameters) | The LAMBDA does not accept exactly two parameters. | Write the LAMBDA with a row parameter and a column parameter. |
| Invalid name | A parameter name matches a cell reference, such as `C1`. Names such as `c2` also look like cell references. | Use names such as `row` and `col`. |
| Single value expected | A cell calculation returns an array instead of one value. | Return one value per cell, or use MAP or SCAN for array steps. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Microsoft Office and Office for iPhone | The Microsoft page does not list Excel 2024 or Excel 2021. Returns `#VALUE!` when rows or columns are not positive numbers. |
| Google Sheets | Available | The LAMBDA takes exactly two name arguments followed by the formula expression. Each cell must return a single value, and a named function can be passed without parentheses. |

## Tips and Best Practices

- Use MAKEARRAY when a formula defines the grid, and use data-based array functions when the grid repeats existing values.
- Name the LAMBDA parameters `row` and `col`, which read clearly and avoid cell-reference names.
- Wrap the result in INDEX to read one cell, instead of spilling the whole grid into the sheet.
- Keep the calculation short. A long formula inside each cell is hard to test, so move the rule into a named LAMBDA when it grows.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BYROW](BYROW.md) | Applies a LAMBDA to each row of an existing array. |
| [LAMBDA](LAMBDA.md) | Defines the two-parameter calculation that MAKEARRAY calls for each cell. |
| [MAP](MAP.md) | Calculates a new array from existing arrays item by item. |
| [REDUCE](REDUCE.md) | Combines an array into one value rather than building a grid. |
| [SCAN](SCAN.md) | Builds a running array of intermediate results from an existing array. |
| [SEQUENCE](../Math%20%26%20Trig/SEQUENCE.md) | Creates an array of sequential numbers without a calculation per cell. |

## Official Documentation

- [Microsoft Support: MAKEARRAY function](https://support.microsoft.com/en-us/excel/functions/makearray-function)
- [Google Docs Editors Help: MAKEARRAY](https://support.google.com/docs/answer/12569202)
