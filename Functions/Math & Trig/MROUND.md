---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Rounding
use-case:
  - Case Pack Ordering
  - Cash Rounding
  - Cut Length Planning
related:
  - CEILING
  - FLOOR
  - ROUND
  - ROUNDDOWN
  - ROUNDUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/mround-function
  - https://support.google.com/docs/answer/3093426
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Round To Multiple
tags:
  - excel
  - multiple
  - rounding
  - sheets
---

# MROUND

## Description

**MROUND** rounds a number to the nearest multiple of another number. For example, MROUND(10, 3) returns 9 because 9 is the closest multiple of 3 to 10. Where ROUND works to a fixed number of decimal places, MROUND works to any step size, such as 6 bottles per case, 0.05 for cash, or one eighth of an inch.

When a number falls exactly halfway between two multiples, MROUND moves it to the multiple with the greater absolute value. MROUND(21, 14) returns 28 because 21 is equally far from 14 and 28. The Microsoft page describes the same outcome as rounding away from zero when the remainder is at least half the multiple.

The number and the multiple must have the same sign. Microsoft Excel returns `#NUM!` when they differ, so MROUND(5, -2) fails. Both values can be decimals.

## Syntax

```excel
=MROUND(number, multiple)
```

<!-- Image 1: MROUND Arguments. See Images/Math & Trig/MROUND.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to round. It can be a decimal and must have the same sign as `multiple`. |
| `multiple` | Yes | The step size. Results are multiples of this value. It can be a decimal and must have the same sign as `number`. |

### Return Value

A number that is a multiple of `multiple`, nearest to `number`. MROUND returns `#NUM!` in Excel when `number` and `multiple` have different signs. If either argument is zero, Excel returns 0.

<!-- Image 2: Nearest Multiple on a Number Line. See Images/Math & Trig/MROUND.md -->

## Examples

### Example 1: Nearest Multiple of Three

```excel
=MROUND(10, 3)
```

**Result:** `9`

The multiples of 3 near 10 are 9 and 12. Ten is closer to 9.

### Example 2: Decimal Step Size

```excel
=MROUND(1.3, 0.2)
```

**Result:** `1.4`

Dividing 1.3 by 0.2 gives 6.5, which sits exactly halfway between the multiples 6 x 0.2 and 7 x 0.2. The greater absolute value wins, so the result is 7 x 0.2 = 1.4.

### Example 3: Two Negative Values

```excel
=MROUND(-10, -3)
```

**Result:** `-9`

Both arguments are negative, so the signs match and the result is the negative multiple of 3 nearest to -10.

### Example 4: Rounding a Cell to Quarter Units

With `A2` containing `7.6`:

```excel
=MROUND(A2, 0.25)
```

**Result:** `7.5`

The quarter-unit multiples near 7.6 are 7.5 and 7.75. Because 7.6 is closer to 7.5, the result is 7.5.

### Example 5: Exact Halfway Point

```excel
=MROUND(21, 14)
```

**Result:** `28`

Twenty-one lies exactly between 14 and 28. MROUND moves halfway values to the multiple with the greater absolute value, which is 28.

### Example 6: Mismatched Signs

```excel
=MROUND(5, -2)
```

**Result:** `#NUM!`

The number is positive and the multiple is negative, so Excel rejects the arguments.

## Story Problems

### Problem 1: Ordering Full Cases

A bar buys bottles in cases of 6. The manager wants each order rounded to the nearest full case, so the amounts are in `B2:B5` and the rounded totals go in column `C`.

| Order | Bottles Needed |
| --- | --- |
| Friday | 37 |
| Saturday | 40 |
| Sunday | 9 |
| Monday | 20 |

**Task:** Round each order to the nearest multiple of 6.

**Solution:**

```excel
=MROUND(B2, 6)
```

Copy the formula down to `C2:C5`.

**Answer:** Friday 36, Saturday 42, Sunday 12, and Monday 18. Sunday's 9 is exactly halfway between 6 and 12, so it rounds to the greater value, 12.

### Problem 2: Cash Register Rounding

A café rounds card totals to the nearest 5 cents for the register. The raw totals are in `B2:B4`: 4.37, 9.98, and 2.503 dollars.

| Item | Total |
| --- | --- |
| Muffin | 4.37 |
| Latte | 9.98 |
| Scone | 2.503 |

**Task:** Round each total to the nearest 0.05.

**Solution:**

```excel
=MROUND(B2, 0.05)
```

**Answer:** $4.35, $10.00, and $2.50. The muffin total is 4.37, which is closer to 4.35 than to 4.40, and the scone total is 2.503, which is closest to 2.50.

## Use Cases

### Case Pack Ordering

**Scenario:** A distributor only ships products in full cases, and the sales team needs each customer quantity converted to the nearest full case.

```excel
=MROUND(OrderQty, CaseSize)
```

**Why It Works:** The formula always returns a multiple of the case size. Halfway values round up to the greater multiple, so check the tie rule with your customers before using it for minimum orders.

### Cash Rounding

**Scenario:** A store rounds final cash totals to the nearest 0.05 when the smallest coin is no longer used.

```excel
=MROUND(Total, 0.05)
```

**Why It Works:** Setting the step to 0.05 gives the nearest 5 cents. Keep the unrounded total in a separate column so the audit trail still shows the original amount.

### Cut Length Planning

**Scenario:** A workshop cuts timber in steps of one eighth of an inch and needs the nearest cut for each measurement.

```excel
=MROUND(Length, 0.125)
```

**Why It Works:** The step size of 0.125 equals one eighth, so the result is always a multiple of an eighth of an inch.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The number and multiple have different signs. | Make both positive or both negative, or use ABS on both. |
| Unexpected round up | An exact halfway value moves to the greater multiple. | Expect this behavior, or use ROUNDDOWN or CEILING if you need a fixed direction. |
| `#VALUE!` | One argument is text. | Convert the cell to a number or correct the entry. |
| `0` returned | The number or the multiple is zero. | Check the input cells, or test for zero with IF before rounding. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, 2019, 2021, 2024, Microsoft 365, and Excel for the web | Returns `#NUM!` when the signs differ. Halfway values round to the greater absolute value. |
| Google Sheets | Available | Same nearest-multiple result, and halfway values move to the greater absolute value. The help page does not describe the sign mismatch error, so test that case before relying on it. |

## Tips and Best Practices

- Use MROUND for any step size, such as cases, coins, or fractions, and use ROUND when you only need decimal places.
- Keep the step size in its own labeled cell so the rounding rule can change without editing formulas.
- Round only the final figure for display, and keep unrounded values in calculations.
- Decide on the tie rule before you round a dataset with many halfway values.
- Use CEILING or FLOOR when every value must round in one direction.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ROUND](ROUND.md) | Rounds to a number of decimal places rather than to a step size. |
| [CEILING](CEILING.md) | Always rounds up to the next multiple. |
| [FLOOR](FLOOR.md) | Always rounds down to the previous multiple. |
| [ROUNDUP](ROUNDUP.md) | Rounds away from zero to a set number of digits. |
| [ROUNDDOWN](ROUNDDOWN.md) | Rounds toward zero to a set number of digits. |

## Official Documentation

- [Microsoft Support: MROUND function](https://support.microsoft.com/en-us/excel/functions/mround-function)
- [Google Docs Editors Help: MROUND](https://support.google.com/docs/answer/3093426)
