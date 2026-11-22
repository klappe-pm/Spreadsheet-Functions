---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Date Calculation
use-case:
  - Accrued Interest Split
  - Bond Trade Settlement
  - Coupon Reminder Dates
related:
  - COUPDAYBS
  - COUPDAYS
  - COUPNCD
  - COUPNUM
  - COUPPCD
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/coupdaysnc-function
  - https://support.google.com/docs/answer/3093156
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Days To Next Coupon
  - Days Until Next Coupon
tags:
  - bond-math
  - coupon-period
  - day-count
  - excel
  - sheets
---

# COUPDAYSNC

## Description

**COUPDAYSNC** returns the number of days from the settlement date to the next coupon date. It answers the question "how long until the buyer receives the next coupon payment?" The count is measured within the coupon period that contains the settlement date, so it shrinks as the trade gets closer to the next payment.

The buyer earns the part of the next coupon that falls after settlement. COUPDAYSNC gives the length of that part in days, and dividing it by the total days in the coupon period (COUPDAYS) gives the buyer's share of the coupon. Bond pricing calculations also use this count, because they need to know how much of the coupon period is still to come.

COUPDAYSNC is the forward-looking partner of COUPDAYBS. On the 30/360 and actual/actual bases, the two add up to COUPDAYS. Use COUPDAYSNC for reminder dates, for the buyer's share of a coupon, and for any calculation that needs the remaining part of the current period.

## Syntax

```excel
=COUPDAYSNC(settlement, maturity, frequency, [basis])
```

<!-- Image 1: Days Remaining to the Next Coupon. See Images/Financial/COUPDAYSNC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the bond. It must fall before `maturity`. |
| `maturity` | Yes | The date the bond expires and repays its principal. It must fall after `settlement`. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual or `4` for quarterly. |
| `basis` | No | The day count basis. `0` or omitted uses US (NASD) 30/360. `1` uses actual/actual, `2` actual/360, `3` actual/365 and `4` European 30/360. |

### Return Value

A number of days: the count from the settlement date to the next coupon date. The function returns `#VALUE!` when `settlement` or `maturity` is not a valid date, and `#NUM!` when `frequency` is not 1, 2 or 4, `basis` is outside 0 to 4, or `settlement` falls on or after `maturity`.

## Examples

All examples use a bond that settles on February 10, 2027, and matures on August 15, 2029, with coupons on February 15 and August 15. The quarterly examples use a bond that settles on May 20, 2027, and matures on November 15, 2028.

### Example 1: Days to the Next Coupon

```excel
=COUPDAYSNC(DATE(2027,2,10),DATE(2029,8,15),2,1)
```

**Result:** `5`

The next coupon falls on February 15, 2027, five days after settlement.

### Example 2: A Quarterly Bond on a 30/360 Basis

```excel
=COUPDAYSNC(DATE(2027,5,20),DATE(2028,11,15),4,0)
```

**Result:** `85`

On 30/360, the days from May 20 to the August 15 coupon count as 85.

### Example 3: Buyer's Share of the Next Coupon

```excel
=COUPDAYSNC(DATE(2027,5,20),DATE(2028,11,15),4,1)/COUPDAYS(DATE(2027,5,20),DATE(2028,11,15),4,1)
```

**Result:** `0.9457`

The buyer earns 87 of the 92 days in the coupon period, which is about 95% of the next quarterly coupon.

### Example 4: A Quarterly Bond Close to Its Coupon

```excel
=COUPDAYSNC(DATE(2027,3,3),DATE(2029,9,15),4,0)
```

**Result:** `12`

With settlement on March 3, 2027, and the next coupon on March 15, 2027, 12 days remain on the 30/360 basis.

## Story Problems

The problems use this bond table. Enter each date as a true date value.

| Bond | Settlement | Maturity | Frequency | Basis |
| --- | --- | --- | --- | --- |
| Quill | 2026-10-14 | 2031-04-15 | 2 | 1 |
| Ridge | 2027-03-03 | 2029-09-15 | 4 | 0 |
| Tarn | 2026-12-01 | 2027-12-15 | 1 | 1 |

### Problem 1: Days to the Next Ridge Coupon

A fund manager wants to know how many days remain before the Ridge bond pays its next coupon. The bond pays quarterly, and the trade settles on March 3, 2027.

**Task:** Find the days from settlement to the next coupon for Ridge, which is in row 3.

**Solution:**

```excel
=COUPDAYSNC(B3,C3,D3,E3)
```

**Answer:** `12`, because the next coupon falls on March 15, 2027, 12 days after the settlement date on the 30/360 basis in the table.

### Problem 2: Almost Due Quill Coupon

A broker sells the Quill bond on October 14, 2026, one day before its next semiannual coupon on October 15.

**Task:** Find the days from settlement to the next coupon for Quill, which is in row 2.

**Solution:**

```excel
=COUPDAYSNC(B2,C2,D2,E2)
```

**Answer:** `1`, because October 15, 2026, is one day after the settlement date. The seller has earned 182 of the 183 days in the period, so the buyer's share of the coupon is very small.

<!-- Image 2: Buyer's Share Calculation. See Images/Financial/COUPDAYSNC.md -->

## Use Cases

### Accrued Interest Split

**Scenario:** A broker shows the buyer's share of the next coupon on a trade confirmation, alongside the seller's share.

```excel
=COUPDAYSNC(Settle,Maturity,Freq,Basis)/COUPDAYS(Settle,Maturity,Freq,Basis)
```

**Why It Works:** The buyer's share and the seller's share (COUPDAYBS divided by COUPDAYS) together cover the whole coupon. Use the same basis for both so the confirmation balances.

### Coupon Reminder Dates

**Scenario:** An operations team flags holdings whose next coupon is within 10 days so that cash receipts can be forecast.

```excel
=IF(COUPDAYSNC(DATE(2026,11,22),Maturity,Freq,Basis)<=10,"Coupon Due Soon","Later")
```

**Why It Works:** The `IF` test turns the day count into a simple flag. Replace the fixed settlement date with a cell reference when the list is updated each day.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `frequency` is not 1, 2 or 4. | Enter the number of coupons per year. |
| `#NUM!` | `settlement` is on or after `maturity`. | Check the settlement and maturity dates. |
| `#NUM!` | `basis` is below 0 or above 4. | Use a basis code from 0 to 4. |
| `#VALUE!` | A date is stored as text. | Enter the dates with `DATE` or convert the text to date values. |
| Result is larger than expected | The maturity or frequency does not match the bond's coupon schedule. | Check the maturity date and frequency against the bond's terms. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365 and Excel for the web | The optional argument is named `basis`. |
| Google Sheets | Available | The same four arguments, with the optional argument named `day_count_convention`. The day count options match Excel. |

## Tips and Best Practices

- Enter every date with `DATE` or as a reference to a date cell, so the function never receives text.
- Use the same basis as COUPDAYBS and COUPDAYS when you split a coupon, so the parts stay consistent.
- Check the coupon schedule when a result looks too large, because the count always runs to the next coupon date.
- Use COUPDAYSNC for reminders and for the buyer's share, and use COUPDAYBS for the seller's share.
- Remember that the result is a day count. Multiply by the coupon payment and divide by the period days to get money.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUPDAYBS](COUPDAYBS.md) | The days from the last coupon to settlement, the seller's part of the period. |
| [COUPDAYS](COUPDAYS.md) | The total days in the coupon period, the denominator for both shares. |
| [COUPNCD](COUPNCD.md) | The next coupon date, the date this function counts toward. |
| [COUPNUM](COUPNUM.md) | The number of coupons left until maturity. |
| [COUPPCD](COUPPCD.md) | The last coupon date before settlement. |

## Official Documentation

- [Microsoft Support: COUPDAYSNC function](https://support.microsoft.com/en-us/excel/functions/coupdaysnc-function)
- [Google Docs Editors Help: COUPDAYSNC](https://support.google.com/docs/answer/3093156)
