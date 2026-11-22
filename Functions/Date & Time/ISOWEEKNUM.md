---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Parts
purpose:
  - Date Calculation
use-case:
  - Shift Planning
  - Support Ticket Reporting
  - Weekly Sales Reporting
related:
  - DATE
  - MONTH
  - NETWORKDAYS
  - WEEKDAY
  - WEEKNUM
  - WORKDAY
  - YEAR
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/isoweeknum-function
  - https://support.google.com/docs/answer/7368793
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - ISO Week Number
tags:
  - date-parts
  - excel
  - iso-8601
  - sheets
  - week-number
---

# ISOWEEKNUM

## Description

**ISOWEEKNUM** returns the ISO 8601 week number of the year for a date. Under this standard, weeks start on Monday and week 1 is the week that contains the year's first Thursday. Because of that rule, the first days of January can belong to week 52 or 53 of the previous year, and the last days of December can belong to week 1 of the next year.

Use ISOWEEKNUM when schedules, reports or billing cycles follow the ISO calendar, which is common in international business and in many European organizations. The function gives a different answer from WEEKNUM, which starts weeks on Sunday by default and counts week 1 as the week that contains January 1. Pick one convention for a workbook, state it in the header, and use the same function everywhere.

ISOWEEKNUM returns only the week number, not the year. A date in late December can have a week number of 1, so a label built from YEAR alone will be wrong for those dates. The Use Cases section shows a formula that returns the correct ISO year as well.

## Syntax

```excel
=ISOWEEKNUM(date)
```

<!-- Image 1: Syntax Anatomy. See Images/Date & Time/ISOWEEKNUM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `date` | Yes | A date from a cell, the result of a function such as DATE, or a date serial number. Text that Excel cannot read as a date causes an error. Enter dates with DATE to avoid text problems. |

### Return Value

An integer that is the ISO week number of the date, normally from 1 to 53. Microsoft's documentation states that the function returns `#NUM!` when the argument is not a valid number and `#VALUE!` when it is not a valid date type.

## Examples

### Example 1: Week Number of a Cell Date

```excel
=ISOWEEKNUM(A2)
```

**Result:** `10` (when A2 contains March 9, 2012)

March 9, 2012 is a Friday. The ISO week runs from Monday, March 5 to Sunday, March 11, so the week number is 10.

### Example 2: A January Date That Belongs to the Previous Year

```excel
=ISOWEEKNUM(DATE(2021,1,1))
```

**Result:** `53`

January 1, 2021 is a Friday. Its ISO week runs from Monday, December 28, 2020 to Sunday, January 3, 2021, and that week contains Thursday, December 31, 2020. The week therefore belongs to 2020, and 2020 has 53 ISO weeks, so the result is 53 even though the date is in 2021.

<!-- Image 2: ISO Week Boundary Calendar. See Images/Date & Time/ISOWEEKNUM.md -->

### Example 3: Week Label With Leading Zero

```excel
="W"&TEXT(ISOWEEKNUM(A2),"00")
```

**Result:** `W10` (when A2 contains March 5, 2026)

The format code `"00"` pads single-digit weeks so that labels such as W02 and W10 sort in the correct order.

### Example 4: Alternating Weeks

```excel
=IF(MOD(ISOWEEKNUM(A2),2)=0,"Crew B","Crew A")
```

**Result:** `Crew B` (when A2 contains March 5, 2026, which is in week 10)

MOD returns 0 for even week numbers, so the formula alternates between two crews from one week to the next.

## Story Problems

### Problem 1: Support Tickets by ISO Week

A help desk logs the date each ticket opens in column A.

| Opened On |
| --- |
| 2026-03-02 |
| 2026-03-05 |
| 2026-03-11 |
| 2026-03-12 |
| 2026-03-19 |

**Task:** Count how many tickets were opened in ISO week 10 of 2026.

**Solution:**

```excel
=SUMPRODUCT(--(ISOWEEKNUM(A2:A6)=10))
```

**Answer:** `2`. March 2 is a Monday and March 5 is a Thursday, so both fall in week 10. March 11 and 12 fall in week 11, and March 19 falls in week 12.

### Problem 2: Year-End Calendar Dates

A finance team lists three dates that cross the year boundary.

| Date | Event |
| --- | --- |
| 2025-12-29 | Holiday Freeze Starts |
| 2025-12-31 | Year-End Close |
| 2026-01-05 | Payroll Run |

**Task:** Put ISOWEEKNUM in column C next to each date and state the week number of each event.

**Solution:**

```excel
=ISOWEEKNUM(A2)
```

Fill the formula down to C4.

**Answer:** `1`, `1` and `2`. December 29 and December 31, 2025 belong to week 1 of 2026 because that week contains Thursday, January 1, 2026. January 5, 2026 is a Monday in week 2.

## Use Cases

### Weekly Sales Reporting

**Scenario:** A regional team sends a weekly sales summary and wants a label such as 2026-W01 that stays correct in late December and early January.

```excel
=YEAR(A2-WEEKDAY(A2,2)+4)&"-W"&TEXT(ISOWEEKNUM(A2),"00")
```

**Why It Works:** Under ISO rules, the Thursday of a week decides which year the week belongs to. WEEKDAY(A2,2) returns 1 for Monday through 7 for Sunday, so A2 minus that value plus 4 is the Thursday of the same week. YEAR of that Thursday gives the correct ISO year, even for December 29 to 31, which becomes 2026-W01.

### Crew Rotation by Week

**Scenario:** A warehouse runs two crews that alternate weeks. Each shift row needs the crew name calculated from its date.

```excel
=IF(MOD(ISOWEEKNUM(B2),2)=0,"Crew B","Crew A")
```

**Why It Works:** The week number changes every Monday, so the parity of the week number flips the crew at each week boundary. Because ISOWEEKNUM always starts weeks on Monday, the rotation stays aligned with the shift calendar even at year end.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The argument is not a valid number. | Check that the cell holds a date or a serial number. |
| `#VALUE!` | The argument is text that Excel cannot read as a date. | Convert the text with DATEVALUE or enter the date with DATE. |
| Week 1 for a December date | The date falls in the week that contains the next year's first Thursday. | Use the ISO year formula in the Use Cases section when labels need a year. |
| Week differs from WEEKNUM | The two functions use different week rules. | Choose one function and use it throughout the workbook. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365, Excel 2024, Excel 2021 and Excel 2019 | Returns `#NUM!` for a non-numeric argument and `#VALUE!` for a non-date type. |
| Google Sheets | Available | Weeks follow ISO 8601, with Monday as the first day. Google recommends DATE for entering dates because text values can return errors. |

## Tips and Best Practices

- Use ISOWEEKNUM when the calendar must follow ISO 8601. Use WEEKNUM when your organization counts weeks from Sunday.
- Pair the week number with the ISO year so that dates from late December and early January are labeled correctly.
- Enter dates with DATE or as real date values, not as text that looks like a date.
- Format week labels with TEXT and "00" so that the labels sort properly.
- Write the week convention in a header or note so that readers know which calendar the report uses.

## Related Functions

| Function | Relationship |
| --- | --- |
| [WEEKNUM](WEEKNUM.md) | Week number with a Sunday start by default, for organizations that use that convention. |
| [WEEKDAY](WEEKDAY.md) | Returns the day of the week; mode 2 numbers Monday as 1, which the year formula uses. |
| [YEAR](YEAR.md) | Returns the calendar year; combine it with a Thursday calculation to get the ISO year. |
| [DATE](DATE.md) | Builds a date from year, month and day values. |
| [MONTH](MONTH.md) | Returns the month number, useful for monthly rather than weekly grouping. |
| [NETWORKDAYS](NETWORKDAYS.md) | Counts workdays between two dates, which often pairs with weekly planning. |
| [WORKDAY](WORKDAY.md) | Returns the date a number of workdays after a start date. |

## Official Documentation

- [Microsoft Support: ISOWEEKNUM function](https://support.microsoft.com/en-us/excel/functions/isoweeknum-function)
- [Google Docs Editors Help: ISOWEEKNUM](https://support.google.com/docs/answer/7368793)
