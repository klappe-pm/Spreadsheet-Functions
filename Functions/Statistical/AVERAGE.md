---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Aggregation
use-case:
  - Classroom Grades
  - Sales Benchmarks
  - Ticket Response Times
related:
  - AVERAGEA
  - AVERAGEIF
  - AVERAGEIFS
  - GEOMEAN
  - MEDIAN
  - SUBTOTAL
  - SUMPRODUCT
  - TRIMMEAN
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/average-function
  - https://support.google.com/docs/answer/3093615
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Arithmetic Mean
  - Mean
tags:
  - averages
  - central-tendency
  - excel
  - mean
  - sheets
---

# AVERAGE

## Description

**AVERAGE** returns the arithmetic mean of its numeric arguments: it adds the numbers and divides by how many numbers it found. It is the most common measure of a typical value, and it is the first function most people reach for when they want to summarize a column.

The function treats cells in ranges differently from values typed into the formula. Inside a cell reference or range, AVERAGE skips text, logical values (TRUE and FALSE) and empty cells. Cells that contain the number zero are not skipped, so a zero pulls the average down. That difference matters most when zero means "no data" rather than "a real result of zero". In that case, use AVERAGEIF with a criterion such as `">0"` to leave the zeros out.

AVERAGE does not weight values. Every number counts once, so a value that stands for ten items counts the same as a value that stands for one. When items carry different weights, divide a SUMPRODUCT by the sum of the weights instead. AVERAGE is the same function in Excel and Google Sheets for standard numeric data.

## Syntax

```excel
=AVERAGE(number1, [number2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/AVERAGE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, cell, or range to average. Can be a single value, a range such as `A1:A100`, or a named range. |
| `number2, ...` | No | Additional numbers, cells, or ranges. Excel accepts up to 255 arguments in total. |

### Return Value

A number: the sum of the numeric values divided by the count of those values. The result is `#DIV/0!` when no numeric values are found, and `#VALUE!` when a value typed directly into the argument list cannot be read as a number.

## Examples

### Example 1: Typed Numbers

```excel
=AVERAGE(10, 20, 30)
```

**Result:** `20`

The sum is 60, and dividing by three values gives 20.

### Example 2: Average of a Range

Values in `A2:A6`: 85, 90, 78, 92, 88.

```excel
=AVERAGE(A2:A6)
```

**Result:** `86.6`

The five scores total 433, and 433 divided by 5 is 86.6.

<!-- Image 2: Empty Cells Versus Zeros. See Images/Statistical/AVERAGE.md -->

### Example 3: Empty Cells Are Skipped

Values in `A2:A6`: 100, 200, blank, blank, 300.

```excel
=AVERAGE(A2:A6)
```

**Result:** `200`

Only three cells hold numbers. Their total is 600, and 600 divided by 3 is 200. The blank cells do not affect the count.

### Example 4: Zeros Are Counted

Values in `A2:A6`: 100, 200, 0, 0, 300.

```excel
=AVERAGE(A2:A6)
```

**Result:** `120`

The two zeros are included, so the total of 600 is divided by 5. Compare this with Example 3: the same numbers with blanks in place of zeros give 200.

### Example 5: Text Inside a Range Is Skipped

Values in `A2:A6`: 50, `N/A`, 60, `Pending`, 70.

```excel
=AVERAGE(A2:A6)
```

**Result:** `60`

The two text entries are ignored, and the three numbers total 180. The average is 60, but the result would be misleading if the text entries stood for missing values that should count.

### Example 6: Weighted Average Workaround

Scores in `A2:A4`: 80, 90, 70. Weights in `B2:B4`: 2, 3, 1.

```excel
=SUMPRODUCT(A2:A4, B2:B4) / SUM(B2:B4)
```

**Result:** `83.33`

Each score is multiplied by its weight: 160 + 270 + 70 is 500. Dividing by the total weight of 6 gives 83.33. AVERAGE alone would return 80, because it treats every score equally.

### Example 7: Returning a Default When No Numbers Exist

```excel
=IFERROR(AVERAGE(D2:D6), "No data")
```

**Result:** `No data` when `D2:D6` contains only text or is empty

Without IFERROR, the same range returns `#DIV/0!`. Wrapping the function keeps dashboards readable while the source data is still being entered.

## Story Problems

### Problem 1: Quiz Average With a Missed Quiz

A teacher records five quiz scores in `A1:B6`. A student missed Quiz 3, so that cell is left blank.

| Quiz | Score |
| --- | --- |
| Quiz 1 | 8 |
| Quiz 2 | 9 |
| Quiz 3 | |
| Quiz 4 | 7 |
| Quiz 5 | 10 |

**Task:** Find the student's average across the quizzes that were taken.

**Solution:**

```excel
=AVERAGE(B2:B6)
```

**Answer:** `8.5`. The four scores total 34, and 34 divided by 4 is 8.5. The blank cell is not counted, so the missed quiz does not drag the average down.

<!-- Image 3: Results Panel for the Quiz Problem. See Images/Statistical/AVERAGE.md -->

### Problem 2: Delivery Times With Missing Records

A courier logs delivery days in `A1:B6`. A zero means the delivery was never recorded, not that it arrived the same day.

| Order | Days |
| --- | --- |
| Order 1 | 2 |
| Order 2 | 3 |
| Order 3 | 0 |
| Order 4 | 4 |
| Order 5 | 5 |

**Task:** Find the average delivery time for recorded deliveries only.

**Solution:**

```excel
=AVERAGEIF(B2:B6, ">0")
```

**Answer:** `3.5` days. The four recorded values total 14, and 14 divided by 4 is 3.5. Plain AVERAGE would return 2.8 because it counts the zero.

## Use Cases

### Classroom Grades

**Scenario:** A teacher calculates each student's average across a set of assignments, and some students have blank entries for excused work.

```excel
=AVERAGE(B2:F2)
```

**Why It Works:** Blank cells for excused work are skipped automatically. Zeros entered for missed work are counted, so the teacher should enter a blank rather than a zero when an assignment was excused.

### Sales Benchmarks

**Scenario:** A sales manager compares each representative against the team average to find people who may need coaching.

```excel
=IF(B2 > AVERAGE($B$2:$B$50), "Above average", "Below average")
```

**Why It Works:** The absolute reference `$B$2:$B$50` keeps the average range fixed when the formula is copied down. Use MEDIAN instead when a few very large sales skew the average.

### Ticket Response Times

**Scenario:** A support team reports the average hours to first response and checks it against a service level target.

```excel
=IF(AVERAGE(ResponseHours) <= 4, "Meeting target", "Target missed")
```

**Why It Works:** `ResponseHours` is a named range, so the formula keeps working as tickets are added. Confirm that every value uses the same unit before comparing it to the target.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | The range holds no numeric values. | Check the source data, or wrap the formula in IFERROR to show a default. |
| `#VALUE!` | A value typed directly into the formula is text that cannot be read as a number. | Put the value in a cell and reference it, or correct the entry. |
| Unexpected result | Zeros that mean "no data" are included in the average. | Use AVERAGEIF with `">0"`, or enter blanks instead of zeros. |
| Unexpected result | Numbers stored as text inside a range are skipped. | Convert them to numbers with VALUE or by multiplying by 1. |
| Unexpected result | Hidden rows are included in the average. | Use SUBTOTAL with function number 101 to average only visible rows. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Up to 255 arguments. Pre-dynamic-array versions may need Ctrl+Shift+Enter for some array expressions. |
| Google Sheets | Available | Google's help page lists a limit of 30 values, and the function accepts more. Array expressions work without special entry. |

## Tips and Best Practices

- Decide what a zero means before averaging. If zero means "no data", use blanks or AVERAGEIF.
- Compare AVERAGE with MEDIAN when the data contains extreme values.
- Use AVERAGEIF or AVERAGEIFS when only some rows should count.
- Wrap the formula in IFERROR when the range can be empty, so dashboards do not show errors.
- Use absolute references such as `$B$2:$B$50` when the formula will be copied.
- Show the sample size next to the average, for example with COUNT, so readers know how much data sits behind the number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGEA](AVERAGEA.md) | Counts text as 0 and TRUE as 1, so it is useful when those values should affect the result. |
| [AVERAGEIF](AVERAGEIF.md) | Averages only the values that meet one condition. |
| [AVERAGEIFS](AVERAGEIFS.md) | Averages only the values that meet several conditions at once. |
| [GEOMEAN](GEOMEAN.md) | Geometric mean, suited to growth rates and multiplicative data. |
| [MEDIAN](MEDIAN.md) | Middle value, less affected by outliers. |
| [SUBTOTAL](../Math%20%26%20Trig/SUBTOTAL.md) | Average of visible rows only when function number 101 is used. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Builds a weighted average when divided by the sum of the weights. |
| [TRIMMEAN](TRIMMEAN.md) | Average after removing a set share of the highest and lowest values. |

## Official Documentation

- [Microsoft Support: AVERAGE function](https://support.microsoft.com/en-us/excel/functions/average-function)
- [Google Docs Editors Help: AVERAGE](https://support.google.com/docs/answer/3093615)
