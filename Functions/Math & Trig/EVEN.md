---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Rounding
use-case:
  - Carton Pairing
  - Packaging Rounding
  - Tray Loading Checks
related:
  - CEILING
  - FLOOR
  - INT
  - ODD
  - ROUND
  - ROUNDUP
  - TRUNC
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/even-function
  - https://support.google.com/docs/answer/3093409
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Round Up to Even
tags:
  - excel
  - rounding
  - sheets
---

# EVEN

## Description

**EVEN** rounds a number to the nearest even integer, moving away from zero. A positive value rounds up to the next even integer, and a negative value rounds down to the next even integer with a larger absolute value. A number that is already an even integer does not change.

EVEN differs from ROUND and ROUNDUP, which round to a number of decimal places. EVEN always returns an even integer, so a value such as 2.1 becomes 4, not 2. Use it for packaging, pairing and batching rules where the count must come in even pairs.

To round away from zero to the next whole number instead, use ROUNDUP with 0 decimal places. To round toward zero, use TRUNC.

## Syntax

```excel
=EVEN(number)
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/EVEN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to round. Google Sheets names this argument `value`. A non-numeric value returns `#VALUE!`. |

### Return Value

A number: the input rounded away from zero to the nearest even integer. The result is `#VALUE!` when the input is not numeric.

## Examples

### Example 1: Positive Fraction

```excel
=EVEN(1.5)
```

**Result:** `2`

1.5 rounds up to the nearest even integer, which is 2.

### Example 2: Odd Whole Number

```excel
=EVEN(3)
```

**Result:** `4`

An odd integer moves up to the next even integer.

### Example 3: Even Whole Number

```excel
=EVEN(2)
```

**Result:** `2`

An even integer does not change.

### Example 4: Negative Number

```excel
=EVEN(-1)
```

**Result:** `-2`

Negative values round away from zero, so -1 moves to -2 rather than to 0.

### Example 5: Value From a Cell

Cell A2 holds `7.2`.

```excel
=EVEN(A2)
```

**Result:** `8`

Any fraction above 7 rounds up to 8, because 8 is the next even integer.

<!-- Image 2: Rounding Direction on a Number Line. See Images/Math & Trig/EVEN.md -->

## Story Problems

### Problem 1: Carton Pairing

A packing line puts cartons on a conveyor in pairs. Each carton count is recorded in column B, and any odd count must be raised to the next even number before the pairs are added up.

| Carton | Count |
| --- | --- |
| Carton 1 | 3 |
| Carton 2 | 8 |
| Carton 3 | 5 |
| Carton 4 | 12 |

**Task:** Round each count up to an even number and add the rounded counts in one formula.

**Solution:**

```excel
=SUMPRODUCT(EVEN(B2:B5))
```

**Answer:** `30`. The rounded counts are 4, 8, 6 and 12, which add to 30.

### Problem 2: Tray Loading

A bakery needs an even number of trays for each batch. The planner records a tray count of 7.9 for Batch Y and needs the even count to load.

| Batch | Trays |
| --- | --- |
| Batch X | 2.3 |
| Batch Y | 7.9 |

**Task:** Round the Batch Y tray count to an even number.

**Solution:**

```excel
=EVEN(B3)
```

**Answer:** `8`, because 7.9 rounds up to the next even integer.

## Use Cases

### Carton Pairing

**Scenario:** A packing sheet stores the number of cartons for each order in a table named Cartons. The total number of paired cartons feeds a daily report.

```excel
=SUMPRODUCT(EVEN(Cartons[Count]))
```

**Why It Works:** SUMPRODUCT rounds every count and adds the results in one step. The formula always rounds up, so the report slightly overstates the physical count when odd numbers are present.

### Tray Loading Checks

**Scenario:** A planner checks whether each tray count is already even or will be adjusted before the loading schedule is printed.

```excel
=IF(EVEN(B2)=B2,"Already Even","Rounds Up")
```

**Why It Works:** Only an even integer equals its own EVEN result, so the check separates counts that need no change from those that will be raised.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The input is text or another non-numeric value. | Check the source cell, or convert the text to a number. |
| Result is higher than expected | The input is a fraction, so it moves up to the next even integer. | Use ROUNDUP or ROUND if you need a different rule. |
| Negative result is larger in size | Negative values move away from zero. | This is expected behavior. Use TRUNC if you need the value moved toward zero. |
| Result is unexpectedly 2 for an input near 1 | The input is 1.5 or 1.01, and both round to 2. | Confirm the rounding rule with the business owner before relying on it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in the Math and trigonometry group. | The argument is named `number`. |
| Google Sheets | Available | The argument is named `value`. The page describes the same rule for negative values, rounding to a larger negative even number. |

## Tips and Best Practices

- Use EVEN when the business rule requires pairs, and use ROUNDUP when the rule is about whole units.
- Test one negative input before using EVEN with negative values, because the direction is away from zero.
- Keep the source counts in a separate column so the rounding can be audited.
- Apply EVEN after totals are calculated only when the rule applies to the total rather than to each row.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CEILING](CEILING.md) | Rounds up to a multiple of a chosen significance. |
| [FLOOR](FLOOR.md) | Rounds down to a multiple of a chosen significance. |
| [INT](INT.md) | Rounds down to the nearest integer. |
| [ODD](ODD.md) | Rounds away from zero to the nearest odd integer. |
| [ROUND](ROUND.md) | Rounds to a chosen number of decimal places. |
| [ROUNDUP](ROUNDUP.md) | Rounds away from zero to a chosen number of decimal places. |
| [TRUNC](TRUNC.md) | Removes the decimal part, moving toward zero. |

## Official Documentation

- [Microsoft Support: EVEN function](https://support.microsoft.com/en-us/excel/functions/even-function)
- [Google Docs Editors Help: EVEN](https://support.google.com/docs/answer/3093409)
