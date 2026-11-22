---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Bond Desk Pricing
  - Market Quote Yield
  - Yield Verification
related:
  - ODDFPRICE
  - ODDLPRICE
  - ODDLYIELD
  - PRICE
  - YIELD
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/oddfyield-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Odd First Coupon Bond Yield
tags:
  - bond-yield
  - excel
  - odd-first-period
---

# ODDFYIELD

## Description

**ODDFYIELD** returns the annual yield of a security whose first coupon period is odd. It is the reverse of ODDFPRICE: you supply the market price, and the function returns the yield that makes that price consistent with the security's dates, coupon and redemption value.

Excel solves for the yield iteratively using the Newton method, which is why the function takes no closed form answer and why very unusual inputs can fail to converge. Use it to measure the return on a bond bought at a quoted price, to compare offers on the same security, or to check that an ODDFPRICE result is consistent with a known market price.

The function is available in Excel only. Google Sheets has no odd first period yield function, so use YIELD for securities with regular coupon periods.

## Syntax

```excel
=ODDFYIELD(settlement, maturity, issue, first_coupon, rate, pr, redemption, frequency, [basis])
```

<!-- Image 1: Odd First Period Timeline. See Images/Financial/ODDFYIELD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the security. It must fall after the issue date and before the first coupon date. |
| `maturity` | Yes | The date the security expires. It must fall after the first coupon date. |
| `issue` | Yes | The date the security was issued. |
| `first_coupon` | Yes | The date of the first coupon payment. |
| `rate` | Yes | The annual coupon rate. It cannot be negative. |
| `pr` | Yes | The price per $100 face value. It must be greater than 0. |
| `redemption` | Yes | The amount repaid at maturity per $100 of face value. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual, or `4` for quarterly. |
| `basis` | No | The day count basis: `0` or omitted for US (NASD) 30/360, `1` for actual/actual, `2` for actual/360, `3` for actual/365, or `4` for European 30/360. |

### Return Value

A number: the annual yield, which Excel displays as a percentage when the cell is formatted that way. The function returns `#VALUE!` when a date argument is not a valid date. It returns `#NUM!` when the rate is negative, the price is 0 or less, the basis is outside 0 to 4, or the dates do not satisfy maturity > first coupon > settlement > issue.

## Examples

### Example 1: Yield for a Discounted Price

```excel
=ODDFYIELD(DATE(2027,5,20), DATE(2032,8,15), DATE(2027,3,15), DATE(2027,8,15), 5.25%, 95.5, 100, 2, 0)
```

**Result:** `6.27%`

A price of 95.50 is below par, so the yield is above the 5.25% coupon rate.

### Example 2: Check the Price Back

```excel
=ODDFPRICE(DATE(2027,5,20), DATE(2032,8,15), DATE(2027,3,15), DATE(2027,8,15), 5.25%, 6.27%, 100, 2, 0)
```

**Result:** `95.50`

Passing the yield from Example 1 back into ODDFPRICE returns the original price, which confirms the two functions use the same terms.

<!-- Image 2: Yield and Price Round Trip. See Images/Financial/ODDFYIELD.md -->

### Example 3: Wrap the Yield in IFERROR

With the terms in `B2:B7`, where `B2` is settlement, `B3` is maturity, `B4` is issue, `B5` is first coupon, `B6` is the rate and `B7` is the price:

```excel
=IFERROR(ODDFYIELD(B2, B3, B4, B5, B6, B7, 100, 2, 0), "Check dates")
```

**Result:** `6.27%` when `B7` holds 95.50.

Bad date order returns the text "Check dates" instead of an error code.

## Story Problems

### Problem 1: Yield on a Credit Union Note

A credit union buys a note issued on March 10, 2026. Its first coupon falls on September 1, 2026, and it matures on September 1, 2029. The coupon rate is 4.50%, paid semiannually. The credit union settles on May 15, 2026 at a clean price of 99.20.

| Term | Value |
| --- | --- |
| Settlement | 5/15/2026 |
| Maturity | 9/1/2029 |
| Issue | 3/10/2026 |
| First coupon | 9/1/2026 |
| Coupon rate | 4.50% |
| Price | 99.20 |

**Task:** Find the annual yield the credit union earns at this price, with a redemption value of 100 and 30/360 day counting.

**Solution:**

```excel
=ODDFYIELD(B2, B3, B4, B5, B6, B7, 100, 2, 0)
```

**Answer:** `4.76%`. The price is below par, so the yield is above the 4.50% coupon.

### Problem 2: Comparing Two Price Offers

A second dealer offers the same note at two prices, using the terms from Problem 1 in `B2:B6`. The buyer can accept an offer at 98.40 or one at 99.60.

**Task:** Find the yield for each offer and decide which one earns more.

**Solution:**

```excel
=ODDFYIELD(B2, B3, B4, B5, B6, 98.4, 100, 2, 0)
```

```excel
=ODDFYIELD(B2, B3, B4, B5, B6, 99.6, 100, 2, 0)
```

**Answer:** The offer at 98.40 yields `5.03%`, and the offer at 99.60 yields `4.63%`. The lower price earns more.

<!-- Image 3: Story Problem Inputs and Output. See Images/Financial/ODDFYIELD.md -->

## Use Cases

### Market Quote Yield

**Scenario:** A trader sees a bond quoted at a clean price and needs the yield to present to a client.

```excel
=ODDFYIELD(SettlementDate, MaturityDate, IssueDate, FirstCouponDate, CouponRate, QuotedPrice, 100, 2, 0)
```

**Why It Works:** The named inputs let the trader update the quoted price without changing the formula. The result is the annual yield the buyer earns at that price.

### Yield Verification

**Scenario:** An analyst receives a price from a pricing service and wants to confirm the service used the same terms.

```excel
=ODDFPRICE(SettlementDate, MaturityDate, IssueDate, FirstCouponDate, CouponRate, ServiceYield, 100, 2, 0)
```

**Why It Works:** If the price from ODDFPRICE at the service's yield matches the service's price, both sides used the same dates, coupon and day count basis.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The dates do not satisfy maturity > first coupon > settlement > issue. | Check each date pair and correct the one that is out of order. |
| `#NUM!` | The price is 0 or less. | Enter the price per $100 face value as a positive number. |
| `#VALUE!` | A date argument is text instead of a date. | Enter dates with `DATE` or as true date values. |
| `#NUM!` | The basis is outside 0 to 4. | Use `0`, `1`, `2`, `3` or `4`. |
| Yield shows as a large decimal | The result is a decimal, and the cell is not formatted as a percentage. | Format the cell as a percentage. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Dates must be real date values, and the function solves for yield iteratively. |
| Google Sheets | Not available | Use YIELD for securities with regular coupon periods. |

## Tips and Best Practices

- Enter the market price per $100 face value, not as a percentage of face value expressed as a decimal.
- Use the same basis as the offering documents, because a different day count changes the yield.
- Compare yields only for securities with the same settlement date, since accrued interest depends on it.
- Use ODDFPRICE with the yield from this function to confirm that the two agree within rounding.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ODDFPRICE](ODDFPRICE.md) | Returns the price for a given yield, the inverse of this function. |
| [ODDLPRICE](ODDLPRICE.md) | Prices a security whose last coupon period is odd. |
| [ODDLYIELD](ODDLYIELD.md) | Returns the yield for a security with an odd last period. |
| [PRICE](PRICE.md) | Prices a security with regular coupon periods. |
| [YIELD](YIELD.md) | Returns the yield for a security with regular coupon periods. |

## Official Documentation

- [Microsoft Support: ODDFYIELD function](https://support.microsoft.com/en-us/excel/functions/oddfyield-function)
