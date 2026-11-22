---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
purpose:
  - Statistical Analysis
use-case:
  - Call Center Wait Consistency
  - Machine Run Time Spread
  - Pooled Within-Group Spread
related:
  - AVEDEV
  - STDEV.S
  - SUMSQ
  - VAR.P
  - VAR.S
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/devsq-function
  - https://support.google.com/docs/answer/3093625
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sum Of Squared Deviations
  - Squared Deviation Sum
tags:
  - excel
  - sheets
  - spread
  - variance
---

# DEVSQ

## Description

**DEVSQ** returns the sum of squared deviations. For each data point it finds the distance from the sample mean, squares that distance, and adds the squares together. The result measures how spread out the values are, expressed as a total rather than an average.

DEVSQ returns a sum, not a variance. To turn it into a variance, divide by the number of points minus 1 for a sample, which gives the same result as VAR.S. Divide by the number of points for a population, which gives the same result as VAR.P. Dividing the sum by a count is the step that most often causes confusion, so check which divisor your analysis needs.

DEVSQ accepts numbers typed directly into the argument list and ranges or arrays. In a range or an array, text, logical values and empty cells are ignored, and cells that contain zero are included. Microsoft lists the function for up to 255 arguments in total.

## Syntax

```excel
=DEVSQ(number1, [number2], ...)
```

<!-- Image 1: DEVSQ Syntax Anatomy. See Images/Statistical/DEVSQ.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first value, array or range to include. |
| `number2, ...` | No | Additional values, arrays or ranges. Up to 255 arguments in total. A single range can also hold all the values. |

### Return Value

A number: the sum of the squared differences between each value and the mean of the values. It returns 0 when every value is the same. An error value in the arguments, or text that cannot be converted to a number when typed directly into the list, causes an error.

## Examples

### Example 1: Call Wait Times in a Range

Column A holds five call wait times in seconds in `A2:A6`: 12, 15, 9, 14 and 10.

```excel
=DEVSQ(A2:A6)
```

**Result:** `26`

The mean is 12. The squared distances are 0, 9, 9, 4 and 4, which add up to 26.

### Example 2: Values Typed Into the Formula

```excel
=DEVSQ(2, 4, 6, 8)
```

**Result:** `20`

The mean is 5. The distances are -3, -1, 1 and 3, and their squares add up to 9 plus 1 plus 1 plus 9, which is 20.

### Example 3: Blank Cells Are Ignored

The same list as Example 1, with an empty cell in `A7`.

```excel
=DEVSQ(A2:A7)
```

**Result:** `26`

The empty cell is not included in the calculation, so the result does not change. A zero typed into `A7` would be included and would change the result.

### Example 4: Dividing for a Sample Variance

```excel
=DEVSQ(A2:A6) / (COUNT(A2:A6) - 1)
```

**Result:** `6.5`

Dividing the sum of 26 by the four degrees of freedom gives 6.5. VAR.S returns the same value for these five numbers.

<!-- Image 2: Sum of Squares to Variance. See Images/Statistical/DEVSQ.md -->

## Story Problems

### Problem 1: Machine Run Times on a Shop Floor

A maintenance team logs the run time in minutes for six sampled machines in `A1:B7`.

| Machine | Run Time |
| --- | --- |
| Press 1 | 30 |
| Press 2 | 42 |
| Press 3 | 35 |
| Press 4 | 50 |
| Press 5 | 28 |
| Press 6 | 43 |

**Task:** Find the sum of squared deviations of the run times.

**Solution:**

```excel
=DEVSQ(B2:B7)
```

**Answer:** `358`. The mean run time is 38 minutes. The squared distances are 64, 16, 9, 144, 100 and 25, which sum to 358.

<!-- Image 3: Machine Run Time Result. See Images/Statistical/DEVSQ.md -->

### Problem 2: Spread of Test Scores in a Class

A teacher records the test scores of five students in `A1:B6` and wants the sum of squared deviations, then the sample variance from it.

| Student | Score |
| --- | --- |
| Amara | 72 |
| Bo | 85 |
| Cruz | 90 |
| Dana | 64 |
| Eli | 79 |

**Task:** Find the sum of squared deviations of the scores, then divide it by one less than the number of students.

**Solution:**

```excel
=DEVSQ(B2:B6)
```

**Answer:** `426`. The mean score is 78. Dividing 426 by 4 gives 106.5, which is the sample variance that VAR.S returns for these scores.

## Use Cases

### Call Center Wait Consistency

**Scenario:** A call center supervisor wants a standard deviation for the wait times in a table, and needs the sum of squares as the first step.

```excel
=SQRT(DEVSQ(Calls[Wait Seconds]) / (COUNT(Calls[Wait Seconds]) - 1))
```

**Why It Works:** The sum of squares divided by n minus 1 is the sample variance, and its square root is the sample standard deviation. The formula matches STDEV.S, and it shows each step of the calculation.

### Machine Run Time Spread

**Scenario:** A plant engineer compares how consistent the run times of one press line are from week to week.

```excel
=DEVSQ(Runs[Minutes])
```

**Why It Works:** Structured references keep the range in step with new runs. The total gives a figure that can be compared with other sums of squares from the same sample size.

### Pooled Within-Group Spread

**Scenario:** A researcher compares two shifts and needs the spread inside each shift added together before running a larger test.

```excel
=DEVSQ(Shift1!B2:B20) + DEVSQ(Shift2!B2:B20)
```

**Why It Works:** Each shift has its own mean, so each DEVSQ measures spread around its own average. Adding the two sums gives the combined within-group total, which larger tests such as analysis of variance use.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result too small | A number is stored as text in a range, so the function skips it. | Convert the text to numbers, for example with `VALUE`, or re-enter the values. |
| Result differs from VAR.S | The sum was not divided by n minus 1. | Divide by `COUNT(range) - 1` to match the sample variance. |
| Error in the result | A text entry was typed directly into the argument list, or an error value sits in a range. | Use cell references for data, and fix the error value at its source. |
| Zero changes the answer | A zero is included, while an empty cell is ignored. | Clear the cell if the value is missing rather than entering zero. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Accepts up to 255 arguments. Text, logical values and empty cells in a range are ignored. |
| Google Sheets | Available | Syntax `DEVSQ(value1, [value2, ...])`. The help page lists examples without sample results. |

## Tips and Best Practices

- Use DEVSQ when you need the total of squared distances, such as for a pooled analysis, and use VAR.S or VAR.P for an average.
- Keep data in one range rather than typing many values into the formula.
- Check the count of numbers with COUNT before you divide, because text and blanks change the count.
- Keep one sample per DEVSQ call when you want the spread of a single group.
- Label the units next to the result, because a sum of squared minutes has units that are harder to read than a standard deviation.

## Related Functions

| Function | Relationship |
| --- | --- |
| [VAR.S](VAR.S.md) | Divides the sum of squares by n minus 1 for a sample variance. |
| [VAR.P](VAR.P.md) | Divides the sum of squares by n for a population variance. |
| [STDEV.S](STDEV.S.md) | Returns the square root of the sample variance. |
| [AVEDEV](AVEDEV.md) | Averages the absolute distances from the mean instead of squaring them. |
| [SUMSQ](../Math%20%26%20Trig/SUMSQ.md) | Adds squares of the values themselves, not of their distances from the mean. |

## Official Documentation

- [Microsoft Support: DEVSQ function](https://support.microsoft.com/en-us/excel/functions/devsq-function)
- [Google Docs Editors Help: DEVSQ](https://support.google.com/docs/answer/3093625)
