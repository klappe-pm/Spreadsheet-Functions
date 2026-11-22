---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Combining Mixed Values Into Keys
  - Logging Mixed Column Values
  - Preparing Strict Text for Formulas
related:
  - CONCAT
  - ISTEXT
  - T
  - TEXT
  - VALUE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/valuetotext-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Value To Text
tags:
  - conversion
  - excel
  - format-control
  - text
---

# VALUETOTEXT

## Description

**VALUETOTEXT** returns any value as text. Text values pass through unchanged, and numbers, dates, logical values and errors are converted to their text form. Use it when a column mixes types, such as TRUE, numbers and words, and every entry must be joined, logged or compared as text.

The function has two output formats. The default, `0`, gives the concise text that matches how the value looks in a cell with General formatting. The strict format, `1`, adds quotation marks around text and escape characters, so the result can be pasted into the formula bar as a valid value. Booleans, numbers and errors are not quoted in strict format.

VALUETOTEXT is an Excel function, and it is not available in Google Sheets. For a formatted number such as a currency or a percentage, use TEXT instead, because VALUETOTEXT does not apply a number format.

## Syntax

```excel
=VALUETOTEXT(value, [format])
```

<!-- Image 1: Concise and Strict Output. See Images/Text/VALUETOTEXT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | Yes | The value to convert. Text is returned unchanged, and other values are converted to text. |
| `format` | No | `0` for concise output (the default) or `1` for strict output. Any other number returns `#VALUE!`. |

### Return Value

A text string. The function returns `#VALUE!` when `format` is anything other than `0` or `1`.

## Examples

### Example 1: Logical Value in Concise Format

Cell `A2` contains `TRUE`.

```excel
=VALUETOTEXT(A2)
```

**Result:** `TRUE`

The default format is `0`, so the output is the plain word. The result is text, so it can be joined with other text.

### Example 2: Number With Decimals

Cell `A3` contains `2048.5`.

```excel
=VALUETOTEXT(A3,0)
```

**Result:** `2048.5`

The number keeps its decimal part. Because the result is text, a formula that expects a number will not treat it as one.

### Example 3: Text in Strict Format

```excel
=VALUETOTEXT("Hello",1)
```

**Result:** `"Hello"`

Strict format puts quotation marks around the text, so the output is shaped like a text constant in a formula.

### Example 4: Number in Strict Format

Cell `A4` contains `42`.

```excel
=VALUETOTEXT(A4,1)
```

**Result:** `42`

Numbers are not quoted in strict format, so the output is the same as the concise output.

<!-- Image 2: Concise Versus Strict Output. See Images/Text/VALUETOTEXT.md -->

### Example 5: Invalid Format Argument

```excel
=VALUETOTEXT(A4,2)
```

**Result:** `#VALUE!`

Only `0` and `1` are valid format arguments, so the formula returns an error.

## Story Problems

### Problem 1: Mixed Values in an Audit Column

An inspector logged four readings in one column. Each reading has a different type: a pass flag, a count, a word and a fraction.

| Reading |
| --- |
| TRUE |
| 1500 |
| Hello |
| 0.25 |

**Task:** Convert each reading to concise text in column B so the whole column can be joined into one log line.

**Solution:**

```excel
=VALUETOTEXT(A2,0)
```

Fill the formula down from `B2` to `B5`.

**Answer:** `TRUE`, `1500`, `Hello` and `0.25`. Each result is text, so `ISTEXT` returns TRUE for all four cells.

### Problem 2: Building a Text Key From Mixed Cells

A parts list uses a numeric ID in cell `A2` and a letter code in cell `B2`. The team wants a text key such as `1047-Q3` for lookups in another system.

| ID | Code |
| --- | --- |
| 1047 | Q3 |

**Task:** Join the ID and the code into one text key with a hyphen between them.

**Solution:**

```excel
=VALUETOTEXT(A2,0)&"-"&VALUETOTEXT(B2,0)
```

**Answer:** `1047-Q3`. The concise format gives `1047` for the number and `Q3` for the text, and the `&` operator joins them with the hyphen.

## Use Cases

### Combining Mixed Values Into Keys

**Scenario:** A warehouse builds lookup keys from a numeric ID and a text code, and some rows hold a logical flag instead of a code.

```excel
=VALUETOTEXT(A2,0)&"|"&VALUETOTEXT(B2,0)
```

**Why It Works:** Each part is converted to text first, so the join works even when a cell holds a number or TRUE.

### Logging Mixed Column Values

**Scenario:** A quality team copies a column of readings into a log that must show each entry exactly as it appears.

```excel
=TEXTJOIN(", ",TRUE,VALUETOTEXT(A2:A5,0))
```

**Why It Works:** Each entry becomes text in the same way it appears in a cell, and TEXTJOIN places them in one line. Check the result in a current Excel version, because array support varies in older releases.

### Preparing Strict Text for Formulas

**Scenario:** A developer needs the exact formula-ready form of a cell value to paste into a generated formula.

```excel
=VALUETOTEXT(B2,1)
```

**Why It Works:** Strict format quotes text and leaves numbers and logical values bare, so the output can be pasted back into a formula as a constant.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The `format` argument is not `0` or `1`. | Use `0` or `1`, or leave the argument out. |
| Quotation marks in the result | Strict format was used. | Use `0` for plain text, or remove the quotation marks with SUBSTITUTE. |
| Error in the result | The source cell contains an error value. | Fix the source cell, or wrap the source in IFERROR before converting. |
| Number lost its formatting | VALUETOTEXT does not apply a number format. | Use TEXT with a format code such as `"0.00"` when a fixed display is needed. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows and Mac), Excel for the web, Excel 2021 (Windows and Mac), and Microsoft Office | Not available in Excel 2019 or Excel 2016. |
| Google Sheets | Not available | Use TEXT for formatted text output, or the `&` operator with TEXT for joined values. |

## Tips and Best Practices

- Use format `0` for logs and keys, and format `1` only when the output must be pasted back into a formula.
- Convert each part of a join separately, so a number or logical value never reaches the `&` operator as an unexpected type.
- Use TEXT instead when a number needs a fixed display such as currency, a percentage or a set number of decimals.
- Check the Excel version before sharing a workbook, because older versions show `#NAME?` for this function.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CONCAT](../Text/CONCAT.md) | Joins text ranges; combine with VALUETOTEXT when the parts are mixed types. |
| [ISTEXT](../Information/ISTEXT.md) | Confirms that a result is text. |
| [T](../Text/T.md) | Returns text only when the argument is text, and an empty string otherwise. |
| [TEXT](../Text/TEXT.md) | Converts a number to text with a display format. |
| [VALUE](../Text/VALUE.md) | The reverse direction: converts a text string into a number. |

## Official Documentation

- [Microsoft Support: VALUETOTEXT function](https://support.microsoft.com/en-us/excel/functions/valuetotext-function)
