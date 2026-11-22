---
domain: Spreadsheet Functions
category: Financial
subcategory: Investment Returns
purpose:
  - Investment Analysis
use-case:
  - Growth Milestone Tracking
  - Savings Goal Planning
related:
  - FV
  - NPER
  - PV
  - RATE
  - RRI
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/pduration-function
  - https://support.google.com/docs/answer/9368165
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Periods to Reach Future Value
tags:
  - excel
  - growth-period
  - investment-growth
  - sheets
---

# PDURATION

## Description

**PDURATION** returns the number of periods an investment needs to grow from its present value to a target future value, at a fixed rate per period. It answers the question "how long will this take?" for a savings goal, a growth target or a milestone that a value must reach.

The unit of the answer matches the unit of the rate. An annual rate gives years, and a monthly rate gives months. The result is usually a fraction, because a target is rarely reached exactly at the end of a whole period.

Use PDURATION when the rate and the two amounts are known and you need the time. To find the rate instead, use RRI. To find the future value of a fixed number of periods, use FV. Google Sheets documents the calculation as the logarithm of the ratio of the future value to the present value, divided by the logarithm of 1 plus the rate.

## Syntax

```excel
=PDURATION(rate, pv, fv)
```

<!-- Image 1: Growth From Present to Future Value. See Images/Financial/PDURATION.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `rate` | Yes | The growth rate per period. It must be positive. Use the rate for the same period length you want the answer in. |
| `pv` | Yes | The present value, the current amount of the investment. It must be positive. |
| `fv` | Yes | The future value, the target amount to reach. It must be positive. |

### Return Value

A number: the number of periods needed to grow from `pv` to `fv`, in the same period unit as the rate. Excel returns `#NUM!` when any argument is not positive, and `#VALUE!` when an argument has an invalid data type.

## Examples

### Example 1: Years to Reach a Target

```excel
=PDURATION(4%, 5000, 6500)
```

**Result:** `6.69`

At 4% a year, 5,000 grows to 6,500 in about 6.69 years.

### Example 2: Months With a Monthly Rate

```excel
=PDURATION(5%/12, 4000, 9000)
```

**Result:** `195.03`

The annual rate of 5% is divided by 12 to give a monthly rate. The answer is 195.03 months, which is about 16 years.

<!-- Image 2: Annual and Monthly Periods. See Images/Financial/PDURATION.md -->

### Example 3: Wrap the Result in IFERROR

With the rate in `B2`, the present value in `B3` and the future value in `B4`:

```excel
=IFERROR(PDURATION(B2, B3, B4), "Check values")
```

**Result:** `6.69` when `B2` is 4%, `B3` is 5,000 and `B4` is 6,500.

A zero or negative amount shows "Check values" instead of an error code.

## Story Problems

### Problem 1: Years to Reach a Savings Target

A saver has 4,000 invested at 3% a year and wants the balance to reach 5,000. The saver wants to know how many years this will take if the rate stays the same.

| Term | Value |
| --- | --- |
| Annual rate | 3.00% |
| Present value | 4000 |
| Target value | 5000 |

**Task:** Find the number of years until the balance reaches 5,000.

**Solution:**

```excel
=PDURATION(B2, B3, B4)
```

**Answer:** `7.55` years, which is about seven years and seven months.

### Problem 2: Months to Reach a Monthly Target

A small business holds 6,000 in an account that earns 0.5% a month. The owner wants the balance to reach 9,000.

**Task:** Find the number of months needed, using the monthly rate.

**Solution:**

```excel
=PDURATION(B2, B3, B4)
```

Here `B2` is 0.5%, `B3` is 6000 and `B4` is 9000.

**Answer:** `81.30` months, which is about six years and nine months.

<!-- Image 3: Story Problem Inputs and Output. See Images/Financial/PDURATION.md -->

## Use Cases

### Savings Goal Planning

**Scenario:** A household wants to know how long a current balance will take to reach a down payment target.

```excel
=PDURATION(AnnualRate, CurrentBalance, DownPaymentTarget)
```

**Why It Works:** The answer is in years because the rate is annual. If the household wants months, it divides the annual rate by 12 and uses a monthly rate instead.

### Growth Milestone Tracking

**Scenario:** An analyst tracks how long a portfolio needs to reach each of several milestone values at a fixed growth rate.

```excel
=PDURATION(GrowthRate, PortfolioValue, MilestoneValue)
```

**Why It Works:** Changing only the milestone value shows the time to each target, which makes it easy to compare milestones at the same growth assumption.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The rate, present value or future value is zero or negative. | Enter positive values for all three arguments. |
| `#VALUE!` | An argument has an invalid data type, such as text. | Enter numbers, or convert text values with `VALUE`. |
| Answer in the wrong unit | The annual rate was used when the user expected months. | Divide the annual rate by 12 and read the answer as months. |
| Answer looks too long | The present value and future value were entered in the wrong order. | Put the current amount in `pv` and the target in `fv`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Arguments are named `rate`, `pv` and `fv`, and all three must be positive. |
| Google Sheets | Available | Arguments are named `rate`, `present_value` and `future_value`, and all three must be greater than 0. |

## Tips and Best Practices

- Keep the rate and the answer in the same period unit, and convert the rate first when you need months.
- Enter the current amount in `pv` and the target in `fv`, because reversing them gives a negative growth result.
- Use RRI to check the rate implied by the same amounts and periods.
- Read a fractional answer as a partial period, not a rounded whole period.

## Related Functions

| Function | Relationship |
| --- | --- |
| [RRI](RRI.md) | Returns the rate needed to reach a target value over a number of periods. |
| [FV](FV.md) | Returns the future value of an investment after a set number of periods. |
| [NPER](NPER.md) | Returns the number of periods for a loan or investment with regular payments. |
| [PV](PV.md) | Returns the present value of a future amount. |
| [RATE](RATE.md) | Solves for the rate when regular payments are involved. |

## Official Documentation

- [Microsoft Support: PDURATION function](https://support.microsoft.com/en-us/excel/functions/pduration-function)
- [Google Docs Editors Help: PDURATION](https://support.google.com/docs/answer/9368165)
