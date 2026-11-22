---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Arithmetic
purpose:
  - Date Calculation
  - Financial Modeling
use-case:
  - Lease Expiry Dates
  - Month-End Accruals
  - Month-End Reporting Cutoffs
related:
  - DATE
  - DAY
  - EDATE
  - MONTH
  - TODAY
  - YEAR
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/eomonth-function
  - https://support.google.com/docs/answer/3093044
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - End Of Month
  - Month End
tags:
  - date-arithmetic
  - excel
  - month-end
  - sheets
---

# EOMONTH

## Description

**EOMONTH** returns the last day of the month that is a given number of months before or after a start date. Use it for month-end accruals, reporting cutoffs, lease expiry dates and any schedule that must land on a month end. Its result is always the last calendar day of a month, so the day number changes with the month: 28, 29, 30 or 31.

The months argument works like the one in EDATE. A zero returns the end of the start date's own month, a positive number moves forward, and a negative number moves backward. Decimal values are truncated, so 2.6 months counts as 2 months. Both Excel and Sheets document this truncation.

EOMONTH is the right choice when every date should be a month end. For a date on the same day of the month, use EDATE. Use DATE with a day of 0 when you want the same result without a separate function, for example `DATE(2026, 7, 0)` returns June 30, 2026.

## Syntax

```excel
=EOMONTH(start_date, months)
```

<!-- Image 1: Start Date and Month Offset. See Images/Date & Time/EOMONTH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `start_date` | Yes | The starting date. Enter a date cell, a function that returns a date, or a serial number. Text dates can cause errors. |
| `months` | Yes | The number of months to move from `start_date`. Zero stays in the same month, and decimal values are truncated. |

### Return Value

The date of the last day of the target month, as a serial number in Excel. Excel returns `#NUM!` when `start_date` is not a valid date or when the start date plus the months value is not a valid date.

## Examples

### Example 1: Month End of a Date

```excel
=EOMONTH(DATE(2026, 2, 10), 0)
```

**Result:** `2/28/2026`

A zero in the months argument keeps the date in February, and the function returns the last day of that month.

### Example 2: Month End Two Months Ahead

```excel
=EOMONTH(A2, 2)
```

**Result:** With A2 holding November 22, 2026, the result is `1/31/2027`.

Two months after November is January, and January has 31 days.

### Example 3: Leap Year Month End

```excel
=EOMONTH(A2, -1)
```

**Result:** With A2 holding March 15, 2028, the result is `2/29/2028`.

One month before March is February, and 2028 is a leap year, so February ends on the 29th.

### Example 4: First Day of the Next Month

```excel
=EOMONTH(A2, 0) + 1
```

**Result:** With A2 holding November 22, 2026, the result is `12/1/2026`.

Adding 1 to a month end gives the first day of the following month, which is useful for period start dates.

<!-- Image 2: Month-End Schedule. See Images/Date & Time/EOMONTH.md -->

## Story Problems

### Problem 1: Month-End Accrual Dates

A consultant bills work when it is done, but the accounting team records the expense on the last day of the month in which the work was performed. The dates of three jobs are listed below.

| Job | Work Date |
| --- | --- |
| Audit | January 9, 2026 |
| Survey | April 22, 2026 |
| Training | July 3, 2026 |

**Task:** Put the accrual date for each job in column C, the last day of the month of the work date in column B.

**Solution:**

```excel
=EOMONTH(B2, 0)
```

**Answer:** January 31, 2026 for the audit, April 30, 2026 for the survey, and July 31, 2026 for the training. Each accrual lands on the month's last day, so the day number varies.

### Problem 2: Lease Expiry Date

A tenant signs a six-month lease starting November 15, 2026. The property manager needs the expiry date for the renewal diary.

| Lease Start | Term (Months) |
| --- | --- |
| November 15, 2026 | 6 |

**Task:** Return the expiry date in `C2` as the last day of the month that is six months after the start date.

**Solution:**

```excel
=EOMONTH(A2, B2)
```

**Answer:** May 31, 2027. Six months after November 2026 is May 2027, and the function returns its last day.

## Use Cases

### Month-End Accrual Journal

**Scenario:** An accounts team records an accrual for each open purchase order on the last day of the month it was received.

```excel
=EOMONTH(C2, 0)
```

**Why It Works:** EOMONTH gives the posting date for the accrual without needing a month length table, and it works for February in leap years.

### Reporting Cutoff

**Scenario:** A sales team closes its books on the last day of each month and flags any transaction dated after the current month's cutoff.

```excel
=IF(A2 <= EOMONTH(TODAY(), 0), "Current Period", "Future Period")
```

**Why It Works:** EOMONTH of today gives the last day of the current month, so any transaction dated on or before that day is counted in the current close.

### Days Left in the Month

**Scenario:** A project manager wants to know how many days remain in the current month for a sprint report.

```excel
=EOMONTH(TODAY(), 0) - TODAY()
```

**Why It Works:** Subtracting today's date from the month's last day gives the days remaining, which updates on each day the report is opened.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The start_date is not a valid date. | Use a date cell, DATE or DATEVALUE for the start date. |
| `#NUM!` | The start date plus months is outside the valid date range. | Check the months value and the start date. |
| Number shown instead of a date | The result cell has a Number format. | Format the result cell as a date. |
| Wrong month | A decimal months value was truncated, not rounded. | Enter whole months. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns a serial number for the last day of the month. Returns `#NUM!` for invalid input. Decimal months are truncated. |
| Google Sheets | Available | Returns the last calendar day of the calculated month. Decimal months are truncated, not rounded. |

## Tips and Best Practices

- Use EOMONTH with a zero months value to get the end of the current month for any date.
- Add 1 to a month end to get the first day of the next month, for period start dates.
- Use EDATE when the schedule should keep the same day of the month, and EOMONTH when it should land on month ends.
- Enter whole months, and avoid decimal values that are truncated without warning.
- Format result cells as dates, because EOMONTH returns a serial number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Returns the last day of a month when the day argument is 0, without a separate function. |
| [DAY](DAY.md) | Reads the day number of the month end, for example to count days remaining. |
| [EDATE](EDATE.md) | Moves a date by whole months while keeping its day number. |
| [MONTH](MONTH.md) | Reads the month number of the calculated date. |
| [TODAY](TODAY.md) | Supplies the current date for days-remaining and cutoff calculations. |
| [YEAR](YEAR.md) | Reads the year of the calculated month end. |

## Official Documentation

- [Microsoft Support: EOMONTH function](https://support.microsoft.com/en-us/excel/functions/eomonth-function)
- [Google Docs Editors Help: EOMONTH](https://support.google.com/docs/answer/3093044)
