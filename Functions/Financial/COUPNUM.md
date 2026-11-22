---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Counting
use-case:
  - Bond Coupon Schedules
  - Pension Fund Holdings
  - Remaining Coupon Counts
related:
  - COUPDAYS
  - COUPDAYSNC
  - COUPNCD
  - COUPPCD
  - PRICE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/coupnum-function
  - https://support.google.com/docs/answer/3093208
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Coupons Left To Maturity
  - Remaining Coupon Count
tags:
  - bond-math
  - counting
  - coupon-period
  - excel
  - sheets
---

# COUPNUM

## Description

**COUPNUM** returns the number of coupon payments that fall between the settlement date and the maturity date. The count includes the coupon paid on the maturity date, because that payment is still owed to the holder when the trade settles. For a semiannual bond with about ten years left, COUPNUM returns about 20.

Use COUPNUM to count the cash receipts left in a holding, to check a coupon schedule, or to decide how many periods a yield or price calculation must cover. Microsoft describes the result as rounded up to the nearest whole coupon, so a partial period still counts as one payment.

COUPNUM does not return a date or an amount. To find when the next payment arrives, use COUPNCD. To find the amount of each payment, multiply the coupon rate by the par value and divide by the frequency.

## Syntax

```excel
=COUPNUM(settlement, maturity, frequency, [basis])
```

<!-- Image 1: Remaining Coupon Count. See Images/Financial/COUPNUM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the bond. It must fall before `maturity`. |
| `maturity` | Yes | The date the bond expires and repays its principal. It must fall after `settlement`. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual or `4` for quarterly. |
| `basis` | No | The day count basis. `0` or omitted uses US (NASD) 30/360. `1` uses actual/actual, `2` actual/360, `3` actual/365 and `4` European 30/360. |

### Return Value

A whole number: the count of coupon payments from settlement to maturity, including the payment on the maturity date. The function returns `#VALUE!` when `settlement` or `maturity` is not a valid date, and `#NUM!` when `frequency` is not 1, 2 or 4, `basis` is outside 0 to 4, or `settlement` falls on or after `maturity`.

## Examples

All examples use a bond that settles on February 10, 2027, and matures on August 15, 2029, with coupons on February 15 and August 15, unless the example says otherwise.

### Example 1: Coupons Left on a Semiannual Bond

```excel
=COUPNUM(DATE(2027,2,10),DATE(2029,8,15),2,1)
```

**Result:** `6`

The payments are February 15, 2027, August 15, 2027, February 15, 2028, August 15, 2028, February 15, 2029 and August 15, 2029 (the maturity payment).

### Example 2: A Quarterly Bond on a 30/360 Basis

```excel
=COUPNUM(DATE(2027,3,3),DATE(2029,9,15),4,0)
```

**Result:** `11`

Quarterly payments run from March 15, 2027, through September 15, 2029, which is 11 payments on the 30/360 basis.

### Example 3: An Annual Note

```excel
=COUPNUM(DATE(2026,12,1),DATE(2027,12,15),1,1)
```

**Result:** `2`

The two remaining payments are December 15, 2026, and December 15, 2027.

### Example 4: Flagging Long Holdings

```excel
=IF(COUPNUM(DATE(2027,2,10),DATE(2029,8,15),2,1)>4,"Long Hold","Short Hold")
```

**Result:** `Long Hold`

The count of 6 is above the threshold of 4, so the formula flags the holding. Change the threshold to match your own review rule.

## Story Problems

The problems use this bond table. Enter each date as a true date value.

| Bond | Settlement | Maturity | Frequency | Basis |
| --- | --- | --- | --- | --- |
| Quill | 2026-10-14 | 2031-04-15 | 2 | 1 |
| Ridge | 2027-03-03 | 2029-09-15 | 4 | 0 |
| Tarn | 2026-12-01 | 2027-12-15 | 1 | 1 |

### Problem 1: Remaining Payments on the Ridge Bond

A pension fund holds the Ridge bond and wants to know how many quarterly coupons it still has to receive. The fund buys the bond on March 3, 2027, and the bond matures on September 15, 2029.

**Task:** Count the coupon payments left from settlement to maturity for Ridge, which is in row 3.

**Solution:**

```excel
=COUPNUM(B3,C3,D3,E3)
```

**Answer:** `11`, because the quarterly payments run from March 15, 2027, to September 15, 2029, including the final payment.

### Problem 2: Two Payments Left on the Tarn Note

A small charity holds the Tarn note, which pays once a year. The charity settles on December 1, 2026, and the note matures on December 15, 2027.

**Task:** Count the coupon payments left for Tarn, which is in row 4.

**Solution:**

```excel
=COUPNUM(B4,C4,D4,E4)
```

**Answer:** `2`, because the payments fall on December 15, 2026, and December 15, 2027.

<!-- Image 2: Coupon Schedule Table. See Images/Financial/COUPNUM.md -->

## Use Cases

### Bond Coupon Schedules

**Scenario:** A treasury team lists how many payments each bond still owes so that the cash forecast covers every holding.

```excel
=COUPNUM(SettleDate,Maturity,Freq,Basis)
```

**Why It Works:** The count gives the number of rows a schedule needs for each bond. Store the frequency and basis in the same table so one formula covers the portfolio.

### Pension Fund Holdings

**Scenario:** A pension fund reviews how many coupons remain on each bond it holds before it decides whether to sell.

```excel
=COUPNUM(B2,C2,D2,E2)
```

**Why It Works:** A holding with few payments left has less future income to protect, which can inform the sale decision. Read the count together with the yield, not on its own.

### Remaining Coupon Counts

**Scenario:** An analyst wants a quick summary of the number of payments left across a set of notes that settle on the same day.

```excel
=COUPNUM(DATE(2026,12,1),Maturity,Freq,Basis)
```

**Why It Works:** Using one fixed settlement date makes the counts comparable across notes. Replace the date with a cell reference when the settlement day changes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `frequency` is not 1, 2 or 4. | Enter the number of coupons per year. |
| `#NUM!` | `settlement` is on or after `maturity`. | Check the settlement and maturity dates. |
| `#NUM!` | `basis` is below 0 or above 4. | Use a basis code from 0 to 4. |
| `#VALUE!` | A date is stored as text. | Enter the dates with `DATE` or convert the text to date values. |
| Count is one higher than expected | The count includes the payment on the maturity date. | Subtract 1 only when your process excludes the final payment. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365 and Excel for the web | The optional argument is named `basis`. |
| Google Sheets | Available | The same four arguments, with the optional argument named `day_count_convention`. The day count options match Excel. |

## Tips and Best Practices

- Enter every date with `DATE` or as a reference to a date cell, so the function never receives text.
- Use the same frequency for each bond you compare, because a quarterly bond has four times as many payments as an annual one over the same years.
- Read the count together with COUPNCD when you need both the number of payments and the next date.
- Remember that the count includes the maturity payment, so reconcile it with the bond's schedule before you post a receivable.
- Keep the basis consistent across a portfolio so the counts match the other coupon day functions.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUPDAYS](COUPDAYS.md) | The length of the current coupon period, measured in days. |
| [COUPDAYSNC](COUPDAYSNC.md) | The days from settlement to the next coupon, the day count for the first payment. |
| [COUPNCD](COUPNCD.md) | The date of the next coupon, which is the first of the payments this function counts. |
| [COUPPCD](COUPPCD.md) | The coupon date before settlement, the last payment already made. |
| [PRICE](PRICE.md) | Calculates a bond price from its yield, using the same settlement, maturity and frequency inputs. |

## Official Documentation

- [Microsoft Support: COUPNUM function](https://support.microsoft.com/en-us/excel/functions/coupnum-function)
- [Google Docs Editors Help: COUPNUM](https://support.google.com/docs/answer/3093208)
