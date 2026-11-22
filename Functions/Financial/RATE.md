---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
purpose:
  - Investment Analysis
  - Loan Analysis
use-case:
  - Dealer Financing Rate
  - Investment Growth Rate
  - Savings Goal Rate
related:
  - FV
  - IRR
  - NPER
  - PMT
  - PV
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/rate-function
  - https://support.google.com/docs/answer/3093257
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Interest Rate Per Period
  - Annuity Rate
tags:
  - annuity
  - excel
  - interest-rate
  - sheets
---

# RATE

## Description

**RATE** returns the interest rate per period of an annuity. An annuity is a series of equal payments made at regular intervals, and RATE works backward from the payments, the number of periods and the present value to find the rate that makes them consistent. Use it to find the rate hidden in a loan offer, a financing plan or a savings plan.

The result is a rate per period, not a yearly rate. A monthly loan returns a monthly rate, so multiply the result by 12 for a nominal annual rate. A quarterly plan needs a multiplier of 4. The number of periods and the payment must use the same period length as the rate.

RATE has no closed-form solution, so Excel finds it by iteration. The optional guess argument gives the search a starting point. Most problems converge with the default guess, but if the function returns an error, supply a guess closer to the expected rate. The function can have more than one solution or none, so check the result against a known payment schedule when the inputs are unusual.

Use PV to find a present value when you know the rate, and PMT to find a payment when you know the rate and the amount borrowed.

## Syntax

```excel
=RATE(nper, pmt, pv, [fv], [type], [guess])
```

<!-- Image 1: Syntax Anatomy. See Images/Financial/RATE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `nper` | Yes | The total number of payment periods in the annuity. |
| `pmt` | Yes | The payment made each period. It cannot change over the life of the annuity. If omitted, `fv` is required. |
| `pv` | Yes | The present value of the future payments, such as the loan amount or the amount invested today. |
| `fv` | No | The future value, or the cash balance you want after the last payment. Defaults to 0. |
| `type` | No | When payments occur. `0` or omitted means end of period. `1` means beginning of period. |
| `guess` | No | Your estimate of the rate per period. Defaults to 10%. Use a value between 0 and 1 for most problems. |

### Return Value

The interest rate per period, shown as a decimal or a percentage depending on the cell format. Excel returns `#NUM!` when successive results do not converge to within 0.0000001 after 20 iterations.

## Examples

### Example 1: Annual Rate on a Car Loan

```excel
=RATE(60, -450, 22000)*12
```

**Result:** `8.37%`

The function returns the monthly rate, about 0.698%. Multiplying by 12 converts it to a nominal annual rate. The payment of 450 is negative because it leaves the borrower's account, and the loan amount of 22,000 is positive because it is received.

<!-- Image 2: Monthly to Annual Conversion. See Images/Financial/RATE.md -->

### Example 2: Growth of a Single Investment

```excel
=RATE(10, 0, -5000, 9000)
```

**Result:** `6.05%`

With no periodic payments, the rate is the growth that takes 5,000 invested today to 9,000 in 10 years. The payment is 0, so the function solves a simple compound growth problem.

### Example 3: Setting a Guess for the Search

```excel
=RATE(36, -310, 10000, 0, 0, 0.01)*12
```

**Result:** `7.27%`

The guess of 0.01 gives the search a starting point near the monthly rate. A guess close to the answer helps when the default guess fails to converge.

### Example 4: Rate Needed to Grow a Value

```excel
=RATE(5, 0, -1000, 1500)
```

**Result:** `8.45%`

To grow 1,000 into 1,500 in five years, the annual rate must be about 8.45%. This matches the growth rate formula (1.5 raised to the power of 1/5, minus 1), which is a useful check on the function's output.

## Story Problems

### Problem 1: Financing Office Equipment

A clinic finances a 10,000 scanner with 36 monthly payments of 310. The clinic's accountant wants the nominal annual rate.

| Item | Value |
| --- | --- |
| Amount financed | 10,000 |
| Monthly payment | 310 |
| Number of payments | 36 |

**Task:** Find the annual nominal rate on the financing plan.

**Solution:**

```excel
=RATE(36, -310, 10000)*12
```

**Answer:** `7.27%`. The monthly rate is about 0.606%, and multiplying by 12 gives the nominal annual rate.

<!-- Image 3: Story Problem Result Panel. See Images/Financial/RATE.md -->

### Problem 2: Quarterly Supplier Credit

A supplier offers 10,000 of credit, repaid with eight quarterly payments of 1,400. A buyer wants to compare this offer with a bank loan that charges a stated yearly rate.

| Item | Value |
| --- | --- |
| Amount financed | 10,000 |
| Quarterly payment | 1,400 |
| Number of payments | 8 |

**Task:** Find the annual nominal rate, using quarters as the period.

**Solution:**

```excel
=RATE(8, -1400, 10000)*4
```

**Answer:** `10.36%`. The quarterly rate is about 2.59%, and multiplying by 4 gives the annual nominal rate.

## Use Cases

### Dealer Financing Rate

**Scenario:** A dealer offers a vehicle for 12,000 financed with 36 monthly payments of 400. A buyer wants to know the rate hidden in the offer before signing.

```excel
=RATE(36, -400, 12000)*12
```

**Why It Works:** The function isolates the rate from the other three figures. Here the result is 12.25%, which a buyer can compare with a bank's quoted rate. Check the result by rebuilding the payment with PMT.

### Savings Goal Rate

**Scenario:** A family saves 250 a month for five years and wants to reach 18,000. They ask which annual return the savings plan needs to earn.

```excel
=RATE(60, -250, 0, 18000)*12
```

**Why It Works:** With no starting balance, the present value is 0 and fv carries the goal. The result, 7.22%, is the nominal annual return the savings plan must earn to hit the target.

### Investment Growth Rate

**Scenario:** An analyst records the value of an investment at two dates and wants the annual growth rate between them.

```excel
=RATE(5, 0, -1000, 1500)
```

**Why It Works:** This is the same growth problem as Example 4. Using RATE avoids a separate exponent formula and makes it easy to change the period count when the dates change.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The search did not converge within 20 iterations. | Enter a guess close to the expected rate, such as 0.01 for a monthly loan. |
| Rate looks too small by a factor of 12 | The result is a monthly rate, but a yearly rate was expected. | Multiply by 12 for a monthly schedule or by 4 for a quarterly one. |
| Nonsense result | Payments and the present value have the same sign, so no rate fits the inputs. | Enter money received and money paid with opposite signs. |
| Wrong result | The number of periods is in years but the payment is monthly. | Convert nper to the same period count as the payment. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel versions, including Microsoft 365 and Excel for the web | Arguments are named nper, pmt, pv, fv, type and guess. The default guess is 10%. Returns `#NUM!` when the search does not converge. |
| Google Sheets | Available | Arguments are named number_of_periods, payment_per_period, present_value, future_value, end_or_beginning and rate_guess. The default guess is 0.1, which is the same 10%. |

## Tips and Best Practices

- Convert the result to the period you need. Multiply a monthly rate by 12 for a nominal annual rate.
- Keep the payment and the present value opposite in sign, so the solver has a real rate to find.
- Use a guess near the expected rate when the default fails, and keep the guess in the same period units as nper.
- Check the answer by rebuilding the payment with PMT and comparing it with the original payment.
- Remember that a nominal annual rate is not the same as the effective annual rate. Use EFFECT to convert between them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FV](FV.md) | Finds the future value when the rate is known. |
| [IRR](../Financial/IRR.md) | Finds the rate from a series of uneven cash flows. |
| [NPER](NPER.md) | Finds the number of periods when the rate is known. |
| [PMT](PMT.md) | Finds the payment when the rate is known. |
| [PV](PV.md) | Finds the present value when the rate is known. |

## Official Documentation

- [Microsoft Support: RATE function](https://support.microsoft.com/en-us/excel/functions/rate-function)
- [Google Docs Editors Help: RATE](https://support.google.com/docs/answer/3093257)
