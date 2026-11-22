---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Arithmetic
purpose:
  - Date Calculation
  - Loan Analysis
use-case:
  - Contract Renewal Dates
  - Loan Maturity Dates
  - Subscription Billing Dates
related:
  - DATE
  - DATEDIF
  - DAYS360
  - EOMONTH
  - TODAY
  - WORKDAY
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/edate-function
  - https://support.google.com/docs/answer/3092974
date-created: 2025-06-20
date-revised: 2026-11-22
aliases:
  - Add Months
  - Months Offset
tags:
  - date-arithmetic
  - excel
  - month-addition
  - sheets
---

# EDATE

## Description

**EDATE** returns the date that is a given number of months before or after a start date. It keeps the same day of the month, so a contract that starts on the 15th renews on the 15th. Use it for renewal dates, loan maturity dates and any schedule that moves by whole months.

EDATE is safer than adding months with DATE. In Excel, when the day does not exist in the target month, EDATE returns the last day of that month. For example, a start date of January 31 plus one month returns February 28 (or February 29 in a leap year). Adding months with DATE(YEAR(A2), MONTH(A2) + 1, DAY(A2)) would roll that date into early March instead.

The months argument can be negative to move backward. Any decimal part is truncated, not rounded, so 2.9 months counts as 2 months. Use EOMONTH when the schedule should always fall on the last day of a month.

## Syntax

```excel
=EDATE(start_date, months)
```

<!-- Image 1: Start Date Plus Months. See Images/Date & Time/EDATE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `start_date` | Yes | The starting date. Enter a date cell, a function that returns a date such as DATE, or a serial number. Text dates can cause errors. |
| `months` | Yes | The number of months to add (positive) or subtract (negative). Decimal values are truncated to whole months. |

### Return Value

A date serial number in Excel, or a date in Sheets, for the date the given number of months from `start_date`. Excel returns `#VALUE!` when `start_date` is not a valid date.

## Examples

### Example 1: Add Three Months

```excel
=EDATE(DATE(2026, 1, 15), 3)
```

**Result:** `4/15/2026`

January 15 moved forward three months keeps the day number 15 and lands on April 15.

### Example 2: Subtract Months

```excel
=EDATE(A2, -6)
```

**Result:** With A2 holding March 20, 2026, the result is `9/20/2025`.

A negative months value moves the date backward, and the function handles the change of year.

### Example 3: Decimal Months Are Truncated

```excel
=EDATE(A2, 2.9)
```

**Result:** With A2 holding March 20, 2026, the result is `5/20/2026`.

The 2.9 is truncated to 2, so the result is two months after the start date, not three.

### Example 4: Target Month Is Shorter

```excel
=EDATE(A2, 1)
```

**Result:** With A2 holding January 31, 2026, the result is `2/28/2026`.

February has no 31st, so EDATE returns the last day of February. The day stays at the end of the month rather than rolling into March.

<!-- Image 2: Month-End Clamp. See Images/Date & Time/EDATE.md -->

## Story Problems

### Problem 1: Renewal Dates for a Service Contract

A software contract starts on January 31, 2026 and renews every month for three months. The vendor needs each renewal date for the invoice schedule.

| Start Date | Months Ahead |
| --- | --- |
| January 31, 2026 | 1 |
| January 31, 2026 | 2 |
| January 31, 2026 | 3 |

**Task:** In column C, return the renewal date for each row by adding the months in column B to the start date in A.

**Solution:**

```excel
=EDATE(A2, B2)
```

**Answer:** February 28, 2026, March 31, 2026 and April 30, 2026. Each date is counted from the original January 31 start, so the result stays at the last day of any month that is shorter.

### Problem 2: Loan Maturity Date

A business loan is issued on August 15, 2026 with an 18-month term. The finance team needs the maturity date for the repayment calendar.

| Loan Issued | Term (Months) |
| --- | --- |
| August 15, 2026 | 18 |

**Task:** Return the maturity date in `C2` by adding the term in `B2` to the issue date in `A2`.

**Solution:**

```excel
=EDATE(A2, B2)
```

**Answer:** February 15, 2028. Eighteen months after August 2026 is February 2028, and the 15th is kept.

## Use Cases

### Contract Renewal Calendar

**Scenario:** A procurement team tracks contracts with a start date and a renewal interval in months, and it needs the next renewal date for each.

```excel
=EDATE(B2, C2)
```

**Why It Works:** Adding the interval to the start date gives the next renewal. Pairing the formula with TODAY and a filter flags contracts that renew within the next 60 days.

### Subscription Billing Dates

**Scenario:** A billing system charges each subscriber on the same day each month, and it needs the next charge date.

```excel
=EDATE(B2, DATEDIF(B2, TODAY(), "M") + 1)
```

**Why It Works:** DATEDIF counts the complete months since the subscription began, adding 1 gives the next charge month, and EDATE keeps the original billing day, falling back to the last day of shorter months.

### Loan Repayment Schedule

**Scenario:** A lender builds a repayment table with one row per monthly payment, each dated one month after the previous row.

```excel
=EDATE(A2, 1)
```

**Why It Works:** Each row uses the date above it as the start, and the next row adds one month. This keeps the payment day consistent through short months.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The start_date argument is not a valid date (Excel). | Use a date cell, DATE, or DATEVALUE for the start date. |
| Number shown instead of a date | The result cell has a Number format. | Format the result cell as a date. |
| Date one month later than expected | The start date was a month end, and the target month is shorter. | Expect the last day of the target month, or use EOMONTH for month-end schedules. |
| Two months instead of three | A decimal months value was truncated. | Enter whole months. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Returns a serial number. Returns `#VALUE!` for an invalid start date. Decimal months are truncated. |
| Google Sheets | Available | Same arguments. Decimal months are truncated, not rounded. |

## Tips and Best Practices

- Use the original start date with the cumulative month count, as in Problem 1, instead of chaining from the last result, so short months do not shift the schedule.
- Enter whole months only, and check the input when a schedule is built from text.
- Use EOMONTH instead when every date should be the last day of its month.
- Use EDATE with DATEDIF to find the next anniversary of a date.
- Format the result cells as dates, because EDATE returns a date serial number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds a date from parts, but does not keep the day when the target month is shorter. |
| [DATEDIF](DATEDIF.md) | Counts the complete months between two dates, the inverse of adding months. |
| [DAYS360](DAYS360.md) | Counts days between EDATE dates on a 30-day month basis. |
| [EOMONTH](EOMONTH.md) | Moves a date by whole months and returns the last day of the target month. |
| [TODAY](TODAY.md) | Supplies the current date for renewal and billing checks. |
| [WORKDAY](WORKDAY.md) | Adds working days, not months, to a date. |

## Official Documentation

- [Microsoft Support: EDATE function](https://support.microsoft.com/en-us/excel/functions/edate-function)
- [Google Docs Editors Help: EDATE](https://support.google.com/docs/answer/3092974)
