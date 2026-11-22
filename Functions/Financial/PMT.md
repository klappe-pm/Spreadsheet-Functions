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
  - FV
  - IPMT
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

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Payment far too large | The annual rate was used with a monthly term. | Divide the annual rate by 12 for monthly payments. |
| Payment far too small | The term is in years but the rate is monthly, or the other way around. | Convert both arguments to the same period. |
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
- Check the sign of the result against your cash flow direction, because a negative payment is money you pay out.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PPMT](PPMT.md) | Returns the principal part of a payment for one period. |
| [IPMT](IPMT.md) | Returns the interest part of a payment for one period. |
| [PV](PV.md) | Returns the present value of a series of payments. |
| [FV](FV.md) | Returns the future value of an investment with regular payments. |
| [RATE](RATE.md) | Solves for the interest rate when the payment is known. |

## Official Documentation

- [Microsoft Support: PMT function](https://support.microsoft.com/en-us/excel/functions/pmt-function)
- [Google Docs Editors Help: PMT](https://support.google.com/docs/answer/3093185)
