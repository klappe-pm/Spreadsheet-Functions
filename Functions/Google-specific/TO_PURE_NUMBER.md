---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Parser Functions
purpose:
  - Data Cleaning
  - Number Formatting
use-case:
  - Date Gap Calculation
  - Export Cleanup
related:
  - 'N'
  - TO_DATE
  - TO_DOLLARS
  - TO_PERCENT
level: 2
source:
  - https://support.google.com/docs/answer/3094243
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Strip Formatting
tags:
  - conversion
  - data-cleaning
  - formatting
  - sheets
---

# TO_PURE_NUMBER

## Description

**TO_PURE_NUMBER** returns the plain number behind a formatted value. A cell that shows `$1,250.00`, `50%`, `3/15/2025` or `12:00 PM` holds a number underneath, and TO_PURE_NUMBER removes the display formatting so that only that number is returned. The result has no currency symbol, percent sign, date display or thousands separators.

Use TO_PURE_NUMBER when a formula or an export needs the raw value of a formatted cell. Date formats are a common case: the serial number behind a date is the count of days since December 30, 1899, and subtracting two serial numbers gives the number of days between the dates. The function is the formula version of choosing Format, then Number, then Normal.

TO_PURE_NUMBER is similar to N, but the two handle non-numeric input differently. N returns 0 for text, and TO_PURE_NUMBER returns the text unchanged. Use TO_PURE_NUMBER when the input is a formatted number that you want to clean up, and use N when you need a number from a value that might be text.

## Syntax

```excel
=TO_PURE_NUMBER(value)
```

<!-- Image 1: Formatted Display Versus Pure Number. See Images/Google-specific/TO_PURE_NUMBER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value, or a reference to a cell, to convert. It can be a formatted number such as a currency, percentage, date or time. Non-numeric input is returned unchanged. |

### Return Value

A plain number with no formatting. Dates return their serial number, times return the fraction of a day, and percentages return the decimal. If the input is not numeric, the function returns it unchanged. The official documentation does not list error values or other limits for TO_PURE_NUMBER.

## Examples

Each example is a separate formula. The cell formats are noted where they matter.

### Example 1: Currency Cell

```excel
=TO_PURE_NUMBER(A2)
```

**Result:** `1250` when `A2` displays as `$1,250.00`

The currency symbol and the decimal places are removed, and the underlying number remains.

### Example 2: Percentage Input

```excel
=TO_PURE_NUMBER(50%)
```

**Result:** `0.5`

The percent sign is a format, so the function returns the decimal behind it.

### Example 3: Date Cell

```excel
=TO_PURE_NUMBER(B2)
```

**Result:** `45658` when `B2` displays as `1/1/2025`

The date is returned as its serial number, the count of days since December 30, 1899.

### Example 4: Time Cell

```excel
=TO_PURE_NUMBER(C2)
```

**Result:** `0.5` when `C2` displays as `12:00 PM`

A time is a fraction of a day, and noon is halfway through the day.

<!-- Image 2: Date Cells and Their Serial Numbers. See Images/Google-specific/TO_PURE_NUMBER.md -->

### Example 5: Text Input Returned Unchanged

```excel
=TO_PURE_NUMBER("Pending")
```

**Result:** `Pending`

Text passes through without an error, so a column that mixes numbers and labels keeps its labels.

## Story Problems

### Problem 1: Days Between Two Dates

A project plan lists a start date in `B2` and a due date in `C2`. Both cells are formatted as dates, and the team wants the number of days between them.

| Milestone | Start | Due |
| --- | --- | --- |
| Design review | 1/1/2025 | 3/15/2025 |

**Task:** Calculate the number of days from the start to the due date in `D2`.

**Solution:**

```excel
=TO_PURE_NUMBER(C2)-TO_PURE_NUMBER(B2)
```

**Answer:** `73`. The serial number for March 15, 2025 is 45731, the serial for January 1, 2025 is 45658, and 45731 minus 45658 is 73.

<!-- Image 3: Days Between Two Formatted Dates. See Images/Google-specific/TO_PURE_NUMBER.md -->

### Problem 2: Invoice Amounts for an Export

Two invoice amounts in `B2:B3` are formatted as currency, so they display as `$1,250.00` and `$980.50`. An export template needs the plain values to add them in a text field.

**Task:** Return the two amounts as plain numbers and add them in `B5`.

**Solution:**

```excel
=TO_PURE_NUMBER(B2)+TO_PURE_NUMBER(B3)
```

**Answer:** `2230.5`, because 1250 plus 980.5 is 2230.5.

## Use Cases

### Date Gap Calculation

**Scenario:** A shipping log stores order and delivery dates as formatted dates, and the operations team wants the number of days each delivery took.

```excel
=TO_PURE_NUMBER(D2)-TO_PURE_NUMBER(C2)
```

**Why It Works:** Subtracting serial numbers gives the day count, while the formatted dates would still show a date result.

### Export Cleanup

**Scenario:** A reporting tool reads a column of amounts, and it rejects values that carry a currency symbol or a thousands separator.

```excel
=TO_PURE_NUMBER(E2)
```

**Why It Works:** The formatting is removed while the number stays the same, so the export holds clean values that the reporting tool can read.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Date shows a large number such as `45731` | The function returns the serial number, which is the date's underlying value. | Apply a date format to the result cell, or use TO_DATE to show it as a date again. |
| Percentage shows `0.5` | The function returns the decimal form of the percentage. | Multiply by 100 or apply a percent format to show it as a percentage again. |
| Text comes back unchanged | The input is text, not a number. | Use N if the value should become 0 for text, or VALUE to convert numeric text. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Multiply by 1 to return the plain number, or use N, which returns 0 for text. |
| Google Sheets | Available | Removes all formatting and returns the number, and non-numeric input is returned unchanged. |

## Tips and Best Practices

- Use TO_PURE_NUMBER before subtracting dates, so the result is a day count rather than a formatted date.
- Apply a number format to the result cell after using TO_PURE_NUMBER, because the output is shown as a plain number.
- Use N when text should count as zero, and TO_PURE_NUMBER when text should pass through to be checked.
- Test the input type first with ISNUMBER when a column can contain both numbers and labels.

## Related Functions

| Function | Relationship |
| --- | --- |
| [N](../Information/N.md) | Returns a number from a value, and returns 0 for text. |
| [TO_DATE](TO_DATE.md) | Converts a number back into a date for display. |
| [TO_DOLLARS](TO_DOLLARS.md) | Applies the Currency format to a number. |
| [TO_PERCENT](TO_PERCENT.md) | Applies the Percent format to a number. |

## Official Documentation

- [Google Docs Editors Help: TO_PURE_NUMBER](https://support.google.com/docs/answer/3094243)
