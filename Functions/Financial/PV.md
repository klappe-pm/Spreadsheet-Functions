---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
purpose:
  - Financial Modeling
  - Loan Analysis
use-case:
  - Annuity Versus Lump Sum
  - Bond Price Estimate
  - Loan Affordability
related:
  - FV
  - NPER
  - NPV
  - PMT
  - RATE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/pv-function
  - https://support.google.com/docs/answer/3093243
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Discounted Value
  - Present Value
tags:
  - annuity
  - excel
  - sheets
  - time-value-of-money
---

# PV

## Description

**PV** returns the present value of a series of equal payments, a future lump sum, or both, discounted at a constant interest rate. It answers the question "what is a stream of future cash worth today?" Lenders use it to size a loan from a payment the borrower can afford, buyers use it to price a bond or an annuity, and planners use it to compare a lump sum with a payment plan.

PV is the reverse of FV. FV grows a present amount forward in time, while PV discounts future amounts back to the present. Both functions assume the rate and the payment amount stay the same for every period. When payments change from period to period, use NPV instead.

Sign conventions matter. Cash you receive is positive and cash you pay out is negative. When the payments and the future value are positive (money you receive), PV returns a negative number, which is the amount you would have to pay today to receive them. Negate the result with a leading minus sign to show the value as a positive number in a report.

Set the type argument to 1 when payments happen at the start of each period, such as rent or lease payments made in advance. The default, 0, assumes payments happen at the end of each period.

## Syntax

```excel
=PV(rate, nper, pmt, [fv], [type])
```

<!-- Image 1: Syntax Anatomy. See Images/Financial/PV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The interest rate per period. For monthly payments on an annual rate, divide the annual rate by 12. |
| `nper` | Yes | The total number of payment periods. For 30 years of monthly payments, enter `30*12`. The rate and nper must use the same period length. |
| `pmt` | Yes | The payment made each period. It stays constant for the life of the annuity. Enter money you receive as positive and money you pay as negative. |
| `fv` | No | The future value, or the cash balance you want after the last payment. Defaults to 0 when omitted. If `pmt` is omitted, `fv` is required. |
| `type` | No | When payments occur. `0` or omitted means end of period. `1` means beginning of period. |

### Return Value

A single number: the present value of the payments and the future value. The result is negative when the inputs are positive cash receipts, and positive when the payments are entered as negative cash outflows. A non-numeric argument produces an error.

## Examples

All examples use the standard PV syntax with the arguments shown.

### Example 1: Loan Amount a Payment Supports

```excel
=PV(0.05/12, 360, -1500)
```

**Result:** `279,422.43`

The payment of 1,500 per month is entered as negative because it is cash the borrower pays out. At 5% a year, paid monthly for 30 years, that stream supports a loan of about 279,422 today. The positive result is the amount the borrower receives.

### Example 2: Present Value of a Single Future Amount

```excel
=PV(0.04, 5, 0, 20000)
```

**Result:** `-16,438.54`

With no periodic payments (pmt is 0), PV discounts the 20,000 due in five years back to today at 4% a year. The negative sign means you would need to set aside 16,438.54 today to have 20,000 in five years.

### Example 3: Beginning Versus End of Period

```excel
=PV(0.06/12, 24, -300, 0, 1)
```

**Result:** `6,802.70`

This loan pays 300 at the start of each of 24 months. Changing the type argument to 0 or omitting it gives `6,768.86` for the same payments made at the end of each month. Payments made earlier are worth more, so the start-of-period result is higher.

<!-- Image 2: Payment Timing Comparison. See Images/Financial/PV.md -->

### Example 4: Present Value as a Positive Number

```excel
=-PV(0.06, 12, 3000)
```

**Result:** `25,151.53`

Negating the function shows the present value of receiving 3,000 a year for 12 years at 6% as a positive number. The negation changes only the display; the calculation is the same.

### Example 5: Choosing Between Payments and a Lump Sum

```excel
=IF(-PV(0.06, 12, 3000) < 30000, "Take the Lump Sum", "Take the Payments")
```

**Result:** `"Take the Lump Sum"`

The payments are worth 25,151.53 today, which is less than the 30,000 lump sum offer, so the lump sum has the higher value at this discount rate.

## Story Problems

### Problem 1: Settlement Offer on Annual Payments

A supplier owes a customer 2,400 at the end of each year for 10 years. The supplier offers a single payment of 18,000 today instead. The customer's required return is 5% a year.

| Year | Payment | Offer |
| --- | --- | --- |
| 1 to 10 | 2,400 each year | 18,000 today |

**Task:** Find the present value of the payments and decide which option is worth more.

**Solution:**

```excel
=-PV(0.05, 10, 2400)
```

**Answer:** `18,532.16`. The payments are worth 532.16 more than the 18,000 offer, so the customer should keep the payments.

<!-- Image 3: Story Problem Result Panel. See Images/Financial/PV.md -->

### Problem 2: Leasing a Vehicle With Payments in Advance

A business can lease a van for 36 months at 400 per month, paid at the start of each month. Buying the van outright costs 13,000 today. The business discounts cash flows at 8% a year.

| Term | Monthly Payment | Purchase Price |
| --- | --- | --- |
| 36 months | 400 | 13,000 |

**Task:** Find the present value of the lease payments and compare it with the purchase price.

**Solution:**

```excel
=-PV(0.08/12, 36, 400, 0, 1)
```

**Answer:** `12,849.82`. The lease costs 150.18 less than buying in today's money. Lease terms, residual value and ownership are not part of this comparison.

## Use Cases

### Loan Affordability Check

**Scenario:** A household can afford a 1,200 monthly mortgage payment at 6.5% annual interest over 25 years and wants to know the largest loan the payment supports.

```excel
=PV(0.065/12, 25*12, -1200)
```

**Why It Works:** The payment is negative because it leaves the household's account. The result is the loan amount the household can receive. Lenders use the same arithmetic when they pre-approve a borrower.

### Bond Price Estimate

**Scenario:** A bond pays a 60 coupon each year for 10 years and returns its 1,000 face value at maturity. Market rates for similar bonds are 5%.

```excel
=-PV(0.05, 10, 60, 1000)
```

**Why It Works:** The coupons and face value are positive cash receipts, so PV is negative. Negating it gives the price an investor would pay, about 1,077.22. The bond trades above par because its coupon rate of 6% is above the 5% market rate.

### Annuity Versus Lump Sum

**Scenario:** A retiree is offered 30,000 today or 3,000 a year for 12 years. The retiree's expected return on invested money is 6%.

```excel
=IF(-PV(0.06, 12, 3000) < 30000, "Take the Lump Sum", "Take the Payments")
```

**Why It Works:** Both options are converted to present value at the same rate, so they can be compared directly. A higher discount rate lowers the payment stream's value and can change the decision.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A parameter contains text, a currency symbol or a space. | Enter each argument as a number or a cell that holds a number. |
| Very large or very small result | The rate was typed as a whole number, such as `6`, instead of `0.06`. | Enter 6% as `0.06` or `6%`. |
| Result too large or small by about 12 times | The annual rate was used with monthly periods. | Divide the annual rate by 12 and multiply the years by 12. |
| Unexpected negative result | Receipts were entered as positive values, so the result is the cost to obtain them. | Negate the function with `-PV()` for a positive display. |
| Payment stream appears to have no effect | The payment argument was left empty or set to 0 without an fv value. | Enter the payment, the future value, or both. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel versions, including Microsoft 365 and Excel for the web | Arguments are named rate, nper, pmt, fv and type. |
| Google Sheets | Available | Arguments are named rate, number_of_periods, payment_amount, future_value and end_or_beginning. The order and behavior match Excel. |

## Tips and Best Practices

- Match the rate to the payment period. Monthly payments need a monthly rate and a period count in months.
- Keep a consistent sign convention across the workbook: money in is positive, money out is negative.
- Test several discount rates to see how sensitive the present value is before you decide.
- Use `-PV()` in reports so readers see a positive value without a confusing sign.
- For a delayed annuity, find the value at the start of the payments with PV, then discount that amount back to today with a second PV.
- Use NPV when cash flows vary from period to period.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FV](FV.md) | Grows a present amount forward; the inverse of discounting a future amount with PV. |
| [NPER](NPER.md) | Solves for the number of periods when the rate, payment and present value are known. |
| [NPV](NPV.md) | Discounts a series of uneven cash flows rather than equal payments. |
| [PMT](PMT.md) | Solves for the payment when the present value is known. |
| [RATE](RATE.md) | Solves for the interest rate when the other arguments are known. |

## Official Documentation

- [Microsoft Support: PV function](https://support.microsoft.com/en-us/excel/functions/pv-function)
- [Google Docs Editors Help: PV](https://support.google.com/docs/answer/3093243)
