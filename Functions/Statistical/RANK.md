---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Ranking
use-case:
  - Exam Score Positions
  - Race Results
  - Sales Leaderboards
related:
  - COUNTIF
  - LARGE
  - PERCENTRANK.INC
  - RANK.AVG
  - RANK.EQ
  - SMALL
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/rank-function
  - https://support.google.com/docs/answer/3094098
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Rank Position
tags:
  - compatibility
  - excel
  - ranking
  - sheets
---

# RANK

## Description

**RANK** returns the position of a number within a list of numbers. By default the largest number has rank 1, so the function answers "where does this value place in the list?" Use it for leaderboards, test positions and any list where you need to show who is first, second and so on.

RANK is the older form of RANK.EQ. Microsoft Excel keeps it for backward compatibility and says it may not be available in future versions, so use RANK.EQ or RANK.AVG for new work. RANK.EQ gives the same result as RANK for tied values. RANK.AVG returns the average of the tied positions instead.

Tied values share the same rank, and the ties affect later ranks. If two values share rank 1, the next value down has rank 3, not 2. Set `order` to any nonzero value to rank in ascending order, so the smallest value gets rank 1, which suits times and costs where lower is better.

## Syntax

```excel
=RANK(number, ref, [order])
```

<!-- Image 1: RANK Syntax Anatomy. See Images/Statistical/RANK.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value whose position you want. It must appear in `ref`, or the function returns `#N/A`. |
| `ref` | Yes | The list of numbers to rank against, such as `B2:B6`. Text and blank cells are ignored. |
| `order` | No | `0` or omitted ranks in descending order, with the largest value first. Any nonzero value ranks in ascending order, with the smallest value first. |

### Return Value

A whole number from 1 upward, or `#N/A` when `number` is not in `ref`.

## Examples

Examples use the scores 88, 92, 75, 92 and 60 in `B2:B6`.

### Example 1: Rank of a Score

```excel
=RANK(B2, B2:B6)
```

**Result:** `3`

Only the two scores of 92 are higher than 88, so 88 is third.

### Example 2: Tied Scores

```excel
=RANK(B3, B2:B6)
```

**Result:** `1`

Both scores of 92 share rank 1. The next lower score, 88, keeps rank 3 because two values sit above it.

### Example 3: Ascending Order

```excel
=RANK(B3, B2:B6, 1)
```

**Result:** `4`

With `order` set to 1, the smallest score is rank 1. The two 92 scores occupy ranks 4 and 5, and RANK returns the top of the tie, 4.

### Example 4: Value Not in the List

```excel
=IFERROR(RANK(95, B2:B6), "Not in list")
```

**Result:** `Not in list`

RANK can only rank a value that appears in `ref`, so the IFERROR message appears instead of `#N/A`.

## Story Problems

### Problem 1: Exam Score Position

Six students scored 71, 84, 84, 90, 65 and 77 in `C2:C7`. The teacher wants the position of a student who scored 84, with the highest score first.

| Student | Score |
| --- | --- |
| A | 71 |
| B | 84 |
| C | 84 |
| D | 90 |
| E | 65 |
| F | 77 |

**Task:** Find the rank of the score 84 in descending order.

**Solution:**

```excel
=RANK(C3, C2:C7)
```

**Answer:** `2`. Only the score 90 is higher, and both 84 scores share rank 2.

### Problem 2: Sales Leaderboard

A sales team reports units sold in `D2:D6`: 340, 295, 410, 295 and 380. The manager wants the leaderboard position of the rep who sold 380.

**Task:** Find the position of 380, with the highest number first.

**Solution:**

```excel
=RANK(D5, D2:D6)
```

**Answer:** `2`. The rep who sold 410 is first, and 380 is second.

## Use Cases

### Exam Score Positions

**Scenario:** A teacher reports each student's position in a class test.

```excel
=RANK(B2, $B$2:$B$30)
```

**Why It Works:** The absolute range keeps the reference fixed when the formula is copied down the column. Ties share a rank, which is usually what a class list should show.

### Race Results

**Scenario:** A race organizer ranks finish times so the fastest time is first.

```excel
=RANK(C2, $C$2:$C$40, 1)
```

**Why It Works:** Setting `order` to 1 ranks the smallest time first. Keep the times in one unit, such as seconds, so the ranks are comparable.

### Sales Leaderboards

**Scenario:** A sales manager shows each rep's position on a monthly leaderboard.

```excel
=RANK(D2, $D$2:$D$12)
```

**Why It Works:** The formula shows the position for each row. Use RANK.EQ for the same result in new workbooks.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | `number` does not appear in `ref`. | Check that the value is in the list, or wrap the formula in IFERROR. |
| Unexpected rank | `ref` is a relative range, so it shifts when the formula is copied. | Use absolute references such as `$B$2:$B$6`. |
| Ranks look skipped | Ties push later values down, so 1, 1, 3 appears. | This is expected. Use RANK.AVG for averaged tie ranks. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Compatibility function, kept for backward compatibility | Replaced by RANK.EQ and RANK.AVG, which Microsoft recommends for new work. |
| Google Sheets | Available | Same arguments. The optional ascending flag defaults to 0, so ranking is descending. |

## Tips and Best Practices

- Use RANK.EQ for new work that needs the same ranks as RANK, and RANK.AVG when tied values should share an average.
- Use absolute references for the list so every copied formula ranks against the same values.
- Remember that `order` 0 is descending. A nonzero value gives ascending order.
- Pair RANK with INDEX and MATCH to show the name for each position on a leaderboard.

## Related Functions

| Function | Relationship |
| --- | --- |
| [RANK.EQ](RANK.EQ.md) | The current version, which gives tied values the same rank. |
| [RANK.AVG](RANK.AVG.md) | Returns the average rank for tied values. |
| [PERCENTRANK.INC](PERCENTRANK.INC.md) | Returns the value's position as a percentage of the list. |
| [LARGE](LARGE.md) | Returns the kth largest value, the value at a given rank. |
| [SMALL](SMALL.md) | Returns the kth smallest value. |
| [COUNTIF](COUNTIF.md) | Counts values above or below a number, which gives a rank by hand. |

## Official Documentation

- [Microsoft Support: RANK function](https://support.microsoft.com/en-us/excel/functions/rank-function)
- [Google Docs Editors Help: RANK](https://support.google.com/docs/answer/3094098)
