---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Data Validation
  - Type Checking
use-case:
  - Mixed Identifier Check
  - Note Flagging
  - Text Field Validation
related:
  - IF
  - ISBLANK
  - ISLOGICAL
  - ISNONTEXT
  - ISNUMBER
level: 1
source:
  - https://support.microsoft.com/en-us/excel/is-functions
  - https://support.google.com/docs/answer/3093297
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Is Text
tags:
  - data-validation
  - excel
  - information
  - sheets
  - type-checking
---

# ISTEXT

## Description

**ISTEXT** returns TRUE when a value is text and FALSE for everything else, including numbers, logical values, errors and blank cells. A value stored as text counts even when it looks like a number, so the text string `"00417"` returns TRUE.

Use ISTEXT to find text entries in a column that should hold numbers, to flag rows that need a note, or to route each row to the right formula. It is the opposite of ISNONTEXT. Because ISTEXT does not convert values, a number stored as text still returns TRUE.

A reference to a blank cell returns FALSE. The Google Sheets help page notes that a literal empty string, written as `""`, returns TRUE, so a formula that returns an empty string can look like text. Use ISBLANK or a length check when empty results need their own handling.

## Syntax

```excel
=ISTEXT(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISTEXT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value, text string or cell reference to test. A cell that holds text or a formula that returns text is the usual input. |

### Return Value

TRUE when `value` is text, or a reference to a cell that holds text. FALSE for numbers, logical values, errors and blank cells.

## Examples

### Example 1: A Text Cell

Cell A2 holds `Maple`.

```excel
=ISTEXT(A2)
```

**Result:** `TRUE`

The cell holds text, so the function returns TRUE.

### Example 2: A Number Cell

Cell A3 holds the number `2026`.

```excel
=ISTEXT(A3)
```

**Result:** `FALSE`

The cell holds a number, so the function returns FALSE.

### Example 3: A Text String

```excel
=ISTEXT("cat")
```

**Result:** `TRUE`

The literal string "cat" is text, so the function returns TRUE.

### Example 4: Labeling Codes by Type

Cell B2 holds the text `00417`, stored as text so its leading zeros stay in place.

```excel
=IF(ISTEXT(B2),"Text code","Numeric code")
```

**Result:** `Text code`

The label reports the type, which is useful when codes are mixed in one column.

## Story Problems

### Problem 1: Mixed Customer Identifiers

A customer system stores IDs in column A. Some IDs use a prefix and are text. A few older IDs were imported as numbers, and one was imported as text that happens to contain digits. The support team wants the count of text IDs.

| Customer ID |
| --- |
| C-1009 |
| 2044 |
| C-2210 |
| 3050 (text) |
| 4120 |

**Task:** Count the text entries in `A2:A6`.

**Solution:**

```excel
=SUMPRODUCT(ISTEXT(A2:A6)*1)
```

**Answer:** `3`. The entries C-1009, C-2210 and the text 3050 are text.

### Problem 2: Flagging Rows With Notes

A delivery log has a Notes column. Some rows hold a written note, and others hold a number or are empty. The manager wants a label that marks each row that has a note.

| Order | Notes |
| --- | --- |
| 101 | Late |
| 102 | 14 |
| 103 | Paid |
| 104 | 0 |
| 105 | Hold |

**Task:** Fill column C with a formula that shows "Note" when the Notes entry is text and "No note" otherwise.

**Solution:**

```excel
=IF(ISTEXT(B2),"Note","No note")
```

**Answer:** Note, No note, Note, No note, Note. Rows 2, 4 and 6 hold text in the Notes column, and the number 14 and the value 0 do not.

<!-- Image 2: Note Flagging Results. See Images/Information/ISTEXT.md -->

## Use Cases

### Note Flagging

**Scenario:** A support queue shows a small marker next to tickets that have a written note from an agent.

```excel
=IF(ISTEXT(C2),"Has note","")
```

**Why It Works:** Text in the note column produces the marker. Blank cells and numbers produce nothing, so the queue shows only tickets with a real note.

### Text Field Validation

**Scenario:** A survey requires a written reason in the comments column, and a number entered there means the respondent typed the wrong thing.

```excel
=IF(ISTEXT(D2),"OK","Enter a written reason")
```

**Why It Works:** The check flags numbers and blanks alike. A reviewer sees the warning before the responses are analyzed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `TRUE` for a number | The number was imported as text. | Convert the value with VALUE or reformat the column as Number. |
| `FALSE` for a blank cell | A blank cell is not text. | Test with ISBLANK when blanks need their own label. |
| `TRUE` for a formula that shows nothing | The formula returns an empty string, which is text. | Test the length with `=LEN(A2)>0` instead. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Microsoft 365 for Mac, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016. | Returns TRUE for text, including numbers stored as text. Blank cells return FALSE. |
| Google Sheets | Available | Same syntax. A literal empty string returns TRUE, and a blank cell reference returns FALSE. |

## Tips and Best Practices

- Use ISTEXT to find numbers stored as text before a calculation fails or sorts incorrectly.
- Pair with IF to label rows by type instead of letting the formulas show errors.
- Combine ISTEXT with LEN when a formula can return an empty string.
- Use SUMPRODUCT with `*1` to count text entries in a range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ISNONTEXT](ISNONTEXT.md) | The opposite test, which returns TRUE for anything that is not text. |
| [ISNUMBER](ISNUMBER.md) | Tests for numbers, the counterpart to ISTEXT for mixed columns. |
| [ISLOGICAL](ISLOGICAL.md) | Tests for TRUE and FALSE values. |
| [ISBLANK](ISBLANK.md) | Identifies empty cells, which ISTEXT reports as FALSE. |
| [IF](../Logical/IF.md) | Routes each row based on the ISTEXT result. |

## Official Documentation

- [Microsoft Support: IS functions](https://support.microsoft.com/en-us/excel/is-functions)
- [Google Docs Editors Help: ISTEXT](https://support.google.com/docs/answer/3093297)
