---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Statistical Analysis
use-case:
  - Legacy Workbook Maintenance
  - Pump Run Hours
  - Test Score Spread
related:
  - AVERAGE
  - STDEV.S
  - STDEVA
  - STDEVP
  - VAR
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/stdev-function
  - https://support.google.com/docs/answer/3094054
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sample Standard Deviation Legacy
tags:
  - compatibility
  - excel
  - sheets
  - spread
---

# STDEV

## Description

**STDEV** returns the standard deviation of a sample, which measures how far a set of values typically sits from their average. It assumes that the values are a sample of a larger group and divides by n minus 1 in its calculation.

STDEV is a legacy function. Microsoft has replaced it with STDEV.S, which gives the same result for the same sample and is the function to use in new work. Microsoft notes that STDEV may not be available in future versions of Excel, so change existing formulas to STDEV.S when you maintain a workbook. Keep STDEV only when a workbook depends on it and the change is not yet planned.

Use STDEV for a complete population only when you intend to treat the data as a sample. For a complete population, use STDEVP or, in current workbooks, STDEV.P.

## Syntax

```excel
=STDEV(number1, [number2], ...)
```

<!-- Image 1: Number Arguments for STDEV. See Images/Statistical/STDEV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, range, array or reference that contains numbers, treated as a sample. |
| `number2, ...` | No | Additional numbers or ranges. Excel accepts up to 254 arguments in total. |

### Return Value

A number: the sample standard deviation. In a range or array, only numbers are counted. Empty cells, logical values, text and error values are ignored. Numbers, text that looks like a number, and logical values typed directly into the argument list are counted. Error values, and text that cannot be converted to a number when typed as an argument, cause an error.

## Examples

All examples use the values 4, 8, 6, 5, 3 and 7 in `A2:A7`.

### Example 1: Sample Standard Deviation

```excel
=STDEV(A2:A7)
```

**Result:** `1.8708` (rounded to four decimals)

The result matches STDEV.S on the same range. The squared distances from the mean of 5.5 add up to 17.5, which divided by 5 gives a variance of 3.5.

### Example 2: Typed Values

```excel
=STDEV(4, 8, 6, 5, 3, 7)
```

**Result:** `1.8708` (rounded to four decimals)

Numbers typed directly into the argument list produce the same result as the range in Example 1.

### Example 3: Text in a Range

With `A8` holding the text `n/a` and `A9` left empty:

```excel
=STDEV(A2:A9)
```

**Result:** `1.8708` (rounded to four decimals)

Text and empty cells inside a range are ignored, so the result is unchanged.

<!-- Image 2: Legacy Function Matches Its Replacement. See Images/Statistical/STDEV.md -->

### Example 4: Matching the Modern Replacement

```excel
=STDEV(A2:A7)-STDEV.S(A2:A7)
```

**Result:** `0`

The difference is zero, which confirms that STDEV and STDEV.S give the same result for the same sample. Replace STDEV with STDEV.S when you update a workbook.

## Story Problems

### Problem 1: Scores on One Test Sitting

A teacher records five students' scores on a unit test. The students are treated as a sample of the school's Year 9 group.

| Student | Score |
| --- | --- |
| 1 | 72 |
| 2 | 85 |
| 3 | 91 |
| 4 | 64 |
| 5 | 78 |

**Task:** Measure how widely the scores are spread around the class average.

**Solution:**

```excel
=STDEV(B2:B6)
```

**Answer:** `10.6066` points. The mean is 78, and a typical score differs from it by about 10 points.

### Problem 2: Pump Run Hours

A maintenance team logs the run hours of four pumps in one week. The four pumps are a sample from a larger fleet.

| Pump | Run Hours |
| --- | --- |
| A | 5.5 |
| B | 6 |
| C | 6.5 |
| D | 7 |

**Task:** Estimate the spread of run hours across the fleet.

**Solution:**

```excel
=STDEV(B2:B5)
```

**Answer:** `0.6455` hours. Use STDEV.S in the workbook when you revise it, because the result is the same.

<!-- Image 3: Story Problem Results. See Images/Statistical/STDEV.md -->

## Use Cases

### Test Score Spread

**Scenario:** A school report includes the spread of each class's test scores, so parents can compare the classes.

```excel
=STDEV.S(ClassScores)
```

**Why It Works:** The formula uses the current name for the function. The result matches the legacy STDEV exactly, and the workbook stays compatible with recent versions.

### Pump Run Hours

**Scenario:** A maintenance supervisor keeps an older workbook that uses STDEV to flag pumps with unusual run hours.

```excel
=IF(ABS(B2-AVERAGE(RunHours))>2*STDEV(RunHours),"Check Pump","Normal")
```

**Why It Works:** The formula compares each pump with two standard deviations from the mean. Consider replacing STDEV with STDEV.S when the workbook is next revised.

### Legacy Workbook Maintenance

**Scenario:** An analyst inherits a workbook built years ago that uses STDEV in many places.

```excel
=STDEV.S(Sheet1!B2:B20)
```

**Why It Works:** Replacing each legacy call with STDEV.S keeps the result unchanged and removes a function that Microsoft may drop in a future version.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | Too few values to measure spread. Google Sheets documents this for fewer than two values. | Supply at least two values. |
| `#VALUE!` | Text that cannot be read as a number was typed into the argument list. | Put the values in cells, or type only numbers. |
| `#NAME?` | The function name is misspelled. | Check the spelling of STDEV. |
| Unexpected result | The data is the complete population, not a sample. | Use STDEVP or STDEV.P for a complete group. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web | Legacy function kept for compatibility. Microsoft recommends STDEV.S. |
| Google Sheets | Available | Calculates the sample standard deviation. Text typed directly into the argument list causes an error, while text in a referenced cell is ignored. |

## Tips and Best Practices

- Replace STDEV with STDEV.S in new work and in workbooks that you maintain.
- Use STDEV.P or STDEVP for a complete population rather than a sample.
- Check legacy workbooks with a search for STDEV( before sharing them with users on newer versions.
- Compare STDEV with STDEV.S on a sample of your data when you are unsure whether the results have changed.
- Keep the data range free of headers so that labels are not counted.

## Related Functions

| Function | Relationship |
| --- | --- |
| [STDEV.S](STDEV.S.md) | The modern replacement with the same sample calculation. |
| [STDEVP](STDEVP.md) | The legacy population standard deviation. |
| [STDEVA](STDEVA.md) | Sample standard deviation that treats logical values and text differently. |
| [VAR](VAR.md) | Sample variance, the square of STDEV. |
| [AVERAGE](AVERAGE.md) | The mean that the spread is measured around. |

## Official Documentation

- [Microsoft Support: STDEV function](https://support.microsoft.com/en-us/excel/functions/stdev-function)
- [Google Docs Editors Help: STDEV](https://support.google.com/docs/answer/3094054)
