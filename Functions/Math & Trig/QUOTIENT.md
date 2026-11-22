---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Arithmetic
purpose:
  - Arithmetic Operations
use-case:
  - Full Case Counts
  - Pallet Load Planning
  - Whole Hour Billing
related:
  - FLOOR
  - INT
  - MOD
  - ROUNDDOWN
  - TRUNC
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/quotient-function
  - https://support.google.com/docs/answer/3093436
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Integer Division
  - Whole Quotient
tags:
  - arithmetic
  - division
  - excel
  - sheets
---

# QUOTIENT

## Description

**QUOTIENT** divides one number by another and returns only the whole-number part of the result. The remainder is discarded. `=QUOTIENT(17,5)` returns 3, because 5 goes into 17 three full times with 2 left over. The function is a counting tool: it answers how many complete groups fit, not how large the fraction is.

Use QUOTIENT when partial units have no value, such as full cases, full pallets, or completed billing hours. The ordinary division operator returns a fraction instead. The official Excel page gives the contrast directly: `=5/2` returns 2.5, while `=QUOTIENT(5,2)` returns 2. Pair QUOTIENT with MOD when you also need the leftover amount.

QUOTIENT truncates toward zero, so negative results move toward zero rather than down. The result of `QUOTIENT(-17,5)` is -3, not -4. If you need a floor for positive and negative numbers alike, use INT instead, which rounds toward negative infinity.

## Syntax

```excel
=QUOTIENT(numerator, denominator)
```

<!-- Image 1: Quotient and Remainder Layout. See Images/Math & Trig/QUOTIENT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `numerator` | Yes | The number to be divided, also called the dividend. It can be negative or contain decimals. |
| `denominator` | Yes | The number to divide by, also called the divisor. It must not be zero. |

### Return Value

A whole number: the integer part of `numerator` divided by `denominator`, with the sign of the true quotient and any fraction removed. If either argument is not numeric, QUOTIENT returns `#VALUE!`.

<!-- Image 2: Division Operator Versus QUOTIENT. See Images/Math & Trig/QUOTIENT.md -->

## Examples

### Example 1: Whole Groups From a Division

```excel
=QUOTIENT(17,5)
```

**Result:** `3`

Five fits into 17 three times, with a remainder of 2 that QUOTIENT drops.

### Example 2: Negative Numerator

```excel
=QUOTIENT(-17,5)
```

**Result:** `-3`

The true quotient is -3.4. QUOTIENT truncates toward zero, so the result is -3.

### Example 3: Decimal Inputs

```excel
=QUOTIENT(7.5,2)
```

**Result:** `3`

The true quotient is 3.75. The integer part is 3, and the 0.75 is removed.

### Example 4: Full Units in a Shipment

```excel
=QUOTIENT(1000,24)
```

**Result:** `41`

A shipment of 1,000 bottles packed 24 to a case contains 41 full cases. The formula ignores the 16 loose bottles.

### Example 5: Leftover Units With MOD

```excel
=MOD(1000,24)
```

**Result:** `16`

MOD returns the remainder after division. Together, Example 4 and this example account for all 1,000 bottles: 41 full cases of 24 plus 16 loose bottles.

## Story Problems

### Problem 1: Full Pallets From a Warehouse Count

A distribution center receives 1,450 boxes of the same product. Each pallet holds 48 boxes, and only full pallets can be shipped as one unit.

| Item | Value |
| --- | --- |
| Boxes Received | 1450 |
| Boxes per Pallet | 48 |

**Task:** Calculate how many full pallets the center can ship.

**Solution:**

```excel
=QUOTIENT(B2,B3)
```

**Answer:** `30` full pallets. The 30 pallets hold 1,440 boxes, which leaves 10 boxes that do not fill a pallet.

### Problem 2: Billable Hours for a Repair Call

A technician bills in full 60-minute blocks. A repair call lasted 185 minutes.

| Item | Value |
| --- | --- |
| Call Length (minutes) | 185 |
| Block Length (minutes) | 60 |

**Task:** Calculate the number of full billable hours, ignoring the leftover minutes.

**Solution:**

```excel
=QUOTIENT(B2,B3)
```

**Answer:** `3` full hours. The remaining 5 minutes fall short of a full block and are not billed.

## Use Cases

### Full Case Counts

**Scenario:** A grocery buyer orders product by the case, and each store needs only complete cases counted.

```excel
=QUOTIENT(B2,C2)
```

**Why It Works:** The number of units in `B2` is divided by the units per case in `C2`. The result counts complete cases, which avoids promising a partial case to a store.

### Pallet Load Planning

**Scenario:** A logistics planner compares full pallets with leftover boxes for each shipment.

```excel
=QUOTIENT(D2,E2)&" pallets, "&MOD(D2,E2)&" boxes left over"
```

**Why It Works:** QUOTIENT gives the full pallets and MOD gives the leftover boxes, so the planner sees both figures in one text string.

### Whole Hour Billing

**Scenario:** A service firm charges a flat rate for each completed hour of work and nothing for a partial hour.

```excel
=QUOTIENT(B2,60)*C2
```

**Why It Works:** The minutes in `B2` are divided by 60 to count complete hours, and the hourly rate in `C2` multiplies that count. The formula can be wrapped in ROUND if the rate has decimals.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | One of the arguments is text or another non-numeric value. | Convert the input to a number, or check for stray text in the cell. |
| `#DIV/0!` | The denominator is zero. | Guard the formula with IF, for example `=IF(C2=0,"",QUOTIENT(B2,C2))`. |
| Unexpected fraction | The division operator was used instead of QUOTIENT, so the result still has a decimal. | Use QUOTIENT when only the whole part is wanted. |
| Unexpected negative result | A negative numerator truncates toward zero, not down. | Use INT if the result must always round down, including for negative numbers. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | Non-numeric arguments return `#VALUE!`. Truncates toward zero. |
| Google Sheets | Available | Same two arguments. The official page states that the divisor cannot be zero. |

## Tips and Best Practices

- Use QUOTIENT with MOD to show both full units and leftovers.
- Use INT instead of QUOTIENT when a floor is needed for negative values.
- Guard against a zero denominator with IF, because a blank input can otherwise break a whole column.
- Remember that `=5/2` returns 2.5 and `=QUOTIENT(5,2)` returns 2, so choose the function that matches the business rule.
- Use QUOTIENT rather than `ROUND(A/B,0)` when the rule is whole units only, because `ROUND(18/5,0)` returns 4 while `QUOTIENT(18,5)` returns 3.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FLOOR](FLOOR.md) | Rounds down to a multiple of a chosen significance value. |
| [INT](INT.md) | Rounds down to the nearest integer, which differs from QUOTIENT for negative results. |
| [MOD](MOD.md) | Returns the remainder that QUOTIENT discards. |
| [ROUNDDOWN](ROUNDDOWN.md) | Truncates a number toward zero to a set number of digits. |
| [TRUNC](TRUNC.md) | Removes the decimal part of a number toward zero, similar to QUOTIENT applied to a single value. |

## Official Documentation

- [Microsoft Support: QUOTIENT function](https://support.microsoft.com/en-us/excel/functions/quotient-function)
- [Google Docs Editors Help: QUOTIENT](https://support.google.com/docs/answer/3093436)
