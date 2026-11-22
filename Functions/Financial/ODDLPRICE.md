---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Bond Desk Pricing
  - Portfolio Valuation
  - Short Maturity Note Pricing
related:
  - ODDFPRICE
  - ODDLYIELD
  - PRICE
  - PRICEMAT
  - YIELD
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/oddlprice-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Odd Last Coupon Bond Price
tags:
  - bond-pricing
  - excel
  - odd-last-period
---

# ODDLPRICE

## Description

**ODDLPRICE** returns the price per $100 face value of a security whose last coupon period is odd, meaning the period between the last coupon date and maturity is shorter or longer than a regular coupon period. This happens for securities that are close to maturity when the schedule does not line up with the maturity date, which is common for short notes and bonds that were issued on a non-standard date.

The result is a clean price. Accrued interest from the last coupon date to the settlement date is subtracted, so add it back when you need the full amount the buyer pays.

Use ODDLYIELD for the reverse calculation: it returns the yield that a given market price implies. For a security whose first coupon period is odd, use ODDFPRICE instead. ODDLPRICE is available in Excel only, and Google Sheets has no equivalent.

## Syntax

```excel
=ODDLPRICE(settlement, maturity, last_interest, rate, yld, redemption, frequency, [basis])
```

<!-- Image 1: Odd Last Period Timeline. See Images/Financial/ODDLPRICE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the security. It must fall after the last interest date and before maturity. |
| `maturity` | Yes | The date the security expires and its principal is repaid. It must fall after the settlement date. |
| `last_interest` | Yes | The most recent coupon date before settlement. It must fall before the settlement date. |
| `rate` | Yes | The annual coupon rate. It cannot be negative. |
| `yld` | Yes | The annual yield, the return the buyer requires. It cannot be negative. |
| `redemption` | Yes | The amount repaid at maturity per $100 of face value. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual, or `4` for quarterly. |
| `basis` | No | The day count basis: `0` or omitted for US (NASD) 30/360, `1` for actual/actual, `2` for actual/360, `3` for actual/365, or `4` for European 30/360. |

### Return Value

A number: the clean price per $100 face value. The function returns `#VALUE!` when a date argument is not a valid date. It returns `#NUM!` when the rate or yield is negative, when the basis is outside 0 to 4, or when the dates do not satisfy maturity > settlement > last interest.

## Examples

### Example 1: Price a Short Note

```excel
=ODDLPRICE(DATE(2026,6,10), DATE(2026,8,15), DATE(2026,2,15), 4%, 4.5%, 100, 2, 0)
```

**Result:** `99.90`

The last coupon date is February 15, 2026 and maturity is August 15, 2026. The 4.5% yield is above the 4% coupon, so the price sits slightly below par.

### Example 2: Price at a Different Yield

```excel
=ODDLPRICE(DATE(2026,6,10), DATE(2026,8,15), DATE(2026,2,15), 4%, 3.5%, 100, 2, 0)
```

**Result:** `100.08`

Lowering the yield to 3.5% raises the price above par. The same note and settlement date are used.

<!-- Image 2: Price Changes With Yield. See Images/Financial/ODDLPRICE.md -->

### Example 3: Wrap the Price in IFERROR

With the terms in `B2:B6`, where `B2` is settlement, `B3` is maturity, `B4` is last interest, `B5` is the rate and `B6` is the yield:

```excel
=IFERROR(ODDLPRICE(B2, B3, B4, B5, B6, 100, 2, 0), "Check dates")
```

**Result:** `99.90`

If the dates are out of order, the cell shows "Check dates" instead of an error code.

## Story Problems

### Problem 1: Pricing a Short Maturity Note

A treasury team holds a note that paid its last coupon on March 15, 2026 and matures on October 31, 2026. The team plans to sell the note on July 20, 2026. The coupon rate is 4.8%, paid semiannually, and the buyer requires a yield of 5.1%.

| Term | Value |
| --- | --- |
| Settlement | 7/20/2026 |
| Maturity | 10/31/2026 |
| Last interest | 3/15/2026 |
| Coupon rate | 4.80% |
| Yield | 5.10% |

**Task:** Find the clean price per $100 face value, with a redemption value of 100 and 30/360 day counting.

**Solution:**

```excel
=ODDLPRICE(B2, B3, B4, B5, B6, 100, 2, 0)
```

**Answer:** `99.89`, rounded to the cent. The required yield is above the coupon rate, so the price falls slightly below par.

### Problem 2: Price for a Bond Close to Maturity

A second note has a last interest date of June 15, 2026, a settlement date of September 2, 2026 and a maturity of December 15, 2026. Its coupon rate is 3.6%, and the buyer requires a yield of 4.4%.

**Task:** Find the clean price per $100 face value for this note.

**Solution:**

```excel
=ODDLPRICE(DATE(2026,9,2), DATE(2026,12,15), DATE(2026,6,15), 3.6%, 4.4%, 100, 2, 0)
```

**Answer:** `99.76`, rounded to the cent.

<!-- Image 3: Story Problem Inputs and Output. See Images/Financial/ODDLPRICE.md -->

## Use Cases

### Short Maturity Note Pricing

**Scenario:** A treasury team sells notes before maturity and needs a quoted clean price for each possible sale date.

```excel
=ODDLPRICE(SaleDate, MaturityDate, LastCouponDate, CouponRate, BuyerYield, 100, 2, 0)
```

**Why It Works:** Each sale date is a separate row, and the formula updates when a new date or yield is entered.

### Bond Desk Pricing

**Scenario:** A desk quotes a bond whose maturity falls off the regular coupon schedule.

```excel
=ODDLPRICE(SettlementDate, MaturityDate, LastCouponDate, CouponRate, QuoteYield, 100, 2, 0)
```

**Why It Works:** Using the last coupon date rather than assuming a regular period keeps the quote consistent with the actual schedule.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The dates do not satisfy maturity > settlement > last interest. | Check each date pair and correct the one that is out of order. |
| `#VALUE!` | A date argument is text instead of a date. | Enter dates with `DATE` or as true date values. |
| `#NUM!` | The rate or yield is negative. | Enter both as zero or positive decimals. |
| `#NUM!` | The basis is outside 0 to 4. | Use `0`, `1`, `2`, `3` or `4`. |
| Price looks too low | The result is a clean price, and accrued interest was not added. | Add the accrued interest when the full settlement amount is needed. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Dates must be real date values, because text dates can produce errors. |
| Google Sheets | Not available | Use PRICE for securities with regular coupon periods. |

## Tips and Best Practices

- Use the last interest date from the security's schedule, not the issue date, because the odd period starts at the last coupon.
- Enter the yield as a decimal or percentage in the same way the rate is entered, so both are read correctly.
- Add the accrued interest from the last coupon date to settlement when a full cash amount is needed.
- Check the date order before changing the rate or yield, because most `#NUM!` errors come from the dates.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ODDFPRICE](ODDFPRICE.md) | Prices a security whose first coupon period is odd. |
| [ODDLYIELD](ODDLYIELD.md) | Returns the yield for this same odd last period setup. |
| [PRICE](PRICE.md) | Prices a security with regular coupon periods. |
| [PRICEMAT](PRICEMAT.md) | Prices a security that pays all of its interest at maturity. |
| [YIELD](YIELD.md) | Returns the yield for a security with regular coupon periods. |

## Official Documentation

- [Microsoft Support: ODDLPRICE function](https://support.microsoft.com/en-us/excel/functions/oddlprice-function)
