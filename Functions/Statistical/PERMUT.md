---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
purpose:
  - Counting
  - Probability
use-case:
  - Committee Role Assignments
  - Podium Finishes
  - Seating Arrangements
related:
  - COMBIN
  - COMBINA
  - FACT
  - PERMUTATIONA
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/permut-function
  - https://support.google.com/docs/answer/3094036
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Permutations
tags:
  - combinatorics
  - counting
  - excel
  - permutation
  - sheets
---

# PERMUT

## Description

**PERMUT** returns the number of ways to choose a given number of items from a pool of items when the order of the choices matters. Choosing a first, second and third place from twelve runners gives 1320 different podium orders, because the same three runners in a different order count as a different result.

Use PERMUT when each position is distinct, such as roles, places or seats. Use COMBIN when the order does not matter, such as choosing a team. Use PERMUTATIONA when the same item may be picked more than once.

Both arguments are truncated to integers, so 7.9 is treated as 7. The arguments must be numeric, and the number of items must be at least as large as the number chosen.

## Syntax

```excel
=PERMUT(number, number_chosen)
```

<!-- Image 1: Permutation Arguments Diagram. See Images/Statistical/PERMUT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The total number of items in the pool, a positive integer. Google Sheets calls this argument `n`. |
| `number_chosen` | Yes | The number of items selected for each arrangement, a non-negative integer no larger than `number`. Google Sheets calls this argument `k`. |

### Return Value

A whole number that counts the ordered arrangements. The function returns `#NUM!` when `number` is zero or negative, when `number_chosen` is negative, or when `number` is less than `number_chosen`. It returns `#VALUE!` when either argument is not numeric.

## Examples

### Example 1: Basic Count

```excel
=PERMUT(10, 3)
```

**Result:** `720`

The first pick has 10 choices, the second has 9 and the third has 8, so 10 × 9 × 8 = 720.

### Example 2: Using Cell References

Cell `A2` holds 8 and cell `A3` holds 2.

```excel
=PERMUT(A2, A3)
```

**Result:** `56`

Eight items taken two at a time give 8 × 7 = 56 ordered pairs.

### Example 3: A Race Podium

```excel
=PERMUT(12, 3)
```

**Result:** `1320`

Twelve runners can fill the gold, silver and bronze places in 12 × 11 × 10 = 1320 different orders.

### Example 4: Handling Invalid Input

```excel
=IFERROR(PERMUT(3, 5), "Invalid")
```

**Result:** `Invalid`

Three items cannot fill five places without repetition, so the function returns `#NUM!` and IFERROR shows the message.

## Story Problems

### Problem 1: Choosing a President and a Secretary

A club has seven candidates listed in `A2:A8`. Each person can hold only one office, and the two offices are different.

**Task:** Count the number of ways to fill the president and secretary offices.

**Solution:**

```excel
=PERMUT(7, 2)
```

**Answer:** `42`. Seven people can be president, then six remain for secretary, so 7 × 6 = 42.

### Problem 2: Seating Five Guests in Five Chairs

A dinner table has five chairs and five guests, and each guest sits in a different chair.

**Task:** Count the seating arrangements.

**Solution:**

```excel
=PERMUT(5, 5)
```

**Answer:** `120`. When every item is chosen, the count is the factorial of the pool size, here 5 × 4 × 3 × 2 × 1 = 120.

<!-- Image 2: Podium Orders for Three Places. See Images/Statistical/PERMUT.md -->

## Use Cases

### Podium Finishes

**Scenario:** A race organizer counts the possible top-three results before a race with a known number of entrants.

```excel
=PERMUT(Entrants, 3)
```

**Why It Works:** Each place is distinct, so order matters. Use the entrant count in a named cell so the figure updates when the field changes.

### Seating Arrangements

**Scenario:** An event planner counts how many ways a group can fill a row of reserved seats.

```excel
=PERMUT(Guests, Seats)
```

**Why It Works:** Each guest occupies a different seat, so the function counts every distinct order. Check that the number of seats never exceeds the number of guests, or the formula returns `#NUM!`.

### Committee Role Assignments

**Scenario:** A nominating committee counts the ways to assign three roles from a pool of applicants.

```excel
=PERMUT(Applicants, 3)
```

**Why It Works:** Each role is different, so the same person in two roles counts as a different assignment. Use COMBIN instead if all three people share the same role.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `number` is zero or negative, `number_chosen` is negative, or `number` is less than `number_chosen`. | Check the pool size and the count chosen. |
| `#VALUE!` | One argument is text or a blank cell. | Enter numbers or reference cells that contain numbers. |
| Smaller than expected | Decimal inputs were truncated to integers. | Enter whole numbers, or round the inputs on purpose before calling the function. |
| Count too high | COMBIN was expected, but PERMUT counts order. | Use COMBIN when the order of the selected items does not matter. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions | Both arguments are truncated to integers. Errors are `#NUM!` for invalid counts and `#VALUE!` for non-numeric input. |
| Google Sheets | Available | Arguments are named `n` and `k`. The official page does not list specific error conditions. |

## Tips and Best Practices

- Use PERMUT whenever position or role matters, and COMBIN when only membership matters.
- Check a small case by hand, such as PERMUT(3, 2) = 6 for AB, BA, AC, CA, BC and CB.
- Keep the pool size and the count chosen in labeled input cells so scenarios are easy to compare.
- Divide PERMUT by a factorial when you need the count of groups rather than ordered picks.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COMBIN](../Math%20%26%20Trig/COMBIN.md) | Counts selections when the order does not matter. |
| [COMBINA](../Math%20%26%20Trig/COMBINA.md) | Counts selections with repetition when the order does not matter. |
| [FACT](../Math%20%26%20Trig/FACT.md) | Returns the factorial, which equals PERMUT(n, n). |
| [PERMUTATIONA](PERMUTATIONA.md) | Counts ordered arrangements when items may repeat. |

## Official Documentation

- [Microsoft Support: PERMUT function](https://support.microsoft.com/en-us/excel/functions/permut-function)
- [Google Docs Editors Help: PERMUT](https://support.google.com/docs/answer/3094036)
