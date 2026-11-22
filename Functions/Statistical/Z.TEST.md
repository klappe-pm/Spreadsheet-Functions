---
domain: Spreadsheet Functions
category: Statistical
subcategory: Hypothesis Tests
purpose:
  - Hypothesis Testing
  - Statistical Analysis
use-case:
  - Call Volume Targets
  - Delivery Time Benchmarks
  - Process Mean Checks
related:
  - AVERAGE
  - CONFIDENCE.NORM
  - NORM.S.DIST
  - STDEV.S
  - T.TEST
  - ZTEST
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/z-test-function
  - https://support.google.com/docs/answer/3094067
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - One Tailed Z Test
  - Z Test P-Value
tags:
  - excel
  - hypothesis-testing
  - sheets
  - statistics
---

# Z.TEST

## Description

**Z.TEST** returns the one-tailed P-value of a z-test. It tests whether a sample mean could plausibly come from a population with a hypothesized mean. The result is the probability of seeing a sample mean as large as the observed average if the true population mean equals the value you test against. A small result, such as below 0.05, is evidence that the population mean is greater than the value you tested.

The function uses the sample mean and the standard error of the mean. If you supply the population standard deviation as the optional `sigma` argument, Z.TEST uses it. If you leave `sigma` out, Z.TEST uses the sample standard deviation computed from the data. Use a z-test when the population standard deviation is known or the sample is large. For small samples with an unknown standard deviation, T.TEST is the usual choice.

Z.TEST returns a one-tailed value only. For a two-tailed test, double the smaller of the one-tailed result and 1 minus that result. Z.TEST replaces the older ZTEST function, which returns the same results.

## Syntax

```excel
=Z.TEST(array, x, [sigma])
```

<!-- Image 1: Syntax Arguments on a Worksheet. See Images/Statistical/Z.TEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array of data to test. Empty ranges return `#N/A`. |
| `x` | Yes | The hypothesized population mean, the value you test the sample mean against. |
| `sigma` | No | The known population standard deviation. When omitted, the sample standard deviation of `array` is used. |

### Return Value

A number from 0 to 1: the one-tailed P-value. The function returns `#N/A` when `array` is empty. Google Sheets names the same arguments `data`, `value` and `standard_deviation`.

## Examples

All examples use 10 daily call counts in `B2:B11`: 12, 15, 9, 14, 11, 13, 10, 16, 12 and 14. Their mean is 12.6.

### Example 1: One-Tailed Test Against 11

```excel
=Z.TEST(B2:B11, 11)
```

**Result:** `0.011364`

With the sample standard deviation, the one-tailed P-value is about 0.011, so a mean of 11 is unlikely to be the true average.

<!-- Image 2: Tail Areas for One-Tailed and Two-Tailed Tests. See Images/Statistical/Z.TEST.md -->

### Example 2: Two-Tailed Test Against 11

```excel
=2*MIN(Z.TEST(B2:B11, 11), 1-Z.TEST(B2:B11, 11))
```

**Result:** `0.022728`

Doubling the smaller tail gives the two-tailed P-value, which tests for a difference in either direction.

### Example 3: Known Population Standard Deviation

```excel
=Z.TEST(B2:B11, 11, 2)
```

**Result:** `0.005706`

Supplying `sigma` of 2 replaces the sample standard deviation, which changes the standard error and makes the result smaller.

### Example 4: Testing Against the Observed Mean

```excel
=Z.TEST(B2:B11, 12)
```

**Result:** `0.196485`

The sample mean is 12.6, so testing against 12 gives a larger P-value. The data gives weak evidence that the true mean is above 12.

## Story Problems

### Problem 1: Delivery Times Against a Promise

A courier company promises an average delivery time of 40 minutes. A dispatcher records the times for 8 deliveries in `B2:B9`: 42, 38, 47, 45, 40, 44, 39 and 46 minutes. The dispatcher wants to know whether the true average is above 40.

| Delivery | Minutes |
| --- | --- |
| 1 | 42 |
| 2 | 38 |
| 3 | 47 |
| 4 | 45 |
| 5 | 40 |
| 6 | 44 |
| 7 | 39 |
| 8 | 46 |

**Task:** Find the one-tailed P-value for a hypothesized mean of 40 minutes, using the sample standard deviation.

**Solution:**

```excel
=Z.TEST(B2:B9, 40)
```

**Answer:** `0.013976`. The sample mean is 42.625 minutes, so the evidence that deliveries take longer than 40 minutes is strong at the 0.05 level.

### Problem 2: Same Data With a Known Spread

The courier knows from years of records that the standard deviation of delivery times is 3 minutes. The same 8 deliveries in `B2:B9` are tested against 40 minutes.

**Task:** Repeat the test using the known standard deviation of 3 as the optional argument.

**Solution:**

```excel
=Z.TEST(B2:B9, 40, 3)
```

**Answer:** `0.006664`. The known spread makes the standard error smaller than the sample estimate, so the P-value is lower.

<!-- Image 3: Results for the Delivery Times Story. See Images/Statistical/Z.TEST.md -->

## Use Cases

### Process Mean Checks

**Scenario:** A quality engineer checks whether a filling line still averages 500 milliliters, using a known standard deviation of 4 milliliters.

```excel
=IF(Z.TEST(FillSamples, 500, 4)<0.05, "Investigate", "On Target")
```

**Why It Works:** The formula flags the line only when the evidence is strong. Because the test is one-tailed, it detects a mean above the target; for a shift in either direction, double the P-value first.

### Benchmark Comparison

**Scenario:** A training team compares the average score of a new class with a published benchmark of 70.

```excel
=Z.TEST(ClassScores, 70)
```

**Why It Works:** A small result suggests the class mean is above the benchmark. Keep the sample size in mind, because a z-test with few scores is less reliable.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The `array` argument is empty. | Check that the range contains numbers. |
| Result differs from a two-tailed test | The function returns a one-tailed value only. | Double the smaller tail for a two-tailed test. |
| Wrong direction | The hypothesized mean is on the wrong side of the sample mean. | Compare the result with the sample average to confirm the direction. |
| Unexpected change after new data | `sigma` was left out, so the sample standard deviation changed. | Supply a fixed `sigma` when the population value is known. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available; Microsoft's help page gives no version limit | Arguments are `array`, `x` and `sigma`. |
| Google Sheets | Available | Arguments are `data`, `value` and `standard_deviation`. The value of `standard_deviation` defaults to `STDEV(data)`. |

## Tips and Best Practices

- Check the sample size first; a z-test with a known population standard deviation is more dependable than one that estimates the spread from a few values.
- State the hypothesis before running the test so the tail choice is not made after seeing the result.
- Keep the hypothesized mean in a labeled cell so the test is easy to repeat.
- Pair the P-value with the sample mean and the difference from the target so readers see the size of the effect.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Returns the sample mean that Z.TEST compares with the hypothesized value. |
| [CONFIDENCE.NORM](CONFIDENCE.NORM.md) | Returns the margin of error for a normal confidence interval. |
| [NORM.S.DIST](NORM.S.DIST.md) | Returns the standard normal probability used inside the calculation. |
| [STDEV.S](STDEV.S.md) | Returns the sample standard deviation that Z.TEST uses when `sigma` is omitted. |
| [T.TEST](T.TEST.md) | Use instead when the population standard deviation is unknown and the sample is small. |
| [ZTEST](ZTEST.md) | Older name for the same test, kept for compatibility. |

## Official Documentation

- [Microsoft Support: Z.TEST function](https://support.microsoft.com/en-us/excel/functions/z-test-function)
- [Google Docs Editors Help: Z.TEST](https://support.google.com/docs/answer/3094067)
