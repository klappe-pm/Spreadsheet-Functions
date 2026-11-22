---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Array Generation
purpose:
  - Array Shaping
use-case:
  - Locker Numbering
  - Tier Point Schedules
related:
  - FILTER
  - MMULT
  - RANDARRAY
  - SORT
  - TRANSPOSE
  - UNIQUE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/sequence-function
  - https://support.google.com/docs/answer/9368244
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Number Sequence
  - Sequential Numbers
tags:
  - dynamic-array
  - excel
  - sheets
  - spill-range
---

# SEQUENCE

## Description

**SEQUENCE** returns an array of sequential numbers. You choose how many rows and columns the array has, where the numbers start, and how much each number changes from the one before. The result is a dynamic array, so it fills a block of cells automatically, and the block grows or shrinks when the arguments change.

Use SEQUENCE to generate numbered labels, counters, schedules, or test grids without filling cells by hand. It is also useful as an argument to other array functions, such as INDEX, SUM, or TEXT, where a list of numbers is needed in a single formula.

When columns is omitted, the result is a single vertical column. For a horizontal list, set rows to 1 and give a column count, or transpose the result with TRANSPOSE. A negative step counts downward, so SEQUENCE(1, 4, 10, -2) returns 10, 8, 6, 4 across the row.

SEQUENCE requires the dynamic array engine. It is available in Microsoft 365, Excel 2024, Excel 2021, and Excel for the web, but not in Excel 2019 or Excel 2016. Google Sheets supports it natively.

## Syntax

```excel
=SEQUENCE(rows, [columns], [start], [step])
```

<!-- Image 1: Sequence Argument Layout. See Images/Math & Trig/SEQUENCE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rows` | Yes | The number of rows in the result. |
| `columns` | No | The number of columns in the result. When omitted, the result is a single column. |
| `start` | No | The first number in the sequence. The default is 1. |
| `step` | No | The amount added to each value to get the next one. Use a negative value to count down. The default is 1. |

### Return Value

Returns an array of numbers with the requested number of rows and columns. The values run across each row before moving to the next row. If the result is the final value of the formula, it spills into the cells below and to the right. Returns #VALUE! when an argument is not numeric and #SPILL! when the output range is blocked by existing content.

## Examples

### Example 1: Four-By-Five Grid of Numbers

```excel
=SEQUENCE(4, 5)
```

**Result:** A spilled block of 4 rows and 5 columns, showing 1 to 5 in the first row, 6 to 10 in the second row, 11 to 15 in the third row, and 16 to 20 in the fourth row.

The function fills the rows in order, so the top-left cell is 1 and the bottom-right cell is 20.

### Example 2: Vertical Counter

```excel
=SEQUENCE(3)
```

**Result:** 1, 2, 3 down a single column

With only rows supplied, the other arguments take their defaults. The start is 1, the step is 1, and the result is one column.

<!-- Image 2: Start and Step Values. See Images/Math & Trig/SEQUENCE.md -->

### Example 3: Custom Start and Step

```excel
=SEQUENCE(3, 2, 5, 10)
```

**Result:** A block of 3 rows and 2 columns: 5 and 15 in the first row, 25 and 35 in the second row, and 45 and 55 in the third row.

The start is 5, and each value is 10 more than the one before it.

### Example 4: Counting Down

```excel
=SEQUENCE(1, 4, 40, -10)
```

**Result:** 40, 30, 20, 10 across one row

A negative step produces a descending sequence. This is useful for countdowns and reverse priority lists.

### Example 5: Month Names From a Sequence

```excel
=TEXT(DATE(2026, SEQUENCE(1, 3), 1), "mmm")
```

**Result:** Jan, Feb, Mar across one row

SEQUENCE supplies the month numbers, DATE builds a date for each one, and TEXT formats each date as a three-letter month name.

## Story Problems

### Problem 1: Locker Numbering for a Gym

A gym has four rows of five lockers. The first locker is numbered 101, and the numbers continue across each row. The manager builds the grid with one formula instead of typing each number.

| Row | Lockers |
| --- | --- |
| 1 | 101 to 105 |
| 2 | 106 to 110 |
| 3 | 111 to 115 |
| 4 | 116 to 120 |

**Task:** Find the locker number in row 3, column 2 of the grid.

**Solution:**

```excel
=INDEX(SEQUENCE(4, 5, 101, 1), 3, 2)
```

**Answer:** `112`. Row 3 starts at 111, so column 2 is the next number, 112.

### Problem 2: Loyalty Points by Tier

A loyalty program has five tiers. The first tier needs 10 points, and each tier needs 5 more points than the one before it.

| Tier | Points Needed |
| --- | --- |
| 1 | 10 |
| 2 | 15 |
| 3 | 20 |
| 4 | 25 |
| 5 | 30 |

**Task:** Find the total points needed to reach all five tiers.

**Solution:**

```excel
=SUM(SEQUENCE(5, 1, 10, 5))
```

**Answer:** `100`, which is 10 + 15 + 20 + 25 + 30.

## Use Cases

### Locker Numbering

**Scenario:** A facilities team labels rows of storage bins in a warehouse and wants the labels to update when the grid size changes.

```excel
=SEQUENCE(B2, B3, 1001, 1)
```

**Why It Works:** B2 holds the number of rows and B3 holds the number of columns. Changing either input resizes the label block, and the start value keeps the numbering continuous across the warehouse.

### Tier Point Schedules

**Scenario:** A rewards team builds a schedule where each tier requires a fixed increase over the previous one.

```excel
=SEQUENCE(B2, 1, B3, B4)
```

**Why It Works:** B2 is the number of tiers, B3 is the first tier's points, and B4 is the increase per tier. The schedule can be checked with SUM to confirm the total points.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#SPILL!` | Cells below or beside the formula contain data. | Clear the cells in the output range, or move the formula. |
| `#VALUE!` | An argument is text, not a number. | Convert the text with VALUE or correct the source cell. |
| `#NAME?` | The version does not include the function. | Use an alternative such as ROW(INDIRECT("1:"&n)) in older versions. |
| `#REF!` | A linked source workbook is closed. | Keep the source workbook open or copy the values. |
| Wrong direction | The step is positive when a countdown was intended. | Use a negative step value. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel for the web, Excel 2024, Excel 2021, and Excel for mobile | Not available in Excel 2019 or Excel 2016. Use ROW with INDIRECT or a fill series as the closest alternative. |
| Google Sheets | Available | Results spill into empty cells. Omitted columns return a single column, and omitted start and step default to 1. |

## Tips and Best Practices

- Put the rows, columns, start, and step values in their own input cells, so the array can be resized without editing the formula.
- Leave the cells below and to the right of the formula empty to avoid a #SPILL! error.
- Wrap SEQUENCE in INDEX when you need one number from the grid rather than the whole block.
- Use TRANSPOSE to turn a vertical sequence into a horizontal one, or set rows to 1 directly.
- Check the start and step values when the numbers are used as identifiers, because a wrong step creates duplicate or skipped labels.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the rows that match a condition, often applied to a SEQUENCE result. |
| [MMULT](MMULT.md) | Multiplies two arrays, which can be built from SEQUENCE blocks. |
| [RANDARRAY](RANDARRAY.md) | Generates random numbers in the same array shape, unlike the fixed numbers from SEQUENCE. |
| [SORT](../Lookup%20%26%20Reference/SORT.md) | Sorts a sequence or other array into a chosen order. |
| [TRANSPOSE](../Lookup%20%26%20Reference/TRANSPOSE.md) | Converts a vertical sequence into a horizontal one. |
| [UNIQUE](../Lookup%20%26%20Reference/UNIQUE.md) | Removes duplicate values from a sequence or other list. |

## Official Documentation

- [Microsoft Support: SEQUENCE function](https://support.microsoft.com/en-us/excel/functions/sequence-function)
- [Google Docs Editors Help: SEQUENCE](https://support.google.com/docs/answer/9368244)
