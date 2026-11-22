---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Investment Analysis
use-case:
  - Cash Management Investments
  - Short Term Note Yield
  - Treasury Purchase Comparison
related:
  - DISC
  - MDURATION
  - PRICE
  - RECEIVED
  - TBILLEQ
  - YIELD
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/intrate-function
  - https://support.google.com/docs/answer/3093174
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Fully Invested Security Rate
  - Security Interest Rate
tags:
  - bonds
  - day-count-basis
  - excel
  - sheets
---

# INTRATE

## Description

**INTRATE** returns the interest rate for a fully invested security. A fully invested security is paid for in full at settlement, pays no periodic interest, and returns a single redemption amount at maturity. Use it for short-term notes and discount-style securities bought at one price and redeemed at a face amount.

The result depends on the day count basis as well as the amounts. The same dates and amounts can give noticeably different rates: in Example 2 below, basis 0 (US 30/360) returns 4.08% where basis 2 (actual/360) returns 3.99%. Use the basis written in the security's terms. The default is basis 0.

Google Sheets has a function with the same name but a different argument list. Sheets takes buy and sell dates and prices, not settlement, maturity, investment and redemption. Do not copy an Excel INTRATE formula into Sheets.

## Syntax

```excel
=INTRATE(settlement, maturity, investment, redemption, [basis])
```

<!-- Image 1: Settlement, Maturity and Amount Cells. See Images/Financial/INTRATE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the buyer acquires the security, after its issue date. Enter it with `DATE` or as the result of another formula. |
| `maturity` | Yes | The date the security expires and the redemption amount is paid. |
| `investment` | Yes | The amount paid for the security. Must be greater than 0. |
| `redemption` | Yes | The amount received at maturity. Must be greater than 0. |
| `basis` | No | The day count basis: 0 or omitted for US (NASD) 30/360, 1 for actual/actual, 2 for actual/360, 3 for actual/365, and 4 for European 30/360. |

### Return Value

A decimal rate such as `0.0399`, displayed as a percentage when the cell is formatted that way. The function returns `#VALUE!` when settlement or maturity is not a valid date, and `#NUM!` when the investment or redemption is 0 or less, the basis is outside 0 to 4, or settlement is on or after maturity.

## Examples

All examples use these inputs: settlement in `B2` is `3/1/2025`, maturity in `B3` is `9/1/2025`, investment in `B4` is `980000`, redemption in `B5` is `1000000`, and basis in `B6` is `2`. The period from settlement to maturity is 184 actual days.

### Example 1: Actual/360 Basis

```excel
=INTRATE(B2, B3, B4, B5, B6)
```

**Result:** `3.99%`

The 20,000 gain on a 980,000 purchase, annualized on an actual/360 basis over 184 days, gives 3.99%.

### Example 2: Default 30/360 Basis

```excel
=INTRATE(B2, B3, B4, B5)
```

**Result:** `4.08%`

Basis 0 counts the same six months as 180 days, so the same amounts produce a higher rate than basis 2.

<!-- Image 2: Day Count Basis Comparison. See Images/Financial/INTRATE.md -->

### Example 3: Actual/365 Basis

```excel
=INTRATE(B2, B3, B4, B5, 3)
```

**Result:** `4.05%`

Actual/365 uses a 365-day year, which sits between the other two results for this period.

### Example 4: Catching a Date Error

```excel
=IFERROR(INTRATE(B3, B2, B4, B5, B6), "Check the dates")
```

**Result:** `Check the dates`

The dates are reversed, so settlement falls after maturity and the function returns `#NUM!`. `IFERROR` replaces that error with a readable message.

## Story Problems

### Problem 1: Six Month Note Yield

A city treasurer buys a six-month note for 980,000 and receives 1,000,000 at maturity. The settlement and maturity dates are in the table below.

| Item | Value |
| --- | --- |
| Settlement date | 3/1/2025 |
| Maturity date | 9/1/2025 |
| Purchase price | 980000 |
| Redemption amount | 1000000 |

**Task:** Calculate the annual rate on an actual/360 basis, with the basis entered as `2`.

**Solution:**

```excel
=INTRATE(DATE(2025,3,1), DATE(2025,9,1), 980000, 1000000, 2)
```

**Answer:** `3.99%`. The gain of 20,000 on 980,000, over 184 days on an actual/360 basis, gives 3.99%.

### Problem 2: Comparing Two Notes

Two notes settle on 3/1/2025 and mature on 9/1/2025 with a redemption of 1,000,000. The purchase prices differ, as shown in the table.

| Note | Purchase Price | Redemption |
| --- | --- | --- |
| Note A | 980000 | 1000000 |
| Note B | 975000 | 1000000 |

**Task:** Calculate the rate for each note on an actual/360 basis and state which note earns more.

**Solution:**

```excel
=INTRATE(DATE(2025,3,1), DATE(2025,9,1), B2, C2, 2)
```

Fill the formula down one row, so Note B uses `B3` and `C3`.

**Answer:** Note A earns `3.99%` and Note B earns `5.02%`. Note B costs less for the same redemption, so it earns more.

<!-- Image 3: Note Comparison Results. See Images/Financial/INTRATE.md -->

## Use Cases

### Cash Management Investments

**Scenario:** A company holds surplus cash in short-term notes and needs the yield on each purchase before it approves the order.

```excel
=INTRATE(SettleDate, MaturityDate, Price, FaceValue, 2)
```

**Why It Works:** The named ranges hold the terms of each note, so the same formula can be filled down a list of purchases. Confirm the basis in the offering terms before filling the formula down.

### Short Term Note Yield

**Scenario:** A finance team wants to know whether a note bought at a discount beats the yield on its bank deposit.

```excel
=IF(INTRATE(B2, B3, B4, B5, 2) > DepositRate, "Note wins", "Deposit wins")
```

**Why It Works:** The comparison uses the same basis as the deposit quote. A mismatched basis can flip the answer on close calls, so align the day count before comparing.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The settlement or maturity is text, not a date. | Enter the dates with `DATE` or as results of date formulas. |
| `#NUM!` | Settlement is on or after maturity. | Check that the settlement date comes before the maturity date. |
| `#NUM!` | The investment or redemption is 0 or less, or the basis is outside 0 to 4. | Enter positive amounts and a basis from 0 to 4. |
| Rate differs from the quote | The default 30/360 basis was used, but the terms specify actual/360. | Enter the basis from the security's terms. |
| Wrong result in Sheets | An Excel formula was copied into Sheets, where the arguments are different. | Rewrite the formula with the Sheets argument order. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, Excel 2019, Excel 2021, Excel 2024, Microsoft 365, Excel for the web and Excel for iPhone | Takes settlement, maturity, investment, redemption and an optional basis from 0 to 4. |
| Google Sheets | Available | Takes buy date, sell date, buy price, sell price and an optional day count convention from 0 to 4. The page does not state the return value or error conditions. |

## Tips and Best Practices

- Enter dates with `DATE` so that they are numbers and not text.
- Use the basis written in the security's terms, not the default, unless the terms say basis 0.
- Use `YIELD` for bonds that pay periodic coupons, because INTRATE assumes no interest before maturity.
- Use `MDURATION` with a bond's yield to estimate how much its price moves when yields change.
- Wrap the formula in `IFERROR` when the dates come from a data import, so that one bad row does not break a whole column.

## Related Functions

| Function | Relationship |
| --- | --- |
| [YIELD](YIELD.md) | Yield for a bond that pays periodic interest. |
| [PRICE](PRICE.md) | Price per 100 of face value for a coupon-paying security at a given yield. |
| [RECEIVED](RECEIVED.md) | Amount received at maturity for a fully invested security. |
| [DISC](DISC.md) | Discount rate for a security bought at a discount. |
| [TBILLEQ](TBILLEQ.md) | Bond-equivalent yield for a Treasury bill. |
| [MDURATION](MDURATION.md) | Price sensitivity of a bond to a change in yield. |

## Official Documentation

- [Microsoft Support: INTRATE function](https://support.microsoft.com/en-us/excel/functions/intrate-function)
- [Google Docs Editors Help: INTRATE](https://support.google.com/docs/answer/3093174)
