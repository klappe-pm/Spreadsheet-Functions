---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Legacy Compatibility
purpose:
  - Rounding
use-case:
  - Case Pack Rounding
  - Price Point Rounding
related:
  - CEILING.MATH
  - CEILING.PRECISE
  - FLOOR
  - ISO.CEILING
  - ROUNDUP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/ceiling-function
  - https://support.google.com/docs/answer/3093471
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Round Up To Multiple
tags:
  - compatibility
  - excel
  - pricing
  - rounding
  - sheets
---

# CEILING

## Description

**CEILING** rounds a number up to the nearest multiple of a significance value. "Up" means away from zero: a positive number moves to a larger value, and a negative number moves to a value with a larger absolute value. A number that is already an exact multiple does not change.

Microsoft lists CEILING in its Compatibility category, which means it is kept for older workbooks. For new work, use `CEILING.MATH`, which lets you choose how negative numbers round, or `CEILING.PRECISE`, which always rounds a number up toward positive infinity. Both newer functions cover the same purpose and handle negative inputs in a more predictable way.

CEILING is still useful for rounding prices or quantities to a fixed step, such as nickels or case packs, when the workbook already depends on it. Google Sheets accepts the same two values, but it names the second argument `factor` and makes it optional with a default of 1.

## Syntax

```excel
=CEILING(number, significance)
```

<!-- Image 1: CEILING Rounding Direction. See Images/Math & Trig/CEILING.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to round. Positive and negative values are both accepted. |
| `significance` | Yes | The multiple to round to, such as 1, 0.05, or 6. Google Sheets calls this argument `factor`, makes it optional, and defaults it to 1. It cannot be 0. |

### Return Value

A number equal to `number` rounded up to the nearest multiple of `significance`. The function returns `#VALUE!` when either argument is not numeric. A negative `number` with a positive `significance` rounds toward zero, so `-2.5` with a significance of 2 returns `-2`.

## Examples

### Example 1: Rounding Up to the Next Whole Number

```excel
=CEILING(2.5, 1)
```

**Result:** `3`

The value 2.5 is rounded up to the next multiple of 1.

### Example 2: A Negative Number With a Positive Significance

```excel
=CEILING(-2.5, 2)
```

**Result:** `-2`

The nearest multiple of 2 above -2.5 is -2. Negative numbers with a positive significance move toward zero.

### Example 3: A Negative Number With a Negative Significance

```excel
=CEILING(-2.5, -2)
```

**Result:** `-4`

Both values are negative, so the rounding moves away from zero to the multiple -4.

### Example 4: Rounding to a Fraction

```excel
=CEILING(0.234, 0.01)
```

**Result:** `0.24`

The value 0.234 is rounded up to the next hundredth.

### Example 5: Combined With Other Functions

```excel
=CEILING(A2, 0.05)
```

**Result:** `12.4` when A2 contains 12.37

Rounding up to the next nickel (0.05) keeps prices on a fixed step. The story problems use this pattern.

## Story Problems

### Problem 1: Case Packs for a Stationery Order

A school supplier sells items in cases of 6. Staff enter the number of units each class wants, and the order must be filled in full cases.

| Item | Units Wanted | Units to Order |
| --- | --- | --- |
| Pens | 13 | |
| Notebooks | 24 | |
| Markers | 31 | |
| Erasers | 40 | |
| Labels | 7 | |

**Task:** Round each quantity up to a full case of 6 and total the units to order.

**Solution:**

```excel
=CEILING(B2, 6)
```

Copy the formula down to row 6, then total column C with `=SUM(C2:C6)`.

**Answer:** The units to order are 18, 24, 36, 42, and 12, for a total of `132` units. The total is 132 because 18 + 24 + 36 + 42 + 12 = 132.

<!-- Image 2: Case Pack Rounding Table. See Images/Math & Trig/CEILING.md -->

### Problem 2: Price Point Rounding to the Nickel

A café rounds the cost of each menu item up to the next nickel so the cash drawer stays simple. The unrounded costs are in column B.

| Item | Cost | Rounded Price |
| --- | --- | --- |
| Latte | 12.37 | |
| Muffin | 4.02 | |
| Soup | 8.49 | |
| Tea | 0.61 | |

**Task:** Round each cost up to the next nickel and total the rounded prices.

**Solution:**

```excel
=CEILING(B2, 0.05)
```

**Answer:** The rounded prices are 12.40, 4.05, 8.50, and 0.65. The total is `25.60`.

<!-- Image 3: Nickel Rounding Results. See Images/Math & Trig/CEILING.md -->

## Use Cases

### Case Pack Rounding

**Scenario:** A purchasing team converts requested units into full cases before it sends an order to a supplier.

```excel
=CEILING(Requests[Units], 6)
```

**Why It Works:** Each request is rounded up to the next full case. The result never falls short of what the requester asked for, so the team does not need a separate check.

### Price Point Rounding

**Scenario:** A small retailer rounds computed prices to the nearest nickel for a cash-only checkout.

```excel
=CEILING(B2 * (1 + TaxRate), 0.05)
```

**Why It Works:** The tax-inclusive price is calculated first, then rounded up to the next nickel. Keep the rounding as the last step so the tax is not rounded twice.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | One of the arguments is text or a blank cell that holds text. | Convert the value to a number, or check for text with `ISNUMBER`. |
| Unexpected negative result | A negative number rounds toward zero when the significance is positive. | Use `CEILING.MATH` or `CEILING.PRECISE` if the direction must be set explicitly. |
| Result is not a multiple | The significance is a text value or a formatted cell that does not hold the intended number. | Check that the significance cell contains a plain number. |
| Zero in Google Sheets | The `factor` argument is 0. | Use a nonzero factor, because Google Sheets does not accept 0. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions and Excel for the web | Listed in the Compatibility category. Both arguments are required in the Microsoft syntax. |
| Google Sheets | Available | Second argument is named `factor` and is optional with a default of 1. Google documents that `factor` cannot be 0. |

## Tips and Best Practices

- Use `CEILING.MATH` or `CEILING.PRECISE` in new workbooks, since they handle negative numbers with clear rules.
- Keep the significance in its own cell so the rounding step is easy to change.
- Round the final value, not an intermediate one, when the result feeds a price or a total.
- Check results for negative inputs before you rely on them, because the direction differs from the positive case.
- Use `ROUNDUP` when you need to round to a number of decimal places rather than to a multiple.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CEILING.MATH](CEILING.MATH.md) | Newer function with a mode argument that sets how negative numbers round. |
| [CEILING.PRECISE](CEILING.PRECISE.md) | Newer function that always rounds up toward positive infinity. |
| [FLOOR](../Math%20%26%20Trig/FLOOR.md) | Rounds down to the nearest multiple, the opposite direction. |
| [ISO.CEILING](../Math%20%26%20Trig/ISO.CEILING.md) | Rounds up to a multiple using the ISO standard rules. |
| [ROUNDUP](../Math%20%26%20Trig/ROUNDUP.md) | Rounds up to a number of decimal places rather than a multiple. |

## Official Documentation

- [Microsoft Support: CEILING function](https://support.microsoft.com/en-us/excel/functions/ceiling-function)
- [Google Docs Editors Help: CEILING](https://support.google.com/docs/answer/3093471)
