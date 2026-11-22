---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
purpose:
  - Statistical Analysis
use-case:
  - Process Control Checks
  - Weekly Traffic Swings
related:
  - AVERAGE
  - DEVSQ
  - MEDIAN
  - STDEV.P
  - STDEV.S
  - VAR.S
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/avedev-function
  - https://support.google.com/docs/answer/3093613
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Average Absolute Deviation
  - Mean Absolute Deviation
tags:
  - excel
  - sheets
  - spread
  - statistics
  - variability
---

# AVEDEV

## Description

**AVEDEV** measures how spread out a set of numbers is around their average. It finds the mean of the data, measures how far each value sits from that mean (ignoring whether the value is above or below it), and returns the average of those distances. A small result means the values cluster tightly around the mean; a large result means they vary widely.

Use AVEDEV when you want a spread measure that is easy to explain to a non-statistician. Each value contributes its distance in the same units as the data, so a result of 2.5 means a typical value sits about 2.5 units from the mean. Standard deviation (STDEV.S or STDEV.P) also measures spread, but it squares the distances before averaging. That squaring gives extra weight to large deviations, so a single outlier moves standard deviation more than it moves AVEDEV.

AVEDEV is not a legacy function, but it is less common than standard deviation in formal statistics. Choose it for routine monitoring, quick checks in a worksheet, or reports that must be read by people who do not work with squared values. Both Excel and Google Sheets calculate it the same way for numeric data. Excel's arguments are named `number1, [number2], ...`, while Sheets names them `value1, [value2, ...]`.

## Syntax

```excel
=AVEDEV(number1, [number2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/AVEDEV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, a cell reference, a range, or an array to analyze. |
| `number2, ...` | No | Additional numbers, references, or ranges. Excel accepts up to 255 arguments in total. A single array or a reference to an array also works. |

### Return Value

A number: the average of the absolute deviations of the data points from their mean. The result is in the same units as the data. Text and logical values inside a range or reference are ignored, and cells that contain zero are included. A numeric value typed directly into the argument list is counted.

## Examples

### Example 1: Typed Numbers

```excel
=AVEDEV(4, 6, 8, 10, 12)
```

**Result:** `2.4`

The mean is 8. The distances from 8 are 4, 2, 0, 2 and 4, which total 12. Dividing 12 by five values gives 2.4.

### Example 2: A Column of Measurements

Values in `A2:A9`: 98, 101, 99, 103, 97, 100, 102, 96.

```excel
=AVEDEV(A2:A9)
```

**Result:** `2`

The mean is 99.5. The eight distances total 16, and 16 divided by 8 is 2.

<!-- Image 2: Distance From the Mean. See Images/Statistical/AVEDEV.md -->

### Example 3: Text Inside a Range

Values in `A2:A6`: 10, `n/a`, 14, 12, 18.

```excel
=AVEDEV(A2:A6)
```

**Result:** `2.5`

The text entry is skipped, so the function works with four numbers. Their mean is 13.5, and the distances total 10.

### Example 4: Zeros Are Counted

Values in `B2:B5`: 0, 0, 6, 6.

```excel
=AVEDEV(B2:B5)
```

**Result:** `3`

Both zeros are real data points, so they stay in the calculation. The mean is 3, and every value sits exactly 3 from it.

## Story Problems

### Problem 1: Bottle Fill Consistency

A bottling line targets 500 ml per bottle. The quality team records six fills in `A1:B7`.

| Bottle | Fill (ml) |
| --- | --- |
| 1 | 498 |
| 2 | 502 |
| 3 | 500 |
| 4 | 497 |
| 5 | 503 |
| 6 | 500 |

**Task:** Measure the typical distance of a fill from the average fill, rounded to two decimals.

**Solution:**

```excel
=ROUND(AVEDEV(B2:B7), 2)
```

**Answer:** `1.67` ml. The average fill is exactly 500 ml, and the distances total 10 across six bottles (10 divided by 6 is 1.6667).

<!-- Image 3: Fill Results Panel. See Images/Statistical/AVEDEV.md -->

### Problem 2: Website Traffic Swings

A small publisher counts weekly visits in `A1:B6`.

| Week | Visits |
| --- | --- |
| Week 1 | 1200 |
| Week 2 | 1350 |
| Week 3 | 1100 |
| Week 4 | 1500 |
| Week 5 | 1250 |

**Task:** Find how far a typical week sits from the average week in visits.

**Solution:**

```excel
=AVEDEV(B2:B6)
```

**Answer:** `116` visits. The average is 1280 visits, and the five distances total 580 (580 divided by 5 is 116).

## Use Cases

### Process Control Checks

**Scenario:** A quality engineer reviews a daily sample of part lengths and wants a simple spread figure to compare from one week to the next.

```excel
=AVEDEV(Lengths[Measurement])
```

**Why It Works:** The table reference grows as new samples are added, so the spread figure updates without editing the formula. Compare the value against a limit the team agreed on in advance.

### Monthly Expense Variation

**Scenario:** A household budget tracks monthly grocery spending and wants to know how much the amount usually moves around its average.

```excel
=AVEDEV(Groceries!B2:B13)
```

**Why It Works:** A larger result flags months with unusually uneven spending. Because the result uses the same units as the data, the owner can read it directly as dollars per month.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A typed argument is text that cannot be read as a number. | Put the text value in a cell and reference it, or correct the entry. |
| Unexpected result | Numbers stored as text inside a range are ignored, so the average covers fewer values. | Convert the text to numbers with `VALUE` or by multiplying by 1, then recalculate. |
| Unexpected result | Blank cells in the range are left out, so the count is smaller than expected. | Confirm the range covers every row that should be included. |
| Unexpected result | A header row was included in the range. | Start the range below the header. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, Excel 2019, Excel 2021, Excel 2024 and Microsoft 365, including Mac and web | Arguments are named `number1, [number2], ...`; up to 255 arguments. |
| Google Sheets | Available | Arguments are named `value1, [value2, ...]`. Text in ranges is ignored. |

## Tips and Best Practices

- Use AVEDEV alongside AVERAGE so readers see both the typical value and the typical distance from it.
- Pair it with MEDIAN when outliers are present, because the mean that AVEDEV depends on can be pulled by extreme values.
- Keep a single unit across the range, since mixing grams and kilograms produces a meaningless spread.
- Start ranges below header rows so labels are not counted as data.
- Use STDEV.S instead when the result feeds a formal statistical test or a confidence interval.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Supplies the mean from which AVEDEV measures distances. |
| [DEVSQ](DEVSQ.md) | Sums squared deviations from the mean, the basis of variance. |
| [MEDIAN](MEDIAN.md) | Middle value that is less affected by outliers. |
| [STDEV.P](STDEV.P.md) | Standard deviation for a full population. |
| [STDEV.S](STDEV.S.md) | Standard deviation for a sample. |
| [VAR.S](VAR.S.md) | Sample variance, the square of the sample standard deviation. |

## Official Documentation

- [Microsoft Support: AVEDEV function](https://support.microsoft.com/en-us/excel/functions/avedev-function)
- [Google Docs Editors Help: AVEDEV](https://support.google.com/docs/answer/3093613)
