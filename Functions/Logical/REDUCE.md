---
domain: Spreadsheet Functions
category: Logical
subcategory: Lambda Helpers
purpose:
  - Aggregation
  - Conditional Logic
use-case:
  - Compound Growth Factors
  - Highest Value Search
  - Positive Amount Totals
related:
  - LAMBDA
  - LET
  - MAP
  - SCAN
  - SUM
  - SUMPRODUCT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/reduce-function
  - https://support.google.com/docs/answer/12568597
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Accumulate Values
  - Fold Array
tags:
  - aggregation
  - dynamic-array
  - excel
  - lambda
  - sheets
---

# REDUCE

## Description

**REDUCE** combines the items of an array into one value. It starts with an initial value, called the accumulator, and calls a LAMBDA once for each item. The LAMBDA receives the current accumulator and the current item, and its result becomes the accumulator for the next item. When every item has been processed, REDUCE returns the final accumulator.

Use REDUCE when the way items combine is not a plain sum or count. Examples include compounding growth rates, keeping only positive amounts, or finding a highest value under a custom rule. For a plain sum, SUM or SUMPRODUCT is shorter and easier to read.

The initial value sets the starting point and must match the calculation. Use 0 for a sum, 1 for a product and an empty string for text. A product that starts at 0 stays at 0 no matter how many items follow.

## Syntax

```excel
=REDUCE([initial_value], array, LAMBDA(accumulator, value, calculation))
```

Google Sheets uses the same arguments with the initial value required: `REDUCE(initial_value, array_or_range, LAMBDA)`.

<!-- Image 1: Syntax Anatomy. See Images/Logical/REDUCE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `initial_value` | Optional in Excel, required in Sheets | The starting value of the accumulator. If Excel omits it, the first item of the array is used. |
| `array` | Yes | The array or range to reduce. Items are read row by row. |
| `LAMBDA` | Yes | A LAMBDA with an accumulator name, a value name and a final calculation. The calculation must return one value for each item. |

### Return Value

A single value: the accumulator after the last item. An invalid LAMBDA, or a LAMBDA with the wrong number of parameters, returns `#VALUE!` in Microsoft Excel.

## Examples

### Example 1: Summing Squares

```excel
=REDUCE(0,A2:A4,LAMBDA(acc,v,acc+v^2))
```

**Result:** `14` when A2:A4 hold 1, 2 and 3.

The accumulator starts at 0. Each item adds its square: 0 + 1 = 1, then 1 + 4 = 5, then 5 + 9 = 14.

### Example 2: Multiplying Items

```excel
=REDUCE(1,A2:A4,LAMBDA(acc,v,acc*v))
```

**Result:** `24` when A2:A4 hold 3, 2 and 4.

The starting value is 1, because multiplying by 0 would leave the product at 0. The steps are 1 × 3 = 3, 3 × 2 = 6 and 6 × 4 = 24.

<!-- Image 2: Accumulator Steps for REDUCE. See Images/Logical/REDUCE.md -->

### Example 3: Counting Even Numbers

```excel
=REDUCE(0,A2:A7,LAMBDA(acc,v,acc+IF(MOD(v,2)=0,1,0)))
```

**Result:** `3` when A2:A7 hold 4, 7, 10, 3, 8 and 1.

Each even number adds 1 to the count and each odd number adds nothing. The even values are 4, 10 and 8.

### Example 4: Joining Text

```excel
=REDUCE("",A2:A4,LAMBDA(acc,v,acc&v))
```

**Result:** `abc` when A2:A4 hold a, b and c.

The starting value is an empty string, so the first step adds "a" to nothing. Each item is appended to the text built so far.

### Example 5: Using a Named Calculation

```excel
=REDUCE(100,B2:B3,LAMBDA(acc,r,acc*(1+r)))
```

**Result:** `110.25` when B2:B3 hold 0.05 and 0.05.

The balance of 100 grows by 5% twice: 100 × 1.05 = 105, then 105 × 1.05 = 110.25. Each rate in the range is applied to the balance left by the step before it.

## Story Problems

### Problem 1: Compound Growth Over Three Months

A savings balance of 1000 changes by a growth factor each month: 1.02, then 1.05, then 0.98.

| Month | Growth Factor |
| --- | --- |
| January | 1.02 |
| February | 1.05 |
| March | 0.98 |

**Task:** Apply the three factors to the starting balance of 1000 in one formula.

**Solution:**

```excel
=REDUCE(1000,B2:B4,LAMBDA(acc,g,acc*g))
```

**Answer:** `1049.58`. The balance goes 1000 × 1.02 = 1020, then 1020 × 1.05 = 1071, then 1071 × 0.98 = 1049.58.

<!-- Image 3: Growth Worksheet. See Images/Logical/REDUCE.md -->

### Problem 2: Totaling Only Positive Amounts

A ledger has five amounts, and the negative amounts are refunds that should not be added to the total of sales.

| Amount |
| --- |
| 120 |
| -20 |
| 75 |
| -5 |
| 40 |

**Task:** Total only the positive amounts with one REDUCE formula.

**Solution:**

```excel
=REDUCE(0,A2:A6,LAMBDA(acc,v,IF(v>0,acc+v,acc)))
```

**Answer:** `235`. The positive amounts are 120, 75 and 40, and the refunds are skipped.

## Use Cases

### Compound Growth Factors

**Scenario:** A planning model applies a list of annual growth rates to a starting revenue figure.

```excel
=REDUCE(StartRevenue,GrowthRates,LAMBDA(acc,g,acc*g))
```

**Why It Works:** The starting value and the list of factors are both on the sheet, so a new year changes the inputs rather than the formula. Each factor is multiplied into the running total.

### Highest Value Search

**Scenario:** A team wants the highest score in a list of non-negative results, without sorting the data.

```excel
=REDUCE(0,Scores,LAMBDA(best,s,MAX(best,s)))
```

**Why It Works:** MAX keeps the larger of the current best and the next score. The starting value of 0 works only when every score is zero or above, so use the lowest possible score for other data.

### Positive Amount Totals

**Scenario:** A sales report needs a total of positive transactions, while refunds stay in the source data.

```excel
=REDUCE(0,Amounts,LAMBDA(acc,v,IF(v>0,acc+v,acc)))
```

**Why It Works:** The IF inside the LAMBDA decides whether each item is added, so the filter is part of the calculation and needs no helper column.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` (Incorrect Parameters) | The LAMBDA does not have two names followed by a calculation, or it is not a LAMBDA. | Write the LAMBDA with an accumulator name, a value name and a calculation. |
| Result stays 0 | The product starts at 0. | Use 1 as the initial value for a product. |
| Single value expected | The calculation returns an array for an item. | Return one value per item. |
| Invalid name | A name matches a cell reference, such as `B2`. | Use names such as `acc` and `v`. |
| Missing initial value in Sheets | The Sheets syntax has no optional initial value. | Supply the initial value, such as 0, 1 or `""`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Microsoft Office and Office for iPhone | The initial value is optional. The Microsoft page does not list Excel 2024 or Excel 2021. |
| Google Sheets | Available | The initial value is required. The LAMBDA takes two names, the accumulator and the value, and a named function can be passed without parentheses. |

## Tips and Best Practices

- Choose the initial value that matches the operation: 0 for a sum, 1 for a product, and "" for text.
- Put filters inside the LAMBDA with IF, so the source data stays unchanged.
- Use SCAN when you need every intermediate step, not only the final result.
- For a plain total, use SUM or SUMPRODUCT, because they are easier to read.
- Test with a short list before you point REDUCE at a long range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SCAN](SCAN.md) | Returns each intermediate step of the same kind of calculation. |
| [LAMBDA](LAMBDA.md) | Defines the accumulator-and-value calculation REDUCE uses. |
| [MAP](MAP.md) | Transforms each item and returns an array rather than one value. |
| [LET](LET.md) | Names intermediate values inside the LAMBDA when a step is long. |
| [SUM](../Math%20%26%20Trig/SUM.md) | Adds a range directly. Use it when no per-item rule is needed. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Multiplies matching arrays and adds the results in one step. |

## Official Documentation

- [Microsoft Support: REDUCE function](https://support.microsoft.com/en-us/excel/functions/reduce-function)
- [Google Docs Editors Help: REDUCE](https://support.google.com/docs/answer/12568597)
