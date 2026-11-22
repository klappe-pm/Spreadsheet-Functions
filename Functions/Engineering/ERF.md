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
  - ERF.PRECISE
  - ERFC
  - ERFC.PRECISE
  - NORM.DIST
  - NORM.S.DIST
  - SQRT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/erf-function
  - https://support.google.com/docs/answer/9116267
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Error Function
  - Gauss Error Function
tags:
  - error-function
  - excel
  - probability
  - sheets
---

# ERF

## Description

**ERF** returns the Gauss error function, which is the integral of the function `2/SQRT(PI())*EXP(-t^2)` over an interval. Statisticians use it to find the share of a normal distribution that lies between two points, so it appears in tolerance analysis, quality control and probability work. You supply the lower limit, and the upper limit is optional.

When you give only one argument, ERF integrates from 0 up to that value. When you give both, it integrates between them, so `ERF(0.5,1)` is the integral from 0.5 to 1. Because the function is an integral, reversing the limits flips the sign of the result.

For a normal distribution with standard deviation sigma, the share of values within plus or minus z sigma is `ERF(z/SQRT(2))`. ERF.PRECISE is the single-argument form of the same integral, and ERFC gives the complement, 1 minus ERF.

## Syntax

```excel
=ERF(lower_limit, [upper_limit])
```

<!-- Image 1: Area Under the Error Function Curve. See Images/Engineering/ERF.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `lower_limit` | Yes | The lower bound of the integration. Non-numeric input returns `#VALUE!`. |
| `upper_limit` | No | The upper bound. When omitted, the integral runs from 0 to `lower_limit`. Non-numeric input returns `#VALUE!`. |

### Return Value

A decimal number between -1 and 1 for ordinary inputs. The result is the integral between the two limits. The function returns `#VALUE!` when either limit is not numeric.

## Examples

### Example 1: One Argument

```excel
=ERF(0.745)
```

**Result:** `0.70792892`

With one argument, the integral runs from 0 to 0.745, which gives 0.70792892.

### Example 2: One Whole Number

```excel
=ERF(1)
```

**Result:** `0.84270079`

The integral from 0 to 1 is 0.84270079, a value that often appears in normal distribution tables.

### Example 3: Two Arguments

```excel
=ERF(0.5,1)
```

**Result:** `0.3222009`

The integral from 0.5 to 1 is the value at 1 minus the value at 0.5, which is about 0.3222.

### Example 4: Symmetric Limits

```excel
=ERF(-1,1)
```

**Result:** `1.6854016`

The function is odd, so the integral from -1 to 1 equals twice the integral from 0 to 1.

## Story Problems

### Problem 1: Shaft Diameter Tolerance

A machine shop produces steel shafts whose diameters follow a normal distribution. The quality team wants the share of shafts that fall within one, two and three standard deviations of the mean. For a normal distribution, that share is `ERF(z/SQRT(2))`.

| Band (Sigma) |
| --- |
| 1 |
| 2 |
| 3 |

**Task:** Calculate the share of shafts inside each band, starting at row 2 in column A, and write the results in column B.

**Solution:**

```excel
=ERF(A2/SQRT(2))
```

Enter this in B2 and fill it down to B4.

**Answer:** `0.6827`, `0.9545`, and `0.9973`. About 68.27 percent of shafts fall within one sigma, 95.45 percent within two, and 99.73 percent within three.

### Problem 2: Share Between the Mean and a Limit

A plant measures how far each fill weight sits from the target, in standard deviations. The team needs the share of the distribution between the mean and each limit, which is half of the share within plus or minus that limit.

| Limit (Sigma) |
| --- |
| 0.5 |
| 1 |
| 2 |

**Task:** Calculate the share between the mean and each limit, starting at row 2 in column A, and write the results in column B.

**Solution:**

```excel
=ERF(A2/SQRT(2))/2
```

Enter this in B2 and fill it down to B4.

**Answer:** `0.1915`, `0.3413`, and `0.4772`. The limit of one sigma covers about 34.13 percent between the mean and the limit on one side.

<!-- Image 2: Sigma Band Shares Table. See Images/Engineering/ERF.md -->

## Use Cases

### Normal Distribution Probability

**Scenario:** A planning sheet estimates the share of output that falls between the mean and a chosen limit.

```excel
=ERF(B2/SQRT(2))/2
```

**Why It Works:** The formula converts the limit from sigma units into the error function argument and halves the result, since the distribution is symmetric around the mean.

### Process Tolerance Analysis

**Scenario:** A process engineer wants the share of parts inside a symmetric tolerance band of plus or minus a chosen number of sigma.

```excel
=ERF(ABS(B2)/SQRT(2))
```

**Why It Works:** ABS makes the band symmetric even if the sigma value is entered as a negative number. Check that the process is close to normal before you rely on the result.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A limit is text or blank in a way that cannot be read as a number. | Clean the source cell or enter the limit as a number. |
| Negative result | The limits are reversed, so the integral runs backward. | Put the smaller limit first, or take the absolute value of the result. |
| Result off by a factor of two | The share within a band was read as the share from the mean to the limit. | Use the formula that matches the question: within the band, or from the mean. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, including Microsoft 365 and Excel for the web | Accepts one or two arguments. Results match the integral definition. |
| Google Sheets | Available | Names the arguments `lower_bound` and `upper_bound`. The optional upper bound works the same way. |

## Tips and Best Practices

- Use a helper column for sigma values, so the bands can be changed without editing the formulas.
- Remember that the two-argument form is a difference of two integrals, so the order of the limits matters.
- Pair ERF with NORM.DIST when you need a direct cumulative probability for a stated mean and standard deviation.
- Use ERFC for the upper tail, since subtracting ERF from 1 can lose precision for very large limits.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ERF.PRECISE](ERF.PRECISE.md) | Single-argument form that integrates from 0 to x. |
| [ERFC](ERFC.md) | Complementary error function, 1 minus ERF. |
| [ERFC.PRECISE](ERFC.PRECISE.md) | Precise complementary form for the upper tail. |
| [NORM.DIST](../Statistical/NORM.DIST.md) | Returns normal probabilities directly for a mean and standard deviation. |
| [NORM.S.DIST](../Statistical/NORM.S.DIST.md) | Returns standard normal probabilities directly. |
| [SQRT](../Math%20%26%20Trig/SQRT.md) | Converts sigma values into the error function argument. |

## Official Documentation

- [Microsoft Support: ERF function](https://support.microsoft.com/en-us/excel/functions/erf-function)
- [Google Docs Editors Help: ERF](https://support.google.com/docs/answer/9116267)
