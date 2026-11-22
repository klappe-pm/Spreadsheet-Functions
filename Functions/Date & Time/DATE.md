---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Construction
purpose:
  - Data Cleaning
  - Date Calculation
use-case:
  - Invoice Due Dates
  - Monthly Reporting Periods
  - Payment Schedules
related:
  - DATEVALUE
  - DAY
  - EDATE
  - EOMONTH
  - MONTH
  - TIME
  - TODAY
  - YEAR
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/date-function
  - https://support.google.com/docs/answer/3092969
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Build Date
  - Create Date
tags:
  - date
  - date-construction
  - excel
  - serial-number
  - sheets
---

# DATE

## Description

**DATE** builds a date from three numbers: a year, a month and a day. It returns a serial number that Excel and Google Sheets display as a date. Use it when the year, month and day sit in separate cells, when you need to build a fixed date inside a formula, or when you need to change one part of an existing date.

DATE also accepts month and day values outside their normal ranges and rolls them into the correct date. A month of 14 returns February of the following year, and a day of 0 returns the last day of the previous month. This makes it easy to find month ends (`DATE(year, month + 1, 0)`) and to add months to a date without a lookup table.

Years need care. Excel and Sheets treat a year from 0 to 1899 as an offset from 1900, so `DATE(25, 6, 15)` returns June 15, 1925, not 2025. Always enter four-digit years. If you need to move a date by whole months with end-of-month handling, EDATE and EOMONTH are clearer choices than DATE arithmetic.

## Syntax

```excel
=DATE(year, month, day)
```

<!-- Image 1: Year, Month and Day Arguments. See Images/Date & Time/DATE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `year` | Yes | The year. Values from 1900 to 9999 are used as the year. Values from 0 to 1899 have 1900 added to them, so 25 becomes 1925. |
| `month` | Yes | The month. Normal values are 1 to 12. A value above 12 moves into the following year, and a value below 1 moves back into previous years. |
| `day` | Yes | The day. Normal values are 1 to 31. A value above the length of the month moves into the next month, and a value of 0 or less moves back into the previous month. |

### Return Value

A date serial number. In Excel's default 1900 date system, January 1, 1900 is serial 1, and January 10, 2026 is serial 46032. Excel returns `#NUM!` when the year is below 0 or 10000 or higher. Sheets returns `#NUM!` for the same year range and `#VALUE!` when an argument is text that cannot be read as a number.

## Examples

### Example 1: Build a Specific Date

```excel
=DATE(2026, 1, 10)
```

**Result:** `1/10/2026` (serial number 46032)

Each argument is a plain number, and the result is a true date that can be used in comparisons and calculations.

### Example 2: Build a Date From Cells

```excel
=DATE(A2, B2, C2)
```

**Result:** With A2 set to 2027, B2 set to 5 and C2 set to 18, the result is May 18, 2027.

Keep the year, month and day in separate columns when the source data is already split this way. DATE combines them into one value.

### Example 3: Month Value Above 12

```excel
=DATE(2026, 14, 2)
```

**Result:** `2/2/2027`

Month 14 is February of the following year, because 12 months from January 2026 reaches January 2027 and 2 more months reaches February 2027. The day stays at 2.

<!-- Image 2: Month Overflow Table. See Images/Date & Time/DATE.md -->

### Example 4: Last Day of a Month

```excel
=DATE(2026, 7, 0)
```

**Result:** `6/30/2026`

A day of 0 returns the last day of the previous month. Using the next month number with a day of 0 gives the last day of any month, with leap years handled automatically.

### Example 5: Add Months to a Date

```excel
=DATE(YEAR(A2), MONTH(A2) + 3, DAY(A2))
```

**Result:** With A2 set to January 31, 2026, the result is May 1, 2026.

April has only 30 days, so day 31 of April rolls forward to May 1. Use EDATE when you want the result to stop at the last day of the target month.

### Example 6: Four-Digit Year Versus Two-Digit Year

```excel
=DATE(25, 6, 15)
```

**Result:** `6/15/1925`

The year 25 falls in the 0 to 1899 range, so 1900 is added to it. Enter `2025` instead to get June 15, 2025.

## Story Problems

### Problem 1: Quarterly Payment Schedule

A small equipment lender sends payment reminders on dates built from a year, month and day column. The clerk entered the schedule in `A1:D5` without checking the day values.

| Payment | Year | Month | Day |
| --- | --- | --- | --- |
| 1 | 2026 | 1 | 15 |
| 2 | 2026 | 2 | 31 |
| 3 | 2026 | 4 | 0 |
| 4 | 2026 | 13 | 1 |

**Task:** Build each reminder date in column E with DATE, then state the dates for payments 2 and 4.

**Solution:**

```excel
=DATE(B2, C2, D2)
```

**Answer:** Payment 2 is March 3, 2026, because February 2026 has 28 days and day 31 rolls 3 days past the end of the month. Payment 4 is January 1, 2027, because month 13 is January of the next year. Payment 3 is March 31, 2026, because day 0 of April is the last day of March.

### Problem 2: Last Day of a Fiscal Quarter

A finance team reports results by fiscal quarter. Each quarter ends on the last day of its third month. The analyst stores the year in `A2` and the quarter number in `B2`.

| Fiscal Year | Quarter |
| --- | --- |
| 2026 | 3 |

**Task:** Return the last day of the quarter with DATE, using the quarter number to find the month after the quarter ends.

**Solution:**

```excel
=DATE(A2, B2 * 3 + 1, 0)
```

**Answer:** September 30, 2026. Quarter 3 ends in month 9, so the formula asks for day 0 of month 10, which is September 30.

## Use Cases

### Monthly Reporting Period

**Scenario:** A finance team picks a year and a month in two input cells, then needs the first and last day of that period for a filtered report.

```excel
=DATE(B2, C2, 1)
=DATE(B2, C2 + 1, 0)
```

**Why It Works:** The first formula returns day 1 of the selected month. The second returns the last day of the same month, so the report covers 28, 29, 30 or 31 days without any lookup table.

### Payment Due Date Schedule

**Scenario:** A billing system stores a start year, month and day for each invoice and needs a due date 30 days later.

```excel
=DATE(YEAR(B2), MONTH(B2), DAY(B2)) + 30
```

**Why It Works:** DATE rebuilds the start date from its parts, and adding 30 moves it forward by days. This avoids overflow problems that come from adding to the month number.

### Converting Text Dates

**Scenario:** An export writes dates as text in the form `20260110`, and the analysis needs real date values.

```excel
=DATE(VALUE(LEFT(A2, 4)), VALUE(MID(A2, 5, 2)), VALUE(RIGHT(A2, 2)))
```

**Why It Works:** LEFT, MID and RIGHT split the text into parts, and VALUE converts each part to a number before DATE builds the date. Wrap the formula in IFERROR when some rows may be malformed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The year is below 0 or 10000 or higher. | Use a four-digit year between 1900 and 9999. |
| `#VALUE!` | An argument is text that cannot be read as a number (Sheets). | Convert the text with VALUE or check that the source cell holds a number. |
| Wrong year | A year from 0 to 1899 had 1900 added to it. | Enter the full four-digit year. |
| Unexpected date | A month or day value rolled into another month. | Check the month and day inputs. Overflow is intentional for day 0 and month 13 tricks. |
| `46032` displayed | The cell is formatted as a number, not a date. | Format the cell as a date. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Years 0 to 1899 add 1900. Years 1900 to 9999 are used as entered. Years below 0 or 10000 and higher return `#NUM!`. |
| Google Sheets | Available | Same year rules and month and day rollover. Decimal arguments are truncated, and text arguments return `#VALUE!`. |

## Tips and Best Practices

- Always enter four-digit years, because two-digit years are read differently from what most people expect.
- Use `DATE(year, month + 1, 0)` for the last day of a month instead of counting days in each month.
- Use EDATE or EOMONTH when you need end-of-month behavior for a month addition.
- Validate imported parts before building the date, for example with a check that the month is from 1 to 12.
- Use DATE rather than typed date text in formulas, because typed text depends on regional settings.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATEVALUE](DATEVALUE.md) | Converts a date written as text, when the whole date is in one string. |
| [DAY](DAY.md) | Extracts the day from a date, the reverse of one part of DATE. |
| [EDATE](EDATE.md) | Adds whole months to a date, with end-of-month handling. |
| [EOMONTH](EOMONTH.md) | Returns the last day of a month that is a set number of months away. |
| [MONTH](MONTH.md) | Extracts the month number that DATE uses as input. |
| [TIME](TIME.md) | Builds a time value from hour, minute and second parts. |
| [TODAY](TODAY.md) | Supplies the current date, which DATE can then reshape. |
| [YEAR](YEAR.md) | Extracts the year that DATE uses as input. |

## Official Documentation

- [Microsoft Support: DATE function](https://support.microsoft.com/en-us/excel/functions/date-function)
- [Google Docs Editors Help: DATE](https://support.google.com/docs/answer/3092969)
