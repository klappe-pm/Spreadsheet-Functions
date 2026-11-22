---
domain: Spreadsheet Functions
category: Logical
subcategory: Lambda Helpers
purpose:
  - Array Shaping
  - Data Cleaning
use-case:
  - Insurance Fee Floor
  - Text Cleanup
  - Unit Conversion Column
related:
  - BYCOL
  - BYROW
  - LAMBDA
  - MAKEARRAY
  - REDUCE
  - SCAN
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/map-function
  - https://support.google.com/docs/answer/12568985
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Array Mapping
  - Element Transform
tags:
  - array-processing
  - dynamic-array
  - excel
  - lambda
  - sheets
---

# MAP

## Description

**MAP** applies a calculation to each item in one or more arrays and returns a new array of the results. It is the array version of filling a formula down a column. Write the formula once, and MAP repeats it for every row or item without a helper column.

Give MAP one array when the calculation uses one value, such as converting units or cleaning text. Give it several arrays when each result depends on matching items, such as a quantity and a price in the same row. The LAMBDA names one parameter for each array, in the same order.

MAP does not change the source data. Its output spills into the cells below or beside the formula, so keep the space clear. For a calculation that needs a whole row or column at once, BYROW or BYCOL is the better choice.

## Syntax

```excel
=MAP(array1, [array2, ...], LAMBDA(name1, [name2, ...], calculation))
```

<!-- Image 1: Syntax Anatomy. See Images/Logical/MAP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first array or range to map. Each item is passed to the LAMBDA in turn. |
| `array2, ...` | No | Further arrays or ranges. Each needs one matching name in the LAMBDA. |
| `LAMBDA` | Yes | A LAMBDA that must be the last argument. It needs one parameter for each array, and its calculation must return a single value per item. |

### Return Value

A new array with one result for each item. The Google Sheets help examples lay the results out like the input ranges. If the LAMBDA has the wrong number of parameters or the last argument is not a LAMBDA, the formula returns an error.

## Examples

### Example 1: Doubling Each Value

```excel
=MAP(A2:A4,LAMBDA(x,x*2))
```

**Result:** `6`, `10` and `14` when A2:A4 hold 3, 5 and 7.

The LAMBDA receives each value in turn as `x` and returns double the value. The three results spill into the cells below the formula.

### Example 2: Combining Two Arrays Row by Row

```excel
=MAP(B2:B4,C2:C4,LAMBDA(q,p,q*p))
```

**Result:** `10`, `30` and `10` when B2:B4 hold 2, 3 and 4, and C2:C4 hold 5, 10 and 2.5.

Each quantity in column B is paired with the price in the same row in column C. The LAMBDA has one name for each array, so `q` takes the quantity and `p` takes the price.

<!-- Image 2: Items Mapped One at a Time. See Images/Logical/MAP.md -->

### Example 3: Cleaning Text in Place

```excel
=MAP(A2:A4,LAMBDA(s,UPPER(TRIM(s))))
```

**Result:** `AB`, `CD` and `EF` when A2:A4 hold " ab ", "cd " and " ef".

TRIM removes the extra spaces at each end, and UPPER converts the text to capitals. The result is clean without a helper column for each step.

### Example 4: Filling Blank Entries

```excel
=MAP(D2:D4,LAMBDA(v,IF(v="","Missing",v)))
```

**Result:** `Ana`, `Missing` and `Cy` when D2:D4 hold Ana, a blank cell and Cy.

The IF inside the LAMBDA tests each item. Blank items get the label "Missing" and every other item passes through unchanged.

### Example 5: Mismatched Array Sizes

```excel
=MAP(B2:B3,C2:C4,LAMBDA(q,p,q*p))
```

**Result:** an error. Google Sheets reports "Array arguments to MAP are of different size."

Each array must have the same number of items, so every position has a matching pair. Trim the longer range or extend the shorter one.

## Story Problems

### Problem 1: Converting Lengths to Centimeters

A workshop lists three lengths in inches. One inch is 2.54 centimeters.

| Length (inches) |
| --- |
| 12 |
| 30 |
| 60 |

**Task:** Convert all three lengths to centimeters rounded to one decimal place, starting in column B.

**Solution:**

```excel
=MAP(A2:A4,LAMBDA(i,ROUND(i*2.54,1)))
```

**Answer:** `30.5`, `76.2` and `152.4`. For example, 12 × 2.54 = 30.48, which rounds to 30.5.

### Problem 2: Insurance Fee With a Minimum

A shipper charges insurance of 2% of the declared value, with a minimum fee of 5.

| Declared Value |
| --- |
| 150 |
| 400 |
| 80 |

**Task:** Calculate the fee for each parcel in column B, then find the total of the three fees.

**Solution:**

```excel
=MAP(A2:A4,LAMBDA(v,MAX(5,v*0.02)))
```

```excel
=SUM(MAP(A2:A4,LAMBDA(v,MAX(5,v*0.02))))
```

**Answer:** The fees are `5`, `8` and `5`, and the total is `18`. The 150 parcel is 3 at 2%, so the minimum of 5 applies.

<!-- Image 3: Fee Worksheet. See Images/Logical/MAP.md -->

## Use Cases

### Insurance Fee Floor

**Scenario:** A shipping desk calculates insurance for every parcel in a long list, with a minimum charge on low-value items.

```excel
=MAP(C2:C200,LAMBDA(v,MAX(5,v*0.02)))
```

**Why It Works:** MAX returns the larger of the minimum and the percentage. The rule applies to every row without copying the formula down.

### Text Cleanup

**Scenario:** An imported customer list has stray spaces and mixed capitalization in the names.

```excel
=MAP(A2:A500,LAMBDA(s,PROPER(TRIM(s))))
```

**Why It Works:** TRIM removes extra spaces and PROPER capitalizes each word, so one formula cleans the whole column.

### Unit Conversion Column

**Scenario:** A product sheet stores lengths in inches, and a shared report needs centimeters.

```excel
=MAP(B2:B50,LAMBDA(i,ROUND(i*2.54,1)))
```

**Why It Works:** The conversion factor and the rounding rule sit in one LAMBDA. Changing the rounding changes the whole column at once.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` (Incorrect Parameters) | The LAMBDA has a different number of parameters than arrays in Microsoft Excel. | Give the LAMBDA one parameter for each array. |
| Array arguments different size | The arrays have different numbers of items. | Use ranges of the same length. |
| Single value expected | The LAMBDA returns an array for an item. | Return one value per item, or use BYROW for row-level calculations. |
| Argument must be a LAMBDA | The last argument is a range or a value instead of a LAMBDA. | Put the LAMBDA as the last argument. |
| Invalid name | A parameter name matches a cell reference, such as `C1`. | Use names such as `x`, `v` or `value`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web) and Excel 2024 (Windows and Mac) | The LAMBDA must have one parameter for each array. Not listed for Excel 2021. |
| Google Sheets | Available | Each array needs one name in the LAMBDA. A named function can replace the LAMBDA without parentheses. Mismatched array sizes return an error. |

## Tips and Best Practices

- Keep the arrays in the same order as the LAMBDA names, because the first name always takes the first array.
- Check that every array has the same number of items before you map two of them together.
- Use IF inside the LAMBDA to handle blanks, rather than cleaning the source data first.
- Use BYROW or BYCOL when the calculation needs a whole row or column, not a single item.
- Wrap MAP in SUM, AVERAGE or another aggregate when you need a total instead of the spilled list.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LAMBDA](LAMBDA.md) | Defines the calculation MAP applies to each item. |
| [REDUCE](REDUCE.md) | Combines items into one result instead of returning an array. |
| [SCAN](SCAN.md) | Returns each running step of a combining calculation. |
| [MAKEARRAY](MAKEARRAY.md) | Builds a new array from row and column numbers rather than from existing items. |
| [BYROW](BYROW.md) | Applies a LAMBDA to each row, so the calculation sees the whole row. |
| [BYCOL](BYCOL.md) | Applies a LAMBDA to each column, so the calculation sees the whole column. |

## Official Documentation

- [Microsoft Support: MAP function](https://support.microsoft.com/en-us/excel/functions/map-function)
- [Google Docs Editors Help: MAP](https://support.google.com/docs/answer/12568985)
