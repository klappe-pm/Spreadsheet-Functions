---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Data Cleaning
  - Statistical Analysis
use-case:
  - Budget Variance Reporting
  - Distance Between Readings
  - Tolerance Checks
related:
  - IF
  - ROUND
  - SIGN
  - SQRT
  - SUMPRODUCT
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/abs-function
  - https://support.google.com/docs/answer/3093459
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Absolute Value
  - Distance From Zero
  - Magnitude
tags:
  - arithmetic
  - excel
  - magnitude
  - sheets
  - variance
---

# ABS

## Description

**ABS** returns the absolute value of a number, which is its distance from zero with the sign removed. A positive number comes back unchanged, a negative number comes back as its positive equivalent, and zero stays zero. So `ABS(-15)` and `ABS(15)` both return 15.

Use ABS when the size of a value matters and its direction does not. A budget report might need the size of each variance whether the spending came in over or under plan. A distance between two readings is always positive, whichever reading is larger. Tolerance checks use ABS to turn a two-sided test into a single comparison.

ABS changes only the sign. It does not round or scale the number. Because of this, a column of mixed positive and negative values can net to a small total with SUM, while the sum of the absolute values shows the total movement. Choose the function that matches the question you are answering.

## Syntax

```excel
=ABS(number)
```

<!-- Image 1: Absolute Value on a Number Line. See Images/Math & Trig/ABS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The real number whose absolute value you want. It can be a typed number, a cell reference, or the result of another formula. |

### Return Value

A non-negative number. Positive numbers and zero return unchanged, and negative numbers return the positive equivalent. A value that cannot be read as a number returns `#VALUE!`.

## Examples

### Example 1: Negative Input

```excel
=ABS(-15)
```

**Result:** `15`

The minus sign is removed and the magnitude is returned.

### Example 2: Absolute Difference Between Two Cells

Budget in `B2` is 120 and actual in `C2` is 95.

```excel
=ABS(B2-C2)
```

**Result:** `25`

The result is 25 whichever cell is larger, so swapping `B2` and `C2` gives the same answer.

<!-- Image 2: Difference in Both Directions. See Images/Math & Trig/ABS.md -->

### Example 3: Sum of Magnitudes Without Cancellation

Values in `D2:D6` are 500, -300, 120, -80 and -45.

```excel
=SUMPRODUCT(ABS(D2:D6))
```

**Result:** `1045`

Plain `SUM(D2:D6)` returns 195 because the negative values offset the positive ones. Taking the absolute value of each cell first adds up the movement in both directions.

### Example 4: Tolerance Test

Measured value in `E2` is 10.2 and the target in `F2` is 10.5.

```excel
=IF(ABS(E2-F2)<=0.5,"Within tolerance","Adjust")
```

**Result:** `Within tolerance`

The difference is 0.3, which is inside the 0.5 band. The test works the same whether the measurement is above or below the target.

## Story Problems

### Problem 1: Monthly Budget Variance

A team budgets 5000 for marketing each month. Spending for the first four months is below.

| Month | Budget | Actual |
| --- | --- | --- |
| Jan | 5000 | 4700 |
| Feb | 5000 | 5350 |
| Mar | 5000 | 4980 |
| Apr | 5000 | 5120 |

**Task:** Find the total size of the variances, counting over-spend and under-spend as separate amounts of movement.

**Solution:**

```excel
=SUMPRODUCT(ABS(C2:C5-B2:B5))
```

**Answer:** `790`, because the variances are 300, 350, 20 and 120. The net variance is only 150, which hides how much the spending moved.

<!-- Image 3: Variance Table With Signed and Absolute Values. See Images/Math & Trig/ABS.md -->

### Problem 2: Part Width Check

A machine shop cuts parts to a target width of 25.00 mm with a tolerance of 0.05 mm on either side.

| Part | Width (mm) |
| --- | --- |
| P-101 | 25.03 |
| P-102 | 24.96 |
| P-103 | 25.08 |
| P-104 | 24.99 |

**Task:** Count the parts whose width is within tolerance.

**Solution:**

```excel
=SUMPRODUCT(--(ABS(B2:B5-25)<=0.05))
```

**Answer:** `3`. Parts P-101, P-102 and P-104 are within 0.05 mm of target. P-103 is 0.08 mm over and fails.

## Use Cases

### Budget Variance Reporting

**Scenario:** A finance analyst needs a list of departments whose spending moved more than 10 percent from budget, whether they overspent or underspent.

```excel
=IF(ABS(C2-B2)/B2>0.1,"Review","OK")
```

**Why It Works:** `ABS(C2-B2)` gives the size of the variance and dividing by the budget converts it to a rate. Keep the signed difference in another column when the report also needs to show direction.

### Distance Between Readings

**Scenario:** A logistics team records the odometer reading at each stop and wants the distance between two stops, regardless of the order in which they were entered.

```excel
=ABS(B3-B2)
```

**Why It Works:** Subtracting in either order can produce a negative number, and ABS makes the distance positive.

### Tolerance Checks

**Scenario:** A quality team accepts a batch when each sample's weight is within a fixed band around the target weight.

```excel
=IF(ABS(D2-Target)<=Tolerance,"Accept","Reject")
```

**Why It Works:** One comparison covers both the lower and upper limits, so the formula is easier to audit than two separate tests.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text that cannot be read as a number, or a cell that holds an error. | Convert the value to a number or correct the referenced cell. |
| Total looks too small | `SUM` was applied to values that include negatives, so they offset each other. | Use `SUMPRODUCT(ABS(range))` to add the magnitudes. |
| `#NAME?` | The function name is misspelled. | Type `ABS`, not `ABSOLUTE`. |
| Total is wrong in older Excel | `SUM(ABS(range))` was entered without array handling, so ABS used only one cell. | Use `SUMPRODUCT(ABS(range))`, which handles arrays in every version. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Works element by element inside `SUMPRODUCT` and in dynamic array formulas. |
| Google Sheets | Available | Same arguments and results for real numbers. Use `ARRAYFORMULA` or `SUMPRODUCT` to apply it to a range. |

## Tips and Best Practices

- Use ABS when direction does not matter. Keep the signed value when debits and credits, or gains and losses, need separate treatment.
- Use `SUMPRODUCT(ABS(range))` instead of `SUM(ABS(range))` so the formula works in every version of Excel.
- Replace two comparisons such as `AND(x>=low, x<=high)` with `ABS(x-target)<=band` for a symmetric tolerance.
- To sort by size regardless of sign, add a helper column with the ABS values and sort on that column.
- Combine `ABS(x)` with `SIGN(y)` to give the size of `x` the direction of `y`.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SIGN](SIGN.md) | Returns -1, 0 or 1. Use it when the direction is needed without the size. |
| [SQRT](SQRT.md) | Returns a square root. Use it with ABS in distance formulas. |
| [SUMPRODUCT](SUMPRODUCT.md) | Sums the results of ABS across a range. |
| [IF](../Logical/IF.md) | Applies ABS inside a tolerance or threshold test. |
| [ROUND](ROUND.md) | Rounds a result after ABS has removed the sign. |

## Official Documentation

- [Microsoft Support: ABS function](https://support.microsoft.com/en-us/excel/functions/abs-function)
- [Google Docs Editors Help: ABS](https://support.google.com/docs/answer/3093459)
