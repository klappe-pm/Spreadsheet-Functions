---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Rounding
use-case:
  - Full Case Counts
  - Truncated Unit Pricing
related:
  - FLOOR
  - INT
  - MOD
  - ROUND
  - ROUNDDOWN
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/trunc-function
  - https://support.google.com/docs/answer/3093588
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Truncate
  - Truncate Digits
tags:
  - excel
  - rounding
  - sheets
  - truncation
---

# TRUNC

## Description

**TRUNC** shortens a number by dropping its less significant digits. With no second argument it removes the decimal part and returns a whole number. With a second argument it keeps that many digits after the decimal point. TRUNC never rounds: 8.9 becomes 8, and -8.9 becomes -8.

Use TRUNC when cutting digits must be exact, such as counting only full cases, or showing a price in cents without raising it. ROUND is the better choice when the nearest value matters.

TRUNC and INT both produce whole numbers, but they differ for negative values. TRUNC drops the decimal part, so TRUNC(-4.3) returns -4. INT rounds down to the next lower integer, so INT(-4.3) returns -5.

## Syntax

```excel
=TRUNC(number, [num_digits])
```

<!-- Image 1: Truncation on a Number Line. See Images/Math & Trig/TRUNC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The number to shorten. Google Sheets calls this argument `value`. |
| `num_digits` | No | The number of digits to keep after the decimal point. Default 0, which returns a whole number. A negative value sets the digits to the left of the decimal point to zero. Google Sheets calls this argument `places`. |

### Return Value

A number with no more decimal places than `num_digits` allows. Text that cannot be read as a number returns `#VALUE!`.

## Examples

### Example 1: Whole Number Part

```excel
=TRUNC(8.9)
```

**Result:** `8`

The decimal part .9 is removed without rounding up.

### Example 2: Negative Number

```excel
=TRUNC(-8.9)
```

**Result:** `-8`

Truncation moves a negative value toward zero, so -8.9 becomes -8.

<!-- Image 2: Digits Argument Positions. See Images/Math & Trig/TRUNC.md -->

### Example 3: Keeping Two Decimal Places

```excel
=TRUNC(3.141592654,2)
```

**Result:** `3.14`

The second argument keeps two digits after the decimal point. The digit after 4 is dropped, not rounded.

### Example 4: Negative Digits

```excel
=TRUNC(1234.567,-2)
```

**Result:** `1200`

A negative second argument sets the tens and ones digits to zero and drops the decimal part.

### Example 5: Comparing TRUNC and INT

```excel
=TRUNC(-4.3)
=INT(-4.3)
```

**Result:** `-4` for TRUNC and `-5` for INT

Both functions return a whole number, but INT rounds down to -5 while TRUNC drops the decimal part to -4.

## Story Problems

### Problem 1: Full Cases Only

A warehouse packs bottles into cases of 12. Each customer order must ship only full cases, and any leftover bottles stay in the warehouse.

| Order | Bottles |
| --- | --- |
| Harbor Cafe | 150 |
| Lakeside Deli | 98 |
| Pine Bistro | 240 |

**Task:** Find the total number of full cases to ship across all three orders.

**Solution:**

```excel
=SUMPRODUCT(TRUNC(B2:B4/12))
```

**Answer:** `40` full cases, because 150 bottles give 12 cases, 98 give 8, and 240 give 20. Eight bottles remain unpacked.

<!-- Image 3: Case Count Worksheet. See Images/Math & Trig/TRUNC.md -->

### Problem 2: Unit Cost in Whole Cents

A café's supplier lists unit costs with four decimal places. The café's pricing policy keeps each cost in whole cents without rounding up.

| Item | Unit Cost ($) |
| --- | --- |
| Sugar | 0.4378 |
| Flour | 0.3867 |

**Task:** Find the sugar unit cost in whole cents, without rounding. Sugar is in row 2.

**Solution:**

```excel
=TRUNC(B2,2)
```

**Answer:** `0.43`. ROUND would give 0.44, because the third digit is 7.

## Use Cases

### Full Case Counts

**Scenario:** A fulfillment team needs to know how many complete cases can ship from each order, with the leftover bottles tracked separately.

```excel
=TRUNC(Orders[Bottles]/12)
```

**Why It Works:** Dividing by the case size and truncating leaves only the complete cases. Subtracting the cases times 12 from the total gives the leftover bottles.

### Truncated Unit Pricing

**Scenario:** A shop shows unit prices in cents but must not round a price up.

```excel
=TRUNC(UnitCost,2)
```

**Why It Works:** Keeping two decimal places without rounding means a cost of 0.4378 shows as 0.43 instead of 0.44. Use this only when the policy requires cutting, not rounding.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text that cannot be read as a number. | Convert the value to a number. |
| Unexpected whole number for a negative value | INT was expected, but TRUNC drops the decimal part, so -4.3 becomes -4. | Use INT when the result must round down to the next lower integer. |
| Decimal places missing | The second argument was left out, so the result has no decimal places. | Add the number of digits you need as the second argument. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Second argument named `num_digits`. Default is 0. |
| Google Sheets | Available | Second argument named `places`. The same truncation behavior applies. |

## Tips and Best Practices

- Use TRUNC when a cut must not round, and ROUND when the nearest value matters.
- Use `MOD(number, divisor)` to find the leftover amount after TRUNC returns the full groups.
- Choose the number of digits deliberately, because omitting the second argument returns a whole number.
- `ROUNDDOWN` takes the same digits argument and rounds toward zero, so its results match TRUNC for both positive and negative numbers.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FLOOR](FLOOR.md) | Rounds down to a multiple of a chosen significance. |
| [INT](INT.md) | Rounds down to the next lower integer, which differs from TRUNC for negative numbers. |
| [MOD](MOD.md) | Returns the remainder, such as the leftover bottles after full cases. |
| [ROUND](ROUND.md) | Rounds to the nearest value instead of cutting digits. |
| [ROUNDDOWN](ROUNDDOWN.md) | Rounds toward zero with the same digits argument. |

## Official Documentation

- [Microsoft Support: TRUNC function](https://support.microsoft.com/en-us/excel/functions/trunc-function)
- [Google Docs Editors Help: TRUNC](https://support.google.com/docs/answer/3093588)
