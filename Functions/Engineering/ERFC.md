---
domain: Spreadsheet Functions
category: Engineering
subcategory: Error Functions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Specification Limit Risk
  - Tail Probability Reports
related:
  - ERF
  - ERF.PRECISE
  - ERFC.PRECISE
  - NORM.S.DIST
  - NORMSDIST
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/erfc-function
  - https://support.google.com/docs/answer/3093407
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Complementary Error Function
tags:
  - error-function
  - excel
  - probability
  - sheets
  - statistics
---

# ERFC

## Description

**ERFC** returns the complementary error function of a number x. It equals 1 minus ERF(x), and it integrates the function e^(-t^2) from x to infinity, scaled by 2 divided by the square root of pi.

The most useful application is the upper tail of a normal distribution. The probability that a standard normal value is greater than z equals 0.5 * ERFC(z / SQRT(2)). Engineers use this form to estimate how often a measurement will fall beyond a specification limit once the limit has been converted to a z-score.

ERFC is more reliable than 1 minus ERF(x) when x is large. In that range ERF is very close to 1, so subtracting it from 1 discards significant digits. ERFC returns the small tail value directly. Microsoft Excel supports ERFC in all current versions. Google Sheets lists both ERFC and the related ERFC.PRECISE function.

## Syntax

```excel
=ERFC(x)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/ERFC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The lower bound of the integral, as a number or a cell that contains a number. Text that cannot be read as a number returns `#VALUE!`. |

### Return Value

A decimal number. For x of 0 or greater the result is between 0 and 1; for negative x the result is between 1 and 2. ERFC(0) returns 1.

## Examples

### Example 1: Basic Usage

```excel
=ERFC(1)
```

**Result:** `0.15729921`

The scaled area under e^(-t^2) from 1 to infinity is about 0.157, which matches the value from the Microsoft example.

### Example 2: Tail Probability From a Z-Score

Cell `A2` holds the z-score `2`.

```excel
=0.5*ERFC(A2/SQRT(2))
```

**Result:** `0.02275`

This is the probability that a standard normal value is greater than 2, about 2.3 percent.

### Example 3: Negative Input

```excel
=ERFC(-1)
```

**Result:** `1.8427008`

For negative x the result is above 1. The value equals 2 minus ERFC(1), which is 2 minus 0.1572992.

### Example 4: The Same Calculation in ERFC.PRECISE

```excel
=ERFC.PRECISE(1)
```

**Result:** `0.15729921`

Excel and Google Sheets both list ERFC.PRECISE with the same single argument.

<!-- Image 2: Tail Probability Worksheet. See Images/Engineering/ERFC.md -->

## Story Problems

### Problem 1: Shaft Diameter Tolerance

A machine shop checks how often a turned shaft is oversize. The process mean is 25.00 mm and the standard deviation is 0.10 mm. The table converts several upper limits to z-scores.

| Upper Limit (mm) | Z-Score |
| --- | --- |
| 25.10 | 1.0 |
| 25.15 | 1.5 |
| 25.20 | 2.0 |
| 25.25 | 2.5 |

**Task:** In `C2:C5`, calculate the share of shafts above each limit, using the z-scores in `B2:B5`.

**Solution:**

```excel
=0.5*ERFC(B2/SQRT(2))
```

Fill the formula down to `C5`.

**Answer:** `C2:C5` return `0.15866`, `0.06681`, `0.02275` and `0.00621`. For example, about 15.9 percent of shafts exceed 25.10 mm.

### Problem 2: Pressure Relief Setting

A valve opens when a standardized pressure reading exceeds 1.5. Cell `B2` holds the threshold.

**Task:** Calculate the probability that a reading exceeds the threshold, assuming a standard normal distribution.

**Solution:**

```excel
=0.5*ERFC(B2/SQRT(2))
```

**Answer:** `0.06681`. Roughly 6.7 percent of readings will open the valve.

## Use Cases

### Specification Limit Risk

**Scenario:** A quality team wants the expected share of parts beyond an upper limit, using the process mean and standard deviation.

```excel
=0.5*ERFC(((UpperLimit-ProcessMean)/ProcessSD)/SQRT(2))
```

**Why It Works:** The expression turns the limit into a z-score and then into a tail probability. Multiply the result by the batch size to estimate the number of out-of-tolerance parts.

### Tail Probability Reports

**Scenario:** A reliability analyst reports how likely a load exceeds a design value across several scenarios.

```excel
=0.5*ERFC(Scenarios[ZScore]/SQRT(2))
```

**Why It Works:** Structured references let the formula extend as scenarios are added. The output is a probability between 0 and 1, so format the column as a percentage.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text, blank or an error value. | Convert the input to a number or wrap the reference in `N()`. |
| Inverted probability | The formula returns the upper tail, but the analyst expected the area below z. | Use `1 - 0.5*ERFC(z/SQRT(2))` for the lower tail. |
| Wrong probability | The z-score was not standardized, so the formula uses the raw measurement. | Subtract the mean and divide by the standard deviation first. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365 and Excel for the web | Returns `#VALUE!` for nonnumeric input. |
| Google Sheets | Available | Same single argument and return value as Excel, as described in the Google Docs Editors help. |

## Tips and Best Practices

- Use `0.5*ERFC(z/SQRT(2))` for upper-tail probabilities of a standard normal variable.
- Keep the z-score in its own cell so the standardization step is visible during review.
- Use NORM.S.DIST when the workbook only needs ordinary normal probabilities and does not require the error function form.
- Check the sign of the input: ERFC returns values above 1 for negative x, which can look like an error to reviewers.
- Compare results with ERF when you need the cumulative part: ERF(x) equals 1 minus ERFC(x).

## Related Functions

| Function | Relationship |
| --- | --- |
| [ERF](ERF.md) | Returns the error function itself; ERF(x) equals 1 minus ERFC(x). |
| [ERF.PRECISE](ERF.PRECISE.md) | Excel version of the error function for the same range of inputs. |
| [ERFC.PRECISE](ERFC.PRECISE.md) | Excel version of the complementary error function with the same description. |
| [NORM.S.DIST](../Statistical/NORM.S.DIST.md) | Returns standard normal probabilities directly, without the error function form. |
| [NORMSDIST](../Statistical/NORMSDIST.md) | Legacy function that returns the standard normal cumulative distribution. |

## Official Documentation

- [Microsoft Support: ERFC function](https://support.microsoft.com/en-us/excel/functions/erfc-function)
- [Google Docs Editors Help: ERFC](https://support.google.com/docs/answer/3093407)
