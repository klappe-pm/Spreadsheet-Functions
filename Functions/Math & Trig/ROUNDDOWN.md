---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Number Formatting
  - Rounding
use-case:
  - Complete Hours Worked
  - Conservative Revenue Reporting
  - Full Containers Filled
related:
  - FLOOR
  - INT
  - MOD
  - ROUND
  - ROUNDUP
  - TRUNC
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/rounddown-function
  - https://support.google.com/docs/answer/3093442
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Round Down
  - Round Toward Zero
  - Truncate Decimal
tags:
  - excel
  - precision
  - rounding
  - sheets
  - truncation
---

# ROUNDDOWN

## Description

**ROUNDDOWN** rounds a number toward zero to a set number of decimal places. Unlike ROUND, which moves to the nearest value, ROUNDDOWN drops the extra digits and always moves the result toward zero, whatever the digit being dropped. A positive number gets smaller, and a negative number gets closer to zero. For example, ROUNDDOWN(2.9, 0) returns 2, not 3.

Use ROUNDDOWN when only complete amounts should count, such as whole hours worked, full boxes packed, or revenue that has reached a reporting threshold. It keeps a partial unit from being counted before it is finished.

The num_digits argument also accepts negative values to round to tens, hundreds, or thousands. ROUNDDOWN is not the same as INT. INT rounds toward negative infinity, so INT(-2.9) returns -3, while ROUNDDOWN(-2.9, 0) returns -2.

Microsoft Excel and Google Sheets calculate ROUNDDOWN the same way. The Excel documentation lists both arguments as required, while Google Sheets makes the second argument, named places, optional with a default of 0.

## Syntax

```excel
=ROUNDDOWN(number, num_digits)
```

<!-- Image 1: Rounding Argument Anatomy. See Images/Math & Trig/ROUNDDOWN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The numeric value to round down. Positive values get smaller, and negative values move closer to zero. |
| `num_digits` | Yes | The digit position to round to. Positive values set decimal places (2 means hundredths), 0 rounds to a whole number, and negative values round to tens (-1), hundreds (-2), thousands (-3), and so on. |

### Return Value

Returns a number rounded toward zero to the requested digit position. For a positive input the result is less than or equal to the input. For a negative input the result is greater than or equal to the input. The function returns #VALUE! when an argument is text that cannot be read as a number.

## Examples

### Example 1: Round Down to a Whole Number

```excel
=ROUNDDOWN(2.9, 0)
```

**Result:** 2

The value 2.9 is closer to 3, but ROUNDDOWN always moves toward zero. The decimal part is discarded, which returns only the amount that is fully complete.

### Example 2: Round Down to Two Decimal Places

```excel
=ROUNDDOWN(3.14959, 2)
```

**Result:** 3.14

The digits after the second decimal place are dropped without being considered for rounding. The third decimal place does not push the result up.

<!-- Image 2: Rounding Direction Comparison. See Images/Math & Trig/ROUNDDOWN.md -->

### Example 3: Negative Numbers Move Toward Zero

```excel
=ROUNDDOWN(-2.9, 0)
```

**Result:** -2

For negative numbers, toward zero means less negative. The result is -2, not -3. This is the main difference between ROUNDDOWN and INT.

### Example 4: Round Down to the Nearest Hundred

```excel
=ROUNDDOWN(-1850, -2)
```

**Result:** -1800

With num_digits set to -2, the value rounds to hundreds. The negative value moves toward zero, so -1850 becomes -1800 rather than -1900.

### Example 5: Round Down a Percentage to One Decimal Place

```excel
=ROUNDDOWN(47.86, 1)
```

**Result:** 47.8

The second decimal (6) is dropped, and the first decimal stays at 8. The result is never rounded up, even though 47.86 is closer to 47.9.

## Story Problems

### Problem 1: Full Drums From Batch Volumes

A small brewery bottles four batches of cider in a single week. Each full drum holds 250 liters, and the brewery ships only full drums. Each batch is counted on its own, so a batch that fills part of a drum does not contribute to the total.

| Batch | Liters Bottled |
| --- | --- |
| B-101 | 1284.6 |
| B-102 | 958.2 |
| B-103 | 1103.95 |
| B-104 | 77.09 |

**Task:** Count the full 250-liter drums that can be filled from the four batches.

**Solution:**

```excel
=SUMPRODUCT(ROUNDDOWN(B2:B5/250, 0))
```

**Answer:** `12`, because the batches fill 5, 3, 4, and 0 full drums (1284.6, 958.2, 1103.95, and 77.09 liters divided by 250). The last batch is too small for a full drum.

### Problem 2: Quarterly Sales Statements

A sales manager reports each rep's quarterly sales rounded down to the nearest 1,000 dollars, so that no figure is overstated. The totals are then added for the department statement.

| Rep | Sales |
| --- | --- |
| Ana Ruiz | 4760 |
| Ben Ortiz | 12340.5 |
| Chen Li | 999.99 |
| Dee Patel | 25000 |

**Task:** Find the department total after each rep's sales is rounded down to the nearest 1,000.

**Solution:**

```excel
=SUMPRODUCT(ROUNDDOWN(B2:B5, -3))
```

**Answer:** `41000`, because the rounded figures are 4,000, 12,000, 0, and 25,000. The 999.99 figure rounds down to 0 rather than 1,000.

## Use Cases

### Complete Hours Worked

**Scenario:** A consultant logs minutes for each client project, and the firm bills only whole hours in the first invoice pass.

```excel
=ROUNDDOWN(B2/60, 0)
```

**Why It Works:** Dividing minutes by 60 gives a decimal number of hours. ROUNDDOWN keeps only the complete hours, so 179 minutes becomes 2 billable hours and the remaining 59 minutes wait for the next period.

### Conservative Revenue Reporting

**Scenario:** A finance team reports a forecast to the nearest thousand dollars without overstating the figure to the board.

```excel
=ROUNDDOWN(B2, -3)
```

**Why It Works:** A negative num_digits value rounds to thousands. A forecast of 4,760,000 reports as 4,760,000, and a forecast of 4,759,999 reports as 4,759,000. Results stay at or below the original figure for positive values.

### Full Containers Filled

**Scenario:** A distributor has 1,750 cartons to load, and each pallet holds 48 cartons. Only complete pallets can leave the warehouse.

```excel
=ROUNDDOWN(B2/B3, 0)
```

**Why It Works:** The division gives 36.46 pallets, and ROUNDDOWN returns 36 complete pallets. The remaining cartons can be counted with MOD, which returns 14 cartons.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text, not a number. | Convert the text with VALUE or correct the source cell. |
| Unexpected total | ROUNDDOWN was used where nearest-value rounding was intended. | Use ROUND when the result should go to the nearest value. |
| Different result from INT | Negative numbers round in different directions. | Use INT when negative values should move away from zero. |
| Missing trailing zeros | ROUNDDOWN removes digits but does not add them. | Apply a number format such as 0.00 to display two decimals. |
| Wrong rounding digit | The sign of num_digits was misread. | Positive values count decimals, and -2 means hundreds. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2024, Excel 2021, Excel 2019, Excel 2016, and Excel for the web | Both arguments are required. Negative num_digits rounds to the left of the decimal point. |
| Google Sheets | Available | The second argument is named places and is optional, defaulting to 0. Behavior matches Excel. |

## Tips and Best Practices

- Use ROUNDDOWN for amounts that must be complete before they count, such as finished units or full hours.
- Pair ROUNDDOWN with ROUNDUP to build a low and high range around the same estimate.
- Use MOD to calculate the leftover amount after ROUNDDOWN, so the two results always add back to the original.
- Use TRUNC(value) when no decimal places are needed. It returns the same result as ROUNDDOWN(value, 0) and is shorter to write.
- Check negative values before relying on the result, because a deduction of -2.50 rounds to -2.00, which may not be the conservative choice.
- Apply number formatting to show trailing zeros, since ROUNDDOWN does not add them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FLOOR](FLOOR.md) | Rounds down to a multiple of a chosen significance, such as 0.25 or 5. |
| [INT](INT.md) | Rounds down toward negative infinity. Matches ROUNDDOWN for positive numbers only. |
| [MOD](MOD.md) | Returns the remainder left after a division, which is the partial unit ROUNDDOWN discards. |
| [ROUND](ROUND.md) | Rounds to the nearest value instead of toward zero. |
| [ROUNDUP](ROUNDUP.md) | Rounds away from zero, the opposite direction. |
| [TRUNC](TRUNC.md) | Removes digits toward zero and is simpler when no precision is needed. |

## Official Documentation

- [Microsoft Support: ROUNDDOWN function](https://support.microsoft.com/en-us/excel/functions/rounddown-function)
- [Google Docs Editors Help: ROUNDDOWN](https://support.google.com/docs/answer/3093442)
