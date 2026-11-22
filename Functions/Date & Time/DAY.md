---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Parts
purpose:
  - Data Validation
  - Date Calculation
use-case:
  - Billing Day Schedules
  - Month-End Close Checks
  - Payroll Pay Dates
related:
  - DATE
  - DAYS
  - EOMONTH
  - MONTH
  - TODAY
  - WEEKDAY
  - YEAR
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/day-function
  - https://support.google.com/docs/answer/3093040
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Day Of Month
  - Extract Day
tags:
  - date-parts
  - day-of-month
  - excel
  - sheets
---

# DAY

## Description

**DAY** returns the day of the month from a date, as a whole number from 1 to 31. It ignores the month and year, so a date of March 15, 2026 returns 15. Use it when you need the day part on its own, for example to find payroll dates, billing days or the position of a date within its month.

DAY reads the underlying date value, not the way the date is displayed. A cell that shows `15 Mar 2026`, `3/15/2026` or `2026-03-15` returns 15 in each case, provided the cell holds a real date. A date typed into a formula as slash-separated text is a different case: Google Sheets reads `10/10/2000` as a division, so use DATE to build the date instead.

DAY is the day half of the YEAR, MONTH and DAY set. Together with DATE, it lets you change one part of a date and keep the others. For example, `DATE(YEAR(A2), MONTH(A2) + 1, DAY(A2))` moves a date forward one month, but it overflows when the day does not exist in the new month, so EDATE or EOMONTH is safer for month-end dates.

## Syntax

```excel
=DAY(serial_number)
```

<!-- Image 1: Date Cell to Day Number. See Images/Date & Time/DAY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `serial_number` | Yes | The date to read. Use a cell that holds a date, a function such as DATE, TODAY or DATEVALUE, or a serial number. |

### Return Value

A whole number from 1 to 31. The largest possible value depends on the month of the date, so a February date returns at most 28 or 29, and a date in April, June, September or November returns at most 30.

## Examples

### Example 1: Day From a Date Cell

```excel
=DAY(A2)
```

**Result:** With A2 holding March 15, 2026, the result is `15`.

The cell's display format does not change the result. DAY reads the date behind the cell.

### Example 2: Day From a Built Date

```excel
=DAY(DATE(2026, 9, 22))
```

**Result:** `22`

DATE builds the date from its parts, so this formula is a safe way to write a literal date in a formula.

### Example 3: Days Remaining in the Month

```excel
=DAY(EOMONTH(A2, 0)) - DAY(A2)
```

**Result:** With A2 holding March 15, 2026, the result is `16`.

EOMONTH returns March 31, which has day 31, and subtracting the day 15 leaves 16 days.

<!-- Image 2: Days Remaining in a Month. See Images/Date & Time/DAY.md -->

### Example 4: Flag a Month-End Date

```excel
=IF(DAY(A2) = DAY(EOMONTH(A2, 0)), "Month End", "Not Month End")
```

**Result:** With A2 holding February 28, 2026, the result is `Month End`.

The test works for every month length, because EOMONTH supplies the last day of the month for each date.

### Example 5: Check for a Payroll Day

```excel
=IF(OR(DAY(A2) = 1, DAY(A2) = 15), "Pay Day", "Not Pay Day")
```

**Result:** With A2 holding January 15, 2026, the result is `Pay Day`.

Many payroll calendars pay on the first and fifteenth of each month. Extend the test with WEEKDAY if weekend dates move to another day.

### Example 6: Day From Text

```excel
=DAY(DATEVALUE("3/14/2026"))
```

**Result:** `14`

DATEVALUE converts the text to a date first, and DAY then reads the day. Passing the text straight to DAY is less reliable across regional settings.

## Story Problems

### Problem 1: Billing Days for Subscribers

A software company bills customers on the day they signed up. The billing team lists five billing dates in `B2:B6` and wants to count how many fall on the first or the fifteenth of the month.

| Customer | Billing Date |
| --- | --- |
| Acme | January 1, 2026 |
| Birch | January 15, 2026 |
| Cedar | January 20, 2026 |
| Dune | February 15, 2026 |
| Elm | March 9, 2026 |

**Task:** Count the customers whose billing day is 1 or 15 with DAY inside a single formula.

**Solution:**

```excel
=SUMPRODUCT(--((DAY(B2:B6) = 1) + (DAY(B2:B6) = 15) > 0))
```

**Answer:** `3`. Acme (day 1), Birch (day 15) and Dune (day 15) match. Cedar is on the 20th and Elm is on the 9th.

### Problem 2: Days Left in the Month

A project manager reports progress on September 22, 2026. She wants the number of days left in that month, counting the report date itself as one of the days already used.

| Report Date |
| --- |
| September 22, 2026 |

**Task:** Put the report date in `A2` and return the number of days remaining after it in `B2`.

**Solution:**

```excel
=DAY(EOMONTH(A2, 0)) - DAY(A2)
```

**Answer:** `8`. September has 30 days, so 30 minus 22 leaves 8 days after the report date.

## Use Cases

### Billing Day Schedule

**Scenario:** A subscription platform bills each customer on the same day of the month they joined, and it needs the billing date for the current month.

```excel
=DATE(YEAR(TODAY()), MONTH(TODAY()), MIN(DAY(B2), DAY(EOMONTH(TODAY(), 0))))
```

**Why It Works:** DAY keeps the signup day, and the MIN with the last day of the current month stops a January 31 signup from producing March 3 in February. The result is the billing date for this month.

### Month-End Close Checklist

**Scenario:** An accounting team flags any transaction dated within the last three days of a month for close review.

```excel
=IF(DAY(A2) > DAY(EOMONTH(A2, 0)) - 3, "Review", "Normal")
```

**Why It Works:** The last day of the month comes from EOMONTH, and DAY compares the transaction's day against the three days before it. The test works for February as well as 31-day months.

### Payroll Calendar

**Scenario:** A payroll team pays staff on the 1st and 15th and needs to flag any payment that falls on a weekend so it can be moved.

```excel
=IF(OR(DAY(A2) = 1, DAY(A2) = 15), IF(WEEKDAY(A2, 2) > 5, "Move Payment", "Pay"), "")
```

**Why It Works:** DAY selects the pay dates, and WEEKDAY with type 2 gives Monday as 1 through Sunday as 7, so values above 5 mark Saturday and Sunday.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text that cannot be read as a date. | Convert the text with DATEVALUE, or build the date with DATE. |
| Unexpected 0 or 1 | The argument is a small number, such as the result of dividing `10/10/2000` in Sheets. | Pass a real date cell, or build the date with DATE. |
| Wrong day | The text was read with the other day and month order because of regional settings. | Use DATE with separate year, month and day values. |
| Day shown as a date | The result cell has a date format. | Format the result cell as Number. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns 1 to 31 from a date serial number. Microsoft advises entering dates with DATE or as formula results, and notes that text dates can cause problems. |
| Google Sheets | Available | Returns 1 to 31. Slash-separated dates typed directly into a formula are evaluated as numbers, so use DATE or a date cell. |

## Tips and Best Practices

- Use DAY with EOMONTH to find the last day of a month, then compare it with DAY(A2) to test for month-end dates.
- Use MIN with DAY and the month length when a date may not exist in the target month.
- Build literal dates with DATE, not with typed text, so the formula works in any regional setting.
- Store dates as real date values in data, so DAY reads them the same way in every row.
- Add a helper column with DAY for large data sets when you need to group or count by day of month.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds the date that DAY reads, or changes one part of an existing date. |
| [DAYS](DAYS.md) | Counts the days between two dates, rather than reading the day of one date. |
| [EOMONTH](EOMONTH.md) | Returns the last day of a month, the usual companion for month-end tests. |
| [MONTH](MONTH.md) | Reads the month number, the companion to the day number. |
| [TODAY](TODAY.md) | Supplies the current date, the usual input for a current day of month. |
| [WEEKDAY](WEEKDAY.md) | Returns the day of the week, which pairs with DAY for payroll and billing rules. |
| [YEAR](YEAR.md) | Reads the year, completing the set of date part functions. |

## Official Documentation

- [Microsoft Support: DAY function](https://support.microsoft.com/en-us/excel/functions/day-function)
- [Google Docs Editors Help: DAY](https://support.google.com/docs/answer/3093040)
