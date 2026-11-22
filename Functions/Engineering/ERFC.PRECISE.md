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
  - ERFC
  - NORM.S.DIST
  - NORMSDIST
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/erfc-precise-function
  - https://support.google.com/docs/answer/3093407
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - error-function
  - excel
  - probability
  - sheets
  - statistics
---

# ERFC.PRECISE

## Description

**ERFC.PRECISE** returns the complementary error function of a number x, which is the integral of the error-function integrand from x to infinity. Microsoft describes it as the complementary ERF function integrated between x and infinity. The result equals 1 minus ERF(x).

Use ERFC.PRECISE when a workbook is built for Excel and the formula must follow Microsoft's function naming. It supports the same tail-probability work as ERFC: multiply the result by 0.5 and divide the input by the square root of 2 to get the upper tail of a standard normal distribution.

Google Sheets does not list ERFC.PRECISE. Google's engineering help covers ERFC, so use ERFC in any workbook that is shared with Google Sheets users. Microsoft's examples give the same result for both functions at an input of 1.

## Syntax

```excel
=ERFC.PRECISE(x)
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/ERFC.PRECISE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The lower bound of the integral, as a number or a cell that contains a number. Nonnumeric input returns `#VALUE!`. |

### Return Value

A decimal number. The result is between 0 and 1 for x of 0 or greater, and between 1 and 2 for negative x.

## Examples

### Example 1: Basic Usage

```excel
=ERFC.PRECISE(1)
```

**Result:** `0.15729921`

The value matches the Microsoft example for ERFC.PRECISE with an input of 1.

### Example 2: Upper-Tail Probability

Cell `B2` holds the z-score `1.5`.

```excel
=0.5*ERFC.PRECISE(B2/SQRT(2))
```

**Result:** `0.06681`

About 6.7 percent of standard normal values are greater than 1.5.

### Example 3: Comparing With ERFC

```excel
=ERFC.PRECISE(A2)-ERFC(A2)
```

**Result:** `0` when both functions return the same value

The difference is zero when both functions return the same value for the input in `A2`. Use this check when you replace ERFC with ERFC.PRECISE in an existing model.

### Example 4: Zero Input

```excel
=ERFC.PRECISE(0)
```

**Result:** `1`

The integral from 0 to infinity covers the whole positive half of the function, so the result is 1.

<!-- Image 2: Battery Retest Worksheet. See Images/Engineering/ERFC.PRECISE.md -->

## Story Problems

### Problem 1: Battery Cell Voltage Check

A pack assembler measures how far each cell's voltage sits above the nominal value, in standard deviations. Cells above 2.0 are sent for retest.

| Cell | Z-Score |
| --- | --- |
| C01 | 0.5 |
| C02 | 2.0 |
| C03 | 1.2 |
| C04 | 2.5 |

**Task:** Put the share of cells expected above each z-score in column C, then find the share expected above 2.0 (cell `B3`).

**Solution:**

```excel
=0.5*ERFC.PRECISE(B3/SQRT(2))
```

**Answer:** `0.02275`. Roughly 2.3 percent of cells are expected to exceed 2.0 and need retest. In Google Sheets, replace ERFC.PRECISE with ERFC.

### Problem 2: Delivery Time Tail

A courier company models delivery times as a standard normal variable. The team wants the probability that a route takes more than 3 standard deviations longer than average.

**Task:** Calculate the upper-tail probability for a z-score of 3 in cell `B2`.

**Solution:**

```excel
=0.5*ERFC.PRECISE(B2/SQRT(2))
```

**Answer:** `0.00135`. Only about 1 in 741 routes is expected to exceed that threshold.

## Use Cases

### Specification Limit Risk

**Scenario:** A process engineer estimates how many parts exceed an upper limit each shift.

```excel
=BatchSize*0.5*ERFC.PRECISE(((UpperLimit-Mean)/SD)/SQRT(2))
```

**Why It Works:** The formula converts the limit to a z-score, takes the tail probability and multiplies by the batch size to give an expected count.

### Tail Probability Reports

**Scenario:** A risk team reports the chance that a stress scenario exceeds a design limit.

```excel
=0.5*ERFC.PRECISE(Scenarios[ZScore]/SQRT(2))
```

**Why It Works:** The structured reference extends automatically when scenarios are added to the table. Format the output as a percentage.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text, blank or an error value. | Convert the input to a number before calling the function. |
| `#NAME?` | The workbook is opened in Google Sheets, which does not list ERFC.PRECISE. | Replace the function with ERFC. |
| Inverted probability | The formula returns the upper tail, but the analyst expected the lower tail. | Use `1 - 0.5*ERFC.PRECISE(z/SQRT(2))`. |
| Unexpected value | The z-score was not standardized. | Subtract the mean and divide by the standard deviation first. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Excel for Microsoft 365 and Excel for the web | Returns `#VALUE!` for nonnumeric input. |
| Google Sheets | Not available | Use ERFC, which has the same arguments and return value. |

## Tips and Best Practices

- Use ERFC.PRECISE in Excel-only models, and ERFC in any model shared with Google Sheets users.
- Keep a check cell that compares ERFC and ERFC.PRECISE when you migrate a workbook between the two.
- Use NORM.S.DIST for ordinary normal probabilities that do not need the error function form.
- Label the z-score column clearly so reviewers can see the standardization step.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ERF](ERF.md) | Returns the error function; ERF(x) equals 1 minus ERFC.PRECISE(x). |
| [ERF.PRECISE](ERF.PRECISE.md) | Excel version of the error function for the same range of inputs. |
| [ERFC](ERFC.md) | Complementary error function that Google Sheets supports; use it when portability matters. |
| [NORM.S.DIST](../Statistical/NORM.S.DIST.md) | Returns standard normal probabilities without the error function form. |
| [NORMSDIST](../Statistical/NORMSDIST.md) | Legacy function that returns the standard normal cumulative distribution. |

## Official Documentation

- [Microsoft Support: ERFC.PRECISE function](https://support.microsoft.com/en-us/excel/functions/erfc-precise-function)
- [Google Docs Editors Help: ERFC](https://support.google.com/docs/answer/3093407)
