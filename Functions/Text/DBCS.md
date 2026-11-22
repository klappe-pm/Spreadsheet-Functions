---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Text Manipulation
use-case:
  - Full-width Form Fields
  - Japanese Label Printing
  - Japanese Mailing Lists
related:
  - ASC
  - CHAR
  - LEN
  - LENB
  - TRIM
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/dbcs-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Full Width Conversion
tags:
  - double-byte
  - excel
  - japanese-text
  - text-conversion
---

# DBCS

## Description

**DBCS** converts half-width (single-byte) English letters and katakana in a text string to full-width (double-byte) characters. It is the reverse of ASC. Text that contains none of those characters is returned unchanged, so the function is safe to apply to a whole column.

Use DBCS when a Japanese form, label or mailing list requires letters and katakana in full-width form. Apply TRIM first when the source text has stray spaces, because the spaces are kept by the conversion.

Microsoft documents DBCS for Japanese language settings, and notes that the name of the function and the characters it converts depend on the language settings of the computer. Test the output on the same language setting that the recipient uses. DBCS is available in Excel only; Google Sheets has no documented equivalent.

<!-- Image 1: Half-Width Versus Full-Width Text. See Images/Text/DBCS.md -->

## Syntax

```excel
=DBCS(text)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text, or a cell reference that contains text, to convert. Text without half-width English letters or katakana is returned unchanged. |

### Return Value

Text in which half-width English letters and katakana are replaced by their full-width forms. The documentation does not state a separate data type; the result is text.

## Examples

### Example 1: Converting a Word to Full-Width Letters

```excel
=DBCS("EXCEL")
```

**Result:** `ＥＸＣＥＬ`

Each half-width letter becomes its full-width form, which takes up two character positions.

### Example 2: Converting a Cell Value

```excel
=DBCS(A2)
```

Where `A2` contains `ABC`.

**Result:** `ＡＢＣ`

The cell value is converted in the same way as a typed string.

### Example 3: Text Already in Full-Width Form

```excel
=DBCS(A3)
```

Where `A3` contains `東京`, which is already full-width.

**Result:** `東京`

Text without half-width letters or katakana is returned unchanged.

### Example 4: Checking a Round Trip

```excel
=ASC(DBCS(A2)) = A2
```

Where `A2` contains `ABC`.

**Result:** `TRUE`

Converting to full-width and back with ASC returns the original text, so the comparison is TRUE.

<!-- Image 2: Round Trip With ASC. See Images/Text/DBCS.md -->

## Story Problems

### Problem 1: Full-Width City Codes on a Form

A Japanese form requires city codes in full-width letters. The codes are typed in half-width form in `A2:B3`.

| City | Code |
| --- | --- |
| Tokyo | TOKYO |
| Osaka | OSAKA |

**Task:** Put the full-width version of each code in column C.

**Solution:**

```excel
=DBCS(B2)
```

Fill this formula down to `C3`.

**Answer:** `ＴＯＫＹＯ` and `ＯＳＡＫＡ`, because each half-width letter becomes its full-width form.

### Problem 2: Mixed Entries

A list in `A2:A4` contains three entries: `ABC`, `東京` and `XY`.

**Task:** Convert each entry in column B, and say which entries change.

**Solution:**

```excel
=DBCS(A2)
```

Fill this formula down to `B4`.

**Answer:** `ＡＢＣ` and `ＸＹ` change, while `東京` is returned unchanged, because it already contains only full-width characters.

## Use Cases

### Full-Width Form Fields

**Scenario:** A Japanese application form requires a reference code in full-width letters, but the staff type codes in half-width form.

```excel
=DBCS(TRIM(B2))
```

**Why It Works:** TRIM removes stray spaces first, so the converted code has no extra characters. The formula can be copied into the form template column so every entry is converted the same way.

### Japanese Label Printing

**Scenario:** Mailing labels for a Japanese recipient list need the sender code in full-width letters, and the byte length must fit the label.

```excel
=DBCS(A2)
```

**Why It Works:** The conversion produces the full-width form used on the label. Check the field length with LENB, because full-width characters take up two bytes each on a double-byte system.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Text stays the same | The text has no half-width English letters or katakana. | Expected behavior. Check that the input contains the characters you expect. |
| Different characters on another computer | The function name and converted characters depend on the language settings. | Test on the same language setting as the recipient. |
| `#NAME?` in Google Sheets | The function is not available in Sheets. | Use an alternative for Sheets, or convert the text in Excel first. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Converts half-width English letters and katakana to full-width for Japanese language settings. |
| Google Sheets | Not available | No documented equivalent. ASC converts in the opposite direction. |

## Tips and Best Practices

- Apply TRIM before conversion so stray spaces are not carried into the result.
- Test a sample on the target language setting before you convert a whole column.
- Use ASC on the output to check that the round trip returns the original text.
- Check byte limits with LENB when a field is measured in bytes.
- Keep the original column so you can compare the converted values.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ASC](ASC.md) | Converts full-width text back to half-width. It is the reverse of DBCS. |
| [CHAR](CHAR.md) | Returns characters from code numbers, which is useful for building test strings. |
| [LEN](LEN.md) | Counts characters, which you can compare with LENB for double-byte text. |
| [LENB](LENB.md) | Counts bytes, which matters when a field has a byte limit. |
| [TRIM](TRIM.md) | Removes stray spaces before conversion. |

## Official Documentation

- [Microsoft Support: DBCS function](https://support.microsoft.com/en-us/excel/functions/dbcs-function)
