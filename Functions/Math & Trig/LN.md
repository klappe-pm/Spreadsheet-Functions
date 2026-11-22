---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Logarithms and Powers
purpose:
  - Arithmetic Operations
  - Financial Modeling
use-case:
  - Growth Rate Modeling
  - Investment Doubling Time
related:
  - EXP
  - LOG
  - LOG10
  - POWER
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/ln-function
  - https://support.google.com/docs/answer/3093422
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Natural Logarithm
tags:
  - excel
  - growth-rate
  - logarithm
  - sheets
---

# LN

## Description

**LN** returns the natural logarithm of a positive number: the power to which the constant e (about 2.71828) must be raised to produce that number. For example, LN(10) returns about 2.302585, and LN(EXP(1)) returns 1. LN is the inverse of EXP, so LN(EXP(x)) returns x.

Use LN for continuous growth and decay, and for finding how long a balance takes to double at a steady rate. The number of periods needed to double at a rate r per period is LN(2)/LN(1+r). At 5 percent per year, that is about 14.2 years.

The number argument must be positive. The official pages do not describe the result or error for zero or negative input, so validate those values before the call. To take a logarithm in another base, use LOG with a base argument. For base 10, use LOG10.

## Syntax

```excel
=LN(number)
```

<!-- Image 1: The Natural Logarithm Curve. See Images/Math & Trig/LN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A positive real number whose natural logarithm you want. In Sheets, this argument is named `value`. |

### Return Value

A number: the natural logarithm of `number`, based on the constant e. Positive values above 1 give positive results, and values between 0 and 1 give negative results.

## Examples

### Example 1: Natural Log of 10

```excel
=LN(10)
```

**Result:** `2.302585`

Displayed to six decimal places. The value is the power to which e must be raised to reach 10.

### Example 2: Inverse With EXP

```excel
=LN(EXP(1))
```

**Result:** `1`

The natural logarithm of e is 1, because e is the base of the logarithm.

### Example 3: Natural Log of 100

```excel
=LN(100)
```

**Result:** `4.605170`

Displayed to six decimal places. Doubling the input adds LN(2), about 0.693147, to the result.

<!-- Image 2: Doubling Time at a Steady Rate. See Images/Math & Trig/LN.md -->

### Example 4: Doubling Time at 5 Percent

With the annual rate of 0.05 in `B2`:

```excel
=LN(2)/LN(1+B2)
```

**Result:** `14.2067`

Displayed to four decimal places. A balance growing 5 percent a year takes about 14.2 years to double.

## Story Problems

### Problem 1: Doubling Time for Two Savings Accounts

A household compares two savings accounts with steady annual rates. The rates are in `B2:B3`.

| Account | Annual Rate |
| --- | --- |
| Savings A | 0.05 |
| Savings B | 0.08 |

**Task:** Calculate the number of years each balance takes to double, rounded to two decimal places.

**Solution:**

```excel
=ROUND(LN(2)/LN(1+B2),2)
```

Fill the formula down to row 3.

**Answer:** `14.21` years for Savings A and `9.01` years for Savings B. The unrounded values are 14.2067 and 9.0065.

### Problem 2: Continuous Growth Rate of Website Traffic

A website had 1,200 visits in year 0 and 4,800 visits in year 4. The team wants the continuous annual growth rate, which is LN of the ratio divided by the number of years.

| Year | Visits |
| --- | --- |
| Year 0 | 1200 |
| Year 4 | 4800 |

**Task:** Calculate the continuous annual growth rate in decimal form, rounded to four decimal places. The four years between the two readings are entered in `C2`.

**Solution:**

```excel
=ROUND(LN(B3/B2)/C2,4)
```

**Answer:** `0.3466`, which is about 34.66 percent a year in continuous terms. The calculation is LN(4) divided by 4.

## Use Cases

### Investment Doubling Time

**Scenario:** A planner estimates how many years a fund takes to double at a steady annual return before choosing a product.

```excel
=LN(2)/LN(1+B2)
```

**Why It Works:** The formula uses LN to solve for the exponent in the growth equation. The result assumes the rate stays steady, which real returns rarely do, so treat it as an estimate.

### Growth Rate Modeling

**Scenario:** An analyst compares a starting value and an ending value to find the continuous growth rate over a set number of years.

```excel
=LN(C2/B2)/D2
```

**Why It Works:** LN of the ratio gives the total growth on a log scale, and dividing by the number of years gives the average rate per year. Both values must be positive.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error or wrong result | The number is zero or negative, which is outside the documented input. | Check the source value with IF before calling LN. |
| `#VALUE!` | An argument is text rather than a number. | Convert the value to a number or correct the cell reference. |
| Unexpected result | A base-10 logarithm was intended, but LN returns the natural logarithm. | Use LOG10 for base 10, or LOG with a base argument for any other base. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Requires a positive number. The page does not describe the result for zero or negative input. |
| Google Sheets | Available | The same natural logarithm. The argument is named `value` and must be positive. |

## Tips and Best Practices

- Use LN for continuous growth and decay, and LOG for any other base.
- Keep the rate and the number of periods in labeled cells so that the doubling formula is easy to audit.
- Test the result with a known value, such as LN(EXP(1)), when a model is first built.
- Remember that a doubling time from a steady rate is an estimate, not a forecast.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EXP](EXP.md) | Raises e to a power, the inverse of LN. |
| [LOG](LOG.md) | Takes a logarithm in any base, with base 10 as the default. |
| [LOG10](LOG10.md) | Takes a base-10 logarithm, a shortcut when the base is 10. |
| [POWER](POWER.md) | Raises a number to a power, the reverse of a logarithm. |

## Official Documentation

- [Microsoft Support: LN function](https://support.microsoft.com/en-us/excel/functions/ln-function)
- [Google Docs Editors Help: LN](https://support.google.com/docs/answer/3093422)
