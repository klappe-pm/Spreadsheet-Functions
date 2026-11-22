---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Hypothesis Testing
  - Statistical Analysis
use-case:
  - Campaign Response Comparison
  - Training Effectiveness Review
  - Warehouse Process Comparison
related:
  - CHITEST
  - FTEST
  - T.DIST
  - T.TEST
  - TDIST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/ttest-function
  - https://support.google.com/docs/answer/6055837
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Student T Test
tags:
  - compatibility
  - excel
  - hypothesis-testing
  - p-value
  - sheets
  - t-test
---

# TTEST

## Description

**TTEST** returns the probability associated with a Student's t-test. You give it two data sets and it tells you how likely a difference between their means is if the two groups actually share the same average. A small result, such as 0.05 or lower, suggests the difference is unlikely to be chance alone.

The function runs three kinds of test, chosen by the `type` argument: a paired test for matched observations such as before and after readings on the same people, a two-sample test that assumes equal variances, and a two-sample test that allows unequal variances. The `tails` argument picks a one-tailed or two-tailed result. Use a one-tailed test only when you decided before seeing the data which direction you expect the difference to take.

TTEST is a legacy compatibility function. Microsoft states that it has been replaced by T.TEST, which takes the same four arguments with clearer names. TTEST remains available so older workbooks keep working, but it may not exist in future versions of Excel. For new work, use T.TEST.

## Syntax

```excel
=TTEST(array1,array2,tails,type)
```

<!-- Image 1: Two Samples and the Test Settings. See Images/Statistical/TTEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first data set, such as `A2:A9`. |
| `array2` | Yes | The second data set. For a paired test it must contain the same number of values as `array1`. |
| `tails` | Yes | 1 for a one-tailed test or 2 for a two-tailed test. Other values return `#NUM!`. |
| `type` | Yes | 1 for a paired test, 2 for a two-sample test with equal variances, or 3 for a two-sample test with unequal variances. |

### Return Value

A probability from 0 to 1. The two-tailed result is double the one-tailed result. The function returns `#N/A` when a paired test (`type` 1) receives data sets with different numbers of values, `#VALUE!` when `tails` or `type` is not numeric, and `#NUM!` when `tails` is not 1 or 2.

## Examples

All examples use two samples of eight measurements, with a header row in row 1. Sample A is in `A2:A9` and sample B is in `B2:B9`.

| Sample A | Sample B |
| --- | --- |
| 18.2 | 17.1 |
| 20.1 | 18.5 |
| 19.4 | 17.9 |
| 21.0 | 19.6 |
| 17.8 | 16.8 |
| 19.9 | 18.0 |
| 20.6 | 18.9 |
| 18.7 | 17.4 |

The mean of sample A is 19.46 and the mean of sample B is 18.03.

### Example 1: Two-Tailed Test With Equal Variances

```excel
=TTEST(A2:A9,B2:B9,2,2)
```

**Result:** `0.0160`

The two-sample test with equal variances and two tails returns 0.0160. The difference of about 1.44 between the means is unlikely to be chance at the 5 percent level.

### Example 2: One-Tailed Test

```excel
=TTEST(A2:A9,B2:B9,1,2)
```

**Result:** `0.0080`

The one-tailed result is half of the two-tailed result in Example 1. Use it only when the direction of the difference was fixed before the data was collected.

### Example 3: Two-Sample Test With Unequal Variances

```excel
=TTEST(A2:A9,B2:B9,2,3)
```

**Result:** `0.0164`

Type 3 does not assume the two samples have the same spread. Here the result is close to Example 1, because the two samples have similar variances.

### Example 4: Paired Test

```excel
=TTEST(A2:A9,B2:B9,2,1)
```

**Result:** `0.0000029`

A paired test treats each row as one matched pair and tests the differences. Every pair in this data shows sample A higher by 1.0 to 1.9, so the paired result is far smaller than the two-sample results.

### Example 5: The Replacement Function

```excel
=T.TEST(A2:A9,B2:B9,2,2)
```

**Result:** `0.0160`

T.TEST takes the same arguments as TTEST and returns the same value. Use it in new formulas and keep TTEST only in workbooks that already rely on it.

## Story Problems

### Problem 1: Warehouse Pick Times

Two warehouse teams record the minutes each took to pick one order. Team A's seven records are in `A2:A8`, and Team B's seven records are in `B2:B8`. The operations manager wants to know whether the average pick time differs between the teams at the 5 percent level.

| Order | Team A | Team B |
| --- | --- | --- |
| 1 | 6.4 | 7.8 |
| 2 | 7.1 | 8.3 |
| 3 | 5.8 | 7.0 |
| 4 | 6.9 | 8.6 |
| 5 | 7.4 | 7.9 |
| 6 | 6.2 | 8.1 |
| 7 | 6.7 | 7.5 |

**Task:** Compute the two-tailed p-value for two independent samples with equal variances.

**Solution:**

```excel
=TTEST(A2:A8,B2:B8,2,2)
```

**Answer:** `0.0010`. The result is below 0.05, so the difference in average pick time is statistically significant. Team A averages 6.64 minutes and Team B averages 7.89 minutes.

### Problem 2: Training Effect on Quiz Scores

A trainer gives the same six employees a quiz before and after a training course. The before scores are in `B2:B7` and the after scores are in `C2:C7`. Each row is one employee, so the test must be paired.

| Employee | Before | After |
| --- | --- | --- |
| E1 | 61 | 68 |
| E2 | 58 | 63 |
| E3 | 70 | 75 |
| E4 | 66 | 70 |
| E5 | 74 | 79 |
| E6 | 69 | 72 |

**Task:** Compute the two-tailed p-value for the matched before and after scores.

**Solution:**

```excel
=TTEST(B2:B7,C2:C7,2,1)
```

**Answer:** `0.0003`. Every employee improved, by between 3 and 7 points, with an average gain of 4.83 points. The small p-value shows the gain is very unlikely to be chance.

<!-- Image 2: Two-Sample and Paired Results. See Images/Statistical/TTEST.md -->

## Use Cases

### Warehouse Process Comparison

**Scenario:** A site manager wants to know whether a new picking layout actually speeds up order picking compared with the old layout.

```excel
=TTEST(OldLayout,NewLayout,2,3)
```

**Why It Works:** Type 3 allows the two layouts to have different spreads, which is a safer default when the teams work in different zones. Check the p-value against the threshold agreed before the trial.

### Training Effectiveness Review

**Scenario:** An HR team compares quiz scores for the same staff before and after a course.

```excel
=TTEST(PreScores,PostScores,1,1)
```

**Why It Works:** A paired test removes the variation between people, so it detects smaller gains than a two-sample test would. Use a one-tailed test only when a gain was the only outcome the course could produce.

### Campaign Response Comparison

**Scenario:** A marketing analyst compares daily click-through rates for two email subject lines sent to matched audiences.

```excel
=TTEST(SubjectA,SubjectB,2,2)
```

**Why It Works:** The two-sample test compares the averages of the two groups. Make sure each group has enough days of data, because very small samples make the p-value unreliable.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | A paired test (`type` 1) receives data sets with different numbers of values. | Make both ranges the same length, with each row forming one pair. |
| `#NUM!` | `tails` is a number other than 1 or 2. | Enter 1 or 2 for `tails`. |
| `#VALUE!` | `tails` or `type` is not a number. | Enter the numbers directly or reference cells that contain them. |
| Misleading p-value | The wrong `type` was used, so the test assumes the wrong kind of relationship. | Choose type 1 for matched pairs, type 2 when spreads look similar, and type 3 when they differ. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions | Legacy compatibility function. Microsoft recommends T.TEST, and TTEST may be removed from future versions. |
| Google Sheets | Available as an alias | The Sheets help page for TTEST refers to T.TEST, which takes the same arguments. The T.TEST page documents `#DIV/0!` when the variances of both ranges are zero. |

## Tips and Best Practices

- Write new formulas with T.TEST, and keep TTEST only in existing workbooks.
- Choose the test type before looking at the results, so the choice does not depend on which answer you want.
- Use the two-tailed result unless the direction of the effect was fixed in advance.
- Keep the two data sets in the same order when the test is paired, so each row stays with its matching partner.
- Check the sample sizes. Small samples give unstable p-values even when the means look clearly different.
- Report the p-value together with the two means so readers can judge the size of the difference.

## Related Functions

| Function | Relationship |
| --- | --- |
| [T.TEST](T.TEST.md) | Modern replacement with the same arguments and result. |
| [T.DIST](T.DIST.md) | Returns the t-distribution probability for a given t value. |
| [TDIST](TDIST.md) | Legacy t-distribution function that returns the same kind of probability. |
| [FTEST](FTEST.md) | Compares the variances of two data sets, which helps choose the test type. |
| [CHITEST](CHITEST.md) | Tests independence in a table of observed and expected counts. |

## Official Documentation

- [Microsoft Support: TTEST function](https://support.microsoft.com/en-us/excel/functions/ttest-function)
- [Google Docs Editors Help: TTEST](https://support.google.com/docs/answer/6055837)
