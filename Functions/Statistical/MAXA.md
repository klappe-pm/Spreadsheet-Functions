---
domain: Spreadsheet Functions
category: Statistical
subcategory: Extremes
purpose:
  - Aggregation
  - Statistical Analysis
use-case:
  - Mixed Entry Columns
  - Pass Fail Checklists
related:
  - AVERAGEA
  - COUNTA
  - MAX
  - MIN
  - MINA
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/maxa-function
  - https://support.google.com/docs/answer/3094016
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Maximum Including Text
  - Maximum With Logical Values
tags:
  - aggregation
  - excel
  - logical-values
  - maximum
  - sheets
---

# MAXA

## Description

**MAXA** returns the largest value in a set, and it treats the values in references differently from MAX. A TRUE value in a cell or range counts as 1, and a FALSE value counts as 0. Text inside a cell or range is ignored in Excel. Blank cells are ignored.

The difference from MAX matters when a column mixes numbers with logical values, such as checkboxes or pass and fail flags. MAX skips those flags, so a range that holds only TRUE and FALSE returns 0. MAXA reads them as 1 and 0, so the same range returns 1 when any TRUE is present.

Use MAXA when logical values in a reference should count toward the result. Use MAX when you want only true numbers. Use MAXIFS when the largest value must meet a condition. Google Sheets treats text as 0 in MAXA, which can change the result, so check the platform notes below before you share a workbook.

## Syntax

```excel
=MAXA(value1, [value2], ...)
```

<!-- Image 1: Logical Values in a Reference. See Images/Statistical/MAXA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first value, cell, range, or named range to evaluate. |
| `value2, ...` | No | Up to 254 more values or references, for a total of 255 arguments in Excel. |

### Return Value

A single number: the largest value after logical values are converted to 1 and 0. It returns 0 when the arguments contain no values. It returns an error when an argument is an error value, or when text that cannot be read as a number is typed directly into the list.

## Examples

### Example 1: Logical Values in a Range

Assume `B2:B4` holds the values `0.5`, `FALSE`, and `TRUE`.

```excel
=MAXA(B2:B4)
```

**Result:** `1`

TRUE counts as 1 and FALSE counts as 0. The largest of 0.5, 0, and 1 is 1.

<!-- Image 2: MAX Compared With MAXA. See Images/Statistical/MAXA.md -->

### Example 2: The Same Range With MAX

Using the same `B2:B4` values:

```excel
=MAX(B2:B4)
```

**Result:** `0.5`

MAX ignores the logical values in a reference, so only 0.5 is left to compare. The two functions give different answers for the same cells.

### Example 3: Numbers Typed Directly

```excel
=MAXA(2, TRUE, "7")
```

**Result:** `7`

The typed text `"7"` is read as the number 7, and TRUE counts as 1. The largest of 2, 1, and 7 is 7.

### Example 4: Text in a Reference Is Ignored

Assume `C2:C6` holds `Ready`, `12`, a blank cell, `30`, and `Hold`.

```excel
=MAXA(C2:C6)
```

**Result:** `30`

Excel ignores the text and the blank cell in a reference, so the comparison uses 12 and 30. Google Sheets treats the text as 0, which still gives 30 here but would change the result if every number were negative.

### Example 5: Empty Range Returns Zero

Assume `D2:D4` is blank.

```excel
=MAXA(D2:D4)
```

**Result:** `0`

No values are present, so MAXA returns 0.

## Story Problems

### Problem 1: Did Any Inspection Pass?

A quality team records whether each inspection line passed, using TRUE for a pass and FALSE for a fail, in `A1:B5`.

| Line | Passed |
| --- | --- |
| Line 1 | FALSE |
| Line 2 | FALSE |
| Line 3 | TRUE |
| Line 4 | FALSE |

**Task:** Determine whether at least one line passed. Return 1 for yes and 0 for no.

**Solution:**

```excel
=MAXA(B2:B5)
```

**Answer:** `1`, so at least one line passed. MAX would return 0 for this range because it ignores logical values in references.

### Problem 2: Latest Reading Next to Notes

A sensor logs temperatures in `C2:C6`, and a technician typed notes into the same column when the sensor went offline.

| Reading |
| --- |
| 18.5 |
| offline |
| 21.0 |
| (blank) |
| 19.2 |

**Task:** Find the highest temperature reading, ignoring the notes.

**Solution:**

```excel
=MAXA(C2:C6)
```

**Answer:** `21`. In Excel the text and the blank cell are ignored, so 21.0 is the largest reading.

## Use Cases

### Pass Fail Checklists

**Scenario:** A project lead wants a quick flag showing whether any item on a checklist has been marked complete.

```excel
=MAXA(Checklist[Complete])
```

**Why It Works:** Checkbox values are TRUE or FALSE. MAXA returns 1 when any box is checked, which can drive a status cell with IF.

### Mixed Entry Columns

**Scenario:** Field staff enter readings in one column, but some rows hold notes such as "offline" or "retest".

```excel
=MAXA(FieldLog[Reading])
```

**Why It Works:** Excel ignores the text notes in the reference, so the result is the largest reading. Check the column first if you rely on the result in Google Sheets, where text counts as 0.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `0` | The range is empty or contains only text. | Check the range with COUNTA, or wrap the result in IF(COUNTA(range)>0, MAXA(range), "No data"). |
| `#VALUE!` | Text that cannot be read as a number is typed directly into the list. | Reference a cell instead, or remove the text from the list. |
| Unexpected result | A column mixes TRUE values with numbers, and the TRUE values count as 1. | Use MAX if logical values should not count, or move the flags to a separate column. |
| `#REF!` | A referenced cell or range was deleted. | Restore the range or edit the formula to point to the new cells. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions, including Excel 2016, Excel 2019, Excel 2021, Excel 2024, and Microsoft 365 | Logical values in references count as 1 and 0. Text and blank cells in references are ignored. |
| Google Sheets | Available | Text in any argument is counted as 0. Logical values and blank cells are not described on the help page, so test them before relying on the result. |

## Tips and Best Practices

- Use MAXA only when TRUE and FALSE values should count as 1 and 0.
- Keep flags and readings in separate columns when the result must be the same in Excel and Google Sheets.
- Use MAX for pure numeric ranges, because it is easier to audit.
- Test the formula on a small sample that contains each type of value before applying it to a large range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MAX](MAX.md) | Ignores logical values and text in references. |
| [MINA](MINA.md) | The lowest-value counterpart that uses the same rules. |
| [COUNTA](COUNTA.md) | Counts every non-blank cell, including text and logical values. |
| [AVERAGEA](AVERAGEA.md) | Averages a range with the same treatment of logical values and text. |
| [MIN](MIN.md) | Returns the smallest numeric value and ignores logical values in references. |

## Official Documentation

- [Microsoft Support: MAXA function](https://support.microsoft.com/en-us/excel/functions/maxa-function)
- [Google Docs Editors Help: MAXA](https://support.google.com/docs/answer/3094016)
