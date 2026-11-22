---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Hypothesis Testing
use-case:
  - Machine Variability Check
  - Two Group Spread Comparison
related:
  - F.DIST.RT
  - F.TEST
  - TTEST
  - VAR.S
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/ftest-function
  - https://support.google.com/docs/answer/7004183
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Equal Variance Test
tags:
  - compatibility
  - excel
  - hypothesis-testing
  - sheets
---

# FTEST

## Description

**FTEST** returns the probability from an F-test of whether two samples have the same variance. The result is a two-tailed probability. A small probability, usually below 0.05, suggests that the two samples have different spreads. A larger probability means the data does not show a clear difference in variance.

FTEST returns a probability, not the F statistic. Microsoft's support page warns that the LINEST function returns the F statistic, so the two functions give different values for the same data. Use FTEST only when you need the probability itself.

FTEST is a legacy function. Microsoft replaced it with **F.TEST**, which returns the same kind of result and remains available for backward compatibility. Use F.TEST in new work, and keep FTEST only in workbooks that already use it. Microsoft notes that FTEST may not be available in future versions of Excel.

## Syntax

```excel
=FTEST(array1, array2)
```

<!-- Image 1: Two Samples Layout. See Images/Statistical/FTEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first sample, as a range or an array of numbers. Text, logical values and blank cells are ignored. |
| `array2` | Yes | The second sample, in the same form as `array1`. Zeros are included in the test. |

### Return Value

A probability between 0 and 1. The function returns `#DIV/0!` when either sample has fewer than two numeric values, or when either sample has a variance of zero.

## Examples

The examples use two small samples. Sample A is in `A2:A6` with the values 10, 12, 9, 11 and 13. Sample B is in `B2:B6` with the values 20, 25, 18, 30 and 22. Sample A has a variance of 2.5 and sample B has a variance of 22.

### Example 1: Comparing Two Samples

```excel
=FTEST(A2:A6, B2:B6)
```

**Result:** `0.0582`

The probability is above 0.05, so the test does not show a clear difference in variance at the 5 percent level, even though sample B is much more spread out.

### Example 2: The Same Test With F.TEST

```excel
=F.TEST(A2:A6, B2:B6)
```

**Result:** `0.0582`

F.TEST returns the same probability as FTEST for the same samples. Use this form in new workbooks.

<!-- Image 2: Spread Comparison Chart. See Images/Statistical/FTEST.md -->

### Example 3: Turning the Probability Into a Decision

```excel
=IF(FTEST(A2:A6, B2:B6) < 0.05, "Variances differ", "No clear difference")
```

**Result:** `No clear difference`

The 0.05 threshold is a common convention. Choose a different threshold only when the review process requires one.

### Example 4: Checking the Variances Directly

```excel
=VAR.S(A2:A6)
```

**Result:** `2.5`

VAR.S returns the sample variance of sample A. Check the variances like this to see why the probability is high or low, because FTEST does not return them.

## Story Problems

### Problem 1: Bottle Fill Consistency

A bottling plant compares two filling machines. The filled volumes in milliliters are in `A2:A8` for Machine A and `B2:B8` for Machine B. Machine A has six readings, so its last row is blank.

| Row | Machine A | Machine B |
| --- | --- | --- |
| 2 | 500.2 | 499.0 |
| 3 | 499.8 | 501.2 |
| 4 | 500.5 | 500.9 |
| 5 | 499.6 | 498.4 |
| 6 | 500.1 | 501.5 |
| 7 | 500.4 | 499.3 |
| 8 | blank | 500.6 |

**Task:** Decide whether the two machines have different spreads in their fill volumes.

**Solution:**

```excel
=FTEST(A2:A8, B2:B8)
```

**Answer:** `0.0148`. The probability is below 0.05, and Machine B has a much larger variance (about 1.47) than Machine A (about 0.12), so the two machines do not fill with the same consistency.

<!-- Image 3: Decision Result Panel. See Images/Statistical/FTEST.md -->

### Problem 2: Delivery Days on Two Routes

A logistics team records delivery days for two routes over seven weeks. Route X has a steady pattern, and Route Y has some very fast and very slow weeks.

| Week | Route X | Route Y |
| --- | --- | --- |
| 1 | 3 | 2 |
| 2 | 4 | 6 |
| 3 | 4 | 8 |
| 4 | 5 | 3 |
| 5 | 6 | 9 |
| 6 | 4 | 1 |
| 7 | 5 | 7 |

**Task:** Test whether the two routes have the same spread in delivery days.

**Solution:**

```excel
=FTEST(B2:B8, C2:C8)
```

**Answer:** `0.0121`. The probability is well below 0.05, so the routes have different spreads. Route Y varies much more from week to week.

## Use Cases

### Machine Variability Check

**Scenario:** A quality engineer confirms that two production lines produce parts with similar consistency before combining their data.

```excel
=F.TEST(Line1_Weights, Line2_Weights)
```

**Why It Works:** A low probability means the lines differ in spread, so pooling their data would hide a quality problem. The F.TEST name is used here because it is the current function.

### Two Group Spread Comparison

**Scenario:** An analyst checks whether two sales regions have the same spread in monthly revenue before choosing a t test.

```excel
=FTEST(Region_East, Region_West)
```

**Why It Works:** The variance test decides whether the t test should assume equal variances. Keep the variance check in a separate column so reviewers can see the decision.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | A sample has fewer than two numbers, or a sample has zero variance. | Add data, or check that all values in the sample are not identical. |
| Probability looks wrong | The function was read as the F statistic, which is a different value. | Use VAR.S to check the variances and F.DIST.RT for the statistic's tail probability. |
| Unexpected result | A sample includes text or logical values that were treated as missing. | Clean the sample so every value is a number. |
| `#NAME?` | The version does not recognize FTEST. | Use F.TEST, which is the current function. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Legacy compatibility function. Microsoft recommends F.TEST for new work. |
| Google Sheets | Available | Non-numeric cells are skipped. The Google page notes that F.TEST is an alternative name for the same function. |

## Tips and Best Practices

- Use F.TEST in new workbooks, and document FTEST only where older files depend on it.
- Run the variance check before a t test, because the choice of t test depends on whether the variances are equal.
- Check both sample sizes first; a sample with one value cannot produce a result.
- Keep the two samples in separate columns with clear headers, so a reviewer can see which group is which.
- Report the probability with the variances, so the reader can see the size of the difference and not only the test result.

## Related Functions

| Function | Relationship |
| --- | --- |
| [F.TEST](F.TEST.md) | Current name for the same test, recommended for new work. |
| [F.DIST.RT](F.DIST.RT.md) | Returns the right-tail probability of the F distribution for an F statistic. |
| [TTEST](TTEST.md) | Compares the means of two samples, often run after the variance check. |
| [VAR.S](VAR.S.md) | Returns the sample variance used to judge the spread of each sample. |

## Official Documentation

- [Microsoft Support: FTEST function](https://support.microsoft.com/en-us/excel/functions/ftest-function)
- [Google Docs Editors Help: FTEST](https://support.google.com/docs/answer/7004183)
