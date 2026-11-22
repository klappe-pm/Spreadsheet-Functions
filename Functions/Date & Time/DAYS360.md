---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Arithmetic
purpose:
  - Bond Analysis
  - Date Calculation
use-case:
  - Bond Coupon Periods
  - Loan Interest Accrual
  - Monthly Billing Periods
related:
  - DATE
  - DATEDIF
  - DAYS
  - EDATE
  - EOMONTH
  - YEARFRAC
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/days360-function
  - https://support.google.com/docs/answer/3093042
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Thirty Over 360 Days
tags:
  - date-arithmetic
  - day-count-convention
  - excel
  - interest-accrual
  - sheets
---

# DAYS360

## Description

**DAYS360** counts the days between two dates using a year of 360 days, made of twelve 30-day months. Lenders, bond markets and many accounting systems use this convention to calculate interest, because every full month contributes the same 30 days. Use it when a contract specifies a 30/360 day count.

The function has two conventions, chosen by the optional `method` argument. The default is the U.S. (NASD) method, which adjusts the 31st day of a month in a set of cases. The European method changes every 31st to the 30th. Both methods return a whole number, and the result is negative when the start date is later than the end date.

DAYS360 differs from DAYS, which counts actual calendar days. For a period from January 31 to July 31, DAYS360 returns 180 and DAYS returns 181. Use DAYS when the actual number of days matters, and DAYS360 when the contract uses the 30-day convention.

## Syntax

```excel
=DAYS360(start_date, end_date, [method])
```

<!-- Image 1: Start Date, End Date and Method. See Images/Date & Time/DAYS360.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `start_date` | Yes | The starting date. Enter a date cell, a function that returns a date, or a serial number. |
| `end_date` | Yes | The ending date, with the same input rules as `start_date`. |
| `method` | No | Selects the day count convention. In Excel, `FALSE` or omitted uses the U.S. (NASD) method, and `TRUE` uses the European method. In Sheets, `0` or omitted uses the U.S. method, and any other value uses the European method. |

### Return Value

A whole number of days on a 360-day year basis. The result is negative when `start_date` is later than `end_date`. The function returns `#VALUE!` when a date argument cannot be read as a date.

## Examples

### Example 1: U.S. Method on Month Ends

```excel
=DAYS360(A2, B2)
```

**Result:** With A2 holding January 31, 2026 and B2 holding July 31, 2026, the result is `180`.

Six 30-day months make 180 days. Under the U.S. method, both month-end dates become the 30th, so the count is exactly six months.

### Example 2: European Method

```excel
=DAYS360(A2, B2, TRUE)
```

**Result:** With A2 holding January 15, 2026 and B2 holding March 31, 2026, the result is `75`.

The European method changes the 31st of March to the 30th. From January 15 to March 30 on the 30-day basis is two months (60 days) plus 15 days, which is 75.

### Example 3: U.S. Method on the Same Dates

```excel
=DAYS360(A2, B2)
```

**Result:** With the dates from Example 2, the result is `76`.

Because the start day is 15, the U.S. method moves the end date to April 1, not March 30. That adds one day compared with the European result.

<!-- Image 2: U.S. Versus European Day Count. See Images/Date & Time/DAYS360.md -->

### Example 4: A Full Year

```excel
=DAYS360(DATE(2026, 2, 1), DATE(2027, 1, 31))
```

**Result:** `360`

Under the U.S. method, the 31st of January becomes the 1st of February, which gives one full 360-day year.

### Example 5: Negative Result

```excel
=DAYS360(DATE(2026, 5, 1), DATE(2026, 4, 1))
```

**Result:** `-30`

The start date is one month after the end date, so the result is negative one 30-day month.

## Story Problems

### Problem 1: Loan Interest on a 30/360 Basis

A business borrowed $50,000 at 6 percent per year. The loan agreement uses the 30/360 convention, and interest accrues from January 31, 2026 to July 31, 2026.

| Principal | Annual Rate | Start Date | End Date |
| --- | --- | --- | --- |
| $50,000 | 6% | January 31, 2026 | July 31, 2026 |

**Task:** Find the 30/360 day count in `E2` and the interest owed in `F2`, using 360 days per year.

**Solution:**

```excel
=DAYS360(C2, D2)
=A2 * B2 * E2 / 360
```

The first formula goes in `E2` and the second in `F2`.

**Answer:** 180 days, and interest of $1,500. The actual calendar count is 181 days, but the agreement uses the 30-day convention.

### Problem 2: Bond Coupon Days, Two Conventions

A bond pays a coupon for the period from January 15, 2026 to March 31, 2026. The finance team checks the day count under both conventions.

| Period Start | Period End |
| --- | --- |
| January 15, 2026 | March 31, 2026 |

**Task:** Return the U.S. count in `C2` and the European count in `D2`.

**Solution:**

```excel
=DAYS360(A2, B2)
=DAYS360(A2, B2, TRUE)
```

**Answer:** The U.S. method gives 76 days and the European method gives 75 days. Under the U.S. method, the 31st of March moves to April 1, because the start day (15) is before the 30th, which adds one day.

## Use Cases

### Bond Coupon Schedule

**Scenario:** A treasury analyst lists the coupon periods for a bond that pays twice a year, using the 30/360 convention in the bond terms.

```excel
=DAYS360(B2, C2) / 360
```

**Why It Works:** Dividing the 30/360 day count by 360 gives the fraction of a year in the coupon period, which is the factor used for accrued interest on a 30/360 bond.

### Loan Interest Accrual

**Scenario:** A lender calculates monthly interest for a loan whose contract says every month has 30 days.

```excel
=D2 * E2 * DAYS360(B2, C2) / 360
```

**Why It Works:** The principal in D2 and the annual rate in E2 are multiplied by the 30/360 day count, then divided by 360. The result is interest for the period in the same units as the principal.

### Monthly Billing Periods

**Scenario:** A service provider bills each customer for the days between two billing dates when the contract uses 30-day months.

```excel
=DAYS360(B2, C2, TRUE)
```

**Why It Works:** The European method treats every 31st as the 30th, which keeps month-end billing dates consistent across all periods.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A date argument is text that cannot be read as a date. | Use DATE or a date cell instead of text. |
| Negative result | The start date is later than the end date. | Swap the dates, or wrap the result in ABS when only the size matters. |
| One day more or less than expected | The U.S. and European methods handle 31st-of-month dates differently. | Set `method` to match the contract. |
| Wrong result in Sheets | Slash-separated dates typed directly into the formula are evaluated as division. | Use DATE, or refer to a cell that holds a date. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Default is the U.S. (NASD) method. `TRUE` selects the European method. Returns a negative number when start_date is after end_date. |
| Google Sheets | Available | Default is `0`, the U.S. method. Any other value selects the European method. Slash-separated dates typed directly are read as division. |

## Tips and Best Practices

- Check the day count convention in the contract before choosing a method.
- Use DATE or cell references for every date, so the 30/360 count does not depend on regional text.
- Divide by 360 for the year fraction under this convention, and use the same convention for every period in a schedule.
- Compare the result with DAYS when reconciling a schedule, so a difference of one or two days is expected and explained.
- Use YEARFRAC when a different basis, such as actual over actual, is required.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DATE](DATE.md) | Builds literal dates for DAYS360 formulas. |
| [DATEDIF](DATEDIF.md) | Returns complete months or years, not a 30-day count. |
| [DAYS](DAYS.md) | Counts actual calendar days, the alternative to the 30-day convention. |
| [EDATE](EDATE.md) | Creates the period end dates that a 30/360 schedule uses. |
| [EOMONTH](EOMONTH.md) | Returns month-end dates for schedules that run to the end of each month. |
| [YEARFRAC](YEARFRAC.md) | Expresses a period as a year fraction using a selectable day count basis. |

## Official Documentation

- [Microsoft Support: DAYS360 function](https://support.microsoft.com/en-us/excel/functions/days360-function)
- [Google Docs Editors Help: DAYS360](https://support.google.com/docs/answer/3093042)
