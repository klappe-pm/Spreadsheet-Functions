---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Aggregation
  - Statistical Analysis
use-case:
  - Average Unit Cost
  - Course Grade Weighting
  - Survey Result Weighting
related:
  - AVERAGE
  - MEDIAN
  - SUM
  - SUMPRODUCT
level: 3
source:
  - https://support.google.com/docs/answer/9084098
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Weighted Mean
tags:
  - averages
  - sheets
  - statistics
  - weighted-average
---

# AVERAGE.WEIGHTED

## Description

**AVERAGE.WEIGHTED** returns the weighted average of a set of values. Each value is multiplied by its weight, the products are added, and the total is divided by the sum of the weights. A value with a weight of 3 counts three times as much as a value with a weight of 1, which makes the function the right choice when items do not contribute equally.

Use it for course grades where each assignment has a percentage of the final mark, for an average unit cost where each purchase has a quantity, or for survey results where each response has a weight. The result is always on the same scale as the values, so a set of grades gives a grade and a set of prices gives a price.

AVERAGE.WEIGHTED is available in Google Sheets only. Excel has no function with this name. The closest equivalent is SUMPRODUCT divided by SUM, which gives the same result. Each value must have exactly one weight, the weights cannot be negative, and at least one weight must be positive. Weights can be percentages, counts or any other positive numbers, because the function divides by their total.

## Syntax

```excel
=AVERAGE.WEIGHTED(values, weights, [additional values], [additional weights])
```

<!-- Image 1: Values Paired With Weights. See Images/Statistical/AVERAGE.WEIGHTED.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `values` | Yes | The values to average. Can be a cell range or numbers typed directly. |
| `weights` | Yes | The weight for each value, in the same order. Can be a cell range or numbers typed directly. Each value needs exactly one weight. |
| `additional values` | No | More values to include. |
| `additional weights` | No | The weights for the additional values. Each additional value needs exactly one additional weight. |

### Return Value

A number: the sum of each value multiplied by its weight, divided by the sum of the weights. The result is an error when the value and weight counts differ, when a weight is negative, or when every weight is zero. When ranges are used, the weights range must have the same number of rows and columns as the values range.

## Examples

### Example 1: Values and Weights Typed Directly

```excel
=AVERAGE.WEIGHTED(2, 10, 4, 15)
```

**Result:** `3.2`

The products are 20 (2 × 10) and 60 (4 × 15). Their total is 80, and dividing by the total weight of 25 gives 3.2.

### Example 2: Percentage Weights in a Range

Scores in `A2:A4`: 88, 92, 75. Weights in `B2:B4`: 0.3, 0.3, 0.4.

```excel
=AVERAGE.WEIGHTED(A2:A4, B2:B4)
```

**Result:** `84`

The weights already total 1, so the result is simply the weighted sum: 26.4 + 27.6 + 30 = 84.

### Example 3: A Zero Weight

```excel
=AVERAGE.WEIGHTED(50, 0, 70, 1)
```

**Result:** `70`

A weight of 0 removes the first value from the calculation. Only 70, with a weight of 1, remains.

### Example 4: Negative Weights

```excel
=AVERAGE.WEIGHTED(50, -1, 70, 1)
```

**Result:** An error, because negative weights are not allowed.

Weights must be zero or positive. Check the weight column for signs before averaging, especially when weights come from a calculation that can produce negative values.

## Story Problems

### Problem 1: Final Course Grade

A teacher weights three components of a course: homework, quizzes and a final exam. The data is in `A1:C4`.

| Component | Score | Weight |
| --- | --- | --- |
| Homework | 88 | 0.2 |
| Quizzes | 75 | 0.3 |
| Final exam | 92 | 0.5 |

**Task:** Calculate the final course grade using the weights.

**Solution:**

```excel
=AVERAGE.WEIGHTED(B2:B4, C2:C4)
```

**Answer:** `86.1`. The weighted products are 17.6, 22.5 and 46, which total 86.1. The weights total 1, so the result is the final grade.

<!-- Image 2: Results Panel for the Grade Problem. See Images/Statistical/AVERAGE.WEIGHTED.md -->

### Problem 2: Average Unit Cost Across Purchases

A shop buys the same item in three batches at different prices. The batch data is in `A1:C4`.

| Batch | Unit Price | Quantity |
| --- | --- | --- |
| Batch 1 | 4.00 | 100 |
| Batch 2 | 5.50 | 50 |
| Batch 3 | 3.25 | 200 |

**Task:** Find the average cost per unit across all units bought, which means weighting each price by its quantity.

**Solution:**

```excel
=AVERAGE.WEIGHTED(B2:B4, C2:C4)
```

**Answer:** `3.79` per unit, rounded to two decimals. The total spend is 1,325 for 350 units, and 1,325 divided by 350 is 3.7857. A simple AVERAGE of the three prices would give 4.25, which overstates the cost.

## Use Cases

### Average Unit Cost

**Scenario:** A purchasing team reports the blended cost of a product bought at several prices over a quarter.

```excel
=AVERAGE.WEIGHTED(UnitPrices, Quantities)
```

**Why It Works:** Each price is weighted by how many units were bought at that price, so large purchases affect the average more than small ones.

### Course Grade Weighting

**Scenario:** An instructor calculates each student's final grade when the components have different percentages.

```excel
=AVERAGE.WEIGHTED(Scores, Percentages)
```

**Why It Works:** The percentages can be stored as decimals that sum to 1 or as whole numbers. Either way, the function divides by the total weight, so the grade stays on the 0 to 100 scale.

### Survey Result Weighting

**Scenario:** A research team adjusts survey results so that each age group counts in proportion to its share of the population.

```excel
=AVERAGE.WEIGHTED(Responses, PopulationShare)
```

**Why It Works:** Each response is weighted by its group's population share, which corrects for groups that responded at different rates.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error | The number of values does not match the number of weights. | Give each value exactly one weight, and use ranges with the same size. |
| Error | A weight is negative. | Correct the weight, since negative weights are not allowed. |
| Error | Every weight is zero. | Make sure at least one weight is positive. |
| Unexpected result | Blank cells or text in the value or weight ranges are handled differently from numbers. | Clean the ranges first, or test the behavior in your sheet before relying on it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available. Closest alternative: `=SUMPRODUCT(values, weights) / SUM(weights)` | Use SUMPRODUCT with SUM to get the same weighted average. |
| Google Sheets | Available | Accepts values and weights as ranges or typed numbers, with additional pairs. The help page does not describe blank and text handling, so test those cases. |

## Tips and Best Practices

- Keep the values and weights in parallel columns so each weight sits beside its value.
- Check that the weights total the expected amount before reporting a result.
- Use percentages or counts for weights, but keep one convention for the whole table.
- Compare the result with AVERAGE on the same range to see how much the weights change it.
- Use SUMPRODUCT and SUM when the file must open in Excel.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Gives every value the same weight, so it is the unweighted version of this function. |
| [MEDIAN](MEDIAN.md) | Middle value, useful when outliers distort any mean. |
| [SUM](../Math%20%26%20Trig/SUM.md) | Totals the weights in the Excel alternative. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Multiplies values by weights and adds the products, the basis of the Excel alternative. |

## Official Documentation

- [Google Docs Editors Help: AVERAGE.WEIGHTED](https://support.google.com/docs/answer/9084098)
