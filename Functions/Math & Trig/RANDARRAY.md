---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Random Numbers
purpose:
  - Array Shaping
  - Randomization
use-case:
  - Mock Data Generation
  - Monte Carlo Simulation Grids
  - Randomized Survey Samples
related:
  - CHOOSEROWS
  - RAND
  - RANDBETWEEN
  - ROUND
  - SEQUENCE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/randarray-function
  - https://support.google.com/docs/answer/9211904
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Random Array
tags:
  - dynamic-array
  - excel
  - randomization
  - sheets
---

# RANDARRAY

## Description

**RANDARRAY** returns a block of random numbers in one formula. You choose the number of rows and columns, and the function fills the block with random values. Without any arguments, it returns a single random decimal from 0 up to 1. In Excel, the function can also set a minimum and maximum, and it can return whole numbers instead of decimals.

Use RANDARRAY when you need many random values at once, such as sample data, a grid for a simulation, or a column of random sort keys. A single RAND formula returns one value, so a block of RAND results needs a copy of the formula in every cell. RANDARRAY needs only one formula, and Excel spills the result into the cells below and to the right of it.

Excel's arguments give fine control over the output. The optional `min` and `max` set the bounds, and `whole_number` returns integers when set to TRUE. Google Sheets accepts only the rows and columns, so it returns decimals from 0 to 1 and needs a simple formula to change the range or make whole numbers.

## Syntax

```excel
=RANDARRAY([rows], [columns], [min], [max], [whole_number])
```

<!-- Image 1: Argument Order for RANDARRAY. See Images/Math & Trig/RANDARRAY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rows` | No | The number of rows in the returned array. When omitted with no other arguments, the result is a single value. |
| `columns` | No | The number of columns in the returned array. Set this with `rows` for a block. |
| `min` | No | The smallest number returned. The default is 0. Must be less than `max`. |
| `max` | No | The largest number returned. The default is 1. Must be greater than `min`. |
| `whole_number` | No | TRUE returns whole numbers. FALSE, or omitted, returns decimals. Excel only. |

### Return Value

An array of random numbers sized by `rows` and `columns`. When both are omitted, the result is one decimal from 0 up to 1. If `min` is not less than `max` in Excel, the function returns `#VALUE!`. The array spills into the empty cells beside and below the formula.

<!-- Image 2: Spill Area for a Random Block. See Images/Math & Trig/RANDARRAY.md -->

## Examples

### Example 1: A Block of Decimals From 0 to 1

```excel
=RANDARRAY(3,2)
```

**Result:** a 3 row by 2 column block of decimals, each from 0 up to, but not including, 1

The formula fills six cells with independent random decimals. Because the array spills, the cells below and to the right of the formula must be empty.

### Example 2: Simulated Dice Rolls

```excel
=RANDARRAY(5,1,1,6,TRUE)
```

**Result:** five whole numbers, each from 1 to 6

The minimum is 1 and the maximum is 6, and TRUE returns whole numbers. The result is a column that behaves like five dice rolls.

### Example 3: Decimals Between 10 and 20

```excel
=RANDARRAY(4,1,10,20)
```

**Result:** four decimals, each from 10 up to 20

The bounds replace the defaults of 0 and 1. Leaving `whole_number` out returns decimals.

### Example 4: One Value From 0 to 1

```excel
=RANDARRAY()
```

**Result:** a single decimal from 0 up to, but not including, 1

With no arguments, the function returns one value in one cell, as RAND does.

### Example 5: Two by Two Whole Numbers From 0 to 100

```excel
=ROUND(RANDARRAY(2,2)*100, 0)
```

**Result:** a 2 by 2 block of whole numbers from 0 to 100

RANDARRAY produces decimals from 0 to 1, multiplying by 100 scales them to 0 to 100, and ROUND returns whole numbers. This method works in Google Sheets, which lacks the `min`, `max` and `whole_number` arguments.

## Story Problems

### Problem 1: Mock Order Quantities for a Training File

A training team needs six rows of sample order quantities. Each quantity should be a whole number from 1 to 50.

| Item | Value |
| --- | --- |
| Rows Needed | 6 |
| Smallest Quantity | 1 |
| Largest Quantity | 50 |

**Task:** Write one formula that creates the six whole-number quantities.

**Solution:**

```excel
=RANDARRAY(6,1,1,50,TRUE)
```

**Answer:** A column of six whole numbers, each from 1 to 50, which spills downward from the formula cell. The values change on each recalculation, so paste them as values before distributing the file.

### Problem 2: Random Multipliers for a Simulation Grid

A planner runs a simulation with a 3 by 3 grid of multipliers. Each multiplier should be a decimal between 0.9 and 1.1.

| Item | Value |
| --- | --- |
| Grid Rows | 3 |
| Grid Columns | 3 |
| Lowest Multiplier | 0.9 |
| Highest Multiplier | 1.1 |

**Task:** Write one formula that creates the 3 by 3 grid of multipliers.

**Solution:**

```excel
=RANDARRAY(3,3,0.9,1.1)
```

**Answer:** A 3 by 3 block of decimals, each from 0.9 up to 1.1. Every multiplier falls inside that range, and the block changes on each recalculation.

## Use Cases

### Mock Data Generation

**Scenario:** A developer needs a large test list of ticket counts for a dashboard before the live data is connected.

```excel
=RANDARRAY(B2,1,1,500,TRUE)
```

**Why It Works:** The number of rows comes from `B2`, and the formula fills them with whole numbers from 1 to 500. Paste the values once the test data is fixed, so that the dashboard does not change during review.

### Monte Carlo Simulation Grids

**Scenario:** A finance analyst multiplies a forecast by a grid of random factors to test how sensitive the result is.

```excel
=RANDARRAY(B2,B3,0.9,1.1)*C2
```

**Why It Works:** The grid holds one random factor per cell, and multiplying by the base forecast in `C2` returns a grid of scenario values. The spread of the results shows how much the forecast could move.

### Randomized Survey Samples

**Scenario:** A researcher selects a random sample of customers from a list that has no useful order.

```excel
=RANDARRAY(COUNTA(A2:A50),1)
```

**Why It Works:** The formula creates one random key for each customer name in `A2:A50`. Place the keys beside the names, sort by the key column, and take the top rows as the sample. Paste the sorted result as values to keep the sample fixed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The `min` argument is not less than `max` in Excel. | Swap the bounds, or check the values in the cells that supply them. |
| `#SPILL!` | Cells below or beside the formula are not empty. | Clear the cells in the spill area, then recalculate. |
| Decimals appear instead of whole numbers | The `whole_number` argument is omitted or FALSE. | Set `whole_number` to TRUE in Excel, or wrap the result in ROUND. |
| Values change after a report is sent | The formula recalculates whenever the sheet changes. | Paste the array as values before sharing the file. |
| Google Sheets returns only decimals from 0 to 1 | Sheets accepts only rows and columns. | Multiply by the range width, add the lower bound, and wrap in ROUND if needed. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, and Excel for iPad, iPhone and Android | The official Applies To list does not include Excel 2019 or Excel 2016. Supports `min`, `max` and `whole_number`. |
| Google Sheets | Available | Accepts `rows` and `columns` only. Returns decimals from 0 to 1. The official page says a value for rows is required when columns is given. |

## Tips and Best Practices

- Use TRUE for `whole_number` when the values stand for counts, quantities or dice.
- Set `min` and `max` in the formula rather than scaling the result in another column.
- Leave the spill area empty, because a single non-empty cell blocks the entire array.
- Paste the array as values before you share or archive the results.
- Give the formula its row count from a cell, so the grid resizes when the plan changes.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSEROWS](../Lookup%20%26%20Reference/CHOOSEROWS.md) | Picks specific rows from an array, useful after sorting by random keys. |
| [RAND](RAND.md) | Returns one random decimal, so a block needs a formula in every cell. |
| [RANDBETWEEN](RANDBETWEEN.md) | Returns one random whole number between two bounds. |
| [ROUND](ROUND.md) | Converts decimals to whole numbers or a fixed number of places. |
| [SEQUENCE](SEQUENCE.md) | Creates an ordered array of numbers, useful as a row index. |

## Official Documentation

- [Microsoft Support: RANDARRAY function](https://support.microsoft.com/en-us/excel/functions/randarray-function)
- [Google Docs Editors Help: RANDARRAY](https://support.google.com/docs/answer/9211904)
