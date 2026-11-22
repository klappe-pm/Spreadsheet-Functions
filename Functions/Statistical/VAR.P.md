---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
purpose:
  - Statistical Analysis
use-case:
  - Entire Population Variance
  - Factory Output Spread
related:
  - DVARP
  - STDEV.P
  - VAR.S
  - VARP
  - VARPA
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/var-p-function
  - https://support.google.com/docs/answer/3094113
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Population Variance
tags:
  - dispersion
  - excel
  - population
  - sheets
  - variance
---

# VAR.P

## Description

**VAR.P** calculates the variance of a complete population. It measures how widely the values spread around their mean, and it treats every value you supply as the entire group of interest. The result divides the sum of squared deviations by the number of values, so it is slightly smaller than the sample variance of the same numbers.

Use VAR.P when the numbers cover everything you care about, such as every machine on a line, every branch in a region or every order placed in a month. Use VAR.S when the numbers are a sample drawn from a larger group. Using VAR.P on a sample understates the spread, and using VAR.S on a complete population overstates it.

VARP is the legacy function that returns the same population variance. Use VAR.P in new formulas. Arguments can be numbers, names, arrays or references, and when a range is supplied the function skips empty cells, logical values and text. To include logical values and numeric text from a range, use VARPA. The square root of VAR.P is the population standard deviation, which STDEV.P returns directly.

## Syntax

```excel
=VAR.P(number1,[number2],...)
```

<!-- Image 1: Population Divisor Compared With Sample Divisor. See Images/Statistical/VAR.P.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, reference or array that holds population values. |
| `number2, ...` | No | Up to 253 more numbers, references or arrays from the same population, for a total of 254 arguments. Numbers typed directly into the list are counted, including logical values and numeric text. |

### Return Value

A number: the population variance. The function returns an error when an argument is an error value or when text typed directly into the list cannot be converted to a number. Empty cells, logical values and text inside a range are skipped.

## Examples

All examples use six values in `A2:A7`: 4, 8, 6, 5, 3 and 7. Their mean is 5.5 and the sum of squared deviations is 17.5.

### Example 1: Population Variance of a Range

```excel
=VAR.P(A2:A7)
```

**Result:** `2.9167`

Dividing 17.5 by six, the number of values, gives 2.9167. This is the variance when the six values are the entire population.

### Example 2: Add a Seventh Value

```excel
=VAR.P(A2:A7,10)
```

**Result:** `4.9796`

Adding 10 raises the mean to 6.14 and the population variance to 4.9796. The divisor becomes seven.

### Example 3: Standard Deviation of the Population

```excel
=SQRT(VAR.P(A2:A7))
```

**Result:** `1.7078`

The square root of the population variance is the population standard deviation, in the same units as the values.

### Example 4: Empty Cells Are Skipped

```excel
=VAR.P(A2:A9)
```

**Result:** `2.9167`

When `A8` and `A9` are empty, they do not count toward the number of values, so the result matches Example 1.

### Example 5: Values Typed Directly

```excel
=VAR.P(4,8,6,5,3,7)
```

**Result:** `2.9167`

Typing the population values into the formula gives the same result as referencing the range.

## Story Problems

### Problem 1: Output of Every Machine

A plant has five identical machines, and the supervisor records the output of each machine in units per hour in `A2:A6`. The five machines are the entire fleet, so the supervisor wants the population variance of their output.

| Machine | Output (units per hour) |
| --- | --- |
| M1 | 42 |
| M2 | 47 |
| M3 | 39 |
| M4 | 51 |
| M5 | 46 |

**Task:** Compute the population variance of the five machine outputs.

**Solution:**

```excel
=VAR.P(B2:B6)
```

**Answer:** `17.2`. The mean output is 45 units per hour. The squared deviations add up to 86, and dividing by five gives 17.2.

<!-- Image 2: Machine Output Population Result. See Images/Statistical/VAR.P.md -->

### Problem 2: Defects Across Four Shifts

A factory runs four shifts a day, and the quality team records defects per shift for one day in `A2:A5`. Those four shifts are every shift the plant operates, so the population variance describes the whole day.

| Shift | Defects |
| --- | --- |
| Early | 3 |
| Day | 5 |
| Late | 2 |
| Night | 6 |

**Task:** Compute the population variance of the four defect counts.

**Solution:**

```excel
=VAR.P(A2:A5)
```

**Answer:** `2.5`. The mean is four defects per shift. The squared deviations add up to 10, and dividing by four gives 2.5.

## Use Cases

### Factory Output Spread

**Scenario:** A production planner checks whether the output of all machines on one line is consistent enough to schedule shared work.

```excel
=SQRT(VAR.P(Machines[Output]))
```

**Why It Works:** Every machine on the line is included, so the population version is correct. The square root gives a standard deviation the planner can compare with the target.

### Entire Population Variance

**Scenario:** A regional manager compares monthly sales across all branches, since every branch is part of the report.

```excel
=VAR.P(Branches[MonthlySales])
```

**Why It Works:** The table holds every branch, so VAR.P describes the whole region without treating the branches as a sample.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | An argument is an error value, or text typed directly into the list cannot be converted to a number. | Correct the source cell or the typed value. |
| Unexpected result | The values are a sample from a larger group, so the result understates the spread. | Use VAR.S when the values are a sample. |
| Unexpected result | Logical values and text inside a range are skipped. | Use VARPA when logical values should count as 1 or 0. |
| Unexpected result | A header or label cell inside the range holds a number that is not a data value. | Select only the cells that hold data values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows and Mac), Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Accepts up to 254 arguments. Logical values and text inside a range are skipped. |
| Google Sheets | Available as an alias | The Sheets help page for VAR.P refers to VARP, which calculates the variance of an entire population. |

## Tips and Best Practices

- Use VAR.P only when the data covers every item in the group you are describing.
- Use VAR.S when the data is a sample, because the sample version is larger and more honest about uncertainty.
- Report the population standard deviation with STDEV.P for results in the original units.
- Keep the range limited to the population members, so that unrelated totals do not enter the calculation.
- Use VARPA when a range holds logical flags that should count as 1 or 0.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DVARP](../Database/DVARP.md) | Population variance of the records that match database criteria. |
| [STDEV.P](STDEV.P.md) | Population standard deviation, the square root of this result. |
| [VAR.S](VAR.S.md) | Sample variance that divides by one fewer than the number of values. |
| [VARP](VARP.md) | Legacy population variance that returns the same result. |
| [VARPA](VARPA.md) | Population variance that counts logical values inside a range. |

## Official Documentation

- [Microsoft Support: VAR.P function](https://support.microsoft.com/en-us/excel/functions/var-p-function)
- [Google Docs Editors Help: VARP](https://support.google.com/docs/answer/3094113)
