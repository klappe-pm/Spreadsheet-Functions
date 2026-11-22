---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
purpose:
  - Arithmetic Operations
use-case:
  - Extended Line Totals
  - Recipe Quantity Scaling
related:
  - ADD
  - DIVIDE
  - MINUS
  - PRODUCT
  - SUMPRODUCT
level: 1
source:
  - https://support.google.com/docs/answer/3093978
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Multiply Two Numbers
tags:
  - arithmetic
  - operator
  - sheets
---

# MULTIPLY

## Description

**MULTIPLY** returns the product of two numbers. `=MULTIPLY(B2, C2)` returns the same result as `=B2*C2`. The function is the named form of the multiplication operator, which suits formulas that a script or template generates.

Use MULTIPLY to calculate line totals from a quantity and a unit price, to scale a recipe or material list, or to apply a rate to an amount. The product can be nested inside other functions, for example to add a tax rate to a subtotal.

MULTIPLY accepts only two scalar values. It does not accept ranges or more than two arguments. To multiply a list of numbers together, use PRODUCT. To multiply pairs of ranges and add the results, use SUMPRODUCT. Microsoft Excel has no MULTIPLY function, so Excel users write the `*` operator instead.

## Syntax

```excel
=MULTIPLY(factor1, factor2)
```

<!-- Image 1: Operator Syntax Anatomy. See Images/Google-specific/MULTIPLY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `factor1` | Yes | The first multiplicand. A single number or a cell that holds one. |
| `factor2` | Yes | The second multiplicand. A single number or a cell that holds one. |

### Return Value

A number equal to `factor1` times `factor2`. If either argument is text that cannot be read as a number, the formula returns an error.

## Examples

All examples use this stationery order list.

| Item | Quantity | Unit Price |
| --- | --- | --- |
| Pens | 12 | 1.25 |
| Notebooks | 4 | 6.50 |
| Folders | 25 | 0.40 |

### Example 1: Pens Line Total

```excel
=MULTIPLY(B2, C2)
```

**Result:** `15`

Twelve pens at 1.25 each come to 15.

### Example 2: Notebooks Line Total

```excel
=MULTIPLY(B3, C3)
```

**Result:** `26`

Four notebooks at 6.50 each come to 26.

### Example 3: Two Literal Numbers

```excel
=MULTIPLY(3, 4)
```

**Result:** `12`

Both factors are typed into the formula.

### Example 4: Folders Line Total

```excel
=MULTIPLY(B4, C4)
```

**Result:** `10`

Twenty-five folders at 0.40 each come to 10.

<!-- Image 2: Stationery Line Totals. See Images/Google-specific/MULTIPLY.md -->

### Example 5: Nest Inside Another Multiplication

```excel
=MULTIPLY(MULTIPLY(B2, C2), 1.08)
```

**Result:** `16.2`

The pens total of 15 is multiplied by 1.08, which adds an 8 percent tax to the line.

## Story Problems

### Problem 1: Shipping Cartons

A warehouse charges 2.75 per carton to pack an order. Carton counts are in column B of `A1:C4`, and the rate is typed into each row of column C.

| Order | Cartons | Rate per Carton |
| --- | --- | --- |
| 5001 | 14 | 2.75 |
| 5002 | 9 | 2.75 |
| 5003 | 22 | 2.75 |

**Task:** In column D, calculate the packing charge for each order.

**Solution:**

```excel
=MULTIPLY(B2, C2)
```

Fill the formula down to D4.

**Answer:** `38.50`, `24.75` and `60.50` for orders 5001, 5002 and 5003. Each charge is the carton count times 2.75.

### Problem 2: Scaling a Recipe

A bakery makes a batch of each recipe and needs the total flour, in cups, for the planned number of batches. The cups per batch are in column B and the batch counts are in column C of `A1:C3`.

| Recipe | Cups per Batch | Batches |
| --- | --- | --- |
| Muffins | 2.5 | 3 |
| Bread | 1.25 | 4 |

**Task:** In column D, calculate the total cups of flour for each recipe.

**Solution:**

```excel
=MULTIPLY(B2, C2)
```

Fill the formula down to D3.

**Answer:** `7.5` cups for muffins and `5` cups for bread. Three batches of 2.5 cups and four batches of 1.25 cups give those totals.

## Use Cases

### Extended Line Totals

**Scenario:** A procurement clerk builds a purchase order where each line is a quantity times a unit price.

```excel
=MULTIPLY(B2, C2)
```

**Why It Works:** Each line total is calculated from its own quantity and price, so the order total can be added with SUM once every line is complete.

### Recipe Quantity Scaling

**Scenario:** A caterer doubles or triples recipes for an event and needs the scaled amount of each ingredient.

```excel
=MULTIPLY(B2, $F$1)
```

**Why It Works:** The scale factor in `F1` multiplies every base quantity. Changing `F1` from 2 to 3 updates every ingredient at once.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error in place of a number | One factor is text, such as a number stored as text. | Convert the text with VALUE or retype the cell as a number. |
| Formula does not calculate | The function has fewer or more than two arguments. | Use MULTIPLY with two values, or nest it for a third factor. |
| Error when a range is passed | MULTIPLY accepts scalar values only. | Use PRODUCT for a list, or SUMPRODUCT for pairs of ranges. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use the `*` operator, for example `=B2*C2`. |
| Google Sheets | Available | Returns the same result as the `*` operator for two scalar values. |

## Tips and Best Practices

- Keep quantities and prices in separate cells so that either one can be changed without rewriting the formula.
- Use an absolute reference such as `$F$1` for a scale factor or tax rate that applies to every row.
- Nest MULTIPLY to apply a second rate, as in Example 5, but keep each step visible when a reviewer needs to audit it.
- Use SUMPRODUCT when you need the total of many multiplied pairs in one cell.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PRODUCT](../Math%20%26%20Trig/PRODUCT.md) | Multiplies a range or list of numbers. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Multiplies pairs of ranges and adds the results. |
| [ADD](ADD.md) | Adds two numbers. |
| [DIVIDE](DIVIDE.md) | Divides one number by another. |
| [MINUS](MINUS.md) | Subtracts one number from another. |

## Official Documentation

- [Google Docs Editors Help: MULTIPLY](https://support.google.com/docs/answer/3093978)
