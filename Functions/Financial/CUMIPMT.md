---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
purpose:
  - Financial Modeling
  - Loan Analysis
use-case:
  - Annual Mortgage Interest Statement
  - Interest Deduction Planning
  - Loan Payoff Comparison
related:
  - CUMPRINC
  - IPMT
  - PMT
  - PPMT
  - RATE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/cumipmt-function
  - https://support.google.com/docs/answer/3093211
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Cumulative Interest
  - Cumulative Loan Interest
tags:
  - amortization
  - excel
  - loan
  - sheets
---

# CUMIPMT

## Description

**CUMIPMT** returns the total interest paid on a loan between two payment periods. Instead of adding up individual interest amounts one period at a time, you give it the rate, the number of periods, the loan amount, and the first and last periods you care about, and it returns the sum in one step. It is the function to use when a question asks how much interest was paid in year 3 of a mortgage, or across the first 60 months of a car loan.

The function assumes a loan with fixed payments and a fixed rate. Each payment covers the interest accrued since the previous payment, and the rest reduces the balance. Early payments therefore carry most of the interest, which is why CUMIPMT for periods 1 to 12 is much larger than CUMIPMT for periods 349 to 360 on the same 30-year loan.

CUMIPMT and [CUMPRINC](CUMPRINC.md) split the same payments into their two parts. For any range of periods, the interest total plus the principal total equals the sum of the payments in that range. Use [IPMT](IPMT.md) when you need the interest for one period, and [PMT](PMT.md) when you need the regular payment itself.

Excel returns interest paid as a negative number because it is cash leaving the borrower. Wrap the function in ABS when a report needs a positive figure. Google Sheets uses the same six-argument design, but its argument names differ and it rounds the period arguments, which is covered under Platform Differences.

## Syntax

```excel
=CUMIPMT(rate, nper, pv, start_period, end_period, type)
```

<!-- Image 1: CUMIPMT Argument Layout. See Images/Financial/CUMIPMT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The interest rate per period. For a 6% annual loan with monthly payments, use `0.06/12`. Keep it in the same time unit as `nper`. |
| `nper` | Yes | The total number of payment periods. For a 30-year monthly loan, use `30*12` (360). Must be greater than 0. |
| `pv` | Yes | The present value, which for a loan is the amount borrowed. Enter it as a positive number. A value of 0 or less returns `#NUM!`. |
| `start_period` | Yes | The first payment period in the range, counted from 1. Must be at least 1 and no greater than `end_period`. |
| `end_period` | Yes | The last payment period in the range. Must be at least 1 and no less than `start_period`. |
| `type` | Yes | When payments fall due: `0` for the end of each period, `1` for the beginning. Any other value returns `#NUM!`. |

### Return Value

A single negative number equal to the total interest paid between `start_period` and `end_period`. The result is negative because the borrower pays the interest out. The function returns `#NUM!` when `rate`, `nper` or `pv` is 0 or less, when a period is below 1, when `start_period` is greater than `end_period`, or when `type` is not 0 or 1.

## Examples

All examples use a loan of 200000 at 6% a year, repaid in 360 monthly payments. The monthly payment is 1199.10.

### Example 1: Interest in the First Year

Inputs: rate `0.06/12`, nper `360`, pv `200000`, periods 1 to 12, type `0`.

```excel
=CUMIPMT(0.06/12, 360, 200000, 1, 12, 0)
```

**Result:** `-11933.19`

The borrower pays about 11,933 in interest during the first 12 months. Almost all of the 14,389 paid in that year goes to interest, because the balance is still high.

### Example 2: Interest in the Second Year

Inputs: the same loan, periods 13 to 24.

```excel
=CUMIPMT(0.06/12, 360, 200000, 13, 24, 0)
```

**Result:** `-11781.71`

Interest in year 2 is slightly lower than in year 1 because the balance fell during year 1.

<!-- Image 2: Interest Share of Payments by Year. See Images/Financial/CUMIPMT.md -->

### Example 3: Total Interest Over the Life of the Loan

```excel
=CUMIPMT(0.06/12, 360, 200000, 1, 360, 0)
```

**Result:** `-231676.38`

Across all 360 payments, the interest is 231,676.38. This matches the total paid (1199.10 times 360) minus the 200000 borrowed.

### Example 4: Positive Interest Total

```excel
=ABS(CUMIPMT(0.06/12, 360, 200000, 1, 12, 0))
```

**Result:** `11933.19`

ABS removes the sign so the figure can go into a report that shows interest as an expense.

### Example 5: Interest in One Period

```excel
=CUMIPMT(0.06/12, 360, 200000, 1, 1, 0)
```

**Result:** `-1000.00`

Period 1 accrues interest on 200000 at 0.5% a month, which is exactly 1000. Testing a single period like this is a quick way to confirm that the rate and nper units match.

## Story Problems

### Problem 1: Interest Statement for a Home Loan

A couple borrowed 150000 at 5% a year over 15 years to buy a house. Their lender asks for the interest paid in the first 12 months for their tax records.

| Input | Value |
| --- | --- |
| Loan amount | 150000 |
| Annual rate | 5% |
| Term in years | 15 |

**Task:** Put the loan amount in `B2`, the annual rate in `B3` and the term in `B4`, then find the interest paid in months 1 to 12.

**Solution:**

```excel
=CUMIPMT(B3/12, B4*12, B2, 1, 12, 0)
```

**Answer:** `-7343.51`. Excel shows the interest as negative, so the couple paid 7343.51 in interest during year 1. The monthly payment is about 1186.19, and the rest of the year's payments reduced the balance.

### Problem 2: Interest in the Second Year

Using the same loan, the couple wants to know how much interest they pay in the second year, which is months 13 to 24.

| Input | Value |
| --- | --- |
| Loan amount | 150000 |
| Annual rate | 5% |
| Term in years | 15 |

**Task:** Change the start and end periods to 13 and 24 and find the interest for that year.

**Solution:**

```excel
=CUMIPMT(B3/12, B4*12, B2, 13, 24, 0)
```

**Answer:** `-6990.96`. Year 2 interest is about 350 lower than year 1 because the balance fell, so the couple paid off a little more principal each month.

## Use Cases

### Annual Mortgage Interest Statement

**Scenario:** A bank customer needs a yearly summary of mortgage interest for a tax preparer.

```excel
=CUMIPMT(Rate/12, Years*12, Loan, 1, 12, 0)
```

**Why It Works:** Named cells hold the rate, term and loan amount, so the same formula can be copied down a sheet with one row per loan. Each row shows the interest for a different year.

### Interest Deduction Planning

**Scenario:** A small landlord compares the interest deductible in each of the next five years on a commercial loan.

```excel
=CUMIPMT(0.065/12, 240, 400000, 1, 12, 0)
```

**Why It Works:** Change the first and last periods to 13 and 24, 25 and 36, and so on, to build a year-by-year table. Confirm the sign convention before adding the figures to a budget.

### Loan Payoff Comparison

**Scenario:** A buyer compares two loans of the same amount: a 30-year loan and a 15-year loan at the same rate.

```excel
=CUMIPMT(0.055/12, 360, 250000, 1, 360, 0)
=CUMIPMT(0.055/12, 180, 250000, 1, 180, 0)
```

**Why It Works:** Totals show how much more interest the longer loan costs over its life. Both formulas use the same rate and amount, so the difference comes only from the term.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | `rate`, `nper` or `pv` is 0 or negative. | Enter the loan amount as a positive number and check that the rate is above 0. |
| `#NUM!` | `start_period` is less than 1, or greater than `end_period`. | Count periods from 1 and make sure the start is not after the end. |
| `#NUM!` | `type` is a value other than 0 or 1. | Use 0 for end-of-period payments or 1 for beginning-of-period payments. |
| Result is far too small | The rate was entered as an annual figure with monthly periods. | Divide the annual rate by 12 and multiply the term in years by 12. |
| Result is negative | Excel reports interest paid as cash leaving the borrower. | Use ABS for a positive total, or subtract from zero in the report. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Listed for Excel 2016, Excel 2019, Excel 2021, Excel 2024 and Microsoft 365 | All six arguments are required. Interest is returned as a negative number. |
| Google Sheets | Available | Argument names are `rate`, `number_of_periods`, `present_value`, `first_period`, `last_period` and `end_or_beginning`. A decimal `first_period` rounds up and a decimal `last_period` rounds down. The help page does not document error values or the sign of the result, so check the sign in Sheets before relying on it. |

## Tips and Best Practices

- Divide the rate and multiply the term so that both use the same time unit as the payments.
- Test one period first, such as `CUMIPMT(..., 1, 1, 0)`, to confirm the inputs before summing a long range.
- Keep the loan amount in its own cell so the same formula works for every loan in a list.
- Pair CUMIPMT with [CUMPRINC](CUMPRINC.md) on the same range; their totals should add up to the payments made.
- Use [IPMT](IPMT.md) and [PPMT](PPMT.md) when you need a period-by-period schedule rather than a single total.
- Check the type argument against the loan contract, because beginning-of-period payments change the interest total.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CUMPRINC](CUMPRINC.md) | Totals the principal portion of the same payments over the same periods. |
| [IPMT](IPMT.md) | Returns the interest for one period instead of a range. |
| [PPMT](PPMT.md) | Returns the principal for one period. |
| [PMT](PMT.md) | Returns the regular payment that CUMIPMT assumes. |
| [RATE](RATE.md) | Solves for the interest rate when the payments and term are known. |

## Official Documentation

- [Microsoft Support: CUMIPMT function](https://support.microsoft.com/en-us/excel/functions/cumipmt-function)
- [Google Docs Editors Help: CUMIPMT](https://support.google.com/docs/answer/3093211)
