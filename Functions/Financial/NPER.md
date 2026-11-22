---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
purpose:
  - Financial Modeling
  - Loan Analysis
use-case:
  - Loan Payoff Timeline
  - Payment Plan Length
  - Savings Goal Timing
related:
  - FV
  - IPMT
  - PMT
  - PV
  - RATE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/nper-function
  - https://support.google.com/docs/answer/3093183
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Number Of Periods
  - Payment Count
tags:
  - amortization
  - excel
  - savings-goal
  - sheets
---

# NPER

## Description

**NPER** returns the number of periods needed for an investment or loan to reach a target, based on a constant interest rate and constant payments. Use it to answer questions such as how long a loan takes to repay at a given monthly payment, or how many deposits are needed to reach a savings goal.

The result is often fractional. A loan that needs 57.68 monthly payments is paid off with 58 payments, and the last one is smaller than the rest. Round up with `ROUNDUP` when the question asks for the number of payments.

Keep the rate and the payment in the same period. A monthly payment needs a monthly rate, so divide an annual rate by 12. Excel and Sheets treat money paid out as negative and money received as positive, so a loan received as a positive amount has negative payments.

## Syntax

```excel
=NPER(rate, pmt, pv, [fv], [type])
```

<!-- Image 1: Rate, Payment and Present Value Arguments. See Images/Financial/NPER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The interest rate per period. Use `6%/12` for a monthly payment on a 6% annual loan. |
| `pmt` | Yes | The payment made each period. It stays the same for the life of the loan and usually includes principal and interest only. |
| `pv` | Yes | The present value, or the amount borrowed or invested today. |
| `fv` | No | The balance to reach after the last payment. Omitted means 0. |
| `type` | No | When payments are due: 0 for the end of each period (the default) or 1 for the beginning. |

### Return Value

The number of periods as a decimal, such as `57.68`. It can be fractional because the last period may be partly complete.

## Examples

### Example 1: Loan Payoff

```excel
=NPER(0.06/12, -400, 20000)
```

**Result:** `57.68`

Paying 400 a month on a 20,000 loan at 6% a year takes about 57.68 months.

### Example 2: Savings Goal

```excel
=NPER(0.04/12, -200, 0, 15000)
```

**Result:** `67.05`

Depositing 200 a month at 4% a year, starting from zero, reaches 15,000 after about 67.05 deposits.

### Example 3: Payments at the Beginning

```excel
=NPER(0.06/12, -400, 20000, 0, 1)
```

**Result:** `57.35`

When each payment is due at the start of the month, the loan clears a little sooner.

<!-- Image 2: Loan Balance Falling Across Payments. See Images/Financial/NPER.md -->

### Example 4: Rounding Up to Whole Payments

```excel
=ROUNDUP(NPER(0.06/12, -400, 20000), 0)
```

**Result:** `58`

A loan with 57.68 periods needs 58 payments, the last of which is smaller.

## Story Problems

### Problem 1: Repaying an Equipment Loan

A bakery borrows 20,000 at 6% a year and pays 400 each month. The accountant needs the number of payments.

| Item | Value |
| --- | --- |
| Loan amount | 20000 |
| Annual rate | 6% |
| Monthly payment | 400 |

**Task:** Find the number of monthly payments, rounded up to a whole payment.

**Solution:**

```excel
=ROUNDUP(NPER(6%/12, -B4, B2), 0)
```

**Answer:** `58` payments. The unrounded value is 57.68, so after 57 full payments a balance of 270.92 remains, and the 58th payment is 272.27.

### Problem 2: Reaching a Savings Goal

A family wants 15,000 for a car. It can save 200 a month in an account that pays 4% a year, starting from zero.

| Item | Value |
| --- | --- |
| Target amount | 15000 |
| Monthly deposit | 200 |
| Annual rate | 4% |

**Task:** Find the number of monthly deposits needed to reach the target.

**Solution:**

```excel
=ROUNDUP(NPER(4%/12, -200, 0, 15000), 0)
```

**Answer:** `68` deposits. After 67 deposits the balance is just short of 15,000, so the 68th deposit completes the goal.

<!-- Image 3: Payment Count Results. See Images/Financial/NPER.md -->

## Use Cases

### Loan Payoff Timeline

**Scenario:** A borrower wants to know how long a loan will last if the monthly payment is increased.

```excel
=ROUNDUP(NPER(Rate/12, -NewPayment, Balance), 0)
```

**Why It Works:** Changing the payment cell updates the payoff count, so the borrower can test several payment amounts before choosing one.

### Savings Goal Timing

**Scenario:** A saver wants to know how many monthly deposits a target fund needs, given a fixed contribution.

```excel
=ROUNDUP(NPER(Rate/12, -Deposit, 0, TargetAmount), 0)
```

**Why It Works:** Setting the present value to 0 starts the account empty. The future value holds the target, and the payment is negative because it is money put in.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| No solution | The payment is smaller than the interest, so the balance never falls to the target. | Increase the payment or lower the target. |
| Wrong count by a factor of 12 | An annual rate was used with monthly payments. | Divide the annual rate by 12. |
| Negative result | The signs of the payment and the present value match, so the loan and payments do not offset. | Enter money received as positive and money paid as negative. |
| Fractional result | The loan does not divide evenly into whole payments. | Round up with `ROUNDUP` to get the number of payments. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Microsoft 365 and Excel for the web | Returns a decimal number of periods. The page refers readers to PV for a fuller description of the arguments. |
| Google Sheets | Available | Uses `rate`, `payment_amount`, `present_value`, `future_value` and `end_or_beginning` in the same order. The page does not state the sign convention. |

## Tips and Best Practices

- Keep the rate and the payment in the same period: monthly rate with monthly payments, annual rate with annual payments.
- Round the result up with `ROUNDUP` when the question asks for whole payments.
- Use PMT to find the payment for a given term, and NPER to find the term for a given payment.
- Check the result with FV or PV: the balance after the calculated periods should be close to zero or the target.
- Keep the sign convention consistent across the sheet, with money paid out negative and money received positive.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PMT](PMT.md) | Level payment for a given rate, term and amount. |
| [PV](PV.md) | Present value that a series of payments is worth today. |
| [FV](FV.md) | Future value of an investment or a series of deposits. |
| [RATE](RATE.md) | Rate per period for a given term and payment. |
| [IPMT](IPMT.md) | Interest part of a payment for one period. |

## Official Documentation

- [Microsoft Support: NPER function](https://support.microsoft.com/en-us/excel/functions/nper-function)
- [Google Docs Editors Help: NPER](https://support.google.com/docs/answer/3093183)
