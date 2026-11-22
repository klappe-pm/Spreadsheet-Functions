---
domain: Spreadsheet Functions
category: Engineering
subcategory: Comparison and Conversion
purpose:
  - Conditional Logic
use-case:
  - Minimum Specification Checks
  - Threshold Alarm Counts
related:
  - COUNTIFS
  - DELTA
  - IF
  - IFERROR
  - SUMPRODUCT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/gestep-function
  - https://support.google.com/docs/answer/9061379
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Step Function
tags:
  - comparison
  - excel
  - sheets
  - threshold
---

# GESTEP

## Description

**GESTEP** (greater than or equal to step) tests whether a number is greater than or equal to a threshold. It returns 1 when the number meets or exceeds the threshold and 0 when it does not. The step argument is optional; when it is omitted, GESTEP compares the number with 0.

The result is a number, not a logical TRUE or FALSE, so it can be added with SUM or SUMPRODUCT to count how many values meet a threshold. Because the comparison is inclusive, a value that equals the step returns 1.

GESTEP is a niche engineering function. Most workbooks use a comparison operator such as `>=` inside IF, which is easier to read. Use GESTEP when a numeric 1 or 0 is required for arithmetic, such as a count of values above a limit inside an array calculation.

## Syntax

```excel
=GESTEP(number, [step])
```

<!-- Image 1: Syntax Anatomy. See Images/Engineering/GESTEP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The value to test, as a number or a cell that contains a number. |
| `step` | No | The threshold that `number` is compared against. If omitted, the default is 0. |

### Return Value

The number 1 when `number` is greater than or equal to `step`, or the number 0 otherwise. Nonnumeric input returns `#VALUE!`.

## Examples

### Example 1: Value Above the Step

```excel
=GESTEP(5, 4)
```

**Result:** `1`

Five is greater than four, so the result is 1.

### Example 2: Value Equal to the Step

```excel
=GESTEP(5, 5)
```

**Result:** `1`

The comparison is inclusive, so a value equal to the step returns 1.

### Example 3: Default Step

```excel
=GESTEP(-1)
```

**Result:** `0`

When `step` is omitted, the comparison is against 0. Negative numbers return 0.

### Example 4: Testing a Cell Against a Threshold

Cell `B2` holds the reading `72` and cell `C2` holds the threshold `70`.

```excel
=GESTEP(B2, C2)
```

**Result:** `1`

The reading is above the threshold, so the flag is 1.

<!-- Image 2: Inclusive Threshold Count. See Images/Engineering/GESTEP.md -->

## Story Problems

### Problem 1: Bolts That Meet Minimum Length

A fastener supplier records the length of six bolts in millimeters. The minimum accepted length is 50 mm.

| Bolt | Length (mm) |
| --- | --- |
| B-01 | 48 |
| B-02 | 50 |
| B-03 | 52 |
| B-04 | 49 |
| B-05 | 55 |
| B-06 | 50 |

**Task:** Count the bolts whose length is at least 50 mm, using the lengths in `B2:B7`.

**Solution:**

```excel
=SUMPRODUCT(GESTEP(B2:B7, 50))
```

**Answer:** `4`. Bolts B-02, B-03, B-05 and B-06 meet the minimum, and the inclusive test counts B-02 and B-06 even though their length equals 50 mm exactly.

### Problem 2: Temperature Alarm Count

A server room logs temperatures every hour. Any reading of 85 degrees Celsius or higher triggers an alarm. The readings are in `B2:B6`.

| Hour | Temperature (C) |
| --- | --- |
| 09:00 | 78 |
| 10:00 | 85 |
| 11:00 | 88 |
| 12:00 | 81 |
| 13:00 | 86 |

**Task:** Count the alarms in the period.

**Solution:**

```excel
=SUMPRODUCT(GESTEP(B2:B6, 85))
```

**Answer:** `3`. The readings 85, 88 and 86 trigger the alarm.

## Use Cases

### Minimum Specification Checks

**Scenario:** A quality team counts how many parts in a batch meet a minimum dimension.

```excel
=SUMPRODUCT(GESTEP(Batch[Length], MinLength))
```

**Why It Works:** GESTEP returns 1 or 0 for each row, and SUMPRODUCT adds the results. The count stays correct when the table grows.

### Threshold Alarm Counts

**Scenario:** An operations manager counts how many sensor readings in a shift reached an alarm level.

```excel
=SUMPRODUCT(GESTEP(Readings[Value], AlarmLevel))
```

**Why It Works:** The function is inclusive, so a reading that equals the alarm level counts as an alarm. Use `>` inside COUNTIF when the rule must be strictly greater.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `number` or `step` contains text. | Convert the cell to a number or clean the source data. |
| Count too high | Values equal to the step are counted. | Use `COUNTIF(range, ">"&step)` for a strict comparison. |
| Unexpected zero | The source values are numbers stored as text. | Convert the column to true numbers before counting. |
| `0` for a blank cell | A blank cell counts as 0 in the comparison. | Test for blanks first with IF and ISBLANK. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel 2019, Excel 2021, Excel 2024, Excel for Microsoft 365 and Excel for the web | Step defaults to 0 when omitted. |
| Google Sheets | Available | Same arguments and results; Sheets returns `#VALUE!` when either argument is nonnumeric. |

## Tips and Best Practices

- Use SUMPRODUCT with GESTEP to count matches over a range without entering an array formula.
- Put the threshold in its own cell so a manager can change it without editing the formula.
- Use IF with the `>=` operator when the result is shown as text such as "Alarm" or "OK".
- Remember that the comparison is inclusive; document the rule so reviewers know whether equality counts.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DELTA](DELTA.md) | Tests whether two numbers are equal and returns 1 or 0. |
| [IF](../Logical/IF.md) | Returns text or other results based on a comparison; clearer for display purposes. |
| [IFERROR](../Logical/IFERROR.md) | Handles `#VALUE!` results from nonnumeric input. |
| [COUNTIFS](../Statistical/COUNTIFS.md) | Counts rows that meet one or more criteria, with a choice of strict or inclusive tests. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Adds the 1 and 0 results from GESTEP across a range. |

## Official Documentation

- [Microsoft Support: GESTEP function](https://support.microsoft.com/en-us/excel/functions/gestep-function)
- [Google Docs Editors Help: GESTEP](https://support.google.com/docs/answer/9061379)
