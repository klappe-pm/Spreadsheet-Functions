---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Logarithms and Powers
purpose:
  - Aggregation
  - Special Functions
use-case:
  - Polynomial Cost Curves
  - Shipping Surcharge Tables
related:
  - EXP
  - FACT
  - MMULT
  - POWER
  - SUMPRODUCT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/seriessum-function
  - https://support.google.com/docs/answer/3093444
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Power Series Sum
tags:
  - excel
  - polynomial
  - power-series
  - sheets
---

# SERIESSUM

## Description

**SERIESSUM** returns the sum of a power series. You supply an input value x, a starting power n, a step m that increases the power for each term, and a list of coefficients. Each coefficient multiplies one power of x, and the function adds the results together.

The formula is a1 * x^n + a2 * x^(n+m) + ... + ai * x^(n+(i-1)m), where i is the number of coefficients. With n = 0 and m = 1, SERIESSUM evaluates an ordinary polynomial, which is the most common business use. With m = 2, it evaluates only even powers, which is how many series approximations are written.

Use SERIESSUM when a model is written as a list of coefficients, such as a cost curve with fixed, linear, and squared terms. For a single power of a number, use POWER instead. For a series built from factorials, combine SERIESSUM with FACT.

The coefficients can be typed as an array constant such as {1,3,5}, or referenced as a range or column. The number of coefficients sets the number of terms.

## Syntax

```excel
=SERIESSUM(x, n, m, coefficients)
```

<!-- Image 1: Series Term Layout. See Images/Math & Trig/SERIESSUM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The input value to the power series. It may be a cell reference or a number. |
| `n` | Yes | The starting power to which x is raised for the first term. |
| `m` | Yes | The amount added to the power for each successive term. Use 1 for a polynomial and 2 for even powers only. |
| `coefficients` | Yes | An array or range of values that multiply each power of x. The number of values sets the number of terms. |

### Return Value

Returns a single number equal to the sum of the coefficient terms. Returns #VALUE! when any argument is not numeric. All arguments are required, so omitting one returns an argument error.

## Examples

### Example 1: Evaluating a Quadratic

```excel
=SERIESSUM(2, 0, 1, {1, 3, 5})
```

**Result:** 27

The terms are 1 times 2 to the power 0, plus 3 times 2 to the power 1, plus 5 times 2 to the power 2. That gives 1 + 6 + 20 = 27.

### Example 2: Starting Above Zero

```excel
=SERIESSUM(2, 1, 1, {4, 5})
```

**Result:** 28

The first term uses the power 1, and the second term uses the power 2. That gives 4 times 2 plus 5 times 4, which equals 28.

<!-- Image 2: Even Powers in a Series. See Images/Math & Trig/SERIESSUM.md -->

### Example 3: Even Powers Only

```excel
=SERIESSUM(0.5, 0, 2, {1, -0.5, 0.0416667})
```

**Result:** 0.8776

With m = 2, the powers are 0, 2, and 4. The result approximates the cosine of 0.5 radians, which is 0.8776, using the first three terms of its power series.

### Example 4: Coefficients From a Range

```excel
=SERIESSUM(A2, 0, 1, B2:B4)
```

**Result:** The polynomial value for the x value in A2, using the coefficients in B2 to B4

Placing the coefficients in cells lets an analyst change the curve without rewriting the formula.

### Example 5: Equal Coefficients

```excel
=SERIESSUM(3, 0, 1, {1, 1, 1})
```

**Result:** 13

The terms are 1, 3, and 9, which add to 13. Equal coefficients produce the sum of successive powers of x.

## Story Problems

### Problem 1: Shipping Surcharge by Distance

A courier charges a surcharge that depends on the distance, x, in kilometers. The surcharge is written as a polynomial: a fixed fee of 12, plus 1.5 for each kilometer, plus 0.04 for each squared kilometer.

| Coefficient | Value |
| --- | --- |
| Fixed fee | 12 |
| Per kilometer | 1.5 |
| Per squared kilometer | 0.04 |

**Task:** Find the surcharge for a 100 kilometer delivery.

**Solution:**

```excel
=SERIESSUM(100, 0, 1, {12; 1.5; 0.04})
```

**Answer:** `562`, from 12 + 1.5 times 100 + 0.04 times 10,000. The squared term adds the most, which is why long routes cost more per kilometer.

### Problem 2: Surcharge for a Shorter Route

The same courier uses the same coefficients for a shorter route. The coefficients are placed in cells B2 to B4, and the distance is in cell A2.

| Cell | Value |
| --- | --- |
| A2 (distance in km) | 40 |
| B2 (fixed fee) | 12 |
| B3 (per kilometer) | 1.5 |
| B4 (per squared kilometer) | 0.04 |

**Task:** Find the surcharge for the 40 kilometer route using the cell references.

**Solution:**

```excel
=SERIESSUM(A2, 0, 1, B2:B4)
```

**Answer:** `136`, from 12 + 1.5 times 40 + 0.04 times 1,600.

## Use Cases

### Polynomial Cost Curves

**Scenario:** A manufacturer models the cost of a production run as a fixed setup cost plus a linear term and a squared term for overtime.

```excel
=SERIESSUM(B2, 0, 1, C2:C4)
```

**Why It Works:** B2 holds the production volume, and C2 to C4 hold the coefficients for setup, linear, and squared costs. Changing the coefficients in one place updates every row of the cost table.

### Shipping Surcharge Tables

**Scenario:** A logistics team builds a surcharge table for many distances, using one set of coefficients for every row.

```excel
=SERIESSUM(A5, 0, 1, $B$2:$B$4)
```

**Why It Works:** The coefficient range is locked with absolute references, so each row uses the same curve while the distance in column A changes. Copy the formula down the column to fill the table.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | An argument is text, not a number. | Convert the text with VALUE or correct the source cell. |
| Unexpected total | The coefficients are in the wrong order. | List the coefficients from the lowest power to the highest. |
| Missing terms | The step m does not match the intended powers. | Use m = 1 for every power, or m = 2 for even powers only. |
| Result too small or large | The input x is in the wrong units. | Convert the input to the units the coefficients expect. |
| Argument count error | A required argument was left out. | Supply all four arguments, using 0 for n when the series starts at the constant term. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019, and Excel 2016 | All four arguments are required. Non-numeric arguments return #VALUE!. |
| Google Sheets | Available | Uses the same four arguments, named x, n, m, and a. Coefficients can be an array or a range. |

## Tips and Best Practices

- Store the coefficients in a labeled column, so the curve can be audited and changed without editing formulas.
- Use the array constant form for short, fixed series and a range for longer ones.
- Check the result with a simple case, such as x = 0, where only the first coefficient remains.
- Use POWER instead when the formula has only one power of x.
- Use m = 2 for series of even powers, which is common in approximations of trigonometric functions.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EXP](EXP.md) | Calculates e raised to a power, which many power series approximate. |
| [FACT](FACT.md) | Returns factorials, which are used as coefficients in exponential and trigonometric series. |
| [MMULT](MMULT.md) | Multiplies arrays, which can be used when several series are evaluated together. |
| [POWER](POWER.md) | Raises one number to one power, the single-term version of a series. |
| [SUMPRODUCT](SUMPRODUCT.md) | Multiplies arrays term by term and adds the results, a related approach to a weighted sum. |

## Official Documentation

- [Microsoft Support: SERIESSUM function](https://support.microsoft.com/en-us/excel/functions/seriessum-function)
- [Google Docs Editors Help: SERIESSUM](https://support.google.com/docs/answer/3093444)
