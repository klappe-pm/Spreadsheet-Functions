---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Logarithms and Powers
purpose:
  - Arithmetic Operations
use-case:
  - Doubling Count
  - Order of Magnitude Comparison
related:
  - EXP
  - LN
  - LOG10
  - POWER
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/log-function
  - https://support.google.com/docs/answer/3093495
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Logarithm With Base
tags:
  - excel
  - logarithm
  - sheets
---

# LOG

## Description

**LOG** returns the logarithm of a positive number to a base you choose. If the base is omitted, it defaults to 10, so LOG(100) returns 2 because 10 raised to the power 2 is 100. With a base argument, LOG(8,2) returns 3, because 2 raised to the power 3 is 8.

Use LOG when a question asks how many times a base must be multiplied to reach a value. For example, LOG(1600/200,2) returns 3, which means a count starts at 200 and doubles three times to reach 1,600. For the natural logarithm with base e, use LN. For base 10 specifically, LOG10 is a dedicated function with the same result as LOG with its default base.

The number argument must be positive. The official pages describe it that way, but they do not describe the result or error for zero or negative numbers, and they do not describe a zero or negative base. Validate those inputs before the call.

## Syntax

```excel
=LOG(number, [base])
```

<!-- Image 1: Number and Base Arguments. See Images/Math & Trig/LOG.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The positive real number whose logarithm you want. In Sheets, this argument is named `value`. |
| `base` | No | The base of the logarithm. If omitted, the base is 10. |

### Return Value

A number: the logarithm of `number` to the given `base`. Results with many decimal places may show small rounding differences, so round the result when it is used in a comparison.

## Examples

### Example 1: Default Base 10

```excel
=LOG(100)
```

**Result:** `2`

Ten raised to the power 2 is 100.

### Example 2: Base 2

```excel
=LOG(8,2)
```

**Result:** `3`

Two raised to the power 3 is 8.

### Example 3: Base 10 for a Large Number

```excel
=LOG(45000)
```

**Result:** `4.653213`

Displayed to six decimal places. The result shows that 45,000 lies between 10 to the power 4 and 10 to the power 5.

<!-- Image 2: Counting Doublings. See Images/Math & Trig/LOG.md -->

### Example 4: Counting Doublings

With 200 in `A2` and 1600 in `A3`:

```excel
=LOG(A3/A2,2)
```

**Result:** `3`

The ratio 1600 divided by 200 is 8, and LOG to base 2 of 8 is 3. The count doubles 200 to 400, then 800, then 1,600.

## Story Problems

### Problem 1: Doublings in a Customer Base

A subscription service had 200 users at the start of a campaign and 1,600 users at the end. The growth team wants to know how many doublings that represents.

| Point | Users |
| --- | --- |
| Start | 200 |
| End | 1600 |

**Task:** Count the number of times the starting user base doubled to reach the ending count.

**Solution:**

```excel
=LOG(B3/B2,2)
```

**Answer:** `3`. The base doubled from 200 to 400, from 400 to 800, and from 800 to 1,600.

### Problem 2: Order of Magnitude of Annual Sales

A retailer reports annual sales of 45,000 units and wants to know its order of magnitude, meaning the power of 10 closest to the value.

| Measure | Value |
| --- | --- |
| Annual sales (units) | 45000 |

**Task:** Calculate the base-10 logarithm of the sales figure, then find the whole-number power of 10 below it.

**Solution:**

```excel
=ROUNDDOWN(LOG(B2),0)
```

**Answer:** `4`. The logarithm is 4.65, so the sales figure lies between 10 to the power 4 and 10 to the power 5.

## Use Cases

### Doubling Count

**Scenario:** A marketing analyst counts how many times a metric doubled between two dates, such as a campaign that grew from 200 to 1,600 sign-ups.

```excel
=LOG(B3/B2,2)
```

**Why It Works:** The formula uses base 2 so that each whole-number result is one doubling. The result is exact only when the ratio is a power of 2, so round the result for growth that does not double exactly.

### Order of Magnitude Comparison

**Scenario:** A data team compares datasets of very different sizes and groups each one by its power of 10.

```excel
=ROUNDDOWN(LOG(B2),0)
```

**Why It Works:** LOG with the default base 10 gives the exponent, and ROUNDDOWN keeps the whole-number part. A result of 4 places the dataset between 10,000 and 100,000.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected result | The base is omitted, so the base is 10, not 2 or e. | Pass the base explicitly, or use LN or LOG10 when the base is fixed. |
| Error or wrong result | The number or base is zero or negative, which is outside the documented input. | Validate the source values with IF before calling LOG. |
| `#VALUE!` | An argument is text rather than a number. | Convert the value to a number or correct the cell reference. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Base defaults to 10. The page requires a positive number. |
| Google Sheets | Available | Base defaults to 10. The argument is named `value` and must be positive. |

## Tips and Best Practices

- Pass the base explicitly in every formula so that a reader does not assume base 10.
- Use LOG with base 2 to count doublings, and with base 10 to compare orders of magnitude.
- Round results that feed a comparison, because logarithms of exact powers can show tiny rounding differences.
- Use LN when the natural logarithm is the intended quantity, since LN is the matching function for growth-rate formulas.

## Related Functions

| Function | Relationship |
| --- | --- |
| [EXP](EXP.md) | Raises e to a power, the inverse of LN. |
| [LN](LN.md) | Returns the natural logarithm, base e. |
| [LOG10](LOG10.md) | Returns the base-10 logarithm with no base argument. |
| [POWER](POWER.md) | Raises a number to a power, the reverse of a logarithm. |

## Official Documentation

- [Microsoft Support: LOG function](https://support.microsoft.com/en-us/excel/functions/log-function)
- [Google Docs Editors Help: LOG](https://support.google.com/docs/answer/3093495)
