---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Unit Conversion
use-case:
  - Legacy Bond Price Import
  - Price Quote Conversion
  - Treasury Note Quote Conversion
related:
  - DISC
  - DOLLARFR
  - DURATION
  - PRICE
  - YIELD
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/dollarde-function
  - https://support.google.com/docs/answer/3093167
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Fractional Dollar to Decimal
  - Fraction to Decimal Price
tags:
  - bonds
  - excel
  - fractional-pricing
  - sheets
---

# DOLLARDE

## Description

**DOLLARDE** converts a price written as a whole number and a fraction into a plain decimal. Bond and Treasury markets have long quoted prices in fractions of a dollar. A price of 102-16 means 102 and 16/32, and a spreadsheet cannot calculate with that form directly. DOLLARDE turns the quote into a decimal such as 102.5 so that it can be used in [PRICE](PRICE.md), [YIELD](YIELD.md), [DISC](DISC.md) or any other formula.

The function reads the digits after the decimal point as the numerator and the `fraction` argument as the denominator. In `1.02` with a fraction of 16, the digits `02` stand for 2 sixteenths, so the result is 1.125. A fraction of 8 gives eighths, a fraction of 32 gives thirty-seconds, and so on. The numerator is taken exactly as it is written, so a value such as `99.24` with a fraction of 32 means 99 and 24/32.

DOLLARDE is the reverse of [DOLLARFR](DOLLARFR.md), which converts a decimal price back into the fractional notation. Use DOLLARDE when a quote arrives in fractional form and you need to calculate with it, and use DOLLARFR when a decimal result must be displayed in the market's fractional style.

Google Sheets provides DOLLARDE with the same two arguments, named `fractional_price` and `unit`. Its help page gives no error behavior, so confirm the results of unusual inputs in Sheets.

## Syntax

```excel
=DOLLARDE(fractional_dollar, fraction)
```

<!-- Image 1: Fractional Quote Reading Guide. See Images/Financial/DOLLARDE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `fractional_dollar` | Yes | A number with an integer part and a fraction part separated by a decimal point. The digits after the point are the numerator. |
| `fraction` | Yes | The whole number used as the denominator, such as 8 for eighths or 32 for thirty-seconds. If it is not an integer, it is truncated. |

### Return Value

A decimal number equal to the integer part plus the numerator divided by the fraction. The function returns `#NUM!` when `fraction` is below 0 and `#DIV/0!` when `fraction` is 0 or is at least 0 and below 1 after truncation.

## Examples

### Example 1: Thirty-Seconds Quote

```excel
=DOLLARDE(99.24, 32)
```

**Result:** `99.75`

The fraction part `24` is 24 thirty-seconds, which equals 0.75.

### Example 2: Eighths Quote

```excel
=DOLLARDE(99.04, 8)
```

**Result:** `99.5`

The fraction part `04` is 4 eighths, which equals 0.5.

### Example 3: Quote Ending in a Zero

```excel
=DOLLARDE(102.16, 32)
```

**Result:** `102.5`

The digits `16` are 16 thirty-seconds, or exactly one half. This is a common quote for a note priced at par plus half a point.

### Example 4: Converting a Cell Reference

```excel
=DOLLARDE(A2, B2)
```

With `A2` holding `99.24` and `B2` holding `32`, the result is `99.75`.

**Result:** `99.75`

Keeping the quote and the denominator in separate cells lets one formula handle quotes in different denominators.

<!-- Image 2: Eighths and Thirty-Seconds Quote Comparison. See Images/Financial/DOLLARDE.md -->

## Story Problems

### Problem 1: Treasury Note Price in Decimal

A dealer posts a Treasury note at 102-16 in thirty-seconds. The analyst's model needs the decimal price to calculate yield.

| Input | Value |
| --- | --- |
| Quoted price | 102.16 |
| Fraction denominator | 32 |

**Task:** Put the quoted price in `B2` and the denominator in `B3`, then convert the quote to a decimal price.

**Solution:**

```excel
=DOLLARDE(B2, B3)
```

**Answer:** `102.5`. The 16 thirty-seconds equal one half, so the note is priced at 102.50.

### Problem 2: Averaging Two Quotes in Different Denominators

A trader receives two quotes: 98.04 in eighths and 99.28 in thirty-seconds. The sheet needs both as decimals before their average is calculated.

| Quote | Fractional Price | Denominator |
| --- | --- | --- |
| Bond A | 98.04 | 8 |
| Bond B | 99.28 | 32 |

**Task:** Convert each quote with the denominator beside it, then average the two decimal prices in one formula.

**Solution:**

```excel
=AVERAGE(DOLLARDE(B2, C2), DOLLARDE(B3, C3))
```

**Answer:** `99.1875`. Bond A is 98 and 4/8, which is 98.5, and Bond B is 99 and 28/32, which is 99.875. The average of 98.5 and 99.875 is 99.1875.

## Use Cases

### Price Quote Conversion

**Scenario:** A fixed-income desk receives quotes in fractional form from a broker and needs decimals for its risk model.

```excel
=DOLLARDE(Quote, Denominator)
```

**Why It Works:** Storing the quote and the denominator separately makes it clear which market convention each price uses.

### Treasury Note Quote Conversion

**Scenario:** A treasury analyst reads a daily sheet of note prices quoted in thirty-seconds.

```excel
=DOLLARDE(B2, 32)
```

**Why It Works:** The denominator is fixed for the market, so the formula can be copied down the whole column.

### Legacy Bond Price Import

**Scenario:** An analyst imports a file of older bond prices from a system that stored them as text.

```excel
=DOLLARDE(VALUE(A2), 8)
```

**Why It Works:** VALUE converts the text into a number before the conversion. Without it, the function receives text and may return an error.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | The `fraction` argument is 0, or it is between 0 and 1 and truncates to 0. | Enter a whole-number denominator such as 8, 16 or 32. |
| `#NUM!` | The `fraction` argument is below 0. | Enter a positive denominator. |
| Result is much too large | The quote was typed as a decimal such as 99.75 instead of the fractional notation 99.24. | Enter the quote in the market's fractional form, with the digits after the point as the numerator. |
| Text is returned as an error | The price is stored as text. | Convert the cell with VALUE or enter it as a number. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions listed on the Microsoft page | The Microsoft page gives the error rules for `#NUM!` and `#DIV/0!`. |
| Google Sheets | Available | The arguments are named `fractional_price` and `unit`. The help page gives sample usages but no error behavior. |

## Tips and Best Practices

- Keep the denominator in its own cell so that the same formula works for eighths, sixteenths and thirty-seconds.
- Enter the quote as text only when you must preserve its exact appearance, then convert it with VALUE before calculating.
- Check the result with a simple sum, such as 99 plus 24/32, to confirm the conversion before using it in a model.
- Use [DOLLARFR](DOLLARFR.md) to display a decimal result in market notation again.
- Round the converted price to the tick size of the market, since some markets accept only specific fractions.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DOLLARFR](DOLLARFR.md) | Converts a decimal price back into fractional notation. |
| [DISC](DISC.md) | Returns the discount rate of a security from its decimal price. |
| [PRICE](PRICE.md) | Returns the price of a security that pays periodic interest, using decimal inputs. |
| [YIELD](YIELD.md) | Returns the yield of a security from its decimal price. |
| [DURATION](DURATION.md) | Returns the Macaulay duration of a security. |

## Official Documentation

- [Microsoft Support: DOLLARDE function](https://support.microsoft.com/en-us/excel/functions/dollarde-function)
- [Google Docs Editors Help: DOLLARDE](https://support.google.com/docs/answer/3093167)
