---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Query and Filtering
purpose:
  - Ranking
  - Sorting and Filtering
use-case:
  - Top Sales Reps
  - Top Scores Shortlist
related:
  - FILTER
  - LARGE
  - RANK.EQ
  - SORT
  - SORTBY
  - TAKE
level: 3
source:
  - https://support.google.com/docs/answer/7354624
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Top N Rows
  - Sort and Limit
tags:
  - filtering
  - ranking
  - sheets
  - sorting
  - top-n
---

# SORTN

## Description

**SORTN** sorts a range and returns only its first rows after the sort. It answers questions such as "who are the top five sellers" or "which three items are lowest in stock" in one formula. The number of rows returned is controlled by the `n` argument, which defaults to 1.

SORTN chooses the sort order with one or more column and direction pairs. Only the columns you name determine the order, and the other columns keep their original order within each row. Use the display ties mode to decide what happens when rows share the same value at the cut-off point: show exactly `n` rows, include every row tied with the last one, or remove duplicate rows first.

SORTN is specific to Google Sheets. Microsoft Excel has no equivalent function. The closest Excel 365 approach combines SORT with TAKE, but that combination has no tie-handling options. For sorting without a row limit, use SORT, or SORTBY to sort by a column that is not part of the output.

## Syntax

```excel
=SORTN(range, [n], [display_ties_mode], [sort_column1, is_ascending1], [sort_column2, is_ascending2], ...)
```

<!-- Image 1: Top N Argument Layout. See Images/Google-specific/SORTN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `range` | Yes | The data to sort, such as `A2:C6`. Header rows are excluded unless you include them on purpose. |
| `n` | No | The number of rows to return. Must be greater than 0. The default is 1. |
| `display_ties_mode` | No | How ties at the cut-off are shown. `0` returns at most the first `n` rows. `1` returns the first `n` rows plus any rows identical to the `n`th row. `2` removes duplicate rows and then returns at most `n` rows. `3` returns at most `n` unique rows but shows every duplicate of those rows. The default is `0`. |
| `sort_column1` | No | The column to sort by, as a position within `range` such as `2` for the second column, or as a single-column range with the same number of rows. |
| `is_ascending1` | No | `TRUE` to sort the first column from smallest to largest, or `FALSE` to sort from largest to smallest. |
| `sort_column2`, `is_ascending2` | No | An optional second sort column and direction. Pairs can repeat in order of precedence when ties occur. |

### Return Value

The first `n` rows of `range` after sorting, with every column of each row kept. The result spills into the cells below the formula. The function returns an error when `n` is 0 or less.

## Examples

All examples use this player table in `A1:C6`, with headers in row 1.

| Player | Points | Wins |
| --- | --- | --- |
| Rivers | 88 | 12 |
| Chen | 92 | 9 |
| Okafor | 75 | 14 |
| Lindqvist | 91 | 11 |
| Moreno | 60 | 10 |

### Example 1: Top Scorer

```excel
=SORTN(A2:C6, 1, 0, 2, FALSE)
```

**Result:** Chen, 92, 9

Sorting by Points in descending order puts Chen first, and `n` of 1 keeps only that row.

### Example 2: Top Three Scorers

```excel
=SORTN(A2:C6, 3, 0, 2, FALSE)
```

**Result:** Chen, 92, 9; Lindqvist, 91, 11; Rivers, 88, 12

The three highest Points totals are returned, with each player's full row.

### Example 3: Fewest Wins

```excel
=SORTN(A2:C6, 2, 0, 3, TRUE)
```

**Result:** Chen, 92, 9; Moreno, 60, 10

Sorting the Wins column from smallest to largest puts Chen (9) and Moreno (10) first.

<!-- Image 2: Sorted Output Examples. See Images/Google-specific/SORTN.md -->

### Example 4: Filter First, Then Sort

```excel
=SORTN(FILTER(A2:C6, B2:B6>=80), 2, 0, 2, FALSE)
```

**Result:** Chen, 92, 9; Lindqvist, 91, 11

FILTER keeps the players with at least 80 points, and SORTN then returns the top two of those rows by Points.

## Story Problems

### Problem 1: Top Three Sales Reps

A sales manager wants the three reps with the highest sales for a recognition slide. The data is in `A1:B6`.

| Rep | Sales |
| --- | --- |
| Ivy | 5400 |
| Jamal | 7200 |
| Kai | 6100 |
| Lena | 5800 |
| Mo | 3900 |

**Task:** Return the top three reps with their sales, highest first.

**Solution:**

```excel
=SORTN(A2:B6, 3, 0, 2, FALSE)
```

**Answer:** Jamal with 7200, Kai with 6100 and Lena with 5800. Ivy at 5400 is fourth, so she is not returned.

### Problem 2: Three Lowest Stock Levels

A workshop wants to reorder the three items with the fewest units on hand. The data is in `A1:B6`.

| Item | Units |
| --- | --- |
| Bolts | 40 |
| Nuts | 12 |
| Washers | 25 |
| Screws | 8 |
| Rivets | 19 |

**Task:** Return the three items with the smallest unit counts, lowest first.

**Solution:**

```excel
=SORTN(A2:B6, 3, 0, 2, TRUE)
```

**Answer:** Screws with 8 units, Nuts with 12 and Rivets with 19. Washers and Bolts have more units and are not returned.

## Use Cases

### Top Sales Reps

**Scenario:** A regional dashboard shows the five best sellers each month, and the list updates when the source data changes.

```excel
=SORTN(Sales!A2:C, 5, 0, 3, FALSE)
```

**Why It Works:** The sort uses the third column of the range, and the limit of five keeps the list short. A new month of data is picked up as soon as the range covers it.

### Top Scores Shortlist

**Scenario:** A selection panel wants the candidates with the highest scores, and it wants every candidate tied with the last place included.

```excel
=SORTN(Scores!A2:C, 10, 1, 2, FALSE)
```

**Why It Works:** A display ties mode of 1 returns the first ten rows and any rows identical to the tenth one, so no candidate who ties for the final place is dropped.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error returned | `n` is 0 or negative. | Use a whole number greater than 0. |
| Tied rows are cut off | Display ties mode is 0, which returns exactly `n` rows. | Set `display_ties_mode` to 1 to include rows tied with the last one. |
| Wrong order | The sort column position does not match the column you intended. | Count the columns in `range` from 1, or use a single-column range of the same height. |
| Header row sorted into the results | The range starts at the header row. | Start `range` at the first data row. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use `=TAKE(SORT(A2:B6, 2, -1), 3)` in Excel 365 for a similar top three. TAKE has no tie-handling options. |
| Google Sheets | Available | Supports display ties modes 0 to 3 and multiple sort column pairs. |

## Tips and Best Practices

- Start `range` at the first data row so that headers are never sorted with the data.
- Filter before sorting when only some rows should compete, as in Example 4.
- Use the ties mode deliberately: 0 gives exactly `n` rows, while 1 keeps every row tied with the last one.
- Sort columns are counted by position within `range`, so check the sort column number again after you insert a column.
- Add a second sort pair to break ties predictably, such as sorting by Points and then by Wins.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SORT](../Lookup%20%26%20Reference/SORT.md) | Sorts a whole range without limiting the number of rows. |
| [SORTBY](../Lookup%20%26%20Reference/SORTBY.md) | Sorts a range by a separate array, which can be outside the output. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Keeps only the rows that meet a condition, usually before SORTN. |
| [TAKE](../Lookup%20%26%20Reference/TAKE.md) | Returns the first rows of a range, the Excel approach to a row limit. |
| [LARGE](../Statistical/LARGE.md) | Returns the nth largest value in a range, without the other columns. |
| [RANK.EQ](../Statistical/RANK.EQ.md) | Returns the rank of one value within a range. |

## Official Documentation

- [Google Docs Editors Help: SORTN](https://support.google.com/docs/answer/7354624)
