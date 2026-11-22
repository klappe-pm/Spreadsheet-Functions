---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
purpose:
  - Ranking
use-case:
  - Quiz Ranking
  - Revenue Leaderboards
  - Sales Position Reporting
related:
  - LARGE
  - PERCENTRANK.INC
  - RANK
  - RANK.AVG
  - SMALL
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/rank-eq-function
  - https://support.google.com/docs/answer/3267310
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Equal Rank
tags:
  - excel
  - ranking
  - sheets
  - ties
---

# RANK.EQ

## Description

**RANK.EQ** returns the rank of a number within a list. Tied values receive the same rank, and that rank is the top position of the tie. The largest value has rank 1 by default, which is descending order. Use it for leaderboards, sales positions and any report where a shared rank is the expected result.

RANK.EQ replaces RANK in Excel. The two functions return the same results, and RANK.EQ is the name to use in new workbooks. Ties affect later ranks: if two values share rank 1, the next value has rank 3, and no value has rank 2.

Set `order` to any nonzero value to rank in ascending order, where the smallest value has rank 1. Use RANK.AVG instead when tied values should show their average position.

## Syntax

```excel
=RANK.EQ(number, ref, [order])
```

<!-- Image 1: RANK.EQ Syntax Anatomy. See Images/Statistical/RANK.EQ.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value whose rank you want. It must appear in `ref`. |
| `ref` | Yes | The list of numbers to rank against, such as `G2:G6`. Non-numeric values are ignored. |
| `order` | No | `0` or omitted ranks in descending order, with the largest value first. Any nonzero value ranks in ascending order, with the smallest value first. |

### Return Value

A whole number from 1 upward. Tied values return the same whole number, and the function returns `#N/A` when `number` is not in `ref`.

## Examples

Examples use the revenue figures 42, 55, 42, 38 and 61 in `G2:G6`.

### Example 1: Rank of the Largest Value

```excel
=RANK.EQ(G6, G2:G6)
```

**Result:** `1`

The value 61 is the largest, so it has rank 1.

### Example 2: Tied Values Share the Top Rank

```excel
=RANK.EQ(G2, G2:G6)
```

**Result:** `3`

Both 42 values occupy positions 3 and 4 in descending order, and RANK.EQ returns the top position, 3.

### Example 3: Ascending Order

```excel
=RANK.EQ(G2, G2:G6, 1)
```

**Result:** `2`

In ascending order the values are 38, 42, 42, 55 and 61. The first 42 occupies positions 2 and 3, so RANK.EQ returns 2.

### Example 4: Value Not in the List

```excel
=IFERROR(RANK.EQ(50, G2:G6), "Not in list")
```

**Result:** `Not in list`

The value 50 does not appear in `G2:G6`, so the message replaces the `#N/A` error.

## Story Problems

### Problem 1: Store Revenue Leaderboard

Five stores reported monthly revenue in thousands in `G2:G6`: 42, 55, 42, 38 and 61. The regional manager wants the leaderboard position of stores with 42 thousand in revenue.

| Store | Revenue (thousands) |
| --- | --- |
| North | 42 |
| East | 55 |
| South | 42 |
| West | 38 |
| Central | 61 |

**Task:** Find the rank of a store with 42 thousand in revenue, with the highest revenue first.

**Solution:**

```excel
=RANK.EQ(G2, G2:G6)
```

**Answer:** `3`. Central and East rank 1 and 2, and both 42 stores share rank 3.

### Problem 2: Quiz Score Positions

A quiz class scored 9, 7, 9, 6, 8 and 9 in `H2:H7`. The teacher wants the position of the student who scored 8, with the highest score first.

**Task:** Find the rank of the score 8 in descending order.

**Solution:**

```excel
=RANK.EQ(H6, H2:H7)
```

**Answer:** `4`. Three students scored 9 and occupy ranks 1 to 3, so the score of 8 is fourth.

## Use Cases

### Quiz Ranking

**Scenario:** A teacher shows each student's position on a class quiz, with ties shown as the same position.

```excel
=RANK.EQ(B2, $B$2:$B$30)
```

**Why It Works:** Ties share the top rank, which matches how most class lists are read. The absolute range keeps the list fixed as the formula is copied down.

### Revenue Leaderboards

**Scenario:** A regional manager ranks stores each month and highlights the top three.

```excel
=RANK.EQ(C2, $C$2:$C$40)
```

**Why It Works:** The rank is a whole number, so a simple test such as `<=3` picks out the top three stores, including ties.

### Sales Position Reporting

**Scenario:** A sales operations analyst reports each rep's position against quota attainment.

```excel
=RANK.EQ(D2, $D$2:$D$25)
```

**Why It Works:** The formula returns the same rank for tied reps, which makes it clear when two reps are level.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | `number` does not appear in `ref`. | Check that the value is in the list, or wrap the formula in IFERROR. |
| Unexpected rank | The range is relative, so it shifts when the formula is copied. | Use absolute references such as `$G$2:$G$6`. |
| Gap in ranks | Ties push later values down, so no value has rank 2 after two values share rank 1. | This is expected. Use RANK.AVG for averaged ranks. |
| Reversed order | `order` is left at 0 when lower values should rank first. | Set `order` to 1 for ascending ranking. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Replaces RANK. Tied values share the top rank of the group. |
| Google Sheets | Available | Same arguments. `is_ascending` defaults to FALSE, which ranks in descending order. |

## Tips and Best Practices

- Use RANK.EQ for new workbooks, and use RANK.AVG when averaged positions are better for the report.
- Make the list an absolute range so every formula ranks against the same values.
- Use `order` 1 for measures where lower is better, such as times or costs.
- Combine RANK.EQ with INDEX and MATCH to show the name next to each position.

## Related Functions

| Function | Relationship |
| --- | --- |
| [RANK](RANK.md) | The older function that returns the same results. |
| [RANK.AVG](RANK.AVG.md) | Gives tied values the average of their positions. |
| [PERCENTRANK.INC](PERCENTRANK.INC.md) | Returns the value's position as a percentage of the list. |
| [LARGE](LARGE.md) | Returns the kth largest value. |
| [SMALL](SMALL.md) | Returns the kth smallest value. |

## Official Documentation

- [Microsoft Support: RANK.EQ function](https://support.microsoft.com/en-us/excel/functions/rank-eq-function)
- [Google Docs Editors Help: RANK.EQ](https://support.google.com/docs/answer/3267310)
