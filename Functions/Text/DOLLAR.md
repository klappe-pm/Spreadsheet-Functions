---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Number Formatting
use-case:
  - Budget Summaries
  - Invoice Memos
  - Report Labels
related:
  - FIXED
  - NUMBERVALUE
  - ROUND
  - TEXT
  - VALUE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/dollar-function
  - https://support.google.com/docs/answer/3094071
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Currency Text
  - Dollar Format
tags:
  - currency
  - excel
  - formatting
  - sheets
  - text-conversion
---

# DOLLAR

## Description

**DOLLAR** converts a number into text formatted as currency. The result includes the currency symbol, thousands separators and a fixed number of decimal places, for example `$1,234.57`. Use it when a number must appear inside a sentence, a label or a memo, such as `"Amount due: " & DOLLAR(C2)`.

DOLLAR always returns text, not a number. A cell that holds the result cannot be added, averaged or compared as a value, and functions such as SUM and AVERAGE ignore it. When the value must stay numeric, keep the original number and apply a currency format from the Format Cells dialog (Ctrl+1 in Excel) or from the Format menu in Google Sheets.

The currency symbol and grouping style follow the language settings in Excel and the locale of the spreadsheet in Google Sheets. A workbook shared with users in another region can therefore show a different symbol even though the formula is identical.

DOLLAR differs from FIXED in one way: FIXED formats the number with separators and decimals but never adds a currency symbol. Use TEXT when you need a custom format code such as `$#,##0.00` or a date pattern.

## Syntax

```excel
=DOLLAR(number, [decimals])
```

<!-- Image 1: DOLLAR Syntax and Arguments. See Images/Text/DOLLAR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to format: a number, a cell reference to a number, or a formula that returns a number. A number stored as text is converted if it can be read as a number. |
| `decimals` | No | The number of digits to show to the right of the decimal point. Defaults to 2 when omitted. A negative value rounds to the left of the decimal point, so `-2` rounds to hundreds. In Google Sheets this argument is named `number_of_places`. |

### Return Value

A text string in currency format, rounded to the requested decimal places, such as `"$1,234.57"`. The function returns an error when `number` cannot be read as a number, usually `#VALUE!`.

## Examples

### Example 1: Basic Currency Text

```excel
=DOLLAR(1234.567)
```

**Result:** `"$1,234.57"`

With no second argument the function rounds to two decimal places and adds thousands separators.

### Example 2: Rounding to Hundreds

```excel
=DOLLAR(1234.567, -2)
```

**Result:** `"$1,200"`

A negative `decimals` value rounds the number to the left of the decimal point. Here 1,234.567 rounds to the nearest hundred, which gives 1,200, and the result has no decimal places.

### Example 3: Zero Decimal Places

```excel
=DOLLAR(48.6, 0)
```

**Result:** `"$49"`

Setting `decimals` to 0 rounds to a whole dollar. The value 48.6 rounds up to 49 because the digit after the decimal point is 6.

### Example 4: Text Built From a Sentence

```excel
="Amount due: "&DOLLAR(C2)
```

Where C2 contains 99.5

**Result:** `"Amount due: $99.50"`

The ampersand joins the label and the currency text. The value in C2 is unchanged and can still be used in calculations.

### Example 5: Summing Before Formatting

```excel
=DOLLAR(SUM(B2:B5))
```

Where B2:B5 contain 40, 12.5, 7.25 and 100

**Result:** `"$159.75"`

Add the numbers first, then format the total. Formatting each value and adding the text results would fail, because SUM ignores text.

## Story Problems

### Problem 1: Expense Report Total

An employee lists four receipts in B2:B5 of a travel expense sheet. The approval email needs the total written as currency text.

| Receipt | Amount |
| --- | --- |
| Train fare | 214.75 |
| Hotel tax | 38.20 |
| Taxi | 96.50 |
| Meals | 12.99 |

**Task:** Write the total as currency text in B7 so it can be pasted into the email body.

**Solution:**

```excel
=DOLLAR(SUM(B2:B5))
```

**Answer:** `"$362.44"`. The receipts add to 362.44, and DOLLAR formats that total with two decimal places.

<!-- Image 2: Expense Report Total as Currency Text. See Images/Text/DOLLAR.md -->

### Problem 2: Budget Rounded to Thousands

A department head has a yearly budget in A2. The board summary should show the figure rounded to the nearest thousand dollars.

| Line | Value |
| --- | --- |
| Yearly budget | 2456789 |

**Task:** Write a formula in A4 that returns the budget as currency text rounded to thousands.

**Solution:**

```excel
=DOLLAR(A2, -3)
```

**Answer:** `"$2,457,000"`. The value 2,456,789 rounds to 2,457,000 at the thousands position.

## Use Cases

### Invoice Memo Text

**Scenario:** An accounts team writes payment reminders from a template. Each reminder states the balance in the first sentence.

```excel
="Your balance of "&DOLLAR(Invoices[Balance])&" is due on "&TEXT(Invoices[Due Date],"mmmm d")&"."
```

**Why It Works:** DOLLAR turns the balance into a currency string that fits in a sentence. TEXT formats the date in the same way. The balance column stays numeric for reports.

### Budget Summary Rounded to Thousands

**Scenario:** A finance team presents department totals to executives who want to read figures in thousands of dollars without decimals.

```excel
=DOLLAR(B2, -3)
```

**Why It Works:** A negative `decimals` value rounds the figure before it is displayed. The underlying value in B2 is unchanged, so the same cell still feeds totals and variance calculations.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The `number` argument is text that cannot be read as a number, such as `"n/a"`. | Clean the source cell or wrap it in IFERROR. |
| Total is missing from a sum | Adding cells that contain DOLLAR results. SUM ignores text. | Sum the numeric cells first, then wrap the total in DOLLAR. |
| Wrong currency symbol | The workbook or locale uses different currency settings. | Change the language or locale setting, or use a number format instead. |
| Displayed value differs from the sum | Each cell was rounded before adding. | Add the unrounded numbers, then round the total with DOLLAR or ROUND. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions. | The currency symbol follows the language settings. Microsoft recommends a number format when the value must stay numeric. |
| Google Sheets | Available. | The format follows the spreadsheet locale. The default is two decimal places. Sheets also offers a separate function that applies a currency format to a number without converting it to text. |

## Tips and Best Practices

- Keep the numeric value in one cell and place DOLLAR results in a separate report column.
- Use Format Cells or the Format menu for currency display in tables that feed other formulas.
- Round with ROUND before DOLLAR when the rounding rule matters in later calculations.
- Test the output in the target locale before sharing a template across regions.
- Use TEXT with a custom format code when you need a symbol other than the locale currency.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FIXED](FIXED.md) | Formats a number with separators and decimals, without a currency symbol. |
| [TEXT](TEXT.md) | Formats a value with any custom format code, including currency patterns. |
| [ROUND](../Math%20%26%20Trig/ROUND.md) | Rounds a number before it is kept as a value or converted to text. |
| [VALUE](VALUE.md) | Converts text that holds a number back to a number. |
| [NUMBERVALUE](NUMBERVALUE.md) | Converts text to a number with custom separators. |

## Official Documentation

- [Microsoft Support: DOLLAR function](https://support.microsoft.com/en-us/excel/functions/dollar-function)
- [Google Docs Editors Help: DOLLAR](https://support.google.com/docs/answer/3094071)
