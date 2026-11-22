---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Parser Functions
purpose:
  - Financial Modeling
  - Number Formatting
use-case:
  - Commission Rate Display
  - Discount Rate Display
related:
  - TEXT
  - TO_DOLLARS
  - TO_PURE_NUMBER
  - UNARY_PERCENT
level: 2
source:
  - https://support.google.com/docs/answer/3094284
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Number To Percent
tags:
  - conversion
  - formatting
  - percentages
  - sheets
---

# TO_PERCENT

## Description

**TO_PERCENT** shows a number as a percentage. It follows the convention that 1 equals 100 percent, so the value `0.25` displays as `25%`. The function applies the Percent number format to the cell, and the stored value stays the same decimal number.

Use TO_PERCENT when a column of rates should read as percentages but the formulas behind it need the decimal form. A commission of 0.08 multiplied by a sale amount still gives the right commission, and the cell shows 8%. The function is the formula version of choosing Format, then Number, then Percent from the menu.

TO_PERCENT does not divide or multiply the value. It changes only the display. If you have a number such as 25 that means 25 percent, use UNARY_PERCENT to interpret it as a percentage, because `UNARY_PERCENT(100)` returns 1. TO_PERCENT is roughly the inverse of UNARY_PERCENT. Non-numeric input is returned unchanged.

## Syntax

```excel
=TO_PERCENT(value)
```

<!-- Image 1: Decimal Value Versus Percent Display. See Images/Google-specific/TO_PERCENT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The number, or a reference to a cell that holds a number, to show as a percentage. A value of 1 displays as 100%. Non-numeric input is returned unchanged. |

### Return Value

A number with the Percent format applied. The value stays numeric and keeps its decimal form, so 0.25 is still 0.25 in the cell. If the input is not numeric, the function returns it unchanged. The official documentation does not list error values or other limits for TO_PERCENT.

## Examples

Each example is a separate formula. The results show the displayed value, and the stored value is the decimal in the input.

### Example 1: Rate From a Cell

```excel
=TO_PERCENT(A2)
```

**Result:** `25%` when `A2` holds `0.25`

The cell shows the rate as a percentage, and `A2` still holds the decimal form.

### Example 2: Typed Decimal

```excel
=TO_PERCENT(0.4)
```

**Result:** `40%`

A typed decimal works the same way as a cell reference.

### Example 3: Whole Number Input

```excel
=TO_PERCENT(1)
```

**Result:** `100%`

The value 1 represents the whole, so it displays as 100 percent.

### Example 4: Rate Used in a Calculation

```excel
=TO_PERCENT(B2)*C2
```

**Result:** `8%` for the rate, and `120` when `B2` holds `0.08` and `C2` holds `1500`

The cell with the formula shows the rate as a percentage. The multiplication uses the decimal value in `B2`, so the commission on 1500 is 120.

<!-- Image 2: Rate Display Beside a Calculation. See Images/Google-specific/TO_PERCENT.md -->

### Example 5: Text Input Returned Unchanged

```excel
=TO_PERCENT("n/a")
```

**Result:** `n/a`

A placeholder passes through unchanged, so a table can show "n/a" where a rate is not set.

## Story Problems

### Problem 1: Sales Commission Rates

A sales team has commission rates stored as decimals in `B2:B4`. The manager wants the rates to display as percentages on the report.

| Rep | Rate | Sales |
| --- | --- | --- |
| Avery | 0.08 | 4200 |
| Blake | 0.15 | 2600 |
| Casey | 0.1 | 3100 |

**Task:** Show Avery's rate in `D2` as a percentage, then calculate Blake's commission in `D3` using the decimal rate and the sales amount.

**Solution:**

```excel
=TO_PERCENT(B2)
=B3*C3
```

**Answer:** `D2` displays `8%`. Blake's commission is `390`, because 0.15 multiplied by 2600 is 390.

<!-- Image 3: Commission Report Result. See Images/Google-specific/TO_PERCENT.md -->

### Problem 2: Discount Display

A store lists discounts as decimals in `B2:B3`: 0.2 for a summer sale and 0.15 for a clearance rack. The price sheet must show the discounts as percentages.

**Task:** Display both discounts as percentages in `C2` and `C3`.

**Solution:**

```excel
=TO_PERCENT(B2)
=TO_PERCENT(B3)
```

**Answer:** `20%` and `15%`, shown from the stored decimals 0.2 and 0.15.

## Use Cases

### Commission Rate Display

**Scenario:** A payroll sheet stores each rep's commission rate as a decimal, but managers read the report and expect percentages.

```excel
=TO_PERCENT(D2)
```

**Why It Works:** The cell reads as a percentage, and the commission formulas that multiply by the stored decimal still produce the correct amounts.

### Discount Rate Display

**Scenario:** A price sheet lists discount rates that come from a supplier file, which stores them as decimals.

```excel
=TO_PERCENT(E2)
```

**Why It Works:** TO_PERCENT changes the display only, so the discounted price formula that uses the same cell continues to work.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Rate shows 2500% | The input is 25 instead of 0.25, so the percent display multiplies it by 100. | Enter the rate as a decimal, or use UNARY_PERCENT on the number 25. |
| Value stays text | The input is text such as `"25%"`, which is returned unchanged. | Convert the text to a number first, for example with VALUE. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Apply the Percent format from Format Cells, or enter the value with a percent sign. |
| Google Sheets | Available | Applies the Percent format to a number and keeps the value numeric. |

## Tips and Best Practices

- Store rates as decimals and display them with TO_PERCENT, so formulas multiply by the same value that the report shows.
- Use UNARY_PERCENT when a source file writes rates as whole numbers such as 25, because it converts them to decimals.
- Check the number of decimal places in the cell format, since the display can round a rate you expected to see with a fraction.
- Keep a rate cell's format consistent across a column, so a total row reads the same way as the rows above it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TEXT](../Text/TEXT.md) | Formats a number as text with a pattern such as `0.0%`. |
| [TO_DOLLARS](TO_DOLLARS.md) | Applies the Currency format to a number. |
| [TO_PURE_NUMBER](TO_PURE_NUMBER.md) | Removes the percent display and returns the plain decimal. |
| [UNARY_PERCENT](UNARY_PERCENT.md) | Interprets a value as a percentage, so 100 becomes 1. |

## Official Documentation

- [Google Docs Editors Help: TO_PERCENT](https://support.google.com/docs/answer/3094284)
