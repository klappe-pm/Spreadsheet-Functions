---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
purpose:
  - Bond Analysis
  - Unit Conversion
use-case:
  - Exchange Quote Formatting
  - Fractional Bond Quote Display
  - Publishing Treasury Prices
related:
  - DISC
  - DOLLARDE
  - DURATION
  - PRICE
  - YIELD
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/dollarfr-function
  - https://support.google.com/docs/answer/3093217
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Decimal to Fractional Dollar
  - Decimal Price to Fraction
tags:
  - bonds
  - excel
  - fractional-pricing
  - sheets
---

# DOLLARFR

## Description

**DOLLARFR** converts a decimal price into the fractional notation that bond and Treasury markets use for quotes. A decimal price of 99.375 is 99 and three eighths, which the market writes as 99-12 when quoted in thirty-seconds. DOLLARFR returns that quote as a number in which the digits after the decimal point hold the numerator, so 99.375 with a fraction of 32 comes back as 99.12.

The result is a display format, not a value to calculate with. Its digits after the decimal point are the numerator, so the number 99.12 is not the same as 99.12 in decimal arithmetic. Keep the decimal price in the cell that feeds your calculations and use DOLLARFR only in a cell that shows the quote. To convert back to a decimal before calculating, use [DOLLARDE](DOLLARDE.md).

The `fraction` argument sets the denominator. A fraction of 8 gives eighths, 16 gives sixteenths and 32 gives thirty-seconds. The Microsoft page says that a non-integer `fraction` is truncated, so 32.9 is read as 32.

Google Sheets provides DOLLARFR with the same two arguments, named `decimal_price` and `unit`. Its help page explains the notation with an example of 100.125 converted in eighths, which gives 100.01, but it does not describe error behavior.

## Syntax

```excel
=DOLLARFR(decimal_dollar, fraction)
```

<!-- Image 1: Decimal to Fractional Quote Layout. See Images/Financial/DOLLARFR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `decimal_dollar` | Yes | A decimal number, such as 99.375, to be written in fractional notation. |
| `fraction` | Yes | The whole number used as the denominator, such as 8 for eighths or 32 for thirty-seconds. If it is not an integer, it is truncated. |

### Return Value

A number whose digits after the decimal point hold the numerator of the fraction. For example, 99.375 with a fraction of 32 returns 99.12, which means 99 and 12/32. The function returns `#NUM!` when `fraction` is below 0 and `#DIV/0!` when `fraction` is 0.

## Examples

### Example 1: Thirty-Seconds Quote

```excel
=DOLLARFR(99.75, 32)
```

**Result:** `99.24`

The decimal part 0.75 equals 24 thirty-seconds, so the quote is written 99-24.

### Example 2: Eighths Quote

```excel
=DOLLARFR(99.75, 8)
```

**Result:** `99.06`

The decimal part 0.75 equals 6 eighths, so the quote is written 99-06.

### Example 3: Eighths Quote From the Google Help Page

```excel
=DOLLARFR(100.125, 8)
```

**Result:** `100.01`

The decimal part 0.125 equals 1 eighth, so the quote is written 100-01.

### Example 4: Converting a Cell Reference

```excel
=DOLLARFR(A2, B2)
```

With `A2` holding `99.375` and `B2` holding `32`, the result is `99.12`.

**Result:** `99.12`

The result is a display value. Keep the decimal price in `A2` for any further calculation.

<!-- Image 2: Decimal Price and Quote Side by Side. See Images/Financial/DOLLARFR.md -->

## Story Problems

### Problem 1: Price Board for Treasury Notes

A dealer's price board shows notes in thirty-seconds. The decimal price of one note is 99.375, and the board must show it in the market format.

| Input | Value |
| --- | --- |
| Decimal price | 99.375 |
| Denominator | 32 |

**Task:** Put the decimal price in `B2` and the denominator in `B3`, then find the quote to show on the board.

**Solution:**

```excel
=DOLLARFR(B2, B3)
```

**Answer:** `99.12`, which the board shows as 99-12. The decimal part 0.375 equals 12 thirty-seconds.

### Problem 2: Quote in Eighths

A broker sends a list of prices in decimal form, and the client wants each one in eighths. One price in the list is 101.5.

| Input | Value |
| --- | --- |
| Decimal price | 101.5 |
| Denominator | 8 |

**Task:** Convert the price to eighths.

**Solution:**

```excel
=DOLLARFR(B2, B3)
```

**Answer:** `101.04`, which the client reads as 101-04. The decimal part 0.5 equals 4 eighths.

## Use Cases

### Exchange Quote Formatting

**Scenario:** A trading desk prints a daily sheet of prices in the fractional notation used on the exchange.

```excel
=DOLLARFR(DecimalPrice, Denominator)
```

**Why It Works:** The sheet calculates in decimals and formats the result in the market's style, so the calculations stay accurate while the output matches the exchange.

### Fractional Bond Quote Display

**Scenario:** A reporting analyst shows bond prices to clients who expect the old fractional style.

```excel
=DOLLARFR(Price, 32)
```

**Why It Works:** Using the decimal price as the source keeps the underlying value intact. Only the display changes.

### Publishing Treasury Prices

**Scenario:** A research team publishes a table of note prices with the quote and the decimal side by side.

```excel
=DOLLARFR(C2, 32)
```

**Why It Works:** Column C holds the decimal price, and the fractional quote in the next column is a formula that can be copied down the table.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | The `fraction` argument is 0. | Enter a whole-number denominator such as 8, 16 or 32. |
| `#NUM!` | The `fraction` argument is below 0. | Enter a positive denominator. |
| Calculation gives a wrong price | The fractional result was used in later math. | Keep the decimal price for calculations and convert back with DOLLARDE only when needed. |
| Quote does not match the market | The decimal part does not fall on a multiple of 1/denominator. | Check that the price is an exact fraction of the denominator before converting, such as 0.375 for 12/32. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions listed on the Microsoft page | The Microsoft page gives the `#NUM!` and `#DIV/0!` rules. It does not state the return type in detail. |
| Google Sheets | Available | The arguments are named `decimal_price` and `unit`. The help page gives an example in eighths but no error behavior. |

## Tips and Best Practices

- Calculate with the decimal price and use DOLLARFR only for display.
- Keep the denominator in a labeled cell so that the same formula serves each market convention.
- Compare the result with a manual conversion of the decimal part to make sure the fraction matches the market.
- Use [DOLLARDE](DOLLARDE.md) to read a fractional quote back into a decimal.
- Remember that the numerator is shown as a decimal digit, so a result such as 99.2 means 99 and 20/32 when the denominator is 32.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DOLLARDE](DOLLARDE.md) | Converts a fractional quote into a decimal price. |
| [DISC](DISC.md) | Returns the discount rate of a security from its decimal price. |
| [PRICE](PRICE.md) | Returns the price of a security that pays periodic interest. |
| [YIELD](YIELD.md) | Returns the yield of a security from its decimal price. |
| [DURATION](DURATION.md) | Returns the Macaulay duration of a security. |

## Official Documentation

- [Microsoft Support: DOLLARFR function](https://support.microsoft.com/en-us/excel/functions/dollarfr-function)
- [Google Docs Editors Help: DOLLARFR](https://support.google.com/docs/answer/3093217)
