---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Rounding
purpose:
  - Number Formatting
  - Rounding
use-case:
  - Budget Summaries
  - Invoice Rounding
  - Tax Calculations
related:
  - CEILING
  - FLOOR
  - INT
  - MROUND
  - ROUNDDOWN
  - ROUNDUP
  - TRUNC
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/round-function
  - https://support.google.com/docs/answer/3093440
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Round Decimal
  - Round Number
tags:
  - decimals
  - excel
  - precision
  - rounding
  - sheets
---

# ROUND

## Description

**ROUND** rounds a number to a set number of digits and returns the rounded number. `=ROUND(4.2857,2)` returns 4.29. Unlike formatting, ROUND changes the stored value, so later calculations use the rounded figure. Use ROUND when the rounded value is the value that matters, such as a tax amount on an invoice or a total in a board report.

The `num_digits` argument sets the place of rounding. A positive value rounds to that many decimal places, 0 rounds to the nearest whole number, and a negative value rounds to the left of the decimal point. For example, `=ROUND(1234,-2)` returns 1200, and `=ROUND(78500,-3)` returns 79000. Both Excel and Google Sheets round a digit of 5 or more upward in magnitude, so 2.5 rounds to 3 and -2.5 rounds to -3. Excel's documentation does not state the tie rule in words, but its examples match the same behavior.

ROUND is different from formatting a cell to show fewer decimals. Formatting changes only the display, and every calculation still uses the full value. If you need a rounded figure in a sum or a percentage, wrap the calculation in ROUND. Use ROUNDUP, ROUNDDOWN, CEILING, FLOOR or MROUND when the rule is a specific direction or a specific multiple rather than standard rounding.

## Syntax

```excel
=ROUND(number, num_digits)
```

<!-- Image 1: Digits Argument Positions. See Images/Math & Trig/ROUND.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The number to round. Can be a number, a cell reference or a formula result. |
| `num_digits` | Yes | The number of digits to keep. Positive values set decimal places, 0 gives a whole number, and negative values round to tens, hundreds, thousands and so on. |

### Return Value

A number rounded to the requested place. The result is a numeric value, so it works in further calculations. ROUND returns `#VALUE!` when either argument is text that cannot be read as a number.

<!-- Image 2: Negative Digits to the Left of the Decimal. See Images/Math & Trig/ROUND.md -->

## Examples

### Example 1: Round to Two Decimal Places

```excel
=ROUND(4.2857,2)
```

**Result:** `4.29`

The third decimal digit is 5 or more, so the second decimal place rounds up from 8 to 9.

### Example 2: Round to a Whole Number

```excel
=ROUND(7.8,0)
```

**Result:** `8`

With `num_digits` set to 0, ROUND returns the nearest integer. A value of 7.4 would round down to 7.

### Example 3: Halfway Values Round Away From Zero

```excel
=ROUND(-2.5,0)
```

**Result:** `-3`

A value exactly halfway between two integers rounds away from zero. 2.5 becomes 3, and -2.5 becomes -3.

### Example 4: Round to the Nearest Ten

```excel
=ROUND(1234,-1)
```

**Result:** `1230`

A negative `num_digits` rounds to the left of the decimal point. The digit in the ones place is 4, so the number rounds down to the nearest ten.

### Example 5: Round to the Nearest Thousand

```excel
=ROUND(78500,-3)
```

**Result:** `79000`

The value sits exactly halfway between 78,000 and 79,000. Because halves round away from zero, the result is 79,000.

### Example 6: Negative Value to the Nearest Hundred

```excel
=ROUND(-50.55,-2)
```

**Result:** `-100`

Fifty point five five is closer to 100 than to 0 when rounded to hundreds, and the sign is kept, so the result is -100.

## Story Problems

### Problem 1: Sales Tax on a Three-Item Invoice

A shop prints one sales tax amount for an invoice. The three line items total $771.52, and the tax rate is 8.25 percent. The amount is printed in cents.

| Item | Amount |
| --- | --- |
| Line Item 1 | 486.37 |
| Line Item 2 | 212.05 |
| Line Item 3 | 73.10 |
| Tax Rate | 0.0825 |

**Task:** Calculate the sales tax on the invoice total, rounded to cents.

**Solution:**

```excel
=ROUND(SUM(B2:B4)*B5,2)
```

**Answer:** `63.65`. The total of 771.52 times 0.0825 is 63.6504, which rounds to 63.65.

### Problem 2: Average Survey Score

Three customers rated a service 6, 7 and 9 on a scale of 10. The team reports the average to one decimal place.

| Customer | Score |
| --- | --- |
| A | 6 |
| B | 7 |
| C | 9 |

**Task:** Calculate the average score, rounded to one decimal place.

**Solution:**

```excel
=ROUND(AVERAGE(B2:B4),1)
```

**Answer:** `7.3`. The average is 22 divided by 3, which is 7.3333, and it rounds to 7.3.

## Use Cases

### Financial Reporting and Currency Calculations

**Scenario:** An accounts team calculates discounted line prices and totals that must be exact to the cent.

```excel
=ROUND(ListPrice*(1-DiscountRate),2)
```

**Why It Works:** The discount is applied before rounding, and ROUND is applied once to the final amount. Rounding each step separately can make the total differ by a cent from the invoice.

### Statistical Data Presentation

**Scenario:** A research team reports a mean and a standard deviation with a fixed number of decimal places.

```excel
=ROUND(AVERAGE(B2:B20),1)
```

**Why It Works:** The average keeps full precision in the calculation, and the report shows one decimal place. Round the number that is reported, and do not round the data that feeds the average.

### Budget Summaries

**Scenario:** A department head presents annual spending in thousands for a board summary.

```excel
=ROUND(B2,-3)
```

**Why It Works:** A negative `num_digits` of -3 rounds the amount in `B2` to the nearest thousand. Keep the detailed figures in the operational sheet and use the rounded figure only in the summary.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | One of the arguments is text. | Convert the cell to a number, or check for a number stored as text. |
| Value looks different from the total | The display was formatted to fewer decimals, but the stored value was not rounded. | Wrap the calculation in ROUND if the rounded value is the one that matters. |
| Total is a cent off | Each line was rounded before the total was calculated. | Sum the unrounded values and round the total once, unless the business rule rounds each line. |
| Negative result seems wrong | Halves round away from zero, so -2.5 becomes -3. | This is the expected behavior. Use INT or ROUNDUP if another direction is required. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | Standard rounding. Negative `num_digits` rounds to tens, hundreds and so on. Returns `#VALUE!` for text inputs. |
| Google Sheets | Available | Same two arguments, with `places` as the second name. The official page says a digit of 5 or more rounds the magnitude up, regardless of sign. |

Both platforms use floating-point arithmetic, so a stored value can differ very slightly from the decimal you typed. ROUND hides that difference in the displayed result.

## Tips and Best Practices

- Round final results, not intermediate steps, so that errors do not accumulate.
- Use formatting for display and ROUND for values that must change.
- Use a negative `num_digits` for thousands and millions in summaries.
- Use ROUNDUP for quantities that must cover a need, such as stock orders, and ROUNDDOWN for completed units.
- Use MROUND when the rounding multiple is not a power of ten, such as quarters or fives.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CEILING](CEILING.md) | Rounds up to the nearest multiple of a chosen value. |
| [FLOOR](FLOOR.md) | Rounds down to the nearest multiple of a chosen value. |
| [INT](INT.md) | Rounds down to the nearest integer, toward negative infinity. |
| [MROUND](MROUND.md) | Rounds to the nearest multiple you specify, such as 0.25. |
| [ROUNDDOWN](ROUNDDOWN.md) | Always rounds toward zero to a set number of digits. |
| [ROUNDUP](ROUNDUP.md) | Always rounds away from zero to a set number of digits. |
| [TRUNC](TRUNC.md) | Removes the decimal part without rounding. |

## Official Documentation

- [Microsoft Support: ROUND function](https://support.microsoft.com/en-us/excel/functions/round-function)
- [Google Docs Editors Help: ROUND](https://support.google.com/docs/answer/3093440)
