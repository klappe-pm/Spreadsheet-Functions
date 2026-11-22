---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Roman and Base Conversion
purpose:
  - Number Base Conversion
use-case:
  - Chapter Numbering Cleanup
  - Document Indexing
  - Legacy Record Conversion
related:
  - CONVERT
  - DEC2HEX
  - ROMAN
  - TEXT
  - VALUE
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/arabic-function
  - https://support.google.com/docs/answer/3238301
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Roman Numeral Converter
  - Roman To Arabic
tags:
  - conversion
  - excel
  - roman-numerals
  - sheets
---

# ARABIC

## Description

**ARABIC** converts a Roman numeral written as text into a standard Arabic (decimal) number. For example, `ARABIC("XIV")` returns 14 and `ARABIC("MMXIII")` returns 2013. The function is the inverse of `ROMAN`, which converts a number into a Roman numeral.

Use ARABIC when a record uses Roman numerals, such as chapter headings, document series, or older catalog codes, and you need the number for sorting, lookups, or arithmetic. The function ignores letter case, so `"mxmvii"` and `"MXMVII"` both return 1997. Leading and trailing spaces are also ignored.

ARABIC accepts a text argument only. It does not accept numbers, dates or other types of input. A minus sign placed before the text, as in `"-MMXI"`, returns a negative value. An empty string returns 0. Text that is not a valid Roman numeral returns `#VALUE!`.

## Syntax

```excel
=ARABIC(text)
```

<!-- Image 1: Roman Symbols and Their Values. See Images/Math & Trig/ARABIC.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | A Roman numeral in quotation marks, an empty string (`""`), or a cell reference that contains text. Microsoft Excel allows up to 255 characters. |

### Return Value

The Arabic number equal to the Roman numeral. A minus sign before the text gives a negative result. An empty string returns 0. Text that is not a valid Roman numeral, including numbers and dates, returns `#VALUE!`.

## Examples

### Example 1: Short Numeral

```excel
=ARABIC("XIV")
```

**Result:** `14`

X is 10, IV is 4, and the total is 14.

### Example 2: Year

```excel
=ARABIC("MMXIII")
```

**Result:** `2013`

Two M symbols give 2000, and XIII adds 13.

### Example 3: Negative Value

```excel
=ARABIC("-MMXI")
```

**Result:** `-2011`

The minus sign goes before the text. It applies to the whole numeral.

### Example 4: Case Is Ignored

Numeral in `A2` is `mxmvii`.

```excel
=ARABIC(A2)
```

**Result:** `1997`

Lowercase letters are read the same as uppercase letters.

### Example 5: Guarding Against Invalid Text

Code in `B2` is `ABC`.

```excel
=IFERROR(ARABIC(B2),"Not Roman")
```

**Result:** `Not Roman`

Letters A, B and C are not Roman numeral symbols, so ARABIC returns `#VALUE!`, which `IFERROR` replaces with a label.

## Story Problems

### Problem 1: Converting Volume Numbers

A library archive labels four volumes with Roman numerals. The archive needs the decimal numbers and their total.

| Volume | Roman Code |
| --- | --- |
| V-1 | XLII |
| V-2 | LXXVIII |
| V-3 | MCMXCIX |
| V-4 | CDXLIV |

**Task:** Convert each code to a number in column C, then total the four numbers.

**Solution:**

```excel
=ARABIC(B2)
```

Fill the formula down from `C2` to `C5`, then use `=SUM(C2:C5)` in a cell below the list.

**Answer:** `2563`. The values are 42, 78, 1999 and 444, and 42 + 78 + 1999 + 444 = 2563.

### Problem 2: Finding an Invalid Adjustment Code

A stock system stores adjustment codes in Roman numerals. A negative adjustment uses a minus sign before the numeral. One code was typed incorrectly.

| Adjustment | Code |
| --- | --- |
| A-1 | -XII |
| A-2 | XX |
| A-3 | |
| A-4 | ABC |

**Task:** Convert each code and identify the one that fails.

**Solution:**

```excel
=ARABIC(B2)
```

Fill the formula down from `C2` to `C5`.

**Answer:** A-1 returns `-12`, A-2 returns `20` and A-3 returns `0` because its code is an empty string. A-4 returns `#VALUE!`, so the code `ABC` must be corrected before the adjustment is posted.

<!-- Image 2: Adjustment Codes With One Error. See Images/Math & Trig/ARABIC.md -->

## Use Cases

### Chapter Numbering Cleanup

**Scenario:** An editor receives a manuscript with chapter numbers typed as Roman numerals and needs them as numbers to sort the table of contents.

```excel
=IFERROR(ARABIC(ChapterLabel),"Check label")
```

**Why It Works:** The formula converts each label and flags any label that is not a valid numeral, so the editor can fix it without losing the rest of the list.

### Document Indexing

**Scenario:** A records team indexes historical documents whose series numbers use Roman numerals, and the index must be searchable by decimal value.

```excel
=ARABIC(SeriesCode)
```

**Why It Works:** The decimal result can be sorted and compared, while the original code stays in its own column for reference.

### Legacy Record Conversion

**Scenario:** A system migration moves codes from an older database that stored Roman numerals, and the new system needs numeric keys.

```excel
=ARABIC(LegacyCode)
```

**Why It Works:** The converted numbers become the new keys. Check for `#VALUE!` results before the migration so invalid codes are reviewed first.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The text is not a valid Roman numeral, or it is a number or date. | Correct the text or check the source data. |
| Result is 0 | The cell is empty or contains an empty string. | Treat blanks separately, or enter a numeral. |
| Unexpected negative value | A minus sign is present before the text. | Remove the sign if the value should be positive. |
| `#NAME?` | The function name is misspelled. | Type `ARABIC`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Accepts up to 255 characters, ignores case, and returns 0 for an empty string. Negative values use a minus sign before the text. |
| Google Sheets | Available | Same purpose and text input. Google's page describes the value of the numeral as falling between 1 and 3999 and does not describe other inputs. |

## Tips and Best Practices

- Use `IFERROR` around ARABIC when a column may contain labels that are not numerals, so one bad entry does not spoil the list.
- Test a sample of converted values against known years or sequence numbers before a large conversion.
- Keep the original code in its own column so the conversion can be audited.
- Use `ROMAN` to check the result in reverse when you need to confirm a conversion.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ROMAN](ROMAN.md) | Converts a number to a Roman numeral. The reverse of ARABIC. |
| [DEC2HEX](../Engineering/DEC2HEX.md) | Converts a decimal number to hexadecimal, another number base. |
| [CONVERT](../Engineering/CONVERT.md) | Converts a number between units of measure. |
| [TEXT](../Text/TEXT.md) | Formats a number as text, which can be useful before a numeral is built. |
| [VALUE](../Text/VALUE.md) | Converts text that holds a plain number into a number. |

## Official Documentation

- [Microsoft Support: ARABIC function](https://support.microsoft.com/en-us/excel/functions/arabic-function)
- [Google Docs Editors Help: ARABIC](https://support.google.com/docs/answer/3238301)
