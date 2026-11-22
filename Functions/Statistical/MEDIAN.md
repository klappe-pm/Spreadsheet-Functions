---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Aggregation
  - Statistical Analysis
use-case:
  - Middle Delivery Time
  - Typical Home Price
related:
  - AVERAGE
  - MODE.SNGL
  - PERCENTILE.INC
  - QUARTILE.INC
  - TRIMMEAN
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/median-function
  - https://support.google.com/docs/answer/3094025
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Middle Value
  - Median Value
tags:
  - averages
  - central-tendency
  - excel
  - sheets
  - statistics
---

# MEDIAN

## Description

**MEDIAN** returns the middle value of a set of numbers. Sort the values from smallest to largest, and the median is the one in the center. When the count is even, MEDIAN returns the average of the two middle values. It answers the question "What is a typical value?" when a few extreme numbers would pull an average away from the usual case.

The difference from AVERAGE matters most when the data has outliers. One very large order can raise an average sharply, but it moves the median only slightly. Use MEDIAN for income, house prices, delivery times, and similar data with a long tail. Use AVERAGE when every value should count equally toward the total.

MEDIAN ignores text, logical values, and blank cells in ranges and references. Zero is a real number, so MEDIAN includes it. Values typed directly into the list follow other rules: logical values and numbers stored as text are counted. A median cannot be found from no numbers, so check the range with COUNT first when the range can be empty.

## Syntax

```excel
=MEDIAN(number1, [number2], ...)
```

<!-- Image 1: Sorted Values and the Middle. See Images/Statistical/MEDIAN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, cell, range, or named range to evaluate, for example `12`, `B2`, or `B2:B7`. |
| `number2, ...` | No | Up to 254 more numbers, cells, or ranges, for a total of 255 arguments in Excel. |

### Return Value

A single number: the middle value of the numbers supplied, or the average of the two middle values when the count is even. Text and blank cells in references do not count. The function returns an error when an argument is an error value, or when text that cannot be read as a number is typed directly into the list.

## Examples

All examples use the values in `B2:B7` and `C2:C6` below, unless the example says otherwise.

| Test | Score | Notes |
| --- | --- | --- |
| A | 12 | 40 |
| B | 7 | (blank) |
| C | 15 | n/a |
| D | 9 | 60 |
| E | 20 | 0 |
| F | 11 | |

### Example 1: Median of an Even Count

```excel
=MEDIAN(B2:B7)
```

**Result:** `11.5`

Six values sorted are 7, 9, 11, 12, 15, 20. The two middle values are 11 and 12, and their average is 11.5.

### Example 2: Median of an Odd Count

Using only the first five scores, `B2:B6` (12, 7, 15, 9, and 20):

```excel
=MEDIAN(B2:B6)
```

**Result:** `12`

Sorted, the values are 7, 9, 12, 15, and 20. The middle value is 12, so no averaging is needed.

### Example 3: Numbers Typed Directly

```excel
=MEDIAN(1, 3, 100)
```

**Result:** `3`

The middle of 1, 3, and 100 is 3. The large value 100 has no effect on the median, although it would raise the average to about 34.67.

### Example 4: Zero Is Included

```excel
=MEDIAN(C2:C6)
```

**Result:** `40`

The text `n/a` and the blank cell are ignored. The numbers that remain are 40, 60, and 0, which sort to 0, 40, 60. The middle value is 40. Because zero counts, the result would be different if the 0 were removed.

### Example 5: Median Compared With Average

```excel
=AVERAGE(B2:B7)
```

**Result:** `12.33` (rounded from 12.333)

The average of the six scores is 74 divided by 6. Compare this with the median in Example 1 (11.5) to see how far a single high score can move the mean.

## Story Problems

### Problem 1: Typical Order Value

A small online shop records five order amounts in `A1:B6`. One order is unusually large.

| Order | Amount |
| --- | --- |
| 1 | 58 |
| 2 | 72 |
| 3 | 1340 |
| 4 | 64 |
| 5 | 81 |

**Task:** Find the typical order value, so the owner has a figure that the large order does not distort.

**Solution:**

```excel
=MEDIAN(B2:B6)
```

**Answer:** `72`. The average of the five orders is 323, which the single 1340 order pulls upward. The median gives a better sense of a usual order.

### Problem 2: Median Repair Time

A repair team records the hours each of six jobs took in `A1:B7`.

| Job | Hours |
| --- | --- |
| Job 1 | 2.5 |
| Job 2 | 4.0 |
| Job 3 | 3.0 |
| Job 4 | 5.5 |
| Job 5 | 1.5 |
| Job 6 | 7.0 |

**Task:** Find the median repair time, which is the middle of the six jobs.

**Solution:**

```excel
=MEDIAN(B2:B7)
```

**Answer:** `3.5` hours. Sorted, the middle values are 3.0 and 4.0, and their average is 3.5.

<!-- Image 2: Median Compared With Average. See Images/Statistical/MEDIAN.md -->

## Use Cases

### Middle Delivery Time

**Scenario:** A logistics manager wants a typical delivery time that is not skewed by a few delayed shipments.

```excel
=MEDIAN(Deliveries[DaysToArrive])
```

**Why It Works:** A few very late deliveries raise the average but leave the median almost unchanged, so the figure reflects the usual experience.

### Typical Home Price

**Scenario:** A real estate analyst wants the typical sale price in one neighborhood, where a few luxury sales would otherwise skew the result.

```excel
=MEDIAN(IF(Sales[Area]="Riverside", Sales[Price]))
```

**Why It Works:** The IF array returns prices only for the chosen area, and the median ignores the FALSE values it leaves behind. Enter the formula as an array formula in versions of Excel that need it.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error | The range holds no numbers, so there is no middle value. | Check the range with COUNT and wrap the formula in IF(COUNT(range)>0, MEDIAN(range), "No data"). |
| Unexpected result | A number is stored as text, so it is skipped. | Convert the cells to numbers before calculating. |
| Unexpected result | A blank cell is treated as a value you expected to be zero. | Blank cells are ignored. Enter 0 explicitly when zero is a valid value. |
| `#VALUE!` | Text that cannot be read as a number is typed directly into the list. | Reference a cell instead, or remove the text from the list. |
| `#REF!` | A referenced cell or range was deleted. | Restore the range or edit the formula to point to the new cells. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions, including Excel 2016, Excel 2019, Excel 2021, Excel 2024, and Microsoft 365 | Up to 255 arguments. Text, logical values, and blanks in references are ignored. Zeros are included. |
| Google Sheets | Available | Text in the value arguments is ignored. The help page documents 30 arguments. |

## Tips and Best Practices

- Compare the median with the average whenever the data may contain outliers.
- Use MEDIAN with IF inside an array formula to find the median for one group.
- Keep zeros in the range when they are real values, and remove them only when they stand for missing data.
- Check the count with COUNT before reporting a median from a short or empty list.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Returns the arithmetic mean, which every value affects. |
| [MODE.SNGL](MODE.SNGL.md) | Returns the most frequently occurring value instead of the middle value. |
| [QUARTILE.INC](QUARTILE.INC.md) | Returns a quartile, such as the 25th or 75th percentile point. |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Returns any percentile, including the 50th, which equals the median. |
| [TRIMMEAN](TRIMMEAN.md) | Averages the middle part of the data after removing outer values. |

## Official Documentation

- [Microsoft Support: MEDIAN function](https://support.microsoft.com/en-us/excel/functions/median-function)
- [Google Docs Editors Help: MEDIAN](https://support.google.com/docs/answer/3094025)
