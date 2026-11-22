---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Bond Desk Pricing
  - New Issue Pricing
  - Portfolio Valuation
related:
  - ODDFYIELD
  - ODDLPRICE
  - ODDLYIELD
  - PRICE
  - PRICEMAT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/oddfprice-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Odd First Coupon Bond Price
tags:
  - bond-pricing
  - excel
  - odd-first-period
---

# ODDFPRICE

## Description

**ODDFPRICE** returns the price per $100 face value of a security whose first coupon period is odd. A period is odd when its length differs from the regular coupon period, for example when a bond is issued a few weeks after the start of its first regular coupon period. New bond issues often have this shape, so the function is most useful when a desk prices a fresh issue before its payment schedule settles into regular periods.

The result is a clean price. Accrued interest from the issue date to the settlement date is subtracted, so add it back when you need the full amount the buyer pays.

Use ODDFYIELD for the reverse calculation: it returns the yield that a given market price implies, using the same dates and terms. For a security whose last coupon period is odd, use ODDLPRICE instead. ODDFPRICE is available in Excel only, and Google Sheets has no equivalent.

## Syntax

```excel
=ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, [basis])
```

<!-- Image 1: Odd First Period Timeline. See Images/Financial/ODDFPRICE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the security. It must fall after the issue date and before the first coupon date. |
| `maturity` | Yes | The date the security expires and its principal is repaid. It must fall after the first coupon date. |
| `issue` | Yes | The date the security was issued. |
| `first_coupon` | Yes | The date of the first coupon payment. |
| `rate` | Yes | The annual coupon rate. It cannot be negative. |
| `yld` | Yes | The annual yield, the return the buyer requires. It cannot be negative. |
| `redemption` | Yes | The amount repaid at maturity per $100 of face value. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual, or `4` for quarterly. |
| `basis` | No | The day count basis: `0` or omitted for US (NASD) 30/360, `1` for actual/actual, `2` for actual/360, `3` for actual/365, or `4` for European 30/360. |

### Return Value

A number: the clean price per $100 face value. The function returns `#VALUE!` when a date argument is not a valid date. It returns `#NUM!` when the rate or yield is negative, when the basis is outside 0 to 4, or when the dates do not satisfy maturity > first coupon > settlement > issue.

## Examples

### Example 1: Price a Fresh Issue

```excel
=ODDFPRICE(DATE(2027,5,20), DATE(2032,8,15), DATE(2027,3,15), DATE(2027,8,15), 5.25%, 6%, 100, 2, 0)
```

**Result:** `96.67`

The issue date falls after the regular period start of February 15, 2027, so the first period is short. The 6% yield is above the 5.25% coupon, so the price sits below par.

### Example 2: Recover the Yield From a Market Price

```excel
=ODDFYIELD(DATE(2027,5,20), DATE(2032,8,15), DATE(2027,3,15), DATE(2027,8,15), 5.25%, 101.5, 100, 2, 0)
```

**Result:** `4.92%`

This uses the same dates and coupon with a market price of 101.50. A price above par means the yield is below the coupon rate.

<!-- Image 2: Price and Yield Inputs Side by Side. See Images/Financial/ODDFPRICE.md -->

### Example 3: Wrap the Price in IFERROR

With the terms in `B2:B7`, where `B2` is settlement, `B3` is maturity, `B4` is issue, `B5` is first coupon, `B6` is the rate and `B7` is the yield:

```excel
=IFERROR(ODDFPRICE(B2, B3, B4, B5, B6, B7, 100, 2, 0), "Check dates")
```

**Result:** `96.67`

If someone enters the dates in the wrong order, the cell shows "Check dates" instead of an error code.

## Story Problems

### Problem 1: Pricing a New Corporate Bond

A bond desk prepares a quote for a corporate bond issued on October 20, 2026. Its first coupon falls on April 15, 2027, and it matures on April 15, 2031. The coupon rate is 6.00%, paid semiannually. A buyer settles the trade on December 1, 2026 and wants a yield of 5.50%.

| Term | Value |
| --- | --- |
| Settlement | 12/1/2026 |
| Maturity | 4/15/2031 |
| Issue | 10/20/2026 |
| First coupon | 4/15/2027 |
| Coupon rate | 6.00% |
| Yield | 5.50% |

**Task:** Find the clean price per $100 face value, with a redemption value of 100 and 30/360 day counting.

**Solution:**

```excel
=ODDFPRICE(B2, B3, B4, B5, B6, B7, 100, 2, 0)
```

**Answer:** `101.91`, rounded to the cent. The bond trades above par because its 6.00% coupon is higher than the 5.50% yield.

### Problem 2: Yield Implied by a Market Price

The same bond trades in the market at a clean price of 101.20. The trader wants the yield a buyer earns at that price, using the terms from Problem 1.

**Task:** Find the annual yield for a clean price of 101.20.

**Solution:**

```excel
=ODDFYIELD(B2, B3, B4, B5, B6, 101.2, 100, 2, 0)
```

**Answer:** `5.68%`. A lower price than the Problem 1 price produces a higher yield.

<!-- Image 3: Story Problem Inputs and Output. See Images/Financial/ODDFPRICE.md -->

## Use Cases

### Bond Desk Quote Sheet

**Scenario:** A bond desk keeps one row per new issue and wants the quoted price to update when a settlement date or rate changes.

```excel
=ODDFPRICE(SettlementDate, MaturityDate, IssueDate, FirstCouponDate, CouponRate, QuoteYield, 100, 2, 0)
```

**Why It Works:** Each issue keeps its terms in named cells, so the quote updates when an input changes and nobody retypes the formula.

### Portfolio Valuation Check

**Scenario:** A fund's accounting team marks a holding that was issued with a short first coupon.

```excel
=ODDFPRICE(SettlementDate, MaturityDate, IssueDate, FirstCouponDate, CouponRate, MarketYield, 100, 2, 0)
```

**Why It Works:** The yield reflects the return the market requires. Add the accrued interest to the clean price before comparing the result with the cash value of the position.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The dates do not satisfy maturity > first coupon > settlement > issue. | Check each date pair and correct the one that is out of order. |
| `#VALUE!` | A date argument is text instead of a date. | Enter dates with `DATE` or as true date values. |
| `#NUM!` | The rate or yield is negative. | Enter both as zero or positive decimals. |
| `#NUM!` | The basis is outside 0 to 4. | Use `0`, `1`, `2`, `3` or `4`. |
| Price looks too low | The result is a clean price, and accrued interest was not added. | Add the accrued interest when the full settlement amount is needed. |
| Unexpected result | The frequency is not `1`, `2` or `4`. | Enter the number of payments per year as `1`, `2` or `4`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Dates must be real date values, because text dates can produce errors. |
| Google Sheets | Not available | Use PRICE for securities with regular coupon periods. |

## Tips and Best Practices

- Enter dates with `DATE` or as cell references so the result does not depend on regional date formats.
- Check the date order first. Most `#NUM!` errors come from one date pair entered in the wrong order.
- Use basis `0` when the issue terms state 30/360 and basis `1` when they state actual/actual, so the accrual days match the offering documents.
- Add the accrued interest from the issue date to settlement when a full amount is needed, because the result is a clean price.
- Pair the function with ODDFYIELD: price the bond at a yield, then recover that yield from the price to confirm the inputs are consistent.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ODDFYIELD](ODDFYIELD.md) | Returns the yield for a given price, using the same odd first period terms. |
| [ODDLPRICE](ODDLPRICE.md) | Prices a security whose last coupon period is odd. |
| [ODDLYIELD](ODDLYIELD.md) | Returns the yield for a security with an odd last period. |
| [PRICE](PRICE.md) | Prices a security with regular coupon periods. |
| [PRICEMAT](PRICEMAT.md) | Prices a security that pays all of its interest at maturity. |

## Official Documentation

- [Microsoft Support: ODDFPRICE function](https://support.microsoft.com/en-us/excel/functions/oddfprice-function)
