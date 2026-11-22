---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Text Manipulation
use-case:
  - Imported Catalog Cleanup
  - Japanese Product Codes
  - Search Key Normalization
related:
  - CHAR
  - DBCS
  - LEN
  - LENB
  - TRIM
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/asc-function
  - https://support.google.com/docs/answer/9061514
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Half Width Conversion
tags:
  - double-byte
  - excel
  - japanese-text
  - sheets
  - text-conversion
---

# ASC

## Description

**ASC** converts full-width (double-byte) characters to half-width (single-byte) characters. Full-width English letters and full-width katakana, which occupy two character positions on a Japanese system, become their standard-width equivalents. Text that contains no full-width characters comes back unchanged, so the function is safe to apply to a whole column.

Use ASC when data arrives from a Japanese system or a form that stores codes and names in full-width form, and the rest of the workbook expects standard characters. Matching a code with a lookup function fails when one side is full-width and the other is not, so converting both sides to half-width first prevents silent misses.

Microsoft describes ASC for double-byte character set (DBCS) languages such as Japanese. Google Sheets describes it as converting full-width ASCII and katakana characters. Standard-width characters are left alone in both products. The documentation does not list every character that changes, so test a sample of your own data before you rely on the output.

<!-- Image 1: Full-Width to Half-Width Conversion. See Images/Text/ASC.md -->

## Syntax

```excel
=ASC(text)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text, or a cell reference that contains text, to convert. Half-width characters and other standard-width characters are returned unchanged. |

### Return Value

Text in which full-width letters and katakana are replaced by half-width characters. Text without full-width characters is returned as it was.

## Examples

### Example 1: Converting Full-Width Katakana

```excel
=ASC(A2)
```

Where `A2` contains the full-width word ペン (pen).

**Result:** `ﾍﾟﾝ`

Each full-width katakana character becomes its half-width form. The output looks shorter on screen, but it still reads the same word.

### Example 2: Converting Full-Width Letters

```excel
=ASC(A3)
```

Where `A3` contains the full-width text ＡＢＣ.

**Result:** `ABC`

Full-width English letters change to standard-width letters.

### Example 3: Text Already Half-Width

```excel
=ASC("EXCEL")
```

**Result:** `EXCEL`

Standard-width letters are not changed, so the output matches the input.

### Example 4: Checking Whether a Conversion Was Needed

```excel
=ASC(A2)=A2
```

**Result:** `FALSE` when `A2` contains full-width characters, `TRUE` when it does not.

Comparing the converted text with the original is a quick way to flag rows that changed.

<!-- Image 2: Converted Versus Unchanged Text. See Images/Text/ASC.md -->

## Story Problems

### Problem 1: Supplier Codes With Full-Width Letters

A warehouse receives supplier codes typed in full-width letters.

| Code | Product |
| --- | --- |
| ＫＡＢ | Pencil |
| ＺＯＮ | Eraser |
| ＭＡＸ | Ruler |

**Task:** Create a half-width version of each code in column C so the scanner can read it.

**Solution:**

```excel
=ASC(A2)
```

Fill this formula down to `C4`.

**Answer:** `KAB`, `ZON` and `MAX`, because each full-width letter becomes its standard-width letter.

### Problem 2: Checking Which Entries Need Conversion

A data team tests two entries in `B2:B3`.

| Entry |
| --- |
| ＯＫ |
| OK |

**Task:** Use a formula in `C2` that returns `TRUE` when an entry is already half-width.

**Solution:**

```excel
=ASC(B2)=B2
```

**Answer:** `FALSE` for `ＯＫ`, which needs conversion, and `TRUE` for `OK`, which does not.

## Use Cases

### Japanese Order Export Cleanup

**Scenario:** Orders exported from a Japanese system contain full-width product codes that the warehouse scanner cannot read.

```excel
=ASC(A2)
```

**Why It Works:** The formula returns a standard-width code for each row, and the scanner reads the new column. Keep the original column so the change can be audited.

### Matching Keys Across Systems

**Scenario:** A CRM stores customer codes in half-width form, while a billing sheet stores the same codes in full-width form.

```excel
=VLOOKUP(ASC(A2), Billing!A:B, 2, FALSE)
```

**Why It Works:** The lookup key is converted before the match, so both sides use the same characters. Test a few known rows first, because an unconverted character still causes a miss.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Text looks unchanged | The text is already half-width, or it contains a symbol the function does not convert. | Compare with `=ASC(A2)=A2` and test a sample of rows. |
| Some full-width symbols remain | The documentation does not list every character that converts. | Replace the remaining characters with SUBSTITUTE. |
| Results differ between computers | Excel behavior depends on the language settings of the system. | Test on the same language setting that the team uses. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Designed for double-byte character set languages such as Japanese. |
| Google Sheets | Available | Converts full-width ASCII and katakana to half-width. Standard-width characters are unchanged. |

## Tips and Best Practices

- Test a sample of rows first, because the documentation does not list every character that changes.
- Apply TRIM before or after conversion to remove stray spaces.
- Keep the original column so you can compare the results and undo a bad conversion.
- Convert both sides of a lookup key so the match does not fail on character width.
- Use LENB when a field limit is measured in bytes rather than characters.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHAR](CHAR.md) | Returns a character from a code number, which is useful for checking character codes. |
| [DBCS](DBCS.md) | Converts half-width letters and katakana to full-width. It is the reverse of ASC. |
| [LEN](LEN.md) | Counts characters, so you can compare lengths before and after conversion. |
| [LENB](LENB.md) | Counts bytes, which matters for double-byte text. |
| [TRIM](TRIM.md) | Removes extra spaces that often appear alongside full-width text. |

## Official Documentation

- [Microsoft Support: ASC function](https://support.microsoft.com/en-us/excel/functions/asc-function)
- [Google Docs Editors Help: ASC](https://support.google.com/docs/answer/9061514)
