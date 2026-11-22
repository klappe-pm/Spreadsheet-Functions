---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Rounding
use-case:
  - Overdue Day Counts
  - Whole Hour Totals
related:
  - FLOOR.MATH
  - MOD
  - ROUND
  - ROUNDDOWN
  - TRUNC
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/int-function
  - https://support.google.com/docs/answer/3093490
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Round Down to Integer
tags:
  - excel
  - rounding
  - sheets
  - truncation
---

# INT

## Description

**INT** rounds a number down to the nearest integer. Rounding down here means toward negative infinity, so INT(8.9) returns 8, and INT(-8.9) returns -9. INT uses the signed value, so a negative number moves further from zero. Use INT when the next whole number below a value is what counts, such as completed days or full hours.

INT differs from TRUNC and ROUNDDOWN for negative numbers. ROUNDDOWN with 0 digits rounds toward zero, so ROUNDDOWN(-8.9,0) returns -8, while INT returns -9. For positive numbers, all three give the same whole-number result.

INT takes a single argument and has no significance option. To round down to a multiple such as 5 or 0.25, use FLOOR.MATH or FLOOR.PRECISE. Google Sheets documents the same rounding behavior for INT.

## Syntax

```excel
=INT(number)
```

<!-- Image 1: Signed Rounding Direction. See Images/Math & Trig/INT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The real number to round down to an integer. In Sheets, this argument is named `value`. |

### Return Value

An integer: the largest whole number that is less than or equal to `number`. A whole number returns unchanged.

## Examples

### Example 1: Positive Decimal

```excel
=INT(8.9)
```

**Result:** `8`

The value 8.9 rounds down to 8. The decimal part is discarded, not rounded up.

### Example 2: Negative Decimal

```excel
=INT(-8.9)
```

**Result:** `-9`

The value -8.9 rounds down to the next integer below it, which is -9. The result moves further from zero.

### Example 3: Whole Hours From Total Hours

With 58 hours logged in `A2`:

```excel
=INT(A2/24)
```

**Result:** `2`

Dividing 58 by 24 gives 2.4167. INT keeps only the complete days, so the result is 2.

<!-- Image 2: INT Compared With ROUNDDOWN. See Images/Math & Trig/INT.md -->

### Example 4: Comparing With ROUNDDOWN

```excel
=ROUNDDOWN(-8.9,0)
```

**Result:** `-8`

ROUNDDOWN rounds toward zero, so -8.9 becomes -8. INT on the same value returns -9.

## Story Problems

### Problem 1: Overdue Day Counts

A collections team counts only full days past due. Each invoice's days past due, including the partial day, are listed in `A1:B4`.

| Invoice | Days Past Due |
| --- | --- |
| INV-101 | 4.7 |
| INV-102 | 12.2 |
| INV-103 | 0.9 |

**Task:** Count the full days past due for each invoice, then total them.

**Solution:**

```excel
=SUMPRODUCT(INT(B2:B4))
```

**Answer:** `16`. The full days are 4, 12 and 0, which total 16.

### Problem 2: Net Temperature Change

A weather log records temperature changes in degrees. The team rounds each change down to a whole degree, and a drop of 8.9 degrees is recorded as a change of -9 degrees.

| Day | Change (degrees) |
| --- | --- |
| Day 1 | -8.9 |
| Day 2 | 2.6 |

**Task:** Round each change down to a whole degree, then total the rounded changes.

**Solution:**

```excel
=SUMPRODUCT(INT(B2:B3))
```

**Answer:** `-7`. The rounded changes are -9 and 2, which total -7.

## Use Cases

### Overdue Day Counts

**Scenario:** A payment reminder system reports how many whole days each invoice has been overdue.

```excel
=INT(B2)
```

**Why It Works:** INT removes the fractional day, so a balance that is 4.7 days overdue is reported as 4 full days. Confirm that the source column records days, not hours.

### Whole Hour Totals

**Scenario:** A field crew logs work in minutes, and a report needs complete hours only.

```excel
=INT(B2/60)
```

**Why It Works:** Dividing minutes by 60 and applying INT keeps the complete hours. For 185 minutes, the result is 3 hours. Track the leftover minutes separately with MOD if they are needed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected result | A negative value moves further from zero, such as -8.9 becoming -9. | Use TRUNC if the goal is to remove the decimal part toward zero. |
| `#VALUE!` | The argument is text rather than a number. | Convert the value to a number or correct the cell reference. |
| Off-by-one result | The value is a date and time, and the time part was expected to be kept. | Expect INT to keep only the date part, or use MOD to isolate the time. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Rounds the signed value down. Negative values move further from zero. |
| Google Sheets | Available | The same rounding direction. The argument is named `value`. |

## Tips and Best Practices

- Use INT for "next whole number below" logic, and TRUNC when the decimal part should simply be removed.
- Expect negative results to move further from zero, and test with a negative value before deploying a formula.
- Use FLOOR.MATH when the rounding step is a multiple other than 1.
- Keep the source unit in the header, such as days or minutes, so the division step is easy to audit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FLOOR.MATH](FLOOR.MATH.md) | Rounds down to a multiple, not only to whole numbers. |
| [MOD](MOD.md) | Returns the remainder left after INT-style division, such as leftover minutes. |
| [ROUND](ROUND.md) | Rounds to the nearest value or a set number of decimal places. |
| [ROUNDDOWN](ROUNDDOWN.md) | Rounds toward zero, which differs from INT for negative numbers. |
| [TRUNC](TRUNC.md) | Removes the decimal part, which matches INT only for positive numbers. |

## Official Documentation

- [Microsoft Support: INT function](https://support.microsoft.com/en-us/excel/functions/int-function)
- [Google Docs Editors Help: INT](https://support.google.com/docs/answer/3093490)
