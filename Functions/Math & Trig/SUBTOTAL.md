---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Aggregation
  - Sorting and Filtering
use-case:
  - Filtered Report Totals
  - Grand Totals Without Double Counting
  - Visible Stock Totals
related:
  - AGGREGATE
  - COUNTA
  - FILTER
  - SUM
  - SUMIFS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/subtotal-function
  - https://support.google.com/docs/answer/3093649
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Filtered Total
  - Subtotal Function
tags:
  - aggregation
  - excel
  - filtering
  - hidden-rows
  - sheets
---

# SUBTOTAL

## Description

**SUBTOTAL** runs one of eleven summary calculations (sum, average, count, maximum, minimum and others) on a list, and it chooses which rows to include. Rows hidden by a filter are always skipped. Rows hidden by hand are skipped only when you use the 101 to 111 codes. The function is the standard way to build totals that change when people filter a list.

Any SUBTOTAL result inside the referenced range is ignored. That rule lets you place a subtotal row inside a list and still build a grand total over the whole list without counting the subtotal twice.

SUBTOTAL works on vertical ranges such as a column. Use SUM when every row should count regardless of filters, and use SUMIFS when the totals depend on specific criteria rather than on what is visible.

## Syntax

```excel
=SUBTOTAL(function_num, ref1, [ref2], ...)
```

<!-- Image 1: Function Number Anatomy. See Images/Math & Trig/SUBTOTAL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `function_num` | Yes | A number from 1 to 11 or from 101 to 111 that selects the calculation. Codes 1 to 11 include manually hidden rows. Codes 101 to 111 exclude them. Rows hidden by a filter are excluded with either set. |
| `ref1` | Yes | The first range or reference to summarize. Use a vertical range such as `A2:A8`. |
| `ref2, ...` | No | Additional ranges or references. Up to 254 references are allowed in total. |

### Function Numbers

| Include Hidden Rows | Exclude Hidden Rows | Function |
| --- | --- | --- |
| 1 | 101 | AVERAGE |
| 2 | 102 | COUNT |
| 3 | 103 | COUNTA |
| 4 | 104 | MAX |
| 5 | 105 | MIN |
| 6 | 106 | PRODUCT |
| 7 | 107 | STDEV |
| 8 | 108 | STDEVP |
| 9 | 109 | SUM |
| 10 | 110 | VAR |
| 11 | 111 | VARP |

### Return Value

A number with the result of the selected calculation over the visible or included rows. The function returns `#VALUE!` when any reference is a three-dimensional reference that spans several sheets.

## Examples

All examples use the hours in `A2:A8`: 12, 7, 15, 9, 20, 4 and 11.

### Example 1: Total of the Visible List

```excel
=SUBTOTAL(9, A2:A8)
```

**Result:** `78`

Code 9 is SUM. With no filter or hidden rows, every value is included.

### Example 2: Average of the List

```excel
=ROUND(SUBTOTAL(1, A2:A8), 2)
```

**Result:** `11.14`

Code 1 is AVERAGE. The seven values total 78, and 78 divided by 7 is 11.142857, which ROUND shows as 11.14.

### Example 3: Hidden Rows Excluded

Row 5 (value 9) is hidden with Hide Rows.

```excel
=SUBTOTAL(109, A2:A8)
```

**Result:** `69`

Code 109 leaves out the hidden row, so 78 minus 9 gives 69. The formula `=SUBTOTAL(9, A2:A8)` still returns 78 because code 9 includes hidden rows.

<!-- Image 2: Hidden Rows and Filters. See Images/Math & Trig/SUBTOTAL.md -->

### Example 4: Subtotal Row Inside the Range

Cell A9 contains `=SUBTOTAL(9, A2:A8)`, which returns 78.

```excel
=SUBTOTAL(9, A2:A9)
```

**Result:** `78`

The SUBTOTAL result in A9 is ignored, so the total does not double count. A plain SUM over A2:A9 would return 156.

## Story Problems

### Problem 1: Warehouse Stock After a Filter

A stock clerk keeps item counts for three warehouses in `A1:C9`. The list has an AutoFilter on the Warehouse column.

| Item | Warehouse | Units |
| --- | --- | --- |
| Bolts | North | 120 |
| Nuts | South | 80 |
| Washers | North | 45 |
| Pins | East | 60 |
| Rivets | North | 210 |
| Clips | South | 35 |
| Screws | North | 95 |
| Hinges | East | 40 |

**Task:** Filter the Warehouse column to North and total the Units that remain visible.

**Solution:**

```excel
=SUBTOTAL(109, C2:C9)
```

**Answer:** `470`, because the four North rows hold 120, 45, 210 and 95. Clearing the filter returns the total for all eight items to 685.

<!-- Image 3: Filtered Stock List. See Images/Math & Trig/SUBTOTAL.md -->

### Problem 2: Weekly Sales With a Subtotal Row

A café records daily sales in column B. Row 5 holds a subtotal for Monday to Wednesday, and Thursday follows it.

| Day | Sales |
| --- | --- |
| Monday | 120 |
| Tuesday | 95 |
| Wednesday | 140 |
| Subtotal | 355 |
| Thursday | 80 |

**Task:** Write a grand total for the week in cell B8 that does not count the subtotal row twice.

**Solution:**

```excel
=SUBTOTAL(9, B2:B6)
```

**Answer:** `435`, from 120 + 95 + 140 + 80. The SUBTOTAL formula in row 5 is ignored by the grand total.

## Use Cases

### Filtered Report Totals

**Scenario:** A manager filters a sales list to one region and needs the total for that region on the same sheet.

```excel
=SUBTOTAL(9, D2:D500)
```

**Why It Works:** The total updates when the filter changes, because filtered rows are always excluded. Put the formula above the list so it stays visible while people scroll.

### Grand Totals Without Double Counting

**Scenario:** A monthly ledger has a subtotal row after each department. The bottom row must show the company total.

```excel
=SUBTOTAL(9, E2:E120)
```

**Why It Works:** SUBTOTAL ignores other SUBTOTAL results inside the range, so each department subtotal is excluded from the grand total. A SUM formula would count each amount twice.

### Visible Stock Totals

**Scenario:** A buyer filters an inventory list by supplier and wants the count of items shown.

```excel
=SUBTOTAL(103, A2:A800)
```

**Why It Works:** Code 103 counts non-empty entries and skips hidden rows, so the count matches what the buyer sees.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A reference spans several sheets in three dimensions, such as `Sheet1:Sheet3!A2:A8`. | Use a standard range on one sheet, or total each sheet and add the results. |
| Total includes hidden rows | The formula uses a code from 1 to 11, which includes rows hidden by hand. | Use the matching code from 101 to 111, such as 109 for SUM. |
| Total is too high | A total row is outside the range and is counted by SUM instead. | Use SUBTOTAL in place of SUM so that nested subtotals are skipped. |
| Total ignores filtered rows | This is the intended behavior, but the reader expects all rows. | Use SUM for the full list, and SUBTOTAL for the visible list. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Excel for the web | Codes 1 to 11 and 101 to 111 follow the table above. Three-dimensional references return `#VALUE!`. |
| Google Sheets | Available | The arguments are named `function_code` and `range1`, with optional `range2` onward. Codes 102 and 110 appear in the help page as examples of skipping hidden rows. |

## Tips and Best Practices

- Use code 109 for totals and 103 for counts when people hide rows by hand, because it gives the same result as the filtered view.
- Put SUBTOTAL formulas in subtotal rows so the grand total can use the same range.
- Keep the range to one column per formula, because the function is designed for vertical ranges.
- Check the filter state before you copy a total into a report, because the value follows what is visible.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AGGREGATE](AGGREGATE.md) | Adds error handling and more calculations, with the same hidden-row choices. |
| [COUNTA](../Statistical/COUNTA.md) | Counts all non-empty cells, including hidden rows. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the rows that match criteria, which you can then total. |
| [SUM](SUM.md) | Adds every value in a range, ignoring filters. |
| [SUMIFS](SUMIFS.md) | Totals rows that match criteria inside the formula instead of by visibility. |

## Official Documentation

- [Microsoft Support: SUBTOTAL function](https://support.microsoft.com/en-us/excel/functions/subtotal-function)
- [Google Docs Editors Help: SUBTOTAL](https://support.google.com/docs/answer/3093649)
