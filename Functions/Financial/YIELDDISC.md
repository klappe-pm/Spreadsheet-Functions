---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Investment Analysis
use-case:
  - Cash Reserve Comparison
  - Short-Term Discount Paper
  - Treasury Bill Returns
related:
  - DISC
  - PRICEDISC
  - TBILLYIELD
  - YIELD
  - YIELDMAT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/yielddisc-function
  - https://support.google.com/docs/answer/3093270
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Discount Security Yield
  - Annual Yield on a Discount Security
tags:
  - bond-math
  - day-count-basis
  - discount-security
  - excel
  - sheets
---

# YIELDDISC

## Description

**YIELDDISC** returns the annual yield of a discount security, which is a security that pays no coupons and is bought below its redemption value. You supply the settlement date (when the buyer takes ownership), the maturity date, the price per 100 of face value, the redemption value per 100, and an optional day count basis. The difference between the price and the redemption value is the return, and YIELDDISC annualizes it.

Use it to compare short-term discount securities, such as Treasury bills, that trade at different prices. For Treasury bills specifically, TBILLYIELD is the function built for that instrument. YIELDDISC takes the same inputs for any discount security.

## Syntax

```excel
=YIELDDISC(settlement, maturity, pr, redemption, [basis])
```

<!-- Image 1: Discount Security Layout. See Images/Financial/YIELDDISC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The settlement date, which is the date the buyer takes ownership. It must fall before the maturity date. Enter it with DATE or as a cell reference. |
| `maturity` | Yes | The date the security expires and the redemption value is paid. |
| `pr` | Yes | The price per 100 of face value, such as 98.20. Google Sheets names this argument `price`. |
| `redemption` | Yes | The amount paid per 100 of face value at maturity, usually 100. |
| `basis` | No | The day count basis: `0` or omitted for US (NASD) 30/360, `1` for actual/actual, `2` for actual/360, `3` for actual/365, and `4` for European 30/360. |

### Return Value

The annual yield as a decimal, such as 0.0725, which displays as 7.25% when the cell is formatted as a percentage. When an argument is invalid, the function returns an error; see Common Errors.

## Examples

All examples use this bill. The inputs sit in `B1:B5`, with labels in column A.

| Input | Cell | Value |
| --- | --- | --- |
| Settlement date | B1 | 2025-02-10 |
| Maturity date | B2 | 2025-05-12 |
| Price per 100 | B3 | 98.20 |
| Redemption per 100 | B4 | 100 |
| Day count basis | B5 | 2 |

### Example 1: Yield With Actual/360 Basis

```excel
=YIELDDISC(B1, B2, B3, B4, B5)
```

**Result:** `7.25%`

The bill returns 1.80 per 100 over 91 actual days, and the yield annualizes that gain on a 360-day year.

### Example 2: Omitting the Basis

```excel
=YIELDDISC(B1, B2, B3, B4)
```

**Result:** `7.17%`

Without the fifth argument, YIELDDISC uses US (NASD) 30/360, which counts this period as 92 days. The yield is slightly lower than in Example 1.

<!-- Image 2: Actual Days Versus 30/360 Days. See Images/Financial/YIELDDISC.md -->

### Example 3: Yield at a Higher Price

```excel
=YIELDDISC(B1, B2, 98.50, B4, B5)
```

**Result:** `6.02%`

Paying 98.50 instead of 98.20 shortens the return, so the annual yield falls.

### Example 4: Guarding Against Bad Dates

```excel
=IFERROR(YIELDDISC(B1, B2, B3, B4, B5), "Check dates")
```

**Result:** `7.25%`

If the settlement date is later than the maturity date, the cell shows `Check dates` instead of `#NUM!`.

## Story Problems

### Problem 1: Treasury Bill Purchase

An investor buys a discount bill on August 4, 2025 at 98.75 per 100 of face value. The bill matures on November 3, 2025 at 100. The investor uses actual/360 day counting.

| Input | Value |
| --- | --- |
| Settlement | 2025-08-04 |
| Maturity | 2025-11-03 |
| Price | 98.75 |
| Redemption | 100 |
| Basis | 2 |

**Task:** Find the annual yield on the bill.

**Solution:**

```excel
=YIELDDISC(DATE(2025,8,4), DATE(2025,11,3), 98.75, 100, 2)
```

**Answer:** `5.01%`. The 1.25 gain over 91 days annualizes to a yield of about 5.01 percent.

### Problem 2: Short Discount Note

A cash manager buys a discount note on September 15, 2025 at 99.10 per 100 of face value. The note matures on January 13, 2026 at 100, and the manager uses actual/360 counting.

| Input | Value |
| --- | --- |
| Settlement | 2025-09-15 |
| Maturity | 2026-01-13 |
| Price | 99.10 |
| Redemption | 100 |
| Basis | 2 |

**Task:** Find the annual yield on the note.

**Solution:**

```excel
=YIELDDISC(DATE(2025,9,15), DATE(2026,1,13), 99.10, 100, 2)
```

**Answer:** `2.72%`. The 0.90 gain over 120 days annualizes to about 2.72 percent, which is lower because the note is priced closer to its redemption value.

<!-- Image 3: Results Panel for the Story Problems. See Images/Financial/YIELDDISC.md -->

## Use Cases

### Treasury Bill Returns

**Scenario:** A treasurer compares the yield on bills of different maturities before deciding where to place surplus cash.

```excel
=YIELDDISC(Settle, Maturity, Price, 100, 2)
```

**Why It Works:** Each bill occupies one row with its own settlement, maturity and price. The same basis for every row keeps the yields comparable.

### Cash Reserve Comparison

**Scenario:** A business holds cash in discount paper and wants to know whether a shorter bill earns more than a longer one.

```excel
=YIELDDISC(Settle, Maturity, Price, 100)
```

**Why It Works:** Leaving out the basis applies US (NASD) 30/360 to every row. That is a consistent convention, though it can differ from the actual-day counts that some instruments use.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The price or redemption is zero or negative. | Enter positive values for both. |
| `#NUM!` | The settlement date is on or after the maturity date. | Check the order of the two dates. |
| `#NUM!` | The basis is less than 0 or greater than 4. | Use a basis code from 0 to 4. |
| `#VALUE!` | A date is text or is not a valid date. | Enter dates with DATE or as date values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current versions, including Excel for the web | The `basis` argument is optional and defaults to 0. |
| Google Sheets | Available | Same argument order. The basis is named `day_count_convention` and uses the same codes 0 to 4. The help page does not list error conditions. |

## Tips and Best Practices

- Use the same basis for every security in a comparison, or the yields are not directly comparable.
- Enter the price with at least three decimals, because small price changes move the yield noticeably on short securities.
- Use TBILLYIELD for Treasury bills so the calculation matches that instrument's convention.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DISC](DISC.md) | Discount rate of a security, a different measure from the annual yield. |
| [PRICEDISC](PRICEDISC.md) | Price per 100 of face value for a given discount rate, the reverse direction. |
| [TBILLYIELD](TBILLYIELD.md) | Yield for a Treasury bill. |
| [YIELD](YIELD.md) | Annual yield for a security that pays periodic coupons. |
| [YIELDMAT](YIELDMAT.md) | Annual yield for a security that pays interest at maturity. |

## Official Documentation

- [Microsoft Support: YIELDDISC function](https://support.microsoft.com/en-us/excel/functions/yielddisc-function)
- [Google Docs Editors Help: YIELDDISC](https://support.google.com/docs/answer/3093270)
