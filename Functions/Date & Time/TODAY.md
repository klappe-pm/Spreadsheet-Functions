---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Construction
purpose:
  - Date Calculation
use-case:
  - Contract Expiration Alerts
  - Employee Tenure Tracking
  - Invoice Aging Reports
related:
  - DATE
  - DATEDIF
  - EDATE
  - EOMONTH
  - NOW
  - WEEKDAY
  - WORKDAY
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/today-function
  - https://support.google.com/docs/answer/3092984
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Current Date
  - Today Date
tags:
  - current-date
  - date
  - excel
  - sheets
  - volatile
---

# TODAY

## Description

**TODAY** returns the current date as a serial number, which the spreadsheet displays as a date when the cell is formatted that way. The result has no time part, so it always represents the start of the day. It takes no arguments and recalculates whenever the spreadsheet does, so a formula that uses TODAY shows the date on which the sheet was last calculated.

Use TODAY as a moving reference point for deadlines, ages, overdue checks and reporting periods. Because dates are stored as whole numbers, you can add days to TODAY, subtract a date from it, or compare it with a date in a cell. For a value that includes the time of day, use NOW instead.

TODAY is a volatile function, which means it recalculates on most changes to a workbook. A few thousand TODAY formulas rarely cause a problem, but a very large workbook may slow down. When a fixed snapshot is needed, such as the date a report was issued, paste the value as static or type the date in a cell.

## Syntax

```excel
=TODAY()
```

<!-- Image 1: Syntax Anatomy. See Images/Date & Time/TODAY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| *(none)* | No | TODAY takes no arguments. The empty parentheses must still be typed. |

### Return Value

The serial number of the current date, with no time portion. In Excel, a cell formatted as General changes to a date format when TODAY is entered. Change the format to General or Number to see the serial number itself.

## Examples

### Example 1: Display Today's Date

```excel
=TODAY()
```

**Result:** the current date in the cell's date format, for example `11/22/2026` on the day this guide was written

The formula reads the system date at each recalculation. Its displayed value changes from one day to the next.

### Example 2: Days Until a Deadline

```excel
=A2-TODAY()
```

**Result:** the number of days from today to the date in A2, negative once the date has passed

Date subtraction gives a count of days. If A2 holds a date 45 days away, the result is 45. Format the cell as a number, not a date, to see the count.

### Example 3: A Future Date From Today

```excel
=TODAY()+30
```

**Result:** the date 30 days from today, which is `12/22/2026` when today is November 22, 2026

Adding a whole number to TODAY moves the date forward by that many days. This pattern suits invoice due dates and renewal reminders.

### Example 4: Days Left in the Year

```excel
=DATE(YEAR(TODAY()),12,31)-TODAY()
```

**Result:** `39` when today is November 22, 2026

The formula builds December 31 of the current year with DATE and subtracts today. The count shrinks by one each day and reaches 0 on December 31.

<!-- Image 2: Days Until Deadline Timeline. See Images/Date & Time/TODAY.md -->

### Example 5: Last Day of the Current Month

```excel
=EOMONTH(TODAY(),0)
```

**Result:** `11/30/2026` when today is November 22, 2026

EOMONTH with an offset of 0 returns the last day of the month that contains TODAY. An offset of 1 would return the last day of the following month.

## Story Problems

### Problem 1: Overdue Invoices

A consultancy keeps a list of invoices with their due dates in column B. A column flags each invoice that has passed its due date.

| Invoice | Due Date |
| --- | --- |
| INV-201 | 2026-10-31 |
| INV-202 | 2026-11-30 |
| INV-203 | 2026-12-15 |

**Task:** Flag each invoice whose due date is earlier than today.

**Solution:**

```excel
=IF(B2<TODAY(),"Overdue","Open")
```

**Answer:** The result depends on the day the sheet is opened. Every invoice whose due date is before that day shows Overdue, and the flags update automatically. On November 22, 2026, INV-201 is Overdue, while INV-202 and INV-203 are Open.

### Problem 2: Contract Renewal Window

A legal team wants a fixed reporting date, not today's date, so that every printout of the report shows the same numbers. The report date is typed into B1 as January 15, 2027.

| Contract | Expires |
| --- | --- |
| Supplier A | 2027-02-10 |

**Task:** Count the days from the report date in B1 to the expiry date in column B.

**Solution:**

```excel
=B2-$B$1
```

**Answer:** `26`. January has 16 days after the 15th, and February 10 adds 10 more, which gives 26 days. Typing a fixed date in B1 keeps the report the same whenever it is printed.

## Use Cases

### Invoice Aging Reports

**Scenario:** An accounts receivable team groups open invoices into aging buckets so that collections can prioritize the oldest balances.

```excel
=IF(TODAY()-B2<=30,"0 to 30",IF(TODAY()-B2<=60,"31 to 60","Over 60"))
```

**Why It Works:** TODAY minus the invoice date gives the age in days, and nested IF tests place each invoice in a bucket. Because TODAY recalculates, the buckets move forward every day without anyone editing the report.

### Contract Expiration Alerts

**Scenario:** A procurement team wants a warning when a vendor contract is due to expire within 90 days.

```excel
=IF(B2-TODAY()<=0,"Expired",IF(B2-TODAY()<=90,"Renew Soon","Active"))
```

**Why It Works:** Subtracting TODAY from the expiry date gives the days remaining. The first test catches contracts that have ended, and the second flags those due within 90 days, so the status column stays current without manual updates.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument was typed inside the parentheses. | Remove it, because TODAY takes none. |
| Number displayed instead of a date | The cell is formatted as General or Number. | Apply a date format. |
| Date does not update | Calculation is set to manual. | Press F9 in Excel or change the calculation setting to automatic. |
| Different dates across users | Users in different regions may see different dates near midnight. | Document the time zone the sheet uses and check File > Settings > Time zone. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Uses the computer's system date in desktop Excel. The 1900 date system is the default. |
| Google Sheets | Available | Google's TODAY reference describes the current date and does not describe time zones. Check File > Settings > Time zone when users work across regions. |

## Tips and Best Practices

- Keep one TODAY reference in a labeled cell, such as B1, and point other formulas at that cell to reduce recalculation.
- Use a typed report date in a cell instead of TODAY when a report must not change after it is issued.
- Compare dates with TODAY using whole-day values, because TODAY has no time part.
- Pair TODAY with WEEKDAY or NETWORKDAYS when the calculation must skip weekends.
- Document the time zone when a shared sheet depends on the date near midnight.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NOW](NOW.md) | Returns the date and the current time. Use it when the time of day matters. |
| [DATE](DATE.md) | Builds a fixed date from year, month and day values. |
| [DATEDIF](DATEDIF.md) | Returns the complete years, months or days between a start date and TODAY. |
| [EDATE](EDATE.md) | Adds a number of months to TODAY, keeping the same day of the month. |
| [EOMONTH](EOMONTH.md) | Returns the last day of a month, offset from TODAY. |
| [WEEKDAY](WEEKDAY.md) | Returns the day of the week for TODAY, for weekend or workday checks. |
| [WORKDAY](WORKDAY.md) | Returns a date a number of workdays after TODAY. |

## Official Documentation

- [Microsoft Support: TODAY function](https://support.microsoft.com/en-us/excel/functions/today-function)
- [Google Docs Editors Help: TODAY](https://support.google.com/docs/answer/3092984)
