---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Text Manipulation
use-case:
  - Email Domain Extraction
  - File Extension Lookup
  - Owner Name Extraction
related:
  - FIND
  - MID
  - REGEXEXTRACT
  - TEXTBEFORE
  - TEXTSPLIT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/textafter-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Extract After Text
  - Text After Delimiter
tags:
  - delimiters
  - excel
  - text-extraction
---

# TEXTAFTER

## Description

**TEXTAFTER** returns the part of a text string that comes after a delimiter (a character or a string that marks a split point). It replaces fragile combinations of MID, FIND and LEN with one formula that reads the text as a whole. You can pick the first, second or any later occurrence of the delimiter, and you can count from the end of the text with a negative number.

Use TEXTAFTER when the text has a consistent marker before the piece you need, such as the colon before a name, the slash before a region or the dot before a file extension. Combine it with TEXTBEFORE when you need the part on the other side of the same delimiter, or with TEXTSPLIT when you need every piece at once.

Matching is case-sensitive by default, and wildcard characters are not allowed in the text. Set match_mode to 1 to ignore case. If the delimiter is not found, the function returns `#N/A` unless you supply an if_not_found value.

## Syntax

```excel
=TEXTAFTER(text, delimiter, [instance_num], [match_mode], [match_end], [if_not_found])
```

<!-- Image 1: Syntax Anatomy. See Images/Text/TEXTAFTER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to search. Wildcard characters are not allowed. |
| `delimiter` | Yes | The text that marks the split point. The function returns the text after it. An empty delimiter matches at the start of the text. |
| `instance_num` | No | Which occurrence of the delimiter to use. The default is 1. A negative number counts occurrences from the end, so -1 is the last one. Zero is not allowed. |
| `match_mode` | No | 0 matches case-sensitively and is the default. 1 ignores case. |
| `match_end` | No | 0 treats only real matches as delimiters and is the default. 1 treats the end of the text as a delimiter as well. |
| `if_not_found` | No | The value to return when the delimiter is not found. The default is `#N/A`. |

### Return Value

Text: the characters that follow the chosen occurrence of the delimiter. The function returns `#N/A` when the delimiter is not found or when `instance_num` is larger than the number of occurrences, and `#VALUE!` when `instance_num` is 0 or is larger than the length of the text.

## Examples

The examples use `A2` = `Dept/Sales/West/Region7`.

### Example 1: Text After the First Delimiter

```excel
=TEXTAFTER(A2,"/")
```

**Result:** `Sales/West/Region7`

With no instance number, the function uses the first slash and returns everything after it.

### Example 2: Text After the Last Delimiter

```excel
=TEXTAFTER(A2,"/",-1)
```

**Result:** `Region7`

A negative instance number counts from the end, so -1 selects the last slash.

### Example 3: Text After the Second Delimiter

```excel
=TEXTAFTER(A2,"/",2)
```

**Result:** `West/Region7`

The second slash is the split point, so the result starts at the word after it.

### Example 4: Replace a Missing Match

```excel
=TEXTAFTER(A2,"Finance",,,,"Not found")
```

**Result:** `Not found`

The text does not contain Finance, so the if_not_found value is returned instead of `#N/A`. The two commas skip the optional arguments in between.

### Example 5: Ignore Case and Handle the End of Text

```excel
=TEXTAFTER("Q3 Report, NORTH Zone","north",,1)
```

**Result:** ` Zone` (with a leading space)

Setting match_mode to 1 lets lowercase north match NORTH. Wrap the formula in TRIM to remove the leading space.

```excel
=TEXTAFTER("Lee"," ",,,1)
```

**Result:** blank (empty text)

With match_end set to 1, the end of the text counts as the delimiter, so the result is empty. With the default, the same formula returns `#N/A` because no space exists.

## Story Problems

### Problem 1: Owner Names From a Ticket Log

Each ticket in column A records a location and an owner in the same format.

| Ticket |
| --- |
| Harbor &#124; Owner: Ruiz |
| Lakeside &#124; Owner: Chen |
| Midtown &#124; Owner: Okafor |
| Harbor &#124; Owner: Diaz |

**Task:** Pull the owner name from each ticket into column B.

**Solution:**

```excel
=TEXTAFTER(A2,"Owner: ")
```

**Answer:** Ruiz, Chen, Okafor and Diaz, one per row. The delimiter includes the trailing space, so no extra space appears in the names.

### Problem 2: Serial Numbers From Invoice Codes

Invoice codes in column A hold a country code and a serial number, separated by hyphens: `INV-EU-0042`, `INV-US-1187` and `INV-EU-0310`.

**Task:** Extract only the serial number after the last hyphen.

**Solution:**

```excel
=TEXTAFTER(A2,"-",-1)
```

**Answer:** `0042`, `1187` and `0310`. The results are text, so the leading zeros remain.

<!-- Image 2: Instance Number Positions. See Images/Text/TEXTAFTER.md -->

## Use Cases

### Email Domain Extraction

**Scenario:** A contact list needs the company domain from each email address for account matching.

```excel
=TEXTAFTER(A2,"@")
```

**Why It Works:** The first at sign marks the start of the domain. Addresses without an at sign return `#N/A`, so wrap the formula in IFERROR when the list may contain blanks.

### File Extension Lookup

**Scenario:** A folder export lists file names such as `budget.final.xlsx`, and the team needs the extension for sorting.

```excel
=TEXTAFTER(A2,".",-1)
```

**Why It Works:** The negative instance number finds the last dot, so `xlsx` is returned even when the name contains several dots.

### Owner Name Extraction

**Scenario:** Ticket text contains a fixed label before the owner's name, and the label appears once per ticket.

```excel
=TEXTAFTER(A2,"Owner: ",,1)
```

**Why It Works:** The label is found regardless of case, and the result is the owner's name without the label.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The delimiter does not appear in the text, or instance_num is larger than the count of matches. | Supply if_not_found, or wrap the formula in IFERROR. |
| `#VALUE!` | instance_num is 0, or it is larger than the length of the text. | Use 1 or a negative number, and check the source. |
| Empty result | The delimiter is the last thing in the text, or match_end is 1 and the text has no delimiter (the end of the text then counts as one). | Check the source text, or set match_end to 0. |
| No match despite visible text | Case differs and match_mode is 0. | Set match_mode to 1. |
| Extra leading space | The text after the delimiter begins with a space. | Wrap the formula in TRIM. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web) and Excel 2024 (Windows and Mac) | Full argument set, including match_mode, match_end and if_not_found. |
| Google Sheets | Not available | The closest alternatives are MID with FIND or SEARCH, and REGEXEXTRACT for pattern-based extraction. |

## Tips and Best Practices

- Add a trailing space or other visible character to the delimiter when you want to skip it in the result.
- Use a negative instance number to read the last piece of a path, a file name or a serial code.
- Supply if_not_found for lists that may have missing delimiters, so the sheet stays clean.
- Use TRIM around the result when the source has irregular spacing.
- Use TEXTSPLIT when you need every piece in its own cell rather than one piece.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FIND](../Text/FIND.md) | Returns the position of a text match, for use with MID in older formulas. |
| [MID](../Text/MID.md) | Extracts characters by position, which needs FIND to locate the delimiter. |
| [REGEXEXTRACT](../Text/REGEXEXTRACT.md) | Extracts text that matches a regular expression. |
| [TEXTBEFORE](../Text/TEXTBEFORE.md) | Returns the text before the same delimiter. |
| [TEXTSPLIT](../Text/TEXTSPLIT.md) | Splits text into rows and columns at one or more delimiters. |

## Official Documentation

- [Microsoft Support: TEXTAFTER function](https://support.microsoft.com/en-us/excel/functions/textafter-function)
