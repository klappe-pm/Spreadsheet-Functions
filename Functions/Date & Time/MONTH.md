---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Parts
purpose:
  - Date Calculation
use-case:
  - Fiscal Period Reporting
  - Monthly Sales Totals
  - Subscription Billing Cycles
related:
  - DATE
  - DAY
  - EOMONTH
  - TEXT
  - WEEKDAY
  - WEEKNUM
  - YEAR
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/month-function
  - https://support.google.com/docs/answer/3093052
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Extract Month
  - Month Number
tags:
  - date-parts
  - excel
  - month
  - sheets
  - time-periods
---

# MONTH

## Description

**MONTH** returns the month of a date as an integer from 1 to 12. January is 1, February is 2, and December is 12. The result is a plain number, so it can drive a condition, a grouping key or a calculation. The display format of the date does not matter: a cell that shows "Sep 14, 2026" and a cell that shows "14/09/2026" both return 9.

MONTH belongs with YEAR and DAY. Together they split a date into its parts, and DATE puts the parts back together. Microsoft's documentation states that MONTH returns Gregorian values even when a date is shown in another calendar format, such as Hijri.

MONTH does not return a name. To display "September", format the date with TEXT and the "mmmm" code, or build a date with DATE and format it. MONTH also does not compare years, so a March 2025 date and a March 2026 date both return 3. Add a YEAR check when the period must be unique.

## Syntax

```excel
=MONTH(serial_number)
```

<!-- Image 1: Syntax Anatomy. See Images/Date & Time/MONTH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `serial_number` | Yes | The date to read. It can be a cell that contains a date, a function that returns a date such as DATE or DATEVALUE, or a date serial number such as 40909. Enter dates with DATE rather than as text, because text dates can give unexpected results. |

### Return Value

An integer from 1 (January) to 12 (December). Text that Excel cannot read as a date returns `#VALUE!`. Google Sheets documents that MONTH does not convert date formats typed inside a formula the way cell entry does, so use DATE for dates written in a formula.

## Examples

### Example 1: Month From a Date Cell

```excel
=MONTH(A2)
```

**Result:** `9` (when A2 contains September 14, 2026)

The function reads the stored date and returns its month. The display format in A2 does not change the result.

### Example 2: Month From a DATE Function

```excel
=MONTH(DATE(2008,5,23))
```

**Result:** `5`

DATE builds May 23, 2008, and MONTH returns 5. Entering the date with DATE avoids the text-date problems described in the Common Errors section.

### Example 3: Month Name for Display

```excel
=TEXT(A2,"mmmm")
```

**Result:** `September` (when A2 contains September 14, 2026)

TEXT with "mmmm" returns the full month name as text. Use "mmm" for the three-letter abbreviation. The name follows the spreadsheet's language settings, so it may differ in another locale.

### Example 4: Quarter From a Month

```excel
=ROUNDUP(MONTH(A2)/3,0)
```

**Result:** `3` (when A2 contains September 14, 2026)

Dividing the month by 3 and rounding up gives the calendar quarter. January to March is quarter 1, and October to December is quarter 4.

### Example 5: Fiscal Month for a July Start

```excel
=MOD(MONTH(A2)-7,12)+1
```

**Result:** `3` (when A2 contains September 14, 2026)

For a fiscal year that begins in July, July is fiscal month 1 and September is fiscal month 3. The MOD step wraps months before July around to the end of the fiscal year.

## Story Problems

### Problem 1: March Sales Total

A small shop records each sale with a date in column A and an amount in column B. The owner wants the total for March across all years in the list.

| Sale Date | Amount |
| --- | --- |
| 2026-01-14 | 300 |
| 2026-02-03 | 450 |
| 2026-02-27 | 125 |
| 2026-03-08 | 700 |
| 2026-03-30 | 225 |
| 2026-03-31 | 90 |

**Task:** Add the amounts for every sale made in March.

**Solution:**

```excel
=SUMPRODUCT((MONTH(A2:A7)=3)*B2:B7)
```

**Answer:** `1015`. The March sales are 700, 225 and 90, which add to 1,015. The January and February sales are excluded because their month values are 1 and 2.

### Problem 2: Fiscal Month Totals

A company's fiscal year starts in July. Each payment in column A has an amount in column B. The finance team wants the total for fiscal month 1, which is July.

| Payment Date | Amount |
| --- | --- |
| 2026-07-14 | 500 |
| 2026-02-09 | 300 |
| 2026-06-30 | 250 |
| 2026-07-02 | 125 |

**Task:** Sum the amounts that fall in fiscal month 1.

**Solution:**

```excel
=SUMPRODUCT((MOD(MONTH(A2:A5)-7,12)+1=1)*B2:B5)
```

**Answer:** `625`. The July payments of 500 and 125 are in fiscal month 1. The February payment is fiscal month 8, and the June payment is fiscal month 12.

<!-- Image 2: Fiscal Month Calendar. See Images/Date & Time/MONTH.md -->

## Use Cases

### Monthly Sales Totals

**Scenario:** A finance team wants a monthly revenue summary that updates when new transactions are added to a log.

```excel
=SUMPRODUCT((MONTH(A2:A500)=MONTH(TODAY()))*(YEAR(A2:A500)=YEAR(TODAY()))*B2:B500)
```

**Why It Works:** Each transaction is tested for both the month and the year, so December 2025 is not mixed with December 2026. Including the YEAR test is the step that prevents the function from grouping the same month across different years.

### Subscription Billing Cycles

**Scenario:** A subscription service sends each new account's first invoice in the month it starts. A column flags accounts whose start month is the current month.

```excel
=IF(MONTH(B2)=MONTH(TODAY()),"Due This Month","Not Due")
```

**Why It Works:** MONTH compares the start month in B2 with the current month, so an account that started in an earlier month is not flagged. Add a YEAR test when accounts from the same month in an earlier year must also be excluded.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text that Excel cannot read as a date. | Convert the text with DATEVALUE or enter the date with DATE. |
| Wrong month | Text such as 1/2/2026 is read under a different regional date order. | Use unambiguous dates or DATE(year, month, day). |
| Unexpected number | A formula contains a date typed as text, such as MONTH(10/10/2000), which Google Sheets evaluates as arithmetic. | Wrap the date in DATE. |
| Same month in different years | MONTH ignores the year. | Add a YEAR test to the formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Returns the Gregorian month, including for dates shown in other calendar formats. |
| Google Sheets | Available | Same 1 to 12 result. Dates entered as text inside a formula are not converted the way cell entry is. |

## Tips and Best Practices

- Add a helper column with =MONTH(A2) when the same month number is used by several formulas or a pivot table.
- Pair MONTH with YEAR whenever two dates must be in the same month of the same year.
- Use TEXT for display and MONTH for calculation, because MONTH returns a number and TEXT returns a label.
- Build a date from a month number with DATE(2026,MONTH(A2),1) when you need the first day of that month.
- Validate imported columns with ISNUMBER before you rely on MONTH, because text that looks like a date can return a wrong result.

## Related Functions

| Function | Relationship |
| --- | --- |
| [YEAR](YEAR.md) | Returns the year. Combine it with MONTH to identify a unique month. |
| [DAY](DAY.md) | Returns the day of the month. |
| [DATE](DATE.md) | Builds a date from year, month and day values. Use it with MONTH to find the first or last day of a month. |
| [EOMONTH](EOMONTH.md) | Returns the last day of a month that is a given number of months from a start date. |
| [TEXT](../Text/TEXT.md) | Returns the month name when the format code "mmmm" is used. |
| [WEEKDAY](WEEKDAY.md) | Returns the day of the week, when the calendar unit is a day rather than a month. |

## Official Documentation

- [Microsoft Support: MONTH function](https://support.microsoft.com/en-us/excel/functions/month-function)
- [Google Docs Editors Help: MONTH](https://support.google.com/docs/answer/3093052)
