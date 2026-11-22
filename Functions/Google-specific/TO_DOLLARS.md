---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Parser Functions
purpose:
  - Financial Modeling
  - Number Formatting
use-case:
  - Invoice Presentation
  - Price List Formatting
related:
  - DOLLAR
  - FIXED
  - TO_PERCENT
  - TO_PURE_NUMBER
level: 2
source:
  - https://support.google.com/docs/answer/3094241
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Number To Dollars
tags:
  - conversion
  - currency
  - formatting
  - sheets
---

# TO_DOLLARS

## Description

**TO_DOLLARS** shows a number as a dollar amount. It applies the Currency number format to the cell, so a value such as `1250` displays as `$1,250.00` in a US English spreadsheet. The stored value stays the same number, so the cell can still be added, multiplied and compared like any other number.

Use TO_DOLLARS when a column of amounts should look like money without changing the numbers behind it. Totals, averages and other formulas keep working because the cell still holds a number. The function is the formula version of choosing Format, then Number, then Currency from the menu.

TO_DOLLARS and DOLLAR both display money, but they work differently. TO_DOLLARS keeps a number and changes only its display. DOLLAR returns text, so the result cannot be used in further arithmetic. The symbol and decimal rules follow the spreadsheet's locale and currency settings. TO_DOLLARS does not convert between currencies. For current exchange rates, use GOOGLEFINANCE.

## Syntax

```excel
=TO_DOLLARS(value)
```

<!-- Image 1: Number Versus Currency Display. See Images/Google-specific/TO_DOLLARS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The number, or a reference to a cell that holds a number, to show as a dollar amount. Non-numeric input is returned unchanged. |

### Return Value

A number with the Currency format applied. The value stays numeric. If the input is not numeric, the function returns the input unchanged instead of an error. The official documentation does not list error values or other limits for TO_DOLLARS.

## Examples

Each example is a separate formula, and the results assume a US English spreadsheet with the dollar as the currency.

### Example 1: Amount From a Cell

```excel
=TO_DOLLARS(A2)
```

**Result:** `$1,250.00` when `A2` holds `1250`

The cell that contains the formula gets the Currency format. `A2` keeps its number, so it still works in totals.

### Example 2: Typed Number

```excel
=TO_DOLLARS(40826.43)
```

**Result:** `$40,826.43`

The thousands separator and the two decimal places come from the Currency format.

### Example 3: Calculated Amount

```excel
=TO_DOLLARS(B2*C2)
```

**Result:** `$102.00` when `B2` holds `12` and `C2` holds `8.5`

The multiplication runs first, and the product is then displayed as money.

<!-- Image 2: Calculated Amount Display. See Images/Google-specific/TO_DOLLARS.md -->

### Example 4: Small Amount

```excel
=TO_DOLLARS(0.5)
```

**Result:** `$0.50`

The value is less than one dollar, and the format still shows two decimal places.

### Example 5: Text Input Returned Unchanged

```excel
=TO_DOLLARS("Call for price")
```

**Result:** `Call for price`

Non-numeric input passes through without an error, so a price list with a placeholder keeps the placeholder.

## Story Problems

### Problem 1: Price List Display

A shop keeps unit prices as plain numbers in `B2:B4`. The owner wants the prices to display as dollars on the printed list, without changing the numbers used in other formulas.

| Item | Unit Price |
| --- | --- |
| Desk lamp | 1250 |
| Notebook | 89.9 |
| Pen set | 4.5 |

**Task:** Apply the dollar display to the price in `B2` and the price in `B3`, then show the amount of the pen set in `B4` with the same display.

**Solution:**

```excel
=TO_DOLLARS(B2)
=TO_DOLLARS(B3)
=TO_DOLLARS(B4)
```

**Answer:** `$1,250.00`, `$89.90` and `$4.50`. The cells still hold 1250, 89.9 and 4.5 as numbers.

<!-- Image 3: Invoice Total Result. See Images/Google-specific/TO_DOLLARS.md -->

### Problem 2: Invoice Total

A consultant bills two line items in `B2:B3`: a workshop at 1250 dollars and a handout at 89.9 dollars. The invoice total must read as a dollar amount.

**Task:** Show the invoice total in `B5` as a dollar amount.

**Solution:**

```excel
=TO_DOLLARS(SUM(B2:B3))
```

**Answer:** `$1,339.90`, because 1250 + 89.9 = 1339.9.

## Use Cases

### Price List Formatting

**Scenario:** A wholesale catalog lists hundreds of unit prices, and the sales team wants them to display as dollars in a shared view.

```excel
=TO_DOLLARS(D2)
```

**Why It Works:** The display follows the Currency format while the numbers stay usable in discount and tax formulas.

### Invoice Presentation

**Scenario:** An invoice generator sums line items and needs the total to show money formatting in a summary cell.

```excel
=TO_DOLLARS(SUM(E2:E20))
```

**Why It Works:** SUM returns a number, and TO_DOLLARS adds the currency display without turning the total into text.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Amount shows no dollar sign | The spreadsheet's locale or currency setting uses a different symbol or format. | Check the spreadsheet locale and currency under File, then Settings. |
| Amount returns text | The formula used DOLLAR, which returns text, instead of TO_DOLLARS. | Use TO_DOLLARS when the result still needs to be a number. |
| Currency is not converted | TO_DOLLARS only changes the display format. | Convert the amount with an exchange rate, for example from GOOGLEFINANCE. |
| Value is a date or percentage | TO_DOLLARS applies the currency format to whatever number it receives. | Confirm the input is an amount before applying the format. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Apply the Currency format from Format Cells. For text output, use the DOLLAR function. |
| Google Sheets | Available | Applies the Currency format to a number and keeps the value numeric. |

## Tips and Best Practices

- Keep amounts as numbers and apply TO_DOLLARS to the result, so totals and comparisons keep working.
- Use DOLLAR only when the result is a label or a report line that will never be used in a calculation.
- Set the spreadsheet's currency before you build price lists, so the symbol matches the audience.
- Round amounts with ROUND before displaying them if the source values have more decimal places than the currency uses.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DOLLAR](../Text/DOLLAR.md) | Converts a number to a currency text string, which cannot be used in arithmetic. |
| [FIXED](../Text/FIXED.md) | Formats a number as text with a fixed number of decimal places. |
| [TO_PERCENT](TO_PERCENT.md) | Applies the Percent format to a number. |
| [TO_PURE_NUMBER](TO_PURE_NUMBER.md) | Removes currency formatting and returns the plain number. |

## Official Documentation

- [Google Docs Editors Help: TO_DOLLARS](https://support.google.com/docs/answer/3094241)
