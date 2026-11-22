---
domain: Spreadsheet Functions
category: Text
subcategory: Case Conversion
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Email Address Matching
  - Mixed Case Import Cleanup
  - Product Code Standardization
related:
  - CLEAN
  - EXACT
  - PROPER
  - TRIM
  - UPPER
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/lower-function
  - https://support.google.com/docs/answer/3094083
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Convert To Lowercase
  - Lowercase Text
tags:
  - case-conversion
  - data-cleaning
  - excel
  - sheets
  - text
---

# LOWER

## Description

**LOWER** converts every uppercase letter in a text string to lowercase. Letters that are already lowercase, digits, spaces and punctuation are returned unchanged. The result is always text, even when the input is a number.

Use LOWER when the case of a value should not affect the result. It is most useful when you store, display or group values that arrived in mixed case, such as email addresses typed by hand or product codes exported from several systems. LOWER changes what the cell holds, so use it in a helper column or a new column when you want to keep the original text.

LOWER does not need to be used before comparisons. The `=` operator and COUNTIF already ignore case. Use EXACT when you need a case-sensitive comparison, and use LOWER when you want to normalize the text itself. The companion functions UPPER and PROPER change case in the other directions.

## Syntax

```excel
=LOWER(text)
```

<!-- Image 1: LOWER Argument Layout. See Images/Text/LOWER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to convert. Enter it in quotation marks, reference a cell, or use a formula that returns text. A number is converted to text before the change, so the digits are unchanged. |

### Return Value

A text string with every uppercase letter changed to lowercase. The function returns text for any input. It does not return an error for an empty cell; an empty cell returns an empty string.

## Examples

### Example 1: Lowercasing a Literal String

```excel
=LOWER("Quarterly REPORT")
```

**Result:** `quarterly report`

The string is typed directly in the formula. Only the letters are affected.

### Example 2: Lowercasing a Cell Value

Cell `A2` contains `Ana-Lucia M. KIM`.

```excel
=LOWER(A2)
```

**Result:** `ana-lucia m. kim`

The hyphen, the period and the spaces stay exactly as they were. Only the capital letters change.

<!-- Image 2: Mixed Case Column Before and After LOWER. See Images/Text/LOWER.md -->

### Example 3: Case-Insensitive Match of Two Addresses

Cell `A2` contains `Sam.Lee@Example.com` and cell `B2` contains `sam.lee@example.COM`.

```excel
=EXACT(LOWER(A2), LOWER(B2))
```

**Result:** `TRUE`

Both values become the same lowercase text, so EXACT reports a match. Without LOWER, EXACT would return `FALSE` because it is case-sensitive.

### Example 4: Converting a Range

Cells `A2:A4` contain `NORTH`, `South` and `EAST`.

```excel
=LOWER(A2:A4)
```

**Result:** `north`, `south` and `east` in three rows

In Microsoft 365, the formula spills into the cells below it. Make sure the cells below the first result are empty.

## Story Problems

### Problem 1: Counting One Customer Across Mixed Entries

A small shop collects addresses from a web form, a phone order sheet and a trade show list. The same customer appears with different capitalization.

| Email |
| --- |
| ana@example.com |
| ANA@EXAMPLE.COM |
| ana@Example.com |
| bo@example.com |
| Ana@example.com |

**Task:** Count how many rows belong to `ana@example.com` regardless of capital letters.

**Solution:**

```excel
=SUMPRODUCT(--EXACT(LOWER(A2:A6), "ana@example.com"))
```

**Answer:** `4`. Rows 2, 3, 4 and 6 match after conversion. Row 5 holds a different address, `bo@example.com`, and does not match.

### Problem 2: Standardizing Product Codes Before a Lookup

A warehouse receives codes in both upper and lower case. The lookup table stores every code in lowercase.

| Scanned Code |
| --- |
| WX-204 |
| wx-204 |
| Gx-118 |

**Task:** Create a lookup key for each scanned code in `B2:B4` so the codes can match the lowercase table.

**Solution:**

```excel
=LOWER(TRIM(A2))
```

Copy the formula down to `B4`.

**Answer:** `wx-204`, `wx-204` and `gx-118`. The first two codes now match one lookup key, so the warehouse can count them as the same item.

## Use Cases

### Email Address Matching

**Scenario:** A mailing list merges addresses from several systems, and each system uses its own capitalization.

```excel
=LOWER(TRIM(B2))
```

**Why It Works:** TRIM removes stray spaces and LOWER makes the address consistent, so duplicate checks and lookups can compare keys directly.

### Mixed Case Import Cleanup

**Scenario:** A CRM export arrives with department names typed in capitals, title case or lowercase.

```excel
=PROPER(LOWER(A2))
```

**Why It Works:** LOWER first removes the inconsistent capitals, and PROPER then applies one style for display. Use LOWER alone when the data is only for matching.

### Product Code Standardization

**Scenario:** Product codes such as `AB-100` and `ab-100` should count as one product in a sales report.

```excel
=SUMIFS(Sales[Units], Sales[Code Key], LOWER(F2))
```

**Why It Works:** The helper column `Code Key` holds the lowercased codes, so the criteria match every spelling.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#SPILL!` | Cells below the formula contain data. | Clear the cells in the spill range or enter the formula in a single cell. |
| Result looks unchanged | The text has no uppercase letters, or the cell holds a formula result that is not text. | Check the source cell with the formula bar. |
| Number is now text | LOWER returns text for numeric input. | Wrap the result in VALUE if you need a number. |
| Comparison still fails | The text contains extra spaces. | Wrap the input in TRIM before comparing. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Range input spills in Microsoft 365. Older versions need one formula per cell or a Ctrl plus Shift plus Enter array entry. |
| Google Sheets | Available | Range input needs ARRAYFORMULA around the range, for example `=ARRAYFORMULA(LOWER(A2:A4))`. |

## Tips and Best Practices

- Keep the original text in its column and place LOWER results in a helper column when you need both forms.
- Combine LOWER with TRIM when the source comes from a form or a paste, because stray spaces break matches.
- Use EXACT for a case-sensitive check and LOWER when you want to store or group the normalized value.
- Apply the same case rule to both sides of a lookup. Lowercasing only the lookup table is not enough.
- Use PROPER for names shown to people and LOWER for keys used in calculations.

## Related Functions

| Function | Relationship |
| --- | --- |
| [UPPER](UPPER.md) | Converts text to uppercase, the opposite direction. |
| [PROPER](PROPER.md) | Capitalizes the first letter of each word, for display. |
| [EXACT](EXACT.md) | Compares two text values case-sensitively. |
| [TRIM](TRIM.md) | Removes extra spaces, often used with LOWER on imported data. |
| [CLEAN](CLEAN.md) | Removes nonprinting characters before case conversion. |

## Official Documentation

- [Microsoft Support: LOWER function](https://support.microsoft.com/en-us/excel/functions/lower-function)
- [Google Docs Editors Help: LOWER](https://support.google.com/docs/answer/3094083)
