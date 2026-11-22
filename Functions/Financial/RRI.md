---
domain: Spreadsheet Functions
category: Financial
subcategory: Investment Returns
purpose:
  - Financial Modeling
  - Investment Analysis
use-case:
  - Annual Growth Comparison
  - Price Growth Rate
  - Savings Growth Rate
related:
  - FV
  - IRR
  - NPER
  - PV
  - RATE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/rri-function
  - https://support.google.com/docs/answer/9368238
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Compound Growth Rate
  - Equivalent Interest Rate
tags:
  - compound-growth
  - excel
  - growth-rate
  - sheets
---

# RRI

## Description

**RRI** returns the equivalent interest rate that grows a present value to a future value over a number of periods. It is a compound growth rate: the constant rate that would turn the starting amount into the ending amount if the growth compounded once per period. Use it to answer questions such as "what annual growth rate took revenue from one level to another?" or "what rate did this investment earn each year?"

RRI and RATE answer related questions. RRI works only with a starting value, an ending value and a number of periods, so it suits growth that has no regular payments. When payments are part of the picture, use RATE instead.

All three arguments must be positive for a meaningful result. Google Sheets documents that a future value of 0 returns -1, which is a loss of 100%. Microsoft Excel lists `#NUM!` for invalid argument values.

The result is a rate per period. If the periods are years, the result is an annual rate. If the periods are months, convert the result to an annual rate with the appropriate formula.

## Syntax

```excel
=RRI(nper, pv, fv)
```

<!-- Image 1: Syntax Anatomy. See Images/Financial/RRI.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `nper` | Yes | The number of periods between the present value and the future value. Must be greater than 0. |
| `pv` | Yes | The starting value of the investment or quantity. Must be greater than 0. |
| `fv` | Yes | The ending value after the periods. Enter a positive value. A value of 0 returns -1 in Google Sheets. |

### Return Value

A decimal rate per period. A rate of 0.0696 is 6.96% per period. The result is negative when the future value is smaller than the present value, which shows a decline.

## Examples

### Example 1: Annual Growth of a Balance

```excel
=RRI(5, 10000, 14000)
```

**Result:** `6.96%`

A balance grows from 10,000 to 14,000 over five years. The equivalent rate is (1.4 raised to the power of 1/5) minus 1, which is about 6.96% a year.

### Example 2: Annual Price Increase

```excel
=RRI(4, 1200, 1500)
```

**Result:** `5.74%`

A price rises from 1,200 to 1,500 over four years. The function returns the steady yearly increase that produces the same end price.

### Example 3: No Change Over the Period

```excel
=RRI(10, 250, 250)
```

**Result:** `0.00%`

When the ending value equals the starting value, the growth rate is 0 in every period, no matter how many periods pass.

### Example 4: Matching RATE Output

```excel
=RATE(5, 0, -10000, 14000)
```

**Result:** `6.96%`

With no periodic payments, RATE solves the same problem as RRI. The two results match because the present value and future value have opposite signs in the RATE call, which is how RATE expresses growth from the same starting point.

## Story Problems

### Problem 1: Savings Account Growth

A saver deposits 10,000 and expects the account to hold 14,000 after five years with no further deposits. The saver wants the average annual growth rate.

| Item | Value |
| --- | --- |
| Starting balance | 10,000 |
| Ending balance | 14,000 |
| Years | 5 |

**Task:** Find the equivalent annual rate of growth.

**Solution:**

```excel
=RRI(5, 10000, 14000)
```

**Answer:** `6.96%`. The account grows about 6.96% a year, compounded, to reach 14,000.

<!-- Image 2: Story Problem Result Panel. See Images/Financial/RRI.md -->

### Problem 2: Growth in a Service Fee

A consulting firm charged 1,200 for a monthly report in its first year. Four years later the same report costs 1,500. The finance team wants the annual rate of increase in the fee.

| Item | Value |
| --- | --- |
| First year fee | 1,200 |
| Current fee | 1,500 |
| Years | 4 |

**Task:** Find the compound annual rate of increase.

**Solution:**

```excel
=RRI(4, 1200, 1500)
```

**Answer:** `5.74%`. The fee rises about 5.74% a year on average.

## Use Cases

### Savings Growth Rate

**Scenario:** A family wants to know the return their savings account delivered between two statements.

```excel
=RRI(5, 10000, 14000)
```

**Why It Works:** The function uses only the opening balance, the closing balance and the period count. Because it ignores deposits, use it only when no money was added or withdrawn during the period.

### Price Growth Rate

**Scenario:** A purchasing manager reviews a supplier's price history and wants the average yearly increase.

```excel
=RRI(4, 1200, 1500)
```

**Why It Works:** The same formula works for any two values and a period count. Build a column of yearly rates by pointing each row at the first and last values in its series.

### Annual Growth Comparison

**Scenario:** An analyst compares revenue growth across three product lines that started at different levels.

```excel
=RRI(B2, C2, D2)
```

**Why It Works:** Each row uses the same formula with its own starting value, ending value and period count. The results are directly comparable because every rate is expressed per year.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | An argument is zero, negative or otherwise invalid. | Check that nper, pv and fv are positive values. |
| `#VALUE!` | An argument is text rather than a number. | Convert the cell to a number or remove the text. |
| `-1` or -100% | The future value is 0. | Confirm that the ending value is correct. A balance that reaches 0 implies a total loss. |
| Result looks too small | The periods are in months, but the rate is read as annual. | Convert the monthly rate to an annual rate before you report it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel versions, including Microsoft 365 and Excel for the web | Arguments are named nper, pv and fv. Returns `#NUM!` for an invalid argument value and `#VALUE!` for an invalid data type. |
| Google Sheets | Available | Arguments are named number_of_periods, present_value and future_value. All values must be positive, and a future value of 0 returns -1. |

## Tips and Best Practices

- Use RRI for growth between two values. Use RATE when regular payments also affect the result.
- Keep the period unit consistent. Yearly values with a yearly count give an annual rate.
- Check the result by growing the present value with the rate: pv times (1 + rate) raised to nper should equal fv.
- Avoid RRI when deposits or withdrawals occurred between the two values, because the rate would mix growth with cash flows.
- Label the result as a compound annual growth rate when you present it, so readers know it is an average.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FV](FV.md) | Grows a present value at a known rate to a future value. |
| [IRR](IRR.md) | Finds the rate from a series of uneven cash flows. |
| [NPER](NPER.md) | Finds the number of periods needed to reach a target value at a given rate. |
| [PV](PV.md) | Discounts a future value back to today at a known rate. |
| [RATE](RATE.md) | Finds the rate when regular payments are part of the calculation. |

## Official Documentation

- [Microsoft Support: RRI function](https://support.microsoft.com/en-us/excel/functions/rri-function)
- [Google Docs Editors Help: RRI](https://support.google.com/docs/answer/9368238)
