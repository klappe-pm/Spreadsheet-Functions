---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Hypothesis Testing
  - Statistical Analysis
use-case:
  - Legacy Workbook Maintenance
  - Process Mean Checks
  - Test Score Benchmarks
related:
  - CONFIDENCE.NORM
  - NORM.S.DIST
  - STDEV.S
  - T.TEST
  - Z.TEST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/ztest-function
  - https://support.google.com/docs/answer/3094067
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Legacy Z Test
  - Z Test Compatibility
tags:
  - compatibility
  - excel
  - hypothesis-testing
  - sheets
---

# ZTEST

## Description

**ZTEST** returns the one-tailed probability value of a z-test. It answers the same question as Z.TEST: how likely is a sample mean at least as large as the observed average, if the population mean were the hypothesized value. The two functions use the same arithmetic and return the same result for the same inputs.

ZTEST is a compatibility function. Microsoft keeps it for backward compatibility and recommends Z.TEST for new work. Use ZTEST only when you need to keep an existing workbook working or when you read a formula written by someone who used the older name. For new formulas, write Z.TEST.

Google Sheets accepts ZTEST as an alias of Z.TEST, so a formula copied between the two products calculates the same result. The optional third argument works the same way: when it is omitted, the sample standard deviation is used.

## Syntax

```excel
=ZTEST(array, x, [sigma])
```

<!-- Image 1: Legacy and Modern Names Side by Side. See Images/Statistical/ZTEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array of data to test. An empty range returns `#N/A`. |
| `x` | Yes | The hypothesized population mean that the sample mean is compared with. |
| `sigma` | No | The known population standard deviation. When omitted, the sample standard deviation of `array` is used. |

### Return Value

A number from 0 to 1: the one-tailed probability value. The function returns `#N/A` when `array` is empty.

## Examples

All examples use 8 bag weights in grams in `B2:B9`: 505, 498, 502, 507, 500, 504, 499 and 503. Their mean is 502.25.

### Example 1: Sample Standard Deviation

```excel
=ZTEST(B2:B9, 500)
```

**Result:** `0.020212`

The sample standard deviation is about 3.11 grams, which sets the standard error used in the test.

### Example 2: Known Population Standard Deviation

```excel
=ZTEST(B2:B9, 500, 4)
```

**Result:** `0.055806`

Supplying a known standard deviation of 4 grams replaces the sample value and produces a larger P-value for the same target.

### Example 3: Same Result as Z.TEST

```excel
=Z.TEST(B2:B9, 500) - ZTEST(B2:B9, 500)
```

**Result:** `0`

Subtracting the two functions gives zero, which confirms that they return the same value for identical inputs.

## Story Problems

### Problem 1: Filling Line Check With a Known Spread

A plant has always used a standard deviation of 4 grams for its bag filling line. A supervisor records the 8 bags in `B2:B9` and wants to know whether the average weight is above a target of 502 grams.

| Bag | Weight (g) |
| --- | --- |
| 1 | 505 |
| 2 | 498 |
| 3 | 502 |
| 4 | 507 |
| 5 | 500 |
| 6 | 504 |
| 7 | 499 |
| 8 | 503 |

**Task:** Use the legacy function with the known standard deviation of 4 grams to test the target of 502.

**Solution:**

```excel
=ZTEST(B2:B9, 502, 4)
```

**Answer:** `0.429842`. The sample mean is 502.25 grams, only a quarter gram above the target, so the evidence of a shift is weak.

### Problem 2: Two-Tailed Check of an Inherited Formula

An inherited workbook uses ZTEST with the same bag data and a target of 500 grams. The team wants a two-tailed check, which means doubling the smaller tail.

**Task:** Write the two-tailed P-value for the target of 500 using the sample standard deviation.

**Solution:**

```excel
=2*MIN(ZTEST(B2:B9, 500), 1-ZTEST(B2:B9, 500))
```

**Answer:** `0.040424`. Because the value is below 0.05, the mean differs from 500 grams at the 5% level in either direction.

## Use Cases

### Legacy Workbook Maintenance

**Scenario:** A finance team inherits a model from several years ago that calls ZTEST in dozens of cells and must keep producing the same numbers.

```excel
=ZTEST(Scores, 70)
```

**Why It Works:** Leaving the old formula in place keeps every result unchanged. When the model is rebuilt, replacing the name with Z.TEST keeps the values the same.

### Process Mean Checks

**Scenario:** A production supervisor checks a process against a target with a known standard deviation.

```excel
=IF(ZTEST(FillSamples, 500, 4) < 0.05, "Investigate", "On Target")
```

**Why It Works:** The formula flags the process only when the P-value is below 0.05. The test is one-tailed, so it detects a mean above the target.

### Test Score Benchmarks

**Scenario:** A school compares a class average with a district benchmark of 75.

```excel
=ZTEST(ClassScores, 75)
```

**Why It Works:** A small result suggests the class mean is above the benchmark. With a small class, the result is less reliable, so check the sample size before drawing conclusions.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The `array` argument is empty. | Check that the range contains numbers. |
| Result differs from a two-tailed test | The function returns a one-tailed value only. | Double the smaller tail for a two-tailed test. |
| Unexpected result after a change | `sigma` was left out, so the sample standard deviation is used. | Supply a fixed `sigma` when the population value is known. |
| Formula not updated | The legacy name is kept in new work. | Use Z.TEST in new formulas and keep ZTEST only in existing ones. |

## Platform Differences

<!-- Image 2: Function Category in the Insert Function Dialog. See Images/Statistical/ZTEST.md -->

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in the Compatibility category | Microsoft recommends Z.TEST for new work. Results match Z.TEST. |
| Google Sheets | Available as an alias of Z.TEST | Behaves the same as Z.TEST with arguments `data`, `value` and `standard_deviation`. |

## Tips and Best Practices

- Use Z.TEST in new formulas and keep ZTEST in existing workbooks so older models still calculate.
- When you find ZTEST in an inherited file, search for every occurrence before renaming so no cell is missed.
- Store the hypothesized mean and the known standard deviation in labeled cells rather than typing them into each formula.
- Report the tail type next to the P-value so readers know whether it is one-tailed or two-tailed.

## Related Functions

| Function | Relationship |
| --- | --- |
| [Z.TEST](Z.TEST.md) | The modern replacement with the same calculation and a recommended name. |
| [CONFIDENCE.NORM](CONFIDENCE.NORM.md) | Returns the margin of error for a normal confidence interval. |
| [NORM.S.DIST](NORM.S.DIST.md) | Returns the standard normal probability used inside the calculation. |
| [STDEV.S](STDEV.S.md) | Returns the sample standard deviation used when `sigma` is omitted. |
| [T.TEST](T.TEST.md) | Use instead when the population standard deviation is unknown and the sample is small. |

## Official Documentation

- [Microsoft Support: ZTEST function](https://support.microsoft.com/en-us/excel/functions/ztest-function)
- [Google Docs Editors Help: Z.TEST](https://support.google.com/docs/answer/3094067)
