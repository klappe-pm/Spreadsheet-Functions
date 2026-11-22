---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Dynamic Arrays
purpose:
  - Sorting and Filtering
use-case:
  - Customer Priority Lists
  - Inventory Oldest First
  - Sales Leaderboards
related:
  - FILTER
  - RANDARRAY
  - SORTBY
  - SORTN
  - TAKE
  - UNIQUE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/sort-function
  - https://support.google.com/docs/answer/3093150
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Array Sort
  - Sort Range
tags:
  - dynamic-array
  - excel
  - sheets
  - sorting
---

# SORT

## Description

**SORT** returns the rows (or columns) of a range or array in a new order without changing the source data. The result spills into the cells below and to the right of the formula, so the original list stays in its entry order while the sorted view updates whenever the source changes.

In Excel, SORT takes one sort key: a column number (or a row number when `by_col` is TRUE). The sort direction is set with 1 for ascending, which is the default, or -1 for descending. To sort on several keys, or on a key that is not part of the output, use SORTBY instead. Microsoft recommends SORTBY for sorting grid data because it follows the columns when they are inserted or deleted, while SORT uses a column number.

Google Sheets uses a different argument order. Its sort column can be a column index or a separate range of the same height as the data, and the direction is set with TRUE for ascending or FALSE for descending. Google Sheets accepts several sort columns, each followed by its own direction.

Use SORT when the sort key is one of the columns in the output and the order is needed on the sheet. Use FILTER first when only some rows should appear, and wrap the filtered result in SORT.

## Syntax

```excel
=SORT(array, [sort_index], [sort_order], [by_col])
```

<!-- Image 1: SORT Arguments. See Images/Lookup & Reference/SORT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array to sort. It can be a single column, a single row or a multi-column block. The whole block is returned in the new order. |
| `sort_index` | No | The column number to sort by (the row number when `by_col` is TRUE). The default is 1, the first column. |
| `sort_order` | No | `1` for ascending (the default) or `-1` for descending. |
| `by_col` | No | FALSE (the default) sorts rows. TRUE sorts columns by the values in a row, which is rarely needed. |

### Return Value

An array with the same number of columns as the input (or the same number of rows when `by_col` is TRUE). Each row keeps all of its values, so no column is lost. The result spills into the cells below the formula, and the source data is not changed. If the spill range is blocked, the formula returns `#SPILL!`.

## Examples

All examples use this sales list in `A2:C6`.

| Rep | Region | Sales |
| --- | --- | --- |
| Avery | East | 1200 |
| Blake | West | 850 |
| Casey | East | 640 |
| Drew | North | 975 |
| Emery | West | 1530 |

### Example 1: Sort by Sales, Largest First

```excel
=SORT(A2:C6, 3, -1)
```

**Result:** Emery (1530), Avery (1200), Drew (975), Blake (850), Casey (640)

The third column holds the sales figures, and -1 sorts them from largest to smallest. Each row keeps its rep and region.

### Example 2: Sort by Rep Name, Z to A

```excel
=SORT(A2:C6, 1, -1)
```

**Result:** Emery, Drew, Casey, Blake, Avery

Text sorts alphabetically. With -1 the order runs from Z to A.

### Example 3: Sort Columns by a Header Row

```excel
=SORT(A1:C2, 1, 1, TRUE)
```

**Result:** With `A1:C2` holding `30, 10, 20` in row 1 and `Q3, Q1, Q2` in row 2, the result is `10, 20, 30` in row 1 and `Q1, Q2, Q3` in row 2.

Setting `by_col` to TRUE sorts the columns instead of the rows. The first row decides the column order.

### Example 4: Sort a Filtered List

```excel
=SORT(FILTER(A2:C6, B2:B6="East"), 3, -1)
```

**Result:** Avery (1200, East), Casey (640, East)

FILTER keeps the East rows first. SORT then orders the remaining rows by sales, largest first.

<!-- Image 2: Descending Sales Ranking. See Images/Lookup & Reference/SORT.md -->

## Story Problems

### Problem 1: Longest Support Tickets

A support team logs the hours each ticket took in `A2:B7`.

| Ticket | Hours |
| --- | --- |
| T-101 | 3.0 |
| T-102 | 7.5 |
| T-103 | 2.0 |
| T-104 | 9.5 |
| T-105 | 4.25 |
| T-106 | 6.0 |

**Task:** Put the tickets in order from the most hours to the fewest, and name the ticket at the top.

**Solution:**

```excel
=SORT(A2:B7, 2, -1)
```

**Answer:** The top row is `T-104` with 9.5 hours. It is the longest ticket.

### Problem 2: Oldest Stock First

A warehouse lists items with the date each was received in `A2:B6`.

| Item | Received |
| --- | --- |
| Hinges | 2026-02-03 |
| Latches | 2026-01-18 |
| Gaskets | 2026-03-02 |
| Filters | 2026-01-27 |
| Seals | 2026-02-11 |

**Task:** Sort the items so the oldest stock comes first, and name that item.

**Solution:**

```excel
=SORT(A2:B6, 2, 1)
```

**Answer:** `Latches`, received on 2026-01-18. Filters follows on 2026-01-27.

## Use Cases

### Sales Leaderboard

**Scenario:** A sales director wants a leaderboard that lists only reps with sales, ranked from highest to lowest.

```excel
=SORT(FILTER(SalesReps!A2:E50, SalesReps!E2:E50>0), 5, -1)
```

**Why It Works:** FILTER removes reps with no sales, and SORT ranks the rest by the total in column 5. The leaderboard updates when the source changes.

### Oldest Stock First

**Scenario:** A warehouse picks the oldest stock first to rotate inventory.

```excel
=SORT(Inventory!A2:F500, 4, 1)
```

**Why It Works:** Column 4 holds the receipt date. An ascending sort puts the oldest dates at the top. Use -1 when the newest receipts should come first.

### Customer Priority List

**Scenario:** Each account manager needs a list grouped by manager name, with the highest-value accounts first within each group.

```excel
=SORTBY(Customers!A2:G300, Customers!C2:C300, 1, Customers!E2:E300, -1)
```

**Why It Works:** SORT takes only one key, so this case uses SORTBY, which accepts a second key with its own direction. The grouping comes from the first key, and the value order comes from the second.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The `sort_index` is larger than the number of columns in `array`. | Use a column number that exists in the array. |
| `#SPILL!` | The cells below or beside the formula are not empty. | Clear the spill range, or move the formula. |
| Text sorts in an unexpected order | Numbers stored as text sort as text, so 10 comes before 2. | Convert the column to numbers. |
| Multi-column order does not work | SORT takes only one `sort_index` in Excel. | Use SORTBY for two or more keys. |
| Wrong order in Google Sheets | The direction was entered as 1 or -1. | Use TRUE for ascending and FALSE for descending. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2021, Excel 2024, Microsoft 365 and Excel for the web | Not listed for Excel 2019 or earlier. One sort key, direction 1 or -1, optional `by_col`. |
| Google Sheets | Available | Direction is TRUE (ascending) or FALSE (descending). The sort column can be an index or a separate range of the same height. Several sort columns are allowed in order of precedence. |

## Tips and Best Practices

- Use SORTBY instead of SORT when the sort key is outside the output or when you need more than one key.
- Use FILTER before SORT to reduce the rows, which keeps the spilled range small.
- Leave empty rows below a SORT formula so the spill range can grow when the source grows.
- Convert text numbers to real numbers before sorting, or they will sort as text.
- In Google Sheets, write TRUE or FALSE for the direction, because 1 and -1 are not valid there.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SORTBY](SORTBY.md) | Sorts by keys outside the output and supports several keys. |
| [FILTER](FILTER.md) | Selects the rows to sort. |
| [UNIQUE](UNIQUE.md) | Removes duplicates, often followed by SORT for a clean list. |
| [TAKE](TAKE.md) | Returns the first or last rows of a sorted result. |
| [SORTN](../Google-specific/SORTN.md) | A Google Sheets function that sorts and returns the first n rows in one step. |
| [RANDARRAY](../Math%20%26%20Trig/RANDARRAY.md) | Produces random keys for a shuffled order. |

## Official Documentation

- [Microsoft Support: SORT function](https://support.microsoft.com/en-us/excel/functions/sort-function)
- [Google Docs Editors Help: SORT](https://support.google.com/docs/answer/3093150)
