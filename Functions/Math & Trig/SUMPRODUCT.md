---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Matrix
purpose:
  - Aggregation
  - Matrix Math
use-case:
  - Extended Order Totals
  - Multi Condition Totals
  - Weighted Average Price
related:
  - FILTER
  - MMULT
  - SUM
  - SUMIFS
  - SUMSQ
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/sumproduct-function
  - https://support.google.com/docs/answer/3094294
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sum of Products
  - Array Product Sum
tags:
  - arrays
  - excel
  - matrix
  - sheets
---

# SUMPRODUCT

## Description

**SUMPRODUCT** multiplies the entries of two or more arrays position by position, then adds the products. With two columns of equal length, it returns the same answer as multiplying each row by hand and adding the results. Because the arithmetic happens inside one function, it needs no helper column.

SUMPRODUCT also handles conditions. A comparison such as `(B2:B5="East")` returns TRUE or FALSE for each row, and multiplying the results turns them into 1 or 0. Multiplying by 1 or 0 keeps only the rows that pass the test. Adding conditions gives OR logic, which SUMIFS cannot do in one call.

Entries that are not numbers count as zero inside SUMPRODUCT. The arrays must have the same dimensions, or the function returns `#VALUE!`. For a simple total of one column with one condition, SUMIF or SUMIFS is usually clearer.

## Syntax

```excel
=SUMPRODUCT(array1, [array2], [array3], ...)
```

<!-- Image 1: Parallel Arrays. See Images/Math & Trig/SUMPRODUCT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first range or array. Its entries are multiplied by the entries in the same position of the other arrays. |
| `array2, array3, ...` | No | Additional ranges or arrays of the same dimensions. Excel accepts up to 255 arrays. |

### Return Value

A single number equal to the sum of the products of the matching entries. The function returns `#VALUE!` when the arrays have different numbers of rows or columns.

## Examples

All examples use this order list in `A2:D5`. Column A is the item, column B is quantity, column C is price, and column D is region.

| Item | Quantity | Price | Region |
| --- | --- | --- | --- |
| Pens | 3 | 4.50 | East |
| Pads | 10 | 1.25 | West |
| Staples | 2 | 19.99 | East |
| Tape | 5 | 0.80 | North |

### Example 1: Quantity Times Price for All Rows

```excel
=SUMPRODUCT(B2:B5, C2:C5)
```

**Result:** `69.98`

The products are 13.50, 12.50, 39.98 and 4.00. Their sum is 69.98, the same as `=B2*C2+B3*C3+B4*C4+B5*C5`.

### Example 2: Two Regions With OR Logic

```excel
=SUMPRODUCT(((D2:D5="East")+(D2:D5="West"))*B2:B5)
```

**Result:** `15`

Each row is tested for East or West. The quantities 3, 10 and 2 qualify, while the North row is excluded.

### Example 3: Two Conditions With AND Logic

```excel
=SUMPRODUCT((D2:D5="East")*(B2:B5>=2)*C2:C5)
```

**Result:** `24.49`

Only East rows with at least two units count. Those are Pens (4.50) and Staples (19.99).

<!-- Image 2: Condition Arrays. See Images/Math & Trig/SUMPRODUCT.md -->

### Example 4: Arrays of Different Sizes

```excel
=SUMPRODUCT(B2:B5, C2:C4)
```

**Result:** `#VALUE!`

The first array has four rows and the second has three, so the function returns an error. Extend the second range to C5 to fix the formula.

## Story Problems

### Problem 1: Order Value From Quantity and Price

A caterer lists three ingredients with the amount ordered in column B and the unit cost in column C.

| Ingredient | Quantity | Unit Cost |
| --- | --- | --- |
| Flour | 6 | 2.25 |
| Butter | 4 | 7.50 |
| Eggs | 12 | 0.95 |

**Task:** Calculate the total cost of the order without a helper column.

**Solution:**

```excel
=SUMPRODUCT(B2:B4, C2:C4)
```

**Answer:** `54.9`, from 13.50 + 30.00 + 11.40.

<!-- Image 3: Ingredient Order Table. See Images/Math & Trig/SUMPRODUCT.md -->

### Problem 2: Units Shipped From One Warehouse

A distributor records each shipment line with its warehouse, status and units. The manager wants the units for East warehouse lines that are still open.

| Warehouse | Status | Units |
| --- | --- | --- |
| East | Open | 14 |
| West | Open | 9 |
| East | Closed | 22 |
| East | Open | 6 |
| North | Open | 5 |

**Task:** Total the units for East lines with the status Open.

**Solution:**

```excel
=SUMPRODUCT((A2:A6="East")*(B2:B6="Open")*C2:C6)
```

**Answer:** `20`, from 14 and 6. The closed East line and the open lines at other warehouses are excluded.

## Use Cases

### Extended Order Totals

**Scenario:** A purchasing team totals an order with many lines without adding a helper column.

```excel
=SUMPRODUCT(Orders[Qty], Orders[Unit Price])
```

**Why It Works:** Structured references keep the two columns aligned as the table grows. The result equals the sum of the line totals.

### Multi Condition Totals

**Scenario:** A sales lead totals revenue for two regions and one product line in a single formula.

```excel
=SUMPRODUCT(((Sales[Region]="East")+(Sales[Region]="West"))*(Sales[Product]="Widget")*Sales[Revenue])
```

**Why It Works:** The OR test is wrapped in its own parentheses, then multiplied by the AND test. Each condition returns 1 or 0, so only matching rows contribute.

### Weighted Average Price

**Scenario:** A buyer needs the average price per unit when each purchase has a different quantity.

```excel
=SUMPRODUCT(B2:B20, C2:C20)/SUM(B2:B20)
```

**Why It Works:** Multiplying each price by its quantity and dividing by the total quantity gives a weighted average. A simple AVERAGE would give each purchase the same weight.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The arrays have different numbers of rows or columns. | Make every range the same size. |
| Result is zero or too small | Conditions were added with `+` where `*` was needed, or the test compares text with a number. | Combine AND tests with `*` and check the data types of the compared cells. |
| Silent undercount | Text or blank entries count as zero in the product. | Confirm that numeric columns hold numbers, not text. |
| Slow workbook | Full-column references such as `A:A` make every formula scan the whole sheet. | Use bounded ranges such as `A2:A5000`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Excel for the web | Accepts up to 255 arrays. Non-numeric entries are treated as zero. |
| Google Sheets | Available | The arrays are named `array1` and `array2`, with more arrays optional. When the second array is omitted, the help page describes it as an array of 1s. The help page does not describe how text is handled, so test with your data. |

## Tips and Best Practices

- Wrap each condition in parentheses before multiplying, so the operator precedence stays correct.
- Use `*` to combine conditions with AND and `+` to combine them with OR.
- Prefer SUMIFS when the logic is AND only and the total needs no arithmetic.
- Keep ranges bounded so the workbook stays fast.
- Check the row count of each array when you edit a range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns matching rows, which you can then total with SUM. |
| [MMULT](MMULT.md) | Multiplies whole matrices instead of pairing single entries. |
| [SUM](SUM.md) | Adds values without multiplying them first. |
| [SUMIFS](SUMIFS.md) | Totals rows that meet AND conditions without arithmetic inside the formula. |
| [SUMSQ](SUMSQ.md) | Sums squared values, a special case of SUMPRODUCT with the same array. |

## Official Documentation

- [Microsoft Support: SUMPRODUCT function](https://support.microsoft.com/en-us/excel/functions/sumproduct-function)
- [Google Docs Editors Help: SUMPRODUCT](https://support.google.com/docs/answer/3094294)
