---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Number Theory
purpose:
  - Counting
  - Probability
use-case:
  - Ice Cream Combinations
  - Sampling With Replacement
related:
  - COMBIN
  - FACT
  - MULTINOMIAL
  - PERMUT
  - PERMUTATIONA
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/combina-function
  - https://support.google.com/docs/answer/9084101
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Combinations With Repetition
tags:
  - combinations
  - counting
  - excel
  - repetition
  - sheets
---

# COMBINA

## Description

**COMBINA** returns the number of ways to choose a set of items from a pool when the same item can be chosen more than once and the order does not matter. It is the version of `COMBIN` for selections with replacement, where each pick goes back into the pool before the next one.

Use COMBINA for counts such as the number of ice cream cones made from a set of flavors, when one flavor may be repeated, or the number of distinct results when samples are drawn with replacement. Google documents the result as equal to `COMBIN(n + k - 1, k)`, which is a useful check when you build the formula by hand.

For selections where each item may appear only once, use `COMBIN`. For selections where the order matters, use `PERMUT` or `PERMUTATIONA`. Microsoft Excel and Google Sheets accept the same two arguments in the same order.

## Syntax

```excel
=COMBINA(number, number_chosen)
```

<!-- Image 1: Repetition Versus No Repetition. See Images/Math & Trig/COMBINA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The number of items in the pool. Google Sheets calls this argument `n`. It must be zero or greater. Decimal parts are truncated. |
| `number_chosen` | Yes | The number of picks, including repeats. Google Sheets calls this argument `k`. It must be zero or greater. Decimal parts are truncated. |

### Return Value

A whole number: the count of distinct selections of `number_chosen` picks from `number` items, where repeats are allowed. The function returns `#VALUE!` when an argument is not numeric, and `#NUM!` when an argument is outside its allowed range. Google Sheets also returns `#NUM!` when `number` plus `number_chosen` is 1031 or more.

## Examples

### Example 1: Two Items Taken Twice

```excel
=COMBINA(2, 2)
```

**Result:** `3`

With items A and B, the distinct selections are AB, AA, and BB. Order does not matter, so AB and BA count once.

### Example 2: Three Picks From Four Items

```excel
=COMBINA(4, 3)
```

**Result:** `20`

Four flavors chosen three times, with repeats allowed, can be combined in 20 different ways.

### Example 3: Five Items Taken Three Times

```excel
=COMBINA(5, 3)
```

**Result:** `35`

A pool of five items and three picks with repeats gives 35 distinct selections.

### Example 4: Matching the COMBIN Equivalent

```excel
=COMBIN(4 + 3 - 1, 3)
```

**Result:** `20`

Google documents `COMBINA(n, k)` as equal to `COMBIN(n + k - 1, k)`. With n = 4 and k = 3, the equivalent is `COMBIN(6, 3)`, which returns the same 20.

### Example 5: Combined With Other Functions

```excel
=IFERROR(COMBINA(B2, C2), "Out of range")
```

**Result:** `Out of range` when the arguments are outside the allowed limits

The wrapper returns a message instead of an error code, which helps when the inputs come from a user form.

## Story Problems

### Problem 1: Ice Cream Cones With Repeats

A shop offers 4 flavors. A customer orders a cone with 3 scoops, and the same flavor may appear more than once. Order does not matter because the scoops are stacked on one cone.

| Flavors | Scoops | Possible Cones |
| --- | --- | --- |
| 4 | 3 | |

**Task:** Count the number of different cones the shop can make.

**Solution:**

```excel
=COMBINA(B2, C2)
```

**Answer:** The shop can make `20` different cones. Each cone is one combination, and a repeated flavor is allowed.

<!-- Image 2: Ice Cream Cone Count. See Images/Math & Trig/COMBINA.md -->

### Problem 2: Sampling Cards With Replacement

A quality team draws 2 cards from a box of 10 numbered cards. After each draw the card goes back into the box, so the same card can be drawn twice. The team needs the number of distinct two-card results when order does not matter.

| Box Size | Draws | Distinct Results |
| --- | --- | --- |
| 10 | 2 | |
| 6 | 3 | |

**Task:** Count the distinct results for each sampling plan.

**Solution:**

```excel
=COMBINA(B2, C2)
```

**Answer:** The first plan gives `55` distinct results and the second gives `56`. Both counts include results where the same card appears twice.

<!-- Image 3: Sampling Results Table. See Images/Math & Trig/COMBINA.md -->

## Use Cases

### Ice Cream Combinations

**Scenario:** A menu planner wants to know how many distinct three-scoop cones can be built from the flavors on the board.

```excel
=COMBINA(Flavors, 3)
```

**Why It Works:** Repeated flavors are allowed, and the count ignores the order of the scoops. Update the flavor count when the board changes and the number of cones recalculates.

### Sampling With Replacement

**Scenario:** A statistics student plans a simulation that draws small samples from a population and returns each item before the next draw.

```excel
=COMBINA(Population, SampleSize)
```

**Why It Works:** Sampling with replacement allows repeats, so the number of possible unordered samples is a combination with repetition. Use the result to check that the simulation covers the possible outcomes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | An argument is negative, or the inputs exceed the limit. In Google Sheets, `n` plus `k` of 1031 or more returns this error. | Check that both values are zero or greater and that their sum is within the limit. |
| `#VALUE!` | An argument is text or blank. | Convert the value to a number before calling the function. |
| Count is too small | `COMBIN` was used when repeats should be allowed. | Switch to `COMBINA` when the same item can be chosen again. |
| Count is too large | `COMBINA` was used when each item may appear only once. | Switch to `COMBIN` for selections without repetition. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions and Excel for the web | Arguments are named `number` and `number_chosen`. Non-integer values are truncated. |
| Google Sheets | Available | Arguments are named `n` and `k`. Returns `#NUM!` when `n` plus `k` is 1031 or more. |

## Tips and Best Practices

- Use COMBINA when repeated picks are allowed, and COMBIN when each item may appear once.
- Check a small case by hand, such as COMBINA(2, 2) = 3, before you trust the formula on large inputs.
- Keep the pool and pick counts in separate cells so scenarios are easy to compare.
- Use the Google equivalent `COMBIN(n + k - 1, k)` when a reader needs to verify the result with another function.
- Stop the sum of pool and picks well below the Google limit if the workbook may be shared with Sheets users.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMBIN](COMBIN.md) | Counts combinations when each item can be chosen only once. |
| [PERMUT](../Statistical/PERMUT.md) | Counts ordered arrangements without repetition. |
| [PERMUTATIONA](../Statistical/PERMUTATIONA.md) | Counts ordered arrangements with repetition. |
| [FACT](../Math%20%26%20Trig/FACT.md) | Returns a factorial, used when you verify a count by hand. |
| [MULTINOMIAL](../Math%20%26%20Trig/MULTINOMIAL.md) | Counts ways to split a set into groups of several sizes. |

## Official Documentation

- [Microsoft Support: COMBINA function](https://support.microsoft.com/en-us/excel/functions/combina-function)
- [Google Docs Editors Help: COMBINA](https://support.google.com/docs/answer/9084101)
