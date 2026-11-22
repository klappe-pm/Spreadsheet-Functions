---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Statistical Analysis
use-case:
  - Delivery Time Benchmarks
  - Score Distribution Cutoffs
  - Spread Summaries
related:
  - MAX
  - MEDIAN
  - MIN
  - PERCENTILE.INC
  - QUARTILE.EXC
  - QUARTILE.INC
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/quartile-function
  - https://support.google.com/docs/answer/3094041
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Quartile Value
tags:
  - compatibility
  - descriptive-statistics
  - excel
  - sheets
---

# QUARTILE

## Description

**QUARTILE** returns a value from a dataset at a chosen quartile: the minimum, the first quartile (25th percentile), the median, the third quartile (75th percentile) or the maximum. Use it to split a list of numbers into four groups of roughly equal size, for example to set cutoffs for fast, typical and slow delivery times.

QUARTILE is the older form of QUARTILE.INC. Microsoft Excel keeps it for backward compatibility and says it may be removed in future versions, so use QUARTILE.INC for new work. The two functions return the same results. Use QUARTILE.EXC only when you need the exclusive method, which does not return the minimum or maximum.

The quartile number 0 returns the same value as MIN, 2 matches MEDIAN and 4 matches MAX. Use those functions directly when that is all you need, because they are easier to read.

## Syntax

```excel
=QUARTILE(array, quart)
```

<!-- Image 1: QUARTILE Syntax Anatomy. See Images/Statistical/QUARTILE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The numeric values or cell range to evaluate, such as `A2:A8`. Text and blank cells are ignored. |
| `quart` | Yes | The quartile to return: `0` for the minimum, `1` for the first quartile, `2` for the median, `3` for the third quartile and `4` for the maximum. Non-integer values are truncated. |

### Return Value

A number from the dataset or interpolated between two values, depending on the quartile. The function returns `#NUM!` when the array is empty or when `quart` is less than 0 or greater than 4.

## Examples

Examples use the values 12, 15, 18, 22, 25, 30 and 34 in `A2:A8`.

### Example 1: First Quartile

```excel
=QUARTILE(A2:A8, 1)
```

**Result:** `16.5`

The first quartile falls halfway between 15 and 18, so the result is 16.5.

### Example 2: Median

```excel
=QUARTILE(A2:A8, 2)
```

**Result:** `22`

Quartile 2 is the median, the middle value of the seven numbers.

### Example 3: Third Quartile

```excel
=QUARTILE(A2:A8, 3)
```

**Result:** `27.5`

The third quartile falls halfway between 25 and 30.

### Example 4: Maximum With Error Handling

```excel
=IFERROR(QUARTILE(A2:A8, 5), "Use 0 to 4")
```

**Result:** `Use 0 to 4`

A quartile number above 4 returns `#NUM!`, so IFERROR shows a message instead.

## Story Problems

### Problem 1: Courier Delivery Times

A courier records the days each parcel took to arrive: 3, 4, 4, 5, 6, 8 and 9 days, in `B2:B8`. Operations wants the value that 75 percent of parcels arrive within.

| Parcel | Days |
| --- | --- |
| 1 | 3 |
| 2 | 4 |
| 3 | 4 |
| 4 | 5 |
| 5 | 6 |
| 6 | 8 |
| 7 | 9 |

**Task:** Find the third quartile of the delivery times.

**Solution:**

```excel
=QUARTILE(B2:B8, 3)
```

**Answer:** `7` days. Three quarters of the parcels arrive in 7 days or less.

### Problem 2: Entrance Exam Cutoffs

A school ranks eight entrance exam scores in `C2:C9`: 55, 61, 64, 70, 72, 78, 81 and 90. The admissions team uses the first quartile as a review cutoff.

**Task:** Find the first quartile of the scores.

**Solution:**

```excel
=QUARTILE(C2:C9, 1)
```

**Answer:** `63.25`, because the first quartile falls 75 percent of the way from 61 to 64.

## Use Cases

### Delivery Time Benchmarks

**Scenario:** A logistics team wants to label the slowest quarter of shipments as late so it can review them.

```excel
=QUARTILE(DeliveryDays, 3)
```

**Why It Works:** The third quartile marks the cutoff above which the slowest 25 percent of shipments fall. Store the days in a named range so the cutoff updates as new rows are added.

### Score Distribution Cutoffs

**Scenario:** A teacher groups test scores into four bands based on the class quartiles.

```excel
=QUARTILE(Scores, 1)
```

**Why It Works:** Each quartile is a cutoff between bands. Using the same function for all cutoffs keeps the bands consistent when the scores change.

### Spread Summaries

**Scenario:** An analyst reports the interquartile range of a metric as a measure of spread.

```excel
=QUARTILE(Metric, 3)-QUARTILE(Metric, 1)
```

**Why It Works:** The difference between the third and first quartiles is the interquartile range, which is less affected by extreme values than the full range.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The array is empty or `quart` is outside 0 to 4. | Check that the range has values and use 0, 1, 2, 3 or 4. |
| Error passed through | The range contains an error value such as `#DIV/0!`. | Fix the error in the source cells first. |
| Unexpected value | Text in the range is treated as missing, so the count is smaller than expected. | Convert numbers stored as text to numeric values. |
| Wrong quartile | The quartile number is a percentage, such as 75, not 3. | Use 0 to 4 for quartiles. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Compatibility function, kept for backward compatibility | Replaced by QUARTILE.INC, which Microsoft recommends for new work. |
| Google Sheets | Available | Same arguments. The documentation describes the result as the value nearest to the requested quartile. |

## Tips and Best Practices

- Use QUARTILE.INC in new workbooks and keep QUARTILE only where an existing model depends on it.
- Use MIN, MEDIAN and MAX when you need quartiles 0, 2 and 4, because the names say what they return.
- Check that the range holds numbers, not text, before you read the quartile.
- Use a labeled input cell for the quartile number so the same formula can return any quartile.

## Related Functions

| Function | Relationship |
| --- | --- |
| [QUARTILE.INC](QUARTILE.INC.md) | The current version of this calculation, using the inclusive method. |
| [QUARTILE.EXC](QUARTILE.EXC.md) | The exclusive method, which does not return the minimum or maximum. |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Returns any percentile instead of only the four quartiles. |
| [MEDIAN](MEDIAN.md) | Returns the same value as quartile 2 directly. |
| [MIN](MIN.md) | Returns the same value as quartile 0. |
| [MAX](MAX.md) | Returns the same value as quartile 4. |

## Official Documentation

- [Microsoft Support: QUARTILE function](https://support.microsoft.com/en-us/excel/functions/quartile-function)
- [Google Docs Editors Help: QUARTILE](https://support.google.com/docs/answer/3094041)
