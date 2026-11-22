---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
purpose:
  - Ranking
use-case:
  - Bottom Performer Lists
  - Lowest Bid Selection
  - Response Time Benchmarks
related:
  - LARGE
  - MIN
  - PERCENTILE.INC
  - QUARTILE.INC
  - RANK.EQ
  - SORT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/small-function
  - https://support.google.com/docs/answer/3094050
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Kth Smallest Value
  - Nth Smallest Value
tags:
  - excel
  - ranking
  - sheets
---

# SMALL

## Description

**SMALL** returns the k-th smallest value in a set of numbers. You choose the position: 1 returns the smallest value, 2 returns the second smallest, and so on. The function works on the values themselves, so you do not need to sort the list first.

Use SMALL when you need a value at a known rank, such as the third fastest response time, the second lowest bid or the smallest value that is still above a cutoff in a helper column. Its counterpart LARGE works the same way from the top of the list. To find the position of a particular value rather than the value at a position, use RANK.EQ.

Duplicate values count as separate positions. In the list 1, 3, 3, 5, 7, 9, both the second and the third smallest values are 3. Pass `k` as a cell reference when the position should change without editing the formula.

## Syntax

```excel
=SMALL(array, k)
```

<!-- Image 1: Array and K Arguments. See Images/Statistical/SMALL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array of numeric values to search. |
| `k` | Yes | The position to return, counting from the smallest value. Must be a positive number no larger than the count of data points. |

### Return Value

The single value at position `k` in the data set, returned as a number. The function returns `#NUM!` when the array is empty, when `k` is zero or negative, or when `k` is greater than the number of data points.

## Examples

All examples use the values 7, 3, 9, 1, 5 and 3 in `A2:A7`. Cell `B1` holds the number 4.

### Example 1: Smallest Value

```excel
=SMALL(A2:A7, 1)
```

**Result:** `1`

Position 1 is the smallest value in the list, which is the same result MIN gives.

### Example 2: Tied Values

```excel
=SMALL(A2:A7, 3)
```

**Result:** `3`

The sorted list is 1, 3, 3, 5, 7, 9. Both 3s occupy positions 2 and 3, so position 3 returns 3.

### Example 3: Position From a Cell

```excel
=SMALL(A2:A7, B1)
```

**Result:** `5`

Because `B1` holds 4, the formula returns the fourth smallest value, 5. Change `B1` to update the result without editing the formula.

<!-- Image 2: Sorted Positions for Tied Values. See Images/Statistical/SMALL.md -->

### Example 4: Handling a Position That Does Not Exist

```excel
=IFERROR(SMALL(A2:A7, 10), "Out of Range")
```

**Result:** `Out of Range`

The list has six values, so position 10 does not exist. Wrapping the function in IFERROR keeps the sheet tidy when the position comes from user input.

## Story Problems

### Problem 1: Third Fastest Response Time

A support desk records the response time, in milliseconds, of seven automated replies.

| Reply | Response Time (ms) |
| --- | --- |
| 1 | 312 |
| 2 | 287 |
| 3 | 455 |
| 4 | 301 |
| 5 | 268 |
| 6 | 390 |
| 7 | 276 |

**Task:** Find the third fastest response time to use as the team's benchmark.

**Solution:**

```excel
=SMALL(B2:B8, 3)
```

**Answer:** `287`. The sorted times begin 268, 276 and 287, so 287 is the third smallest.

### Problem 2: Second Lowest Supplier Quote

A buyer receives five quotes for the same part.

| Supplier | Quote |
| --- | --- |
| Alpha | 412 |
| Birch | 388 |
| Cedar | 455 |
| Delta | 390 |
| Elm | 430 |

**Task:** Find the second lowest quote, which the buyer wants to use as a negotiation target.

**Solution:**

```excel
=SMALL(B2:B6, 2)
```

**Answer:** `390`. The lowest quote is 388 from Birch, and the second lowest is 390 from Delta.

<!-- Image 3: Story Problem Results. See Images/Statistical/SMALL.md -->

## Use Cases

### Lowest Bid Selection

**Scenario:** A procurement team wants the second cheapest bid as a reference price when the cheapest bidder is not available.

```excel
=SMALL(BidAmounts, 2)
```

**Why It Works:** SMALL returns the value at a rank without sorting the bid list. Pair it with INDEX and MATCH when you also need the name of the bidder.

### Response Time Benchmarks

**Scenario:** A service team sets a service target from the fifth fastest response in a period, so that the target is reached in most cases but not every case.

```excel
=SMALL(ResponseTimes, 5)
```

**Why It Works:** The rank is a single number that can be stored in a cell, so the team can test different targets by changing the position.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `k` is zero, negative or larger than the number of values. | Check that `k` is between 1 and the count of values. |
| `#NUM!` | The array is empty. | Confirm that the range contains values. |
| Unexpected value | Duplicate values occupy several positions, so a tied value can appear at more than one rank. | Count the duplicates with COUNTIF before choosing `k`. |
| Wrong result | `k` counts from the smallest value, not the largest. | Use LARGE when you need the position counted from the top. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web | Same syntax and behavior. Returns `#NUM!` when `k` is out of range. |
| Google Sheets | Available | Same syntax with the arguments named `data` and `n` in its documentation. Returns the value at the nth smallest position. |

## Tips and Best Practices

- Store `k` in its own labeled cell so people can change the position without touching the formula.
- Use SMALL with IFERROR when `k` comes from user input or a list that may be shorter than expected.
- Use LARGE for the top of the list and SMALL for the bottom; both use the same argument pattern.
- Remember that SMALL returns a value, not a position. Use RANK.EQ when you need the position of a known value.
- Use SORT when you need the whole sorted list rather than a single value.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LARGE](LARGE.md) | Returns the k-th largest value, counting from the top. |
| [MIN](MIN.md) | Returns the smallest value, the same as SMALL with k equal to 1. |
| [RANK.EQ](RANK.EQ.md) | Returns the position of a value in a list. |
| [PERCENTILE.INC](PERCENTILE.INC.md) | Returns a value at a percentage point of the data. |
| [QUARTILE.INC](QUARTILE.INC.md) | Returns a quartile boundary of the data. |
| [SORT](../Lookup%20%26%20Reference/SORT.md) | Returns the whole list in sorted order. |

## Official Documentation

- [Microsoft Support: SMALL function](https://support.microsoft.com/en-us/excel/functions/small-function)
- [Google Docs Editors Help: SMALL](https://support.google.com/docs/answer/3094050)
