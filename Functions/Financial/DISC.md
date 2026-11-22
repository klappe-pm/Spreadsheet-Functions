---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
use-case:
  - Bond Purchase Comparison
  - Short-Term Investment Screening
  - Treasury Bill Discount Rate
related:
  - PRICE
  - PRICEDISC
  - TBILLEQ
  - YIELD
  - YIELDDISC
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/disc-function
  - https://support.google.com/docs/answer/3093216
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Discount Rate
  - Security Discount Rate
tags:
  - bonds
  - day-count
  - discount-rate
  - excel
  - sheets
---

# DISC

## Description

**DISC** returns the discount rate for a security that is bought below its redemption value and pays no interest before maturity. Treasury bills and some commercial paper work this way: the buyer pays a price below par, and the difference between that price and the redemption value is the return. DISC converts that difference into an annual rate, so you can compare the security with other investments that quote a yearly rate.

The calculation needs four dates and amounts: the settlement date when the buyer takes ownership, the maturity date when the security expires, the price per 100 of face value, and the redemption value per 100. The optional `basis` argument sets how days are counted. A basis of 2 uses an actual day count over a 360-day year, which is common for money-market instruments. A basis of 0 uses the US 30/360 convention, where every month is treated as 30 days.

DISC is the discount-rate counterpart of [PRICEDISC](PRICEDISC.md), which returns the price for a given discount rate, and [YIELDDISC](YIELDDISC.md), which returns the yield on a discounted security. For securities that pay coupons, use [YIELD](YIELD.md) and [PRICE](PRICE.md) instead. [TBILLEQ](TBILLEQ.md) gives the bond-equivalent yield for Treasury bills.

Google Sheets provides DISC with the same arguments under the names `price`, `redemption` and `day_count_convention`. Its help page does not describe the return value or error behavior, so check results against Excel before relying on them.

## Syntax

```excel
=DISC(settlement, maturity, pr, redemption, [basis])
```

<!-- Image 1: DISC Date and Price Layout. See Images/Financial/DISC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer takes ownership of the security, after issue. Enter it with `DATE` or as the result of another formula. |
| `maturity` | Yes | The date the security expires. It must fall after the settlement date. |
| `pr` | Yes | The price per 100 of face value. Must be greater than 0. |
| `redemption` | Yes | The redemption value per 100 of face value. Must be greater than 0. |
| `basis` | No | The day count basis. `0` or omitted is US (NASD) 30/360. `1` is actual/actual, `2` is actual/360, `3` is actual/365 and `4` is European 30/360. |

### Return Value

A decimal rate for the discount. The calculation is `(redemption - pr) / redemption` multiplied by `B / DSM`, where `DSM` is the number of days from settlement to maturity and `B` is the number of days in the year for the chosen basis. The function returns `#VALUE!` when a date is not valid, and `#NUM!` when `pr` or `redemption` is 0 or less, when `basis` is below 0 or above 4, or when settlement is on or after maturity.

## Examples

All examples use a security that settles on 15 February 2026 and matures on 15 August 2026, with a price of 98.5 and a redemption value of 100.

### Example 1: US 30/360 Basis

```excel
=DISC(DATE(2026,2,15), DATE(2026,8,15), 98.5, 100, 0)
```

**Result:** `0.030000`

Under 30/360, the period from 15 February to 15 August counts as 180 days. The discount is 1.5 points, so the annual rate is 1.5 divided by 100, times 360 divided by 180, which is 3%.

### Example 2: Actual/360 Basis

```excel
=DISC(DATE(2026,2,15), DATE(2026,8,15), 98.5, 100, 2)
```

**Result:** `0.029834`

The actual number of days is 181, so the rate is 1.5 divided by 100, times 360 divided by 181. Money-market instruments often use this basis.

### Example 3: Actual/365 Basis

```excel
=DISC(DATE(2026,2,15), DATE(2026,8,15), 98.5, 100, 3)
```

**Result:** `0.030249`

The same 181 days now use a 365-day year, so the rate is slightly higher than on the actual/360 basis.

### Example 4: Ninety-Day Bill

```excel
=DISC(DATE(2026,3,1), DATE(2026,5,30), 99.2, 100, 2)
```

**Result:** `0.032000`

The 90 days from 1 March to 30 May are divided into a 360-day year, which gives a discount of 0.8 points at an annual rate of 3.2%.

<!-- Image 2: Day Count Basis Comparison. See Images/Financial/DISC.md -->

## Story Problems

### Problem 1: Six-Month Treasury Bill

An investor buys a six-month Treasury bill that settles on 1 March 2026 and matures on 1 September 2026. The price is 97.25 per 100 of face value. The investor wants the discount rate on an actual/360 basis.

| Input | Value |
| --- | --- |
| Settlement date | 2026-03-01 |
| Maturity date | 2026-09-01 |
| Price per 100 | 97.25 |
| Redemption value | 100 |

**Task:** Enter the dates in `B2` and `B3`, the price in `B4` and the redemption value in `B5`, then find the discount rate with basis 2.

**Solution:**

```excel
=DISC(B2, B3, B4, B5, 2)
```

**Answer:** `0.053804`, or about 5.38%. The bill has 184 days to maturity, so the discount of 2.75 points is spread over 184 days of a 360-day year.

### Problem 2: Corporate Discount Note

A company sells a 90-day note that settles on 15 January 2026 and matures on 15 April 2026. It is priced at 99 per 100, and the redemption value is 100. The treasurer uses the 30/360 convention set in the company policy.

| Input | Value |
| --- | --- |
| Settlement date | 2026-01-15 |
| Maturity date | 2026-04-15 |
| Price per 100 | 99 |
| Redemption value | 100 |

**Task:** Find the discount rate using basis 0.

**Solution:**

```excel
=DISC(B2, B3, B4, B5, 0)
```

**Answer:** `0.040000`, or 4%. Under 30/360 the note has 90 days, so the 1-point discount is annualized as 1 divided by 100, times 360 divided by 90.

## Use Cases

### Treasury Bill Discount Rate

**Scenario:** A cash manager compares short-term bills from several auctions using the discount rate quoted in each prospectus.

```excel
=DISC(SettleDate, MatureDate, Price, 100, 2)
```

**Why It Works:** Each row holds one bill's dates and price, so the rates can be sorted and compared on the same basis.

### Bond Purchase Comparison

**Scenario:** An investor decides between a discounted security and a bank deposit paying a fixed annual rate.

```excel
=DISC(Settle, Maturity, Price, 100, 3)
```

**Why It Works:** Converting the discount to an annual rate makes the security comparable with deposits and other quoted rates. Use the same basis as the deposit's day count to avoid a false difference.

### Short-Term Investment Screening

**Scenario:** A treasury team lists several short-term securities on one sheet and ranks them by discount rate.

```excel
=DISC(B2, C2, D2, 100, 2)
```

**Why It Works:** Each row holds one security's settlement date, maturity date and price. Copying the formula down gives one rate per row, which can then be sorted and compared with a target rate.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A date is not a valid date, often because it was typed as text. | Enter dates with `DATE` or convert the text to a date. |
| `#NUM!` | `pr` or `redemption` is 0 or negative. | Enter the price and redemption value per 100 as positive numbers. |
| `#NUM!` | `basis` is below 0 or above 4. | Use a whole number from 0 to 4. |
| `#NUM!` | Settlement is on or after the maturity date. | Check that the settlement date comes before the maturity date. |
| Rate differs from a broker quote | The broker uses a different day count basis. | Compare the basis in the quote and set `basis` to match. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions listed on the Microsoft page | Basis values 0 to 4 are documented. Errors follow the rules in the Return Value section. |
| Google Sheets | Available | The argument is named `day_count_convention` and uses the same values 0 to 4. The help page does not describe the return value or error behavior. |

## Tips and Best Practices

- Enter dates with `DATE` so that they are read as serial numbers and not as text.
- Use the day count basis from the security's offering document, because each basis gives a different rate.
- Convert the discount rate to a yield with [YIELDDISC](YIELDDISC.md) when you need to compare with a bond that pays interest.
- Store the price and redemption value in separate cells so that a sensitivity table can test different prices.
- Check the number of days to maturity before reporting a rate, since very short securities amplify small price changes.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PRICEDISC](PRICEDISC.md) | Returns the price per 100 for a given discount rate. |
| [YIELDDISC](YIELDDISC.md) | Returns the yield on a discounted security. |
| [TBILLEQ](TBILLEQ.md) | Returns the bond-equivalent yield of a Treasury bill. |
| [PRICE](PRICE.md) | Returns the price of a security that pays periodic interest. |
| [YIELD](YIELD.md) | Returns the yield of a security that pays periodic interest. |

## Official Documentation

- [Microsoft Support: DISC function](https://support.microsoft.com/en-us/excel/functions/disc-function)
- [Google Docs Editors Help: DISC](https://support.google.com/docs/answer/3093216)
