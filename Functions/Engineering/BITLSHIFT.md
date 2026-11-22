---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bitwise Operations
purpose:
  - Bitwise Operations
use-case:
  - Power of Two Scaling
  - Sensor Count Scaling
related:
  - BITAND
  - BITOR
  - BITRSHIFT
  - BITXOR
  - POWER
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/bitlshift-function
  - https://support.google.com/docs/answer/9061443
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bit Left Shift
tags:
  - bitwise
  - excel
  - powers-of-two
  - sheets
---

# BITLSHIFT

## Description

**BITLSHIFT** moves the bits of a whole number to the left by a set number of places and returns the result in decimal. Each place to the left doubles the value, so shifting by 3 multiplies the number by 8. Zeros fill the empty positions on the right.

Use BITLSHIFT when a model multiplies by a power of 2 and the bit pattern is the clearest way to express the step. A negative shift amount moves bits to the right, which gives the same result as BITRSHIFT. For ordinary multiplication by a power of 2, the POWER function or the `*` operator does the same job.

In Microsoft Excel, the number must be an integer from 0 to `2^48 - 1` (281,474,976,710,655), and the shift amount must be between -53 and 53. An input outside these limits returns `#NUM!`. Google Sheets requires a non-negative value and a shift amount between -53 and 53.

BITLSHIFT is available in both Microsoft Excel and Google Sheets.

## Syntax

```excel
=BITLSHIFT(number, shift_amount)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/BITLSHIFT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A whole number, zero or greater. Google Sheets calls it `value`. |
| `shift_amount` | Yes | The number of places to shift, from -53 to 53. A positive value shifts left, and a negative value shifts right. |

### Return Value

A decimal number equal to the input times 2 raised to the shift amount, with any bits shifted past the input range dropped. The function returns `#NUM!` in Excel when an argument is outside its limits, and `#VALUE!` when an argument is not numeric.

## Examples

### Example 1: Shifting Left by Three Places

```excel
=BITLSHIFT(5, 3)
```

**Result:** `40`

The binary value 101 becomes 101000 after three zeros are added on the right, which is 40.

### Example 2: Negative Shift Moves Bits Right

```excel
=BITLSHIFT(100, -3)
```

**Result:** `12`

A shift of -3 moves each bit three places to the right. The binary value 1100100 becomes 1100, which is 12.

### Example 3: Filled Down a Column

Values in `A2:A4` are 1, 3 and 6, and each row shifts by 2 places.

```excel
=BITLSHIFT(A2, 2)
```

Fill the formula down to `B4`.

**Result:** `4` (A2), `12` (A3), `24` (A4)

Each result is the input multiplied by 4, which is the effect of a two-place left shift.

<!-- Image 2: Left Shift Bit Diagram. See Images/Engineering/BITLSHIFT.md -->

### Example 4: Shift Outside the Limit

```excel
=BITLSHIFT(5, 60)
```

**Result:** `#NUM!`

The shift amount 60 is above the limit of 53, so the function returns an error.

## Story Problems

### Problem 1: Scaling Raw Sensor Counts

A test bench stores a raw count and a shift for each sensor board. The engineer scales each count by its shift and needs the total of the three scaled values.

| Board | Raw Count | Shift |
| --- | --- | --- |
| B1 | 3 | 2 |
| B2 | 5 | 3 |
| B3 | 7 | 1 |

**Task:** Put `=BITLSHIFT(B2, C2)` in `D2`, fill it down to `D4`, then add the three results.

**Solution:**

```excel
=SUM(D2:D4)
```

**Answer:** `66`, from 12 + 40 + 14.

<!-- Image 3: Results Panel for the Story Problems. See Images/Engineering/BITLSHIFT.md -->

### Problem 2: Reducing a Count With a Negative Shift

A line counter reports 45 items in a batch. The supervisor wants the number of complete groups of four, which is the count shifted right by two places.

| Item | Value |
| --- | --- |
| Batch count | 45 |
| Shift | -2 |

**Task:** Calculate the shifted value with a negative shift amount.

**Solution:**

```excel
=BITLSHIFT(45, -2)
```

**Answer:** `11`. The two lowest bits are dropped, and 45 divided by 4 gives 11 complete groups.

## Use Cases

### Power of Two Scaling

**Scenario:** A pricing sheet doubles or quadruples a base quantity for each tier, and the modeler prefers an explicit shift over a power expression.

```excel
=BITLSHIFT(Table1[BaseUnits], Table1[Tier])
```

**Why It Works:** The tier number is the shift amount, so each row multiplies its base units by 2 raised to the tier.
Keep the tier between 0 and 53, because larger values return `#NUM!`.

### Sensor Count Scaling

**Scenario:** A monitoring team converts raw counts from a board that reports in fixed steps, shifting each count by a fixed number of places.

```excel
=BITLSHIFT(C2, 4)
```

**Why It Works:** A four-place shift multiplies each count by 16, which matches the step size on the board.
Check the result against a plain multiplication once, so the team trusts the shift.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The number is negative or above `2^48 - 1`, or the shift amount is outside -53 to 53. | Validate both inputs before the call. |
| `#VALUE!` | An argument is text, blank or an error. | Convert the input to a number or reference a numeric cell. |
| Unexpected result | Bits shifted right were dropped, so the value is smaller than expected. | Use a plain division when the fraction matters. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365 and current Excel versions | Number is limited to 0 to `2^48 - 1`, and shift amount to -53 to 53. Check the Microsoft Support page for the exact version list. |
| Google Sheets | Available | Arguments are `value` and `shift_amount`. The value must be non-negative, and the shift amount must be between -53 and 53. |

## Tips and Best Practices

- Use the shift amount for powers of 2 only when the bit meaning matters; otherwise use the `*` operator or POWER.
- Keep shift amounts in a labeled input column so a reviewer can see the scale for each row.
- Test one row by hand before filling a long column.
- Remember that a negative shift discards bits and returns the whole-number part of the division.
- Pair BITLSHIFT with BITRSHIFT in a model that moves values both ways.

## Related Functions

| Function | Relationship |
| --- | --- |
| [BITAND](BITAND.md) | Tests the bits that a shift produces. |
| [BITOR](BITOR.md) | Combines shifted flags into one value. |
| [BITRSHIFT](BITRSHIFT.md) | Shifts bits to the right, the same as a negative shift here. |
| [BITXOR](BITXOR.md) | Compares the bit patterns of two numbers. |
| [POWER](../Math%20%26%20Trig/POWER.md) | Multiplies by a power of 2 without bit notation. |

## Official Documentation

- [Microsoft Support: BITLSHIFT function](https://support.microsoft.com/en-us/excel/functions/bitlshift-function)
- [Google Docs Editors Help: BITLSHIFT](https://support.google.com/docs/answer/9061443)
