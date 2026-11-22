---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Workdays
purpose:
  - Date Calculation
use-case:
  - Project Schedule Planning
  - Service Level Deadlines
  - Turnaround Time Reporting
related:
  - DATE
  - DAYS
  - NETWORKDAYS.INTL
  - SUMIFS
  - WORKDAY
  - WORKDAY.INTL
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/networkdays-function
  - https://support.google.com/docs/answer/3092979
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Business Days
  - Working Days Between Dates
tags:
  - business-days
  - excel
  - sheets
  - workdays
  - workweek
---

# NETWORKDAYS

## Description

**NETWORKDAYS** counts the whole working days between a start date and an end date, inclusive of both dates. Saturday and Sunday are treated as weekend days. If you give it a list of holidays, those dates are removed from the count as well. It is the standard tool for estimating business-day durations such as project phases, service response windows and invoice terms.

Use NETWORKDAYS when the weekend is Saturday and Sunday. For any other weekend, such as Friday and Saturday or a single day off, use NETWORKDAYS.INTL, which accepts a weekend argument. To go the other way, from a start date and a number of working days to a finish date, use WORKDAY.

NETWORKDAYS counts whole days only. A time component on either date is ignored. Microsoft's documentation does not describe the result when end_date is earlier than start_date, so put the earlier date first in any formula you depend on.

## Syntax

```excel
=NETWORKDAYS(start_date, end_date, [holidays])
```

<!-- Image 1: Syntax Anatomy. See Images/Date & Time/NETWORKDAYS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `start_date` | Yes | The first date of the period. It can be a cell, a DATE result or a serial number. |
| `end_date` | Yes | The last date of the period. The count includes this date when it is a workday. |
| `holidays` | No | A range of cells or an array constant that lists dates to exclude. Leave it out to count only weekends. |

### Return Value

An integer that counts the workdays from start_date to end_date, inclusive. Dates that are not valid return `#VALUE!` in Microsoft Excel.

## Examples

### Example 1: Workdays Without Holidays

```excel
=NETWORKDAYS(A2,B2)
```

**Result:** `20` (when A2 contains March 2, 2026 and B2 contains March 27, 2026)

The period has four full weeks, which is 20 weekdays. Both end dates are counted because the range is inclusive.

### Example 2: Workdays With a Holiday List

```excel
=NETWORKDAYS(A2,B2,D2:D3)
```

**Result:** `18` (with holidays March 9 and March 16, 2026 in D2:D3)

Both holidays fall on Mondays, which are workdays, so each removes one day from the 20 weekdays in Example 1.

### Example 3: A Period That Spans the Year End

```excel
=NETWORKDAYS(DATE(2026,12,21),DATE(2027,1,4))
```

**Result:** `11`

The period runs from Monday, December 21, 2026 to Monday, January 4, 2027. That is two full weeks plus one extra Monday, which gives 11 weekdays. The year boundary needs no special handling.

### Example 4: A Weekend Start Date

```excel
=NETWORKDAYS(A2,A2)
```

**Result:** `0` (when A2 contains Saturday, March 7, 2026)

When the start and end are the same weekend day, the count is 0. The same formula returns 1 for a single weekday.

## Story Problems

### Problem 1: Website Redesign Schedule

A design team starts a website redesign on March 2, 2026 and expects to deliver on March 27, 2026. The office is closed on March 9 for a company event.

| Start | End | Office Closed |
| --- | --- | --- |
| 2026-03-02 | 2026-03-27 | 2026-03-09 |

**Task:** Count the working days in the project, excluding the closure.

**Solution:**

```excel
=NETWORKDAYS(A2,B2,C2)
```

**Answer:** `19`. The period contains 20 weekdays, and the closure on Monday, March 9 removes one of them.

<!-- Image 2: Holiday Excluded Calendar. See Images/Date & Time/NETWORKDAYS.md -->

### Problem 2: Laboratory Turnaround Time

A laboratory receives samples on June 1, 2026 and must report results by June 30, 2026. Its holiday on June 19 falls on a Friday.

| Received | Due | Holiday |
| --- | --- | --- |
| 2026-06-01 | 2026-06-30 | 2026-06-19 |

**Task:** Count the working days available for the turnaround.

**Solution:**

```excel
=NETWORKDAYS(A2,B2,C2)
```

**Answer:** `21`. June 2026 has 22 weekdays. The June 19 holiday falls on a weekday, so the count drops to 21.

## Use Cases

### Service Level Deadlines

**Scenario:** A support desk promises a response within five business days. Each ticket needs a due date that skips weekends and company holidays.

```excel
=WORKDAY(B2,5,$H$2:$H$10)
```

**Why It Works:** WORKDAY returns the date five working days after the opening date, which is the due date. NETWORKDAYS is used in the report to measure the working days that have actually passed, so both functions share the same holiday list in H2:H10.

### Turnaround Time Reporting

**Scenario:** A manager wants to compare how many working days each request took from start to finish, using one shared holiday list.

```excel
=NETWORKDAYS(B2,C2,Holidays)
```

**Why It Works:** Using a named range for the holiday list keeps every formula consistent when the list changes. Because NETWORKDAYS is inclusive, a request opened and closed on the same weekday returns 1, which means one working day.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A date is not a valid date value, often because it is text. | Convert the cell with DATEVALUE or enter the date with DATE. |
| Count is one too high | The formula includes an end date that was not meant to count. | Subtract 1 if the end date should be excluded, or use WORKDAY for an offset. |
| Holidays have no effect | The holiday dates are text or sit outside the period. | Confirm the holiday cells are real dates within the range. |
| Count includes weekends | The weekend is not Saturday and Sunday. | Switch to NETWORKDAYS.INTL and set the weekend argument. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions | Holidays can be a range or an array constant of serial numbers. Invalid dates return `#VALUE!`. |
| Google Sheets | Available | Same arguments and Saturday and Sunday weekend. Holidays can be a range or an array of date values. |

## Tips and Best Practices

- Keep one holiday list on its own sheet or in a named range, and reference it from every workday formula.
- Enter holidays as real dates. A holiday typed as text is silently ignored in the count.
- Use NETWORKDAYS.INTL when the weekend differs from Saturday and Sunday.
- Pair NETWORKDAYS with WORKDAY so that a deadline and the measured duration use the same calendar.
- Check a short period by hand once after building the formula, because the inclusive count is easy to misread.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NETWORKDAYS.INTL](NETWORKDAYS.INTL.md) | Same count with a custom weekend. Use it when Saturday and Sunday are not the weekend. |
| [WORKDAY](WORKDAY.md) | Returns the date that is a number of workdays after a start date, the reverse of counting. |
| [WORKDAY.INTL](WORKDAY.INTL.md) | Returns a workday offset with a custom weekend. |
| [DATE](DATE.md) | Builds dates for the start, end and holiday arguments. |
| [DAYS](DAYS.md) | Counts calendar days, including weekends, between two dates. |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Totals values by date range when the business-day count is not needed. |

## Official Documentation

- [Microsoft Support: NETWORKDAYS function](https://support.microsoft.com/en-us/excel/functions/networkdays-function)
- [Google Docs Editors Help: NETWORKDAYS](https://support.google.com/docs/answer/3092979)
