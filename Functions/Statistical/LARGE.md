---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
purpose:
  - Ranking
use-case:
  - Leaderboard Cutoffs
  - Top Expense Review
  - Top Sales Performers
related:
  - MAX
  - MEDIAN
  - PERCENTILE.INC
  - RANK.EQ
  - SMALL
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/large-function
  - https://support.google.com/docs/answer/3094008
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Kth Largest Value
  - Nth Largest
tags:
  - excel
  - ranking
  - sheets
  - statistical
  - top-n
---

# LARGE

## Description

**LARGE** returns the k-th largest value in a range or array. You choose the position: 1 returns the biggest value, 2 returns the second biggest, and so on. The function counts from the top of the list, so it answers questions such as "what is the third highest sales figure" without sorting the data first.

Use LARGE when you need a specific rank rather than a summary. It is useful for a leaderboard cutoff, a top-five list, or a threshold such as the value that the top ten items must beat. For the single biggest value, MAX is simpler. For the smallest values, use SMALL, which works the same way from the bottom.

Duplicates count as separate positions. In a list of 45, 45, 33, the second largest value is 45, not 33. When you need the position of a value within the list rather than the value itself, use RANK.EQ. When you need a percentage cutoff rather than a fixed rank, use PERCENTILE.INC.

## Syntax

```excel
=LARGE(array, k)
```

<!-- Image 1: Ranking From the Top of a List. See Images/Statistical/LARGE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range, array or list of numbers to search. |
| `k` | Yes | The position from the top, a whole number from 1 to the count of values in `array`. Enter a number or a cell reference. |

### Return Value

The value at position `k` counting from the largest. It returns `#NUM!` when `array` is empty, when `k` is 0 or less, or when `k` is larger than the number of data points.

## Examples

The examples use this list in `A2:A8`: 12, 45, 7, 33, 21, 45, 18. The number 45 appears twice.

### Example 1: The Largest Value

```excel
=LARGE(A2:A8, 1)
```

**Result:** `45`

With k equal to 1, the function returns the top value, which is the same answer as MAX.

### Example 2: The Third Largest Value

```excel
=LARGE(A2:A8, 3)
```

**Result:** `33`

The sorted order from the top is 45, 45, 33, 21, 18, 12, 7, so position 3 is 33.

### Example 3: Duplicates Take Separate Positions

```excel
=LARGE(A2:A8, 2)
```

**Result:** `45`

The second position is the second copy of 45. Duplicates are not skipped, so a tied value can occupy more than one rank.

### Example 4: Taking the Rank From a Cell

Cell `C2` holds the number 4.

```excel
=LARGE(A2:A8, C2)
```

**Result:** `21`

Changing the value in `C2` changes the rank without editing the formula, which suits a report where the user picks the position.

## Story Problems

### Problem 1: Third Best Sales Month

A regional team records sales for eight representatives in `B2:B9`.

| Representative | Sales |
| --- | --- |
| Ana | 5200 |
| Ben | 4100 |
| Cy | 6800 |
| Dee | 3900 |
| Eli | 6100 |
| Fay | 4700 |
| Gus | 5900 |
| Hal | 4300 |

**Task:** Find the sales figure of the third best representative so that the bonus threshold can be set at that level.

**Solution:**

```excel
=LARGE(B2:B9, 3)
```

**Answer:** `5900`, from Gus. The top three are 6800, 6100 and 5900.

### Problem 2: Honors Score Cutoff

A teacher wants the score of the fourth highest student in `C2:C11` to set an honors cutoff.

| Student | Score |
| --- | --- |
| 1 | 78 |
| 2 | 92 |
| 3 | 85 |
| 4 | 92 |
| 5 | 67 |
| 6 | 74 |
| 7 | 88 |
| 8 | 95 |
| 9 | 81 |
| 10 | 70 |

**Task:** Find the fourth highest score. Two students scored 92, so decide how the tie affects the ranking.

**Solution:**

```excel
=LARGE(C2:C11, 4)
```

**Answer:** `88`. The sorted order is 95, 92, 92, 88, so the tied 92s occupy positions 2 and 3.

<!-- Image 2: Tied Scores in a Ranked List. See Images/Statistical/LARGE.md -->

## Use Cases

### Leaderboard Cutoffs

**Scenario:** A game publishes the score needed to reach the top ten players.

```excel
=LARGE(Scores[Points], 10)
```

**Why It Works:** Structured references grow with the table. The tenth largest score is the cutoff, and any player at or above it appears on the board.

### Top Expense Review

**Scenario:** A finance manager reviews the three largest expense claims each quarter.

```excel
=LARGE(Expenses[Amount], 3)
```

**Why It Works:** The third largest amount sets a review threshold. Claims at or above that amount are the ones to inspect, without sorting the full table.

### Top Sales Performers

**Scenario:** A sales director wants the sales total of the top five representatives.

```excel
=SUMPRODUCT(LARGE(Sales!B2:B50, {1,2,3,4,5}))
```

**Why It Works:** An array constant gives LARGE five positions at once. SUMPRODUCT adds the results, so one formula returns the combined total of the top five.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `k` is 0, negative or larger than the number of values. | Check that `k` is between 1 and the count of values. |
| `#NUM!` | `array` is empty, for example a filter that returned no rows. | Test with COUNT before calling LARGE. |
| Unexpected value | Duplicates are counted as separate positions. | Use UNIQUE first when each value should appear once. |
| Wrong ranking | `k` counts from the top, but the intent was the bottom. | Use SMALL for the lowest values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Works with a range, an array or a dynamic array result. Arguments are `array` and `k`. |
| Google Sheets | Available | Same behavior with the arguments named `data` and `n`. The order of arguments is the same. |

## Tips and Best Practices

- Use MAX for the first position. LARGE with k equal to 1 gives the same answer, but MAX reads more clearly.
- Store k in a cell when the rank may change, and label the cell so the report explains the cutoff.
- Check COUNT before choosing k, because k cannot exceed the number of numeric values.
- Use LARGE with IF or FILTER when only certain rows should be ranked, for example one region's sales.
- Remember that ties create repeated values, so a rank cutoff may include more people than the number you requested.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SMALL](SMALL.md) | Returns the k-th smallest value, the mirror of LARGE. |
| [MAX](MAX.md) | Returns the largest value directly, the same as LARGE with k equal to 1. |
| [RANK.EQ](RANK.EQ.md) | Returns the position of a given value instead of the value at a position. |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Returns a value at a percentage point rather than a fixed rank. |
| [MEDIAN](MEDIAN.md) | Returns the middle value, which sits between the top and bottom ranks. |

## Official Documentation

- [Microsoft Support: LARGE function](https://support.microsoft.com/en-us/excel/functions/large-function)
- [Google Docs Editors Help: LARGE](https://support.google.com/docs/answer/3094008)
