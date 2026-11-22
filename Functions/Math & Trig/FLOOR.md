---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Legacy Compatibility
purpose:
  - Rounding
use-case:
  - Full Case Packing
  - Lot Size Rounding
related:
  - CEILING
  - FLOOR.MATH
  - FLOOR.PRECISE
  - INT
  - MROUND
  - ROUNDDOWN
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/floor-function
  - https://support.google.com/docs/answer/3093487
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Round Down to Multiple
tags:
  - compatibility
  - excel
  - rounding
  - sheets
---

# FLOOR

## Description

**FLOOR** rounds a number down to the nearest multiple of a significance value. For example, FLOOR(47,5) returns 45, the largest multiple of 5 that does not exceed 47. Excel lists FLOOR in its Compatibility category, so it is kept mainly for older workbooks.

For new Excel workbooks, use FLOOR.MATH or FLOOR.PRECISE. Both are documented as related functions, and each gives explicit rules for negative numbers: FLOOR.MATH uses a mode argument, and FLOOR.PRECISE rounds down whatever the sign of the number.

Excel requires the significance argument. A positive number with a negative significance returns `#NUM!`. Google Sheets also provides FLOOR, but its factor argument is optional, defaults to 1, and cannot be 0.

## Syntax

```excel
=FLOOR(number, significance)
```

<!-- Image 1: Number and Significance Arguments. See Images/Math & Trig/FLOOR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to round down. |
| `significance` | Yes | The multiple to round to, such as `5` for multiples of 5 or `0.25` for quarter units. In Sheets, this argument is named `factor` and is optional, with a default of 1. A positive number with a negative significance returns `#NUM!` in Excel. |

### Return Value

A number: `number` rounded down to the nearest multiple of `significance`. Non-numeric arguments return `#VALUE!`.

## Examples

### Example 1: Whole Number Multiple

```excel
=FLOOR(47,5)
```

**Result:** `45`

The calculation divides 47 by 5 to get 9.4, drops the fraction to get 9, and multiplies by 5.

### Example 2: Decimal Multiple

```excel
=FLOOR(3.9,0.25)
```

**Result:** `3.75`

The value 3.9 divided by 0.25 is 15.6. The fraction is dropped, leaving 15, and 15 × 0.25 is 3.75.

<!-- Image 2: Rounding Down to a Multiple on a Number Line. See Images/Math & Trig/FLOOR.md -->

### Example 3: Small Significance

```excel
=FLOOR(0.234,0.01)
```

**Result:** `0.23`

The value 0.234 divided by 0.01 is 23.4, which rounds down to 23. Multiplying 23 by 0.01 gives 0.23.

### Example 4: Mixed Signs Return an Error

```excel
=FLOOR(2.5,-2)
```

**Result:** `#NUM!`

Excel rejects a positive number with a negative significance. Use a positive significance instead, or use FLOOR.PRECISE, which ignores the sign of its significance.

## Story Problems

### Problem 1: Full Cases of Bottles

A drinks distributor ships only complete cases of 12 bottles. Three orders arrive in `A1:B4`.

| Order | Bottles Ordered |
| --- | --- |
| Order A | 150 |
| Order B | 95 |
| Order C | 240 |

**Task:** Round each order down to a multiple of 12, then total the bottles that can ship as full cases.

**Solution:**

```excel
=SUMPRODUCT(FLOOR(B2:B4,12))
```

**Answer:** `468`. Order A ships 144 bottles (12 cases), Order B ships 84 (7 cases), and Order C ships 240 (20 cases). The total is 144 + 84 + 240 = 468.

### Problem 2: Cash Prices Rounded Down to Five Cents

A café rounds each menu price down to the nearest 0.05 so that its cash drawer handles only nickels.

| Item | Price |
| --- | --- |
| Muffin | 4.37 |
| Juice | 12.99 |
| Bagel | 7.02 |

**Task:** Round each price down to the nearest 0.05 and total the rounded prices.

**Solution:**

```excel
=SUMPRODUCT(FLOOR(B2:B4,0.05))
```

**Answer:** `24.30`. The rounded prices are 4.35, 12.95 and 7.00, which total 24.30.

## Use Cases

### Full Case Packing

**Scenario:** A warehouse accepts only complete cases of 12 units, so each order must be trimmed to a full-case quantity before it is released.

```excel
=FLOOR(B2,12)
```

**Why It Works:** The formula returns the largest multiple of 12 that does not exceed the order quantity. The leftover units stay in inventory rather than being shipped as a partial case.

### Lot Size Rounding

**Scenario:** A fabric supplier sells cloth only in lots of 25 meters, so a buyer's requested length must be reduced to the nearest full lot below it.

```excel
=FLOOR(B2,25)
```

**Why It Works:** A quantity of 130 meters becomes 125 meters, the nearest full lot below it. Check the source quantity is positive, because negative quantities need different rounding rules.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text rather than a number. | Convert the value to a number or correct the cell reference. |
| `#NUM!` | A positive number has a negative significance. | Use a positive significance, or use FLOOR.PRECISE. |
| Unexpected result | A value such as 0.1 is stored in binary, so an exact multiple can fall just below it and round down a step. | Round the value to the needed decimals with ROUND before calling FLOOR. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Listed in the Compatibility category. Significance is required. |
| Google Sheets | Available | The argument is named `factor` and is optional with a default of 1. A factor of 0 is not allowed. |

## Tips and Best Practices

- Use FLOOR.MATH or FLOOR.PRECISE in new Excel workbooks that handle negative numbers.
- Keep the significance in an input cell so the rounding step is visible and easy to change.
- Wrap a range in SUMPRODUCT when you need to round every value and total the results.
- Round to the needed decimals first when a value sits exactly on a multiple.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CEILING](CEILING.md) | Rounds up to a multiple, the opposite direction. |
| [FLOOR.MATH](FLOOR.MATH.md) | Newer rounding function with a mode argument for negative numbers. |
| [FLOOR.PRECISE](FLOOR.PRECISE.md) | Newer rounding function that always rounds down, whatever the sign. |
| [INT](INT.md) | Rounds down to a whole number with no significance argument. |
| [MROUND](MROUND.md) | Rounds to the nearest multiple rather than always down. |
| [ROUNDDOWN](ROUNDDOWN.md) | Rounds toward zero to a set number of decimal places. |

## Official Documentation

- [Microsoft Support: FLOOR function](https://support.microsoft.com/en-us/excel/functions/floor-function)
- [Google Docs Editors Help: FLOOR](https://support.google.com/docs/answer/3093487)
