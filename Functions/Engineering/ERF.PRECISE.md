---
domain: Spreadsheet Functions
category: Engineering
subcategory: Error Functions
purpose:
  - Probability
  - Statistical Analysis
use-case:
  - Normal Distribution Probability
  - Process Tolerance Analysis
related:
  - ERF
  - ERFC
  - ERFC.PRECISE
  - NORM.DIST
  - NORM.S.DIST
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/erf-precise-function
  - https://support.google.com/docs/answer/9116267
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Precise Error Function
tags:
  - error-function
  - excel
  - probability
  - sheets
---

# ERF.PRECISE

## Description

**ERF.PRECISE** returns the error function integrated from 0 up to a single value `x`. It is the one-argument form of the error function, so it suits workbooks that always integrate from zero. It returns a value between -1 and 1 for ordinary inputs, and its result for a given `x` matches ERF with that same single argument.

Use ERF.PRECISE when the model needs only the share of a normal distribution between the mean and a point, or when the sheet should be simple to audit. If you need the integral between two limits, use ERF with both arguments. For the upper tail, use ERFC.PRECISE, which is the complement of this function.

The error function is odd, so ERF.PRECISE of a negative value is the negative of the result for the positive value. For example, `ERF.PRECISE(-1)` returns the negative of `ERF.PRECISE(1)`.

## Syntax

```excel
=ERF.PRECISE(x)
```

<!-- Image 1: Area From Zero to the Input Under the Error Function. See Images/Engineering/ERF.PRECISE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The upper end of the integral that starts at 0. Non-numeric input returns `#VALUE!`. |

### Return Value

A decimal number between -1 and 1 for ordinary inputs. The function returns `#VALUE!` when `x` is not numeric.

## Examples

### Example 1: Positive Input

```excel
=ERF.PRECISE(0.745)
```

**Result:** `0.70792892`

The integral from 0 to 0.745 is 0.70792892, the same value ERF gives for that argument.

### Example 2: Whole Number Input

```excel
=ERF.PRECISE(1)
```

**Result:** `0.84270079`

The integral from 0 to 1 is 0.84270079.

### Example 3: Negative Input

```excel
=ERF.PRECISE(-1)
```

**Result:** `-0.84270079`

The function is odd, so a negative input returns the negative of the value for the positive input.

### Example 4: Larger Input

```excel
=ERF.PRECISE(2)
```

**Result:** `0.99532227`

At 2, the function is already close to 1, which is why it is used for the share of a distribution within about two standard deviations.

## Story Problems

### Problem 1: Tolerance Bands on a Filling Line

A filling line checks bottle fills against a normal distribution. The quality team wants the share of fills within plus or minus 0.5, 1.5 and 2.5 standard deviations, which is `ERF.PRECISE(z/SQRT(2))` for each band.

| Band (Sigma) |
| --- |
| 0.5 |
| 1.5 |
| 2.5 |

**Task:** Calculate the share of fills inside each band, starting at row 2 in column A, and write the results in column B.

**Solution:**

```excel
=ERF.PRECISE(A2/SQRT(2))
```

Enter this in B2 and fill it down to B4.

**Answer:** `0.3829`, `0.8664`, and `0.9876`. About 38.29 percent of fills fall within half a sigma, 86.64 percent within 1.5 sigma, and 98.76 percent within 2.5 sigma.

### Problem 2: Share Between the Mean and a Limit

A coating thickness process reports how far each reading sits above the mean, in standard deviations. The engineer needs the share of readings between the mean and each limit.

| Limit (Sigma) |
| --- |
| 0.75 |
| 1.25 |
| 2.25 |

**Task:** Calculate the share between the mean and each limit, starting at row 2 in column A, and write the results in column B.

**Solution:**

```excel
=ERF.PRECISE(A2/SQRT(2))/2
```

Enter this in B2 and fill it down to B4.

**Answer:** `0.2734`, `0.3944`, and `0.4878`. Halving the share within the band gives the share on one side of the mean.

<!-- Image 2: Tolerance Band Shares Table. See Images/Engineering/ERF.PRECISE.md -->

## Use Cases

### Normal Distribution Probability

**Scenario:** A capacity model needs the share of output between the mean and a planning limit, expressed in standard deviations.

```excel
=ERF.PRECISE(B2/SQRT(2))/2
```

**Why It Works:** The limit is converted to the error function argument, and halving the result gives the share on one side of the mean. The same pattern works for any symmetric distribution that is close to normal.

### Process Tolerance Analysis

**Scenario:** A process engineer compares the share inside a tolerance band with a target yield.

```excel
=ERF.PRECISE(ABS(B2)/SQRT(2))
```

**Why It Works:** ABS makes the band symmetric when the sigma value is entered with a sign. Compare the result with the target yield in a separate cell to flag bands that fall short.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text or blank in a way that cannot be read as a number. | Clean the source cell or enter the value as a number. |
| Negative result | The input is negative, which is correct for this odd function. | Take the absolute value first if only the size of the share is needed. |
| Two-argument formula fails | ERF.PRECISE takes one argument only. | Use ERF with two arguments to integrate between two limits. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 and Excel for the web | Single argument `x`. Integrates from 0 to `x`. |
| Google Sheets | Available | The help page for the ERF family is the reference. Confirm the argument list there before you use the function. |

## Tips and Best Practices

- Use ERF.PRECISE in models that always start at the mean, so the formula stays short and clear.
- Convert sigma values with SQRT(2) once in a helper column rather than repeating it in every formula.
- Keep the band limits in input cells so reviewers can test different tolerances.
- Use ERFC.PRECISE for upper-tail shares, rather than subtracting this result from 1.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ERF](ERF.md) | Two-argument form that integrates between any two limits. |
| [ERFC](ERFC.md) | Complement of ERF, 1 minus the result. |
| [ERFC.PRECISE](ERFC.PRECISE.md) | Precise complement for upper-tail shares. |
| [NORM.DIST](../Statistical/NORM.DIST.md) | Returns normal probabilities directly for a mean and standard deviation. |
| [NORM.S.DIST](../Statistical/NORM.S.DIST.md) | Returns standard normal probabilities directly. |

## Official Documentation

- [Microsoft Support: ERF.PRECISE function](https://support.microsoft.com/en-us/excel/functions/erf-precise-function)
- [Google Docs Editors Help: ERF](https://support.google.com/docs/answer/9116267)
