---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
purpose:
  - Data Validation
  - Type Checking
use-case:
  - Import Cleanup
  - Name Field Validation
related:
  - ISBLANK
  - ISLOGICAL
  - ISNUMBER
  - ISTEXT
  - NOT
level: 1
source:
  - https://support.microsoft.com/en-us/excel/is-functions
  - https://support.google.com/docs/answer/3093295
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - data-validation
  - excel
  - information
  - sheets
  - type-checking
---

# ISNONTEXT

## Description

**ISNONTEXT** returns TRUE for every value that is not text. That includes numbers, dates, logical values, errors and blank cells. It returns FALSE only for text, including numbers typed as text and text strings that contain spaces.

Use ISNONTEXT to flag entries in a column that should hold names or codes but contain something else, such as a number that lost its leading zeros during an import. It is the logical opposite of ISTEXT, which means `ISNONTEXT(value)` gives the same result as `NOT(ISTEXT(value))`.

Blank cells are a common surprise. Excel documents that a blank cell returns TRUE, so combine the test with ISBLANK when blank entries need a different label.

## Syntax

```excel
=ISNONTEXT(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISNONTEXT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value or cell reference to test. Text, numbers, logical values, errors and blanks are all accepted. |

### Return Value

TRUE when `value` is not text, or refers to a cell that does not hold text, including a blank cell. FALSE when `value` is text, or refers to a cell that holds text.

## Examples

### Example 1: A Number

Cell A2 holds `1250`.

```excel
=ISNONTEXT(A2)
```

**Result:** `TRUE`

The cell holds a number, which is not text, so the function returns TRUE.

### Example 2: A Text String

```excel
=ISNONTEXT("cat")
```

**Result:** `FALSE`

The string "cat" is text, so the function returns FALSE.

### Example 3: A Blank Cell

Cell B2 is empty.

```excel
=ISNONTEXT(B2)
```

**Result:** `TRUE`

Excel treats a blank cell as not text, so the function returns TRUE. Test with ISBLANK first if blanks need their own label.

### Example 4: Checking a Name Entry

Cell C2 holds the text `Acme`.

```excel
=IF(ISNONTEXT(C2),"Enter a name","OK")
```

**Result:** `OK`

Text passes the check, so the label stays OK.

## Story Problems

### Problem 1: Mixed Entries in a Name Column

A registration form collects names in column B. Some entries arrived as numbers or logical values during a data import. The clerk wants the count of entries that are not text.

| Entry | Field Value |
| --- | --- |
| 1 | Lena |
| 2 | 2204 |
| 3 | Omar |
| 4 | TRUE |
| 5 | 98 |

**Task:** Count the non-text values in `B2:B6`.

**Solution:**

```excel
=SUMPRODUCT(ISNONTEXT(B2:B6)*1)
```

**Answer:** `3`. The values 2204, TRUE and 98 are not text.

### Problem 2: Product Codes That Lost Their Zeros

A warehouse exports product codes. Some codes start with zeros, and the import changed a few of them to plain numbers, which dropped the leading zeros. Codes must be text before they reach the stock system.

| Code |
| --- |
| 00417 |
| 417 |
| B22 |
| 1080 |
| 2210 |

**Task:** Count the codes in `A2:A6` that are not text and need conversion.

**Solution:**

```excel
=SUMPRODUCT(ISNONTEXT(A2:A6)*1)
```

**Answer:** `2`. Codes 417 and 1080 are numbers, so both need conversion.

<!-- Image 2: Product Codes Check. See Images/Information/ISNONTEXT.md -->

## Use Cases

### Name Field Validation

**Scenario:** A signup sheet should accept only text in the name column, and a number in that column usually means a mistake.

```excel
=IF(ISNONTEXT(A2),"Enter a name","OK")
```

**Why It Works:** The check runs on every row. Any row that holds a number, a date or a logical value gets the warning, so the reviewer can fix it before it reaches the mailing list.

### Import Cleanup

**Scenario:** A data import mixes text codes and numeric codes. Numeric codes must become text before the file is uploaded.

```excel
=IF(ISNONTEXT(A2),"Convert to text","OK")
```

**Why It Works:** Numbers that were stored without their leading zeros show up immediately, so the team can reformat those cells as text and restore the original codes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `TRUE` for a blank cell | Excel treats blank cells as not text. | Test with ISBLANK first, then ISNONTEXT for the rest. |
| `FALSE` for a number typed as text | The entry "1234" is text, even though it looks like a number. | Test the converted value with `=ISNUMBER(VALUE(A2))` if it must be numeric. |
| `FALSE` for a cell that looks empty | The cell holds a space or another nonprinting character, which counts as text. | Remove the characters with TRIM or CLEAN. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Microsoft 365 for Mac, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016. | Returns TRUE for blank cells. Numbers stored as text return FALSE. |
| Google Sheets | Available | Same syntax. An empty string returns FALSE, and whitespace or nonprinting characters count as text. |

## Tips and Best Practices

- Pair with ISBLANK when a blank entry must be handled separately from non-text values.
- Use ISTEXT when the goal is to count text instead of non-text.
- Use TRIM and CLEAN before testing imported text so hidden characters do not cause surprises.
- Use SUMPRODUCT with `*1` to count non-text values in a range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ISTEXT](ISTEXT.md) | The opposite test, which returns TRUE for text. |
| [ISNUMBER](ISNUMBER.md) | Tests for numbers only, which is narrower than ISNONTEXT. |
| [ISLOGICAL](ISLOGICAL.md) | Tests for TRUE and FALSE values, one of the types ISNONTEXT includes. |
| [ISBLANK](ISBLANK.md) | Separates empty cells from other non-text values. |
| [NOT](../Logical/NOT.md) | Reverses ISTEXT, which gives the same result as ISNONTEXT. |

## Official Documentation

- [Microsoft Support: IS functions](https://support.microsoft.com/en-us/excel/is-functions)
- [Google Docs Editors Help: ISNONTEXT](https://support.google.com/docs/answer/3093295)
