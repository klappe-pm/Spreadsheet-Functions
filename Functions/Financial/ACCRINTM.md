---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Interest at Maturity Notes
  - Short Term Note Valuation
  - Treasury Accrual Reporting
related:
  - ACCRINT
  - COUPDAYBS
  - DISC
  - PRICEMAT
  - YIELDMAT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/accrintm-function
  - https://support.google.com/docs/answer/3093202
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Accrued Interest At Maturity
  - Maturity Interest Accrual
tags:
  - accrued-interest
  - bond-math
  - day-count
  - excel
  - sheets
---

# ACCRINTM

## Description

**ACCRINTM** returns the interest that has built up on a security that pays all of its interest, together with its principal, on the maturity date. Short term notes of this kind follow the pattern. The function counts the days from the issue date to the maturity date, then applies the annual rate to the par value using the day count basis you choose.

Use ACCRINTM for a security with a single interest payment at maturity. For a security that pays coupons on a schedule, such as a semiannual bond, use ACCRINT instead.

Microsoft Excel and Google Sheets name the arguments differently. Excel's second argument is called `settlement`, but for this function it holds the maturity date. Google Sheets calls it `maturity`, names the fourth argument `redemption` and makes it optional, so check each argument before you copy a formula between the two platforms.

## Syntax

```excel
=ACCRINTM(issue, settlement, rate, par, [basis])
```

<!-- Image 1: Interest at Maturity Period. See Images/Financial/ACCRINTM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `issue` | Yes | The date the security was first issued. |
| `settlement` | Yes | In Excel, the maturity date of the security. Enter it with `DATE` or as a date value. Must fall after `issue`. |
| `rate` | Yes | The annual interest rate as a decimal, for example `0.048` for 4.8%. Must be greater than 0. |
| `par` | Yes | The par (face) value of the security, for example `1000`. Must be greater than 0. |
| `basis` | No | The day count basis. `0` or omitted uses US (NASD) 30/360. `1` uses actual/actual, `2` actual/360, `3` actual/365 and `4` European 30/360. |

### Return Value

A number: the interest accrued from the issue date to the maturity date, in the same currency unit as `par`. The function returns `#VALUE!` when a date is not valid, and `#NUM!` when `rate` or `par` is zero or negative, `basis` is outside 0 to 4, or `issue` falls on or after the maturity date.

## Examples

All examples use a note issued on March 1, 2026, that matures on December 1, 2026.

### Example 1: Interest on a 30/360 Basis

```excel
=ACCRINTM(DATE(2026,3,1),DATE(2026,12,1),0.048,1000,0)
```

**Result:** `36`

Nine months at 30/360 is 270 days, so the interest is 1,000 x 4.8% x 270 / 360 = 36.

### Example 2: Interest on an Actual/365 Basis

```excel
=ACCRINTM(DATE(2026,3,1),DATE(2026,12,1),0.048,1000,3)
```

**Result:** `36.1644`

The actual calendar span is 275 days, so the interest is 1,000 x 4.8% x 275 / 365. Actual/365 gives slightly more interest than 30/360 here because the calendar days are counted directly.

<!-- Image 2: Day Count Basis Comparison. See Images/Financial/ACCRINTM.md -->

### Example 3: A Note Measured Mid-Term

```excel
=ACCRINTM(DATE(2026,4,10),DATE(2026,10,10),0.0525,5000,0)
```

**Result:** `131.25`

A 5,000 note at 5.25% for six months on 30/360 earns 5,000 x 5.25% x 180 / 360.

### Example 4: Rounded for a Statement

```excel
=ROUND(ACCRINTM(DATE(2026,3,1),DATE(2026,12,1),0.048,1000,3),2)
```

**Result:** `36.16`

Rounding to cents is applied in the outer formula so the source calculation keeps full precision.

## Story Problems

### Problem 1: Interest on a Short Note

A credit union issues a note of 2,000 at 6.15% on June 15, 2026. The note matures on January 15, 2027, seven months later. The credit union uses the 30/360 convention on its statements.

| Item | Value |
| --- | --- |
| Issue date | 2026-06-15 |
| Maturity date | 2027-01-15 |
| Annual rate | 0.0615 |
| Par value | 2000 |
| Basis | 0 |

**Task:** Calculate the total interest paid at maturity.

**Solution:**

```excel
=ACCRINTM(B2,B3,B4,B5,B6)
```

**Answer:** `71.75`, because 210 days of 30/360 interest on 2,000 at 6.15% is 2,000 x 6.15% x 210 / 360.

### Problem 2: Treasury Note on an Actual/365 Basis

A treasury office buys a 5% note with a par value of 5,000 on February 1, 2026. The note matures on August 1, 2026. The office's policy is to use actual days over a 365-day year.

| Item | Value |
| --- | --- |
| Issue date | 2026-02-01 |
| Maturity date | 2026-08-01 |
| Annual rate | 0.05 |
| Par value | 5000 |
| Basis | 3 |

**Task:** Find the interest due at maturity, rounded to the cent, and compare it with the 30/360 result of 125.

**Solution:**

```excel
=ROUND(ACCRINTM(B2,B3,B4,B5,B6),2)
```

**Answer:** `123.97`, because 181 actual days at 5% on 5,000 is 5,000 x 5% x 181 / 365 (123.9726). That is about 1.03 less than the 125 produced by 30/360, which counts the same period as 180 days.

## Use Cases

### Interest at Maturity Notes

**Scenario:** A finance team tracks a portfolio of notes that pay principal and interest together on the maturity date.

```excel
=ACCRINTM(IssueDate,MaturityDate,Rate,Par,Basis)
```

**Why It Works:** Each row holds one note, so the same formula can be copied down the list. The result is the interest the portfolio will receive at maturity.

### Treasury Accrual Reporting

**Scenario:** A treasury office reports interest accrued on short term instruments at the end of each quarter.

```excel
=ROUND(ACCRINTM(B2,B3,B4,B5,3),2)
```

**Why It Works:** Fixing the basis to 3 keeps every quarterly report on the same convention. Store the basis in one cell and point each formula at it if policy ever changes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `issue` is on or after the maturity date. | Check that the maturity date comes after the issue date. |
| `#NUM!` | `basis` is below 0 or above 4. | Use one of the five basis codes. |
| `#NUM!` | `rate` or `par` is zero or negative. | Enter a positive rate and par value. |
| `#VALUE!` | A date is stored as text. | Enter the date with `DATE` or convert the text to a date value. |
| Interest is about 100 times too large | The rate was entered as a whole number, such as `4.8`, instead of a decimal such as `0.048`. | Enter the rate as a decimal or as a percentage-formatted cell. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Microsoft 365 and Excel for the web | Arguments are `issue`, `settlement`, `rate`, `par` and `basis`. `settlement` holds the maturity date. |
| Google Sheets | Available | Arguments are `issue`, `maturity`, `rate`, `redemption` and `day_count_convention`. The redemption argument is optional. |

## Tips and Best Practices

- Enter dates with `DATE` or cell references to real date values so the day count is calculated correctly.
- Use ACCRINTM only for interest paid at maturity, and use ACCRINT for coupon bonds.
- Store the basis in one labeled cell so every calculation in the workbook follows the same convention.
- Round only in the final display or posting cell.
- Label the second argument clearly in shared workbooks, because Excel calls it `settlement` while the function uses the maturity date.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ACCRINT](ACCRINT.md) | Accrued interest for securities that pay periodic coupons. |
| [COUPDAYBS](COUPDAYBS.md) | Day count from the last coupon date to settlement for coupon bonds. |
| [DISC](DISC.md) | Discount rate for a security bought at a discount and redeemed at par. |
| [PRICEMAT](PRICEMAT.md) | Price of a security that pays interest at maturity, the companion to this function. |
| [YIELDMAT](YIELDMAT.md) | Yield of a security that pays interest at maturity, calculated from its price. |

## Official Documentation

- [Microsoft Support: ACCRINTM function](https://support.microsoft.com/en-us/excel/functions/accrintm-function)
- [Google Docs Editors Help: ACCRINTM](https://support.google.com/docs/answer/3093202)
