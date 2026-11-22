---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Arithmetic Operations
use-case:
  - Checksum Validation
  - Rotating Shift Schedules
  - Time Component Extraction
related:
  - INT
  - ISEVEN
  - ISODD
  - QUOTIENT
  - ROUND
  - TRUNC
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/mod-function
  - https://support.google.com/docs/answer/3093497
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Modulo
  - Remainder
tags:
  - excel
  - modular-arithmetic
  - remainder
  - sheets
---

# MOD

## Description

**MOD** returns the remainder left after one number is divided by another. MOD(10, 3) returns 1 because 3 fits into 10 three times with 1 left over. The function is the spreadsheet form of the modulo operation.

MOD is useful whenever a value needs to wrap around or be tested for divisibility. It can label even and odd numbers, cycle through a fixed list of shifts, split a total number of minutes into minutes within the hour, and pull the time of day out of a date and time value.

The sign of the result follows the divisor, not the dividend. MOD(-10, 3) returns 2, and MOD(10, -3) returns -2. This matches the usual mathematical convention, but it differs from some programming languages, so test negative inputs before relying on them. The result is always the number that makes `number = divisor x INT(number / divisor) + MOD(number, divisor)` true.

## Syntax

```excel
=MOD(number, divisor)
```

<!-- Image 1: Dividend, Divisor and Remainder. See Images/Math & Trig/MOD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to divide. It can be negative or include decimals. |
| `divisor` | Yes | The value to divide by. It cannot be zero. The result takes the sign of this value. |

### Return Value

The remainder after `number` is divided by `divisor`. MOD returns `#DIV/0!` when `divisor` is zero, and `#VALUE!` when either argument is text that cannot be read as a number.

## Examples

### Example 1: Basic Remainder

```excel
=MOD(10, 3)
```

**Result:** `1`

Three goes into 10 three times, using 9, which leaves 1.

### Example 2: Evenly Divisible Number

```excel
=MOD(15, 5)
```

**Result:** `0`

Fifteen is an exact multiple of 5, so nothing is left over. A result of 0 means the number is divisible.

### Example 3: Negative Dividend With a Positive Divisor

```excel
=MOD(-10, 3)
```

**Result:** `2`

The result takes the sign of the divisor, 3. Mathematically, -10 = 3 x (-4) + 2.

### Example 4: Positive Dividend With a Negative Divisor

```excel
=MOD(10, -3)
```

**Result:** `-2`

The result takes the sign of the divisor, -3. Mathematically, 10 = (-3) x (-4) + (-2).

### Example 5: Alternating Row Pattern

```excel
=MOD(ROW(), 2)
```

**Result:** `1` in row 1, `0` in row 2, `1` in row 3, and so on

Use this pattern in conditional formatting, such as `=MOD(ROW(), 2) = 0`, to shade every other row.

<!-- Image 2: Time of Day From a Date and Time Value. See Images/Math & Trig/MOD.md -->

### Example 6: Time of Day From a Date and Time

With `A2` containing `45000.75`:

```excel
=MOD(A2, 1)
```

**Result:** `0.75`

In spreadsheet date systems, the whole number is the date and the decimal part is the time. The decimal 0.75 is 18:00, or 6:00 PM.

## Story Problems

### Problem 1: Rotating Shift Schedule

A clinic rotates four nurses through a shift that repeats every four days. Day numbers 1 to 10 are in `A2:A11`, and column `B` should show which nurse, numbered 1 to 4, works each day.

| Day | Nurse |
| --- | --- |
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |
| 10 | |

**Task:** Fill column `B` with the nurse number for each day, then find the nurse assigned to day 10 and the number of days nurse 1 works.

**Solution:**

```excel
=MOD(A2 - 1, 4) + 1
```

Copy the formula down to `B2:B11`. Then count nurse 1 with `=COUNTIF(B2:B11, 1)`.

**Answer:** Nurse 2 works day 10, because MOD(9, 4) is 1 and adding 1 gives 2. Nurse 1 works 3 days (days 1, 5, and 9).

### Problem 2: Converting Call Minutes to Hours and Minutes

A call center logs total call durations in minutes in `B2:B5`: 185, 47, 130, and 600.

| Call | Total Minutes |
| --- | --- |
| Call A | 185 |
| Call B | 47 |
| Call C | 130 |
| Call D | 600 |

**Task:** Put the whole hours in column `C` with `INT(B2 / 60)` and the leftover minutes in column `D`. Report the leftover minutes for Call C.

**Solution:**

```excel
=MOD(B4, 60)
```

**Answer:** `10` minutes. Call C lasted 130 minutes, which is 2 hours and 10 minutes, because 130 = 60 x 2 + 10.

## Use Cases

### Rotating Shift Schedules

**Scenario:** A support team rotates staff through shifts that repeat every week, and the schedule needs to wrap back to the first person.

```excel
=INDEX(Staff, MOD(WeekNumber - 1, StaffCount) + 1)
```

**Why It Works:** MOD returns 0 to one less than the team size, so adding 1 gives a valid position in the staff list. Subtracting 1 first lines the cycle up with week 1.

### Time Component Extraction

**Scenario:** A payroll sheet stores clock-in times as date and time values and needs the time portion alone.

```excel
=MOD(ClockIn, 1)
```

**Why It Works:** Whole numbers hold the date and the fraction holds the time, so MOD by 1 removes the date. Multiply the result by 24 to get hours.

### Checksum Validation

**Scenario:** A data entry form stores a check digit that must make the digit total divisible by 10.

```excel
=MOD(SUM(DigitCells), 10) = 0
```

**Why It Works:** The formula returns TRUE when the digit total is a multiple of 10. This is a simple checksum. Standard schemes such as Luhn double alternate digits first, so use the exact rule for the code you are validating.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | The divisor is zero. | Test the divisor first with IF, or wrap the formula in IFERROR. |
| `#VALUE!` | An argument is text that is not a number. | Convert the source cell to a number or correct the entry. |
| Unexpected negative or positive sign | The result takes the sign of the divisor. | Use the divisor's sign deliberately, or apply ABS to the divisor. |
| Result close to 0 or to the divisor instead of exact | Decimal values are stored in binary, so small rounding errors appear. | Round the result, such as ROUND(MOD(A2, 0.25), 10). |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, 2019, 2021, 2024, Microsoft 365, and Excel for the web | Result has the same sign as the divisor. Returns `#DIV/0!` for a zero divisor. |
| Google Sheets | Available | Same syntax and arguments. The help page does not describe negative input or the zero divisor error, so test these cases before relying on them. |

## Tips and Best Practices

- Remember that the sign of the result follows the divisor, so MOD(-10, 3) is 2, not -1.
- Use `MOD(index - 1, count) + 1` to map any counter onto a repeating list of 1 to count.
- Use MOD(ROW(), 2) with conditional formatting for striped rows, and adjust for header rows by subtracting the header count.
- Pair MOD with INT to split a value into quotient and remainder: INT(A2 / B2) gives the quotient and MOD(A2, B2) gives the remainder.
- Round decimal results when you compare them with exact values, because binary storage can leave tiny errors.

## Related Functions

| Function | Relationship |
| --- | --- |
| [INT](INT.md) | Gives the whole-number part of a division, the quotient that pairs with MOD. |
| [QUOTIENT](QUOTIENT.md) | Returns only the integer part of a division, the companion to MOD. |
| [TRUNC](TRUNC.md) | Drops the decimal part toward zero; it differs from INT for negative numbers. |
| [ROUND](ROUND.md) | Cleans up decimal remainders before comparing them. |
| [ISEVEN](../Information/ISEVEN.md) | Tests for an even number, a simpler check than MOD(number, 2) = 0. |
| [ISODD](../Information/ISODD.md) | Tests for an odd number, a simpler check than MOD(number, 2) = 1. |

## Official Documentation

- [Microsoft Support: MOD function](https://support.microsoft.com/en-us/excel/functions/mod-function)
- [Google Docs Editors Help: MOD](https://support.google.com/docs/answer/3093497)
