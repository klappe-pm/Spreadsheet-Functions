---
domain: Spreadsheet Functions
category: Financial
subcategory: Investment Returns
purpose:
  - Financial Modeling
  - Investment Analysis
use-case:
  - Education Savings Projection
  - Emergency Fund Growth
  - Retirement Savings Projection
related:
  - FVSCHEDULE
  - NPER
  - PMT
  - PV
  - RATE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/fv-function
  - https://support.google.com/docs/answer/3093224
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Future Value
  - Future Value of Savings
tags:
  - compound-interest
  - excel
  - investment
  - sheets
---

# FV

## Description

**FV** returns the future value of an investment that grows at a constant interest rate. It handles a lump sum, a series of regular payments, or both at once. A deposit of 250 a month into an account paying 5% a year grows to about 38,821 after ten years, and FV calculates that total in one step, without a table of monthly balances.

The function follows a sign convention that trips up many users. Cash you pay out, such as a deposit, is entered as a negative number, and cash you receive, such as the final balance, comes back as a positive number. If you enter both the payments and the starting amount as positive numbers, the result is negative, which means the calculation has been set up as a loan rather than a savings plan.

Timing matters as well. By default, payments fall at the end of each period. Setting `type` to 1 moves them to the beginning of each period, which adds one period of growth to every payment. The rate and the number of periods must use the same time unit, so a monthly payment needs a monthly rate, obtained by dividing the annual rate by 12, and a number of periods counted in months.

FV is the forward-looking counterpart of [PV](PV.md), which discounts future amounts back to today. [PMT](PMT.md) solves for the payment needed to reach a target, [NPER](NPER.md) solves for the number of periods, and [RATE](RATE.md) solves for the rate. [FVSCHEDULE](FVSCHEDULE.md) applies a series of different rates when the rate changes over time.

## Syntax

```excel
=FV(rate, nper, pmt, [pv], [type])
```

<!-- Image 1: FV Cash Flow Signs. See Images/Financial/FV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The interest rate per period. For 5% a year paid monthly, use `0.05/12`. |
| `nper` | Yes | The total number of payment periods. For 10 years of monthly payments, use `10*12` (120). |
| `pmt` | Yes | The payment made each period, which stays the same for the whole term. Enter payments you make as negative numbers. If `pmt` is 0, the function calculates the growth of `pv` alone. |
| `pv` | No | The present value, or the lump sum you start with. If omitted, it is 0. Enter a sum you invest as a negative number. |
| `type` | No | When payments fall due. `0` or omitted means the end of each period. `1` means the beginning of each period. |

### Return Value

A single number giving the value of the investment at the end of the last period. A positive result means the money is owed to you, and a negative result means it is owed by you. When the deposits and the starting amount are both negative, the result is positive.

## Examples

### Example 1: Monthly Savings Plan

```excel
=FV(0.05/12, 120, -250)
```

**Result:** `38820.57`

Saving 250 a month for 10 years at 5% a year, starting from zero, produces about 38,821. Total deposits are 30,000, so about 8,821 of the balance is interest.

### Example 2: Lump Sum and Monthly Deposits Together

```excel
=FV(0.04, 10, -1000, -5000, 1)
```

**Result:** `19887.57`

The starting amount of 5000 and the annual deposits of 1000 are both entered as negative numbers. The `1` in the last position means the deposits are made at the start of each year.

### Example 3: Monthly Deposits With an Opening Balance

```excel
=FV(0.06/12, 60, -300, -2000, 0)
```

**Result:** `23628.71`

The opening balance of 2000 and the monthly deposits of 300 both grow for 60 months at 0.5% a month.

### Example 4: Lump Sum Only

```excel
=FV(0.07, 20, 0, -10000)
```

**Result:** `38696.84`

With no regular payments, the function shows how a single 10000 deposit grows at 7% for 20 years.

### Example 5: Reversing the Sign

```excel
=FV(0.05/12, 120, 250)
```

**Result:** `-38820.57`

Entering the payments as positive numbers reverses the sign of the result. This is the expected outcome when the same formula models a loan from the lender's point of view.

<!-- Image 2: Savings Growth Over Time. See Images/Financial/FV.md -->

## Story Problems

### Problem 1: Building an Emergency Fund

A family has 2000 in a savings account. It plans to deposit 250 a month for 8 years into an account paying 4.5% a year, compounded monthly. The family wants to know the balance at the end.

| Input | Value |
| --- | --- |
| Annual rate | 0.045 |
| Years | 8 |
| Monthly deposit | 250 |
| Opening balance | 2000 |

**Task:** Put the annual rate in `B2`, the years in `B3`, the monthly deposit in `B4` and the opening balance in `B5`. Enter the deposit and opening balance as negative numbers in the formula, then find the balance after 96 months.

**Solution:**

```excel
=FV(B2/12, B3*12, -B4, -B5)
```

**Answer:** `31689.04`. The family deposits 24,000 plus the opening 2000, and about 5,689 of the balance is growth.

### Problem 2: Annual Deposits at the Start of the Year

A couple deposits 2000 at the start of each year into an account paying 3% a year for 15 years. The couple wants the balance at the end of the 15th year.

| Input | Value |
| --- | --- |
| Annual rate | 0.03 |
| Years | 15 |
| Annual deposit | 2000 |

**Task:** Find the balance using the same input cells, with the deposits made at the start of each year.

**Solution:**

```excel
=FV(B2, B3, -B4, 0, 1)
```

**Answer:** `38313.76`. Because each deposit is made at the start of the year, it earns one extra year of interest compared with an end-of-year deposit.

## Use Cases

### Retirement Savings Projection

**Scenario:** An employee estimates the balance of a retirement account at age 65 from current contributions and an expected return.

```excel
=FV(Return/12, YearsToRetire*12, -MonthlyContribution, -CurrentBalance)
```

**Why It Works:** Each input sits in a labeled cell, so the employee can test different returns and contribution levels without changing the formula.

### Education Savings Projection

**Scenario:** A parent checks whether a monthly deposit will reach a college savings target by the time a child turns 18.

```excel
=FV(Rate/12, 18*12, -MonthlyDeposit)
```

**Why It Works:** Comparing the projected balance with the target shows whether the deposit is large enough, and PMT can then solve for the deposit that meets the target exactly.

### Emergency Fund Growth

**Scenario:** A household tracks how its emergency fund grows if it keeps saving at the current rate.

```excel
=FV(SavingsRate/12, Months, -MonthlyAddition, -CurrentFund)
```

**Why It Works:** Projecting the fund at several horizons shows the balance at each point in time, which helps set realistic savings goals.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | One of the arguments is text. | Enter every argument as a number. |
| Result is negative when expecting a positive value | Deposits and the opening balance were entered as positive numbers. | Enter money you pay in as negative numbers. |
| Result is far too small | The annual rate was used with monthly periods, or the rate was typed as 5 instead of 0.05. | Divide the annual rate by 12 for monthly periods and enter the rate as a decimal. |
| Result is off by one period of growth | `type` does not match when the deposits are made, for example 0 is used for deposits made at the start of each period. | Set `type` to 1 for beginning-of-period payments and 0 for end-of-period payments. |
| Result differs from an online calculator | The calculator assumes a different timing or compounding frequency. | Confirm the timing, rate period and compounding in both places. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions listed on the Microsoft page | `pmt` is required, `pv` and `type` are optional. The Microsoft page does not list error conditions. |
| Google Sheets | Available | The arguments are named `rate`, `number_of_periods`, `payment_amount`, `present_value` and `end_or_beginning`. `present_value` and `end_or_beginning` default to 0. The help page gives sample calls but no outputs. |

## Tips and Best Practices

- Match the rate and the number of periods: divide the annual rate by 12 and multiply the years by 12 for monthly deposits.
- Enter money you put in as negative numbers so that the final balance is positive.
- Compare the result with and without the opening balance to see how much of the total comes from each source.
- Run several rates, such as 4%, 6% and 8%, before presenting a projection, because the outcome is sensitive to the rate.
- Use [PMT](PMT.md) to find the deposit needed for a goal, then check it with FV.
- Decide whether the projection is nominal or inflation-adjusted, and say so in the report.

## Related Functions

| Function | Relationship |
| --- | --- |
| [PV](PV.md) | Discounts a future amount or series of payments back to today. |
| [PMT](PMT.md) | Calculates the regular payment needed to reach a target balance. |
| [NPER](NPER.md) | Calculates how many periods are needed to reach a target balance. |
| [RATE](RATE.md) | Calculates the rate needed to reach a target balance. |
| [FVSCHEDULE](FVSCHEDULE.md) | Calculates future value when the interest rate changes from period to period. |

## Official Documentation

- [Microsoft Support: FV function](https://support.microsoft.com/en-us/excel/functions/fv-function)
- [Google Docs Editors Help: FV](https://support.google.com/docs/answer/3093224)
