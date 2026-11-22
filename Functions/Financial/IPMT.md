---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
purpose:
  - Financial Modeling
  - Loan Analysis
use-case:
  - Amortization Schedules
  - Loan Interest Split
  - Mortgage Interest Review
related:
  - CUMIPMT
  - CUMPRINC
  - ISPMT
  - PMT
  - PPMT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/ipmt-function
  - https://support.google.com/docs/answer/3093175
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Interest Payment For Period
  - Loan Interest Portion
tags:
  - amortization
  - excel
  - loans
  - sheets
---

# IPMT

## Description

**IPMT** returns the interest part of a loan or annuity payment for one specific period. The payment itself is constant for an annuity, but the split between interest and principal changes each period: early payments are mostly interest, and later payments are mostly principal. IPMT shows how much of a given payment goes to interest.

Pair IPMT with PPMT, which returns the principal part of the same payment. The two results add up to the total payment from PMT. Use IPMT when a schedule needs interest by period, such as for tax reporting, a lender statement or a mortgage review.

Keep the rate and the number of periods in the same units. For monthly payments on a loan with an annual rate, divide the rate by 12 and multiply the years by 12. Excel returns interest paid as a negative number when the loan amount is positive, because interest is a cash outflow for the borrower.

## Syntax

```excel
=IPMT(rate, per, nper, pv, [fv], [type])
```

<!-- Image 1: Rate, Period and Loan Amount Arguments. See Images/Financial/IPMT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The interest rate per period. Use `7.5%/12` for a monthly payment on a 7.5% annual loan. |
| `per` | Yes | The payment period to calculate. Must be from 1 to `nper`. |
| `nper` | Yes | The total number of payment periods in the loan. |
| `pv` | Yes | The present value, or the loan amount. A positive loan amount produces negative interest results. |
| `fv` | No | The balance remaining after the last payment. Omitted means 0. |
| `type` | No | When payments are due: 0 for the end of each period (the default) or 1 for the beginning. |

### Return Value

The interest portion of the payment for the chosen period, as a number. Excel returns a negative number when `pv` is positive. Microsoft's page gives the valid range for `per` as 1 to `nper` and does not list other error values.

## Examples

### Example 1: First Monthly Payment

```excel
=IPMT(0.075/12, 1, 60, 15000)
```

**Result:** `-93.75`

The first payment of a 15,000 loan at 7.5% a year, repaid over 60 months, contains 93.75 of interest: 15,000 x 0.625% per month.

### Example 2: Interest in a Later Month

```excel
=IPMT(0.075/12, 13, 60, 15000)
```

**Result:** `-77.69`

By payment 13, the balance is lower, so the interest part is smaller than in Example 1.

<!-- Image 2: Interest Share Falls Over the Loan Term. See Images/Financial/IPMT.md -->

### Example 3: Annual Payments

```excel
=IPMT(0.075, 3, 5, 15000)
```

**Result:** `-723.10`

With one payment a year over five years, the third payment carries 723.10 of interest.

### Example 4: Combining With PPMT

```excel
=IPMT(0.075/12, 13, 60, 15000) + PPMT(0.075/12, 13, 60, 15000)
```

**Result:** `-300.57`

Interest (-77.69) and principal (-222.88) add up to the level monthly payment of 300.57, shown negative because the loan amount is positive.

## Story Problems

### Problem 1: Equipment Loan Interest in Month Thirteen

A print shop borrows 15,000 at 7.5% a year, repaid in 60 equal monthly payments. The loan terms are in the table below.

| Item | Value |
| --- | --- |
| Loan amount | 15000 |
| Annual rate | 7.5% |
| Number of monthly payments | 60 |

**Task:** Find how much of payment 13 is interest.

**Solution:**

```excel
=-IPMT(7.5%/12, 13, 60, 15000)
```

**Answer:** `77.69`. The balance before payment 13 is still high enough that the monthly interest is 77.69.

### Problem 2: Annual Payments in Year Three

A farm equipment loan of 15,000 at 7.5% is repaid in five equal annual payments of 3,707.47. The accountant needs the interest in the third payment.

| Item | Value |
| --- | --- |
| Loan amount | 15000 |
| Annual rate | 7.5% |
| Number of annual payments | 5 |

**Task:** Find the interest portion of payment 3.

**Solution:**

```excel
=-IPMT(7.5%, 3, 5, 15000)
```

**Answer:** `723.10`. The interest is 7.5% of the balance that remains after two payments.

<!-- Image 3: Interest Results for the Loan Problems. See Images/Financial/IPMT.md -->

## Use Cases

### Amortization Schedules

**Scenario:** A lender builds a 60-month schedule that shows interest and principal for every payment.

```excel
=IPMT(Rate/12, A2, Term, Loan)
```

**Why It Works:** Filling the formula down the column of period numbers gives the interest for each row, and `PPMT` in an adjacent column gives the principal. The two columns total the level payment in every row.

### Mortgage Interest Review

**Scenario:** A homeowner wants to see how much of the first payment goes to interest before choosing whether to make extra principal payments.

```excel
=-IPMT(Rate/12, 1, Term*12, Loan)
```

**Why It Works:** The first period carries the largest interest share, so this cell shows the most interest the borrower pays on any single payment. Compare it with the level payment from PMT to see how slowly principal falls at the start of a loan.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Period out of range | `per` is less than 1 or greater than `nper`. | Use a period from 1 to `nper`. |
| Interest far too large | An annual rate was used with monthly periods. | Divide the annual rate by 12 for monthly payments. |
| Interest sign is negative | The loan amount is positive, so interest is a cash outflow. | Use a leading minus sign or present the result as a cost. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, Excel 2019, Excel 2021, Excel 2024, Microsoft 365, Excel for the web and Excel for iPhone | Returns a negative value for interest paid when `pv` is positive. |
| Google Sheets | Available | Uses the same argument order as Excel. The page does not state the sign of the result, so check it against a known schedule. |

## Tips and Best Practices

- Build a full amortization table and check that the last balance is 0 before relying on any single period.
- Keep `rate` and `nper` in matching units: monthly rate with monthly periods, annual rate with annual periods.
- Use PMT to find the level payment before using IPMT or PPMT.
- Use `CUMIPMT` to add interest across a range of periods instead of summing many IPMT results.
- Format the result with a negative sign convention that matches the report, and label it so readers know it is interest paid.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PPMT](PPMT.md) | Principal part of the same payment. IPMT and PPMT add up to PMT. |
| [PMT](PMT.md) | Level payment for the loan, used as the total of interest and principal. |
| [CUMIPMT](CUMIPMT.md) | Total interest across a range of periods. |
| [CUMPRINC](CUMPRINC.md) | Total principal across a range of periods. |
| [ISPMT](ISPMT.md) | Interest for a loan with equal principal payments instead of equal total payments. |

## Official Documentation

- [Microsoft Support: IPMT function](https://support.microsoft.com/en-us/excel/functions/ipmt-function)
- [Google Docs Editors Help: IPMT](https://support.google.com/docs/answer/3093175)
