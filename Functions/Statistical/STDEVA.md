---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
purpose:
  - Statistical Analysis
use-case:
  - Checklist Pass Flags
  - Mixed Entry Log Review
  - Survey Response Spread
related:
  - AVERAGEA
  - COUNTA
  - STDEV.P
  - STDEV.S
  - VARA
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/stdeva-function
  - https://support.google.com/docs/answer/3094055
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sample Standard Deviation With Text
tags:
  - excel
  - logical-values
  - sheets
  - spread
---

# STDEVA

## Description

**STDEVA** returns the standard deviation of a sample, measured as the spread of the values around their average. It works like STDEV.S, with one difference: it gives logical values and text a numeric meaning, so you can include TRUE, FALSE and text entries in a calculation.

The rule depends on how each entry is supplied. TRUE counts as 1. FALSE and text typed directly into the argument list count as 0. Inside a range or array, text and empty cells are ignored, so STDEVA on a range of numbers gives the same result as STDEV.S on that range. Use STDEVA when the mixed entries are typed into the formula and you want those rules applied.

STDEVA assumes its arguments are a sample. When the values are the complete group, Microsoft points to STDEVPA for the population version. Google Sheets documents the same treatment of text, setting each text value it encounters to 0.

## Syntax

```excel
=STDEVA(value1, [value2], ...)
```

<!-- Image 1: Value Arguments for STDEVA. See Images/Statistical/STDEVA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first value, range, array or reference that represents a sample. |
| `value2, ...` | No | Additional values or ranges, up to 255 arguments in total. |

### Return Value

A number: the sample standard deviation. Arguments that contain TRUE evaluate as 1, and arguments that contain text or FALSE evaluate as 0. In an array or reference, empty cells and text are ignored. Error values, and text that cannot be converted to a number when typed as an argument, cause an error.

## Examples

### Example 1: Text Typed as an Argument

```excel
=STDEVA(4, 8, "n/a", 6)
```

**Result:** `3.4157` (rounded to four decimals)

The text argument `"n/a"` is evaluated as 0, so the function uses the values 4, 8, 0 and 6.

### Example 2: TRUE Typed as an Argument

```excel
=STDEVA(4, 8, TRUE, 6)
```

**Result:** `2.9861` (rounded to four decimals)

TRUE evaluates as 1, so the function uses the values 4, 8, 1 and 6.

### Example 3: FALSE Typed as an Argument

```excel
=STDEVA(4, 8, FALSE, 6)
```

**Result:** `3.4157` (rounded to four decimals)

FALSE evaluates as 0, which gives the same result as the text in Example 1.

<!-- Image 2: Typed Entries Versus Range Entries. See Images/Statistical/STDEVA.md -->

### Example 4: Text in a Range Is Ignored

With `A2:A7` holding the values 4, 8, 6, 5, 3 and 7, and `A8` holding the text `n/a`:

```excel
=STDEVA(A2:A8)
```

**Result:** `1.8708` (rounded to four decimals)

Inside a range the text is ignored, so the result matches STDEV.S on the same six numbers.

## Story Problems

### Problem 1: Four Readings Typed Into One Formula

A technician records four sensor readings. One sensor did not report, and the technician enters the missing reading as the text `n/a` directly in the formula.

| Reading | Value |
| --- | --- |
| 1 | 4 |
| 2 | 8 |
| 3 | n/a |
| 4 | 6 |

**Task:** Find the spread of the readings, counting the missing reading as 0.

**Solution:**

```excel
=STDEVA(4, 8, "n/a", 6)
```

**Answer:** `3.4157`. Because the text argument counts as 0, the spread includes the missing reading as a low value, which makes the result larger than the spread of the three real readings.

### Problem 2: Survey Responses in a Range

A survey lists five response scores for one question. One respondent skipped the question, and the cell holds the text `n/a`.

| Respondent | Score |
| --- | --- |
| 1 | 4 |
| 2 | 8 |
| 3 | n/a |
| 4 | 6 |
| 5 | 5 |

**Task:** Find the spread of the scores using the range.

**Solution:**

```excel
=STDEVA(B2:B6)
```

**Answer:** `1.7078`. The text inside the range is ignored, so the function uses only the four numeric scores.

<!-- Image 3: Story Problem Results. See Images/Statistical/STDEVA.md -->

## Use Cases

### Checklist Pass Flags

**Scenario:** A quality lead types a short list of checks, where a passed check is TRUE and a failed check is FALSE, and wants the spread of the results.

```excel
=STDEVA(TRUE, FALSE, TRUE, TRUE)
```

**Why It Works:** Typed TRUE and FALSE values count as 1 and 0, so the spread describes how often checks pass. For a list held in cells, check the result carefully, because logical values in ranges are not evaluated the same way.

### Survey Response Spread

**Scenario:** A researcher scores responses where skipped questions are entered as the text `n/a` in a sheet.

```excel
=STDEV.S(ResponseScores)
```

**Why It Works:** Text in a range is ignored, so STDEV.S gives the same spread as STDEVA on the numeric responses. Using STDEV.S here makes the rule explicit to other readers.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A text value that cannot be read as a number was typed into the argument list. | Replace it with a number, or with TRUE or FALSE if a logical value is intended. |
| Unexpected larger result | Text typed as an argument counted as 0 rather than being skipped. | Remove the text from the argument list, or reference a range that holds only numbers. |
| Unexpected smaller result | Text in a range was skipped, so fewer values were used. | Confirm that the range holds only the values that should be counted. |
| `#DIV/0!` | Too few values were supplied to measure spread. | Supply at least two values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel 2016 and later, Excel for Microsoft 365, Excel for the web | Evaluates TRUE as 1 and text typed as an argument as 0. Ignores text and empty cells inside ranges. |
| Google Sheets | Available | Sets each text value it encounters to 0. Its documentation does not describe logical values. |

## Tips and Best Practices

- Use STDEV.S for ordinary numeric ranges, and reserve STDEVA for formulas where typed logical values or text are intended.
- Check the result against STDEV.S on the same numbers to confirm that only the intended values are counted.
- Use STDEVPA when the values are the complete group.
- Keep logical values and text out of numeric ranges unless you are sure how they will be counted.
- Document the treatment of text and TRUE or FALSE in the sheet so later editors understand the result.

## Related Functions

| Function | Relationship |
| --- | --- |
| [STDEV.S](STDEV.S.md) | Sample standard deviation that ignores text and logical values in ranges. |
| [STDEV.P](STDEV.P.md) | Population standard deviation for a complete group. |
| [VARA](VARA.md) | Sample variance using the same logical and text rules. |
| [AVERAGEA](AVERAGEA.md) | Average using the same logical and text rules. |
| [COUNTA](COUNTA.md) | Counts non-empty cells, including text. |

## Official Documentation

- [Microsoft Support: STDEVA function](https://support.microsoft.com/en-us/excel/functions/stdeva-function)
- [Google Docs Editors Help: STDEVA](https://support.google.com/docs/answer/3094055)
