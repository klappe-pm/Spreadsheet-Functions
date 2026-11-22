---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Number Formatting
  - Text Manipulation
use-case:
  - Dashboard Title Amounts
  - Invoice Number Padding
  - Timesheet Totals
related:
  - CONCATENATE
  - DOLLAR
  - FIXED
  - NUMBERVALUE
  - VALUE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/text-function
  - https://support.google.com/docs/answer/3094139
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Date To Text
  - Format Value
  - Number To Text
tags:
  - date-formatting
  - excel
  - number-formatting
  - sheets
  - text-conversion
---

# TEXT

## Description

**TEXT** converts a number, date or time into a text string that follows a format pattern. The pattern (the format code) controls the decimal places, thousands separators, leading zeros, currency symbols, percent signs, date parts and time parts. The result always looks the way the pattern says, which is the main reason to use it.

Plain concatenation loses that formatting. If A2 holds 48213.5 and you join it to a label with the ampersand, the label shows 48213.5. Wrapping the cell in TEXT with the pattern `$#,##0.00` produces $48,213.50. Dates work the same way: a date is stored as a serial number, so TEXT with `mmmm d, yyyy` is the way to show it as a sentence.

The result is text, not a number. Keep the original value in its own cell for calculations, and use TEXT only where a person reads the result. Format codes also depend on the locale. Separators and the order of date parts can differ between regional settings, so test a pattern on the locale of the people who will read it.

## Syntax

```excel
=TEXT(value, format_text)
```

<!-- Image 1: Syntax Anatomy. See Images/Text/TEXT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The number, date or time to format. It can be a literal number, a cell reference or a formula result. |
| `format_text` | Yes | The format pattern in double quotes, such as `"0.00"` or `"mmm yyyy"`. The pattern cannot contain an asterisk. |

### Return Value

Text. The function returns a string that matches the pattern, so the result cannot be used directly in arithmetic. An invalid pattern returns `#VALUE!`.

## Examples

### Example 1: Currency With Separators

```excel
=TEXT(48213.5,"$#,##0.00")
```

**Result:** `$48,213.50`

The comma adds thousands separators, and the two zeros after the decimal point force two decimal places.

### Example 2: Percentage

```excel
=TEXT(0.0725,"0.00%")
```

**Result:** `7.25%`

The percent sign multiplies the value by 100 and adds the symbol, so the pattern works on a decimal ratio.

### Example 3: Fixed-Width Number

```excel
=TEXT(318,"00000")
```

**Result:** `00318`

Each zero is a required digit. Leading zeros fill the gap, which suits codes and identifiers that must keep the same width.

### Example 4: Phone Number From Digits

```excel
=TEXT(5551230987,"(000) 000-0000")
```

**Result:** `(555) 123-0987`

Literal characters such as parentheses, spaces and hyphens appear in the output as typed. Use this when the digits are stored as a single number.

### Example 5: Full Date in Words

```excel
=TEXT(DATE(2024,3,9),"dddd, mmmm d, yyyy")
```

**Result:** `Saturday, March 9, 2024`

Four d characters give the full weekday name, four m characters give the full month name, and one d gives the day without a leading zero.

### Example 6: Elapsed Hours Above 24

```excel
=TEXT(1.25,"[h]:mm")
```

**Result:** `30:00`

The value 1.25 is one and a quarter days, which is 30 hours. The brackets around h show total elapsed hours instead of resetting at 24.

<!-- Image 2: Format Pattern Results. See Images/Text/TEXT.md -->

## Story Problems

### Problem 1: Invoice Labels With Padded Numbers

Column A holds invoice numbers and column B holds the amounts. The accounting export needs a label for each invoice.

| Invoice | Amount |
| --- | --- |
| 417 | 1250 |
| 52 | 88.5 |
| 1380 | 4012.75 |

**Task:** Build a label in column C that reads `Invoice` followed by the invoice number padded to five digits, then the amount in dollars with two decimals.

**Solution:**

```excel
="Invoice "&TEXT(A2,"00000")&": "&TEXT(B2,"$#,##0.00")
```

**Answer:** `Invoice 00417: $1,250.00`, `Invoice 00052: $88.50` and `Invoice 01380: $4,012.75`. The ampersand joins the pieces, and TEXT supplies the padding and the currency format.

### Problem 2: Total Shift Hours Over 24

Three shifts are stored as time values in `B2:B4`: 0.375 (9:00), 0.4375 (10:30) and 0.5 (12:00). A normal time format would show the total as 7:30 because it resets at 24 hours.

**Task:** Show the total of the three shifts as hours and minutes, with hours allowed to pass 24.

**Solution:**

```excel
=TEXT(SUM(B2:B4),"[h]:mm")
```

**Answer:** `31:30`. The three values add to 1.3125 days, which is 31.5 hours, or 31 hours and 30 minutes.

## Use Cases

### Dashboard Title Amounts

**Scenario:** A dashboard title shows the quarter's revenue in millions. The number must update when the source changes.

```excel
="Revenue: "&TEXT(B2,"$#,##0.0,,")&" million"
```

**Why It Works:** Two commas after the pattern divide the value by one million. With B2 holding 2400000, the title reads `Revenue: $2.4 million`. The scaling is applied only to the display, so B2 keeps its full value.

### Invoice Number Padding

**Scenario:** An accounting system needs invoice numbers that are always five digits long.

```excel
=TEXT(A2,"00000")
```

**Why It Works:** Each zero reserves a digit, so 52 becomes `00052`. Use this in an export column, and keep the original number in the source column.

### Timesheet Totals

**Scenario:** A timesheet adds up daily durations that can exceed one day in total.

```excel
=TEXT(SUM(C2:C20),"[h]:mm")
```

**Why It Works:** The brackets around h keep counting past 24 hours. A plain `h:mm` pattern would wrap the total back to a number under 24.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The pattern is invalid, or it does not suit the value, such as a date pattern applied to a text entry. | Check the pattern and confirm the value is a number, date or time. |
| Month appears where minutes belong | `m` means month unless it follows an hour code or comes before a seconds code. | Write minutes as `h:mm` or `hh:mm`. |
| Unexpected rounding | Digits beyond the decimal places in the pattern are rounded. | Use more decimal places in the pattern, or round the value first with ROUND. |
| Separators look wrong | Thousands and decimal separators follow the regional settings. | Test the pattern on the target locale, or build the separators with SUBSTITUTE. |
| Math on the result fails | TEXT returns text, not a number. | Keep the original number in another cell for calculations. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Supports fraction patterns such as `# ?/?`, the `?` digit placeholder and `[h]` elapsed time. Color codes are accepted but not displayed. |
| Google Sheets | Available | Fraction patterns and the `?` digit placeholder are not supported. Test special patterns before relying on them. |

## Tips and Best Practices

- Keep the source value in its own cell and use TEXT only for display or labels.
- Use `0` for digits that must always appear and `#` for digits that may be left out.
- Scale large numbers with trailing commas in the pattern rather than dividing first, and state the unit in the label.
- Put literal words in double quotes inside the pattern, and double any quotation mark that appears inside the pattern.
- Build a sentence with the ampersand and TEXT, such as `="Total: "&TEXT(A1,"$#,##0.00")`.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CONCATENATE](../Text/CONCATENATE.md) | Joins TEXT output with other text labels. |
| [DOLLAR](../Text/DOLLAR.md) | Formats a number as currency with a fixed style. |
| [FIXED](../Text/FIXED.md) | Formats a number with a set number of decimals and an optional separator. |
| [NUMBERVALUE](../Text/NUMBERVALUE.md) | Converts text to a number using specified separators. |
| [VALUE](../Text/VALUE.md) | Converts text that looks like a number back into a number. |

## Official Documentation

- [Microsoft Support: TEXT function](https://support.microsoft.com/en-us/excel/functions/text-function)
- [Google Docs Editors Help: TEXT](https://support.google.com/docs/answer/3094139)
