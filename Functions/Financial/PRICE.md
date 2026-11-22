---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Investment Portfolio Valuation
  - Pension Bond Pricing
  - Yield Sensitivity Analysis
related:
  - DURATION
  - ODDFPRICE
  - PRICEDISC
  - PRICEMAT
  - YIELD
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/price-function
  - https://support.google.com/docs/answer/3093188
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bond Price Per 100
tags:
  - bond-pricing
  - excel
  - sheets
---

# PRICE

## Description

**PRICE** returns the price per $100 face value of a security that pays periodic interest, such as a government or corporate bond with regular coupon payments. You supply the settlement date, the maturity date, the annual coupon rate, the expected annual yield, the redemption value and the number of coupon payments per year. The function calculates what a buyer should pay so that the return matches the yield.

The result is a clean price. Accrued interest from the last coupon date to settlement is subtracted, so add it back when you need the full amount the buyer pays.

PRICE assumes regular coupon periods. For a first or last coupon period that is shorter or longer than normal, use ODDFPRICE or ODDLPRICE in Excel. For the reverse calculation, use YIELD to find the yield from a known price. For securities that pay all interest at maturity, use PRICEMAT, and for discount securities such as Treasury bills, use PRICEDISC.

## Syntax

```excel
=PRICE(settlement, maturity, rate, yld, redemption, frequency, [basis])
```

<!-- Image 1: Bond Price Inputs. See Images/Financial/PRICE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the bond. It must fall before the maturity date. |
| `maturity` | Yes | The date the bond expires and its principal is repaid. It must fall after the settlement date. |
| `rate` | Yes | The annual coupon rate. It cannot be negative. |
| `yld` | Yes | The annual yield the buyer requires. It cannot be negative. |
| `redemption` | Yes | The amount repaid at maturity per $100 of face value. It must be greater than 0. |
| `frequency` | Yes | The number of coupon payments per year: `1` for annual, `2` for semiannual, or `4` for quarterly. |
| `basis` | No | The day count basis: `0` or omitted for US (NASD) 30/360, `1` for actual/actual, `2` for actual/360, `3` for actual/365, or `4` for European 30/360. |

### Return Value

A number: the clean price per $100 face value. The function returns `#VALUE!` when the settlement or maturity is not a valid date. It returns `#NUM!` when the rate or yield is negative, the redemption value is 0 or less, the frequency is not `1`, `2` or `4`, the basis is outside 0 to 4, or the settlement date is on or after the maturity date.

## Examples

### Example 1: Price a Semiannual Bond

```excel
=PRICE(DATE(2026,4,1), DATE(2031,9,15), 4.5%, 5%, 100, 2, 0)
```

**Result:** `97.64`

The 5% yield is above the 4.5% coupon, so the bond sells below par. The settlement falls between the March 15 and September 15 coupon dates.

### Example 2: Price a Quarterly Bond

```excel
=PRICE(DATE(2026,4,1), DATE(2031,9,15), 4.5%, 5%, 100, 4, 0)
```

**Result:** `97.62`

Quarterly payments of the same annual coupon slightly change the timing of the cash flows and therefore the price.

<!-- Image 2: Semiannual and Quarterly Results. See Images/Financial/PRICE.md -->

### Example 3: Wrap the Price in IFERROR

With the terms in `B2:B8`, where `B2` is settlement, `B3` is maturity, `B4` is the rate, `B5` is the yield, `B6` is the redemption value, `B7` is the frequency and `B8` is the basis:

```excel
=IFERROR(PRICE(B2, B3, B4, B5, B6, B7, B8), "Check inputs")
```

**Result:** `97.64`

If an input is invalid, the cell shows "Check inputs" instead of an error code.

## Story Problems

### Problem 1: Pricing a Bond for a Pension Fund

A pension fund considers buying a bond that pays a 6.00% coupon twice a year and matures on July 1, 2030. The fund settles the trade on August 20, 2026 and requires a yield of 5.20%. The bond repays 100 per 100 of face value at maturity.

| Term | Value |
| --- | --- |
| Settlement | 8/20/2026 |
| Maturity | 7/1/2030 |
| Coupon rate | 6.00% |
| Yield | 5.20% |
| Redemption | 100 |
| Frequency | 2 |
| Basis | 0 |

**Task:** Find the clean price per $100 face value the fund should pay.

**Solution:**

```excel
=PRICE(B2, B3, B4, B5, B6, B7, B8)
```

**Answer:** `102.76`, rounded to the cent. The bond sells above par because its coupon is higher than the required yield.

### Problem 2: Price Sensitivity When Yields Rise

The fund reviews the same bond if market yields rise to 6.50%. Use the terms from Problem 1, changing only the yield.

**Task:** Find the clean price if the required yield rises to 6.50%.

**Solution:**

```excel
=PRICE(B2, B3, B4, 0.065, B6, B7, B8)
```

**Answer:** `98.31`, rounded to the cent. The price falls by about 4.45 points, showing that a higher required yield lowers the bond's value.

<!-- Image 3: Story Problem Inputs and Output. See Images/Financial/PRICE.md -->

## Use Cases

### Investment Portfolio Valuation

**Scenario:** An asset manager marks a portfolio of coupon bonds at the current market yield at the end of each month.

```excel
=PRICE(SettlementDate, MaturityDate, CouponRate, MarketYield, 100, 2, 0)
```

**Why It Works:** Each bond uses its own dates and coupon, and the function returns a clean price that can be compared with the cost basis. Add accrued interest when the report needs the full market value.

### Yield Sensitivity Analysis

**Scenario:** A treasurer wants to know how a bond price changes if market yields move up or down by a fixed amount.

```excel
=PRICE(SettlementDate, MaturityDate, CouponRate, BaseYield + Shift, 100, 2, 0)
```

**Why It Works:** Changing only the yield argument isolates the effect of rates on price, which is the core question for interest rate risk.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The settlement date is on or after the maturity date. | Enter a settlement date earlier than maturity. |
| `#NUM!` | The rate or yield is negative. | Enter both as zero or positive decimals. |
| `#NUM!` | The redemption value is 0 or less. | Enter the redemption value per $100 of face value, usually `100`. |
| `#NUM!` | The frequency is not `1`, `2` or `4`. | Use the number of coupon payments per year. |
| `#NUM!` | The basis is outside 0 to 4. | Use `0`, `1`, `2`, `3` or `4`. |
| `#VALUE!` | A date argument is text instead of a date. | Enter dates with `DATE` or as true date values. |
| Price far too high or low | The rate was entered as `4.5` instead of `4.5%`. | Enter the rate as a percentage or a decimal such as `0.045`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | The optional argument is named `basis`. |
| Google Sheets | Available | The optional argument is named `day_count_convention` and uses the same codes 0 to 4. |

## Tips and Best Practices

- Enter the rate and yield as percentages, such as `4.5%`, so that the two inputs are read as the same kind of value.
- Use the day count basis stated in the bond's documents, because the basis changes the accrual days and the price.
- Use `DATE` for every date so the function does not depend on regional date formats.
- Use YIELD to check a result: the yield of the calculated price should return the yield you entered.
- Add accrued interest when you need the full amount the buyer pays, because PRICE returns a clean price.

## Related Functions

| Function | Relationship |
| --- | --- |
| [YIELD](YIELD.md) | Returns the yield for a given price, the reverse of this function. |
| [DURATION](DURATION.md) | Measures how sensitive the bond price is to changes in yield. |
| [ODDFPRICE](ODDFPRICE.md) | Prices a bond whose first coupon period is odd. |
| [PRICEMAT](PRICEMAT.md) | Prices a security that pays all of its interest at maturity. |
| [PRICEDISC](PRICEDISC.md) | Prices a discount security such as a Treasury bill. |

## Official Documentation

- [Microsoft Support: PRICE function](https://support.microsoft.com/en-us/excel/functions/price-function)
- [Google Docs Editors Help: PRICE](https://support.google.com/docs/answer/3093188)
