---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Parser Functions
purpose:
  - Number Formatting
  - Text Manipulation
use-case:
  - Export Text Columns
  - Invoice Amount Labels
related:
  - DOLLAR
  - TEXT
  - TO_DATE
  - TO_PURE_NUMBER
level: 2
source:
  - https://support.google.com/docs/answer/3094285
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Number To Text
tags:
  - conversion
  - formatting
  - sheets
  - text
---

# TO_TEXT

## Description

**TO_TEXT** converts a number into text. Unlike a plain conversion that drops the display, TO_TEXT keeps the formatting the number already has. A currency such as `1250` formatted as dollars becomes the text `$1,250.00`, a percentage keeps its percent sign, and a date keeps its date appearance. The result is text, so it cannot be used in arithmetic until it is converted back.

Use TO_TEXT when a formatted value must be joined with other text, placed in a column that expects text, or exported to a system that reads the display form. The function gives the same result as typing an apostrophe before a number, but it works inside a formula.

TO_TEXT is different from DOLLAR and TEXT. DOLLAR builds a currency string with its own rules, and TEXT builds a string from a pattern you write. TO_TEXT reuses the format the cell already has. If the input is not numeric, TO_TEXT returns it unchanged.

## Syntax

```excel
=TO_TEXT(value)
```

<!-- Image 1: Number Versus Text Result. See Images/Google-specific/TO_TEXT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The number, or a reference to a cell that holds a number, to convert to text. The cell's existing format is kept in the text. Non-numeric input is returned unchanged. |

### Return Value

A text string that shows the number as it is formatted in the cell. A currency returns text with the dollar sign and separators, a percentage returns text with the percent sign, and a date returns text in its date form. If the input is not numeric, the function returns the input unchanged. The official documentation does not list error values or other limits for TO_TEXT.

## Examples

Each example is a separate formula. The cell formats are noted where they matter.

### Example 1: Plain Number

```excel
=TO_TEXT(24)
```

**Result:** `24` (text, aligned to the left of the cell by default)

The number becomes a text string, and a formula that treats it as a number needs a conversion back.

### Example 2: Currency Cell

```excel
=TO_TEXT(A2)
```

**Result:** `$1,250.00` when `A2` holds `1250` with the Currency format

The text keeps the dollar sign, the separator and the two decimal places.

### Example 3: Percentage Cell

```excel
=TO_TEXT(B2)
```

**Result:** `25%` when `B2` holds `0.25` with the Percent format

The percent sign is part of the text, so the label reads the way the cell does.

### Example 4: Length of the Text

```excel
=LEN(TO_TEXT(A2))
```

**Result:** `9` when `A2` holds `1250` with the Currency format

The text `$1,250.00` has nine characters, including the symbol, the comma, the period and the zeros.

<!-- Image 3: Percentage Label Beside a Dashboard Title. See Images/Google-specific/TO_TEXT.md -->

### Example 5: Text Input Returned Unchanged

```excel
=TO_TEXT("Pending")
```

**Result:** `Pending`

Text passes through without an error, so a column of mixed values stays readable.

## Story Problems

### Problem 1: Invoice Text Length

An accounting export needs each invoice amount as text, and the field has a limit of 9 characters. The amount in `B2` is formatted as currency and holds the value 1250.

| Invoice | Amount |
| --- | --- |
| INV-2041 | 1250 |

**Task:** Convert the amount to text in `C2`, and count its characters in `D2` to confirm it fits the limit.

**Solution:**

```excel
=TO_TEXT(B2)
=LEN(C2)
```

**Answer:** `$1,250.00` in `C2`, and `9` in `D2`. The amount fits the 9-character limit exactly.

<!-- Image 2: Currency Text in an Export Column. See Images/Google-specific/TO_TEXT.md -->

### Problem 2: Growth Label on a Dashboard

A dashboard shows the growth rate in `B2` as a percentage. The title cell needs to read as a sentence, so the rate must be joined with the words that come before it.

**Task:** Build a label in `C2` that reads `Growth: ` followed by the rate, where `B2` holds `0.25` with the Percent format.

**Solution:**

```excel
="Growth: "&TO_TEXT(B2)
```

**Answer:** `Growth: 25%`, with the percent sign kept from the cell's format.

## Use Cases

### Export Text Columns

**Scenario:** A finance team exports a sheet to a system that only accepts text fields, and the amounts must keep their currency display.

```excel
=TO_TEXT(F2)
```

**Why It Works:** The export receives the same display the team sees in the sheet, and the original numbers remain in their own column for calculations.

### Invoice Amount Labels

**Scenario:** A billing template writes a line in each invoice reading `Amount due: ` followed by the formatted total.

```excel
="Amount due: "&TO_TEXT(G2)
```

**Why It Works:** TO_TEXT keeps the currency display, so the label reads the same way as the amount in the table above it.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result cannot be added | The output is text, not a number. | Convert the text back with VALUE, or add the original cell instead. |
| Text looks different from the cell | The text uses the cell's format, and a different cell format changes the result. | Format the source cell first, then apply TO_TEXT. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use TEXT with a format pattern such as `"$#,##0.00"` to produce a formatted string. |
| Google Sheets | Available | Keeps the existing cell formatting in the returned text. |

## Tips and Best Practices

- Format the source cell before converting it, because TO_TEXT keeps whatever format the cell has.
- Use TEXT when you need to write the format yourself, and TO_TEXT when the cell's format is the one you want.
- Convert back with VALUE or TO_PURE_NUMBER before doing arithmetic on text output.
- Use LEN on the result to check that an exported value fits a field limit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DOLLAR](../Text/DOLLAR.md) | Builds a currency string with its own rules, rather than the cell's format. |
| [TEXT](../Text/TEXT.md) | Formats a number as text with a pattern you write. |
| [TO_DATE](TO_DATE.md) | Converts a number to a date, the reverse of showing a date as a serial number. |
| [TO_PURE_NUMBER](TO_PURE_NUMBER.md) | Returns the plain number from a formatted value, the reverse of TO_TEXT. |

## Official Documentation

- [Google Docs Editors Help: TO_TEXT](https://support.google.com/docs/answer/3094285)
