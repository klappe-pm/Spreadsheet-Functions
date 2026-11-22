---
domain: Spreadsheet Functions
category: Financial
subcategory: Investment Returns
purpose:
  - Financial Modeling
  - Investment Analysis
use-case:
  - Certificate Ladder Growth
  - Savings Rate Changes
  - Variable Rate Investments
related:
  - EFFECT
  - FV
  - NOMINAL
  - PV
  - RATE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/fvschedule-function
  - https://support.google.com/docs/answer/3093226
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Compound Schedule Future Value
  - Variable Rate Future Value
tags:
  - compound-interest
  - excel
  - future-value
  - sheets
---

# FVSCHEDULE

## Description

**FVSCHEDULE** returns the future value of a starting amount after it compounds through a list of interest rates, one rate per period. Use it when the rate changes from period to period, such as a savings account whose bank adjusts the rate each year. The starting amount is the principal, and the rate list is the schedule, applied in order from the first rate to the last.

When the rate stays the same for every period, the FV function is simpler because it takes one rate and one number of periods. FVSCHEDULE covers the case where those rates differ. A blank cell in the schedule counts as a 0% rate for that period, so the balance carries forward unchanged for that period.

Enter rates as decimals or percentages, never as whole numbers. A rate of 9 means 900% in Excel and is invalid in Google Sheets, so type 9% or 0.09.

## Syntax

```excel
=FVSCHEDULE(principal, schedule)
```

<!-- Image 1: Principal and Rate Schedule Layout. See Images/Financial/FVSCHEDULE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `principal` | Yes | The starting amount, a number or a cell reference. |
| `schedule` | Yes | A range or array of interest rates, applied in order. Each value is one period's rate. Blank cells count as 0%. |

### Return Value

A single number: the principal after compounding through every rate in the schedule. The function returns `#VALUE!` when the schedule contains text or another non-numeric value.

## Examples

### Example 1: Basic Usage

```excel
=FVSCHEDULE(5000, {0.04,0.05,0.06})
```

**Result:** `5787.60`

The 5,000 grows by 4% in the first period, then 5% in the second, then 6% in the third: 5000 x 1.04 x 1.05 x 1.06.

### Example 2: Blank Period Counts as 0%

Principal in `E2` is `5000`, and the rates in `B2:B4` are `4%`, blank, and `6%`.

```excel
=FVSCHEDULE(E2, B2:B4)
```

**Result:** `5512.00`

The blank middle period adds no interest, so the balance moves only at 4% and then at 6%.

<!-- Image 2: Balance Growth Across the Rate Schedule. See Images/Financial/FVSCHEDULE.md -->

### Example 3: Interest Earned Only

```excel
=FVSCHEDULE(5000, {0.04,0.05,0.06}) - 5000
```

**Result:** `787.60`

Subtracting the starting amount shows the interest earned over the three periods.

## Story Problems

### Problem 1: Certificate Ladder Growth

A family deposits 12,000 in a four-year certificate ladder. The bank posts a different annual rate each year, listed in `A1:B5`.

| Year | Rate |
| --- | --- |
| 2024 | 3.0% |
| 2025 | 3.5% |
| 2026 | 4.0% |
| 2027 | 4.5% |

**Task:** Put `12000` in `E2`, then calculate the balance at the end of 2027.

**Solution:**

```excel
=FVSCHEDULE(E2, B2:B5)
```

**Answer:** `13903.00`, because 12000 x 1.03 x 1.035 x 1.04 x 1.045 = 13903.00.

### Problem 2: A Paused Interest Year

The same certificate pays nothing in 2026 because the bank suspended interest that year. The 2026 cell in `B4` is left blank.

| Year | Rate |
| --- | --- |
| 2024 | 3.0% |
| 2025 | 3.5% |
| 2026 | (blank) |
| 2027 | 4.5% |

**Task:** Keep the principal in `E2` at 12,000 and calculate the balance at the end of 2027.

**Solution:**

```excel
=FVSCHEDULE(E2, B2:B5)
```

**Answer:** `13432.85`, because 12000 x 1.03 x 1.035 x 1 x 1.045 = 13432.85. The blank year adds no interest.

<!-- Image 3: Results for the Certificate Ladder. See Images/Financial/FVSCHEDULE.md -->

## Use Cases

### Savings Rate Changes

**Scenario:** A savings account earns a rate that the bank resets each year. A planner needs the balance after five years of changing rates.

```excel
=FVSCHEDULE(Deposit, RateSchedule)
```

**Why It Works:** The named range `Deposit` holds the starting balance and `RateSchedule` holds one rate per year. Updating a rate in the schedule recalculates the balance without changing the formula.

### Monthly Rate Schedule

**Scenario:** A treasury team holds a cash balance whose rate changes each month. The rates are listed in a column for the whole year.

```excel
=FVSCHEDULE(CashBalance, MonthlyRates)
```

**Why It Works:** Each row of `MonthlyRates` is one month's rate, so the schedule matches the period length of the balance. If the bank quotes an annual rate, divide it by 12 before entering it as a monthly rate.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The schedule contains text, such as `N/A` or a label. | Replace the text with a rate or clear the cell so it counts as 0%. |
| Very large result | A rate was typed as a whole number, such as `5` instead of `5%`. | Enter the rate as `5%` or `0.05`. |
| Balance does not grow | A blank cell in the schedule counts as 0%. | Enter the rate for every period, or enter `0%` where no interest is paid. |
| Unexpected result | The rates are in the wrong order. | List the rates in period order, first period at the top. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, Excel 2019, Excel 2021, Excel 2024, Microsoft 365, Excel for the web and Excel for iPhone | Blank schedule cells count as 0%. Other non-numeric values return `#VALUE!`. |
| Google Sheets | Available | The schedule must be a range or array. Rates must be decimals or entered with `UNARY_PERCENT`, so `9` is not a valid rate. |

## Tips and Best Practices

- Use FV instead when one rate applies to every period, because it is simpler to audit.
- Keep one rate per period and match the period length of the rate to the period length of the principal.
- Format the rate cells as percentages so the schedule reads correctly while the values stay decimals.
- Put the principal in its own labeled cell so it can be changed without editing the formula.
- Use a blank cell only when no interest applies, and say so in a note beside the schedule.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FV](FV.md) | Future value when one rate applies to every period. |
| [PV](PV.md) | Present value of a single amount or a level payment stream. |
| [RATE](RATE.md) | Solves for the constant rate that produces a given future value. |
| [NOMINAL](NOMINAL.md) | Converts an effective annual rate into a nominal rate for a compounding frequency. |
| [EFFECT](EFFECT.md) | Converts a nominal rate into the effective annual rate. |

## Official Documentation

- [Microsoft Support: FVSCHEDULE function](https://support.microsoft.com/en-us/excel/functions/fvschedule-function)
- [Google Docs Editors Help: FVSCHEDULE](https://support.google.com/docs/answer/3093226)
