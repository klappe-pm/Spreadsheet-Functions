---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
purpose:
  - Statistical Analysis
use-case:
  - Complete Team Hours
  - Legacy Workbook Maintenance
  - Station Defect Spread
related:
  - AVERAGE
  - STDEV
  - STDEV.P
  - STDEV.S
  - VARP
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/stdevp-function
  - https://support.google.com/docs/answer/3094105
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Population Standard Deviation Legacy
tags:
  - compatibility
  - excel
  - population
  - sheets
---

# STDEVP

## Description

**STDEVP** returns the standard deviation of a population, which measures how far the values in a complete group typically sit from their average. It treats the values as the entire group and divides by n in its calculation.

STDEVP is a legacy function. Microsoft has replaced it with STDEV.P, which gives the same result for the same values and is the function to use in new work. Microsoft also notes that the older function may not be available in future versions of Excel, so change existing formulas to STDEV.P when you maintain a workbook.

Use STDEVP only when the values are the complete group you want to describe. If the values are a sample drawn from a larger group, use STDEV.S (or the legacy STDEV) instead, because the population formula understates the spread of a sample.

## Syntax

```excel
=STDEVP(number1, [number2], ...)
```

<!-- Image 1: Number Arguments for STDEVP. See Images/Statistical/STDEVP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number1` | Yes | The first number, range, array or reference that contains numbers, treated as the whole population. |
| `number2, ...` | No | Additional numbers or ranges. Excel accepts up to 254 arguments in total. |

### Return Value

A number: the population standard deviation. In a range or array, only numbers are counted, and empty cells, logical values, text and errors are ignored. Numbers, text that looks like a number, and logical values typed directly into the argument list are counted. Error values, and text that cannot be converted to a number when typed as an argument, cause an error.

## Examples

All examples use the values 7, 9, 11 and 8 in `A2:A5`.

### Example 1: Population Standard Deviation

```excel
=STDEVP(A2:A5)
```

**Result:** `1.4790` (rounded to four decimals)

The mean is 8.75, and the squared distances from the mean add up to 8.75. Dividing by 4, the count of values, gives a variance of 2.1875, and its square root is 1.4790.

### Example 2: Typed Values

```excel
=STDEVP(7, 9, 11, 8)
```

**Result:** `1.4790` (rounded to four decimals)

Typed numbers produce the same result as the range in Example 1.

### Example 3: Text in a Range

With `A6` holding the text `n/a`:

```excel
=STDEVP(A2:A6)
```

**Result:** `1.4790` (rounded to four decimals)

Text inside a range is ignored, so the function uses only the four numbers.

<!-- Image 2: Legacy Function Matches Its Replacement. See Images/Statistical/STDEVP.md -->

### Example 4: Variance From the Same Values

```excel
=STDEVP(A2:A5)^2
```

**Result:** `2.1875`

Squaring the population standard deviation gives the population variance. VARP returns the same value directly.

## Story Problems

### Problem 1: Hours Worked by a Four-Person Team

A manager lists the hours each of four team members worked in one week. The manager wants the spread for this team only, so the four people are the complete group.

| Team Member | Hours |
| --- | --- |
| Ana | 38 |
| Ben | 42 |
| Cara | 40 |
| Dev | 44 |

**Task:** Measure how far the weekly hours differ from the team average.

**Solution:**

```excel
=STDEVP(B2:B5)
```

**Answer:** `2.2361` hours. The team averages 41 hours, and a typical member differs from that by about 2.2 hours.

### Problem 2: Defects Across Five Stations

A line supervisor counts defects at each of five stations during one shift. All five stations are included, so the group is complete.

| Station | Defects |
| --- | --- |
| 1 | 12 |
| 2 | 15 |
| 3 | 9 |
| 4 | 14 |
| 5 | 10 |

**Task:** Find how much the defect counts vary across the line.

**Solution:**

```excel
=STDEVP(B2:B6)
```

**Answer:** `2.2804` defects. The average is 12 defects per station, and the spread is about 2.3 defects. Use STDEV.P in the workbook when you next revise it, because the result is the same.

<!-- Image 3: Story Problem Results. See Images/Statistical/STDEVP.md -->

## Use Cases

### Complete Team Hours

**Scenario:** A project lead reports the spread of hours for a fixed team of four people, which is the whole team and not a sample.

```excel
=STDEV.P(TeamHours)
```

**Why It Works:** The formula uses the current name for the population function. The result matches the legacy STDEVP, and the workbook stays compatible with recent versions.

### Station Defect Spread

**Scenario:** A quality analyst maintains an older report that flags stations whose defect counts differ from the line average.

```excel
=IF(ABS(B2-AVERAGE(Defects))>2*STDEVP(Defects),"Review Station","Normal")
```

**Why It Works:** The formula compares each station with two population standard deviations from the mean. Replace STDEVP with STDEV.P when the report is next updated.

### Legacy Workbook Maintenance

**Scenario:** A finance team inherits a model that uses STDEVP to describe a complete set of monthly figures.

```excel
=STDEV.P(Sheet1!C2:C13)
```

**Why It Works:** The replacement keeps the result unchanged and removes a function that Microsoft may drop in a future version.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | Too few values to measure spread. Google Sheets documents this for fewer than two values. | Supply at least two values. |
| `#VALUE!` | Text that cannot be read as a number was typed into the argument list. | Put the values in cells, or type only numbers. |
| `#NAME?` | The function name is misspelled. | Check the spelling of STDEVP. |
| Unexpected result | The data is a sample of a larger group, not the complete group. | Use STDEV.S for a sample. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web | Legacy function kept for compatibility. Microsoft recommends STDEV.P. |
| Google Sheets | Available | Calculates the population standard deviation. Text typed directly into the argument list causes an error. |

## Tips and Best Practices

- Replace STDEVP with STDEV.P in new work and in workbooks you maintain.
- Confirm that the data is the complete group before you use the population formula.
- Compare STDEVP with STDEV.S on the same data to see how much the choice changes the answer.
- Search workbooks for STDEVP( before you share them with users on newer versions.
- Keep headers out of the range so that labels are not counted.

## Related Functions

| Function | Relationship |
| --- | --- |
| [STDEV.P](STDEV.P.md) | The modern replacement with the same population calculation. |
| [STDEV.S](STDEV.S.md) | Standard deviation for a sample. |
| [STDEV](STDEV.md) | The legacy sample function. |
| [VARP](VARP.md) | Population variance, the square of STDEVP. |
| [AVERAGE](AVERAGE.md) | The mean that the spread is measured around. |

## Official Documentation

- [Microsoft Support: STDEVP function](https://support.microsoft.com/en-us/excel/functions/stdevp-function)
- [Google Docs Editors Help: STDEVP](https://support.google.com/docs/answer/3094105)
