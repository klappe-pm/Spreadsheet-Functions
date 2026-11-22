---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Date Calculation
use-case:
  - Accrued Interest Split
  - Bond Coupon Schedules
  - Pension Fund Holdings
related:
  - ACCRINT
  - COUPDAYBS
  - COUPDAYS
  - COUPNCD
  - COUPNUM
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/couppcd-function
  - https://support.google.com/docs/answer/3093210
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Last Coupon Date
  - Previous Interest Payment Date
tags:
  - bond-math
  - coupon-period
  - day-count
  - excel
  - sheets
---

# COUPPCD

## Description

**COUPPCD** returns the date of the last coupon payment before the settlement date. If a bond settles on February 10 and pays coupons on February 15 and August 15, COUPPCD returns the previous August 15. Like COUPNCD, the coupon dates are set by the maturity date and the frequency, so the result does not depend on when the bond was issued.

The date from COUPPCD marks the start of the interest that has accrued since the last payment. Accrued interest runs from this date to the settlement date, and the days in that span are what COUPDAYBS counts. Use COUPPCD to show a seller where the current interest period began, or to build a list of coupon dates for a portfolio.

The result is a date. Format the cell as a date, or the formula displays a serial number such as 46249.

## Syntax

```excel
=COUPPCD(settlement, maturity, frequency, [basis])
```

<!-- Image 1: Last Coupon Date Before Settlement. See Images/Financial/COUPPCD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the bond. It must fall before `maturity`. |
| `maturity` | Yes | The date the bond expires and repays its principal. It must fall after `settlement`. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual or `4` for quarterly. |
| `basis` | No | The day count basis. `0` or omitted uses US (NASD) 30/360. `1` uses actual/actual, `2` actual/360, `3` actual/365 and `4` European 30/360. |

### Return Value

A date serial: the last coupon date on or before the settlement date, in the chain of coupon dates set by `maturity` and `frequency`. The function returns `#VALUE!` when `settlement` or `maturity` is not a valid date, and `#NUM!` when `frequency` is not 1, 2 or 4, `basis` is outside 0 to 4, or `settlement` falls on or after `maturity`.

## Examples

All examples use a bond that settles on February 10, 2027, and matures on August 15, 2029, with coupons on February 15 and August 15, unless the example says otherwise.

### Example 1: Last Coupon Before Settlement

```excel
=COUPPCD(DATE(2027,2,10),DATE(2029,8,15),2,1)
```

**Result:** `2026-08-15`

The coupon on February 15, 2027, has not yet been paid on February 10, so the last one was August 15, 2026.

### Example 2: A Quarterly Bond

```excel
=COUPPCD(DATE(2027,5,20),DATE(2028,11,15),4,1)
```

**Result:** `2027-05-15`

The quarterly coupon dates are February 15, May 15, August 15 and November 15. The May 15 payment came five days before settlement on May 20.

### Example 3: The Same Bond on a 30/360 Basis

```excel
=COUPPCD(DATE(2027,3,3),DATE(2029,9,15),4,0)
```

**Result:** `2026-12-15`

The quarterly coupon on December 15, 2026, is the last one before the March 3, 2027 settlement, and the 30/360 basis does not change the date.

### Example 4: Full Length of the Coupon Period

```excel
=COUPNCD(DATE(2027,2,10),DATE(2029,8,15),2,1)-COUPPCD(DATE(2027,2,10),DATE(2029,8,15),2,1)
```

**Result:** `184`

Subtracting the last coupon date from the next one gives the length of the coupon period in actual days, which matches COUPDAYS for the same inputs.

## Story Problems

The problems use this bond table. Enter each date as a true date value.

| Bond | Settlement | Maturity | Frequency | Basis |
| --- | --- | --- | --- | --- |
| Quill | 2026-10-14 | 2031-04-15 | 2 | 1 |
| Ridge | 2027-03-03 | 2029-09-15 | 4 | 0 |
| Tarn | 2026-12-01 | 2027-12-15 | 1 | 1 |

### Problem 1: Start of Interest for the Quill Bond

A seller of the Quill bond must show the buyer the date from which interest has built up. The bond pays semiannual coupons on April 15 and October 15, and the trade settles on October 14, 2026.

**Task:** Find the last coupon date before settlement for Quill, which is in row 2.

**Solution:**

```excel
=COUPPCD(B2,C2,D2,E2)
```

**Answer:** `2026-04-15`, because the October 15 payment has not yet been made on the settlement date, so interest runs from April 15.

### Problem 2: Annual Coupon Before the Tarn Settlement

A charity buys the Tarn note on December 1, 2026. The note pays each year on December 15, and the charity's accountant needs the date of the last payment before the purchase.

**Task:** Find the last coupon date before settlement for Tarn, which is in row 4.

**Solution:**

```excel
=COUPPCD(B4,C4,D4,E4)
```

**Answer:** `2025-12-15`, because the December 15, 2026, payment falls after the settlement date.

<!-- Image 2: Coupon Date Table. See Images/Financial/COUPPCD.md -->

## Use Cases

### Accrued Interest Split

**Scenario:** A broker needs the start date of the accrual period to show the seller's interest on a trade confirmation.

```excel
=COUPPCD(Settle,Maturity,Freq,Basis)
```

**Why It Works:** The date marks where the seller's accrued interest begins. Pair it with COUPNCD to show the full coupon period on the same confirmation.

### Bond Coupon Schedules

**Scenario:** An operations team lists the last and next coupon dates for each bond in a portfolio.

```excel
=COUPPCD(SettleDate,Maturity,Freq,Basis)
```

**Why It Works:** Each row holds its own maturity and frequency, so one formula covers the whole list. Copy the formula down and format the column as a date.

### Pension Fund Holdings

**Scenario:** A pension fund reports the date of the last coupon it received on each holding at the end of the quarter.

```excel
=COUPPCD(QuarterEnd,Maturity,Freq,Basis)
```

**Why It Works:** Using the quarter end as the settlement date returns the most recent coupon date before that day. Confirm the result against the cash receipts ledger.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `frequency` is not 1, 2 or 4. | Enter the number of coupons per year. |
| `#NUM!` | `settlement` is on or after `maturity`. | Check the settlement and maturity dates. |
| `#NUM!` | `basis` is below 0 or above 4. | Use a basis code from 0 to 4. |
| `#VALUE!` | A date is stored as text. | Enter the dates with `DATE` or convert the text to date values. |
| A number such as `46249` appears | The cell is formatted as a number, not a date. | Apply a date format to the cell. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365 and Excel for the web | The optional argument is named `basis`. |
| Google Sheets | Available | The same four arguments, with the optional argument named `day_count_convention`. The day count options match Excel. |

## Tips and Best Practices

- Enter every date with `DATE` or as a reference to a date cell, so the function never receives text.
- Format the result cell as a date before you copy, chart or send it.
- Use COUPPCD and COUPNCD together to show the full coupon period in dates.
- Keep the frequency and basis the same across all the bonds you compare on one report.
- When the settlement date falls exactly on a coupon date, check the result against the bond's terms, because the convention for that day matters.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ACCRINT](ACCRINT.md) | Calculates the accrued interest in money terms, measured from the coupon date this function returns. |
| [COUPDAYBS](COUPDAYBS.md) | Counts the days from this date to settlement. |
| [COUPDAYS](COUPDAYS.md) | The length of the coupon period that starts on this date. |
| [COUPNCD](COUPNCD.md) | The next coupon date, the partner of this function. |
| [COUPNUM](COUPNUM.md) | The number of coupons still to be paid after this date. |

## Official Documentation

- [Microsoft Support: COUPPCD function](https://support.microsoft.com/en-us/excel/functions/couppcd-function)
- [Google Docs Editors Help: COUPPCD](https://support.google.com/docs/answer/3093210)
