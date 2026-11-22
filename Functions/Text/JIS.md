---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Text Manipulation
use-case:
  - Japanese Catalog Labels
  - Japanese Product Names
related:
  - ASC
  - CHAR
  - DBCS
  - LENB
  - UNICHAR
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/jis-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Full Width Convert
  - Zenkaku Convert
tags:
  - dbcs
  - excel
  - full-width
  - japanese
  - text-conversion
---

# JIS

## Description

**JIS** converts half-width (single-byte) characters in a text string to full-width (double-byte) characters. In Japanese language settings, half-width English letters and half-width katakana become their full-width forms. For example, `JIS("ABC")` returns full-width letters, and `JIS("ｴｸｾﾙ")` returns `エクセル`.

Text that contains no half-width English letters or katakana is returned unchanged. Spaces, kanji, hiragana and full-width characters that are already present remain as they are.

The function is designed for Japanese workbooks. Microsoft notes that the name and the characters it converts depend on the language settings of the computer. In a workbook set to another language, the result may differ from the Japanese behavior described here. Test the output on a machine with the same settings as the people who will read the workbook.

JIS is the reverse of the ASC function, which converts full-width characters to half-width. Use JIS when a Japanese label or product name must match the full-width style of a catalog.

## Syntax

```excel
=JIS(text)
```

<!-- Image 1: JIS Conversion Direction. See Images/Text/JIS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to convert, either as a literal in quotes or as a reference to a cell that holds the text. Text with no half-width letters or katakana is returned unchanged. |

### Return Value

The converted text as a text string. The function does not return a number. Text that needs no conversion comes back unchanged, so the function does not return an error for ordinary text.

## Examples

### Example 1: Half-Width Letters

```excel
=JIS("EXCEL")
```

**Result:** `ＥＸＣＥＬ`

Each half-width Latin letter becomes its full-width form in Japanese settings. The output looks wider than the input.

### Example 2: Half-Width Katakana

```excel
=JIS("ｴｸｾﾙ")
```

**Result:** `エクセル`

Each half-width katakana character becomes its full-width counterpart, so the word is displayed at the standard width.

### Example 3: Converting a Cell

```excel
=JIS(A2)
```

Where A2 contains `ｶﾀｶﾅ`

**Result:** `カタカナ`

A cell reference works the same as a literal string. The original cell is not changed.

### Example 4: Text Already in Full Width

```excel
=JIS("東京")
```

**Result:** `東京`

Kanji are already full-width, so the function returns them unchanged.

### Example 5: Combining With LEN to Compare Widths

```excel
=LEN(A3) - LEN(JIS(A3))
```

Where A3 contains `ABC`, which is three half-width letters

**Result:** `0`

The character count does not change, because each letter is still one character. The difference appears in display width and byte count, which LENB reports for double-byte text.

## Story Problems

### Problem 1: Converting Katakana Product Names

A Japanese wholesaler stores product names in half-width katakana in A2 because its old system required it. The new catalog uses the standard full-width form.

| Product Name |
| --- |
| ｴｸｾﾙ |

**Task:** Convert the name in A2 to full-width katakana for the catalog.

**Solution:**

```excel
=JIS(A2)
```

**Answer:** `エクセル`. Each half-width katakana character in A2 is replaced with its full-width form.

<!-- Image 2: Half-Width Katakana Converted to Full Width. See Images/Text/JIS.md -->

### Problem 2: Preparing Order Codes

A shop keeps order codes in half-width letters for barcodes, and the printed invoice template needs full-width letters for the code column.

| Order Code |
| --- |
| ABC |
| 東京店 |

**Task:** Convert each code in A2:A3 to full width and state the result for both rows.

**Solution:**

```excel
=JIS(A2)
```

Copy the formula down to row 3.

**Answer:** Row 2 returns `ＡＢＣ`. Row 3 returns `東京店` unchanged, because it already contains full-width characters.

## Use Cases

### Japanese Catalog Labels

**Scenario:** A label printer requires full-width text, but the product list was imported from a system that stores half-width katakana.

```excel
=JIS(B2)
```

**Why It Works:** The formula converts the imported text at the time of printing without changing the source column. Check the result on a sample label before printing a full batch.

### Mixed Japanese and Latin Product Names

**Scenario:** A catalog mixes Japanese words with Latin brand names, and the brand names must match the full-width style of the Japanese text.

```excel
=JIS(C2)
```

**Why It Works:** Latin letters are converted, and kanji are left alone, so one formula handles both kinds of text in the same cell.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The function is not available in the platform in use. | Run the formula in Excel with Japanese language support. |
| No visible change | The text is already full-width or has no half-width letters or katakana. | Check the input with LEN and the source characters. |
| Unexpected output in another language | The function depends on the computer language settings. | Set the language to Japanese on the machine that runs the formula. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Japanese language settings. | Converts half-width English letters and katakana. Behavior depends on the language settings. |
| Google Sheets | Not available. | Sheets has no built-in JIS function. Run the conversion in Excel, or use ASC in Excel for the reverse conversion. |

## Tips and Best Practices

- Test the function on a machine that uses the same language settings as the rest of the team.
- Keep a copy of the original half-width text, because the conversion is not reversed automatically.
- Use JIS on display or export columns, and keep codes used for lookups in one consistent form.
- Use ASC when a full-width code must be converted back to half-width for a barcode system.
- Check printed labels on a sample sheet before converting a full list.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ASC](ASC.md) | Converts full-width characters to half-width, the reverse of JIS. |
| [DBCS](DBCS.md) | Another Japanese text function that handles double-byte characters. Compare its rules before choosing one. |
| [LENB](LENB.md) | Counts bytes, which shows the effect of full-width characters on storage width. |
| [CHAR](CHAR.md) | Returns a character from a code number, useful for building single characters. |
| [UNICHAR](UNICHAR.md) | Returns a character from a Unicode number. |

## Official Documentation

- [Microsoft Support: JIS function](https://support.microsoft.com/en-us/excel/functions/jis-function)
