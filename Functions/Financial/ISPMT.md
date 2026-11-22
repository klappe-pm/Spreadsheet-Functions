---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
purpose:
  - Financial Modeling
  - Loan Analysis
use-case:
  - Even Principal Loans
  - Interest Schedule Review
related:
  - CUMIPMT
  - CUMPRINC
  - IPMT
  - PMT
  - PPMT
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/ispmt-function
  - https://support.google.com/docs/answer/9116481
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Even Principal Interest
tags:
  - amortization
  - excel
  - loans
  - sheets
---

# ISPMT

## Description

**ISPMT** returns the interest charged for a period of a loan or investment that repays equal amounts of principal each period. The interest falls each period because the balance falls, so the total payment also falls over the life of the loan.

This differs from IPMT, which assumes equal total payments, where the principal share rises as the interest share falls. Use ISPMT when the lender's schedule shows the same principal reduction each period, which is common in business loans and some bank term loans.

Keep the rate and the number of periods in the same units. A monthly schedule needs a monthly rate, so divide the annual rate by 12 and multiply the years by 12. Excel returns interest paid as a negative number when the loan amount is positive.

## Syntax

```excel
=ISPMT(rate, per, nper, pv)
```

<!-- Image 1: Even Principal Loan Arguments. See Images/Financial/ISPMT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The interest rate per period, in the same units as `nper`. |
| `per` | Yes | The period whose interest you want. Microsoft gives a range of 1 to `nper`, but its remarks say periods count from zero, so test the first period on a known schedule before you rely on it. |
| `nper` | Yes | The total number of periods in the loan. |
| `pv` | Yes | The present value, or the loan amount. A positive loan amount produces negative interest results. |

### Return Value

The interest for the chosen period as a number, negative in Excel when `pv` is positive. The function returns the interest on the balance that remains after `per` equal principal payments.

## Examples

### Example 1: Interest After Two Principal Payments

```excel
=ISPMT(0.09, 2, 4, 20000)
```

**Result:** `-900.00`

After two of four equal principal payments, 10,000 of the 20,000 loan remains, and 9% of 10,000 is 900.

### Example 2: Monthly Schedule

```excel
=ISPMT(0.09/12, 6, 48, 24000)
```

**Result:** `-157.50`

The 24,000 loan has 21,000 left after six of 48 principal payments. At 0.75% a month, the interest is 157.50.

<!-- Image 2: Declining Interest on an Equal Principal Loan. See Images/Financial/ISPMT.md -->

### Example 3: Interest in the Last Period

```excel
=ISPMT(0.09, 3, 4, 20000)
```

**Result:** `-450.00`

Three payments leave 5,000 outstanding, so the interest in the final period is 450.

## Story Problems

### Problem 1: Monthly Equal Principal Loan

A small clinic borrows 24,000 over 48 months, repaying an equal share of principal each month. The interest rate is 9% a year.

| Item | Value |
| --- | --- |
| Loan amount | 24000 |
| Annual rate | 9% |
| Number of months | 48 |

**Task:** Find the interest charged after six principal payments have been made.

**Solution:**

```excel
=ISPMT(9%/12, 6, 48, 24000)
```

**Answer:** `157.50`. The balance after six payments is 21,000, and 0.75% of 21,000 is 157.50.

### Problem 2: Business Term Loan

A hardware store borrows 60,000 at 8% a year, repaid in five annual payments of equal principal. Its accountant needs the interest after two years of repayments.

| Item | Value |
| --- | --- |
| Loan amount | 60000 |
| Annual rate | 8% |
| Number of years | 5 |

**Task:** Find the interest after two principal payments.

**Solution:**

```excel
=ISPMT(8%, 2, 5, 60000)
```

**Answer:** `-2880.00`, shown negative because the loan amount is positive. The balance is 36,000, and 8% of 36,000 is 2,880.

<!-- Image 3: Interest Results for the Loan Problems. See Images/Financial/ISPMT.md -->

## Use Cases

### Even Principal Loans

**Scenario:** A lender quotes a business loan with a fixed principal reduction each period and needs the interest for each scheduled payment.

```excel
=ISPMT(Rate/12, Period, Term*12, Loan)
```

**Why It Works:** The formula gives the interest for any period from one cell reference, so a schedule can be built by changing only the period column. Check the first row against a hand calculation, because the period count convention matters.

### Interest Schedule Review

**Scenario:** An auditor compares the interest a bank charged with the interest on a schedule built from the loan terms.

```excel
=ABS(ISPMT(Rate/12, A2, Term*12, Loan)) - BankInterest
```

**Why It Works:** The `ABS` wrapper removes the negative sign so the result compares directly with the bank's positive figure. A nonzero difference points to a rate, term or period-count mismatch.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result off by one period | The period count convention differs from the lender's schedule. | Check the first and last periods against the lender's statement and adjust the `per` value. |
| Interest far too large | An annual rate was used with monthly periods. | Divide the annual rate by 12 for monthly payments. |
| Interest sign is negative | The loan amount is positive, so interest is a cash outflow. | Use `ABS` or a leading minus sign when a positive figure is needed. |
| Wrong schedule | The loan repays equal total payments, not equal principal. | Use IPMT for equal total payments and ISPMT only for equal principal payments. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Microsoft 365 and Excel for the web | Returns negative interest when `pv` is positive. Remarks say periods count from zero. |
| Google Sheets | Available | Uses the same argument order. The page does not state the sign of the result or the period count convention. |

## Tips and Best Practices

- Confirm the principal schedule with the lender before choosing ISPMT, because the formula assumes equal principal payments.
- Test one period by hand against the lender's statement before filling the formula down a schedule.
- Keep the rate and the period count in the same units.
- Use IPMT for equal total payments, and PMT to find the level payment on those loans.
- Label the result as interest paid so that the negative sign does not confuse readers.

## Related Functions

| Function | Relationship |
| --- | --- |
| [IPMT](IPMT.md) | Interest for a loan with equal total payments. |
| [PPMT](PPMT.md) | Principal part of an equal-payment loan. |
| [PMT](PMT.md) | Level payment for an equal-payment loan. |
| [CUMIPMT](CUMIPMT.md) | Total interest across a range of periods on an equal-payment loan. |
| [CUMPRINC](CUMPRINC.md) | Total principal across a range of periods on an equal-payment loan. |

## Official Documentation

- [Microsoft Support: ISPMT function](https://support.microsoft.com/en-us/excel/functions/ispmt-function)
- [Google Docs Editors Help: ISPMT](https://support.google.com/docs/answer/9116481)
