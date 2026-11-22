---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
purpose:
  - Financial Modeling
  - Loan Analysis
use-case:
  - Principal Paydown Tracking
  - Refinance Comparison
  - Year-End Loan Balance Review
related:
  - CUMIPMT
  - IPMT
  - NPER
  - PMT
  - PPMT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/cumprinc-function
  - https://support.google.com/docs/answer/3093159
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cumulative Principal
  - Cumulative Loan Principal
tags:
  - amortization
  - excel
  - loan
  - sheets
---

# CUMPRINC

## Description

**CUMPRINC** returns the total principal repaid on a loan between two payment periods. Each regular payment has two parts: the interest that accrued since the last payment, and the principal that reduces the balance. CUMPRINC adds up only the principal part across a range of periods, so you can see how much of the debt was retired in a given year or over a given number of months.

Principal and interest move in opposite directions over a loan's life. In the early years most of each payment is interest and only a small amount reduces the balance. Later payments reverse that split. CUMPRINC makes this visible: the principal total for periods 1 to 12 on a 30-year loan is far smaller than the principal total for periods 349 to 360.

CUMPRINC and [CUMIPMT](CUMIPMT.md) use the same six arguments and split the same payments. For any range, the principal total plus the interest total equals the sum of the payments in that range. Use [PPMT](PPMT.md) for the principal in a single period.

Excel returns principal repaid as a negative number because it is cash leaving the borrower. Wrap the function in ABS when a schedule needs a positive figure. Google Sheets accepts the same arguments under different names and requires `first_period` to be at least 1 and `last_period` to be greater than `first_period`.

## Syntax

```excel
=CUMPRINC(rate, nper, pv, start_period, end_period, type)
```

<!-- Image 1: CUMPRINC Argument Layout. See Images/Financial/CUMPRINC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The interest rate per period. For a 6% annual loan paid monthly, use `0.06/12`. |
| `nper` | Yes | The total number of payment periods. For a 15-year monthly loan, use `15*12` (180). Must be greater than 0. |
| `pv` | Yes | The amount borrowed, entered as a positive number. A value of 0 or less returns `#NUM!`. |
| `start_period` | Yes | The first period in the range, counted from 1. |
| `end_period` | Yes | The last period in the range. Must be at least `start_period`. |
| `type` | Yes | `0` when payments fall at the end of each period, `1` when they fall at the beginning. Any other value returns `#NUM!`. |

### Return Value

A single negative number equal to the principal repaid between `start_period` and `end_period`. The total cannot exceed the amount borrowed. The function returns `#NUM!` when `rate`, `nper` or `pv` is 0 or less, when a period is below 1, when `start_period` is greater than `end_period`, or when `type` is not 0 or 1.

## Examples

All examples use a loan of 200000 at 6% a year, repaid in 360 monthly payments of 1199.10.

### Example 1: Principal Repaid in the First Year

```excel
=CUMPRINC(0.06/12, 360, 200000, 1, 12, 0)
```

**Result:** `-2456.02`

Only 2,456.02 of the 14,389.21 paid in year 1 reduces the balance. The rest is interest, shown in [CUMIPMT](CUMIPMT.md).

### Example 2: Principal in a Single Period

```excel
=CUMPRINC(0.06/12, 360, 200000, 1, 1, 0)
```

**Result:** `-199.10`

The first payment of 1199.10 includes 1000.00 of interest, so 199.10 goes to principal. This is the simplest check on the rate and period units.

### Example 3: Principal in the Second Year

```excel
=CUMPRINC(0.06/12, 360, 200000, 13, 24, 0)
```

**Result:** `-2607.51`

Principal repaid in year 2 is about 150 more than in year 1, because each payment carries a little less interest.

<!-- Image 2: Principal and Interest Split by Period. See Images/Financial/CUMPRINC.md -->

### Example 4: Total Principal Over the Whole Loan

```excel
=CUMPRINC(0.06/12, 360, 200000, 1, 360, 0)
```

**Result:** `-200000.00`

Across every payment, the principal repaid equals the amount borrowed. A result that does not match the loan amount points to an input error.

### Example 5: Checking Principal Plus Interest

```excel
=CUMPRINC(0.06/12, 360, 200000, 1, 12, 0) + CUMIPMT(0.06/12, 360, 200000, 1, 12, 0)
```

**Result:** `-14389.21`

Principal and interest together equal the twelve payments made in year 1. Use this kind of check whenever the two functions feed the same report.

## Story Problems

### Problem 1: Principal Paid in Five Years

A couple borrowed 150000 at 5% a year over 15 years. They want to know how much of the debt they retire in the first five years.

| Input | Value |
| --- | --- |
| Loan amount | 150000 |
| Annual rate | 5% |
| Term in years | 15 |

**Task:** Put the loan amount in `B2`, the annual rate in `B3` and the term in `B4`, then find the principal repaid in months 1 to 60.

**Solution:**

```excel
=CUMPRINC(B3/12, B4*12, B2, 1, 60, 0)
```

**Answer:** `-38164.36`. About 38,164 of the balance is repaid in five years, which is roughly a quarter of the loan. Interest covers the rest of the payments made in that time.

### Problem 2: Principal Share of the First-Year Payments

Using the same loan, the couple compares the principal and interest they pay in year 1.

| Input | Value |
| --- | --- |
| Loan amount | 150000 |
| Annual rate | 5% |
| Term in years | 15 |

**Task:** Find the principal repaid in months 1 to 12, then compare it with the interest for the same months.

**Solution:**

```excel
=CUMPRINC(B3/12, B4*12, B2, 1, 12, 0)
```

**Answer:** `-6890.78`. The principal is less than the interest of 7343.51 for the same year, so the balance falls slowly at first.

## Use Cases

### Principal Paydown Tracking

**Scenario:** A finance team tracks how much of each commercial loan is retired at the end of each fiscal year.

```excel
=CUMPRINC(Rate/12, Term*12, Loan, 1, 12, 0)
```

**Why It Works:** Named cells keep the formula readable and let the team copy it across loans. Shift the period range by twelve for each later year.

### Refinance Comparison

**Scenario:** A homeowner compares the principal repaid in the first five years on the current loan with a refinanced loan at a lower rate.

```excel
=CUMPRINC(0.055/12, 360, 180000, 1, 60, 0)
```

**Why It Works:** Run the same range for each loan. A lower rate usually shifts more of each payment to principal early on, so compare the totals over the same window rather than over the full term.

### Year-End Loan Balance Review

**Scenario:** An accountant confirms that the remaining balance at the end of year 3 matches the original amount less the principal repaid so far.

```excel
=Loan + CUMPRINC(Rate/12, Term*12, Loan, 1, 36, 0)
```

**Why It Works:** Because the principal total is negative, adding it to the loan amount gives the balance left after 36 payments. It is a quick cross-check against the lender's statement.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `rate`, `nper` or `pv` is 0 or negative. | Enter the loan amount as a positive number and check the rate. |
| `#NUM!` | `start_period` is below 1 or greater than `end_period`. | Count periods from 1 and keep the start before the end. |
| `#NUM!` | `type` is not 0 or 1. | Use 0 for end-of-period payments or 1 for beginning-of-period payments. |
| Principal total looks too small | The rate was entered as annual while the periods are monthly. | Divide the rate by 12 and multiply the years by 12. |
| Negative result | Excel reports principal repaid as cash leaving the borrower. | Use ABS for a positive total. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed for Excel 2016, Excel 2019, Excel 2021, Excel 2024 and Microsoft 365 | All six arguments are required. In Excel for the web, set the cell format to General if the result displays incorrectly. |
| Google Sheets | Available | Argument names are `rate`, `number_of_periods`, `present_value`, `first_period`, `last_period` and `end_or_beginning`. The help page does not document error values or the sign of the result. |

## Tips and Best Practices

- Use CUMPRINC with [CUMIPMT](CUMIPMT.md) on the same range, and confirm their sum equals the payments made.
- Build a year-by-year table by moving the start and end periods forward by twelve for monthly loans.
- Enter the loan amount as a positive number so that the sign of the result stays consistent across a workbook.
- Check that the total over the full term equals the loan amount before trusting a model.
- Use [PPMT](PPMT.md) when a schedule needs the principal for one period, and CUMPRINC when it needs a range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CUMIPMT](CUMIPMT.md) | Totals the interest portion of the same payments over the same range. |
| [PPMT](PPMT.md) | Returns the principal portion for a single period. |
| [IPMT](IPMT.md) | Returns the interest portion for a single period. |
| [PMT](PMT.md) | Returns the regular payment that drives both principal and interest. |
| [NPER](NPER.md) | Finds how many periods are needed to repay a loan at a given payment. |

## Official Documentation

- [Microsoft Support: CUMPRINC function](https://support.microsoft.com/en-us/excel/functions/cumprinc-function)
- [Google Docs Editors Help: CUMPRINC](https://support.google.com/docs/answer/3093159)
