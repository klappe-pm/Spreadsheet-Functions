---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Rounding
use-case:
  - Credit Adjustment Rounding
  - Quarter Hour Billing
related:
  - CEILING.MATH
  - FLOOR
  - FLOOR.PRECISE
  - INT
  - MROUND
  - ROUNDDOWN
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/floor-math-function
  - https://support.google.com/docs/answer/9061444
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - excel
  - negative-numbers
  - rounding
  - sheets
---

# FLOOR.MATH

## Description

**FLOOR.MATH** rounds a number down to the nearest integer, or to the nearest multiple of a significance value. Positive numbers always round down. The third argument, mode, decides the direction for negative numbers. When mode is omitted or 0, a negative number rounds down, away from zero: FLOOR.MATH(-8.1,2) returns -10. When mode is any nonzero value, a negative number rounds toward zero: FLOOR.MATH(-5.5,2,-1) returns -4.

Use FLOOR.MATH when the direction for negative amounts matters, such as credit adjustments, or when a time or money total must be cut down to whole blocks. Both the significance argument and the mode argument are optional. Significance defaults to 1, so FLOOR.MATH(6.7) returns 6. The sign of the significance is ignored.

FLOOR.MATH is the newer replacement for FLOOR in Excel. If every negative value should always round down, regardless of direction settings, use FLOOR.PRECISE instead. The official pages do not describe error values for FLOOR.MATH, so validate inputs before the call.

## Syntax

```excel
=FLOOR.MATH(number, [significance], [mode])
```

<!-- Image 1: Three Arguments and the Mode Switch. See Images/Math & Trig/FLOOR.MATH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to round down. |
| `significance` | No | The multiple to round to. The default is 1. The sign of this argument is ignored. |
| `mode` | No | The direction for negative numbers. A value of 0 or an omitted argument rounds them away from zero. Any nonzero value rounds them toward zero. |

### Return Value

A number: `number` rounded down to the nearest integer or to the nearest multiple of `significance`, with the direction for negative values set by `mode`.

## Examples

### Example 1: Round to a Multiple

```excel
=FLOOR.MATH(24.3,5)
```

**Result:** `20`

The value 24.3 divided by 5 is 4.86. The fraction is dropped, leaving 4, and 4 × 5 = 20.

### Example 2: Whole Number Without Significance

```excel
=FLOOR.MATH(6.7)
```

**Result:** `6`

Significance defaults to 1, so the value rounds down to the nearest integer.

### Example 3: Negative Number With the Default Mode

```excel
=FLOOR.MATH(-8.1,2)
```

**Result:** `-10`

The mode is omitted, so the negative value moves down, away from zero. The nearest multiple of 2 below -8.1 is -10.

<!-- Image 2: Negative Values by Mode. See Images/Math & Trig/FLOOR.MATH.md -->

### Example 4: Negative Number Rounded Toward Zero

```excel
=FLOOR.MATH(-5.5,2,-1)
```

**Result:** `-4`

Mode -1 is nonzero, so the negative value rounds toward zero. The nearest multiple of 2 between -5.5 and zero is -4.

## Story Problems

### Problem 1: Quarter Hour Billing

A consultant bills clients in full quarter hours only. Three sessions were logged in `A1:B4`.

| Session | Hours Logged |
| --- | --- |
| Kickoff | 3.9 |
| Review | 2.6 |
| Workshop | 1.2 |

**Task:** Round each session down to a multiple of 0.25 hours, then total the billable hours.

**Solution:**

```excel
=SUMPRODUCT(FLOOR.MATH(B2:B4,0.25))
```

**Answer:** `7.25`. The billable times are 3.75, 2.5 and 1.0 hours, which total 7.25.

### Problem 2: Credit Adjustments Rounded Toward Zero

A billing team reduces negative credit adjustments to the nearest even dollar, always moving toward zero, so no customer receives more credit than the calculation allows.

| Adjustment | Amount |
| --- | --- |
| Refund A | -5.5 |
| Refund B | -7.5 |
| Refund C | -9.9 |

**Task:** Round each adjustment toward zero to the nearest multiple of 2, then total the results.

**Solution:**

```excel
=SUMPRODUCT(FLOOR.MATH(B2:B4,2,-1))
```

**Answer:** `-18`. The rounded values are -4, -6 and -8, which total -18.

## Use Cases

### Quarter Hour Billing

**Scenario:** A legal or consulting firm bills time in quarter-hour blocks and must never bill more time than was logged.

```excel
=FLOOR.MATH(B2,0.25)
```

**Why It Works:** Rounding down to 0.25 keeps the billed time at or below the logged time. Confirm the logged time is in hours, not minutes, before applying the formula.

### Credit Adjustment Rounding

**Scenario:** A payments team rounds negative credit adjustments toward zero so that a reversal never grows past its original amount.

```excel
=FLOOR.MATH(B2,1,-1)
```

**Why It Works:** Mode -1 moves a negative number toward zero, so the adjustment shrinks rather than growing. Use the same mode consistently across the column so the rule stays uniform.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected result | Mode is omitted or 0, so a negative value moves further from zero. | Pass a nonzero mode, such as -1, to round negative values toward zero. |
| Unexpected result | Significance is left out, so it defaults to 1. | Enter the significance explicitly in every formula. |
| `#VALUE!` | An argument is text rather than a number. | Convert the value to a number or correct the cell reference. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel versions | Mode 0 or omitted rounds negative numbers away from zero; any nonzero mode rounds them toward zero. |
| Google Sheets | Available | The same three arguments. Mode 0 or blank rounds negative numbers away from zero; any other value rounds them toward zero. |

## Tips and Best Practices

- Set the mode deliberately for negative values, because omitting it rounds away from zero.
- Enter significance explicitly so that the rounding step is visible to reviewers.
- Use FLOOR.PRECISE when every negative value should round down regardless of mode.
- Round to the needed decimals with ROUND first when a value lies on a multiple and decimal noise may affect the result.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CEILING.MATH](CEILING.MATH.md) | Rounds up with the same mode logic for negative numbers. |
| [FLOOR](FLOOR.md) | The older Excel function that rounds down with a required significance. |
| [FLOOR.PRECISE](FLOOR.PRECISE.md) | Always rounds down, whatever the sign of the number. |
| [INT](INT.md) | Rounds down to an integer with no significance or mode argument. |
| [MROUND](MROUND.md) | Rounds to the nearest multiple rather than always down. |
| [ROUNDDOWN](ROUNDDOWN.md) | Rounds toward zero to a set number of decimal places. |

## Official Documentation

- [Microsoft Support: FLOOR.MATH function](https://support.microsoft.com/en-us/excel/functions/floor-math-function)
- [Google Docs Editors Help: FLOOR.MATH](https://support.google.com/docs/answer/9061444)
