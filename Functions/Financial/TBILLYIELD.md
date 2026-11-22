---
domain: Spreadsheet Functions
category: Financial
subcategory: Treasury Bills
purpose:
  - Bond Analysis
  - Investment Analysis
use-case:
  - Bill Price Yield Check
  - Fund Holdings Review
  - Treasury Bill Purchase Decision
related:
  - PRICEDISC
  - RECEIVED
  - TBILLEQ
  - TBILLPRICE
  - YIELDDISC
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/tbillyield-function
  - https://support.google.com/docs/answer/3093264
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bill Yield
  - Treasury Bill Yield
tags:
  - bonds
  - excel
  - sheets
  - treasury-bills
  - yield
---

# TBILLYIELD

## Description

**TBILLYIELD** returns the yield of a US Treasury bill from its price. The price is quoted per 100 of face value, and the bill pays 100 at maturity. The yield is the return an investor earns on the price paid, spread over the days until maturity and annualized on a 360-day basis.

Use TBILLYIELD to check the return on a bill you are offered or already hold. If a dealer quotes a price of 98.25 for a 180-day bill, TBILLYIELD shows the return that price implies. Use TBILLPRICE for the reverse calculation, which takes a discount rate and returns the price.

The yield is calculated as (100 minus the price) divided by the price, multiplied by 360 divided by DSM, where DSM is the number of days from settlement to maturity. A higher price means a lower yield, because the investor pays more for the same 100 at maturity.

Settlement must fall before maturity, and maturity must fall no more than one year after settlement. Google Sheets describes the function as equivalent to YIELDDISC with Treasury bill conventions for the missing parameters.

## Syntax

```excel
=TBILLYIELD(settlement, maturity, pr)
```

<!-- Image 1: Syntax Anatomy. See Images/Financial/TBILLYIELD.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the bill is delivered to the buyer, after it was issued. Enter it as a date, not as text. |
| `maturity` | Yes | The date the bill expires and pays its face value. Must be after settlement and no more than one year later. |
| `pr` | Yes | The price per 100 of face value. Must be greater than 0. Google Sheets names this argument `price`. |

### Return Value

A decimal yield, shown as a percentage in a percentage-formatted cell. For a bill with a price of 98 and 180 days to maturity, the yield is 4.08%. Excel returns `#VALUE!` when a date is not valid, and `#NUM!` when the price is 0 or less, settlement is not before maturity, or maturity is more than one year after settlement.

## Examples

### Example 1: Yield at a Price of 98

```excel
=TBILLYIELD(DATE(2026,2,15), DATE(2026,8,14), 98)
```

**Result:** `4.08%`

The bill earns 2 points on a price of 98 over 180 days. The yield is (100 minus 98) divided by 98, times 360/180, which is 4.08%.

### Example 2: Short Bill at a Price of 99.70

```excel
=TBILLYIELD(DATE(2026,2,15), DATE(2026,3,17), 99.7)
```

**Result:** `3.61%`

A bill with 30 days to maturity and a price of 99.70 earns 0.30 points. Because the period is short, the same 0.30 points produce a larger annualized yield than it would over 180 days.

### Example 3: Deeper Discount

```excel
=TBILLYIELD(DATE(2026,2,15), DATE(2026,8,14), 97.5)
```

**Result:** `5.13%`

A price of 97.50 for the same 180 days gives 2.5 points of return. The yield is higher than at a price of 98 because the investor pays less for the same 100 at maturity.

## Story Problems

### Problem 1: Checking a Dealer Quote

A fund manager is offered a 180-day Treasury bill at a price of 98.25 per 100 of face value. The manager wants the yield before accepting the quote.

| Item | Value |
| --- | --- |
| Settlement | February 15, 2026 |
| Maturity | August 14, 2026 |
| Price | 98.25 |

**Task:** Find the annualized yield the price implies.

**Solution:**

```excel
=TBILLYIELD(DATE(2026,2,15), DATE(2026,8,14), 98.25)
```

**Answer:** `3.56%`. The bill returns 1.75 points over 180 days, which annualizes to about 3.56% on the 360-day basis.

<!-- Image 2: Story Problem Result Panel. See Images/Financial/TBILLYIELD.md -->

### Problem 2: Comparing a Bill With a Cash Rate

A company can buy a 180-day Treasury bill at 97.50 per 100 of face value, or keep the same cash in a money market fund that yields 5.00%. The treasurer wants both returns on the same basis.

| Item | Value |
| --- | --- |
| Settlement | February 15, 2026 |
| Maturity | August 14, 2026 |
| Price | 97.50 |
| Money market yield | 5.00% |

**Task:** Find the bill's yield at the quoted price and compare it with the money market yield.

**Solution:**

```excel
=TBILLYIELD(DATE(2026,2,15), DATE(2026,8,14), 97.5)
```

**Answer:** `5.13%`. The bill yields about 0.13 percentage points more than the money market fund, so the bill is slightly better on yield.

## Use Cases

### Bill Price Yield Check

**Scenario:** A treasury analyst checks whether a dealer's quoted price for a bill gives a yield above the company's target.

```excel
=TBILLYIELD(DATE(2026,2,15), DATE(2026,8,14), 98.25)
```

**Why It Works:** The function turns the quoted price into a yield that can be compared with a target. A higher yield means the price is more favorable to the buyer.

### Fund Holdings Review

**Scenario:** A fund reviews a list of bills it already holds and wants the yield on each at the current price.

```excel
=TBILLYIELD(B2, C2, D2)
```

**Why It Works:** Each row holds its own settlement date, maturity date and price. Copying the formula down the column produces a yield for every holding in the same units.

### Treasury Bill Purchase Decision

**Scenario:** A buyer compares two bills at different prices and maturities before placing an order.

```excel
=TBILLYIELD(DATE(2026,2,15), DATE(2026,8,14), 98)-TBILLYIELD(DATE(2026,2,15), DATE(2026,3,17), 99.7)
```

**Why It Works:** Subtracting the two yields shows which bill returns more on an annual basis. Here the 180-day bill at 98 yields 4.08% and the 30-day bill yields 3.61%, so the difference is 0.47 percentage points.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | Settlement or maturity is text, not a date. | Enter dates with DATE or use cells formatted as dates. |
| `#NUM!` | The price is 0 or less. | Enter the price per 100 of face value as a positive number. |
| `#NUM!` | Maturity is on or before settlement, or more than one year after it. | Check the bill's dates. |
| Yield far too high | The price was entered as a yield or a discount rate, such as 0.04. | Enter the price per 100, such as 98. |
| Yield is in the wrong units | The result was read as a whole number. | Format the cell as a percentage. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel versions, including Microsoft 365 and Excel for the web | The third argument is named pr. The page lists the settlement, maturity and price error conditions. |
| Google Sheets | Available | The third argument is named price. The official page describes the function as equivalent to YIELDDISC with Treasury bill conventions, and it requires maturity to be no more than one year after settlement. |

## Tips and Best Practices

- Enter the price per 100 of face value, not a discount rate or a yield.
- Enter dates with DATE so the day count is exact.
- Compare yields only between bills on the same basis, or convert other instruments with TBILLEQ first.
- Use TBILLPRICE for the reverse calculation when you have a discount rate instead of a price.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PRICEDISC](PRICEDISC.md) | Price of a discounted security from its discount rate, the reverse of a yield calculation. |
| [RECEIVED](RECEIVED.md) | Amount received at maturity for a fully invested discounted security. |
| [TBILLEQ](TBILLEQ.md) | Bond-equivalent yield of a bill from its discount rate. |
| [TBILLPRICE](TBILLPRICE.md) | Price per 100 of face value from the discount rate, the reverse of this function. |
| [YIELDDISC](YIELDDISC.md) | Yield of a discounted security from its price. Google Sheets describes this function as equivalent to it with bill conventions. |

## Official Documentation

- [Microsoft Support: TBILLYIELD function](https://support.microsoft.com/en-us/excel/functions/tbillyield-function)
- [Google Docs Editors Help: TBILLYIELD](https://support.google.com/docs/answer/3093264)
