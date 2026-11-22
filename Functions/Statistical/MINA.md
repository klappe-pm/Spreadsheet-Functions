---
domain: Spreadsheet Functions
category: Statistical
subcategory: Extremes
purpose:
  - Aggregation
  - Statistical Analysis
use-case:
  - Checklist Completion
  - Lowest Reading Next to Notes
related:
  - AVERAGEA
  - COUNTA
  - MAXA
  - MIN
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/mina-function
  - https://support.google.com/docs/answer/3094018
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Minimum Including Text
  - Minimum With Logical Values
tags:
  - aggregation
  - excel
  - logical-values
  - minimum
  - sheets
---

# MINA

## Description

**MINA** returns the smallest value in a set, and it treats the values in references differently from MIN. A TRUE value in a cell or range counts as 1, and a FALSE value counts as 0. Text inside a cell or range is ignored in Excel. Blank cells are ignored.

The difference from MIN matters when a column mixes numbers with logical values, such as completion flags. MIN skips those flags, so a range of completion flags returns 0 when it has no numbers. MINA reads FALSE as 0, so the result is 0 whenever any FALSE value is present. That makes MINA useful as an "any item still open" test when the flags are TRUE for done and FALSE for open.

Use MINA when logical values in a reference should count toward the result. Use MIN when only real numbers should count. Use MINIFS when the smallest value must meet a condition. Google Sheets counts text as 0 in MINA, which can change the result, so check the platform notes below before you share a workbook.

## Syntax

```excel
=MINA(value1, [value2], ...)
```

<!-- Image 1: Logical Values in a Reference. See Images/Statistical/MINA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first value, cell, range, or named range to evaluate. |
| `value2, ...` | No | Up to 254 more values or references, for a total of 255 arguments in Excel. |

### Return Value

A single number: the smallest value after logical values are converted to 1 and 0. It returns 0 when the arguments contain no values. It returns an error when an argument is an error value, or when text that cannot be read as a number is typed directly into the list.

## Examples

### Example 1: Logical Values in a Range

Assume `B2:B4` holds the values `0.5`, `FALSE`, and `TRUE`.

```excel
=MINA(B2:B4)
```

**Result:** `0`

FALSE counts as 0, which is lower than 0.5 and 1. The smallest value is 0.

<!-- Image 2: MIN Compared With MINA. See Images/Statistical/MINA.md -->

### Example 2: The Same Range With MIN

Using the same `B2:B4` values:

```excel
=MIN(B2:B4)
```

**Result:** `0.5`

MIN ignores the logical values in a reference, so only 0.5 is left to compare. The two functions disagree for the same cells.

### Example 3: Numbers Typed Directly

```excel
=MINA(2, TRUE, "7")
```

**Result:** `1`

TRUE counts as 1, and the typed text `"7"` is read as the number 7. The smallest of 2, 1, and 7 is 1.

### Example 4: Text in a Reference Is Ignored

Assume `C2:C6` holds `Ready`, `12`, a blank cell, `30`, and `Hold`.

```excel
=MINA(C2:C6)
```

**Result:** `12`

Excel ignores the text and the blank cell in a reference, so the comparison uses 12 and 30. Google Sheets counts each text value as 0 and returns 0 here, so use a numeric-only range in Sheets.

### Example 5: Empty Range Returns Zero

Assume `D2:D4` is blank.

```excel
=MINA(D2:D4)
```

**Result:** `0`

No values are present, so MINA returns 0.

## Story Problems

### Problem 1: Checklist Completion

A packing team marks each task as TRUE when it is done and FALSE when it is still open, in `A1:B5`.

| Task | Done |
| --- | --- |
| Unpack | TRUE |
| Label | TRUE |
| Inspect | FALSE |
| Pack | TRUE |

**Task:** Find out whether every task is complete. Return 1 if all are done and 0 if any is still open.

**Solution:**

```excel
=MINA(B2:B5)
```

**Answer:** `0`, so at least one task is still open. The Inspect task is the one holding the result at 0.

### Problem 2: Lowest Reading Next to Notes

A sensor log in `C2:C6` mixes temperatures with short notes typed by a technician.

| Reading |
| --- |
| 4.5 |
| n/a |
| 2.0 |
| (blank) |
| 6.5 |

**Task:** Find the lowest temperature reading, ignoring the notes.

**Solution:**

```excel
=MINA(C2:C6)
```

**Answer:** `2`, in Excel. The text and blank cell are ignored in a reference. In Google Sheets the text would count as 0 and the answer would be 0, so Sheets users should use MIN on a numeric-only range instead.

## Use Cases

### Checklist Completion

**Scenario:** A project lead wants a single cell that shows whether every item on a checklist is finished.

```excel
=IF(MINA(Checklist[Done])=1, "Complete", "Open items remain")
```

**Why It Works:** MINA returns 0 when any FALSE value is present, so the IF test reports an open item as soon as one unchecked box exists.

### Lowest Reading Next to Notes

**Scenario:** Field staff record readings in one column, but some rows hold notes such as "n/a" or "retest".

```excel
=MINA(FieldLog[Reading])
```

**Why It Works:** Excel ignores the text in the reference, so the lowest numeric reading is returned. In Google Sheets, use MIN on a column without text.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `0` | The range is empty, or a FALSE value is present. | Check the range with COUNTA. When FALSE is expected, read the 0 as an open item. |
| `0` in Google Sheets | Text is counted as 0 in a range. | Use MIN on a column without text, or clear the text before calculating. |
| `#VALUE!` | Text that cannot be read as a number is typed directly into the list. | Reference a cell instead, or remove the text from the list. |
| Unexpected result | A column mixes TRUE values with numbers, and the TRUE values count as 1. | Use MIN if logical values should not count. |
| `#REF!` | A referenced cell or range was deleted. | Restore the range or edit the formula to point to the new cells. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions, including Excel 2016, Excel 2019, Excel 2021, Excel 2024, and Microsoft 365 | Logical values in references count as 1 and 0. Text and blank cells in references are ignored. |
| Google Sheets | Available | Text in any argument is counted as 0, so a range with text can return 0 even when all numbers are higher. |

## Tips and Best Practices

- Use MINA only when TRUE and FALSE values should count as 1 and 0.
- Keep completion flags in a separate column from numeric readings.
- Use MIN for pure numeric ranges, because the result is easier to audit.
- Test the formula on a small sample that contains each type of value before applying it to a large range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [MIN](MIN.md) | Ignores logical values and text in references. |
| [MAXA](MAXA.md) | The largest-value counterpart that uses the same rules. |
| [COUNTA](COUNTA.md) | Counts every non-blank cell, including text and logical values. |
| [AVERAGEA](AVERAGEA.md) | Averages a range with the same treatment of logical values and text. |

## Official Documentation

- [Microsoft Support: MINA function](https://support.microsoft.com/en-us/excel/functions/mina-function)
- [Google Docs Editors Help: MINA](https://support.google.com/docs/answer/3094018)
