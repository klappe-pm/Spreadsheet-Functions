---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
purpose:
  - Counting
  - Probability
use-case:
  - Access Code Combinations
  - Scoop Stack Options
related:
  - COMBIN
  - COMBINA
  - FACT
  - PERMUT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/permutationa-function
  - https://support.google.com/docs/answer/9368324
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Permutations With Repetition
tags:
  - combinatorics
  - excel
  - permutation
  - repetition
  - sheets
---

# PERMUTATIONA

## Description

**PERMUTATIONA** returns the number of ordered arrangements when each pick can repeat an item that was already chosen. With `number` items and `number_chosen` picks, the result equals `number` raised to the power of `number_chosen`. For example, choosing two items from three with repetition gives 3 × 3 = 9 ordered results, including pairs such as AA and BB.

Use PERMUTATIONA for codes, PIN numbers and stacks where repeats are allowed. Use PERMUT when every pick must be a different item. Both arguments are truncated to integers before the calculation.

The function is a specialist tool for counting. Most business calculations that need combinations use COMBIN or PERMUT instead.

## Syntax

```excel
=PERMUTATIONA(number, number_chosen)
```

<!-- Image 1: Permutationa Arguments Diagram. See Images/Statistical/PERMUTATIONA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The total number of items available to pick from. Decimals are truncated to integers. |
| `number_chosen` | Yes | The number of picks in each arrangement. Decimals are truncated to integers. |

### Return Value

A whole number equal to `number` raised to the power of `number_chosen`. The function returns `#NUM!` for invalid numeric values, such as a total of zero with picks to make, and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Two Picks From Three Items

```excel
=PERMUTATIONA(3, 2)
```

**Result:** `9`

Each of the two picks can be any of the three items, so 3 × 3 = 9.

<!-- Image 2: Nine Results With Repetition. See Images/Statistical/PERMUTATIONA.md -->

### Example 2: Three-Digit Codes

```excel
=PERMUTATIONA(10, 3)
```

**Result:** `1000`

Each digit from 0 to 9 can repeat, so three digits give 10 × 10 × 10 = 1000 codes, from 000 to 999.

### Example 3: Two Picks From Five Items

```excel
=PERMUTATIONA(5, 2)
```

**Result:** `25`

Five items chosen twice with repetition give 5 × 5 = 25 results.

### Example 4: Truncated Inputs

```excel
=PERMUTATIONA(3.9, 2.2)
```

**Result:** `9`

Both decimals are truncated to 3 and 2, so the result matches Example 1.

## Story Problems

### Problem 1: Three-Digit Access Codes

A door keypad accepts any three digits from 0 to 9, and a digit may repeat.

**Task:** Count how many three-digit codes the keypad can accept.

**Solution:**

```excel
=PERMUTATIONA(10, 3)
```

**Answer:** `1000`. Each of the three positions has ten choices, so 10 × 10 × 10 = 1000.

### Problem 2: Scoop Stacks

A shop offers six flavors. A customer stacks three scoops, and the same flavor may appear more than once. The order from bottom to top matters.

| Flavor |
| --- |
| Vanilla |
| Chocolate |
| Mint |
| Lemon |
| Berry |
| Coffee |

**Task:** Count the number of different three-scoop stacks.

**Solution:**

```excel
=PERMUTATIONA(6, 3)
```

**Answer:** `216`. Each of the three scoops can be any of the six flavors, so 6 × 6 × 6 = 216.

## Use Cases

### Access Code Combinations

**Scenario:** A facilities team estimates how many PIN codes a keypad design can produce before it chooses the code length.

```excel
=PERMUTATIONA(Digits, CodeLength)
```

**Why It Works:** Repeats are allowed, so the count grows quickly with length. Keep the digit count and code length in named input cells so the team can compare designs.

### Scoop Stack Options

**Scenario:** A menu planner counts how many distinct stacks a customer can build from a fixed flavor list.

```excel
=PERMUTATIONA(Flavors, Scoops)
```

**Why It Works:** Each scoop is chosen independently and the order matters, so the function counts every distinct stack. Use PERMUT if a flavor can appear only once.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The total number of items is zero, so no picks are possible. | Check that the item count is at least 1. |
| `#VALUE!` | An argument is text or a blank cell. | Enter numbers or reference cells that contain numbers. |
| Much larger than expected | Repetition was counted, but the items should be distinct. | Use PERMUT when each item can appear only once. |
| Smaller than expected | Decimal inputs were truncated to integers. | Enter whole numbers on purpose. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Both arguments are truncated to integers. Returns `#NUM!` for invalid numeric values. |
| Google Sheets | Available | Arguments are named `number` and `number_chosen`. The official page states that `number_chosen` must be less than or equal to `number`. The Excel page does not state that rule. |

## Tips and Best Practices

- Use PERMUTATIONA only when repeats are allowed, and PERMUT when they are not.
- Check a small case by listing it: PERMUTATIONA(3, 2) gives AA, AB, AC, BA, BB, BC, CA, CB and CC.
- Store the item count and pick count in labeled cells so the scenario is easy to audit.
- Use it for counting possibilities, not for probability, unless you divide by the total number of outcomes.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PERMUT](PERMUT.md) | Counts ordered arrangements when items cannot repeat. |
| [COMBIN](../Math%20%26%20Trig/COMBIN.md) | Counts selections when the order does not matter. |
| [COMBINA](../Math%20%26%20Trig/COMBINA.md) | Counts selections with repetition when the order does not matter. |
| [FACT](../Math%20%26%20Trig/FACT.md) | Returns the factorial used in permutation counts. |

## Official Documentation

- [Microsoft Support: PERMUTATIONA function](https://support.microsoft.com/en-us/excel/functions/permutationa-function)
- [Google Docs Editors Help: PERMUTATIONA](https://support.google.com/docs/answer/9368324)
