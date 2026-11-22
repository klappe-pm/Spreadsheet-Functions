---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
purpose:
  - Ranking
use-case:
  - Delivery Speed Ranking
  - Leaderboard Ties
  - Support Performance Ranking
related:
  - LARGE
  - PERCENTRANK.INC
  - RANK
  - RANK.EQ
  - SMALL
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/rank-avg-function
  - https://support.google.com/docs/answer/3267309
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Average Rank
tags:
  - excel
  - ranking
  - sheets
  - ties
---

# RANK.AVG

## Description

**RANK.AVG** returns the rank of a number within a list. Unlike RANK.EQ, which gives tied values the highest rank in their group, RANK.AVG gives each tied value the average of the positions it occupies. Use it when a fair position matters more than a whole-number rank, such as comparing agents who finished with the same count.

By default the largest value has rank 1, which is descending order. Set `order` to any nonzero value to rank in ascending order, where the smallest value has rank 1. Use ascending order for measures where lower is better, such as delivery times or error counts.

RANK.AVG is part of the modern ranking family that replaced RANK. Choose RANK.EQ when tied values should share the top rank, and RANK.AVG when they should share the average.

## Syntax

```excel
=RANK.AVG(number, ref, [order])
```

<!-- Image 1: RANK.AVG Syntax Anatomy. See Images/Statistical/RANK.AVG.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value whose rank you want. It must appear in `ref`. |
| `ref` | Yes | The list of numbers to rank against, such as `B2:B6`. Non-numeric values are ignored. |
| `order` | No | `0` or omitted ranks in descending order, with the largest value first. Any nonzero value ranks in ascending order, with the smallest value first. |

### Return Value

A number from 1 upward. Whole numbers appear when the value is not tied, and a fraction such as 1.5 appears when the value shares positions with another value.

## Examples

Examples use the scores 88, 92, 75, 92 and 60 in `B2:B6`.

### Example 1: Tied Scores Share the Average Rank

```excel
=RANK.AVG(B3, B2:B6)
```

**Result:** `1.5`

The two 92 scores occupy ranks 1 and 2, so each receives (1 + 2) / 2 = 1.5.

### Example 2: Tied Scores in Ascending Order

```excel
=RANK.AVG(B3, B2:B6, 1)
```

**Result:** `4.5`

In ascending order the two 92 scores occupy ranks 4 and 5, so the average is 4.5.

### Example 3: A Value Without Ties

```excel
=RANK.AVG(B2, B2:B6)
```

**Result:** `3`

The score 88 has no tie, so its rank is a whole number.

### Example 4: Rank as a Share of the List

```excel
=RANK.AVG(B2, B2:B6) / COUNT(B2:B6)
```

**Result:** `0.6`

Dividing the rank of 3 by the five values gives 0.6, a simple share-of-list measure.

## Story Problems

### Problem 1: Support Ticket Resolutions

Six support agents resolved these numbers of tickets in `E2:E7`: 18, 22, 25, 22, 30 and 15. The team lead wants the average rank of an agent who resolved 22 tickets, with the most tickets first.

| Agent | Tickets Resolved |
| --- | --- |
| A | 18 |
| B | 22 |
| C | 25 |
| D | 22 |
| E | 30 |
| F | 15 |

**Task:** Find the average rank of the 22-ticket agent in descending order.

**Solution:**

```excel
=RANK.AVG(E3, E2:E7)
```

**Answer:** `3.5`. The two agents with 22 tickets occupy ranks 3 and 4, so their average is 3.5.

### Problem 2: Pizza Delivery Speed

Five delivery runs in `F2:F6` took 32, 28, 40, 28 and 35 minutes. Lower times rank higher. The dispatch team wants the average rank of a 28-minute run.

**Task:** Find the average rank of the 28-minute run in ascending order.

**Solution:**

```excel
=RANK.AVG(F3, F2:F6, 1)
```

**Answer:** `1.5`. The two 28-minute runs are the fastest, so they occupy ranks 1 and 2.

## Use Cases

### Delivery Speed Ranking

**Scenario:** A dispatch manager ranks drivers by average delivery time and shows tied drivers at the same position.

```excel
=RANK.AVG(C2, $C$2:$C$20, 1)
```

**Why It Works:** Ascending order puts the fastest time first. Tied drivers receive the average of their shared positions, which avoids giving one tied driver an unfair edge.

### Leaderboard Ties

**Scenario:** A games platform shows a player's rank on a leaderboard where several players have the same score.

```excel
=RANK.AVG(D2, $D$2:$D$50)
```

**Why It Works:** The average rank reflects the position range the tie occupies, so the player's rank is not overstated.

### Support Performance Ranking

**Scenario:** A support lead reports how each agent compares with the team on resolved tickets.

```excel
=RANK.AVG(E2, $E$2:$E$12)
```

**Why It Works:** Fractional ranks show when two agents are level. Pair the result with the team size to report a share of the list.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | `number` does not appear in `ref`. | Check that the value is in the list, or wrap the formula in IFERROR. |
| Unexpected rank | The range is relative, so it shifts when the formula is copied. | Use absolute references such as `$E$2:$E$12`. |
| Unexpected fraction | The value is tied, so the average rank is not a whole number. | This is expected. Use RANK.EQ for the top rank of a tie. |
| Wrong direction | `order` is left at 0 when lower values should rank first. | Set `order` to 1 for ascending ranking. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns the average of tied positions. |
| Google Sheets | Available | Same arguments and tie behavior. `is_ascending` defaults to FALSE, which ranks in descending order. |

## Tips and Best Practices

- Use RANK.AVG when tied values should share a fair average position, and RANK.EQ when they should share the top rank.
- Keep the list in absolute references so every formula ranks against the same values.
- Set `order` to 1 whenever lower numbers are better.
- Use COUNT on the same list to turn a rank into a share of the list.

## Related Functions

| Function | Relationship |
| --- | --- |
| [RANK](RANK.md) | The older function, kept for compatibility. |
| [RANK.EQ](RANK.EQ.md) | Gives tied values the top rank of their group instead of the average. |
| [PERCENTRANK.INC](PERCENTRANK.INC.md) | Returns the position of a value as a percentage of the list. |
| [LARGE](LARGE.md) | Returns the kth largest value. |
| [SMALL](SMALL.md) | Returns the kth smallest value. |

## Official Documentation

- [Microsoft Support: RANK.AVG function](https://support.microsoft.com/en-us/excel/functions/rank-avg-function)
- [Google Docs Editors Help: RANK.AVG](https://support.google.com/docs/answer/3267309)
