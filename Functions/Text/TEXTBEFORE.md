---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Text Manipulation
use-case:
  - Amount Before Currency Code
  - Base Product Codes
  - Username From Email
related:
  - FIND
  - LEFT
  - REGEXEXTRACT
  - TEXTAFTER
  - TEXTSPLIT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/textbefore-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Extract Before Text
  - Text Before Delimiter
tags:
  - delimiters
  - excel
  - text-extraction
---

# TEXTBEFORE

## Description

**TEXTBEFORE** returns the part of a text string that comes before a delimiter (a character or a string that marks a split point). It is the mirror of TEXTAFTER: both read the same arguments, and both can pick the first, second or any later occurrence. A negative instance number counts from the end of the text, so the last hyphen in a product code is one argument away.

Use TEXTBEFORE when the piece you need sits in front of a consistent marker, such as the at sign in an email address, the space before a unit of measure or the last hyphen in a product code. Use TEXTAFTER for the piece behind the marker, or TEXTSPLIT when every piece is needed.

Matching is case-sensitive by default. Set match_mode to 1 to ignore case. Wildcard characters are not allowed in the text. When the delimiter is not found, the function returns `#N/A` unless you supply an if_not_found value.

## Syntax

```excel
=TEXTBEFORE(text, delimiter, [instance_num], [match_mode], [match_end], [if_not_found])
```

<!-- Image 1: Syntax Anatomy. See Images/Text/TEXTBEFORE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to search. Wildcard characters are not allowed. |
| `delimiter` | Yes | The text that marks the split point. The function returns the text before it. |
| `instance_num` | No | Which occurrence of the delimiter to use. The default is 1. A negative number counts occurrences from the end, so -1 is the last one. Zero is not allowed. |
| `match_mode` | No | 0 matches case-sensitively and is the default. 1 ignores case. |
| `match_end` | No | 0 treats only real matches as delimiters and is the default. 1 treats the end of the text as a delimiter as well, so the whole text is returned when no delimiter exists. |
| `if_not_found` | No | The value to return when the delimiter is not found. The default is `#N/A`. |

### Return Value

Text: the characters that come before the chosen occurrence of the delimiter. The function returns `#N/A` when the delimiter is not found or when `instance_num` is larger than the number of occurrences, and `#VALUE!` when `instance_num` is 0 or is larger than the length of the text.

## Examples

The examples use `A2` = `Dept/Sales/West/Region7`.

### Example 1: Text Before the First Delimiter

```excel
=TEXTBEFORE(A2,"/")
```

**Result:** `Dept`

With no instance number, the function stops at the first slash.

### Example 2: Text Before the Last Delimiter

```excel
=TEXTBEFORE(A2,"/",-1)
```

**Result:** `Dept/Sales/West`

The -1 instance number finds the last slash, so everything before the final segment is returned.

### Example 3: Text Before the Second Delimiter

```excel
=TEXTBEFORE(A2,"/",2)
```

**Result:** `Dept/Sales`

The second slash is the split point, so the result keeps the first two segments.

### Example 4: Replace a Missing Match

```excel
=TEXTBEFORE(A2,"Finance",,,,"Not found")
```

**Result:** `Not found`

The text does not contain Finance, so the if_not_found value is returned.

### Example 5: Treat the End of Text as a Delimiter

```excel
=TEXTBEFORE("Lee"," ",,,1)
```

**Result:** `Lee`

No space exists, but match_end is 1, so the end of the text counts as the delimiter and the whole text is returned. With the default setting the same formula returns `#N/A`.

## Story Problems

### Problem 1: Usernames From Email Addresses

Column A holds customer email addresses, and the intranet needs only the part before the at sign.

| Email |
| --- |
| dana.reyes@brightpath.io |
| mai.tran@kestrel.co |
| omar.haddad@northwind.org |
| lu.zhang@kestrel.co |

**Task:** Enter a formula in column B that returns the username for each address.

**Solution:**

```excel
=TEXTBEFORE(A2,"@")
```

**Answer:** dana.reyes, mai.tran, omar.haddad and lu.zhang, one per row.

### Problem 2: Base Codes From Model Numbers

Model numbers such as `CX200-RED-M` combine a base code, a color code and a size code, separated by hyphens. The inventory count needs the base code and colour code together, without the size.

**Task:** Return everything before the last hyphen in each model number.

**Solution:**

```excel
=TEXTBEFORE(A2,"-",-1)
```

**Answer:** `CX200-RED` for `CX200-RED-M`, `AL900-BLU` for `AL900-BLU-L` and `CX200-GRN` for `CX200-GRN-S`.

<!-- Image 2: Instance Number Positions. See Images/Text/TEXTBEFORE.md -->

## Use Cases

### Username From Email

**Scenario:** A provisioning script needs the username for each new employee account, and the email address is the only source.

```excel
=TEXTBEFORE(A2,"@")
```

**Why It Works:** The at sign separates the username from the domain, so the part before it is the username. Wrap the formula in IFERROR when the list may contain blank rows.

### Base Product Codes

**Scenario:** A product catalog stores variants as base code plus suffix, and the sales report groups by the base code.

```excel
=TEXTBEFORE(A2,"-",-1)
```

**Why It Works:** Counting from the end removes only the last suffix, so codes with several hyphens keep their structure.

### Amount Before Currency Code

**Scenario:** An import puts amounts and currency codes in one cell, such as `1250.50 USD`, and the amount must be used in calculations.

```excel
=TEXTBEFORE(A2," ")
```

**Why It Works:** The first space separates the number from the currency code. The result is text, so wrap it in VALUE before adding amounts.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The delimiter does not appear in the text, or instance_num is larger than the count of matches. | Supply if_not_found, or wrap the formula in IFERROR. |
| `#VALUE!` | instance_num is 0, or it is larger than the length of the text. | Use 1 or a negative number, and check the source. |
| Empty result | The delimiter is the first character of the text, so nothing comes before it. | Check the source, or use TEXTAFTER if the piece you need follows the delimiter. |
| No match despite visible text | Case differs and match_mode is 0. | Set match_mode to 1. |
| Number from import will not add | The result is text. | Wrap the formula in VALUE before arithmetic. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web) and Excel 2024 (Windows and Mac) | Full argument set, including match_mode, match_end and if_not_found. |
| Google Sheets | Not available | The closest alternatives are LEFT with FIND or SEARCH, and REGEXEXTRACT for pattern-based extraction. |

## Tips and Best Practices

- Use a negative instance number to strip the last suffix from a code, file name or path.
- Supply if_not_found for lists that may have missing delimiters, so the sheet stays clean.
- Use TRIM around the result when the source has irregular spacing.
- Pair TEXTBEFORE with TEXTAFTER on the same delimiter to split one cell into two parts.
- Convert numeric results with VALUE before using them in arithmetic.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FIND](../Text/FIND.md) | Returns the position of a text match, used with LEFT in older formulas. |
| [LEFT](../Text/LEFT.md) | Returns characters from the start of the text, which needs FIND to locate the delimiter. |
| [REGEXEXTRACT](../Text/REGEXEXTRACT.md) | Extracts text that matches a regular expression. |
| [TEXTAFTER](../Text/TEXTAFTER.md) | Returns the text after the same delimiter. |
| [TEXTSPLIT](../Text/TEXTSPLIT.md) | Splits text into rows and columns at one or more delimiters. |

## Official Documentation

- [Microsoft Support: TEXTBEFORE function](https://support.microsoft.com/en-us/excel/functions/textbefore-function)
