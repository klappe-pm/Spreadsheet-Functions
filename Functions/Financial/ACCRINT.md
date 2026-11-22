---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Bond Interest Accrual
  - Bond Trade Settlement
  - Investment Portfolio Reporting
related:
  - ACCRINTM
  - COUPDAYBS
  - COUPPCD
  - PRICE
  - YIELD
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/accrint-function
  - https://support.google.com/docs/answer/3093200
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Accrued Coupon Interest
  - Accrued Interest Periodic
tags:
  - accrued-interest
  - bond-math
  - day-count
  - excel
  - sheets
---

# ACCRINT

## Description

**ACCRINT** returns the interest that has built up on a security that pays interest on a regular schedule, such as a semiannual corporate bond. The interest accrues from the last interest date (or the issue date, for the first period) up to the settlement date, which is the day the buyer takes delivery. When a bond changes hands between coupon dates, the buyer normally pays the seller this accrued interest on top of the price.

Use ACCRINT when the security pays periodic coupons. If the security pays all of its interest at maturity, use ACCRINTM instead. ACCRINT also handles an odd first period, where the first interest date is not one full coupon period after the issue date.

The two platforms name their arguments differently. Microsoft Excel takes the full par amount, such as 1000, and offers an optional `calc_method` argument. Google Sheets calls the same input `redemption` and describes it as the redemption amount per 100 of face value, so enter 100 for a bond that redeems at par. Sheets does not offer `calc_method`.

## Syntax

```excel
=ACCRINT(issue, first_interest, settlement, rate, par, frequency, [basis], [calc_method])
```

<!-- Image 1: Accrued Interest Timeline. See Images/Financial/ACCRINT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `issue` | Yes | The date the security was first issued. Enter it with `DATE` or as a date value. |
| `first_interest` | Yes | The first coupon payment date. |
| `settlement` | Yes | The date the security is delivered to the buyer. It must fall after `issue`. |
| `rate` | Yes | The annual coupon rate as a decimal, for example `0.06` for 6%. Must be greater than 0. |
| `par` | Yes | The par (face) value of the security, for example `1000`. Must be greater than 0. The Microsoft article lists this argument as required. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual or `4` for quarterly. |
| `basis` | No | The day count basis. `0` or omitted uses US (NASD) 30/360. `1` uses actual/actual, `2` actual/360, `3` actual/365 and `4` European 30/360. |
| `calc_method` | No | Applies when `settlement` falls after `first_interest`. `TRUE` (default) returns interest from `issue` to `settlement`. `FALSE` returns interest from `first_interest` to `settlement`. |

### Return Value

A number: the accrued interest, in the same currency unit as `par`. The function returns `#VALUE!` when a date is not valid, and `#NUM!` when `rate` or `par` is zero or negative, `frequency` is not 1, 2 or 4, `basis` is outside 0 to 4, or `issue` falls on or after `settlement`.

## Examples

All examples use a bond issued on January 15, 2026, with its first coupon on July 15, 2026, paying twice a year.

### Example 1: Basic Accrual on a Mid-Period Sale

```excel
=ACCRINT(DATE(2026,1,15),DATE(2026,7,15),DATE(2026,5,1),0.06,1000,2,0)
```

**Result:** `17.6667`

The buyer takes delivery on May 1, 2026, so 106 days of 30/360 interest have built up on each 1,000 of par (1,000 x 6% x 106 / 360). The result is shown unrounded here.

### Example 2: A Larger Position

```excel
=ACCRINT(DATE(2026,1,15),DATE(2026,7,15),DATE(2026,5,1),0.075,5000,2,0)
```

**Result:** `110.4167`

The same dates with a 7.5% rate on 5,000 of par. Accrued interest scales with both par and rate. Here par is 5 times larger and the rate is 1.25 times larger, so the result is 6.25 times Example 1 (17.6667 x 6.25).

<!-- Image 2: Day Count Basis Comparison. See Images/Financial/ACCRINT.md -->

### Example 3: Rounded to Cents

```excel
=ROUND(ACCRINT(DATE(2026,1,15),DATE(2026,7,15),DATE(2026,5,1),0.06,1000,2,0),2)
```

**Result:** `17.67`

Wrapping the function in `ROUND` produces a figure that matches what an invoice or settlement statement shows to the cent.

### Example 4: Checking the Coupon Period Share

```excel
=ACCRINT(DATE(2026,1,15),DATE(2026,7,15),DATE(2026,5,1),0.06,1000,2,0)/(1000*0.06/2)
```

**Result:** `0.5889`

Dividing the accrued interest by one full coupon payment (1,000 x 6% / 2 = 30) gives the share of the next coupon that has built up by the settlement date. About 59% has accrued, which is 106 of the 180 days in the coupon period under 30/360.

## Story Problems

### Problem 1: Accrued Interest on a Bond Sale

A pension fund sells a corporate bond to an insurer on July 20, 2026. The bond was issued on March 1, 2026, and pays coupons on March 1 and September 1 of each year.

| Item | Value |
| --- | --- |
| Issue date | 2026-03-01 |
| First interest date | 2026-09-01 |
| Settlement date | 2026-07-20 |
| Annual rate | 0.045 |
| Par value | 10000 |
| Payments per year | 2 |
| Basis | 0 |

**Task:** Calculate the accrued interest the insurer pays the fund on top of the agreed price.

**Solution:**

```excel
=ACCRINT(B2,B3,B4,B5,B6,B7,B8)
```

**Answer:** `173.75`, because 139 days of 30/360 interest (March 1 to July 20) on 10,000 at 4.5% is 10,000 x 4.5% x 139 / 360.

### Problem 2: Quarterly Note Sold Early

A treasurer sells a quarterly note on February 25, 2026. The note was issued on January 10, 2026, and its first coupon falls on April 10, 2026. The note has a par value of 2,500 and a coupon rate of 7.25%.

| Item | Value |
| --- | --- |
| Issue date | 2026-01-10 |
| First interest date | 2026-04-10 |
| Settlement date | 2026-02-25 |
| Annual rate | 0.0725 |
| Par value | 2500 |
| Payments per year | 4 |
| Basis | 0 |

**Task:** Find the accrued interest to the nearest cent that the buyer owes the treasurer.

**Solution:**

```excel
=ROUND(ACCRINT(B2,B3,B4,B5,B6,B7,B8),2)
```

**Answer:** `22.66`, because 45 days of 30/360 interest on 2,500 at 7.25% is 22.65625 before rounding.

<!-- Image 3: Bond Sale Story Table. See Images/Financial/ACCRINT.md -->

## Use Cases

### Bond Interest Accrual

**Scenario:** An accounting team records accrued interest receivable at the end of each month for a portfolio of semiannual bonds.

```excel
=ACCRINT(B2,B3,DATE(2026,11,30),B5,B6,B7,B8)
```

**Why It Works:** Setting `settlement` to the month end gives the interest earned so far in the period. Keep the dates in cells so the same formula can be copied down the list of holdings.

### Bond Trade Settlement

**Scenario:** A trading desk quotes a clean price, then adds the accrued interest so the buyer and seller agree on the total cash amount.

```excel
=ROUND(ACCRINT(Issue,FirstInterest,Settle,Rate,Par,Freq,Basis),2)
```

**Why It Works:** Named ranges make the trade ticket easy to audit. Confirm the basis matches the bond's market convention, because a different basis changes the day count and therefore the cash amount.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `issue` is on or after `settlement`. | Check that the settlement date comes after the issue date. |
| `#NUM!` | `frequency` is not 1, 2 or 4. | Enter the number of coupons per year, not the number of months between coupons. |
| `#NUM!` | `basis` is below 0 or above 4. | Use one of the five basis codes. |
| `#VALUE!` | A date is stored as text. | Enter the date with `DATE` or convert the text to a date value. |
| Result is far too small in Sheets | `redemption` was entered as 1000 instead of 100. | Enter the redemption amount per 100 of face value. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365 and Excel for the web | Uses the full par amount and supports the optional `calc_method` argument. |
| Google Sheets | Available | Calls the par argument `redemption` (per 100 of face value) and the basis argument `day_count_convention`. Does not offer `calc_method`. |

## Tips and Best Practices

- Enter every date with `DATE` or as a reference to a date cell so the function never receives text.
- Use ACCRINT for periodic coupons and ACCRINTM for interest paid only at maturity.
- Match the `basis` to the bond's terms, because the same dates give different accruals on 30/360 and actual/365.
- Wrap the result in `ROUND` only in the final display or posting cell, not in intermediate calculations.
- When a workbook moves between Excel and Sheets, check the par argument first, since the two platforms scale it differently.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ACCRINTM](ACCRINTM.md) | Calculates accrued interest for a security that pays all interest at maturity. |
| [COUPDAYBS](COUPDAYBS.md) | Counts the days from the last coupon to settlement, the same period that ACCRINT accrues over. |
| [COUPPCD](COUPPCD.md) | Returns the last coupon date before settlement, which anchors the accrual period. |
| [PRICE](PRICE.md) | Calculates the clean price of a periodic coupon bond from its yield, before accrued interest is added. |
| [YIELD](YIELD.md) | Calculates the yield of a periodic coupon bond from its price, the reverse of PRICE. |

## Official Documentation

- [Microsoft Support: ACCRINT function](https://support.microsoft.com/en-us/excel/functions/accrint-function)
- [Google Docs Editors Help: ACCRINT](https://support.google.com/docs/answer/3093200)
