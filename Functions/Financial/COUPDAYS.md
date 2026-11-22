---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Date Calculation
use-case:
  - Bond Coupon Schedules
  - Bond Portfolio Reporting
  - Coupon Period Length
related:
  - COUPDAYBS
  - COUPDAYSNC
  - COUPNCD
  - COUPNUM
  - COUPPCD
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/coupdays-function
  - https://support.google.com/docs/answer/3093204
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Coupon Period Days
  - Days In Coupon Period
tags:
  - bond-math
  - coupon-period
  - day-count
  - excel
  - sheets
---

# COUPDAYS

## Description

**COUPDAYS** returns the number of days in the coupon period that contains the settlement date. For a semiannual bond the coupon period is one half of a year, so the result is usually about 180 days. The function uses the basis you choose, so the same dates can give slightly different counts under 30/360 and actual days.

COUPDAYS is the total that the other coupon day functions divide. COUPDAYBS counts the days already elapsed in the period, and COUPDAYSNC counts the days left until the next coupon. On the 30/360 and actual/actual bases, their sum equals COUPDAYS. Use COUPDAYS as the denominator when you calculate the share of a coupon that has accrued, or when you need the length of a coupon period for a yield calculation.

COUPDAYS does not return the number of days between the issue and maturity dates. It always measures one coupon period, so its result depends on the frequency and the coupon dates, not on the bond's full life.

## Syntax

```excel
=COUPDAYS(settlement, maturity, frequency, [basis])
```

<!-- Image 1: Coupon Period Length. See Images/Financial/COUPDAYS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the bond. It must fall before `maturity`. |
| `maturity` | Yes | The date the bond expires and repays its principal. It must fall after `settlement`. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual or `4` for quarterly. |
| `basis` | No | The day count basis. `0` or omitted uses US (NASD) 30/360. `1` uses actual/actual, `2` actual/360, `3` actual/365 and `4` European 30/360. |

### Return Value

A number of days: the length of the coupon period that contains the settlement date. With basis 3 (actual/365), the result can include a decimal, for example 182.5 for a semiannual bond. The function returns `#VALUE!` when `settlement` or `maturity` is not a valid date, and `#NUM!` when `frequency` is not 1, 2 or 4, `basis` is outside 0 to 4, or `settlement` falls on or after `maturity`.

## Examples

All examples use a bond that settles on February 10, 2027, and matures on August 15, 2029, with coupons on February 15 and August 15. The quarterly example uses a bond that settles on May 20, 2027, and matures on November 15, 2028.

### Example 1: Length of the Current Coupon Period

```excel
=COUPDAYS(DATE(2027,2,10),DATE(2029,8,15),2,1)
```

**Result:** `184`

The coupon period containing February 10, 2027, runs from August 15, 2026, to February 15, 2027, which is 184 actual days.

### Example 2: The Same Period on a 30/360 Basis

```excel
=COUPDAYS(DATE(2027,2,10),DATE(2029,8,15),2,0)
```

**Result:** `180`

Under 30/360 every half year counts as 180 days, regardless of the calendar.

### Example 3: A Quarterly Bond

```excel
=COUPDAYS(DATE(2027,5,20),DATE(2028,11,15),4,1)
```

**Result:** `92`

The coupon period containing May 20, 2027, runs from May 15 to August 15, 2027, which is 92 actual days.

### Example 4: Quarterly Period on a 30/360 Basis

```excel
=COUPDAYS(DATE(2027,3,3),DATE(2029,9,15),4,0)
```

**Result:** `90`

Each quarter counts as 90 days under 30/360, so the result is the same for every quarterly period on that basis.

## Story Problems

The problems use this bond table. Enter each date as a true date value.

| Bond | Settlement | Maturity | Frequency | Basis |
| --- | --- | --- | --- | --- |
| Quill | 2026-10-14 | 2031-04-15 | 2 | 1 |
| Ridge | 2027-03-03 | 2029-09-15 | 4 | 0 |
| Tarn | 2026-12-01 | 2027-12-15 | 1 | 1 |

### Problem 1: Coupon Period for the Quill Bond

A portfolio analyst needs the length of the coupon period that contains the settlement of the Quill bond. The bond pays semiannual coupons on April 15 and October 15.

**Task:** Find the number of days in the coupon period for Quill, which is in row 2.

**Solution:**

```excel
=COUPDAYS(B2,C2,D2,E2)
```

**Answer:** `183`, because the coupon period runs from April 15 to October 15, 2026, which is 183 actual days.

### Problem 2: Annual Coupon on the Tarn Note

A small pension scheme holds the Tarn note, which pays one coupon each year on December 15. The scheme settles the trade on December 1, 2026.

**Task:** Find the number of days in the coupon period that contains the settlement date for Tarn, which is in row 4.

**Solution:**

```excel
=COUPDAYS(B4,C4,D4,E4)
```

**Answer:** `365`, because the coupon period runs from December 15, 2025, to December 15, 2026.

<!-- Image 2: Coupon Period Table. See Images/Financial/COUPDAYS.md -->

## Use Cases

### Bond Coupon Schedules

**Scenario:** A treasury team builds a schedule that shows the length of each coupon period for a set of bonds over the coming year.

```excel
=COUPDAYS(Settle,Maturity,Freq,Basis)
```

**Why It Works:** The result changes with the frequency and the period dates, so keep those inputs in cells and copy the formula down the schedule.

### Coupon Period Length

**Scenario:** An analyst needs the length of the current coupon period as an input to a yield calculation.

```excel
=COUPDAYS(DATE(2027,2,10),DATE(2029,8,15),2,1)
```

**Why It Works:** The yield functions use the coupon period length directly, so the basis here must match the basis used in the yield formula.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `frequency` is not 1, 2 or 4. | Enter the number of coupons per year. |
| `#NUM!` | `settlement` is on or after `maturity`. | Check the settlement and maturity dates. |
| `#NUM!` | `basis` is below 0 or above 4. | Use a basis code from 0 to 4. |
| `#VALUE!` | A date is stored as text. | Enter the dates with `DATE` or convert the text to date values. |
| Unexpected decimal | With basis 3 the period length is 365 divided by the frequency, so a semiannual period is 182.5 days. | Expect decimals with basis 3, or use a basis that counts whole days. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365 and Excel for the web | The optional argument is named `basis`. |
| Google Sheets | Available | The same four arguments, with the optional argument named `day_count_convention`. The day count options match Excel. |

## Tips and Best Practices

- Use COUPDAYS as the denominator for accrued share, and use COUPDAYBS as the numerator.
- Use the same basis for every function that works on the same bond.
- Expect the result to change with the frequency, because a quarterly period is about 90 days and a semiannual period about 180.
- Enter every date as a date value, not as text, so the period is found correctly.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUPDAYBS](COUPDAYBS.md) | The days elapsed in the coupon period, the numerator for the accrued share. |
| [COUPDAYSNC](COUPDAYSNC.md) | The days left until the next coupon, which adds to COUPDAYBS to give this result on the 30/360 and actual/actual bases. |
| [COUPNCD](COUPNCD.md) | The next coupon date, which is the end of the period COUPDAYS measures. |
| [COUPNUM](COUPNUM.md) | The number of coupons left until maturity. |
| [COUPPCD](COUPPCD.md) | The last coupon date, which is the start of the period COUPDAYS measures. |

## Official Documentation

- [Microsoft Support: COUPDAYS function](https://support.microsoft.com/en-us/excel/functions/coupdays-function)
- [Google Docs Editors Help: COUPDAYS](https://support.google.com/docs/answer/3093204)
