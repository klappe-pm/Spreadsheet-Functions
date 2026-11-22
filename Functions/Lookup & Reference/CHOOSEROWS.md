---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
use-case:
  - Latest Entries From a Log
  - Pulling Chosen Records
  - Repeating Rows for Printing
related:
  - CHOOSECOLS
  - DROP
  - FILTER
  - INDEX
  - TAKE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/chooserows-function
  - https://support.google.com/docs/answer/13196659
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Pick Rows
  - Row Selector
tags:
  - array-shaping
  - dynamic-array
  - excel
  - sheets
---

# CHOOSEROWS

## Description

**CHOOSEROWS** returns a new array made of the rows you name, in the order you name them. Pass it a range and the row numbers 1, 3 and 5, and it returns those three rows. A row number can repeat, so one record can appear several times in the result, which is useful for printing labels or copying a template row.

Negative numbers count from the bottom of the array. The number -1 is the last row, -2 is the row above it, and so on. This makes CHOOSEROWS a simple way to return the newest entries from a list that is added to at the bottom.

Use CHOOSEROWS when you know the row positions. For rows that meet a condition, use FILTER. For the first few rows of an array, use TAKE.

## Syntax

```excel
=CHOOSEROWS(array, row_num1, [row_num2], ...)
```

<!-- Image 1: Row Selection Anatomy. See Images/Lookup & Reference/CHOOSEROWS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array that holds the rows to return. |
| `row_num1` | Yes | The first row to return. 1 is the first row, and a negative number counts from the last row. Zero is not allowed. |
| `row_num2`, ... | No | More row numbers, returned in the order given. A row can be listed more than once. |

### Return Value

A new array that holds the requested rows in the order listed. In Excel, a row number of 0, or one whose absolute value is larger than the number of rows, returns `#VALUE!`. The array spills into the cells below and to the right of the formula in Excel 365.

## Examples

All examples use this table in `A1:B7`, with headers in row 1 and the data in rows 2 to 7.

| Day | Score |
| --- | --- |
| Mon | 72 |
| Tue | 85 |
| Wed | 64 |
| Thu | 91 |
| Fri | 78 |
| Sat | 88 |

### Example 1: Two Rows by Position

```excel
=CHOOSEROWS(A2:B7, 2, 4)
```

**Result:** the Tue row and the Thu row

Row 2 of the range is Tue and row 4 is Thu. The rows return in the order listed.

### Example 2: A Row That Repeats

```excel
=CHOOSEROWS(A2:B7, 1, 3, 1)
```

**Result:** the Mon row, the Wed row and the Mon row again

Row 1 appears twice, so its record is repeated in the result.

### Example 3: The Last Row

```excel
=CHOOSEROWS(A2:B7, -1)
```

**Result:** the Sat row

The number -1 counts from the bottom, so it returns the last row of the range.

<!-- Image 2: Positive and Negative Row Numbers. See Images/Lookup & Reference/CHOOSEROWS.md -->

### Example 4: The Last Two Rows in Order

```excel
=CHOOSEROWS(A2:B7, -2, -1)
```

**Result:** the Fri row, then the Sat row

Both negative numbers count from the bottom, and they return in the order listed, so -2 comes first.

### Example 5: Summing Two Rows

```excel
=SUM(CHOOSEROWS(B2:B7, 2, 4))
```

**Result:** `176`

The scores for Tue and Thu are 85 and 91, and those two values add to 176.

## Story Problems

### Problem 1: Latest Three Orders

An online shop lists orders in date order in `A1:B7`. The newest order is at the bottom.

| Order | Amount |
| --- | --- |
| O-201 | 120 |
| O-202 | 75 |
| O-203 | 210 |
| O-204 | 90 |
| O-205 | 150 |
| O-206 | 60 |

**Task:** Total the amounts of the three most recent orders without typing their row numbers.

**Solution:**

```excel
=SUM(CHOOSEROWS(B2:B7, -1, -2, -3))
```

**Answer:** `300`. The three newest rows are O-206 (60), O-205 (150) and O-204 (90), and those add to 300.

### Problem 2: Copies From a Print List

A print list has one row for each item and a copies column. The copies for the mug and the pen are in `B2:B3`.

| Item | Copies |
| --- | --- |
| Mug | 1 |
| Pen | 2 |

**Task:** Total the copies for a print run that prints the pen row twice and the mug row once.

**Solution:**

```excel
=SUM(CHOOSEROWS(B2:B3, 2, 2, 1))
```

**Answer:** `5`. The pen row contributes 2 twice and the mug row contributes 1, so the total is 5.

## Use Cases

### Latest Entries From a Log

**Scenario:** A maintenance log gains a new row each day, and the dashboard must show the three newest entries.

```excel
=CHOOSEROWS(Log!B2:B500, -1, -2, -3)
```

**Why It Works:** Negative numbers always count from the bottom of the range. The range must end at the last used row, because blank rows at the bottom of the range are returned as blanks.

### Pulling Chosen Records

**Scenario:** A sales manager picks five customers from a long list by their row positions to send a follow-up list.

```excel
=CHOOSEROWS(Customers!A2:C200, 5, 9, 12, 20, 33)
```

**Why It Works:** The formula returns exactly the five records in the order the manager wants. The row numbers are positions, so a re-sorted customer list will return different customers.

### Repeating Rows for Printing

**Scenario:** A label printer needs each product row printed twice for a double shelf label run.

```excel
=CHOOSEROWS(Labels!A2:B4, 1, 1, 2, 2, 3, 3)
```

**Why It Works:** Each row number appears twice in the list, so each label row returns twice, one after the other.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A row number is 0, or its absolute value is larger than the number of rows. | Check the row count and the sign of each number. |
| Blank rows in the result | The range runs past the last row of data. | Size the range to the data, or use a table reference that grows with the list. |
| Different records after sorting | Row numbers are positions, so a re-sorted source returns other records. | Recheck the rows after sorting, or use FILTER to select records by a key. |
| `#SPILL!` | The cells below or to the right of the formula already hold data. | Clear the blocked cells, or move the formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024 (Windows and Mac) | Returns an array that spills in Excel 365. Negative numbers count from the bottom row. |
| Google Sheets | Available, in the Array category | Same arguments. The page does not describe the error behavior. |

## Tips and Best Practices

- Use negative numbers for the newest rows when new data is added at the bottom of the list.
- Use FILTER instead when the rows should be chosen by a value rather than by position.
- Keep the range sized to the data, so blank rows do not appear in the result.
- Recheck the row numbers after any sort, because the positions point at different records after a sort.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSECOLS](CHOOSECOLS.md) | Picks columns by number, the column counterpart of this function. |
| [DROP](DROP.md) | Removes rows from the start or end, which suits removing a header or total rows. |
| [FILTER](FILTER.md) | Keeps rows that match a condition rather than rows at fixed positions. |
| [INDEX](INDEX.md) | Returns one cell or row by position when only a single value is needed. |
| [TAKE](TAKE.md) | Keeps the first or last rows of an array from the start or end. |

## Official Documentation

- [Microsoft Support: CHOOSEROWS function](https://support.microsoft.com/en-us/excel/functions/chooserows-function)
- [Google Docs Editors Help: CHOOSEROWS](https://support.google.com/docs/answer/13196659)
