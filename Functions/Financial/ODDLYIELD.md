---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Bond Yield Analysis
  - Market Quote Yield
  - Short Maturity Note Yield
related:
  - ODDFPRICE
  - ODDFYIELD
  - ODDLPRICE
  - PRICE
  - YIELD
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/oddlyield-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Odd Last Coupon Bond Yield
tags:
  - bond-yield
  - excel
  - odd-last-period
---

# ODDLYIELD

## Description

**ODDLYIELD** returns the annual yield of a security whose last coupon period is odd. You supply the market price, and the function returns the yield that the price implies, given the settlement date, the last coupon date, the maturity date and the coupon rate.

The function is the reverse of ODDLPRICE. Use it to measure the return on a note bought at a quoted price, to compare offers on the same security, or to confirm that a price from another source matches the terms.

ODDLYIELD is available in Excel only. Google Sheets has no odd last period yield function, so use YIELD for securities with regular coupon periods.

## Syntax

```excel
=ODDLYIELD(settlement, maturity, last_interest, rate, pr, redemption, frequency, [basis])
```

<!-- Image 1: Odd Last Period Timeline. See Images/Financial/ODDLYIELD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the security. It must fall after the last interest date and before maturity. |
| `maturity` | Yes | The date the security expires. It must fall after the settlement date. |
| `last_interest` | Yes | The most recent coupon date before settlement. |
| `rate` | Yes | The annual coupon rate. It cannot be negative. |
| `pr` | Yes | The price per $100 face value. It must be greater than 0. |
| `redemption` | Yes | The amount repaid at maturity per $100 of face value. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual, or `4` for quarterly. |
| `basis` | No | The day count basis: `0` or omitted for US (NASD) 30/360, `1` for actual/actual, `2` for actual/360, `3` for actual/365, or `4` for European 30/360. |

### Return Value

A number: the annual yield, which Excel displays as a percentage when the cell is formatted that way. The function returns `#VALUE!` when a date argument is not a valid date. It returns `#NUM!` when the rate is negative, the price is 0 or less, the basis is outside 0 to 4, or the dates do not satisfy maturity > settlement > last interest.

## Examples

### Example 1: Yield on a Short Note

```excel
=ODDLYIELD(DATE(2026,6,10), DATE(2026,8,15), DATE(2026,2,15), 4%, 100.25, 100, 2, 0)
```

**Result:** `2.58%`

The price of 100.25 is above par, so the yield is below the 4% coupon rate.

### Example 2: Yield at a Discounted Price

```excel
=ODDLYIELD(DATE(2026,6,10), DATE(2026,8,15), DATE(2026,2,15), 4%, 99.5, 100, 2, 0)
```

**Result:** `6.72%`

A price of 99.50 is below par, and the shorter remaining life means the yield rises well above the coupon rate.

<!-- Image 2: Yield Changes With Price. See Images/Financial/ODDLYIELD.md -->

### Example 3: Wrap the Yield in IFERROR

With the terms in `B2:B6`, where `B2` is settlement, `B3` is maturity, `B4` is last interest, `B5` is the rate and `B6` is the price:

```excel
=IFERROR(ODDLYIELD(B2, B3, B4, B5, B6, 100, 2, 0), "Check dates")
```

**Result:** `2.58%` when `B6` holds 100.25.

If the dates are out of order, the cell shows "Check dates" instead of an error code.

## Story Problems

### Problem 1: Yield on a Note at a Premium

A pension fund buys a note whose last coupon date is June 15, 2026. It settles on September 2, 2026 and matures on December 15, 2026. The coupon rate is 3.6%, paid semiannually, and the fund pays a clean price of 100.10.

| Term | Value |
| --- | --- |
| Settlement | 9/2/2026 |
| Maturity | 12/15/2026 |
| Last interest | 6/15/2026 |
| Coupon rate | 3.60% |
| Price | 100.10 |

**Task:** Find the annual yield the fund earns at this price, with a redemption value of 100 and 30/360 day counting.

**Solution:**

```excel
=ODDLYIELD(B2, B3, B4, B5, B6, 100, 2, 0)
```

**Answer:** `3.22%`. Paying above par pulls the yield below the 3.6% coupon.

### Problem 2: Yield on the Same Note at a Lower Price

The fund has a second offer for the same note at a clean price of 99.40, using the terms from Problem 1 in `B2:B5`.

**Task:** Find the annual yield at a price of 99.40.

**Solution:**

```excel
=ODDLYIELD(B2, B3, B4, B5, 99.4, 100, 2, 0)
```

**Answer:** `5.69%`. The lower price raises the yield well above the coupon rate.

<!-- Image 3: Story Problem Inputs and Output. See Images/Financial/ODDLYIELD.md -->

## Use Cases

### Bond Yield Analysis

**Scenario:** An analyst compares the yield on a short note with the yield on a money market fund.

```excel
=ODDLYIELD(SettlementDate, MaturityDate, LastCouponDate, CouponRate, QuotedPrice, 100, 2, 0)
```

**Why It Works:** The result is the annual yield at the quoted price, so the analyst can compare it directly with other annual rates.

### Short Maturity Note Yield

**Scenario:** A treasury team evaluates whether to hold a note to maturity or sell it at the current market price.

```excel
=ODDLYIELD(TodayDate, MaturityDate, LastCouponDate, CouponRate, MarketPrice, 100, 2, 0)
```

**Why It Works:** Comparing the yield at the market price with the buyer's required yield shows whether holding the note earns more than the market.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The dates do not satisfy maturity > settlement > last interest. | Check each date pair and correct the one that is out of order. |
| `#NUM!` | The price is 0 or less. | Enter the price per $100 face value as a positive number. |
| `#VALUE!` | A date argument is text instead of a date. | Enter dates with `DATE` or as true date values. |
| `#NUM!` | The basis is outside 0 to 4. | Use `0`, `1`, `2`, `3` or `4`. |
| Yield shows as a large decimal | The result is a decimal, and the cell is not formatted as a percentage. | Format the cell as a percentage. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Dates must be real date values, because text dates can produce errors. |
| Google Sheets | Not available | Use YIELD for securities with regular coupon periods. |

## Tips and Best Practices

- Use the last interest date from the security's schedule, not the issue date, because the odd period starts at the last coupon.
- Enter the price per $100 face value, not a percentage of par written as a whole number above 100.
- Use the same basis as the offering documents, because a different day count changes the yield.
- Pair the function with ODDLPRICE: price the note at a yield, then recover that yield from the price to confirm the inputs are consistent.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ODDFPRICE](ODDFPRICE.md) | Prices a security whose first coupon period is odd. |
| [ODDFYIELD](ODDFYIELD.md) | Returns the yield for a security whose first coupon period is odd. |
| [ODDLPRICE](ODDLPRICE.md) | Returns the price for this odd last period setup, the inverse of this function. |
| [PRICE](PRICE.md) | Prices a security with regular coupon periods. |
| [YIELD](YIELD.md) | Returns the yield for a security with regular coupon periods. |

## Official Documentation

- [Microsoft Support: ODDLYIELD function](https://support.microsoft.com/en-us/excel/functions/oddlyield-function)
