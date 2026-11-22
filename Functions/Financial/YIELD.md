---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Investment Analysis
use-case:
  - Bond Price Comparison
  - Municipal Bond Purchases
  - Treasury Note Yields
related:
  - COUPNUM
  - DURATION
  - PRICE
  - YIELDDISC
  - YIELDMAT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/yield-function
  - https://support.google.com/docs/answer/3093255
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bond Yield
  - Periodic Interest Yield
tags:
  - bond-math
  - day-count-basis
  - excel
  - fixed-income
  - sheets
---

# YIELD

## Description

**YIELD** returns the annual yield of a bond or other security that pays periodic interest, based on its market price. You supply the settlement date (when the buyer takes ownership), the maturity date, the annual coupon rate, the price per 100 of face value, the redemption value per 100, and the number of coupon payments per year. Use it to compare bonds with the same structure that trade at different prices or on different dates.

The function accepts coupon frequencies of 1, 2 or 4 per year. For securities that pay no coupons and trade at a discount, use YIELDDISC. For securities that pay all their interest at maturity, use YIELDMAT.

## Syntax

```excel
=YIELD(settlement, maturity, rate, pr, redemption, frequency, [basis])
```

<!-- Image 1: Bond Inputs Layout. See Images/Financial/YIELD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The settlement date, which is the date the buyer takes ownership. It must fall before the maturity date. Enter it with DATE or as a cell reference. |
| `maturity` | Yes | The date the security expires and the redemption value is paid. |
| `rate` | Yes | The annual coupon rate as a decimal, such as 0.04 for 4 percent. Negative rates return an error. |
| `pr` | Yes | The price per 100 of face value, such as 97.50. Google Sheets names this argument `price`. |
| `redemption` | Yes | The amount paid per 100 of face value at maturity, usually 100. |
| `frequency` | Yes | The number of coupon payments per year: 1 for annual, 2 for semiannual, or 4 for quarterly. |
| `basis` | No | The day count basis: `0` or omitted for US (NASD) 30/360, `1` for actual/actual, `2` for actual/360, `3` for actual/365, and `4` for European 30/360. |

### Return Value

The annual yield as a decimal, such as 0.0452, which displays as 4.52% when the cell is formatted as a percentage. When an argument is invalid, the function returns an error; see Common Errors.

## Examples

All examples use this bond. The inputs sit in `B1:B7`, with labels in column A.

| Input | Cell | Value |
| --- | --- | --- |
| Settlement date | B1 | 2025-03-15 |
| Maturity date | B2 | 2030-09-15 |
| Annual coupon rate | B3 | 0.04 |
| Price per 100 | B4 | 97.50 |
| Redemption per 100 | B5 | 100 |
| Coupons per year | B6 | 2 |
| Day count basis | B7 | 0 |

### Example 1: Yield With All Inputs

```excel
=YIELD(B1, B2, B3, B4, B5, B6, B7)
```

**Result:** `4.52%`

The bond costs 97.50 for every 100 of face value, so the buyer earns a little more than the 4 percent coupon as a yield.

### Example 2: Omitting the Basis

```excel
=YIELD(B1, B2, B3, B4, B5, B6)
```

**Result:** `4.52%`

When `basis` is left out, YIELD uses US (NASD) 30/360, the same as the value 0 in Example 1.

<!-- Image 2: Day Count Basis Codes. See Images/Financial/YIELD.md -->

### Example 3: Yield at a Lower Price

```excel
=YIELD(B1, B2, B3, 99, B5, B6, B7)
```

**Result:** `4.21%`

A higher price lowers the yield. At 99 per 100, the same bond yields 4.21 percent.

### Example 4: Rounded Yield for Lookups

```excel
=ROUND(YIELD(B1, B2, B3, B4, B5, B6, B7), 4)
```

**Result:** `0.0452`

Rounding the yield to four decimals gives a clean value for comparisons and lookup tables.

### Example 5: Flagging Bad Inputs

```excel
=IFERROR(YIELD(B1, B2, B3, B4, B5, 3, B7), "Check frequency")
```

**Result:** `Check frequency`

A frequency of 3 is not allowed, so the formula shows a message rather than `#NUM!`.

## Story Problems

### Problem 1: Municipal Bond Purchase

An investor buys a 5% coupon municipal bond on June 1, 2025 at a price of 96.20 per 100 of face value. The bond redeems at 100 on November 15, 2029 and pays coupons twice a year.

| Input | Value |
| --- | --- |
| Settlement | 2025-06-01 |
| Maturity | 2029-11-15 |
| Coupon rate | 0.05 |
| Price | 96.20 |
| Redemption | 100 |
| Frequency | 2 |

**Task:** Calculate the yield the investor earns, using US (NASD) 30/360.

**Solution:**

```excel
=YIELD(DATE(2025,6,1), DATE(2029,11,15), 0.05, 96.20, 100, 2, 0)
```

**Answer:** `5.98%`. The discount from 100 to 96.20 adds to the coupon income, so the yield is above the 5 percent coupon.

### Problem 2: Annual Government Note

A buyer pays 102.10 per 100 of face value for a note settling on January 15, 2025. The note pays 3.5% once a year and matures on January 15, 2028 at 100.

| Input | Value |
| --- | --- |
| Settlement | 2025-01-15 |
| Maturity | 2028-01-15 |
| Coupon rate | 0.035 |
| Price | 102.10 |
| Redemption | 100 |
| Frequency | 1 |

**Task:** Calculate the annual yield on the note.

**Solution:**

```excel
=YIELD(DATE(2025,1,15), DATE(2028,1,15), 0.035, 102.10, 100, 1)
```

**Answer:** `2.76%`. The premium paid above 100 reduces the yield below the 3.5 percent coupon.

<!-- Image 3: Results Panel for the Story Problems. See Images/Financial/YIELD.md -->

## Use Cases

### Municipal Bond Purchases

**Scenario:** A portfolio manager compares several bonds with the same maturity date but different coupons and prices.

```excel
=YIELD(Settle, Maturity, Coupon, Price, 100, 2, 0)
```

**Why It Works:** Each row supplies its own coupon and price, so the yields can be compared on one basis. Using the same basis for every row keeps the comparison fair.

### Bond Price Comparison

**Scenario:** A treasurer decides whether a bond offered at 98.50 beats one offered at 99.25 with the same coupon and maturity.

```excel
=YIELD(Settle, Maturity, Coupon, Offer, 100, 2, 0)
```

**Why It Works:** Running the same formula on each offered price converts both offers to an annual yield on the same basis, so the offer with the higher yield is easy to identify.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | Frequency is not 1, 2 or 4. | Enter 1 for annual, 2 for semiannual, or 4 for quarterly. |
| `#NUM!` | Settlement is on or after maturity. | Check the order of the two dates. |
| `#NUM!` | The price or redemption is zero or negative, or the rate is negative. | Enter positive price and redemption values and a rate of zero or more. |
| `#NUM!` | The basis is less than 0 or greater than 4. | Use a basis code from 0 to 4. |
| `#VALUE!` | A date is text or is not a valid date. | Enter dates with DATE or as date values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions, including Excel for the web | The `basis` argument is optional and defaults to 0. |
| Google Sheets | Available | Same argument order. The basis is named `day_count_convention`, uses the same codes 0 to 4, and the help page does not list error conditions. |

## Tips and Best Practices

- Use the same basis code for every bond in a comparison, because a different basis changes the result.
- Enter the coupon rate in a percentage-formatted cell so it reads as 4% while the formula receives 0.04.
- Check a yield by passing it to PRICE with the same inputs; the price should return the original value.
- Wrap rows in IFERROR in a long bond list so one bad date does not hide the others.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PRICE](PRICE.md) | Price per 100 of face value for a given yield, the reverse of YIELD. |
| [DURATION](DURATION.md) | Weighted average time to receive the bond's cash flows, used with yield for rate risk. |
| [COUPNUM](COUPNUM.md) | Number of coupon payments between settlement and maturity. |
| [YIELDDISC](YIELDDISC.md) | Annual yield for a discount security that pays no coupons. |
| [YIELDMAT](YIELDMAT.md) | Annual yield for a security that pays all interest at maturity. |

## Official Documentation

- [Microsoft Support: YIELD function](https://support.microsoft.com/en-us/excel/functions/yield-function)
- [Google Docs Editors Help: YIELD](https://support.google.com/docs/answer/3093255)
