---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Parts
purpose:
  - Date Calculation
use-case:
  - Payroll Week Numbers
  - Weekly Sales Reporting
related:
  - DATE
  - ISOWEEKNUM
  - WEEKDAY
  - WORKDAY
  - YEAR
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/weeknum-function
  - https://support.google.com/docs/answer/3294949
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Week Number
  - Week of Year
tags:
  - date
  - excel
  - iso-week
  - sheets
  - week-numbering
---

# WEEKNUM

## Description

**WEEKNUM** returns the number of the week within the year that contains a given date. The week count starts with 1 in the first week of the year. Which days make up a week, and which week counts as week 1, depend on the return_type argument.

Use WEEKNUM for weekly reports, payroll periods, and any table that groups dates into weeks. Sunday is the default first day of the week. Setting return_type to 2 starts each week on Monday instead.

WEEKNUM uses one of two numbering systems. In system 1, the week that contains January 1 is week 1. In system 2, which is the ISO 8601 method, the week that contains the year's first Thursday is week 1. Only return_type 21 uses system 2. For ISO week numbers without a type argument, use ISOWEEKNUM.

WEEKNUM returns only the week number. It does not include the year, so two dates in different years can return the same number. Add a YEAR test when a list spans more than one year.

## Syntax

```excel
=WEEKNUM(serial_number, [return_type])
```

<!-- Image 1: Week Systems Compared. See Images/Date & Time/WEEKNUM.md -->

Google Sheets names the arguments `date` and `type`, as in `WEEKNUM(date, [type])`. The arguments are positional, so the same formulas work on both platforms.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `serial_number` (Excel) or `date` (Sheets) | Yes | The date to evaluate. Use a cell that contains a date, the result of DATE, or a serial number. Dates typed as text can cause errors. |
| `return_type` (Excel) or `type` (Sheets) | No | The day that starts the week and the numbering system. When omitted, the value is 1 (weeks start on Sunday, system 1). Values 1, 2, 11 to 17 and 21 are documented on both platforms. |

### Return Value

A whole number that identifies the week of the year, usually from 1 to 53. Excel returns `#NUM!` when serial_number is outside the valid date range or when return_type is not a listed value.

## Examples

All examples use the date 11/22/2026 in cell A2 unless the example shows its own date.

<!-- Image 2: Week Number Results for One Date. See Images/Date & Time/WEEKNUM.md -->

### Example 1: Default Week Numbering

```excel
=WEEKNUM(A2)
```

**Result:** `48`

Weeks start on Sunday and the week containing January 1, 2026 is week 1. November 22 falls in week 48.

### Example 2: Weeks Starting on Monday

```excel
=WEEKNUM(A2, 2)
```

**Result:** `47`

With return_type 2, the Monday 11/16/2026 to Sunday 11/22/2026 span is one week, so the same date returns 47.

### Example 3: ISO Week Numbers

```excel
=WEEKNUM(A2, 21)
```

**Result:** `47`

Return_type 21 uses the ISO 8601 system, where week 1 contains the first Thursday of the year. For this date it matches the ISO week number of 47.

### Example 4: A Mid-Year Date

```excel
=WEEKNUM(DATE(2026, 7, 4), 2)
```

**Result:** `27`

Dates built with DATE avoid the text-date problems that can affect a typed date.

### Example 5: The Same Date in Two Systems

```excel
=WEEKNUM(DATE(2026, 3, 15), 1)
```

**Result:** `12`

```excel
=WEEKNUM(DATE(2026, 3, 15), 2)
```

**Result:** `11`

March 15, 2026 is a Sunday. With Sunday weeks it falls in week 12, but with Monday weeks it belongs to the previous week, which is week 11.

## Story Problems

### Problem 1: Weekly Sales Totals

A store records sales by date in A2:B5. Column A holds the sale date and column B holds the sales amount. The store counts weeks from Sunday.

| Date | Sales |
| --- | --- |
| 03/15/2026 | 1200 |
| 03/16/2026 | 950 |
| 03/22/2026 | 1430 |
| 03/23/2026 | 880 |

**Task:** Total the sales that fall in week 12, using the default Sunday start.

**Solution:**

```excel
=SUMPRODUCT((WEEKNUM(A2:A5, 1)=12)*B2:B5)
```

**Answer:** `2150`. The sales on March 15 (1200) and March 16 (950) are in week 12. March 22 and 23 are in week 13.

### Problem 2: Labeling a Training Session

A training school runs its weeks from Monday to Sunday. The first session date is in B2 as 02/09/2026.

**Task:** Build a label such as "Week 7" for the session sheet.

**Solution:**

```excel
="Week "&WEEKNUM(B2, 2)
```

**Answer:** `Week 7`. February 9, 2026 is a Monday in the seventh Monday-based week of the year.

### Problem 3: Counting Dates in an ISO Week

Four invoice dates are listed in A2:A5: 03/15/2026, 03/16/2026, 03/22/2026 and 03/23/2026. A European partner reports by ISO week.

**Task:** Count how many invoices fall in ISO week 12.

**Solution:**

```excel
=SUMPRODUCT((WEEKNUM(A2:A5, 21)=12)*1)
```

**Answer:** `2`. The Monday March 16 and the Sunday March 22 both belong to ISO week 12, which runs from Monday to Sunday.

## Use Cases

### Payroll Week Numbers

**Scenario:** A payroll team pays hourly staff for weeks that run Monday to Sunday and labels each timesheet with its week number.

```excel
=WEEKNUM(A2, 2)
```

**Why It Works:** Return_type 2 starts each week on Monday, so a timesheet dated Monday through Sunday gets the same number. Pair the label with the year to avoid duplicates across years.

### Weekly Sales Reporting

**Scenario:** A sales log covers several years, and a manager needs the total for week 12 of 2026 only.

```excel
=SUMPRODUCT((YEAR(A2:A500)=2026)*(WEEKNUM(A2:A500, 2)=12)*B2:B500)
```

**Why It Works:** The YEAR test limits the rows to 2026, and the WEEKNUM test then selects week 12 among them. Without the YEAR test, week 12 of every year would be added together. Size the ranges to the filled rows, because blank rows in the range can return an error.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | return_type is not one of the listed values. | Use 1, 2, 11 to 17 or 21. |
| `#NUM!` | serial_number is outside the valid date range or is not a date. | Check that the cell holds a date. |
| Duplicate week numbers | WEEKNUM does not include the year. | Add a YEAR test to the criteria. |
| Unexpected week 1 or 53 | Dates near January 1 belong to the week that contains January 1 under system 1. | Use return_type 21 when the report follows ISO weeks. |
| Error on a typed date | Text dates are read differently by locale. | Enter the date with DATE or convert it with DATEVALUE. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions | Documents return_type 1, 2, 11 to 17 and 21. Other values return `#NUM!`. |
| Google Sheets | Available | Documents the same return_type values. Argument names are `date` and `type`. |

## Tips and Best Practices

- Choose return_type 2 for Monday-based weeks and return_type 21 when the report must match ISO week numbers.
- Always pair WEEKNUM with YEAR when a list covers more than one year.
- Compare the week numbers from two systems on a known date before you publish a report that depends on them.
- Use ISOWEEKNUM when you need ISO week numbers and do not want to remember the type value.
- Use DATE to build the date inside the formula when the source value is a fixed date.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds the date to test, with no text-date ambiguity. |
| [ISOWEEKNUM](ISOWEEKNUM.md) | Returns the ISO 8601 week number without a type argument. |
| [WEEKDAY](WEEKDAY.md) | Returns the day of the week rather than the week of the year. |
| [WORKDAY](WORKDAY.md) | Adds business days, which helps build week-based schedules. |
| [YEAR](YEAR.md) | Returns the year, which must be tested alongside the week number. |

## Official Documentation

- [Microsoft Support: WEEKNUM function](https://support.microsoft.com/en-us/excel/functions/weeknum-function)
- [Google Docs Editors Help: WEEKNUM](https://support.google.com/docs/answer/3294949)
