---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - European Invoice Totals
  - Percent Text Import
  - Survey Response Cleanup
related:
  - FIXED
  - SUBSTITUTE
  - TEXT
  - TRIM
  - VALUE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/numbervalue-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Locale Independent Number
  - Text To Number
tags:
  - data-cleaning
  - excel
  - locale
  - text-conversion
---

# NUMBERVALUE

## Description

**NUMBERVALUE** converts text to a number in a way that does not depend on the regional settings of the computer. You tell it which character is the decimal separator and which is the group (thousands) separator, so the same text always gives the same number, whether the workbook is opened in the United States, Germany or France.

Use NUMBERVALUE when imported text uses separators that differ from your locale, such as `1.250,40` from a European supplier, or when text contains spaces inside a number or a trailing percent sign. VALUE converts text too, but it follows the locale of the machine, so the same formula can give a different result on another computer.

If you leave out both separator arguments, NUMBERVALUE uses the separators of the current locale. Set them explicitly whenever the data came from another system, so the result does not change when the file is opened elsewhere.

## Syntax

```excel
=NUMBERVALUE(text, [decimal_separator], [group_separator])
```

<!-- Image 1: NUMBERVALUE Separator Arguments. See Images/Text/NUMBERVALUE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to convert. An empty string returns 0. |
| `decimal_separator` | No | The character that separates the whole part from the fractional part. If omitted, the locale's decimal separator is used. Only the first character is used. |
| `group_separator` | No | The character that separates thousands or other digit groups. If omitted, the locale's group separator is used. Only the first character is used. |

### Return Value

A number. Spaces in the text are ignored wherever they appear. A trailing percent sign divides the number by 100, and each extra percent sign divides it by 100 again. The function returns `#VALUE!` when the text breaks the separator rules described in the Common Errors section.

## Examples

### Example 1: European Thousands and Decimal Separators

```excel
=NUMBERVALUE("3.456,78", ",", ".")
```

**Result:** `3456.78`

The comma is the decimal separator and the period is the group separator. The period appears before the decimal comma, so it is treated as a group separator and ignored.

<!-- Image 2: Reading the Separators in a Number. See Images/Text/NUMBERVALUE.md -->

### Example 2: Spaces Inside a Number

```excel
=NUMBERVALUE("1 234 567", ".", ",")
```

**Result:** `1234567`

Spaces are ignored wherever they appear, so the text reads as one whole number.

### Example 3: Trailing Percent Signs

```excel
=NUMBERVALUE("45%", ".", ",")
```

**Result:** `0.45`

The trailing percent sign divides the value by 100.

### Example 4: Repeated Percent Signs

```excel
=NUMBERVALUE("9%%", ".", ",")
```

**Result:** `0.0009`

Each percent sign divides by 100 again, so `9%%` is 9 divided by 10,000.

### Example 5: Empty Text

```excel
=NUMBERVALUE("", ".", ",")
```

**Result:** `0`

An empty string converts to zero rather than an error.

## Story Problems

### Problem 1: Totaling Supplier Invoices

A supplier in Germany sends invoice totals as text, using a period for thousands and a comma for decimals. The bookkeeper needs the total for the four invoices in `A2:A5`.

| Invoice Total |
| --- |
| 1.250,40 |
| 318,15 |
| 2.004,00 |
| 87,5 |

**Task:** Convert each total with the separators the supplier uses, then add them.

**Solution:**

```excel
=SUMPRODUCT(NUMBERVALUE(A2:A5, ",", "."))
```

**Answer:** `3660.05`, because 1250.40 + 318.15 + 2004.00 + 87.50 = 3660.05. The last total has one decimal place, and NUMBERVALUE reads it as 87.5.

### Problem 2: Averaging Percentage Responses

A survey tool exports the share of respondents who chose each option as text with a percent sign. The analyst needs the average share across the four options in `A2:A5`.

| Share |
| --- |
| 12.5% |
| 8% |
| 15% |
| 3.5% |

**Task:** Convert the four shares to numbers and average them.

**Solution:**

```excel
=AVERAGE(NUMBERVALUE(A2:A5, ".", ","))
```

**Answer:** `0.0975`, which is 9.75% when the cell is formatted as a percentage. The four shares add to 0.39, and 0.39 divided by 4 is 0.0975.

## Use Cases

### European Invoice Totals

**Scenario:** An accounts payable team imports a supplier file where amounts use a period for thousands and a comma for decimals.

```excel
=NUMBERVALUE(B2, ",", ".")
```

**Why It Works:** The explicit separators give the same amount on every computer. VALUE would read `1.250,40` differently on a machine set to the United States locale.

### Percent Text Import

**Scenario:** A reporting tool exports growth rates such as `4.2%` as text, and the dashboard needs numbers it can format.

```excel
=NUMBERVALUE(C2, ".", ",")
```

**Why It Works:** The trailing percent sign is applied during the conversion, so the cell holds 0.042, which the dashboard can format as 4.2%.

### Survey Response Cleanup

**Scenario:** A survey export puts spaces inside numbers, such as `1 250`, to separate thousands.

```excel
=NUMBERVALUE(D2, ".", ",")
```

**Why It Works:** Spaces are ignored, so `1 250` becomes 1250 without a SUBSTITUTE step.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The decimal separator appears more than once. | Check the text for a stray separator, or split the value at the wrong place. |
| `#VALUE!` | A group separator appears after the decimal separator. | Remove the group separator from the decimal part of the text. |
| `#VALUE!` | An argument is invalid. | Check that the separators are single characters and that the text holds a number. |
| Result is 100 times too small or large | The percent sign was not expected or was repeated. | Check whether the source uses a percent sign that is already a fraction. |
| Result differs on another computer | The separators were left out, so the locale decides. | Pass both separator arguments explicitly. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Check the version list on the Microsoft page for older releases. The separator arguments are optional and default to the locale. |
| Google Sheets | Not available | Use SUBSTITUTE to remove the group separator and replace the decimal separator, then VALUE. The result of VALUE depends on the locale of the spreadsheet. |

## Tips and Best Practices

- Pass both separator arguments whenever the source is not in your own locale.
- Trim the text first with TRIM when the export adds padding spaces.
- Check one converted value by hand before you copy the formula down a column.
- Store converted values in a new column, and keep the original text for audit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [VALUE](VALUE.md) | Converts text to a number using the locale settings. |
| [SUBSTITUTE](SUBSTITUTE.md) | Replaces separators before a locale-based conversion, a Sheets workaround. |
| [TEXT](TEXT.md) | Formats a number as text, the reverse direction. |
| [TRIM](TRIM.md) | Removes extra spaces before conversion. |
| [FIXED](FIXED.md) | Formats a number as text with fixed decimal places. |

## Official Documentation

- [Microsoft Support: NUMBERVALUE function](https://support.microsoft.com/en-us/excel/functions/numbervalue-function)
