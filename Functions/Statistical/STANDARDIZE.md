---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Exam Score Comparison
  - Health Measurement Screening
  - Manufacturing Tolerance Checks
related:
  - AVERAGE
  - NORM.DIST
  - NORM.INV
  - NORM.S.DIST
  - STDEV.S
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/standardize-function
  - https://support.google.com/docs/answer/3094102
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Z Score
  - Normalized Value
tags:
  - distribution
  - excel
  - sheets
  - z-score
---

# STANDARDIZE

## Description

**STANDARDIZE** converts a value from a distribution into a normalized value, also called a z-score. The result tells you how many standard deviations the value sits above or below the mean. A result of 0 means the value equals the mean, a result of 1.5 means it is 1.5 standard deviations above the mean, and a negative result means it is below the mean.

Use STANDARDIZE when you need to compare values that come from different scales. A score of 84 on one test and a height of 180 cm cannot be compared directly, but their z-scores can. The function is also a common first step before using a normal distribution function such as NORM.S.DIST to turn a z-score into a probability.

STANDARDIZE does not calculate the mean or the standard deviation for you. Supply both from the same data set, for example with AVERAGE and STDEV.S. The standard deviation must be greater than zero.

## Syntax

```excel
=STANDARDIZE(x, mean, standard_dev)
```

<!-- Image 1: Value, Mean and Standard Deviation Arguments. See Images/Statistical/STANDARDIZE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The value to normalize. |
| `mean` | Yes | The arithmetic mean of the distribution. |
| `standard_dev` | Yes | The standard deviation of the distribution. Must be greater than zero. |

### Return Value

A number: the normalized value, calculated as (x minus mean) divided by standard_dev. The function returns `#NUM!` when `standard_dev` is zero or negative.

## Examples

### Example 1: Basic Normalized Value

```excel
=STANDARDIZE(85, 70, 12)
```

**Result:** `1.25`

The value 85 is 15 points above the mean of 70. Dividing that gap by the standard deviation of 12 gives 1.25.

### Example 2: Values From Cells

With `A2` holding 58, `B2` holding 70 and `C2` holding 12:

```excel
=STANDARDIZE(A2, B2, C2)
```

**Result:** `-1`

The value is exactly one standard deviation below the mean, so the result is negative.

### Example 3: Zero Standard Deviation

```excel
=STANDARDIZE(85, 70, 0)
```

**Result:** `#NUM!`

A standard deviation of zero means every value in the distribution is the same, so no normalized value can be measured. Check the standard deviation before standardizing.

<!-- Image 2: Positive and Negative Results. See Images/Statistical/STANDARDIZE.md -->

### Example 4: Converting to a Probability

```excel
=NORM.S.DIST(STANDARDIZE(85, 70, 12), TRUE)
```

**Result:** `0.8944` (rounded to four decimals)

NORM.S.DIST returns the share of values expected below the z-score. About 89 percent of values in a normal distribution fall below 1.25 standard deviations above the mean.

## Story Problems

### Problem 1: Comparing a Student Score

A teacher has the score for one student and the summary statistics for the whole class.

| Item | Value |
| --- | --- |
| Student score | 84 |
| Class mean | 72 |
| Standard deviation | 8 |

**Task:** Find how far the student sits above the class average, measured in standard deviations.

**Solution:**

```excel
=STANDARDIZE(B2, B3, B4)
```

**Answer:** `1.5`. The student scored one and a half standard deviations above the class mean, which places the student well above average.

### Problem 2: Checking a Machined Bolt

A machine shop targets a bolt length of 50.0 mm with a standard deviation of 0.4 mm across production runs. A bolt measures 50.9 mm.

| Item | Value |
| --- | --- |
| Measured length (mm) | 50.9 |
| Target mean (mm) | 50.0 |
| Standard deviation (mm) | 0.4 |

**Task:** Find how many standard deviations the bolt is from the target.

**Solution:**

```excel
=STANDARDIZE(B2, B3, B4)
```

**Answer:** `2.25`. The bolt is 2.25 standard deviations above target. A planner who inspects anything beyond 2 standard deviations would review this bolt.

<!-- Image 3: Story Problem Results. See Images/Statistical/STANDARDIZE.md -->

## Use Cases

### Exam Score Comparison

**Scenario:** A school compares scores from two tests with different difficulty and different averages to decide which student improved more.

```excel
=STANDARDIZE(B2, AVERAGE(Test1Scores), STDEV.S(Test1Scores))
```

**Why It Works:** Each score becomes a z-score relative to its own test, so the two tests can be compared on a common scale.

### Manufacturing Tolerance Checks

**Scenario:** A quality engineer flags measurements that sit far from the process target.

```excel
=IF(ABS(STANDARDIZE(C2, TargetMean, ProcessSD))>3,"Inspect","Within Range")
```

**Why It Works:** Taking the absolute value catches both high and low outliers. The threshold of 3 is a common planning choice, so adjust it to the process requirements.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `standard_dev` is zero or negative. | Recalculate the standard deviation from the data and confirm it is greater than zero. |
| `#VALUE!` | One of the arguments is text rather than a number. | Convert the text to a number or reference a cell that holds a number. |
| Unexpected sign | The mean and value were swapped in the formula. | Put the value first, then the mean, then the standard deviation. |
| Wrong magnitude | A variance was used in place of a standard deviation. | Take the square root of the variance, or use STDEV.S directly. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web | Named `standard_dev` in the official syntax. Returns `#NUM!` for a zero or negative standard deviation. |
| Google Sheets | Available | Named `standard_deviation` in its documentation. Same calculation. |

## Tips and Best Practices

- Calculate the mean and standard deviation from the same data set so the z-score is meaningful.
- Use STDEV.S for a sample and STDEV.P for a complete population when you supply the standard deviation.
- Pair STANDARDIZE with NORM.S.DIST to turn a z-score into a cumulative probability.
- Store the mean and standard deviation in labeled cells so the formula stays readable.
- Use the absolute value of the z-score when you only care about distance from the mean.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Supplies the mean argument. |
| [STDEV.S](STDEV.S.md) | Supplies the standard deviation argument from a sample. |
| [NORM.S.DIST](NORM.S.DIST.md) | Converts a z-score into a cumulative probability. |
| [NORM.DIST](NORM.DIST.md) | Gives the cumulative probability for a value with a given mean and standard deviation, without standardizing first. |
| [NORM.INV](NORM.INV.md) | Returns the value at a given cumulative probability, the reverse of NORM.DIST. |

## Official Documentation

- [Microsoft Support: STANDARDIZE function](https://support.microsoft.com/en-us/excel/functions/standardize-function)
- [Google Docs Editors Help: STANDARDIZE](https://support.google.com/docs/answer/3094102)
