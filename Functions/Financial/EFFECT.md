---
domain: Spreadsheet Functions
category: Financial
subcategory: Interest Rate Conversion
purpose:
  - Financial Modeling
  - Investment Analysis
use-case:
  - Credit Card APR Comparison
  - Loan Quote Comparison
  - Savings Account Comparison
related:
  - FV
  - NOMINAL
  - PMT
  - PV
  - RATE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/effect-function
  - https://support.google.com/docs/answer/3093223
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Annual Effective Rate
  - Effective Annual Rate
tags:
  - compound-interest
  - excel
  - interest-rate
  - sheets
---

# EFFECT

## Description

**EFFECT** converts a nominal annual interest rate into the effective annual rate, which is the rate a borrower pays or an investor earns once compounding is included. A bank that quotes 12% a year and compounds the interest monthly actually produces about 12.68% over the year. EFFECT shows that difference, so you can compare accounts and loans that compound at different frequencies on the same basis.

The function takes two arguments: the nominal annual rate and the number of compounding periods per year. It calculates `(1 + nominal_rate / periods) ^ periods - 1`. The more often interest compounds, the higher the effective rate becomes for the same nominal rate, although the increase slows as the frequency rises. Daily compounding of a 6% nominal rate, for example, produces only about 0.015 percentage points more than monthly compounding.

EFFECT works in the other direction from [NOMINAL](NOMINAL.md), which returns the nominal rate from an effective rate. Use EFFECT when a lender or bank quotes a nominal rate and you need the true annual cost or return. Use the effective rate in [FV](FV.md) or [PV](PV.md) only when the period is a full year, or convert it back to the period rate for other periods.

Google Sheets provides EFFECT with the same two arguments, named `nominal_rate` and `periods_per_year`. Its help page gives sample formulas but no example outputs and does not describe error behavior.

## Syntax

```excel
=EFFECT(nominal_rate, npery)
```

<!-- Image 1: Nominal and Effective Rate Comparison. See Images/Financial/EFFECT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `nominal_rate` | Yes | The nominal annual interest rate, entered as a decimal such as 0.12 for 12%. Must be greater than 0. |
| `npery` | Yes | The number of compounding periods per year, such as 12 for monthly compounding. Must be at least 1. Fractional values are truncated to a whole number. |

### Return Value

A decimal number giving the effective annual rate. For example, a nominal rate of 0.12 compounded 12 times a year returns 0.126825. The function returns `#VALUE!` when either argument is not a number, and `#NUM!` when `nominal_rate` is 0 or less or when `npery` is less than 1.

## Examples

### Example 1: Monthly Compounding

```excel
=EFFECT(0.12, 12)
```

**Result:** `0.126825`

A 12% nominal rate compounded monthly earns about 12.68% over a full year.

### Example 2: Quarterly Compounding

```excel
=EFFECT(0.06, 4)
```

**Result:** `0.061364`

A 6% nominal rate compounded quarterly is worth about 6.14% a year. The extra 0.14 points come from interest earned on earlier quarters' interest.

### Example 3: Daily Compounding

```excel
=EFFECT(0.24, 365)
```

**Result:** `0.271149`

A 24% annual rate compounded daily produces an effective rate of about 27.11%. This is the figure that matters when comparing card charges.

### Example 4: Fractional Periods Are Truncated

```excel
=EFFECT(0.06, 4.9)
```

**Result:** `0.061364`

Excel truncates the 4.9 to 4 before the calculation, so the result matches Example 2.

<!-- Image 2: Compounding Frequency Comparison. See Images/Financial/EFFECT.md -->

## Story Problems

### Problem 1: Savings Account Comparison

A saver is offered a savings account paying 5% nominal interest compounded monthly. A second account pays 5.1% compounded once a year. The saver wants the effective annual rate of the first account to compare with the second.

| Input | Value |
| --- | --- |
| Nominal annual rate | 0.05 |
| Compounding periods per year | 12 |

**Task:** Put the rate in `B2` and the periods in `B3`, then find the effective annual rate of the first account.

**Solution:**

```excel
=EFFECT(B2, B3)
```

**Answer:** `0.051162`, or about 5.12%. The monthly account is slightly better than the 5.1% annual account, although the difference is small.

### Problem 2: Credit Card Annual Cost

A credit card statement shows an annual percentage rate of 24%, and the issuer compounds interest daily. The customer wants to know the true annual cost of carrying a balance.

| Input | Value |
| --- | --- |
| Nominal annual rate | 0.24 |
| Compounding periods per year | 365 |

**Task:** Find the effective annual rate using the same input cells.

**Solution:**

```excel
=EFFECT(B2, B3)
```

**Answer:** `0.271149`, or about 27.11%. Carrying a 1000 balance for a year costs about 271 in interest, compared with 240 under simple interest on the stated rate.

## Use Cases

### Savings Account Comparison

**Scenario:** A household compares several savings accounts that quote different nominal rates and compounding frequencies.

```excel
=EFFECT(NominalRate, Periods)
```

**Why It Works:** Each account's effective rate is calculated on the same basis, so the accounts can be ranked by the return the saver actually receives.

### Credit Card APR Comparison

**Scenario:** A consumer compares the true annual cost of two cards, one compounding monthly and one compounding daily.

```excel
=EFFECT(APR, 365)
```

**Why It Works:** The effective rate shows the cost of carrying a balance across the full year, which is more useful than the nominal APR for choosing between cards.

### Loan Quote Comparison

**Scenario:** A business owner compares loan quotes that show nominal rates with different compounding terms.

```excel
=EFFECT(QuoteRate, PaymentsPerYear)
```

**Why It Works:** Converting each quote to an effective rate puts the loans on the same footing before the total cost is calculated.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | One of the arguments is text. | Enter both arguments as numbers. |
| `#NUM!` | `nominal_rate` is 0 or negative. | Enter a positive nominal rate. |
| `#NUM!` | `npery` is less than 1. | Enter at least 1, such as 1 for annual compounding. |
| Result is far too small | The rate was entered as a whole number, such as 12 for 12%. | Enter the rate as a decimal, such as 0.12. |
| Result is one period off | The compounding frequency was entered as the number of years. | Use the number of compounding periods per year. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions listed on the Microsoft page | `npery` is truncated to an integer. The argument names are `Nominal_rate` and `Npery`. |
| Google Sheets | Available | The arguments are named `nominal_rate` and `periods_per_year`. The help page gives sample formulas but no outputs and does not describe error behavior. |

## Tips and Best Practices

- Convert every quote to an effective rate before comparing products with different compounding terms.
- Use 365 for daily compounding and 12 for monthly, and check the bank's disclosure for the exact term.
- Use [NOMINAL](NOMINAL.md) to reverse the calculation when a source gives only the effective rate.
- Pair EFFECT with [FV](FV.md) only for full-year periods, since a mismatched rate and period count gives a wrong future value.
- Show both the nominal and effective rates in a report so readers can see the difference.

## Related Functions

| Function | Relationship |
| --- | --- |
| [NOMINAL](NOMINAL.md) | Converts an effective rate back to the nominal annual rate. |
| [FV](FV.md) | Calculates the future value of a series of payments at a given rate. |
| [PV](PV.md) | Calculates the present value of future payments at a given rate. |
| [RATE](RATE.md) | Solves for the interest rate per period from the loan or investment terms. |
| [PMT](PMT.md) | Calculates the regular payment for a loan at a given rate. |

## Official Documentation

- [Microsoft Support: EFFECT function](https://support.microsoft.com/en-us/excel/functions/effect-function)
- [Google Docs Editors Help: EFFECT](https://support.google.com/docs/answer/3093223)
