---
domain: Spreadsheet Functions
category: Financial
subcategory: Interest Rate Conversion
purpose:
  - Financial Modeling
  - Loan Analysis
use-case:
  - Compounding Frequency Review
  - Loan Rate Comparison
  - Savings Rate Disclosure
related:
  - EFFECT
  - FV
  - NPER
  - PMT
  - RATE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/nominal-function
  - https://support.google.com/docs/answer/3093234
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Nominal Annual Rate
  - Nominal Interest Rate
tags:
  - compounding
  - excel
  - interest-rates
  - sheets
---

# NOMINAL

## Description

**NOMINAL** converts an effective annual interest rate into the nominal annual rate that produces it when compounded a given number of times per year. The nominal rate is the stated rate before compounding, and the effective rate is what the account or loan actually earns or costs over a full year.

Lenders and banks often quote one rate but compound more or less often, so the stated rate can look different from the rate that actually applies. Use NOMINAL to restate an effective rate in the form a loan contract or a disclosure requires, or to compare offers that compound at different frequencies.

NOMINAL is the reverse of EFFECT, which converts a nominal rate into an effective annual rate. Enter both rates as decimals, such as 0.0812 for 8.12%.

## Syntax

```excel
=NOMINAL(effect_rate, npery)
```

<!-- Image 1: Effective Rate and Compounding Periods. See Images/Financial/NOMINAL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `effect_rate` | Yes | The effective annual interest rate. Must be greater than 0. |
| `npery` | Yes | The number of compounding periods per year, such as 12 for monthly. Truncated to a whole number and must be at least 1. |

### Return Value

The nominal annual rate as a decimal. The function returns `#VALUE!` when either argument is not a number, and `#NUM!` when `effect_rate` is 0 or less or `npery` is less than 1.

## Examples

### Example 1: Monthly Compounding

```excel
=NOMINAL(0.0812, 12)
```

**Result:** `7.83%`

An effective rate of 8.12% that compounds monthly is stated as a nominal rate of 7.83%.

### Example 2: Quarterly Compounding

```excel
=NOMINAL(0.0812, 4)
```

**Result:** `7.88%`

The same effective rate compounded quarterly needs a slightly higher nominal rate, because each period compounds less often.

### Example 3: Daily Compounding

```excel
=NOMINAL(0.0812, 365)
```

**Result:** `7.81%`

Daily compounding gives the lowest nominal rate of the three examples for the same effective rate.

### Example 4: Catching an Invalid Period Count

```excel
=IFERROR(NOMINAL(0.0812, 0), "Periods must be at least 1")
```

**Result:** `Periods must be at least 1`

A period count of 0 returns `#NUM!`, so `IFERROR` replaces the error with a message.

<!-- Image 2: Nominal Rate by Compounding Frequency. See Images/Financial/NOMINAL.md -->

## Story Problems

### Problem 1: Savings Account Disclosure

A bank advertises an effective annual yield of 8.12% on a savings account that compounds monthly. The disclosure form needs the stated nominal rate.

| Item | Value |
| --- | --- |
| Effective annual rate | 8.12% |
| Compounding periods per year | 12 |

**Task:** Calculate the nominal annual rate.

**Solution:**

```excel
=NOMINAL(B2, B3)
```

**Answer:** `7.83%`. Monthly compounding at 7.83% a year produces the 8.12% effective yield.

### Problem 2: Comparing Two Loan Offers

Two lenders quote an effective annual rate of 8.12%. Offer A compounds monthly, and Offer B compounds quarterly.

| Offer | Effective Rate | Periods per Year |
| --- | --- | --- |
| Offer A | 8.12% | 12 |
| Offer B | 8.12% | 4 |

**Task:** Calculate the nominal rate for each offer and state which one has the lower stated rate.

**Solution:**

```excel
=NOMINAL(B2, C2)
```

Fill the formula down one row to calculate Offer B.

**Answer:** Offer A states `7.83%` and Offer B states `7.88%`. Offer A has the lower stated rate for the same effective cost.

<!-- Image 3: Offer Comparison Results. See Images/Financial/NOMINAL.md -->

## Use Cases

### Savings Rate Disclosure

**Scenario:** A credit union must show the nominal rate on its product sheet, while its marketing shows the effective annual yield.

```excel
=NOMINAL(EffectiveYield, CompoundingPeriods)
```

**Why It Works:** The formula produces the nominal figure directly from the advertised yield and the compounding schedule, so the two numbers always agree.

### Loan Rate Comparison

**Scenario:** A borrower compares loan offers quoted with different compounding schedules.

```excel
=NOMINAL(OfferEffectiveRate, OfferPeriods)
```

**Why It Works:** Converting every offer to a nominal rate on a common basis shows which contract states the lower rate for the same effective cost.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The effective rate is 0 or less, or the period count is less than 1. | Enter a positive rate and at least 1 period per year. |
| `#VALUE!` | An argument is text, not a number. | Convert the text to a number. |
| Rate far too high | The effective rate was entered as a whole number, such as 8.12 instead of 0.0812. | Enter the rate as a decimal or a percentage. |
| Result differs from the bank's figure | The bank's compounding frequency differs from the period count used. | Confirm the compounding schedule in the product terms. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Microsoft 365 and Excel for the web | Truncates `npery` to a whole number. Returns `#NUM!` for invalid inputs. |
| Google Sheets | Available | Uses `effective_rate` and `periods_per_year` in the same order. The page does not state the error conditions. |

## Tips and Best Practices

- Keep the effective rate as a decimal in its own cell so that the same cell can feed NOMINAL and EFFECT.
- Use the compounding frequency written in the contract, not an assumed one.
- Use EFFECT to check a result: converting the nominal rate back should return the original effective rate.
- Show both the nominal and effective rates in customer-facing documents so the difference is clear.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EFFECT](EFFECT.md) | Converts a nominal rate into the effective annual rate, the reverse of NOMINAL. |
| [RATE](RATE.md) | Finds the rate per period for a loan or annuity. |
| [PMT](PMT.md) | Level payment for a loan at a given rate and period count. |
| [NPER](NPER.md) | Number of periods needed to repay or reach a target amount. |
| [FV](FV.md) | Future value of an investment at a given rate and period count. |

## Official Documentation

- [Microsoft Support: NOMINAL function](https://support.microsoft.com/en-us/excel/functions/nominal-function)
- [Google Docs Editors Help: NOMINAL](https://support.google.com/docs/answer/3093234)
