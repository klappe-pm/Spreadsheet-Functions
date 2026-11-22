---
domain: Spreadsheet Functions
category: Financial
subcategory: Treasury Bills
purpose:
  - Bond Analysis
  - Investment Analysis
use-case:
  - Bill Versus Deposit Comparison
  - Short Term Cash Management
  - Treasury Bill Yield Comparison
related:
  - PRICEDISC
  - RECEIVED
  - TBILLPRICE
  - TBILLYIELD
  - YIELDDISC
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/tbilleq-function
  - https://support.google.com/docs/answer/3093249
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Bond Equivalent Yield
  - Treasury Bill Equivalent Yield
tags:
  - bonds
  - excel
  - sheets
  - treasury-bills
  - yield
---

# TBILLEQ

## Description

**TBILLEQ** returns the bond-equivalent yield of a US Treasury bill from its discount rate. A Treasury bill is sold at a discount and pays its face value at maturity, so its discount rate is not directly comparable with the interest rate on a coupon bond or a bank deposit. The bond-equivalent yield restates the bill's return on a basis that other fixed-income instruments use, which makes the comparison fair.

Use TBILLEQ when you have the discount rate quoted for a bill and need to compare it with another investment. Google Sheets describes the result as the equivalent annualized rate of return of a Treasury bill based on its discount rate. For bills with less than a year to maturity, the result is higher than the discount rate, because the discount is taken from the face value while the investor pays a lower price.

The function uses the number of days from settlement to maturity, called DSM. The Microsoft Excel formula is 365 times the discount rate, divided by 360 minus the discount rate times DSM. Settlement must fall before maturity, and the maturity must fall no more than one year after settlement.

To find the discount rate from a price, or the price from a yield, use TBILLPRICE and TBILLYIELD. TBILLEQ converts a discount rate into a yield on a bond-equivalent basis.

## Syntax

```excel
=TBILLEQ(settlement, maturity, discount)
```

<!-- Image 1: Syntax Anatomy. See Images/Financial/TBILLEQ.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `settlement` | Yes | The date the bill is delivered to the buyer, after it was issued. Enter it as a date, not as text. |
| `maturity` | Yes | The date the bill expires and pays its face value. Must be after settlement and no more than one year later. |
| `discount` | Yes | The bill's discount rate, entered as a decimal such as 0.04 or as a percentage. Must be greater than 0. |

### Return Value

A decimal yield, shown as a percentage in a percentage-formatted cell. The Microsoft Excel page gives the example result of 9.42% (0.09415) for a bill with a 9.14% discount rate and 62 days to maturity. Excel returns `#VALUE!` when a date is not valid, and `#NUM!` when the discount is 0 or less, settlement is after maturity, or maturity is more than one year after settlement.

## Examples

### Example 1: Yield on a 180-Day Bill

```excel
=TBILLEQ(DATE(2026,2,15), DATE(2026,8,14), 0.04)
```

**Result:** `4.14%`

The bill has 180 days from settlement to maturity. Applying the formula gives 365 times 0.04, divided by 360 minus 0.04 times 180, which is 4.14%.

### Example 2: Higher Discount Rate

```excel
=TBILLEQ(DATE(2026,2,15), DATE(2026,8,14), 0.05)
```

**Result:** `5.20%`

The same 180-day bill quoted at a 5% discount rate has a bond-equivalent yield of 5.20%. The gap between the discount rate and the yield widens as the discount rate rises.

### Example 3: Short Bill of 30 Days

```excel
=TBILLEQ(DATE(2026,2,15), DATE(2026,3,17), 0.035)
```

**Result:** `3.56%`

A bill with 30 days to maturity and a 3.5% discount rate has a bond-equivalent yield of 3.56%. The difference from the discount rate is smaller for short bills than for long ones.

## Story Problems

### Problem 1: Bill Versus Deposit

A treasurer can buy a 180-day Treasury bill quoted at a 4% discount rate, or place the same cash in a bank deposit that pays 4.10% a year. The treasurer wants both returns on the same basis before deciding.

| Item | Value |
| --- | --- |
| Settlement | February 15, 2026 |
| Maturity | August 14, 2026 |
| Bill discount rate | 4% |
| Deposit rate | 4.10% |

**Task:** Convert the bill's discount rate to a bond-equivalent yield and compare it with the deposit rate.

**Solution:**

```excel
=TBILLEQ(DATE(2026,2,15), DATE(2026,8,14), 0.04)
```

**Answer:** `4.14%`. The bill returns about 0.04 percentage points more than the deposit on a comparable basis, so the bill pays slightly more on a comparable basis.

<!-- Image 2: Story Problem Result Panel. See Images/Financial/TBILLEQ.md -->

### Problem 2: Comparing Two Bills of Different Lengths

A fund holds two Treasury bills. The first matures in 180 days at a 4% discount rate. The second matures in 30 days at a 3.5% discount rate. The fund manager wants the two yields on the same basis.

| Bill | Days to maturity | Discount rate |
| --- | --- | --- |
| First bill | 180 | 4% |
| Second bill | 30 | 3.5% |

**Task:** Find the bond-equivalent yield of the 30-day bill.

**Solution:**

```excel
=TBILLEQ(DATE(2026,2,15), DATE(2026,3,17), 0.035)
```

**Answer:** `3.56%`. The 30-day bill yields 3.56% on a bond-equivalent basis, which can be compared directly with the 4.14% yield on the 180-day bill.

## Use Cases

### Bill Versus Deposit Comparison

**Scenario:** A company compares a short-term Treasury bill with a bank certificate before moving cash.

```excel
=TBILLEQ(DATE(2026,2,15), DATE(2026,8,14), 0.04)
```

**Why It Works:** Both investments are expressed as a yield, so the comparison uses the same basis. A higher yield means more return per year on the cash invested.

### Short Term Cash Management

**Scenario:** A treasury team holds a ladder of bills and wants a yield column that updates as each discount rate changes.

```excel
=TBILLEQ(B2, C2, D2)
```

**Why It Works:** Each row holds its own settlement date, maturity date and discount rate. Copying the formula down the column keeps every yield on the same basis.

### Treasury Bill Yield Comparison

**Scenario:** An analyst lists the yields of bills across several maturities to see how the yield curve slopes.

```excel
=TBILLEQ(DATE(2026,2,15), DATE(2026,8,14), 0.05)
```

**Why It Works:** Converting each discount rate to a bond-equivalent yield removes the distortion from different maturities, so the rates can be plotted together.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | Settlement or maturity is text, not a date. | Enter dates with DATE or use cells formatted as dates. |
| `#NUM!` | The discount rate is 0 or less. | Enter a positive discount rate. |
| `#NUM!` | Maturity is on or before settlement, or more than one year after it. | Check the bill's dates. Treasury bills have a maturity of one year or less. |
| Yield looks too high | The discount rate was entered as a whole number, such as 4 instead of 0.04. | Enter the rate as 0.04 or as 4%. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel versions, including Microsoft 365 and Excel for the web | Documented formula: 365 times the discount rate, divided by 360 minus the discount rate times DSM. The page lists the settlement and maturity error conditions. |
| Google Sheets | Available | Arguments have the same names and order. The official page enters dates with DATE or another date-parsing function. |

## Tips and Best Practices

- Compare bills with other investments only after converting both to the same basis.
- Enter dates with DATE so the day count is exact.
- Use TBILLPRICE to find the price for a discount rate and TBILLYIELD to find the yield for a price.
- Check that the bill matures within one year of settlement before you rely on the result.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PRICEDISC](PRICEDISC.md) | Price of a discounted security from its discount rate, the general form of the Treasury bill calculation. |
| [RECEIVED](RECEIVED.md) | Amount received at maturity for a fully invested discounted security. |
| [TBILLPRICE](TBILLPRICE.md) | Price per 100 of face value from the discount rate. |
| [TBILLYIELD](TBILLYIELD.md) | Yield of a bill from its price. |
| [YIELDDISC](YIELDDISC.md) | Yield of a discounted security from its price, the general form of the Treasury bill calculation. |

## Official Documentation

- [Microsoft Support: TBILLEQ function](https://support.microsoft.com/en-us/excel/functions/tbilleq-function)
- [Google Docs Editors Help: TBILLEQ](https://support.google.com/docs/answer/3093249)
