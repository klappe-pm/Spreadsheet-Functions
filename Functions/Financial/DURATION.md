---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Bond Interest Rate Sensitivity
  - Portfolio Duration Check
  - Zero-Coupon Comparison
related:
  - ACCRINT
  - COUPDAYBS
  - MDURATION
  - PRICE
  - YIELD
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/duration-function
  - https://support.google.com/docs/answer/3093169
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Macaulay Duration
  - Bond Duration
tags:
  - bonds
  - excel
  - macaulay-duration
  - sheets
---

# DURATION

## Description

**DURATION** returns the Macaulay duration of a security that pays periodic interest, which is the weighted average time, in years, until the investor receives the bond's cash flows. Each coupon and the final principal payment count toward the average, weighted by its present value. A bond with large early coupons has a short duration, and a bond whose value sits mostly in its final payment has a duration close to its remaining life.

Duration matters because it measures how sensitive a bond's price is to changes in interest rates. A bond with a duration of 4 loses roughly 4% of its value when yields rise by one percentage point. Portfolio managers use duration to match assets with liabilities and to compare bonds with different coupons and maturities on a common scale. Excel calculates the duration for a par value of 100.

The function takes the settlement and maturity dates, the annual coupon rate, the annual yield, the number of coupon payments per year, and an optional day count basis. The coupon rate and yield are annual figures even when the bond pays semiannually or quarterly. To convert the result to modified duration, divide it by `1 + yield / frequency`, which is the relationship that [MDURATION](MDURATION.md) uses.

Google Sheets provides DURATION with the same arguments. Its help page describes the function in different terms and does not show example outputs, so compare a Sheets result with a manual calculation before relying on it. Use [PRICE](PRICE.md) and [YIELD](YIELD.md) to find the price and yield of the same security.

## Syntax

```excel
=DURATION(settlement, maturity, coupon, yld, frequency, [basis])
```

<!-- Image 1: DURATION Argument Layout. See Images/Financial/DURATION.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the security. Enter it with `DATE` or as the result of another formula. |
| `maturity` | Yes | The date the security expires. It must fall after the settlement date. |
| `coupon` | Yes | The annual coupon rate, entered as a decimal such as 0.05 for 5%. Must be 0 or greater. |
| `yld` | Yes | The annual yield, entered as a decimal such as 0.06 for 6%. Must be 0 or greater. |
| `frequency` | Yes | The number of coupon payments per year. Allowed values are 1 (annual), 2 (semiannual) and 4 (quarterly). |
| `basis` | No | The day count basis. `0` or omitted is US (NASD) 30/360. `1` is actual/actual, `2` is actual/360, `3` is actual/365 and `4` is European 30/360. |

### Return Value

A decimal number giving the Macaulay duration in years for a security with a par value of 100. The function returns `#VALUE!` when a date is not valid, and `#NUM!` when `coupon` or `yld` is negative, when `frequency` is not 1, 2 or 4, when `basis` is below 0 or above 4, or when settlement is on or after maturity.

## Examples

### Example 1: Semiannual Bond With a Settlement on a Coupon Date

Inputs: settlement 15 January 2026, maturity 15 January 2029, coupon 5%, yield 6%, semiannual, basis 0.

```excel
=DURATION(DATE(2026,1,15), DATE(2029,1,15), 0.05, 0.06, 2, 0)
```

**Result:** `2.820003`

Six coupon payments of 2.50 and a final principal payment of 100 are discounted at 3% per half year. The weighted average time is about 2.82 years.

### Example 2: Annual Coupon Payments

```excel
=DURATION(DATE(2026,1,15), DATE(2029,1,15), 0.05, 0.06, 1, 0)
```

**Result:** `2.857347`

Paying the same coupon once a year instead of twice moves the cash flows later, so the duration is slightly longer.

### Example 3: Modified Duration From Macaulay Duration

```excel
=DURATION(DATE(2026,1,15), DATE(2029,1,15), 0.05, 0.06, 2, 0) / (1 + 0.06/2)
```

**Result:** `2.737867`

Dividing by `1 + yield / frequency` gives the modified duration, which estimates the percentage change in price for a one-point change in yield.

### Example 4: Zero-Coupon Bond

```excel
=DURATION(DATE(2026,1,15), DATE(2029,1,15), 0, 0.06, 2, 0)
```

**Result:** `3`

With no coupons, the only cash flow is the principal at maturity. The duration equals the time to maturity, which is exactly 3 years here.

<!-- Image 2: Bond Cash Flow Timeline. See Images/Financial/DURATION.md -->

## Story Problems

### Problem 1: Annual Bond Interest Sensitivity

A pension fund buys a 3-year bond with an annual coupon of 4% on 1 January 2026. The market yield is 5%. The fund's analyst wants the Macaulay duration to compare with the fund's liabilities.

| Input | Value |
| --- | --- |
| Settlement date | 2026-01-01 |
| Maturity date | 2029-01-01 |
| Annual coupon | 0.04 |
| Annual yield | 0.05 |
| Payments per year | 1 |

**Task:** Put the dates in `B2` and `B3`, the coupon in `B4`, the yield in `B5` and the frequency in `B6`, then find the duration.

**Solution:**

```excel
=DURATION(B2, B3, B4, B5, B6)
```

**Answer:** About `2.884`, which means the bond's average cash flow arrives roughly 2.88 years after settlement. The bond's price per 100 of face value is about 97.28, so the discount to par reflects the yield above the coupon.

### Problem 2: Portfolio Check on a Ten-Period Bond

A manager holds a 5-year bond with a 7% coupon paid semiannually and a yield of 8%. The bond settles on 15 January 2026 and matures on 15 January 2031. The manager wants the duration to compare with the portfolio's target of about 4.3 years.

| Input | Value |
| --- | --- |
| Settlement date | 2026-01-15 |
| Maturity date | 2031-01-15 |
| Annual coupon | 0.07 |
| Annual yield | 0.08 |
| Payments per year | 2 |

**Task:** Find the Macaulay duration with the same input cells.

**Solution:**

```excel
=DURATION(B2, B3, B4, B5, B6, 0)
```

**Answer:** About `4.287`. The bond is just below the 4.3 year target on a Macaulay basis, so the manager will check the modified duration as well.

## Use Cases

### Bond Interest Rate Sensitivity

**Scenario:** A treasury team estimates how much the value of its bond holdings would fall if market yields rose by one percentage point.

```excel
=DURATION(Settle, Maturity, Coupon, Yield, Frequency) / (1 + Yield/Frequency)
```

**Why It Works:** Modified duration converts the Macaulay figure into a price sensitivity. Multiplying it by the position size estimates the change in value for a one-point move in yield.

### Portfolio Duration Check

**Scenario:** A fund manager compares the duration of each holding with the average duration the fund must maintain.

```excel
=SUMPRODUCT(Weights, Durations)
```

**Why It Works:** Each bond's duration is calculated with DURATION, and SUMPRODUCT weights the results by each holding's share of the portfolio.

### Zero-Coupon Comparison

**Scenario:** An investor compares a zero-coupon bond with a coupon bond of the same maturity to see which one is more sensitive to rate changes.

```excel
=DURATION(Settle, Maturity, 0, Yield, 2)
```

**Why It Works:** A zero-coupon bond has a duration equal to its time to maturity, which gives a clear benchmark for coupon bonds of the same term.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A date is not valid, often because it was typed as text. | Enter dates with `DATE` or convert the text to a date. |
| `#NUM!` | `frequency` is a value other than 1, 2 or 4. | Enter 1 for annual, 2 for semiannual or 4 for quarterly payments. |
| `#NUM!` | `coupon` or `yld` is negative. | Enter the rates as non-negative decimals. |
| `#NUM!` | `basis` is below 0 or above 4, or settlement is on or after maturity. | Use a basis from 0 to 4 and check the date order. |
| Result is far too large | The coupon or yield was entered as a whole number, such as 5 for 5%. | Enter the rate as a decimal, such as 0.05. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions listed on the Microsoft page | Returns Macaulay duration for a par value of 100. Frequency must be 1, 2 or 4. |
| Google Sheets | Available | The arguments are named `settlement`, `maturity`, `rate`, `yield`, `frequency` and `day_count_convention`. The help page describes the function in different terms and gives no example outputs, so confirm results against a manual calculation. |

## Tips and Best Practices

- Enter the coupon and yield as decimals and keep them in cells with percentage formatting.
- Use the same day count basis as the bond's prospectus, since the basis affects the cash flow dates.
- Convert to modified duration when you need a price sensitivity, rather than reading the Macaulay figure as a percentage change.
- Settle the bond on a coupon date when you want a result that matches a simple cash flow table, as in Example 1.
- Check a new spreadsheet against a manual calculation of the cash flows before you rely on it for risk limits.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MDURATION](MDURATION.md) | Returns the modified duration, which measures price sensitivity directly. |
| [PRICE](PRICE.md) | Returns the price of the security from its yield. |
| [YIELD](YIELD.md) | Returns the yield of the security from its price. |
| [COUPDAYBS](COUPDAYBS.md) | Returns the days from the last coupon to settlement, which affects the accrued interest. |
| [ACCRINT](ACCRINT.md) | Returns the accrued interest on a security that pays periodic interest. |

## Official Documentation

- [Microsoft Support: DURATION function](https://support.microsoft.com/en-us/excel/functions/duration-function)
- [Google Docs Editors Help: DURATION](https://support.google.com/docs/answer/3093169)
