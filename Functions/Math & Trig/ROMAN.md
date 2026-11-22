---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Roman and Base Conversion
purpose:
  - Number Formatting
use-case:
  - Chapter Numbering
  - Document Section Labels
  - Event Edition Numbers
related:
  - ARABIC
  - BASE
  - DECIMAL
  - TEXT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/roman-function
  - https://support.google.com/docs/answer/3094153
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Arabic to Roman
  - Roman Numerals
tags:
  - conversion
  - excel
  - numerals
  - sheets
---

# ROMAN

## Description

**ROMAN** converts an Arabic number, such as 2024, into its Roman numeral form, MMXXIV. The result is text, not a number, so you cannot add or multiply it. The function accepts whole numbers from 1 to 3999. Numbers outside that range, and negative numbers, return an error in Excel.

Use ROMAN for labels that traditionally use Roman numerals: chapters, parts of a document, sections of a contract, or the edition number of an event. Because the output is text, you can join it to other labels with `&` and use it in headings without changing the underlying numbers in the sheet.

Excel accepts an optional second argument, `form`, which controls how strictly the subtraction rules are applied. The classic form, 0 or omitted, is the traditional notation, and higher forms give shorter versions that are less common in print. Google Sheets uses a similar optional argument with a different name and meaning, so check the output on each platform if the labels must match.

## Syntax

```excel
=ROMAN(number, [form])
```

<!-- Image 1: Number and Form Arguments. See Images/Math & Trig/ROMAN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | The Arabic number to convert. Must be a whole number from 1 to 3999 in Excel. Cell references and formulas are accepted. |
| `form` | No | Selects the style of the numeral. 0 or omitted gives the classic form. Values 1 to 3 give more concise forms, and 4 gives the simplified form. TRUE is classic and FALSE is simplified. |

### Return Value

Text: the Roman numeral for the number. Excel returns `#VALUE!` when the number is negative or greater than 3999. The output uses uppercase letters.

<!-- Image 2: Classic Numeral Breakdown. See Images/Math & Trig/ROMAN.md -->

## Examples

### Example 1: Current Year in Roman Numerals

```excel
=ROMAN(2024)
```

**Result:** `MMXXIV`

The two Ms stand for 2000, and XXIV stands for the remaining 24. The output is a single text string.

### Example 2: A Year With Subtraction

```excel
=ROMAN(1999)
```

**Result:** `MCMXCIX`

The classic form writes 900 as CM and 90 as XC, which is why the output contains subtraction pairs.

### Example 3: Classic Form Requested Explicitly

```excel
=ROMAN(2024,0)
```

**Result:** `MMXXIV`

A form of 0 requests the classic notation. The result matches Example 1, because classic is the default.

### Example 4: Largest Valid Number

```excel
=ROMAN(3999)
```

**Result:** `MMMCMXCIX`

3999 is the largest number Excel converts. It combines three Ms with CM, XC and IX.

### Example 5: Out of Range Input

```excel
=ROMAN(4000)
```

**Result:** `#VALUE!`

The number is greater than 3999, so the function returns an error. Check the input range before converting, as shown in the story problems.

## Story Problems

### Problem 1: Chapter Labels for a Manual

A technical manual has chapter numbers in column `A`. The editor wants each chapter heading to show its number in Roman numerals.

| Chapter | Number |
| --- | --- |
| Installation | 14 |
| Maintenance | 25 |

**Task:** Write a formula that returns the Roman numeral for Maintenance, which is chapter 25.

**Solution:**

```excel
=ROMAN(B3)
```

**Answer:** `XXV`. Chapter 25 is XX for 20 plus V for 5.

### Problem 2: Cornerstone Date

A historic building has the year 1887 carved on its cornerstone. The restoration report must show the year in classic Roman numerals.

| Item | Value |
| --- | --- |
| Year | 1887 |

**Task:** Write a formula that converts the year to Roman numerals.

**Solution:**

```excel
=ROMAN(B2)
```

**Answer:** `MDCCCLXXXVII`. The year is 1000 (M) plus 800 (DCCC) plus 80 (LXXX) plus 7 (VII).

## Use Cases

### Chapter Numbering

**Scenario:** A publisher builds chapter titles from a numbered list, and each title must show the chapter in Roman numerals.

```excel
="Chapter "&ROMAN(A2)
```

**Why It Works:** The formula joins the word Chapter and the numeral into one label. The number stays in `A2`, so reordering chapters only requires changing the number.

### Document Section Labels

**Scenario:** A legal team numbers the articles of an agreement with Roman numerals and needs the labels to appear in a contents table.

```excel
=ROMAN(B2,0)
```

**Why It Works:** The form argument is set to 0 so that the labels use the classic notation expected in legal documents. Keep the number in `B2` as a whole number.

### Event Edition Numbers

**Scenario:** A conference names each annual edition with a Roman numeral, such as Edition XXV for the twenty-fifth event.

```excel
="Edition "&ROMAN(C2)
```

**Why It Works:** The edition number in `C2` is converted and placed in the label. Validate that `C2` holds a whole number from 1 to 3999 before the formula is copied down.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The number is negative or greater than 3999. | Check the value with IF, for example `=IF(AND(A2>=1,A2<=3999),ROMAN(A2),"")`. |
| `#VALUE!` | The number is text, such as a number stored as text. | Convert the cell to a number before calling ROMAN. |
| Result cannot be summed | ROMAN returns text, not a number. | Use ARABIC to convert the numeral back to a number. |
| Labels do not match a style guide | The default classic form was not what the guide expects, or a different form was used. | Set the form argument explicitly, and test the output for the style you need. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | Optional `form` argument from 0 to 4, or TRUE and FALSE. Accepts whole numbers from 1 to 3999. |
| Google Sheets | Available | Optional `rule_relaxation` argument from 0 to 4, with 0 as the strict default. Each value relaxes a different subtraction rule, so the output may differ from Excel's form numbers. |

## Tips and Best Practices

- Use ROMAN for labels only, and keep the underlying number in its own cell for calculations.
- Use ARABIC to convert a Roman numeral back to a number.
- Check the input range before converting, because numbers outside 1 to 3999 produce errors.
- Set the form argument explicitly whenever the output must follow a specific style guide.
- Join the result with `&` to build labels such as "Chapter XIV" without retyping numbers.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ARABIC](ARABIC.md) | Converts a Roman numeral back to an Arabic number, the reverse of ROMAN. |
| [BASE](BASE.md) | Converts a number into text in another base, such as binary or hexadecimal. |
| [DECIMAL](DECIMAL.md) | Converts text in a chosen base back into a decimal number. |
| [TEXT](../Text/TEXT.md) | Formats numbers as text with patterns, for labels that need other formats. |

## Official Documentation

- [Microsoft Support: ROMAN function](https://support.microsoft.com/en-us/excel/functions/roman-function)
- [Google Docs Editors Help: ROMAN](https://support.google.com/docs/answer/3094153)
