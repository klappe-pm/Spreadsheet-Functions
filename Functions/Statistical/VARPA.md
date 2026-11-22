---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
purpose:
  - Statistical Analysis
use-case:
  - Inspection Flag Variance
  - Population Pass Rate Spread
related:
  - STDEVPA
  - VAR.P
  - VARA
  - VARP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/varpa-function
  - https://support.google.com/docs/answer/3094065
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Population Variance With Logicals
tags:
  - excel
  - logical-values
  - population
  - sheets
  - variance
---

# VARPA

## Description

**VARPA** calculates the variance of a complete population and counts logical values in the same way as VARA. TRUE counts as 1 and FALSE counts as 0. The result divides the sum of squared deviations by the number of values, because every value you supply is treated as the entire group.

Use VARPA when the population includes yes or no results, such as pass or fail flags, that should affect the spread. Text behaves differently depending on how it is supplied. Inside a range or array, text is ignored. Text typed directly into the argument list is counted when it represents a number, and it causes an error when it cannot be converted to a number.

The official page does not describe VARPA as a legacy function or name a replacement. For population data without logical values, use VAR.P. For sample data with logical values, use VARA.

## Syntax

```excel
=VARPA(value1,[value2],...)
```

<!-- Image 1: Population Values With Logical Values. See Images/Statistical/VARPA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first value, reference or array that holds population data. |
| `value2, ...` | No | Up to 254 more values, references or arrays from the same population. Logical values inside a reference are counted, and text inside a reference is ignored. |

### Return Value

A number: the population variance, with logical values counted as 1 or 0. The function returns an error when an argument is an error value or when text typed directly into the list cannot be converted to a number. Empty cells and text inside a range are ignored.

## Examples

All examples use four cells in `A2:A5`: the number 10, the logical value TRUE, the text `pending`, and the number 12.

### Example 1: Range With a Logical Value and Text

```excel
=VARPA(A2:A5)
```

**Result:** `22.8889`

The range contributes 10, 1 (for TRUE) and 12. The text `pending` is ignored. The mean is 7.67 and dividing the sum of squared deviations, 68.67, by three gives 22.8889.

### Example 2: The Same Range in VARP

```excel
=VARP(A2:A5)
```

**Result:** `1`

VARP skips the logical value and the text, so only 10 and 12 remain. Their population variance is 1.

### Example 3: Numeric Text Typed Directly

```excel
=VARPA(10,TRUE,"7",12)
```

**Result:** `17.25`

Text typed directly into the list counts when it represents a number, so `"7"` is counted as 7. The four values 10, 1, 7 and 12 have a mean of 7.5 and a population variance of 17.25.

### Example 4: Population Standard Deviation

```excel
=SQRT(VARPA(A2:A5))
```

**Result:** `4.7842`

The square root of the population variance gives the population standard deviation of the counted values.

### Example 5: Typed Logical Values

```excel
=VARPA(TRUE,FALSE,TRUE,TRUE)
```

**Result:** `0.1875`

Typed directly, the logical values count as 1, 0, 1 and 1. Their mean is 0.75 and the population variance is 0.1875.

## Story Problems

### Problem 1: Whole Batch Inspection

A supplier sends a batch of five units to be tested, and each unit is recorded as TRUE for a pass or FALSE for a failure in `B2:B6`. The batch is the entire population the buyer cares about, so the buyer wants the population variance of the pass flags.

| Unit | Passed |
| --- | --- |
| U1 | TRUE |
| U2 | TRUE |
| U3 | FALSE |
| U4 | TRUE |
| U5 | FALSE |

**Task:** Compute the population variance of the five pass flags.

**Solution:**

```excel
=VARPA(B2:B6)
```

**Answer:** `0.24`. The three TRUE values count as 1 and the two FALSE values count as 0, giving a mean of 0.6. The squared deviations add up to 1.2, and dividing by five gives 0.24.

<!-- Image 2: Batch Flags Result. See Images/Statistical/VARPA.md -->

### Problem 2: Whole Crew Attendance

A four-person crew works one shift, and the supervisor records attendance as TRUE for present and FALSE for absent in `B2:B5`. The crew is the whole group under review, so the population variance applies.

| Crew Member | Present |
| --- | --- |
| A | TRUE |
| B | TRUE |
| C | TRUE |
| D | FALSE |

**Task:** Compute the population variance of the four attendance flags.

**Solution:**

```excel
=VARPA(B2:B5)
```

**Answer:** `0.1875`. The mean is 0.75, the squared deviations add up to 0.75, and dividing by four gives 0.1875.

## Use Cases

### Inspection Flag Variance

**Scenario:** A plant reviews every check performed on one production run, where each check is recorded as TRUE or FALSE.

```excel
=SQRT(VARPA(RunChecks[Passed]))
```

**Why It Works:** The run covers every check, so the population divisor applies. The standard deviation shows how evenly the failures are spread across the run.

### Population Pass Rate Spread

**Scenario:** A training team tracks whether every employee in a small group completed a required course.

```excel
=VARPA(Training[Completed])
```

**Why It Works:** The group is the whole population of interest, and TRUE and FALSE values count as 1 and 0, so the variance measures how mixed the completion status is.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | Text typed directly into the list cannot be converted to a number. | Reference a cell instead, or correct the typed value. |
| Unexpected result | Text inside a range is ignored, so the count is smaller than expected. | Confirm which cells hold numbers or logical values. |
| Unexpected result | The data is a sample, so the population divisor understates the spread. | Use VARA for a sample that contains logical values. |
| Unexpected result | Logical values are included when the analysis expects only numbers. | Use VAR.P when the range should contain numbers only. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions | Counts logical values in references. Ignores text inside a range and causes an error for text typed directly that cannot be converted to a number. |
| Google Sheets | Available | The Sheets help page describes VARPA as setting text to the value 0. Text in a range therefore counts as 0 in Sheets, which can give a different result from Excel for the same range. |

## Tips and Best Practices

- Use VARPA only when the population includes logical values that should count as 1 and 0.
- Use VAR.P for numeric populations, because it ignores logical values inside ranges and so avoids surprises.
- Check whether a column holds text before using VARPA, because the text rules differ between typed values and ranges.
- Keep the population definition in the report, since VARPA assumes the values are the whole group.
- Compare VARPA with VARA to see how much the population choice changes the result.

## Related Functions

| Function | Relationship |
| --- | --- |
| [STDEVPA](STDEVPA.md) | Population standard deviation with the same handling of logical values and text. |
| [VAR.P](VAR.P.md) | Modern population variance for numeric data. |
| [VARA](VARA.md) | Sample version of this function that counts logical values. |
| [VARP](VARP.md) | Legacy population variance that skips logical values in ranges. |

## Official Documentation

- [Microsoft Support: VARPA function](https://support.microsoft.com/en-us/excel/functions/varpa-function)
- [Google Docs Editors Help: VARPA](https://support.google.com/docs/answer/3094065)
