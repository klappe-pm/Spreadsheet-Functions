---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Text Manipulation
  - Type Checking
use-case:
  - Mixed Column Cleanup
  - Text Input Checks
related:
  - ISNUMBER
  - ISTEXT
  - TEXT
  - VALUE
  - VALUETOTEXT
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/t-function
  - https://support.google.com/docs/answer/3094138
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Keep Text Only
  - Text Only Value
tags:
  - data-cleaning
  - excel
  - sheets
  - text-conversion
---

# T

## Description

**T** returns its argument when that argument is text. When the argument is a number or a logical value (TRUE or FALSE), T returns an empty text string, which displays as a blank cell. It works as a text filter: fill the formula down a column that mixes names, codes and numbers, and only the text entries come back.

Use T when you need to keep the text entries from a mixed column, or when a formula should return a blank for non-text values. It is rarely needed in practice because spreadsheet programs convert values automatically. Microsoft and Google both describe it as a function included mainly for compatibility with formulas from other spreadsheet programs.

T does not format numbers or dates. To display a number or date as text in a specific pattern, use TEXT. To test whether a value is text without changing it, use ISTEXT.

## Syntax

```excel
=T(value)
```

<!-- Image 1: Syntax Anatomy. See Images/Text/T.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value to test. It can be a text string, a cell reference, or a formula that returns a value of any type. |

### Return Value

Text. When `value` is text, T returns that text unchanged. When `value` is a number, a date or a logical value, T returns an empty text string. When `value` is an error value, Google Sheets returns the error.

## Examples

The examples use this small column. Column A holds the text Rainfall in `A2`, the number 19 in `A3`, and the logical value TRUE in `A4`.

### Example 1: Text Value

```excel
=T(A2)
```

**Result:** `Rainfall`

The cell holds text, so T returns it unchanged.

### Example 2: Number Value

```excel
=T(A3)
```

**Result:** blank cell (empty text)

The number 19 is not text, so T returns an empty string. The number in `A3` itself is not changed.

### Example 3: Logical Value

```excel
=T(A4)
```

**Result:** blank cell (empty text)

TRUE is a logical value, so T returns an empty string.

### Example 4: Label the Non-Text Results

```excel
=IF(T(A3)="","Not text",T(A3))
```

**Result:** `Not text`

Wrapping T in IF replaces the blank result with a label, so a reader can see why the cell is empty.

### Example 5: Build Text From a Text Value

```excel
=T(A2&" 2025")
```

**Result:** `Rainfall 2025`

The ampersand joins the text to another string, and the result is text, so T returns it unchanged.

<!-- Image 2: Mixed Column Before and After T. See Images/Text/T.md -->

## Story Problems

### Problem 1: Keep Only the Text Labels

A survey export mixes region names with numeric codes in one column. The report needs only the names.

| Entry |
| --- |
| North |
| 4402 |
| West |
| TRUE |
| South |

**Task:** Enter `=T(A2)` in `B2`, then fill it down to `B6` so that column B holds only the region names.

**Solution:**

```excel
=T(A2)
```

**Answer:** `B2` shows North, `B3` is blank, `B4` shows West, `B5` is blank and `B6` shows South. Three text labels remain, and the two non-text entries leave blanks.

### Problem 2: Flag Each Entry as Text or Not Text

The same list is in `A2:A6`. The reviewer wants a label beside each entry.

**Task:** Enter a formula in `B2` that returns Text for text entries and Not text for everything else, then fill it down to `B6`.

**Solution:**

```excel
=IF(T(A2)="","Not text","Text")
```

**Answer:** Column B reads Text, Not text, Text, Not text and Text, in the same order as the list.

## Use Cases

### Mixed Column Cleanup

**Scenario:** An import places region names, numeric codes and yes or no flags in one column. A summary sheet needs only the region names.

```excel
=T(A2)
```

**Why It Works:** T passes text through and blanks everything else. Fill the formula down, then copy the results as values into the summary so the helper formulas can be removed.

### Text Input Checks

**Scenario:** A form template expects a text answer in column B for every row, and a reviewer wants to spot rows that contain a number or a date instead.

```excel
=IF(T(B2)="","Enter text","OK")
```

**Why It Works:** Dates are stored as numbers, so a date in B2 returns an empty result and the row is flagged. Add a note to the template so reviewers know that dates belong in a separate column.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Blank result | The input is a number, a date or a logical value, so T returns an empty string. | Use TEXT to show a number as text in a set format, or join it with `&""`. |
| Number stays text | A value stored as text, such as "19", is still text after T. | Use VALUE to convert the text to a number before arithmetic. |
| Date disappears | Dates are numbers in the sheet, so T returns an empty string for them. | Use TEXT with a date pattern, such as `=TEXT(A2,"yyyy-mm-dd")`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Returns text unchanged and an empty string for numbers and logical values. |
| Google Sheets | Available | Same results for text, numbers and logical values. Returns an error value unchanged. |

## Tips and Best Practices

- Use ISTEXT when you need a TRUE or FALSE answer rather than a filtered value.
- Pair T with IF so that blank results carry a label that explains them.
- Do not use T to change numbers into text; use TEXT for that.
- Convert text numbers with VALUE before you add them or compare them as numbers.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ISNUMBER](../Information/ISNUMBER.md) | Tests whether a value is a number and returns TRUE or FALSE. |
| [ISTEXT](../Information/ISTEXT.md) | Tests whether a value is text and returns TRUE or FALSE. |
| [TEXT](../Text/TEXT.md) | Formats a number, date or time as text in a set pattern. |
| [VALUE](../Text/VALUE.md) | Converts text that looks like a number into a number. |
| [VALUETOTEXT](../Text/VALUETOTEXT.md) | Converts a value of any type to text. |

## Official Documentation

- [Microsoft Support: T function](https://support.microsoft.com/en-us/excel/functions/t-function)
- [Google Docs Editors Help: T](https://support.google.com/docs/answer/3094138)
