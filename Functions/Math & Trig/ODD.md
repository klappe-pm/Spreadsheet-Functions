---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Rounding
use-case:
  - Odd Batch Sizes
  - Odd Length Cutting
  - Panel Tie Breaking
related:
  - CEILING
  - EVEN
  - INT
  - ISODD
  - ROUNDUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/odd-function
  - https://support.google.com/docs/answer/3093499
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Round Up To Odd
tags:
  - excel
  - odd-numbers
  - rounding
  - sheets
---

# ODD

## Description

**ODD** rounds a number away from zero to the nearest odd integer. A value that is already an odd whole number stays the same, so ODD(3) returns 3. Any other value moves to the next odd integer on the side away from zero: ODD(2) returns 3, and ODD(1.5) returns 3.

Use ODD when an odd count is required, such as a panel of judges that must avoid ties, a batch size that must split into an odd number of stages, or a length that must be an odd number of units for a symmetric layout. ODD always rounds away from zero, so it differs from ROUND, which rounds to the nearest value, and from INT, which rounds down.

For negative numbers the rule still moves the result away from zero. ODD(-2) returns -3, and ODD(-1) returns -1. ODD is the mirror image of EVEN, which rounds away from zero to the nearest even integer.

## Syntax

```excel
=ODD(number)
```

<!-- Image 1: ODD Rounding Direction. See Images/Math & Trig/ODD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to round. It can be positive, negative, or a decimal. Text that cannot be read as a number is rejected. |

### Return Value

The nearest odd integer on the side away from zero. Odd integers are returned unchanged. ODD returns `#VALUE!` when the argument is non-numeric.

## Examples

### Example 1: Even Whole Number

```excel
=ODD(2)
```

**Result:** `3`

Two is even, so the next odd integer away from zero is 3.

### Example 2: Decimal Value

```excel
=ODD(1.5)
```

**Result:** `3`

The odd integers around 1.5 are 1 and 3. Rounding away from zero moves past 1, because 1 is less than 1.5, so the result is 3.

### Example 3: Negative Even Number

```excel
=ODD(-2)
```

**Result:** `-3`

Rounding moves away from zero, so -2 becomes -3, the next odd integer on the negative side.

### Example 4: Already Odd

With `A2` containing `7`:

```excel
=ODD(A2)
```

**Result:** `7`

An odd integer is returned unchanged.

### Example 5: Text Input

```excel
=ODD("seven")
```

**Result:** `#VALUE!`

Text is not a number, so the function returns an error.

## Story Problems

### Problem 1: Odd Sized Teams for a Quiz

A quiz organizer splits the number of players into teams and wants each team to have an odd number of members, so that a majority vote is never tied. The raw team sizes are in `B2:B5`.

| Team | Members |
| --- | --- |
| Blue | 12 |
| Green | 15 |
| Red | 8 |
| Gold | 21 |

**Task:** Round each team size up to the nearest odd number in column `C`.

**Solution:**

```excel
=ODD(B2)
```

Copy the formula down to `C2:C5`.

**Answer:** Blue 13, Green 15, Red 9, and Gold 21. Blue and Red were even, so each moves to the next odd value. Green and Gold were already odd.

<!-- Image 2: Team Size Results Panel. See Images/Math & Trig/ODD.md -->

### Problem 2: Cut Lengths in Odd Meters

A rope maker sells rods in whole odd meters. The measured lengths in `B2:B4` are 4.2, 7.0, and 3.1 meters.

| Rod | Length (m) |
| --- | --- |
| Rod A | 4.2 |
| Rod B | 7.0 |
| Rod C | 3.1 |

**Task:** Round each length to the next odd whole meter so no rod is shorter than its measurement.

**Solution:**

```excel
=ODD(B2)
```

**Answer:** Rod A is 5 m, Rod B is 7 m, and Rod C is 5 m. Rod B is already an odd whole number, so it stays at 7. The other two rods move to the next odd whole number above their measurements.

## Use Cases

### Odd Batch Sizes

**Scenario:** A production line runs batches in an odd number of stages so that a final checkpoint always has a clear majority reading.

```excel
=ODD(StageCount)
```

**Why It Works:** ODD always returns an odd integer no smaller in magnitude than the input, so the planned stage count never falls short of the requirement.

### Odd Length Cutting

**Scenario:** A fabricator needs symmetrical strips that have a single center mark, so each length must be an odd number of units.

```excel
=ODD(Length)
```

**Why It Works:** An odd number of units leaves one unit at the center, which gives the strip a single midpoint.

### Panel Tie Breaking

**Scenario:** A review board seats an odd number of panelists so that every vote has a winner.

```excel
=ODD(RequestedPanelists)
```

**Why It Works:** The result is always odd, which removes the chance of an even split. Confirm the panel size with the board, because ODD increases even numbers.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text or a blank cell. | Convert the value to a number or fill the blank. |
| Result is larger than expected | ODD rounds away from zero, so an even input always moves up. | Use ROUNDDOWN or INT when the value must go down. |
| Negative result is more negative | The rounding direction is away from zero for negative values too. | Apply ABS when only the magnitude matters. |
| Unexpected result for zero | The help pages do not describe zero input. | Test zero in your sheet, or handle zero with IF before rounding. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, 2019, 2021, 2024, Microsoft 365, and Excel for the web | Rounds away from zero to the nearest odd integer. Returns `#VALUE!` for non-numeric input. |
| Google Sheets | Available | Rounds to the next odd integer away from zero. Google's help page shows ODD(-0.6) as a sample but does not state its result, so test negative decimals before relying on them. |

## Tips and Best Practices

- Use ODD when the rule is "odd count or length", and use ROUND when the rule is "nearest value".
- Remember that ODD rounds away from zero in both directions, so it never returns a value closer to zero than the input.
- Pair ODD with EVEN to see both candidate counts, then choose the one your process needs.
- Keep the input in its own cell so the rounding result can be traced.
- Apply ODD to a derived count rather than a dollar amount, because odd rounding has no monetary meaning.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EVEN](EVEN.md) | Rounds away from zero to the nearest even integer. |
| [ISODD](../Information/ISODD.md) | Tests whether a number is odd without changing it. |
| [ROUNDUP](ROUNDUP.md) | Rounds away from zero to a set number of decimal places. |
| [CEILING](CEILING.md) | Rounds up to a multiple of a chosen step, which can be 1 for whole numbers. |
| [INT](INT.md) | Rounds down to the nearest integer, the opposite direction from ODD. |

## Official Documentation

- [Microsoft Support: ODD function](https://support.microsoft.com/en-us/excel/functions/odd-function)
- [Google Docs Editors Help: ODD](https://support.google.com/docs/answer/3093499)
