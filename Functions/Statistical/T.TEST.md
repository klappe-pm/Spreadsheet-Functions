---
domain: Spreadsheet Functions
category: Statistical
subcategory: Hypothesis Tests
purpose:
  - Hypothesis Testing
  - Statistical Analysis
use-case:
  - Before and After Pilot Results
  - Two Plant Comparison
related:
  - F.TEST
  - T.DIST.2T
  - T.INV.2T
  - TTEST
  - Z.TEST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/t-test-function
  - https://support.google.com/docs/answer/6055837
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Paired T Test
  - Student T Test
tags:
  - excel
  - hypothesis-test
  - sheets
  - statistical
  - t-test
---

# T.TEST

## Description

**T.TEST** returns the p-value of a Student t-test. It compares two samples and gives the probability of seeing a difference at least as large as the one in your data if the two samples really came from populations with the same mean. A small p-value, usually below 0.05, is evidence that the means differ.

The `type` argument sets the kind of test. Use `1` for a paired test, where each value in the first range has a matching partner in the second range, such as the same patient before and after treatment. Use `2` when the two samples are independent and their spreads are similar, and `3` when the two samples are independent and their spreads differ. The two ranges must have the same number of points for a paired test, and Excel returns `#N/A` when they do not.

The `tails` argument is `1` for a one-tailed test, which checks for a difference in one direction chosen before the data was collected, and `2` for a two-tailed test, which checks for a difference either way. The two-tailed result is double the one-tailed result. T.TEST replaces the older TTEST function, which remains available in both Excel and Sheets.

## Syntax

```excel
=T.TEST(array1, array2, tails, type)
```

<!-- Image 1: Two Sample Ranges and the Test Options. See Images/Statistical/T.TEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first sample, such as the before values or the first group. |
| `array2` | Yes | The second sample, such as the after values or the second group. |
| `tails` | Yes | `1` for a one-tailed test or `2` for a two-tailed test. Other values return `#NUM!`. |
| `type` | Yes | `1` for paired, `2` for two-sample equal variance, or `3` for two-sample unequal variance. |

### Return Value

A probability between 0 and 1. Excel returns `#N/A` when `type` is `1` and the two arrays have different sizes, `#VALUE!` when `tails` or `type` is not numeric, and `#NUM!` when `tails` is a value other than 1 or 2. Google Sheets returns `#DIV/0!` when the variance of either range is zero.

## Examples

All paired examples use a before range in `B2:B9` and an after range in `C2:C9` for eight patients.

### Example 1: Two-Tailed Paired Test

```excel
=T.TEST(B2:B9, C2:C9, 2, 1)
```

**Result:** `0.006198`

A p-value this small suggests the change from before to after is unlikely to be chance alone.

### Example 2: One-Tailed Paired Test

```excel
=T.TEST(B2:B9, C2:C9, 1, 1)
```

**Result:** `0.003099`

The one-tailed result is half the two-tailed result. Use it only when the direction of the change was set before the data was collected.

<!-- Image 2: Paired Versus Two-Sample Layouts. See Images/Statistical/T.TEST.md -->

### Example 3: Two Independent Groups With Equal Variance

Group A is in `A2:A7` and group B is in `B2:B8`. Each group is independent of the other.

```excel
=T.TEST(A2:A7, B2:B8, 2, 2)
```

**Result:** `0.000432`

The pooled test uses one shared spread estimate, which fits groups with similar variability.

### Example 4: Unequal Sizes in a Paired Test

```excel
=T.TEST(A2:A7, B2:B8, 2, 1)
```

**Result:** `#N/A`

A paired test needs the same number of points in each range. Group A has six values and group B has seven, so the function returns `#N/A`.

### Example 5: Unequal Variance Test

```excel
=T.TEST(A2:A7, B2:B8, 2, 3)
```

This form uses separate spread estimates for the two groups. Use it when the groups clearly differ in spread, and compare its p-value with the Example 3 result to see how much the choice matters. This page does not state a computed value for these inputs.

## Story Problems

### Problem 1: Pilot Program Blood Pressure

Eight patients had their systolic blood pressure measured before and after a six-week pilot program. The readings are in `B1:C9`, with the header row in row 1.

| Patient | Before | After |
| --- | --- | --- |
| 1 | 72 | 70 |
| 2 | 75 | 74 |
| 3 | 68 | 66 |
| 4 | 80 | 77 |
| 5 | 77 | 75 |
| 6 | 74 | 72 |
| 7 | 69 | 70 |
| 8 | 81 | 78 |

**Task:** Test whether the pilot changed the readings, using a paired two-tailed test.

**Solution:**

```excel
=T.TEST(B2:B9, C2:C9, 2, 1)
```

**Answer:** `0.006198`. The readings dropped in seven of eight patients, and the p-value is well below 0.05.

### Problem 2: Two Plants Filling Speed

Two plants reported independent samples of fill times in seconds, and the managers assume the spreads are similar. Plant A is in `A2:A7` and plant B is in `B2:B8`.

| Plant A | Plant B |
| --- | --- |
| 12.1 | 11.2 |
| 11.8 | 11.5 |
| 12.6 | 11.0 |
| 12.3 | 11.8 |
| 11.9 | 11.4 |
| 12.4 | 11.3 |
| | 11.6 |

**Task:** Test whether the mean fill times differ, using a two-tailed test with equal variance.

**Solution:**

```excel
=T.TEST(A2:A7, B2:B8, 2, 2)
```

**Answer:** `0.000432`. Plant A is slower on average, and the difference is very unlikely to come from chance alone.

<!-- Image 3: Two Sample Result Worksheet. See Images/Statistical/T.TEST.md -->

## Use Cases

### Before and After Pilot Results

**Scenario:** A clinic wants to know whether a new scheduling process changed patient wait times for the same clinicians.

```excel
=T.TEST(Pilot[Before], Pilot[After], 2, 1)
```

**Why It Works:** The paired test pairs each clinician's before and after value, which removes differences between clinicians from the comparison. Both columns must have the same number of rows.

### Two Plant Comparison

**Scenario:** A manufacturer compares the defect rate measured on two independent production lines.

```excel
=T.TEST(LineA[Defects], LineB[Defects], 2, 2)
```

**Why It Works:** The two lines are independent, so the two-sample test applies. Confirm the spreads are similar before choosing type 2, or use type 3 when they differ.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | A paired test uses ranges of different sizes. | Make both ranges the same length, with matching rows. |
| `#NUM!` | `tails` is not 1 or 2. | Enter 1 or 2. |
| `#VALUE!` | `tails` or `type` is text. | Enter the numbers 1, 2 or 3. |
| Wrong p-value | `type` is set to paired for independent groups. | Use type 2 or 3 for independent samples. |
| `#DIV/0!` in Sheets | A range has zero variance. | Check for constant values in either range. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2010 and later, including Microsoft 365 | Returns `#N/A` for paired ranges of different sizes. The page does not state the size rule for types 2 and 3. |
| Google Sheets | Available | Requires `range1` and `range2` to hold the same number of points. Accepts TTEST as an alternative name. |

## Tips and Best Practices

- Choose the test type before you look at the results, and write the choice in the sheet notes.
- Use type 1 only when the two columns describe the same units in the same order.
- Report the test type and tails beside the p-value so readers can reproduce it.
- Compare the p-value with the significance level in a labeled cell, not a hard-coded number.

## Related Functions

| Function | Relationship |
| --- | --- |
| [F.TEST](F.TEST.md) | Tests whether two samples have different variances, which helps choose the test type. |
| [T.DIST.2T](T.DIST.2T.md) | Returns the two-tailed probability for a t-statistic you calculate yourself. |
| [T.INV.2T](T.INV.2T.md) | Returns the two-tailed critical value that a test statistic is compared against. |
| [TTEST](TTEST.md) | Older name for this function that returns the same p-value. |
| [Z.TEST](Z.TEST.md) | Tests a sample mean against a known population mean when the population spread is known. |

## Official Documentation

- [Microsoft Support: T.TEST function](https://support.microsoft.com/en-us/excel/functions/t-test-function)
- [Google Docs Editors Help: T.TEST](https://support.google.com/docs/answer/6055837)
