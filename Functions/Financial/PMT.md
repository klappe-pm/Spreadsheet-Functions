---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
purpose:
  - Loan Analysis
use-case:
  - Auto Loan Budgeting
  - Equipment Financing
  - Savings Goal Planning
related:
  - CUMIPMT
  - FV
  - IPMT
  - NPER
  - PPMT
  - PV
  - RATE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/pmt-function
  - https://support.google.com/docs/answer/3093185
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Loan Payment
  - Periodic Payment Amount
tags:
  - excel
  - loan-payments
  - sheets
  - time-value-of-money
---

# PMT

## Description

**PMT** returns the regular payment needed to repay a loan or reach a savings goal, assuming constant payments and a constant interest rate. Each payment covers both interest and principal. The result does not include taxes, insurance, reserve payments or fees.

The rate and the number of periods must use the same time unit. For a monthly payment on a loan with an annual rate, divide the annual rate by 12 and multiply the years by 12. Excel returns money you pay out as a negative number, so a loan payment appears in parentheses or with a minus sign.

Use PMT when you know the amount borrowed and the term, and want the payment. Use PPMT and IPMT to split a payment into its principal and interest parts. Use RATE or NPER when the payment is known and you need to solve for the rate or the number of periods.

## Syntax

```excel
=PMT(rate, nper, pv, [fv], [type])
```

<!-- Image 1: PMT Argument Layout. See Images/Financial/PMT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The interest rate per period. For monthly payments on an annual rate, use the annual rate divided by 12. |
| `nper` | Yes | The total number of payments. It must use the same period unit as the rate. |
| `pv` | Yes | The present value, the amount borrowed or the lump sum that the payments are worth today. |
| `fv` | No | The cash balance you want after the last payment. Omitted means 0, which is the case for a fully repaid loan. |
| `type` | No | When payments fall due: `0` or omitted for the end of each period, or `1` for the beginning of each period. |

### Return Value

A number: the payment for each period. A payment you make is negative when the present value is positive. The function returns `#VALUE!` when an argument is text that cannot be read as a number.

## Examples

### Example 1: Monthly Payment on a Car Loan

```excel
=PMT(6%/12, 60, 25000)
```

**Result:** `-483.32`

A $25,000 loan at 6% annual interest, repaid over 60 monthly payments. The minus sign shows money paid out.

### Example 2: Payment at the Beginning of Each Period

```excel
=PMT(6%/12, 60, 25000, 0, 1)
```

**Result:** `-480.92`

Payments due at the start of each month reduce the monthly amount slightly, because the first payment is made before any interest accrues.

<!-- Image 2: End and Beginning Payment Timing. See Images/Financial/PMT.md -->

### Example 3: Payment With a Balloon Balance

```excel
=PMT(6%/12, 60, 25000, -5000)
```

**Result:** `-411.66`

Setting `fv` to `-5000` means that after 60 payments, 5,000 of the loan is still owed as a balloon payment, so the regular payment is lower.

### Example 4: Mortgage Payment Shown as a Positive Number

```excel
=-PMT(6%/12, 360, 200000)
```

**Result:** `1199.10`

A $200,000 mortgage at 6% annual interest over 30 years (360 monthly payments). The leading minus sign flips the result so a report shows the payment as a positive amount. The cash flow direction does not change.

### Example 5: Quarterly Payments

```excel
=PMT(8%/4, 5*4, 50000)
```

**Result:** `-3057.84`

A $50,000 loan at 8% annual interest, repaid over 5 years in quarterly payments. The rate is divided by 4 and the years are multiplied by 4, so both use quarters.

### Example 6: Savings With a Starting Balance

```excel
=PMT(6%/12, 20*12, -50000, 500000)
```

**Result:** `-723.94`

A saver has 50,000 now (entered as a negative present value because it is money paid into the account) and wants 500,000 in 20 years at 6% annual interest. The monthly deposit needed is 723.94.

## Story Problems

### Problem 1: Financing an Equipment Purchase

A workshop borrows 18,000 to buy a machine. The loan charges 7.5% interest a year and is repaid in 36 equal monthly payments made at the end of each month.

| Term | Value |
| --- | --- |
| Annual rate | 7.50% |
| Number of months | 36 |
| Amount borrowed | 18000 |

**Task:** Find the monthly payment the workshop must budget for.

**Solution:**

```excel
=PMT(B2/12, B3, B4)
```

**Answer:** `-559.91`, which is a monthly payment of 559.91. The total repaid is about 20,157 over three years.

### Problem 2: Saving for a Fixed Goal

A family wants to save 12,000 in 48 months. Its savings account earns 4.8% a year, compounded monthly. It plans to deposit at the start of each month.

**Task:** Find the monthly deposit needed to reach 12,000.

**Solution:**

```excel
=PMT(B2/12, B3, 0, B4, 1)
```

Here `B2` is 4.8%, `B3` is 48 and `B4` is 12000.

**Answer:** `-226.36`, which means a deposit of 226.36 each month.

### Problem 3: Comparing a 15-Year and a 30-Year Mortgage

A buyer is offered two loans of 250,000. The 15-year loan charges 5.5% a year and the 30-year loan charges 6% a year. Both are repaid in monthly payments.

| Term | Annual Rate | Months |
| --- | --- | --- |
| 15 years | 5.50% | 180 |
| 30 years | 6.00% | 360 |

**Task:** Find both monthly payments and the total repaid on each loan.

**Solution:**

```excel
=PMT(5.5%/12, 180, 250000)
=PMT(6%/12, 360, 250000)
```

Multiply each payment by its number of months to get the total repaid.

**Answer:** `-2042.71` and `-1498.88`. The 15-year loan costs about 544 more each month but repays about 367,688 in total, against about 539,595 for the 30-year loan, a difference of about 171,908.

<!-- Image 3: Story Problem Inputs and Output. See Images/Financial/PMT.md -->

## Use Cases

### Auto Loan Budgeting

**Scenario:** A household compares monthly payments for loans of different lengths before buying a car.

```excel
=PMT(AnnualRate/12, LoanMonths, LoanAmount)
```

**Why It Works:** Dividing the annual rate by 12 keeps the rate and the number of months in the same unit, so the payment is correct for each option.

### Savings Goal Planning

**Scenario:** A saver wants a set amount at the end of a fixed period and needs the monthly contribution.

```excel
=PMT(SavingsRate/12, Months, 0, TargetAmount, 1)
```

**Why It Works:** Using a future value with a present value of 0 solves for the deposit, and type 1 matches deposits made at the start of each month.

### Mortgage Affordability

**Scenario:** A buyer can pay 2,500 a month at 6.5% annual interest over 30 years and wants the largest loan that fits, then the price with a 20% down payment.

```excel
=PV(6.5%/12, 360, -2500)
```

**Why It Works:** PV runs PMT backward and returns about 395,527 as the loan amount. Dividing by 0.8 gives a purchase price of about 494,409. PMT excludes taxes, insurance and fees, so the real monthly cost is higher.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Payment far too large | The annual rate was used with a monthly term. | Divide the annual rate by 12 for monthly payments. |
| Payment far too small | The term is in years but the rate is monthly, or the other way around. | Convert both arguments to the same period. |
| Payment far too large | The rate was typed as 6 instead of 6%. | Enter the rate as a percentage such as `6%` or as the decimal `0.06`. |
| Positive result when a negative was expected | The sign convention treats the amount borrowed as received and payments as paid out. | Keep the sign of `pv` and the result consistent with the cash flow direction. |
| `#VALUE!` | An argument is text that cannot be read as a number. | Enter numbers, or convert text values with `VALUE`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Arguments are named `rate`, `nper`, `pv`, `fv` and `type`. |
| Google Sheets | Available | Arguments are named `rate`, `number_of_periods`, `present_value`, `future_value` and `end_or_beginning`. |

## Tips and Best Practices

- Divide the annual rate by the number of payments per year, and multiply the number of years by the same figure.
- Use `type` 1 only when payments are made at the start of each period, such as rent or a deposit made in advance.
- Use `fv` to model a balloon payment or a target balance, and leave it out for a fully repaid loan.
- Check the sign of the result against your cash flow direction, because a negative payment is money you pay out. Use `=-PMT(...)` for a positive display.
- Multiply the payment by `nper` for the total paid, and subtract `pv` to get the total interest. For the 200,000 mortgage in Example 4, that interest is about 231,676.
- Set `fv` equal to the negative of `pv` for an interest-only payment: `=PMT(6%/12, 360, 200000, -200000)` returns `-1000.00`, which is one month of interest at 0.5%.
- Match the period to the payment frequency for any schedule. Weekly payments on 15,000 at 5% over 5 years use `=PMT(5%/52, 5*52, 15000)`, which returns `-65.23`.
- Enter a negative present value to turn PMT into a withdrawal amount. `=PMT(4%/12, 25*12, -800000)` returns `4222.69`, the monthly amount a 800,000 balance can pay out over 25 years.
- Verify a schedule by adding the first IPMT and PPMT: they must equal the PMT result.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PPMT](PPMT.md) | Returns the principal part of a payment for one period. |
| [IPMT](IPMT.md) | Returns the interest part of a payment for one period. |
| [PV](PV.md) | Returns the present value of a series of payments. |
| [FV](FV.md) | Returns the future value of an investment with regular payments. |
| [NPER](NPER.md) | Solves for the number of payments when the payment is known. |
| [RATE](RATE.md) | Solves for the interest rate when the payment is known. |
| [CUMIPMT](CUMIPMT.md) | Returns the total interest paid between two payments. |

## Official Documentation

- [Microsoft Support: PMT function](https://support.microsoft.com/en-us/excel/functions/pmt-function)
- [Google Docs Editors Help: PMT](https://support.google.com/docs/answer/3093185)
