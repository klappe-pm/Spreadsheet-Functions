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
  - Bond Trade Settlement
related:
  - ACCRINT
  - COUPDAYS
  - COUPDAYSNC
  - COUPNCD
  - COUPPCD
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/coupdaybs-function
  - https://support.google.com/docs/answer/3093154
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Coupon Days Before Settlement
  - Days Since Last Coupon
tags:
  - bond-math
  - coupon-period
  - day-count
  - excel
  - sheets
---

# COUPDAYBS

## Description

**COUPDAYBS** returns the number of days from the start of the current coupon period, which is the last coupon date before settlement, to the settlement date. A bond that pays interest twice a year has a coupon period of about six months. COUPDAYBS tells you how far into that period the trade falls.

The days counted by COUPDAYBS are the days of interest the seller has earned and the buyer will pay for when the bond settles. Divide the result by the total days in the coupon period (COUPDAYS) to get the share of the next coupon that has accrued. Multiply that share by the coupon payment to get the accrued interest.

Use COUPDAYBS when you need the day count for a bond's accrued interest or for a coupon schedule. Its partner, COUPDAYSNC, counts the days remaining until the next coupon. On the 30/360 and actual/actual bases, the two add up to the full coupon period. COUPDAYBS counts from the last coupon date rather than the issue date, so the result does not depend on when the bond was first issued.

## Syntax

```excel
=COUPDAYBS(settlement, maturity, frequency, [basis])
```

<!-- Image 1: Coupon Period Timeline. See Images/Financial/COUPDAYBS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the bond. It must fall before `maturity`. |
| `maturity` | Yes | The date the bond expires and repays its principal. It must fall after `settlement`. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual or `4` for quarterly. |
| `basis` | No | The day count basis. `0` or omitted uses US (NASD) 30/360. `1` uses actual/actual, `2` actual/360, `3` actual/365 and `4` European 30/360. |

### Return Value

A number of days: the count from the last coupon date before settlement to the settlement date. The function returns `#VALUE!` when `settlement` or `maturity` is not a valid date, and `#NUM!` when `frequency` is not 1, 2 or 4, `basis` is outside 0 to 4, or `settlement` falls on or after `maturity`.

## Examples

All examples use a bond that settles on February 10, 2027, and matures on August 15, 2029, with coupons on February 15 and August 15. The quarterly example uses a bond that settles on May 20, 2027, and matures on November 15, 2028.

### Example 1: Days Since the Last Coupon

```excel
=COUPDAYBS(DATE(2027,2,10),DATE(2029,8,15),2,1)
```

**Result:** `179`

The last coupon date before settlement is August 15, 2026. Counting actual days from that date to February 10, 2027 gives 179.

### Example 2: The Same Bond on a 30/360 Basis

```excel
=COUPDAYBS(DATE(2027,2,10),DATE(2029,8,15),2,0)
```

**Result:** `175`

The 30/360 basis counts each month as 30 days, so the result is 4 days lower than the actual count for this period.

### Example 3: Share of the Coupon That Has Accrued

```excel
=COUPDAYBS(DATE(2027,2,10),DATE(2029,8,15),2,1)/COUPDAYS(DATE(2027,2,10),DATE(2029,8,15),2,1)
```

**Result:** `0.9728`

Dividing 179 days by the 184 days in the coupon period shows that about 97% of the coupon has accrued. Multiply this share by the coupon payment to get the accrued interest.

<!-- Image 2: Accrued Share Calculation. See Images/Financial/COUPDAYBS.md -->

### Example 4: A Quarterly Bond

```excel
=COUPDAYBS(DATE(2027,5,20),DATE(2028,11,15),4,1)
```

**Result:** `5`

A quarterly bond with a coupon date on May 15 settles five days after its last coupon, so only 5 days have accrued.

## Story Problems

The problems use this bond table. Enter each date as a true date value.

| Bond | Settlement | Maturity | Frequency | Basis |
| --- | --- | --- | --- | --- |
| Quill | 2026-10-14 | 2031-04-15 | 2 | 1 |
| Ridge | 2027-03-03 | 2029-09-15 | 4 | 0 |
| Tarn | 2026-12-01 | 2027-12-15 | 1 | 1 |

### Problem 1: Accrued Days on the Quill Bond

A fund manager sells the Quill bond. The bond pays semiannual coupons on April 15 and October 15, and the trade settles on October 14, 2026.

**Task:** Find the number of days from the last coupon to the settlement date for Quill, which is in row 2.

**Solution:**

```excel
=COUPDAYBS(B2,C2,D2,E2)
```

**Answer:** `182`, because the last coupon was April 15, 2026, and 182 actual days pass before October 14, 2026.

### Problem 2: Accrued Share on the Ridge Bond

A trader quotes the Ridge bond, which pays quarterly coupons and settles on March 3, 2027. The trader wants the accrued share of the current coupon as a decimal, using the 30/360 basis in the table.

**Task:** Divide the days from the last coupon to settlement by the days in the coupon period for Ridge, which is in row 3. Round the result to four decimals.

**Solution:**

```excel
=ROUND(COUPDAYBS(B3,C3,D3,E3)/COUPDAYS(B3,C3,D3,E3),4)
```

**Answer:** `0.8667`, because 78 of the 90 days in the coupon period have passed on the 30/360 basis.

<!-- Image 3: Bond Table and Accrued Share. See Images/Financial/COUPDAYBS.md -->

## Use Cases

### Accrued Interest Split

**Scenario:** A broker needs to show the seller's share of the next coupon on a trade confirmation.

```excel
=COUPDAYBS(Settle,Maturity,Freq,Basis)/COUPDAYS(Settle,Maturity,Freq,Basis)
```

**Why It Works:** The ratio of days gives the fraction of the coupon that belongs to the seller. Use the same basis as the bond's terms, or the split will not match the confirmation.

### Bond Coupon Schedules

**Scenario:** A finance team builds a schedule of accrued interest for every bond in a portfolio that settles at the end of the month.

```excel
=COUPDAYBS(DATE(2026,11,30),Maturity,Freq,1)
```

**Why It Works:** Each bond has its own maturity and frequency, so keep those in columns and point the formula at them. Copy the formula down the list rather than retyping it for each holding.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `frequency` is not 1, 2 or 4. | Enter the number of coupons per year. |
| `#NUM!` | `settlement` is on or after `maturity`. | Check that the bond has not already matured on the settlement date. |
| `#NUM!` | `basis` is below 0 or above 4. | Use a basis code from 0 to 4. |
| `#VALUE!` | A date is stored as text. | Enter the dates with `DATE` or convert the text to date values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365 and Excel for the web | The optional argument is named `basis`. |
| Google Sheets | Available | The same four arguments, with the optional argument named `day_count_convention`. The day count options match Excel. |

## Tips and Best Practices

- Enter every date with `DATE` or as a reference to a date cell, so the function never receives text.
- Use the same basis as the bond's terms in every formula that works with the same bond.
- Pair COUPDAYBS with COUPDAYS and COUPDAYSNC, because on the 30/360 and actual/actual bases the two parts add up to the full coupon period.
- Remember that the result is a day count, not an amount of money. Multiply by the coupon payment to get accrued interest.
- Check the frequency first, because a wrong frequency changes the coupon period and gives a wrong day count.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ACCRINT](ACCRINT.md) | Calculates accrued interest in money terms for a periodic coupon bond. |
| [COUPDAYS](COUPDAYS.md) | The total days in the coupon period, the denominator for the accrued share. |
| [COUPDAYSNC](COUPDAYSNC.md) | The days from settlement to the next coupon, the other half of the coupon period. |
| [COUPNCD](COUPNCD.md) | The next coupon date after settlement. |
| [COUPPCD](COUPPCD.md) | The last coupon date before settlement, the start date for this count. |

## Official Documentation

- [Microsoft Support: COUPDAYBS function](https://support.microsoft.com/en-us/excel/functions/coupdaybs-function)
- [Google Docs Editors Help: COUPDAYBS](https://support.google.com/docs/answer/3093154)
