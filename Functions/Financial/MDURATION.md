---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Investment Analysis
use-case:
  - Bond Price Sensitivity
  - Interest Rate Risk Review
  - Portfolio Duration Check
related:
  - ACCRINT
  - DURATION
  - INTRATE
  - PRICE
  - YIELD
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/mduration-function
  - https://support.google.com/docs/answer/3093178
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bond Price Sensitivity
  - Modified Macaulay Duration
tags:
  - bonds
  - duration
  - excel
  - interest-rate-risk
  - sheets
---

# MDURATION

## Description

**MDURATION** returns the modified Macaulay duration of a security that pays periodic interest, using an assumed par value of 100. Modified duration measures how sensitive the security's price is to a change in yield. A bond with a modified duration of 4.30 loses about 4.30% of its price for each one percentage point rise in yield, and gains about the same for each one point fall.

The function starts from the Macaulay duration, which is the weighted average time until the bond's cash flows arrive, and divides it by one plus the yield per coupon period. Use it to compare bonds with different coupons, maturities and yields, and to estimate price risk before a rate change.

Coupon payments per year must be 1, 2 or 4. The day count basis matters for bonds with dates that fall between coupon dates, so use the basis in the bond's terms.

## Syntax

```excel
=MDURATION(settlement, maturity, coupon, yld, frequency, [basis])
```

<!-- Image 1: Bond Dates, Coupon and Yield Arguments. See Images/Financial/MDURATION.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership. Enter it with `DATE`, not as text. |
| `maturity` | Yes | The date the security expires and the par value is repaid. |
| `coupon` | Yes | The annual coupon rate, entered as a decimal or percentage. |
| `yld` | Yes | The annual yield, entered as a decimal or percentage. Must not be negative. |
| `frequency` | Yes | Coupon payments per year: 1 for annual, 2 for semiannual, or 4 for quarterly. Other values return `#NUM!`. |
| `basis` | No | The day count basis: 0 or omitted for US (NASD) 30/360, 1 for actual/actual, 2 for actual/360, 3 for actual/365, and 4 for European 30/360. |

### Return Value

A number of years, such as `4.30`, measured on a 100 par value. The function returns `#VALUE!` when a date is not valid, and `#NUM!` when the coupon or yield is negative, the frequency is not 1, 2 or 4, the basis is outside 0 to 4, or settlement is on or after maturity.

## Examples

### Example 1: Semiannual Bond

Inputs in `B2` to `B6`: settlement `1/15/2025`, maturity `1/15/2030`, coupon `6%`, yield `5%`, and frequency `2`.

```excel
=MDURATION(B2, B3, B4, B5, B6)
```

**Result:** `4.30`

The bond pays 3.00 every six months for ten periods, and its cash flows are discounted at 2.5% per period.

### Example 2: Annual Coupons

The same bond with a frequency of `1`:

```excel
=MDURATION(B2, B3, B4, B5, 1)
```

**Result:** `4.26`

Fewer, larger coupon payments put the average cash flow slightly later, but the modified duration is still close to the semiannual result.

### Example 3: Estimated Price Change

```excel
=-MDURATION(B2, B3, B4, B5, B6) * 0.01
```

**Result:** `-4.30%`

For a one percentage point rise in yield, the price falls by about 4.30%. The result is an estimate for small yield changes, because the price curve bends, so the estimate drifts for large moves.

### Example 4: Catching a Frequency Error

```excel
=IFERROR(MDURATION(B2, B3, B4, B5, 3), "Use frequency 1, 2 or 4")
```

**Result:** `Use frequency 1, 2 or 4`

A frequency of 3 is not allowed, so the function returns `#NUM!` and `IFERROR` replaces it with a message.

<!-- Image 2: Price Change for a Yield Move. See Images/Financial/MDURATION.md -->

## Story Problems

### Problem 1: Five Year Corporate Bond

An investor buys a five-year bond with a 6% coupon, paid semiannually, when the market yield is 5%. The settlement and maturity dates are in the table below.

| Item | Value |
| --- | --- |
| Settlement date | 1/15/2025 |
| Maturity date | 1/15/2030 |
| Coupon rate | 6% |
| Yield | 5% |
| Frequency | 2 |

**Task:** Calculate the modified duration in years.

**Solution:**

```excel
=MDURATION(DATE(2025,1,15), DATE(2030,1,15), 6%, 5%, 2)
```

**Answer:** `4.30` years. The bond's price is about 104.38 per 100 of par, and the duration measures its sensitivity to yield.

### Problem 2: Price Change After a Rate Rise

The same investor expects yields to rise by 0.5 percentage points next quarter. The duration from Problem 1 is in `E2`.

| Item | Value |
| --- | --- |
| Modified duration | 4.30 |
| Yield change | 0.5 percentage points |

**Task:** Estimate the percentage change in the bond's price.

**Solution:**

```excel
=-E2 * 0.5%
```

**Answer:** About `-2.15%`. The price falls by roughly 2.15% for a half point rise in yield.

<!-- Image 3: Duration Results for the Bond Problems. See Images/Financial/MDURATION.md -->

## Use Cases

### Bond Price Sensitivity

**Scenario:** A treasury analyst needs to show how much a bond portfolio's value would move if market yields rose by one point.

```excel
=-MDURATION(Settle, Maturity, Coupon, Yield, Frequency) * 0.01
```

**Why It Works:** The formula gives an approximate percentage change for each bond. Multiply by the market value of each position to get a dollar estimate.

### Interest Rate Risk Review

**Scenario:** A pension committee compares two bonds with the same maturity but different coupons before choosing one.

```excel
=MDURATION(Settle, Maturity, CouponA, YieldA, 2)
```

**Why It Works:** Calculate the same formula for each bond with its own coupon and yield, then compare the results. A higher modified duration means more price risk for the same yield change.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The frequency is not 1, 2 or 4. | Enter 1 for annual, 2 for semiannual or 4 for quarterly coupons. |
| `#NUM!` | The coupon or yield is negative, or settlement is on or after maturity. | Check the sign of the rates and the order of the dates. |
| `#VALUE!` | A date is text, not a date value. | Enter the dates with `DATE`. |
| Result looks too large or too small | The yield was entered per coupon period instead of per year. | Enter the annual yield, which the function divides by the frequency. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Microsoft 365 and Excel for the web | Takes coupon and yld as annual rates and the frequency as 1, 2 or 4. |
| Google Sheets | Available | Uses `rate` and `yield` as argument names in the same positions. The page does not state the return value or error conditions. |

## Tips and Best Practices

- Use the modified duration to estimate price change for small yield moves, and recalculate for large ones.
- Pair MDURATION with `DURATION` when you need the Macaulay duration before the yield adjustment.
- Use the same basis for every bond in a comparison so that the results are consistent.
- Enter the coupon and yield as annual rates even when the bond pays quarterly or semiannually.
- Use `PRICE` and `YIELD` together to check that the bond's price and yield are consistent with the duration.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DURATION](DURATION.md) | Macaulay duration before the yield adjustment. |
| [PRICE](PRICE.md) | Price per 100 of par at a given yield, the base for a price change estimate. |
| [YIELD](YIELD.md) | Yield at a given price, the input that sets the discount rate. |
| [INTRATE](INTRATE.md) | Rate for a fully invested security with no periodic coupons. |
| [ACCRINT](ACCRINT.md) | Accrued interest on a security between coupon dates. |

## Official Documentation

- [Microsoft Support: MDURATION function](https://support.microsoft.com/en-us/excel/functions/mduration-function)
- [Google Docs Editors Help: MDURATION](https://support.google.com/docs/answer/3093178)
