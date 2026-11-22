---
domain: Spreadsheet Functions
category: Financial
subcategory: Treasury Bills
purpose:
  - Bond Analysis
  - Investment Analysis
use-case:
  - Bill Purchase Cost
  - Money Market Cash Planning
  - Treasury Bill Ladder
related:
  - PRICEDISC
  - RECEIVED
  - TBILLEQ
  - TBILLYIELD
  - YIELDDISC
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/tbillprice-function
  - https://support.google.com/docs/answer/3093251
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bill Price Per 100
  - Treasury Bill Price
tags:
  - bonds
  - excel
  - sheets
  - treasury-bills
---

# TBILLPRICE

## Description

**TBILLPRICE** returns the price of a US Treasury bill per 100 of face value, based on its discount rate. A Treasury bill is sold below face value and pays its full face value at maturity. The difference between the price paid and the face value is the investor's return, and the discount rate is the quoted measure of that return.

Use TBILLPRICE when a dealer or auction quotes a discount rate and you need the cash price for a given face value. Multiply the function's result by the face value divided by 100 to get the total cost. For example, a price of 98.00 per 100 of face value means a 500,000 face value bill costs 490,000.

The price is calculated as 100 times (1 minus the discount rate times DSM divided by 360), where DSM is the number of days from settlement to maturity. The discount rate is applied to the face value on a 360-day basis, which is why the price is always below 100 for a positive discount rate.

Settlement must fall before maturity, and maturity must fall no more than one year after settlement. To find the discount rate from a price, use the price-to-yield functions instead. TBILLYIELD does that for bills, and YIELDDISC does it for other discounted securities.

## Syntax

```excel
=TBILLPRICE(settlement, maturity, discount)
```

<!-- Image 1: Syntax Anatomy. See Images/Financial/TBILLPRICE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the bill is delivered to the buyer, after it was issued. Enter it as a date, not as text. Settlement and maturity are truncated to whole days. |
| `maturity` | Yes | The date the bill expires and pays its face value. Must be after settlement and no more than one year later. |
| `discount` | Yes | The bill's discount rate, entered as a decimal such as 0.04 or as a percentage. Must be greater than 0. |

### Return Value

A number: the price per 100 of face value. For a bill with a 4% discount rate and 180 days to maturity, the price is 98.00. Excel returns `#VALUE!` when a date is not valid, and `#NUM!` when the discount is 0 or less, settlement is after maturity, or maturity is more than one year after settlement.

## Examples

### Example 1: Price of a 180-Day Bill

```excel
=TBILLPRICE(DATE(2026,2,15), DATE(2026,8,14), 0.04)
```

**Result:** `98.00`

There are 180 days from settlement to maturity. The discount is 0.04 times 180/360, which is 0.02, so the price is 100 times 0.98, or 98.00 per 100 of face value.

### Example 2: Short Bill of 30 Days

```excel
=TBILLPRICE(DATE(2026,2,15), DATE(2026,3,17), 0.035)
```

**Result:** `99.71`

A bill with 30 days to maturity at a 3.5% discount rate costs 99.708 per 100 of face value, shown rounded to 99.71. A short bill sits closer to face value than a long one at the same rate.

### Example 3: Higher Discount Rate

```excel
=TBILLPRICE(DATE(2026,2,15), DATE(2026,8,14), 0.05)
```

**Result:** `97.50`

At a 5% discount rate over the same 180 days, the discount is 2.5 points, so the price is 97.50 per 100 of face value.

## Story Problems

### Problem 1: Municipal Cash Purchase

A city treasurer buys Treasury bills with a face value of 500,000 that mature in 180 days. The bills are quoted at a 4% discount rate.

| Item | Value |
| --- | --- |
| Settlement | February 15, 2026 |
| Maturity | August 14, 2026 |
| Discount rate | 4% |
| Face value | 500,000 |

**Task:** Find the total price the city pays for the bills.

**Solution:**

```excel
=TBILLPRICE(DATE(2026,2,15), DATE(2026,8,14), 0.04)*500000/100
```

**Answer:** `490,000.00`. The price is 98.00 per 100 of face value, and 500,000 of face value is 5,000 units of 100, so the cost is 490,000.00.

<!-- Image 2: Story Problem Result Panel. See Images/Financial/TBILLPRICE.md -->

### Problem 2: Fund Buying a Short Bill

A money market fund buys a 30-day Treasury bill with a face value of 1,000,000 at a 3.5% discount rate. The fund's operations team needs the cash amount for the trade.

| Item | Value |
| --- | --- |
| Settlement | February 15, 2026 |
| Maturity | March 17, 2026 |
| Discount rate | 3.5% |
| Face value | 1,000,000 |

**Task:** Find the price per 100 of face value, then the total cash amount for the trade.

**Solution:**

```excel
=TBILLPRICE(DATE(2026,2,15), DATE(2026,3,17), 0.035)*1000000/100
```

**Answer:** `997,083.33`. The price is 99.7083 per 100 of face value, so the fund pays 997,083.33 for 1,000,000 of face value.

## Use Cases

### Bill Purchase Cost

**Scenario:** A corporate treasury team estimates the cash needed to buy a block of bills at the current quoted discount rate.

```excel
=TBILLPRICE(DATE(2026,2,15), DATE(2026,8,14), 0.04)*FaceValue/100
```

**Why It Works:** The function gives the price per 100, and the face value divided by 100 scales it to the trade size. The result tells the team the cash it must hold before settlement.

### Money Market Cash Planning

**Scenario:** A finance manager plans cash for a month in which several bills mature and new ones are bought.

```excel
=TBILLPRICE(B2, C2, D2)*E2/100
```

**Why It Works:** Each row holds its own dates, discount rate and face value. Summing the cash column shows the total outflow for the month.

### Treasury Bill Ladder

**Scenario:** An investor builds a ladder of bills that mature at different dates and wants the price of each rung.

```excel
=TBILLPRICE(DATE(2026,2,15), DATE(2026,3,17), 0.035)
```

**Why It Works:** A short rung such as this one costs close to face value, while a long rung at the same discount rate costs less per 100, so the price of each rung depends on its own maturity.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | Settlement or maturity is text, not a date. | Enter dates with DATE or use cells formatted as dates. |
| `#NUM!` | The discount rate is 0 or less. | Enter a positive discount rate. |
| `#NUM!` | Maturity is on or before settlement, or more than one year after it. | Check the bill's dates. |
| Price looks like a yield | The result is per 100 of face value, not a percentage. | Read the result as a price. Use TBILLYIELD for the yield. |
| Total cost is 100 times too high | The face value was not divided by 100 when scaling the price. | Multiply the price by face value divided by 100. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel versions, including Microsoft 365 and Excel for the web | Returns the price per 100 of face value. The page lists the settlement, maturity and discount error conditions. |
| Google Sheets | Available | Arguments have the same names and order. The official page describes the function as equivalent to PRICEDISC with Treasury bill conventions for the missing parameters. |

## Tips and Best Practices

- Scale the price to the trade size by multiplying by face value divided by 100.
- Keep the discount rate as a decimal, and check the rate against the auction or dealer quote.
- Enter dates with DATE so the day count is exact.
- Use TBILLYIELD to recover the yield from a price, and TBILLEQ to compare the bill with a deposit.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PRICEDISC](PRICEDISC.md) | Price of a discounted security from its discount rate. Google Sheets describes this function as equivalent to PRICEDISC with bill conventions. |
| [RECEIVED](RECEIVED.md) | Amount received at maturity for a fully invested discounted security. |
| [TBILLEQ](TBILLEQ.md) | Bond-equivalent yield of a bill from its discount rate. |
| [TBILLYIELD](TBILLYIELD.md) | Yield of a bill from its price, the reverse of this function. |
| [YIELDDISC](YIELDDISC.md) | Yield of a discounted security from its price. |

## Official Documentation

- [Microsoft Support: TBILLPRICE function](https://support.microsoft.com/en-us/excel/functions/tbillprice-function)
- [Google Docs Editors Help: TBILLPRICE](https://support.google.com/docs/answer/3093251)
