---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Logarithms and Powers
purpose:
  - Arithmetic Operations
use-case:
  - Digit Count Estimates
  - Order of Magnitude Checks
  - Water Quality Testing
related:
  - EXP
  - LN
  - LOG
  - POWER
  - ROUND
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/log10-function
  - https://support.google.com/docs/answer/3093423
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Base 10 Logarithm
tags:
  - excel
  - logarithm
  - scientific-scale
  - sheets
---

# LOG10

## Description

**LOG10** returns the base-10 logarithm of a positive number. The base-10 logarithm answers the question "10 raised to what power gives this number?" For example, LOG10(1000) returns 3 because 10 to the power of 3 is 1000.

Use LOG10 when values span several orders of magnitude, such as concentrations, sound levels, earthquake magnitudes, or counts that range from single digits to millions. Working on the logarithm scale turns multiplication into addition, which makes large ranges easier to compare and chart.

LOG10 is a shortcut for LOG with the base set to 10. LOG(A2, 10) and LOG10(A2) return the same value. Use LN when you need the natural logarithm (base e) instead.

## Syntax

```excel
=LOG10(number)
```

<!-- Image 1: LOG10 Syntax Anatomy. See Images/Math & Trig/LOG10.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The positive number whose base-10 logarithm you want. It can be a number, a cell reference, or a formula that returns a number. Zero, negative numbers, and text are not valid inputs. |

### Return Value

A number. LOG10 returns the power to which 10 must be raised to produce `number`. Positive values greater than 1 return positive results, values between 0 and 1 return negative results, and 1 returns 0.

## Examples

### Example 1: Power of Ten

```excel
=LOG10(1000)
```

**Result:** `3`

Because 10 x 10 x 10 = 1000, the exponent is 3.

### Example 2: Logarithm of a Cell Value

With `A2` containing `250`:

```excel
=LOG10(A2)
```

**Result:** `2.3979`

The result is rounded here for display. The exact value is about 2.39794, because 10 to the power of 2.39794 is about 250.

### Example 3: Counting Digits in a Number

With `A2` containing `250`:

```excel
=INT(LOG10(A2)) + 1
```

**Result:** `3`

INT rounds the logarithm down to a whole number, and adding 1 gives the count of digits. This works for any positive whole number.

### Example 4: Fractional Powers of Ten

```excel
=LOG10(0.001)
```

**Result:** `-3`

Numbers between 0 and 1 return negative logarithms. Here 0.001 equals 10 to the power of -3.

<!-- Image 2: Logarithmic Scale for Values from 1 to 1000. See Images/Math & Trig/LOG10.md -->

### Example 5: Guarding Against Invalid Input

With `A2` containing `250` and `A3` containing `0`:

```excel
=IF(A3 > 0, LOG10(A3), "Enter a positive value")
```

**Result:** `Enter a positive value`

The IF test prevents LOG10 from receiving zero or a negative number, which are outside its domain.

## Story Problems

### Problem 1: Acidity of Lab Water Samples

A water testing lab measures the hydrogen ion concentration of four samples in moles per liter, listed in `B2:B5`. Acidity is reported as pH, which equals the negative base-10 logarithm of the concentration.

| Sample | Hydrogen Ion Concentration |
| --- | --- |
| Spring | 0.0000001 |
| Creek | 0.00001 |
| Rain | 0.0000025 |
| Lake | 0.00000004 |

**Task:** Calculate the pH for every sample in column `C` and report the value for the rain sample.

**Solution:**

```excel
=-LOG10(B4)
```

Copy the formula down to `C2:C5`.

**Answer:** `5.6021`. The rain sample has a concentration of 2.5 x 10 to the power of -6, and its pH is about 5.60. The spring sample scores 7, the creek sample 5, and the lake sample 7.3979.

<!-- Image 3: pH Results for the Lab Samples. See Images/Math & Trig/LOG10.md -->

### Problem 2: Estimating Digits in Customer Counts

A subscription service stores customer totals in `B2:B4`: 9800, 125000, and 47. The operations team wants the number of digits in each total to size the report columns.

| Account | Customers |
| --- | --- |
| North | 9800 |
| South | 125000 |
| West | 47 |

**Task:** Put the digit count for each account in column `C`.

**Solution:**

```excel
=INT(LOG10(B2)) + 1
```

**Answer:** `4`, `6`, and `2`. The logarithm of 9800 is about 3.99, so INT gives 3 and adding 1 gives 4 digits. The same logic gives 6 digits for 125000 and 2 digits for 47.

## Use Cases

### Order of Magnitude Comparison

**Scenario:** An analyst compares product sales that range from a few units to several million, and wants to group the products by scale.

```excel
=INT(LOG10(B2))
```

**Why It Works:** The integer part of the base-10 logarithm gives the power of ten for each value, so products with the same result sit in the same scale band. Wrap the formula in IF for labels such as "Thousands" or "Millions".

### Digit Count for Column Width

**Scenario:** A reporting tool needs to know how many characters an invoice number will need.

```excel
=INT(LOG10(A2)) + 1
```

**Why It Works:** The formula counts digits without converting the number to text. It works for positive whole numbers only, so pair it with a check for zero when zero values are possible.

### Water Quality Dashboard

**Scenario:** A lab reports pH from hydrogen ion concentration for each sampling site.

```excel
=-LOG10(B2)
```

**Why It Works:** pH is defined as the negative base-10 logarithm of the hydrogen ion concentration, so the negative sign converts the logarithm into the reported scale.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` in Excel | The input is zero or negative, so no logarithm exists. | Filter out zero and negative values with IF before calling LOG10. |
| `#VALUE!` | The input is text or a cell that holds text. | Convert the value to a number or correct the source cell. |
| Unexpected result | The input is a text number such as `"250"` that looks numeric. | Use VALUE or multiply by 1 to convert it to a number. |
| Wrong scale | The data is in thousands but the formula treats it as units. | Divide or multiply by the scale factor before taking the logarithm. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016, 2019, 2021, 2024, Microsoft 365, and Excel for the web | Requires a positive number. |
| Google Sheets | Available | Requires a positive number. Sheets does not return complex results for invalid input. |

## Tips and Best Practices

- Use LOG10 when a dataset spans several powers of ten, and chart the logarithms to make the spread visible.
- Use LOG with a base argument for other bases, such as LOG(A2, 2) for base 2.
- Guard the input with IF or MAX when blank cells or zeros can appear, because LOG10 cannot process them.
- Round only for display, and keep the full value in calculations to avoid compounding rounding error.
- Remember that INT rounds down for positive numbers, so INT(LOG10(A2)) + 1 counts digits for values of 1 or more.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LN](LN.md) | Natural logarithm (base e) for continuous growth and decay models. |
| [LOG](LOG.md) | General logarithm with any base; LOG10 is the base-10 case. |
| [POWER](POWER.md) | Raises a number to a power, the inverse of the logarithm. |
| [EXP](EXP.md) | Raises e to a power, the inverse of LN. |
| [ROUND](ROUND.md) | Rounds the logarithm for display or for comparing bands. |

## Official Documentation

- [Microsoft Support: LOG10 function](https://support.microsoft.com/en-us/excel/functions/log10-function)
- [Google Docs Editors Help: LOG10](https://support.google.com/docs/answer/3093423)
