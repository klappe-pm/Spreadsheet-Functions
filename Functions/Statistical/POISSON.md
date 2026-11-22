---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Probability
use-case:
  - Arrival Rates
  - Call Volume Planning
  - Defect Counts
related:
  - BINOM.DIST
  - FACT
  - NORM.DIST
  - POISSON.DIST
  - PROB
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/poisson-function
  - https://support.google.com/docs/answer/3094097
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Poisson Probability
tags:
  - compatibility
  - distribution
  - excel
  - probability
  - sheets
---

# POISSON

## Description

**POISSON** returns the probability of a given number of events in a fixed interval when events happen independently at a steady average rate. Use it to estimate how likely a count of calls, arrivals, defects or failures is, based on the average count you expect in that same interval.

POISSON is the earlier name for POISSON.DIST and performs the same calculation. Microsoft Excel keeps it for backward compatibility and warns that it may not be available in future versions, so use POISSON.DIST in new workbooks. Google Sheets accepts both names. Use the same time unit for the average and the count, for example calls per minute with a one-minute interval, or the average must be converted first.

## Syntax

```excel
=POISSON(x, mean, cumulative)
```

<!-- Image 1: POISSON Syntax Anatomy. See Images/Statistical/POISSON.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The number of events to test. Values of zero or more are accepted; a non-integer is truncated to a whole number. |
| `mean` | Yes | The expected number of events in the interval. Must be zero or more. |
| `cumulative` | Yes | `TRUE` returns the probability of zero to `x` events, inclusive. `FALSE` returns the probability of exactly `x` events. |

### Return Value

A probability from 0 to 1. The function returns `#VALUE!` when `x` or `mean` is not a number and `#NUM!` when either one is negative.

## Examples

### Example 1: Probability of Exactly Three Events

```excel
=POISSON(3, 2, FALSE)
```

**Result:** `0.180447`

With an average of 2 events, the chance of exactly 3 is about 18 percent.

### Example 2: Probability of Three or Fewer Events

```excel
=POISSON(3, 2, TRUE)
```

**Result:** `0.857123`

Setting `cumulative` to `TRUE` adds the probabilities of 0, 1, 2 and 3 events.

<!-- Image 2: Exact Versus Cumulative Results. See Images/Statistical/POISSON.md -->

### Example 3: Rounded Result With Error Handling

Inputs in `A2` (events) and `B2` (mean): `3` and `2`.

```excel
=IFERROR(ROUND(POISSON(A2, B2, TRUE), 4), "Check inputs")
```

**Result:** `0.8571`

ROUND keeps four decimal places, and IFERROR shows a message if an input is negative or not a number.

### Example 4: Non-Integer Event Count

```excel
=POISSON(2.9, 2, FALSE)
```

**Result:** `0.270671`

The value 2.9 is truncated to 2, so the function returns the probability of exactly 2 events.

## Story Problems

### Problem 1: Help Desk Calls in One Minute

A help desk receives calls at a steady average rate. The team wants to know how likely exactly four calls are in a single minute.

| Input | Value |
| --- | --- |
| Average calls per minute (mean) | 6 |
| Calls to test (x) | 4 |

**Task:** Enter the mean in `B1` and the call count in `B2`, then find the probability of exactly four calls.

**Solution:**

```excel
=POISSON(B2, B1, FALSE)
```

**Answer:** `0.133853`, about a 13 percent chance. Four calls is a plausible count, but it is less likely than the average of six.

### Problem 2: Defects in a Sample Batch

A factory averages 1.5 defects per batch. A batch with more than two defects triggers an inspection, so the quality lead wants the probability of two or fewer.

| Input | Value |
| --- | --- |
| Average defects per batch (mean) | 1.5 |
| Largest count without inspection (x) | 2 |

**Task:** Use the cumulative form to find the probability of at most two defects.

**Solution:**

```excel
=POISSON(B2, B1, TRUE)
```

**Answer:** `0.808847`. About 81 percent of batches have two or fewer defects, so about 19 percent trigger an inspection.

## Use Cases

### Help Desk Staffing

**Scenario:** A support manager wants to know how likely a queue is to receive more than a set number of calls in a minute, using the average from last quarter.

```excel
=1-POISSON(A2, $B$1, TRUE)
```

**Why It Works:** The cumulative form gives the probability of at most `A2` calls, and subtracting it from 1 gives the probability of more than `A2`. Keep the mean in the same time unit as the interval.

### Defect Count Review

**Scenario:** A quality engineer checks how unusual a batch's defect count is compared with the historical average.

```excel
=POISSON(A2, $B$1, FALSE)
```

**Why It Works:** The formula returns the probability of exactly the observed count. A very small result flags the batch for a closer look, but it does not prove a process problem on its own.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `x` or `mean` is text, blank or a range. | Pass single numeric cells or numbers. |
| `#NUM!` | `x` or `mean` is below zero. | Check the inputs and remove negative values. |
| Unexpectedly small result | `cumulative` is `FALSE` when the question asks for "at most". | Use `TRUE` for "zero to x" questions. |
| Wrong probability | The mean is per hour but the interval is per minute. | Convert the mean to the same interval as `x`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Compatibility function in Excel 2016, 2019, 2021, 2024 and Microsoft 365 | Replaced by POISSON.DIST, which Microsoft recommends for new work. |
| Google Sheets | Available | Accepts POISSON and POISSON.DIST; the documentation covers both names together. |

## Tips and Best Practices

- Use POISSON.DIST in new workbooks and keep POISSON only in files that already depend on it.
- Make sure the mean and the interval describe the same period before you calculate.
- Use `TRUE` for "at most" questions and `FALSE` for "exactly" questions.
- Check the result against a total of 1 by summing the exact probabilities over every count you care about.

## Related Functions

| Function | Relationship |
| --- | --- |
| [POISSON.DIST](POISSON.DIST.md) | The current name for the same calculation. |
| [PROB](PROB.md) | Probability that values fall between limits, when you supply the probabilities. |
| [BINOM.DIST](BINOM.DIST.md) | Successes in a fixed number of trials, not events in a time interval. |
| [NORM.DIST](NORM.DIST.md) | A continuous approximation that is often used when the mean is large. |
| [FACT](../Math%20%26%20Trig/FACT.md) | The factorial in the Poisson formula, calculated separately. |

## Official Documentation

- [Microsoft Support: POISSON function](https://support.microsoft.com/en-us/excel/functions/poisson-function)
- [Google Docs Editors Help: POISSON and POISSON.DIST](https://support.google.com/docs/answer/3094097)
