---
domain: Spreadsheet Functions
category: Statistical
subcategory: Hypothesis Tests
purpose:
  - Hypothesis Testing
use-case:
  - Pilot Program Review
  - Queue Performance Review
  - Variance Equality Check
related:
  - F.DIST
  - F.DIST.RT
  - FTEST
  - T.TEST
  - TTEST
  - VAR.S
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/f-test-function
  - https://support.google.com/docs/answer/7004183
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Variance Equality Test
tags:
  - excel
  - hypothesis-testing
  - sheets
  - variance
---

# F.TEST

## Description

**F.TEST** compares the variances of two samples and returns a two-tailed probability. The result is the probability that the two variances are not significantly different. A small result, usually below 0.05, suggests the spreads of the two samples really differ.

The function reads the two ranges directly, so you do not need to calculate the variances first. It uses the sample variance of each range, and the ratio of those variances drives the result.

Run F.TEST before a two-sample t test. If the variances differ, the equal-variance t test is not appropriate, and T.TEST with type 3 (unequal variances) is the better choice. The test is only a guide, so look at the data as well as the p-value.

Google Sheets documents FTEST as the same function under its older name.

## Syntax

```excel
=F.TEST(array1, array2)
```

<!-- Image 1: Two Sample Ranges Compared by F.TEST. See Images/Statistical/F.TEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first range or array of numbers. Text, logical values and empty cells are ignored. |
| `array2` | Yes | The second range or array of numbers. Text, logical values and empty cells are ignored. |

### Return Value

A two-tailed probability from 0 to 1. Each range needs at least two numeric values, and each must have a nonzero variance. Excel returns `#DIV/0!` when either range has fewer than two data points or when either variance is zero.

## Examples

Examples 1 and 2 use these values: `A2:A6` holds 12.1, 13.4, 11.8, 14.0 and 12.7, and `B2:B6` holds 10.2, 11.5, 13.9, 9.8 and 12.6.

### Example 1: Two-Tailed Variance Test

```excel
=F.TEST(A2:A6, B2:B6)
```

**Result:** `0.2540` (rounded to four decimal places)

The probability is well above 0.05, so the two spreads do not differ significantly on this small sample.

### Example 2: Flagging the Result

```excel
=IF(F.TEST(A2:A6, B2:B6)<0.05, "Variances differ", "No evidence of a difference")
```

**Result:** `No evidence of a difference`

The IF wrapper turns the probability into a label. Keep the raw p-value next to the label so readers can see how close the result is to the threshold.

### Example 3: Identical Ranges

```excel
=F.TEST(A2:A6, A2:A6)
```

**Result:** `1`

When both ranges are the same, the variance ratio is exactly 1, so the two-tailed probability is 1. This is a quick check that the ranges are being read correctly.

<!-- Image 2: Variance Test Result and Threshold. See Images/Statistical/F.TEST.md -->

## Story Problems

### Problem 1: Pilot Delivery Times

A courier company tests a new route plan. Pilot A and Pilot B each record the delivery time in minutes on five days. The team wants to know whether the two pilots show different variability before it compares their averages.

| Day | Pilot A | Pilot B |
| --- | --- | --- |
| 1 | 31 | 30 |
| 2 | 35 | 38 |
| 3 | 33 | 41 |
| 4 | 36 | 29 |
| 5 | 34 | 40 |

**Task:** Find the two-tailed probability that the variances are not significantly different, using `B2:B6` for Pilot A and `C2:C6` for Pilot B.

**Solution:**

```excel
=F.TEST(B2:B6, C2:C6)
```

**Answer:** `0.0590`. Pilot B is far more variable, but 0.0590 is above 0.05, so the result is not significant at the 5 percent level. A larger sample would give a clearer answer.

### Problem 2: Queue Wait Times

A support center compares the wait times in two queues. Queue A has steady waits and Queue B has more spread. Each queue has five readings in minutes.

| Reading | Queue A | Queue B |
| --- | --- | --- |
| 1 | 4 | 2 |
| 2 | 5 | 9 |
| 3 | 6 | 3 |
| 4 | 5 | 8 |
| 5 | 4 | 7 |

**Task:** Find the two-tailed probability for the two queues, using `B2:B6` and `C2:C6`.

**Solution:**

```excel
=F.TEST(B2:B6, C2:C6)
```

**Answer:** `0.0260`. Because 0.0260 is below 0.05, the variances of the two queues differ, so the manager should not treat the queues as equally predictable.

## Use Cases

### Choosing a T Test Type

**Scenario:** A researcher compares two groups and wants the t test to match the variance result.

```excel
=T.TEST(A2:A11, B2:B11, 2, IF(F.TEST(A2:A11, B2:B11)<0.05, 3, 2))
```

**Why It Works:** When the variances differ, the formula uses type 3, the unequal-variance t test. Otherwise it uses type 2, the equal-variance test. The choice is made in the same formula, so the result follows the data.

### Pilot Program Review

**Scenario:** An operations team decides whether a pilot has made performance more consistent before it rolls the change out to every site.

```excel
=IF(F.TEST(PilotA, PilotB)<0.05, "Spread changed", "No clear change")
```

**Why It Works:** Named ranges make the review formula easy to audit. A "No clear change" result with a small sample means more data is needed, not that the pilot had no effect.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | A range has fewer than two numeric values. | Add more data or check for missing entries. |
| `#DIV/0!` | A range has zero variance because every value is the same. | Check the data for repeated values or a broken import. |
| Unexpected result | One range has blank cells, so the ranges contain different counts. | Confirm each range holds the expected number of values. |
| Unexpected result | Numbers were stored as text and were ignored. | Convert the text to numbers before running the test. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in current Excel, including Excel for the web | Returns `#DIV/0!` when a range has fewer than two data points or zero variance. |
| Google Sheets | Available | FTEST is the same function under the older name. Non-numeric cells in either range are ignored. |

## Tips and Best Practices

- Check the variances with VAR.S before you read the p-value, so you can see which sample is more spread out.
- Use the same number of observations in each range when you can, because unequal counts make the result harder to interpret.
- Treat a p-value close to 0.05 as a sign to collect more data, not as a final answer.
- Run F.TEST before choosing the t test type, so the two-sample analysis matches the variance assumption.

## Related Functions

| Function | Relationship |
| --- | --- |
| [F.DIST](F.DIST.md) | Returns the probability for a variance ratio you calculated yourself. |
| [F.DIST.RT](F.DIST.RT.md) | Returns the right-tail p-value for a given ratio, one part of the two-tailed result. |
| [FTEST](FTEST.md) | The legacy name for the same variance test. |
| [T.TEST](T.TEST.md) | Compares means with a choice of equal or unequal variances. |
| [TTEST](TTEST.md) | The legacy name for the t test. |
| [VAR.S](VAR.S.md) | Calculates the sample variance for each range. |

## Official Documentation

- [Microsoft Support: F.TEST function](https://support.microsoft.com/en-us/excel/functions/f-test-function)
- [Google Docs Editors Help: F.TEST](https://support.google.com/docs/answer/7004183)
