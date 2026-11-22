---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Workdays
purpose:
  - Date Calculation
use-case:
  - Invoice Due Dates
  - Project Milestones
  - Shipping Lead Times
related:
  - DATE
  - EDATE
  - EOMONTH
  - NETWORKDAYS
  - NETWORKDAYS.INTL
  - WORKDAY.INTL
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/workday-function
  - https://support.google.com/docs/answer/3093059
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Add Workdays
  - Business Day Offset
tags:
  - business-days
  - date
  - excel
  - holidays
  - sheets
---

# WORKDAY

## Description

**WORKDAY** returns the date that is a given number of working days before or after a start date. Saturdays and Sundays are never counted as working days. Any dates in an optional holiday list are skipped as well. The start date itself is not counted, so the result is always a later (or earlier) working day.

Use WORKDAY to set due dates, delivery promises and project milestones that must land on a business day. A negative number of days counts backward from the start date. The result is a date serial number, so format the cell as a date to read it.

WORKDAY always treats Saturday and Sunday as the weekend. When a calendar uses a different weekend, such as Friday and Saturday, use WORKDAY.INTL. To count the business days between two dates instead of finding an end date, use NETWORKDAYS.

## Syntax

```excel
=WORKDAY(start_date, days, [holidays])
```

<!-- Image 1: Start Date, Days and Holiday Range. See Images/Date & Time/WORKDAY.md -->

Google Sheets uses the argument names `start_date`, `num_days` and `holidays`. The order is the same, so the formulas carry over between platforms.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `start_date` | Yes | The date to count from. Use a cell that contains a date, the result of DATE, or a serial number. |
| `days` | Yes | The number of working days to add (positive) or subtract (negative). Decimal values are truncated, so 2.9 counts as 2. |
| `holidays` | No | A range of cells or an array constant that lists the non-working dates. Omit it when there are no holidays to skip. |

### Return Value

A date serial number for the resulting working day. The function returns `#VALUE!` when an argument is not a valid date and `#NUM!` when the result falls outside the valid date range.

## Examples

Examples 2 and 4 use the holiday list in H2:H4, which holds 12/24/2026, 12/25/2026 and 01/01/2027. Examples 1, 3 and 5 use no holiday list.

### Example 1: Due Date With No Holidays

```excel
=WORKDAY(A2, 10)
```

**Result:** `12/04/2026` when A2 holds 11/20/2026

Ten working days after Friday November 20 land on Friday December 4, because the weekends of November 21 to 22 and November 28 to 29 are skipped.

### Example 2: Skipping Holidays

```excel
=WORKDAY(A2, 10, H2:H4)
```

**Result:** `01/06/2027` when A2 holds 12/18/2026

The holidays on December 24, December 25 and January 1 are not counted, so the count runs into January 2027.

<!-- Image 2: Holiday Dates Skipped in a Schedule. See Images/Date & Time/WORKDAY.md -->

### Example 3: Counting Backward

```excel
=WORKDAY(A2, -5)
```

**Result:** `11/11/2026` when A2 holds 11/18/2026

A negative days value counts back five working days from Wednesday November 18, skipping the weekend of November 14 and 15.

### Example 4: Backward Count Across a Holiday

```excel
=WORKDAY(A2, -3, H2:H4)
```

**Result:** `12/29/2026` when A2 holds 01/04/2027

Counting back from Monday January 4, 2027, the holiday on January 1 is skipped, so the three working days are December 31, December 30 and December 29.

### Example 5: Decimal Days

```excel
=WORKDAY(A2, 2.9)
```

**Result:** `12/21/2026` when A2 holds 12/17/2026

The days value is truncated to 2, so the result is two working days after Thursday December 17: Friday December 18 and Monday December 21.

## Story Problems

### Problem 1: Invoice Payment Terms

A consulting firm issues invoices on the date in B2 and sets payment due three working days later. Its holiday list is in D2:D3.

| Item | Value |
| --- | --- |
| Invoice date (B2) | 12/17/2026 |
| Holiday (D2) | 12/24/2026 |
| Holiday (D3) | 12/25/2026 |

**Task:** Find the payment due date.

**Solution:**

```excel
=WORKDAY(B2, 3, D2:D3)
```

**Answer:** `12/22/2026`. The working days are Friday December 18, Monday December 21 and Tuesday December 22.

### Problem 2: Project Milestone After Thanksgiving

A design team starts a project on 11/20/2026 and must deliver milestone 1 after 10 working days. The US Thanksgiving holiday on 11/26/2026 is listed as a holiday in D2.

**Task:** Find the milestone date.

**Solution:**

```excel
=WORKDAY(A2, 10, D2)
```

**Answer:** `12/07/2026`. The holiday on November 26 is skipped, so the tenth working day falls on Monday December 7.

### Problem 3: Shipping Lead Time

An order is placed on Friday 12/18/2026. The warehouse needs four working days to pack it, and the holidays 12/24/2026 and 12/25/2026 are listed in D2:D3.

**Task:** Find the date the order leaves the warehouse.

**Solution:**

```excel
=WORKDAY(A2, 4, D2:D3)
```

**Answer:** `12/28/2026`. The working days are December 21, 22, 23 and then December 28, because the holidays on December 24 and 25 are skipped.

## Use Cases

### Invoice Due Dates

**Scenario:** Accounts receivable sets payment due 30 working days after the invoice date, using a holiday table on another sheet.

```excel
=WORKDAY(B2, 30, Holidays)
```

**Why It Works:** The named range `Holidays` keeps the holiday list in one place, so every invoice uses the same calendar. Update the list once each year.

### Project Milestones

**Scenario:** A project plan lists each task with a duration in working days and needs the finish date for every task.

```excel
=WORKDAY(C2, D2, Holidays)
```

**Why It Works:** Each row adds its duration to the previous finish date in C2. Copy the formula down the column and the chain of dates updates when a duration changes.

### Shipping Lead Times

**Scenario:** A store promises delivery within five working days of the order date.

```excel
=WORKDAY(A2, 5, Holidays)
```

**Why It Works:** Because the holiday list is included, a carrier closure is not counted as a shipping day. Remember that the start date is not counted, so an order placed on a Friday with a one-day lead time is due on the following Monday.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | start_date or a holiday is not a valid date, often because it was typed as text. | Enter the dates with DATE or convert them with DATEVALUE. |
| `#NUM!` | The result falls outside the valid date range. | Check the start date and the size of the days value. |
| Holiday ignored | The holiday cells hold text, or the range does not include them. | Convert the holiday cells to dates and check the range. |
| Wrong result for a different weekend | WORKDAY always uses Saturday and Sunday as the weekend. | Use WORKDAY.INTL with the right weekend code. |
| Off by one day | The start date is not counted, so the first working day after it is day 1. | Test with a short known schedule and adjust the days value. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Weekend is always Saturday and Sunday. Holidays can be a range or an array constant. Decimal days are truncated. |
| Google Sheets | Available | Same arguments and weekend rule. Holidays can be a range or an array of date values. |

## Tips and Best Practices

- Keep the holiday list in a named range on its own sheet so every date formula uses the same calendar.
- Enter holiday dates as real dates, not text, so they are matched correctly.
- Use WORKDAY.INTL for calendars with a different weekend.
- Use NETWORKDAYS to count working days between two dates, which is the reverse of WORKDAY.
- Test a few results by hand around each holiday before you publish a due-date table.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds a start date from year, month and day. |
| [EDATE](EDATE.md) | Adds calendar months rather than working days. |
| [EOMONTH](EOMONTH.md) | Returns the last day of a month, a common end point for working-day counts. |
| [NETWORKDAYS](NETWORKDAYS.md) | Counts the working days between two dates, the reverse of WORKDAY. |
| [NETWORKDAYS.INTL](NETWORKDAYS.INTL.md) | Counts working days with a custom weekend. |
| [WORKDAY.INTL](WORKDAY.INTL.md) | Adds working days with a custom weekend. |

## Official Documentation

- [Microsoft Support: WORKDAY function](https://support.microsoft.com/en-us/excel/functions/workday-function)
- [Google Docs Editors Help: WORKDAY](https://support.google.com/docs/answer/3093059)
