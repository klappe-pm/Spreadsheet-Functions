---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
purpose:
  - Probability
use-case:
  - Arrival Rates
  - Event Probability
  - Server Error Monitoring
related:
  - BINOM.DIST
  - GAMMA.DIST
  - HYPGEOM.DIST
  - NORM.DIST
  - POISSON
  - PROB
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/poisson-dist-function
  - https://support.google.com/docs/answer/3094097
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Poisson Distribution
tags:
  - distribution
  - excel
  - probability
  - sheets
---

# POISSON.DIST

## Description

**POISSON.DIST** returns the Poisson probability for a count of events in a fixed interval, given the expected number of events (the mean) for that interval. It models events that happen independently at a steady average rate, such as arrivals at a counter, system errors or customer complaints.

The last argument chooses the form of the answer. `FALSE` returns the probability of exactly `x` events. `TRUE` returns the cumulative probability of zero to `x` events, which is the probability of "at most `x`". Subtract the cumulative result from 1 to get the probability of more than `x`.

POISSON.DIST replaces the older POISSON function in Excel, and Microsoft recommends it for new work. Google Sheets documents POISSON.DIST as the function to use and accepts POISSON as an alias. The mean and the interval must describe the same period, so convert a per-hour rate before you use it for a 10-minute window.

## Syntax

```excel
=POISSON.DIST(x, mean, cumulative)
```

<!-- Image 1: POISSON.DIST Syntax Anatomy. See Images/Statistical/POISSON.DIST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `x` | Yes | The number of events to test. Values of zero or more are accepted; a non-integer is truncated to a whole number. |
| `mean` | Yes | The expected number of events in the interval. Must be zero or more. |
| `cumulative` | Yes | `TRUE` returns the probability of zero to `x` events, inclusive. `FALSE` returns the probability of exactly `x` events. |

### Return Value

A probability from 0 to 1. The function returns `#VALUE!` when `x` or `mean` is not a number and `#NUM!` when `x` or `mean` is negative.

## Examples

### Example 1: Probability of Exactly Four Events

```excel
=POISSON.DIST(4, 2.5, FALSE)
```

**Result:** `0.133602`

With an average of 2.5 events, a count of exactly 4 has about a 13 percent chance.

### Example 2: Probability of Four or Fewer Events

```excel
=POISSON.DIST(4, 2.5, TRUE)
```

**Result:** `0.891178`

The cumulative result adds the probabilities of 0, 1, 2, 3 and 4 events.

<!-- Image 2: Exact Versus Cumulative Results. See Images/Statistical/POISSON.DIST.md -->

### Example 3: Probability of at Least One Event

```excel
=1-POISSON.DIST(0, 1.2, TRUE)
```

**Result:** `0.698806`

The probability of no events is subtracted from 1. This is the usual way to ask whether something happens at all in the interval.

### Example 4: Non-Integer Count

```excel
=POISSON.DIST(4.9, 2.5, FALSE)
```

**Result:** `0.133602`

The value 4.9 is truncated to 4, so the result matches Example 1.

## Story Problems

### Problem 1: Bakery Counter Gaps

A bakery counter gets an average of 3 customers every 10 minutes. The owner wants to know how likely a 10-minute window with no customers is.

| Input | Value |
| --- | --- |
| Average customers per 10 minutes (mean) | 3 |
| Customers to test (x) | 0 |

**Task:** Enter the mean in `B1` and the count in `B2`, then find the probability of zero customers in the window.

**Solution:**

```excel
=POISSON.DIST(B2, B1, FALSE)
```

**Answer:** `0.049787`, about a 5 percent chance. An empty 10-minute window is rare at this rate.

### Problem 2: Server Errors in a Day

A server logs an average of 0.8 errors per day. An on-call alert fires on more than two errors, so the team wants that probability.

| Input | Value |
| --- | --- |
| Average errors per day (mean) | 0.8 |
| Alert threshold (x) | 2 |

**Task:** Find the probability of more than two errors in one day.

**Solution:**

```excel
=1-POISSON.DIST(B2, B1, TRUE)
```

**Answer:** `0.047423`, about a 5 percent chance on any given day. The complement of the cumulative result gives "more than two" directly.

## Use Cases

### Arrival Rate Planning

**Scenario:** A clinic knows its average patient arrivals per hour and wants the chance of more than a set number of arrivals in a given hour.

```excel
=1-POISSON.DIST(A2, $B$1, TRUE)
```

**Why It Works:** `A2` holds the threshold count and `B1` holds the hourly mean. Both values must use the same one-hour interval.

### Complaint Monitoring

**Scenario:** A customer support lead checks whether a week with 9 complaints is unusual when the average is 5 per week.

```excel
=POISSON.DIST(A2, $B$1, FALSE)
```

**Why It Works:** The formula returns the probability of exactly the observed count. A small result suggests the week is unusual and worth reviewing, but it does not confirm a cause.

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
| Microsoft Excel | Excel 2016, 2019, 2021, 2024 and Microsoft 365, including Excel for the web | Replaces the older POISSON function. |
| Google Sheets | Available | Same arguments; POISSON is accepted as an alias. |

## Tips and Best Practices

- Use `TRUE` for "at most" questions and `FALSE` for "exactly" questions.
- Check that the mean and the interval describe the same period before you calculate.
- Use `1-` with the cumulative form to answer "more than" questions.
- Store the mean in a labeled cell so you can change the rate without rewriting the formula.

## Related Functions

| Function | Relationship |
| --- | --- |
| [POISSON](POISSON.md) | The older name for the same calculation, kept for compatibility. |
| [BINOM.DIST](BINOM.DIST.md) | Successes in a fixed number of trials, not events in a time interval. |
| [NORM.DIST](NORM.DIST.md) | A continuous approximation that is often used when the mean is large. |
| [GAMMA.DIST](GAMMA.DIST.md) | Waiting time until a set number of events occurs. |
| [HYPGEOM.DIST](HYPGEOM.DIST.md) | Successes in a sample drawn without replacement from a fixed population. |
| [PROB](PROB.md) | Probability that values fall between limits, when you supply the probabilities. |

## Official Documentation

- [Microsoft Support: POISSON.DIST function](https://support.microsoft.com/en-us/excel/functions/poisson-dist-function)
- [Google Docs Editors Help: POISSON and POISSON.DIST](https://support.google.com/docs/answer/3094097)
