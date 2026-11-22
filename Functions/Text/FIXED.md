---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Number Formatting
use-case:
  - Budget Summaries
  - CSV Export Preparation
  - Report Labels
related:
  - DOLLAR
  - NUMBERVALUE
  - ROUND
  - TEXT
  - VALUE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/fixed-function
  - https://support.google.com/docs/answer/3094075
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Fixed Decimal Text
  - Number As Text
tags:
  - excel
  - formatting
  - number-text
  - rounding
  - sheets
---

# FIXED

## Description

**FIXED** rounds a number to a set number of decimal places and returns the result as text, with thousands separators unless you turn them off. For example, `FIXED(1234.567, 1)` returns `"1,234.6"`. Use it when a number must be shown in a sentence, a label or a text export with a consistent number of decimals.

FIXED always returns text, so the result cannot be added, averaged or compared as a number. Functions such as SUM and AVERAGE ignore text values. When the value must stay numeric, round it with ROUND and apply a number format to the cell.

FIXED adds a thousands separator by default, and the separator symbol follows the locale. Set the third argument to TRUE in Excel, or to 1 in Google Sheets, when the text must contain digits only, such as a value in a comma-separated file.

FIXED differs from DOLLAR in that it never adds a currency symbol. Use TEXT when you need a custom format code.

## Syntax

```excel
=FIXED(number, [decimals], [no_commas])
```

<!-- Image 1: FIXED Arguments and Output. See Images/Text/FIXED.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The number to round and convert to text. A cell reference or a formula that returns a number works. |
| `decimals` | No | The number of digits to show to the right of the decimal point. Defaults to 2 in Excel. A negative value rounds to the left of the decimal point, so `-1` rounds to tens. In Google Sheets this argument is named `number_of_places`. |
| `no_commas` | No | `TRUE` removes the thousands separators. `FALSE` or omitted keeps them. In Google Sheets this argument is named `suppress_separator`, where any value other than 0 removes the separators. |

### Return Value

A text string with the rounded number, the requested decimal places and, unless suppressed, thousands separators. The function returns `#VALUE!` when `number` cannot be read as a number.

## Examples

### Example 1: Default Formatting

```excel
=FIXED(1234.567)
```

**Result:** `"1,234.57"`

With no optional arguments, the function rounds to two decimal places and keeps the thousands separator.

### Example 2: One Decimal Place

```excel
=FIXED(1234.567, 1)
```

**Result:** `"1,234.6"`

The value is rounded to one decimal place, and the separator stays in place.

### Example 3: Rounding to Tens

```excel
=FIXED(1234.567, -1)
```

**Result:** `"1,230"`

A negative `decimals` value rounds to the left of the decimal point. The number has no decimal places in the result.

### Example 4: Digits Only for an Export

```excel
=FIXED(-1234.567, -1, TRUE)
```

**Result:** `"-1230"`

Setting `no_commas` to TRUE removes the thousands separator, which is useful for files that use commas as field separators.

### Example 5: Default Decimals on a Small Value

```excel
=FIXED(44.332)
```

**Result:** `"44.33"`

The value rounds to two decimal places, the default in Excel.

## Story Problems

### Problem 1: Annual Sales Line in a Report

A regional manager writes a sentence for a board report. The total sales figure is 48,213.456 in A2, and the sentence should show whole units.

| Line | Value |
| --- | --- |
| Total sales | 48213.456 |

**Task:** Write the total as text with no decimal places and thousands separators.

**Solution:**

```excel
="Total sales were "&FIXED(A2, 0)&" units."
```

**Answer:** `"Total sales were 48,213 units."` FIXED rounds 48,213.456 to 48,213 and keeps the separator.

<!-- Image 2: Sales Sentence Built With FIXED. See Images/Text/FIXED.md -->

### Problem 2: Preparing a Value for a Comma-Separated File

A data export needs the reading 1234.5 as plain digits in one field. A comma inside the field would split it into two columns.

| Field | Value |
| --- | --- |
| Meter reading | 1234.5 |

**Task:** Write the reading as text with one decimal place and no thousands separator.

**Solution:**

```excel
=FIXED(A2, 1, TRUE)
```

**Answer:** `"1234.5"`. The value keeps one decimal place, and the TRUE argument removes the separator that would otherwise appear.

## Use Cases

### Budget Summaries

**Scenario:** A department writes a monthly summary that states each total in words and figures.

```excel
="Spent so far: "&FIXED(B2, 0)&" of "&FIXED(C2, 0)&" budgeted."
```

**Why It Works:** FIXED turns each total into a whole-number string with separators. The numeric cells in B2 and C2 remain unchanged for other calculations.

### CSV Export Preparation

**Scenario:** A team exports a product list to a system that expects plain numbers with a fixed number of decimals.

```excel
=FIXED(D2, 2, TRUE)
```

**Why It Works:** The TRUE argument removes separators, so each value is one field. Every row keeps exactly two decimal places, so the column looks uniform in the file.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The `number` argument is text that cannot be read as a number. | Clean the source with VALUE or NUMBERVALUE, or correct the entry. |
| Total is missing from a sum | The FIXED result is text, and SUM ignores it. | Sum the numeric cells, then format the total with FIXED. |
| Separator breaks a CSV export | Thousands separators were left in the text. | Set `no_commas` to TRUE or to 1 in Google Sheets. |
| Rounding looks wrong | Excel keeps at most 15 significant digits of a number. | Round the value with ROUND before formatting. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions. | Defaults to 2 decimal places. `decimals` can be as large as 127, but the value keeps at most 15 significant digits. |
| Google Sheets | Available. | Arguments are named `number_of_places` and `suppress_separator`. Any value other than 0 for `suppress_separator` removes the separators. |

## Tips and Best Practices

- Use FIXED only for display text. Keep the original number in its cell for calculations.
- Round with ROUND first when the rounding rule affects other totals.
- Set `no_commas` for exports and identifiers that must not contain commas.
- Use DOLLAR when the text should include a currency symbol.
- Check the decimal and separator symbols in the target locale before sharing a file.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DOLLAR](DOLLAR.md) | Formats a number as currency text with a currency symbol. |
| [TEXT](TEXT.md) | Formats a number with any custom format code. |
| [ROUND](../Math%20%26%20Trig/ROUND.md) | Rounds a number and keeps it numeric. |
| [NUMBERVALUE](NUMBERVALUE.md) | Converts locale-independent text back to a number. |
| [VALUE](VALUE.md) | Converts text that holds a number back to a number. |

## Official Documentation

- [Microsoft Support: FIXED function](https://support.microsoft.com/en-us/excel/functions/fixed-function)
- [Google Docs Editors Help: FIXED](https://support.google.com/docs/answer/3094075)
