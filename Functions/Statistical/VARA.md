---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
purpose:
  - Statistical Analysis
use-case:
  - Inspection Pass Rates
  - Survey Response Scoring
related:
  - AVERAGEA
  - STDEVA
  - VAR
  - VAR.S
  - VARPA
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/vara-function
  - https://support.google.com/docs/answer/3094064
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sample Variance With Logicals
tags:
  - excel
  - logical-values
  - sample
  - sheets
  - variance
---

# VARA

## Description

**VARA** estimates the variance of a sample, the same way VAR.S does, but it treats the inputs differently. Logical values count as numbers: TRUE is 1 and FALSE is 0. Text typed directly into the argument list counts as 0. Use VARA when a set of yes or no results, such as pass or fail flags, should contribute to the spread.

The rules change between a typed list and a range. Inside a range or array, VARA counts logical values but ignores text, and it skips empty cells. Text typed directly into the list is counted as 0. Keep this distinction in mind, because a text cell in a range and the same text typed into the formula produce different results.

VARA divides the sum of squared deviations by the number of values minus one. Use VAR.S when the data holds only numbers, and VARPA when the data is the entire population rather than a sample.

## Syntax

```excel
=VARA(value1,[value2],...)
```

<!-- Image 1: Logical Values and Text in a Range. See Images/Statistical/VARA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first value, reference or array that holds sample data. |
| `value2, ...` | No | Up to 254 more values, references or arrays from the same sample. Logical values inside a reference are counted, and text inside a reference is ignored. |

### Return Value

A number: the sample variance, with logical values counted as 1 or 0. The function returns an error when an argument is an error value or when text typed directly into the list cannot be converted to a number. Text inside a range is ignored and does not cause an error.

## Examples

All examples use four cells in `A2:A5`: the number 10, the logical value TRUE, the text `pending`, and the number 12.

### Example 1: Range With a Logical Value and Text

```excel
=VARA(A2:A5)
```

**Result:** `34.3333`

The range contributes three values: 10, 1 (for TRUE) and 12. The text `pending` is ignored, so the mean is 7.67 and the sample variance is 34.3333.

### Example 2: The Same Range in VAR

```excel
=VAR(A2:A5)
```

**Result:** `2`

VAR skips the logical value and the text, so only 10 and 12 remain. Their mean is 11 and their sample variance is 2. Comparing this with Example 1 shows why the function choice matters.

### Example 3: Text Typed Directly Into the List

```excel
=VARA(10,TRUE,"pending",12)
```

**Result:** `37.5833`

Typed directly into the list, the text `pending` counts as 0 rather than being ignored. The four values 10, 1, 0 and 12 give a mean of 5.75 and a sample variance of 37.5833.

### Example 4: Standard Deviation From the Variance

```excel
=SQRT(VARA(A2:A5))
```

**Result:** `5.8595`

The square root of the sample variance is the sample standard deviation of the counted values.

### Example 5: Typed Logical Values

```excel
=VARA(TRUE,FALSE,TRUE,TRUE)
```

**Result:** `0.25`

Typed directly, the logical values count as 1, 0, 1 and 1. Their mean is 0.75 and the sample variance is 0.25.

## Story Problems

### Problem 1: Inspection Pass Flags

A quality inspector records whether each of six parts passed a check. The column holds TRUE for a pass and FALSE for a failure. The team wants the sample variance of the flags to see how mixed the results are.

| Part | Passed |
| --- | --- |
| P1 | TRUE |
| P2 | FALSE |
| P3 | TRUE |
| P4 | TRUE |
| P5 | FALSE |
| P6 | TRUE |

**Task:** Compute the sample variance of the pass flags in `B2:B7`.

**Solution:**

```excel
=VARA(B2:B7)
```

**Answer:** `0.2667`. VARA counts the four TRUE values as 1 and the two FALSE values as 0, giving a mean of 0.67. The squared deviations add up to 1.33, and dividing by five gives 0.2667. VAR skips every cell in this range, because logical values are ignored there, so it has no values to work with.

<!-- Image 2: Pass Flags Result. See Images/Statistical/VARA.md -->

### Problem 2: Survey Scores With Missing Answers

A survey asks for a score from 1 to 10. Two respondents typed `n/a` instead of a number. The analyst wants the sample variance of the valid scores in `B2:B8`.

| Respondent | Score |
| --- | --- |
| R1 | 8 |
| R2 | 9 |
| R3 | n/a |
| R4 | 7 |
| R5 | 10 |
| R6 | n/a |
| R7 | 6 |

**Task:** Compute the sample variance of the scores, excluding the two text answers.

**Solution:**

```excel
=VARA(B2:B8)
```

**Answer:** `2.5`. Inside a range VARA ignores the text `n/a`, so it averages the five valid scores 8, 9, 7, 10 and 6. Their mean is 8, and the squared deviations add up to 10, which divided by four gives 2.5.

## Use Cases

### Inspection Pass Rates

**Scenario:** A plant wants to know how variable the pass and fail results are across a sample of checks, where each check is recorded as TRUE or FALSE.

```excel
=SQRT(VARA(Checks[Passed]))
```

**Why It Works:** Logical values in the table count as 1 or 0, so the standard deviation reflects the mix of passes and failures. Keep the column free of text so no value is treated differently from its neighbors.

### Survey Response Scoring

**Scenario:** A research team scores responses where some cells hold numbers and others hold the text `n/a` for skipped questions.

```excel
=VARA(Survey[Score])
```

**Why It Works:** The text cells are ignored inside the range, so skipped questions do not pull the variance toward zero. Use the same layout in every survey so the results remain comparable.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error value | An argument is an error value, or text typed directly into the list cannot be converted to a number. | Correct the source cell or the typed value. |
| Unexpected result | Text typed directly into the list counts as 0, which lowers the mean and changes the variance. | Reference a cell that holds the value, or remove the text from the list. |
| Unexpected result | Logical values inside a range are counted, but the user expected them to be ignored. | Use VAR.S when the range should hold numbers only. |
| Unexpected result | A range that holds only text or blanks has too few values to calculate a variance. | Check that the range holds at least two numbers or logical values. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all listed versions | Counts TRUE as 1 and FALSE as 0 in references. Ignores text inside a range and counts text typed in the list as 0. |
| Google Sheets | Available | The Sheets help page describes VARA as setting text to the value 0. Text in a range therefore counts as 0 in Sheets, which can give a different result from Excel for the same range. |

## Tips and Best Practices

- Use VARA only when logical values should count as 1 and 0 in the spread.
- Use VAR.S for numeric data where logical values or text should not be counted.
- Test the formula on a small range before applying it to a large table, because the rules for text differ between typed values and ranges.
- Clean text answers such as `n/a` out of numeric columns when the workbook must match Excel and Sheets.
- Document which cells hold logical values, so readers understand why the variance includes them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGEA](AVERAGEA.md) | Mean that counts logical values and text in the same way as VARA. |
| [STDEVA](STDEVA.md) | Sample standard deviation with the same handling of logical values and text. |
| [VAR](VAR.md) | Legacy sample variance that skips logical values and text in ranges. |
| [VAR.S](VAR.S.md) | Modern sample variance for numeric data. |
| [VARPA](VARPA.md) | Population version of this function that counts logical values in ranges. |

## Official Documentation

- [Microsoft Support: VARA function](https://support.microsoft.com/en-us/excel/functions/vara-function)
- [Google Docs Editors Help: VARA](https://support.google.com/docs/answer/3094064)
