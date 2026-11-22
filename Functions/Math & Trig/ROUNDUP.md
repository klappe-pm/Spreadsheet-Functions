---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Number Formatting
  - Rounding
use-case:
  - Billing in Time Blocks
  - Packaging Quantities
  - Staff Shift Planning
related:
  - CEILING
  - CEILING.MATH
  - ROUND
  - ROUNDDOWN
  - TRUNC
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/roundup-function
  - https://support.google.com/docs/answer/3093443
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Round Up
  - Round Away From Zero
tags:
  - ceiling
  - excel
  - precision
  - rounding
  - sheets
---

# ROUNDUP

## Description

**ROUNDUP** rounds a number away from zero to a set number of decimal places. Unlike ROUND, which follows the rule that 5 or greater moves up, ROUNDUP always moves away from zero whatever the digit being dropped. A positive number gets larger, and a negative number gets more negative. For example, ROUNDUP(2.001, 0) returns 3, not 2.

Use ROUNDUP when a shortfall is worse than a surplus, such as ordering enough pallets, billing for any started time block, or planning enough staff. It makes sure a partial unit is counted as a whole one.

The num_digits argument also accepts negative values to round to tens, hundreds, or thousands. ROUNDUP always rounds away from zero, so ROUNDUP(-1234, -2) returns -1300, not -1200.

ROUNDUP and CEILING both round upward, but they answer different questions. ROUNDUP rounds to a count of decimal places or powers of 10. CEILING rounds up to a multiple you choose, such as 0.5 or 15. Microsoft Excel and Google Sheets calculate ROUNDUP the same way.

## Syntax

```excel
=ROUNDUP(number, num_digits)
```

<!-- Image 1: Rounding Argument Anatomy. See Images/Math & Trig/ROUNDUP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The numeric value to round up. Positive values get larger, and negative values become more negative. |
| `num_digits` | Yes | The digit position to round to. Positive values set decimal places, 0 rounds to a whole number, and negative values round to tens (-1), hundreds (-2), thousands (-3), and so on. |

### Return Value

Returns a number rounded away from zero to the requested digit position. For a positive input the result is greater than or equal to the input. For a negative input the result is less than or equal to the input. Returns 0 when the input is 0. The function returns #VALUE! when an argument is text that cannot be read as a number.

## Examples

### Example 1: Round Up to a Whole Number

```excel
=ROUNDUP(2.1, 0)
```

**Result:** 3

Any fraction above zero moves the result up to the next whole number. The 0.1 that remains after the decimal point is enough to change 2 into 3.

### Example 2: Round Up a Negative Number

```excel
=ROUNDUP(-2.1, 0)
```

**Result:** -3

For negative numbers, away from zero means more negative. The absolute value increases, so -2.1 becomes -3.

<!-- Image 2: Rounding Direction Comparison. See Images/Math & Trig/ROUNDUP.md -->

### Example 3: Round Up to Two Decimal Places

```excel
=ROUNDUP(3.14159, 2)
```

**Result:** 3.15

The third decimal digit (1) would be dropped by ROUND, but ROUNDUP forces the second decimal place up. The result is 3.15.

### Example 4: Round Up to the Nearest Ten

```excel
=ROUNDUP(1234, -1)
```

**Result:** 1240

With num_digits set to -1, the value rounds to tens. Even the 4 in the ones place is enough to move the result up to 1240.

### Example 5: Round Up a Negative Value to the Nearest Hundred

```excel
=ROUNDUP(-1250, -2)
```

**Result:** -1300

The value moves away from zero, so -1250 becomes -1300 rather than -1200. This is the same behavior as the positive case, mirrored.

### Example 6: Round Up a Large Value to the Nearest Hundred

```excel
=ROUNDUP(7218.4, -2)
```

**Result:** 7300

The hundreds digit is 2, and any remaining amount rounds it up to 3. The 18.4 that follows is still enough to move the result to 7300.

## Story Problems

### Problem 1: Pallets for Customer Orders

A regional distributor ships bottled water on pallets that hold 120 units each. A pallet must be sent in full, so each order needs enough pallets to cover all of its units.

| Order | Units |
| --- | --- |
| O-101 | 1046 |
| O-102 | 240 |
| O-103 | 1201 |
| O-104 | 95 |

**Task:** Find the total number of pallets needed for the four orders.

**Solution:**

```excel
=SUMPRODUCT(ROUNDUP(B2:B5/120, 0))
```

**Answer:** `23`, because the orders need 9, 2, 11, and 1 pallets. Order O-102 fills exactly two pallets, and order O-103 needs a partial eleventh pallet.

### Problem 2: Supplier Price Increase

A stationery supplier raises each item price by 2.75 percent. Prices are rounded up to the next cent, so the supplier never quotes less than the increased price.

| Item | Current Price |
| --- | --- |
| Desk Lamp | 14.99 |
| Notebook Set | 7.45 |
| Office Chair | 102.10 |
| Pen Pack | 3.20 |

**Task:** Find the total of the four new prices after each price is increased and rounded up to the cent.

**Solution:**

```excel
=SUMPRODUCT(ROUNDUP(B2:B5*1.0275, 2))
```

**Answer:** `131.27`, from the new prices 15.41, 7.66, 104.91, and 3.29. For example, 14.99 times 1.0275 is 15.4022, which rounds up to 15.41.

## Use Cases

### Billing in Time Blocks

**Scenario:** A repair service bills in 15-minute blocks, and any started block is charged in full.

```excel
=ROUNDUP(B2/15, 0) * 15
```

**Why It Works:** Dividing minutes by 15 gives a count of blocks. ROUNDUP counts a partial block as a full one, and multiplying by 15 returns the billable minutes. A job of 47 minutes bills as 60 minutes.

### Packaging Quantities

**Scenario:** A bakery orders flour in packs of 12 units, and a customer orders 25 units. The bakery must buy complete packs.

```excel
=ROUNDUP(B2/B3, 0) * B3
```

**Why It Works:** ROUNDUP(25/12, 0) returns 3 packs. Multiplying by the pack size gives 36 units, which covers the order.

### Staff Shift Planning

**Scenario:** A warehouse team needs 61 labor hours to finish a receiving job, and each shift covers 8 hours. The planner must schedule whole shifts.

```excel
=ROUNDUP(B2/8, 0)
```

**Why It Works:** The division gives 7.625 shifts, and ROUNDUP schedules 8 whole shifts. This keeps the plan from falling short of the hours needed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text, not a number. | Convert the text with VALUE or correct the source cell. |
| Unexpected negative result | Negative values move away from zero. | Use ROUNDDOWN or TRUNC when the value should move toward zero. |
| Overstated total | ROUNDUP was used where standard rounding was intended. | Use ROUND for financial totals and reported figures. |
| Wrong digit position | The sign of num_digits was misread. | Positive values count decimals, and -2 means hundreds. |
| Unchanged value | The input is already at the requested precision. | Check the input for hidden decimals, such as a value of 5.0000001. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2024, Excel 2021, Excel 2019, Excel 2016, and Excel for the web | Both arguments are required. Negative num_digits rounds to the left of the decimal point. |
| Google Sheets | Available | The second argument is named places and is optional, defaulting to 0. Behavior matches Excel. |

## Tips and Best Practices

- Use ROUNDUP for "at least" quantities, such as trucks, pallets, or staff shifts, where a shortfall causes a bigger problem than a surplus.
- Multiply back by the pack or block size after ROUNDUP to get the quantity actually ordered or billed.
- Use CEILING for custom steps such as 0.25 or 5, because ROUNDUP works only with decimal places and powers of 10.
- Do not use ROUNDUP for invoice totals or reported actuals, where ROUND is usually the correct method.
- Test edge cases such as exact whole numbers, very small fractions, and negative values before using the result in a contract.
- Document the rounding rule when it affects customer-facing figures, because it is a policy choice.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CEILING](CEILING.md) | Rounds up to a multiple you choose, such as 0.5 or 15. |
| [CEILING.MATH](CEILING.MATH.md) | Rounds up to a multiple, with options for negative numbers. |
| [ROUND](ROUND.md) | Standard rounding that rounds up only when the next digit is 5 or greater. |
| [ROUNDDOWN](ROUNDDOWN.md) | Rounds toward zero, the opposite direction. |
| [TRUNC](TRUNC.md) | Removes digits toward zero without rounding. |

## Official Documentation

- [Microsoft Support: ROUNDUP function](https://support.microsoft.com/en-us/excel/functions/roundup-function)
- [Google Docs Editors Help: ROUNDUP](https://support.google.com/docs/answer/3093443)
