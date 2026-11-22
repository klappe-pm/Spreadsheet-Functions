---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Type Checking
use-case:
  - Checking Formula Results
  - Import Validation
  - Mixed Data Column Audits
related:
  - ISERROR
  - ISFORMULA
  - ISLOGICAL
  - ISNUMBER
  - ISTEXT
  - 'N'
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/type-function
  - https://support.google.com/docs/answer/3267375
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Data Type Code
  - Value Type Code
tags:
  - data-types
  - error-checking
  - excel
  - sheets
  - troubleshooting
---

# TYPE

## Description

**TYPE** returns a number that identifies the kind of value it receives. A number returns 1, text returns 2, a logical value returns 4, an error returns 16, and an array returns 64. Google Sheets and Microsoft Excel use the same codes, and both also use code 128 for other cell types, such as in-cell images and sparklines.

Use TYPE when a formula must branch on the kind of data it receives, or when you audit a column that should hold numbers only. The most common surprise is a number that is stored as text. An imported value such as "880" returns 2, not 1, even though it looks like a number, so arithmetic on it may fail or give the wrong result.

TYPE reports the type of the value that a cell displays, not whether the cell holds a formula. If a cell refers to a formula, TYPE reports the type of that formula's result. Use ISFORMULA to find out whether a cell holds a formula.

## Syntax

```excel
=TYPE(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/TYPE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value to test: a number, text, a logical value, an error, an array, a cell reference or an expression. The function reports the type of the result. |

### Return Value

A code that identifies the type:

| Value Is | TYPE Returns |
| --- | --- |
| Number | 1 |
| Text | 2 |
| Logical value (TRUE or FALSE) | 4 |
| Error value | 16 |
| Array | 64 |
| Compound data or other cell type | 128 |

Neither the Microsoft nor the Google page documents any other codes, so do not test for codes outside this table.

## Examples

All examples use this sample data:

| Cell | Value |
| --- | --- |
| A2 | Smith |
| A3 | 1500 (number) |
| A4 | TRUE |
| A5 | 1500 (text) |

### Example 1: Text

```excel
=TYPE(A2)
```

**Result:** `2`

The cell holds the word Smith, which is text.

### Example 2: Number

```excel
=TYPE(A3)
```

**Result:** `1`

The cell holds a number that can be used in arithmetic.

### Example 3: Number Stored as Text

```excel
=TYPE(A5)
```

**Result:** `2`

The value looks like a number, but it is stored as text, so TYPE returns 2. This is the case that causes most import problems.

### Example 4: Logical Value

```excel
=TYPE(A4)
```

**Result:** `4`

The cell holds TRUE, a logical value.

### Example 5: Error Value

```excel
=TYPE(1/0)
```

**Result:** `16`

Dividing by zero produces the error `#DIV/0!`. TYPE reports the error type rather than passing the error on.

### Example 6: Array

```excel
=TYPE({1,2;3,4})
```

**Result:** `64`

An array constant returns 64, because the input is an array of values rather than a single value.

## Story Problems

### Problem 1: Auditing an Imported Column

A bank export puts four values into column B. The analyst needs to label each row with its type before loading the file into a report.

| Row | Value | Stored As |
| --- | --- | --- |
| 2 | 880 | Number |
| 3 | "880" | Text |
| 4 | TRUE | Logical value |
| 5 | `#DIV/0!` | Error |

**Task:** Put `=TYPE(B2)` in column C and fill it down to row 5, then read the code for each row.

**Solution:**

```excel
=TYPE(B2)
```

**Answer:** Row 2 returns `1`, row 3 returns `2`, row 4 returns `4`, and row 5 returns `16`. Row 3 is the one to fix before loading, because its text value will not add to a total.

<!-- Image 2: Type Codes in an Audit Column. See Images/Information/TYPE.md -->

### Problem 2: A Formula Result That Looks Like a Number

A cell in column C joins the number in A2 with an empty string, so the result looks like a number. A2 holds 42.

**Task:** Determine the type of the value shown in C2 with the formula `=A2&""`.

**Solution:**

```excel
=TYPE(C2)
```

**Answer:** `2`. The joining operator turns the number into text, so C2 returns text even though it displays 42.

## Use Cases

### Checking Formula Results

**Scenario:** A pricing sheet looks up a cost, but the lookup sometimes returns an error. The total should count an error as 0 without hiding real numbers.

```excel
=IF(TYPE(C2)=16, 0, C2)
```

**Why It Works:** The formula tests the type of C2 before using it. Only an error (code 16) is replaced with 0, and every other value passes through unchanged.

### Import Validation

**Scenario:** A payment file arrives with amounts that sometimes sit in cells as text. A helper column flags each amount that is not a number.

```excel
=IF(TYPE(B2)=1, B2, "Check value")
```

**Why It Works:** Numbers return 1 and pass through. Text amounts return 2 and display the warning, so they can be corrected before the total is calculated.

### Mixed Data Column Audits

**Scenario:** A column of customer account numbers should contain numbers only. A reviewer needs to see which rows break that rule.

```excel
=IF(TYPE(A2)=2, "Text", "OK")
```

**Why It Works:** The label marks each text entry, so a filter on the label shows every row that needs a fix.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected `2` | A number is stored as text, often from an import. | Convert the value with VALUE, or re-enter it as a number. |
| `16` | The argument evaluates to an error value. | Handle the error with IFERROR, or fix the formula that produces it. |
| `64` | A range or array was passed where a single value is expected. | Pass one cell to get a single code, and summarize the codes separately. |
| Type does not match the formula | TYPE reports the displayed result, not the formula itself. | Use ISFORMULA to test whether a cell holds a formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available; the Microsoft page lists no version restriction | Uses codes 1, 2, 4, 16, 64 and 128. Code 128 is labeled compound data. |
| Google Sheets | Available | Uses the same codes. Code 128 is described as other cell types, such as in-cell images and sparklines. |

## Tips and Best Practices

- Use TYPE in an audit column, then filter on the codes to find the rows that need attention.
- Test for text before you do arithmetic on imported data, because a text number fails silently in many formulas.
- Use ISNUMBER when you only need a yes or no answer for a number, since it reads more clearly in an IF.
- Remember that TYPE describes the result a cell displays, so a formula that returns text is reported as text.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ISERROR](ISERROR.md) | Tests for any error value and returns TRUE or FALSE. |
| [ISFORMULA](ISFORMULA.md) | Tests whether a cell holds a formula, which TYPE cannot do. |
| [ISLOGICAL](ISLOGICAL.md) | Tests whether a value is TRUE or FALSE. |
| [ISNUMBER](ISNUMBER.md) | Tests whether a value is a number and returns TRUE or FALSE. |
| [ISTEXT](ISTEXT.md) | Tests whether a value is text and returns TRUE or FALSE. |
| [N](N.md) | Converts a logical value or date to a number, which can help when a formula expects one. |

## Official Documentation

- [Microsoft Support: TYPE function](https://support.microsoft.com/en-us/excel/functions/type-function)
- [Google Docs Editors Help: TYPE](https://support.google.com/docs/answer/3267375)
