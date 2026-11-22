---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Arithmetic
purpose:
  - Date Calculation
use-case:
  - Invoice Aging
  - Lease Expiry Tracking
  - Project Timelines
related:
  - DATE
  - DATEDIF
  - DAYS360
  - NETWORKDAYS
  - TODAY
  - YEARFRAC
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/days-function
  - https://support.google.com/docs/answer/9061296
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Days Between Dates
tags:
  - date-arithmetic
  - day-count
  - excel
  - sheets
---

# DAYS

## Description

**DAYS** returns the number of calendar days between two dates. It counts every day, weekends and holidays included, and it takes leap days into account. Use it for invoice aging, time remaining on a lease, or the length of a project in days.

The argument order is end date first, then start date. DAYS subtracts the start from the end, so the result is positive when the end is later. Microsoft describes the calculation as end date minus start date. Google Sheets documents the same argument order, but its page does not state the result when the start is later than the end, so test that case in Sheets before relying on it.

DAYS is the simplest day counter in the library. It gives a whole number of days, so use DATEDIF when you need complete months or years, DAYS360 when a 30-day month convention is required, and NETWORKDAYS when weekends and holidays must be excluded.

## Syntax

```excel
=DAYS(end_date, start_date)
```

<!-- Image 1: End Date Minus Start Date. See Images/Date & Time/DAYS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `end_date` | Yes | The later date. Enter a date cell, a function that returns a date, or a serial number. Text dates must be in quotation marks. |
| `start_date` | Yes | The earlier date, with the same input rules as `end_date`. |

### Return Value

A whole number of days. The result is positive when `end_date` is later than `start_date`. The function returns `#VALUE!` when a date argument is text that cannot be read as a date.

## Examples

### Example 1: Days Between Two Cells

```excel
=DAYS(B2, A2)
```

**Result:** With A2 holding August 4, 2026 and B2 holding September 19, 2026, the result is `46`.

August 4 to September 4 is 31 days, and September 4 to September 19 adds 15 more.

### Example 2: A Leap Year

```excel
=DAYS(DATE(2028, 3, 1), DATE(2028, 2, 1))
```

**Result:** `29`

2028 is a leap year, so February has 29 days and the count includes February 29.

<!-- Image 2: Leap Day in a Day Count. See Images/Date & Time/DAYS.md -->

### Example 3: A Full Year

```excel
=DAYS(DATE(2027, 1, 1), DATE(2026, 1, 1))
```

**Result:** `365`

Between January 1, 2026 and January 1, 2027 there are no leap days, so the count is 365.

### Example 4: Reversed Dates

```excel
=DAYS(DATE(2026, 1, 1), DATE(2026, 1, 10))
```

**Result:** `-9`

Because the function subtracts the start from the end, an end date earlier than the start date gives a negative number.

### Example 5: Days Left Until a Deadline

```excel
=DAYS(A2, TODAY())
```

**Result:** A positive number when the deadline in A2 is in the future, and a negative number when it has passed.

Use this form in dashboards to show how many days remain on a contract or filing deadline.

## Story Problems

### Problem 1: Invoice Aging

A consulting firm issued an invoice on August 4, 2026, and the client paid it on September 19, 2026. The accounts team needs the number of days the invoice took to pay.

| Invoice | Issue Date | Paid Date |
| --- | --- | --- |
| INV-214 | August 4, 2026 | September 19, 2026 |

**Task:** Return the number of days between the issue date and the paid date.

**Solution:**

```excel
=DAYS(C2, B2)
```

**Answer:** `46` days. The paid date is the end date, so it comes first in the formula.

### Problem 2: Days Left on a Lease

A warehouse lease ends on March 31, 2027. The property manager reports on November 22, 2026 and wants the days remaining.

| Report Date | Lease End |
| --- | --- |
| November 22, 2026 | March 31, 2027 |

**Task:** Put the report date in `A2` and the lease end in `B2`, then return the days remaining in `C2`.

**Solution:**

```excel
=DAYS(B2, A2)
```

**Answer:** `129` days. November has 8 days after the 22nd, then December (31), January (31), February (28, since 2027 is not a leap year) and March (31) add up to 129.

## Use Cases

### Invoice Aging Report

**Scenario:** A finance team sorts open invoices by how long they have been outstanding, and it flags any invoice over 60 days.

```excel
=IF(DAYS(TODAY(), B2) > 60, "Overdue 60+", "Current")
```

**Why It Works:** DAYS measures the time from the issue date in B2 to today, and the IF turns the count into a flag that a filter can use.

### Contract Renewal Window

**Scenario:** A procurement team wants to start renewal talks 90 days before each contract ends.

```excel
=IF(DAYS(B2, TODAY()) <= 90, "Start Renewal", "Wait")
```

**Why It Works:** The end date comes first, so the count is the days left until the contract ends. A value of 90 or less means renewal work should start now.

### Project Duration

**Scenario:** A project planner needs the duration in calendar days for each phase, including weekends.

```excel
=DAYS(C2, B2) + 1
```

**Why It Works:** DAYS gives the difference between the end and start dates. Adding 1 counts both the first and the last day of the phase.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A date argument is text that cannot be read as a date. | Use quotation marks around text dates, or use DATE or DATEVALUE. |
| Negative result | The arguments are in the wrong order, or the end date is earlier. | Put the later date first. |
| Off by one | The formula counts the difference, not the days inclusive of both ends. | Add 1 when both the start and end days should count. |
| Date shown instead of a number | The result cell has a date format. | Format the result cell as Number. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Subtracts start_date from end_date. Text dates must be in quotation marks. |
| Google Sheets | Available | Same argument order. Leap days are included. The documentation does not state the sign of a reversed result. |

## Tips and Best Practices

- Keep the later date in the first argument so the result stays positive.
- Use DATE for literal dates in formulas, so they do not depend on regional text formats.
- Use NETWORKDAYS when weekends and holidays must not count.
- Format the result as Number, or the count will show as a date.
- Put a fixed reference date in one cell when many rows need the same comparison date.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds literal dates to use in DAYS formulas. |
| [DATEDIF](DATEDIF.md) | Returns complete years, months or days, rather than a total day count. |
| [DAYS360](DAYS360.md) | Counts days using a 30-day month convention for interest calculations. |
| [NETWORKDAYS](NETWORKDAYS.md) | Counts working days between two dates, excluding weekends and optional holidays. |
| [TODAY](TODAY.md) | Supplies the current date, the usual second argument for days remaining. |
| [YEARFRAC](YEARFRAC.md) | Expresses the same span as a fraction of a year. |

## Official Documentation

- [Microsoft Support: DAYS function](https://support.microsoft.com/en-us/excel/functions/days-function)
- [Google Docs Editors Help: DAYS](https://support.google.com/docs/answer/9061296)
