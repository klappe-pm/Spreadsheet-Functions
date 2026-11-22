---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Data Retrieval
  - Text Manipulation
use-case:
  - Email Domain Extraction
  - Keyword Flagging
  - Product Code Parsing
related:
  - FIND
  - IFERROR
  - MID
  - REGEXMATCH
  - REPLACE
  - SEARCHB
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/search-function
  - https://support.google.com/docs/answer/3094154
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Find Text Position
  - Search Text
tags:
  - excel
  - sheets
  - text-search
  - wildcards
---

# SEARCH

## Description

**SEARCH** returns the position at which one piece of text first appears inside another. The position counts from 1 at the first character of the text being searched. Use it when you need to know where a word, symbol or code starts, usually so that another function such as MID, LEFT or REPLACE can work from that position.

SEARCH ignores letter case, so `e` and `E` both match. When case matters, use [FIND](FIND.md) instead. In Microsoft Excel, SEARCH also accepts two wildcard characters: `?` matches any single character, and `*` matches any run of characters. To search for a literal `?` or `*`, place a tilde (`~`) in front of it.

If the text is not found, SEARCH returns `#VALUE!`. Wrap the formula in IFERROR when a missing match should produce a friendly result instead of an error. The optional third argument starts the search at a later position, but the returned position is still counted from the first character of the text.

SEARCH works the same way in Microsoft Excel and Google Sheets for basic searches. The wildcard behavior is documented on the Microsoft page only.

## Syntax

```excel
=SEARCH(find_text, within_text, [start_num])
```

<!-- Image 1: Find Text and Within Text Anatomy. See Images/Text/SEARCH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `find_text` | Yes | The text to locate. Supports `?` and `*` wildcards in Excel. |
| `within_text` | Yes | The text to search in. A cell reference or a literal string is accepted. |
| `start_num` | No | The character position where the search begins. The default is 1. A value of zero, a negative value, or a value larger than the length of `within_text` returns `#VALUE!`. |

### Return Value

A number giving the position of the first character of `find_text` within `within_text`. The position is counted from the first character of `within_text`, even when `start_num` skips earlier characters. If there is no match, the result is `#VALUE!`.

## Examples

### Example 1: Locate a Letter

```excel
=SEARCH("e", "Quarterly Report")
```

**Result:** `6`

The first `e` (or `E`) is the sixth character. The letter is found without regard to case, so an uppercase `E` in the same position would also match.

### Example 2: Ignore Case in a Reference Code

```excel
=SEARCH("INV", "Ref: inv-2040")
```

**Result:** `6`

The text `inv` in lowercase matches the search term `INV`, so the function returns the position of the first character of the match.

### Example 3: Start the Search Later

```excel
=SEARCH("e", "Quarterly Report", 7)
```

**Result:** `12`

The search starts at position 7, which skips the first `e`. The next `e` is at position 12 in the full text, and that is the position returned.

### Example 4: Wildcard Match

```excel
=SEARCH("a?c", "xxabc")
```

**Result:** `3`

The `?` matches the middle letter `b`, so `a?c` matches the text `abc` that begins at position 3.

### Example 5: Find a Literal Question Mark

```excel
=SEARCH("~?", "Is it done?")
```

**Result:** `11`

The tilde makes the `?` a literal character rather than a wildcard, so SEARCH finds the question mark at position 11.

<!-- Image 2: Position Result and Error Case. See Images/Text/SEARCH.md -->

## Story Problems

### Problem 1: Find the At Sign in an Email Address

A customer service team wants to split each email address into the name part and the domain part. The first step is to find the position of the `@` sign in each address.

| Email Address |
| --- |
| maria.chen@northwind.com |
| dev.ops@contoso.org |

**Task:** Find the position of the `@` sign in the first address.

**Solution:**

```excel
=SEARCH("@", A2)
```

**Answer:** `11`. The name `maria.chen` has ten characters, so the `@` sign is the eleventh character.

### Problem 2: Find the Second Hyphen in a Product Code

A parts database uses codes such as `SKU-2201-RED`. The team needs the position of the second hyphen so it can separate the color from the number.

| Product Code |
| --- |
| SKU-2201-RED |

**Task:** Find the position of the second hyphen in the code.

**Solution:**

```excel
=SEARCH("-", A2, SEARCH("-", A2) + 1)
```

**Answer:** `9`. The first hyphen is at position 4, so the search for the second one starts at position 5 and finds the hyphen at position 9.

<!-- Image 3: Email Domain Extraction Result. See Images/Text/SEARCH.md -->

## Use Cases

### Email Domain Extraction

**Scenario:** A mailing list holds full email addresses, and the marketing team wants the company domain for each contact.

```excel
=MID(A2, SEARCH("@", A2) + 1, 100)
```

**Why It Works:** SEARCH finds the `@` sign, and MID returns the characters that follow it. The length of 100 is large enough for any domain name. Wrap the formula in IFERROR when some cells are blank or missing an `@` sign.

### Keyword Flagging

**Scenario:** A support queue receives free-text tickets, and any ticket that mentions a refund should be flagged for finance.

```excel
=IF(ISNUMBER(SEARCH("refund", A2)), "Finance", "Standard")
```

**Why It Works:** SEARCH returns a number when the word appears and an error when it does not. ISNUMBER turns that into `TRUE` or `FALSE`, and the case-insensitive match catches `Refund`, `REFUND` and `refund`.

### Product Code Parsing

**Scenario:** A code such as `SKU-2201-RED` must be split into its number, which sits between the first two hyphens.

```excel
=MID(A2, SEARCH("-", A2) + 1, SEARCH("-", A2, SEARCH("-", A2) + 1) - SEARCH("-", A2) - 1)
```

**Why It Works:** The first SEARCH finds the first hyphen, the second SEARCH finds the next one, and the difference gives the length of the middle part. MID returns that part, `2201`.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The text is not in `within_text`. | Wrap the formula in IFERROR, or check the source with ISNUMBER first. |
| `#VALUE!` | `start_num` is zero, negative, or larger than the text. | Use a start position between 1 and the length of the text. |
| Position is wrong | `start_num` is set, but the position is counted from the first character. | Read the result as a position in the whole text, not in the part that was searched. |
| Match found where none was expected | A wildcard character was used in `find_text`. | Place a tilde before the `?` or `*` to match it literally. |
| Case-sensitive match needed | SEARCH ignores letter case. | Use FIND for a case-sensitive search. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Supports `?` and `*` wildcards, with `~` to match them literally. The page notes that Compatibility Version 2 counts a surrogate pair as one character. SEARCHB is listed as deprecated. |
| Google Sheets | Available | Same three arguments and order. The page does not document wildcard support, so use REGEXMATCH or REGEXEXTRACT when you need pattern matching. |

## Tips and Best Practices

- Use FIND when the search must be case sensitive.
- Wrap SEARCH in IFERROR whenever a missing match is possible, so downstream formulas do not break.
- Use `start_num` to find the second or later occurrence by searching again from one position after the first match.
- Check the wildcard behavior on sample data before using `?` or `*` in a search term.
- Pair SEARCH with MID, LEFT or REPLACE when you need the matched part, not just its position.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FIND](FIND.md) | Performs the same search with case sensitivity. |
| [MID](MID.md) | Returns the characters found at the position that SEARCH gives. |
| [REPLACE](REPLACE.md) | Swaps the characters at a position found by SEARCH. |
| [IFERROR](../Logical/IFERROR.md) | Returns a replacement value when SEARCH finds no match. |
| [REGEXMATCH](REGEXMATCH.md) | Tests for a pattern match, which SEARCH cannot express in Google Sheets. |
| [SEARCHB](SEARCHB.md) | The byte-based version for double-byte text. |

## Official Documentation

- [Microsoft Support: SEARCH function](https://support.microsoft.com/en-us/excel/functions/search-function)
- [Google Docs Editors Help: SEARCH](https://support.google.com/docs/answer/3094154)
