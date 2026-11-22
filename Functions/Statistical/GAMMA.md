---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Statistical Analysis
use-case:
  - Continuous Factorial Calculation
  - Gamma Distribution Setup
related:
  - FACT
  - GAMMA.DIST
  - GAMMA.INV
  - GAMMALN
  - GAMMALN.PRECISE
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/gamma-function
  - https://support.google.com/docs/answer/9365856
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Gamma Function
tags:
  - excel
  - gamma-function
  - sheets
  - special-functions
---

# GAMMA

## Description

**GAMMA** returns the value of the gamma function at a number. For a positive whole number n, GAMMA(n + 1) equals n factorial, so GAMMA(6) returns 120, the same as FACT(5). The gamma function also accepts fractions and some negative numbers, which lets it extend the factorial idea to values that are not whole numbers.

Most people never call GAMMA directly. It appears inside statistical formulas, such as the density and inverse functions of the gamma distribution, and inside models that need a factorial for a non-integer value. Use GAMMA when you need that factorial extension in a calculation of your own. Use FACT when the number is a whole number and you only need its factorial.

The function accepts one argument. Microsoft's page states that it returns #NUM! for zero and for negative whole numbers, and Google's page states that the input must be positive. Check the platform before you rely on a negative input.

## Syntax

```excel
=GAMMA(number)
```

<!-- Image 1: Factorial Relationship. See Images/Statistical/GAMMA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value at which to evaluate the gamma function. Microsoft accepts fractions and negative numbers that are not whole numbers. Zero and negative whole numbers return `#NUM!`. |

### Return Value

A single number: the gamma function value at `number`. The function returns `#NUM!` for zero and negative whole numbers, and `#VALUE!` when the argument is not a valid number.

## Examples

### Example 1: Factorial Extension

```excel
=GAMMA(6)
```

**Result:** `120`

GAMMA(6) equals 5 factorial, which is 5 times 4 times 3 times 2 times 1. The gamma function is one more than the number that the factorial uses.

### Example 2: Fractional Input

```excel
=GAMMA(0.5)
```

**Result:** `1.772454`

This is the square root of pi, which the gamma function returns for an input of one half. The value is shown to six decimal places.

### Example 3: Negative Fraction

```excel
=GAMMA(-1.5)
```

**Result:** `2.363272`

The gamma function is defined for this negative fraction. The value is 4 times the square root of pi divided by 3.

<!-- Image 2: Gamma Curve. See Images/Statistical/GAMMA.md -->

### Example 4: Comparing With FACT

```excel
=GAMMA(7) = FACT(6)
```

**Result:** `TRUE`

Both sides equal 720. The comparison confirms the relationship between the gamma function and the factorial for whole numbers.

## Story Problems

### Problem 1: Factorial for a Fractional Count

A researcher needs a value for GAMMA(4.5) to scale a probability model. The input is not a whole number, and FACT is defined only for whole numbers.

**Task:** Return the gamma function at 4.5.

**Solution:**

```excel
=GAMMA(4.5)
```

**Answer:** `11.6317`, rounded to four decimal places.

<!-- Image 3: Story Problem Result. See Images/Statistical/GAMMA.md -->

### Problem 2: Checking a Factorial

A spreadsheet uses the factorial of 6 to compute the number of ways to arrange six items. An analyst wants to confirm that the gamma function gives the same number.

**Task:** Return the gamma function value that matches 6 factorial.

**Solution:**

```excel
=GAMMA(7)
```

**Answer:** `720`, which equals 6 factorial. The result matches FACT(6).

## Use Cases

### Continuous Factorial Calculation

**Scenario:** A model needs a factorial for a value that is not a whole number, such as a shape parameter estimated from data.

```excel
=GAMMA(Shape_Estimate + 1)
```

**Why It Works:** The gamma function gives a factorial-like value for fractional inputs, where FACT is defined only for whole numbers. Check the platform and the input sign before you use the result.

### Gamma Distribution Setup

**Scenario:** A planner sets up a gamma distribution and needs the normalizing constant that the formula uses internally.

```excel
=GAMMA(Shape)*Scale^Shape
```

**Why It Works:** The product of the gamma function and the scale power appears in the distribution's normalizing constant. Build the constant in a labeled cell so the reviewer can see each part.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NUM!` | The input is zero or a negative whole number. | Use a positive value or a noninteger input. |
| `#VALUE!` | The argument is text or another value that cannot be read as a number. | Enter a number, or convert the input with VALUE. |
| `#NAME?` | The name is misspelled. | Type GAMMA. |
| Unexpected sign | A negative input is valid in Excel but not in Google Sheets. | Use a positive input in shared workbooks. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Excel for the web | Accepts negative noninteger inputs. Returns `#NUM!` for zero and negative whole numbers. |
| Google Sheets | Available | The help page states that the input must be positive. The page's argument note describes the natural logarithm, which conflicts with its own examples, so use GAMMALN for the logarithm. |

## Tips and Best Practices

- Use FACT for whole numbers, and GAMMA only when the input is fractional.
- Keep inputs positive in shared workbooks, because Google Sheets requires it.
- Use GAMMALN when the gamma value is so large that it overflows, because the logarithm stays in range.
- Label the cell that holds the gamma value so reviewers know it came from a distribution constant.
- Check one known value, such as GAMMA(5) equal to 24, after you build the model.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FACT](../Math%20%26%20Trig/FACT.md) | Returns the factorial of a whole number, the matching result for integer inputs. |
| [GAMMA.DIST](GAMMA.DIST.md) | Uses the gamma function inside the gamma distribution. |
| [GAMMA.INV](GAMMA.INV.md) | Returns the inverse of the gamma distribution. |
| [GAMMALN](GAMMALN.md) | Returns the natural logarithm of the gamma function. |
| [GAMMALN.PRECISE](GAMMALN.PRECISE.md) | Returns the natural logarithm of the gamma function with the precise method. |

## Official Documentation

- [Microsoft Support: GAMMA function](https://support.microsoft.com/en-us/excel/functions/gamma-function)
- [Google Docs Editors Help: GAMMA](https://support.google.com/docs/answer/9365856)
