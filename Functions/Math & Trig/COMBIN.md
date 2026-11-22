---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Number Theory
purpose:
  - Counting
  - Probability
use-case:
  - Committee Selection
  - Lottery Odds
  - Team Pairing
related:
  - COMBINA
  - FACT
  - MULTINOMIAL
  - PERMUT
  - PERMUTATIONA
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/combin-function
  - https://support.google.com/docs/answer/3093400
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Combinations Without Repetition
  - Choose Function
tags:
  - combinations
  - counting
  - excel
  - probability
  - sheets
---

# COMBIN

## Description

**COMBIN** returns the number of ways to choose a set of items from a larger pool when the order of the items does not matter. Each combination counts once, so choosing Ana and Ben is the same as choosing Ben and Ana. The result is written nCk and read "n choose k".

Use COMBIN to count possible groups: committees, teams, sample sets, or lottery picks. It is the basis of many probability calculations, because the chance of one specific group is 1 divided by the number of possible groups.

Each item can be chosen at most once. When items may be chosen more than once, use `COMBINA` instead. For ordered selections, where the position of each item matters, use `PERMUT`. Microsoft Excel and Google Sheets use the same two arguments in the same order.

## Syntax

```excel
=COMBIN(number, number_chosen)
```

<!-- Image 1: Pool and Selection Arguments. See Images/Math & Trig/COMBIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The total number of items in the pool. Google Sheets calls this argument `n`. It must be zero or greater and at least as large as `number_chosen`. |
| `number_chosen` | Yes | The number of items in each group. Google Sheets calls this argument `k`. It must be zero or greater. Decimal parts of both arguments are truncated. |

### Return Value

A whole number: the count of distinct groups of `number_chosen` items that can be drawn from `number` items. The function returns `#VALUE!` when an argument is not numeric, and `#NUM!` when `number` or `number_chosen` is negative, or when `number` is smaller than `number_chosen`.

## Examples

### Example 1: Two Person Teams

```excel
=COMBIN(8, 2)
```

**Result:** `28`

Eight people can form 28 different pairs when the order inside each pair does not matter.

### Example 2: Three Items From Ten

```excel
=COMBIN(10, 3)
```

**Result:** `120`

Ten items give 120 distinct groups of three.

### Example 3: Truncated Arguments

```excel
=COMBIN(5.9, 2)
```

**Result:** `10`

Microsoft truncates numeric arguments to integers, so 5.9 is treated as 5 and the function returns COMBIN(5, 2).

### Example 4: A Standard Card Hand

```excel
=COMBIN(52, 5)
```

**Result:** `2598960`

A five-card hand from a 52-card deck can be dealt in 2,598,960 different ways.

### Example 5: Combined With Other Functions

```excel
=IFERROR(COMBIN(B2, C2), "Check inputs")
```

**Result:** `Check inputs` when B2 is 5 and C2 is 6

The pool is smaller than the group, so `COMBIN` returns `#NUM!`. The `IFERROR` wrapper returns a readable message instead.

## Story Problems

### Problem 1: Choosing a Review Committee

A department has 12 members and must form a committee of 3. A second department has 8 members and needs a pair for a joint review. A third has 20 members and needs a panel of 4.

| Department | Members | Seats | Possible Groups |
| --- | --- | --- | --- |
| Operations | 12 | 3 | |
| Quality | 8 | 2 | |
| Engineering | 20 | 4 | |

**Task:** Count the possible groups for each department.

**Solution:**

```excel
=COMBIN(B2, C2)
```

Copy the formula down to row 4.

**Answer:** Operations has `220` possible committees, Quality has `28` possible pairs, and Engineering has `4845` possible panels. Each count is C(n, k) for its pool and seats.

<!-- Image 2: Committee Group Counts. See Images/Math & Trig/COMBIN.md -->

### Problem 2: Odds for Two Lottery Games

A lottery game picks 6 numbers from 49. A second game picks 5 numbers from 36. Each ticket is one combination, so the number of combinations gives the number of tickets needed to cover every possible draw.

| Game | Pool Size | Numbers Picked | Combinations |
| --- | --- | --- | --- |
| Game A | 49 | 6 | |
| Game B | 36 | 5 | |

**Task:** Count the combinations in each game.

**Solution:**

```excel
=COMBIN(B2, C2)
```

**Answer:** Game A has `13983816` combinations and Game B has `376992`. Covering every draw in Game A would need that many tickets, which is why the odds are so long.

<!-- Image 3: Lottery Combination Counts. See Images/Math & Trig/COMBIN.md -->

## Use Cases

### Committee Selection

**Scenario:** A project manager must choose a three-person review panel from a list of 15 candidates and wants to know how many panels are possible.

```excel
=COMBIN(15, 3)
```

**Why It Works:** Order does not matter for a panel, so every set of three people is counted once. The result tells the manager how many panel options exist before any names are chosen.

### Lottery Odds

**Scenario:** A game designer compares the chance of winning under two rule sets.

```excel
=1 / COMBIN(Pool[Size], Pool[Picks])
```

**Why It Works:** Each ticket covers exactly one combination, so the chance of a single winning ticket is one divided by the total count. Check that the pool and pick columns match the rule set you are modeling.

### Team Pairing

**Scenario:** A tournament organizer needs to know how many different doubles teams can be formed from a group of players.

```excel
=COMBIN(Players, 2)
```

**Why It Works:** A doubles team is a pair with no order, so the count is a combination of two. The formula updates when the player count changes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `number` is smaller than `number_chosen`, or either argument is negative. | Check that the pool is at least as large as the group, and that both values are zero or greater. |
| `#VALUE!` | One argument is text, blank, or a formula that returns text. | Convert the value to a number before calling the function. |
| Count is too small | A decimal argument was truncated, such as 5.9 becoming 5. | Round the input deliberately before calling the function. |
| Count is too large | Ordered selections were counted, but the order does not matter. | Use `PERMUT` only when the order of items changes the outcome. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions and Excel for the web | Arguments are named `number` and `number_chosen`. Numeric arguments are truncated to integers. |
| Google Sheets | Available | Arguments are named `n` and `k`. The page describes the result as FACT(n) divided by FACT(k) times FACT(n minus k). |

## Tips and Best Practices

- Use COMBIN when order does not matter, and PERMUT when it does.
- Use COMBINA when the same item may be chosen more than once.
- Keep the pool size and the group size in separate cells so the counts update when the rules change.
- Check that the pool is at least as large as the group before you copy the formula down a column.
- Use the count as the denominator when you calculate the probability of one specific group.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMBINA](COMBINA.md) | Counts combinations when items may repeat. |
| [PERMUT](../Statistical/PERMUT.md) | Counts ordered arrangements without repetition. |
| [PERMUTATIONA](../Statistical/PERMUTATIONA.md) | Counts ordered arrangements with repetition. |
| [FACT](../Math%20%26%20Trig/FACT.md) | Returns a factorial, the building block of combinations. |
| [MULTINOMIAL](../Math%20%26%20Trig/MULTINOMIAL.md) | Counts ways to split a set into groups of several sizes. |

## Official Documentation

- [Microsoft Support: COMBIN function](https://support.microsoft.com/en-us/excel/functions/combin-function)
- [Google Docs Editors Help: COMBIN](https://support.google.com/docs/answer/3093400)
