---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Date Calculation
use-case:
  - Bond Coupon Schedules
  - Bond Trade Settlement
  - Coupon Payment Forecasting
related:
  - COUPDAYBS
  - COUPDAYS
  - COUPDAYSNC
  - COUPNUM
  - COUPPCD
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/coupncd-function
  - https://support.google.com/docs/answer/3093157
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Next Coupon Date
  - Next Interest Payment Date
tags:
  - bond-math
  - coupon-period
  - day-count
  - excel
  - sheets
---

# COUPNCD

## Description

**COUPNCD** returns the date of the next coupon payment after the settlement date. If a bond settles on February 10 and pays coupons on February 15 and August 15, COUPNCD returns February 15. The coupon dates are set by the maturity date and the frequency, so the result does not depend on when the bond was issued.

Use COUPNCD to schedule cash receipts, to show a buyer when the first payment arrives, or to build a list of coupon dates for a portfolio. The result is a date. Format the cell as a date, or the formula displays a serial number such as 46433.

COUPNCD and COUPPCD are a pair. COUPPCD returns the coupon date before settlement, and COUPNCD returns the coupon date after it. The number of days between them equals COUPDAYS for the same inputs, on the 30/360 and actual/actual bases.

## Syntax

```excel
=COUPNCD(settlement, maturity, frequency, [basis])
```

<!-- Image 1: Coupon Dates Around Settlement. See Images/Financial/COUPNCD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the bond. It must fall before `maturity`. |
| `maturity` | Yes | The date the bond expires and repays its principal. It must fall after `settlement`. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual or `4` for quarterly. |
| `basis` | No | The day count basis. `0` or omitted uses US (NASD) 30/360. `1` uses actual/actual, `2` actual/360, `3` actual/365 and `4` European 30/360. |

### Return Value

A date serial: the next coupon date after `settlement`. The function returns `#VALUE!` when `settlement` or `maturity` is not a valid date, and `#NUM!` when `frequency` is not 1, 2 or 4, `basis` is outside 0 to 4, or `settlement` falls on or after `maturity`.

## Examples

All examples use a bond that settles on February 10, 2027, and matures on August 15, 2029, with coupons on February 15 and August 15, unless the example says otherwise.

### Example 1: Next Coupon Date

```excel
=COUPNCD(DATE(2027,2,10),DATE(2029,8,15),2,1)
```

**Result:** `2027-02-15`

The coupon dates are fixed by the maturity date, so the first coupon after February 10, 2027, falls on February 15, 2027.

### Example 2: A Quarterly Bond

```excel
=COUPNCD(DATE(2027,5,20),DATE(2028,11,15),4,1)
```

**Result:** `2027-08-15`

The quarterly coupon dates are May 15, August 15, November 15 and February 15. Settlement on May 20 falls after May 15, so the next coupon is August 15.

### Example 3: Days Until the Next Coupon

```excel
=COUPNCD(DATE(2027,2,10),DATE(2029,8,15),2,1)-DATE(2027,2,10)
```

**Result:** `5`

Subtracting the settlement date from the next coupon date gives the calendar days remaining. The result matches COUPDAYSNC for the same inputs on the actual/actual basis.

### Example 4: The Next Coupon on the 30/360 Basis

```excel
=COUPNCD(DATE(2027,3,3),DATE(2029,9,15),4,0)
```

**Result:** `2027-03-15`

For a quarterly bond with coupons on the 15th of March, June, September and December, a March 3 settlement has its next coupon on March 15.

## Story Problems

The problems use this bond table. Enter each date as a true date value.

| Bond | Settlement | Maturity | Frequency | Basis |
| --- | --- | --- | --- | --- |
| Quill | 2026-10-14 | 2031-04-15 | 2 | 1 |
| Ridge | 2027-03-03 | 2029-09-15 | 4 | 0 |
| Tarn | 2026-12-01 | 2027-12-15 | 1 | 1 |

### Problem 1: First Cash Receipt from the Ridge Bond

A treasury analyst buys the Ridge bond on March 3, 2027. The analyst needs the date of the first coupon payment to plan the cash receipt.

**Task:** Find the next coupon date after settlement for Ridge, which is in row 3.

**Solution:**

```excel
=COUPNCD(B3,C3,D3,E3)
```

**Answer:** `2027-03-15`, because the Ridge bond pays quarterly on the 15th of March, June, September and December.

### Problem 2: Annual Note Settled Before Its Coupon

An insurer holds the Tarn note, which pays once a year on December 15. The insurer buys the note on December 1, 2026, and wants to know when the next payment comes.

**Task:** Find the next coupon date after settlement for Tarn, which is in row 4.

**Solution:**

```excel
=COUPNCD(B4,C4,D4,E4)
```

**Answer:** `2026-12-15`, because the coupon falls two weeks after the settlement date.

<!-- Image 2: Coupon Forecast Table. See Images/Financial/COUPNCD.md -->

## Use Cases

### Bond Coupon Schedules

**Scenario:** A finance team lists the next coupon date for every bond in a portfolio so that each holding has a dated entry.

```excel
=COUPNCD(SettleDate,Maturity,Freq,Basis)
```

**Why It Works:** Each row holds its own maturity and frequency, so one formula covers the whole list. Copy it down the rows and format the column as a date.

### Bond Trade Settlement

**Scenario:** A trader confirms to the buyer when the first coupon will be paid after the trade settles.

```excel
=COUPNCD(Settle,Maturity,Freq,Basis)
```

**Why It Works:** The confirmation shows the date, so the buyer knows when the first cash payment arrives. Use the same basis as the rest of the confirmation.

### Coupon Payment Forecasting

**Scenario:** An operations team forecasts how much cash the portfolio will receive in the next month.

```excel
=IF(COUPNCD(Settle,Maturity,Freq,Basis)<=DATE(2026,12,31),Coupon,0)
```

**Why It Works:** The test adds a coupon only when its date falls within the forecast window. Replace the fixed date with a cell reference to roll the forecast forward.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `frequency` is not 1, 2 or 4. | Enter the number of coupons per year. |
| `#NUM!` | `settlement` is on or after `maturity`. | Check the settlement and maturity dates. |
| `#NUM!` | `basis` is below 0 or above 4. | Use a basis code from 0 to 4. |
| `#VALUE!` | A date is stored as text. | Enter the dates with `DATE` or convert the text to date values. |
| A number such as `46433` appears | The cell is formatted as a number, not a date. | Apply a date format to the cell. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365 and Excel for the web | The optional argument is named `basis`. |
| Google Sheets | Available | The same four arguments, with the optional argument named `day_count_convention`. The day count options match Excel. |

## Tips and Best Practices

- Enter every date with `DATE` or as a reference to a date cell, so the function never receives text.
- Format the result cell as a date before you copy or chart it.
- Compare COUPPCD and COUPNCD for the same bond to find the full coupon period in dates.
- Use the same frequency across the holding list, and check any bond whose coupons do not follow that frequency.
- For a bond maturing at month end, check the coupon date in the result against the bond's terms, because end of month rules can move the date.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUPDAYBS](COUPDAYBS.md) | Days from the last coupon to settlement, measured back from the previous coupon date. |
| [COUPDAYS](COUPDAYS.md) | Days in the coupon period between the previous and next coupon dates. |
| [COUPDAYSNC](COUPDAYSNC.md) | Days from settlement to this next coupon date. |
| [COUPNUM](COUPNUM.md) | The number of coupons left from settlement to maturity. |
| [COUPPCD](COUPPCD.md) | The coupon date before settlement, the partner of this function. |

## Official Documentation

- [Microsoft Support: COUPNCD function](https://support.microsoft.com/en-us/excel/functions/coupncd-function)
- [Google Docs Editors Help: COUPNCD](https://support.google.com/docs/answer/3093157)
