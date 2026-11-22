---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Text Manipulation
use-case:
  - Email Domain Extraction
  - Invoice Number Parsing
  - Product Code Splitting
related:
  - FINDB
  - ISNUMBER
  - LEFT
  - MID
  - RIGHT
  - SEARCH
level: 2
source:
  - https://support.microsoft.com/en-us/topic/c7912941-af2a-4bdf-a553-d0d89b0a0628
  - https://support.google.com/docs/answer/3094126
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Find Position
  - Find Text Position
tags:
  - case-sensitive
  - excel
  - position
  - sheets
  - text-extraction
---

# FIND

## Description

**FIND** returns the position of one text string inside another. The position is the character number, counted from the first character of the text, where the search text first appears. For example, `FIND("@", "j.lee@northwind.com")` returns 6 because the at sign is the sixth character.

FIND is case-sensitive. The search for `n` does not match an uppercase `N`. When case should not matter, use SEARCH instead. FIND does not treat wildcards such as `*` or `?` as special characters, so the search text is matched literally.

FIND rarely returns a useful answer by itself. Its main job is to supply a position to another function, such as LEFT, MID or RIGHT, which extract the text before, inside or after that position. The third argument, `starting_at`, lets you skip earlier matches, which is useful when a delimiter appears more than once.

If the search text is not found, FIND returns `#VALUE!`. Wrap it in IFERROR when a missing match is possible.

## Syntax

```excel
=FIND(search_for, text_to_search, [starting_at])
```

<!-- Image 1: FIND Arguments and Position Count. See Images/Text/FIND.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `search_for` | Yes | The text to locate. It is matched literally and is case-sensitive. In Excel this argument is named `find_text`. |
| `text_to_search` | Yes | The text to search in. A cell reference or a literal string in quotes works. In Excel this argument is named `within_text`. |
| `starting_at` | No | The character position where the search begins. Defaults to 1. Matches before this position are ignored, but the returned position still counts from the first character. In Excel this argument is named `start_num`. |

### Return Value

A whole number: the character position of the first match at or after `starting_at`. The function returns `#VALUE!` when the search text is not found, when `starting_at` is greater than the length of the text, or when the arguments are reversed.

## Examples

### Example 1: Finding the At Sign in an Email

```excel
=FIND("@", "j.lee@northwind.com")
```

**Result:** `6`

The first five characters are `j.lee`, so the at sign is the sixth character.

### Example 2: Case-Sensitive Match

```excel
=FIND("n", "Nina")
```

**Result:** `3`

The uppercase N at position 1 does not match the lowercase `n`. The first lowercase match is the n at position 3.

### Example 3: Starting the Search Later

```excel
=FIND("wood", "How much wood can a woodchuck chuck", 14)
```

**Result:** `21`

The search starts at character 14. The first occurrence of `wood` at or after that point begins at character 21, in the word "woodchuck".

### Example 4: Locating a Delimiter in a Product Code

```excel
=FIND("-", A2)
```

Where A2 contains `BLU-2025-XL`

**Result:** `4`

The first hyphen is the fourth character. Pass this value to LEFT to extract the color prefix `BLU`.

### Example 5: Handling a Missing Match

```excel
=IFERROR(FIND("-", A3), "No hyphen")
```

Where A3 contains `ABC123`

**Result:** `"No hyphen"`

Without IFERROR, the formula would return `#VALUE!`. The fallback text keeps downstream formulas readable.

### Example 6: Finding the Second Occurrence

```excel
=FIND("-", A2, FIND("-", A2) + 1)
```

Where A2 contains `BLU-2025-XL`

**Result:** `9`

The inner FIND locates the first hyphen at position 4. Adding 1 starts the outer search after it, so the outer FIND returns the second hyphen at position 9.

## Story Problems

### Problem 1: Reading a Size Code From a SKU

A clothing retailer builds SKUs as color, year and size separated by hyphens. The size code is needed for a stock report.

| SKU |
| --- |
| BLU-2025-XL |

**Task:** Find the position of the second hyphen in A2 so that the size code can be extracted with MID.

**Solution:**

```excel
=FIND("-", A2, FIND("-", A2) + 1)
```

**Answer:** `9`. The first hyphen is at position 4, and the second hyphen is at position 9. The size code `XL` starts at position 10.

<!-- Image 2: Locating the Second Hyphen in a SKU. See Images/Text/FIND.md -->

### Problem 2: Extracting the Domain From an Email

A marketing list stores contact emails in A2. The team wants only the company domain to group contacts by organization.

| Contact Email |
| --- |
| j.lee@northwind.com |

**Task:** Return the text after the at sign in A2.

**Solution:**

```excel
=MID(A2, FIND("@", A2) + 1, 100)
```

**Answer:** `northwind.com`. FIND returns 6, so MID starts at character 7 and takes up to 100 characters, which covers the rest of the address.

## Use Cases

### Invoice Number Parsing

**Scenario:** Invoice numbers have a prefix before the first hyphen, such as `INV-2026-0457`. The accounting system needs the prefix to route invoices to the correct ledger.

```excel
=LEFT(A2, FIND("-", A2) - 1)
```

**Why It Works:** FIND locates the first hyphen, and LEFT returns everything before it. Subtracting 1 excludes the hyphen itself. Wrap the formula in IFERROR when some codes lack a hyphen.

### Flagging Keywords in Notes

**Scenario:** A support team marks tickets that mention the word `refund` in the description column.

```excel
=IF(ISNUMBER(FIND("refund", B2)), "Refund Request", "")
```

**Why It Works:** FIND returns a number when the word is present and an error when it is absent. ISNUMBER converts that result to TRUE or FALSE. The search is case-sensitive, so use SEARCH when `Refund` and `refund` should both match.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The search text does not appear in the text. | Wrap FIND in IFERROR, or check the source data for spelling and spacing. |
| `#VALUE!` | The arguments are reversed, so the text is in the first position. | Put the search text first and the text to search second. |
| `#VALUE!` | `starting_at` is greater than the length of the text. | Check the length with LEN before using a computed start position. |
| Match is missed | The case of the search text differs from the source. | Use SEARCH, or convert both sides with LOWER before FIND. |
| Unexpected position | The returned value counts from the start of the text, not from `starting_at`. | Add the start position to the result when you need an offset from another point. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions. | Case-sensitive. Wildcards are not supported. FINDB is the byte-based version for double-byte languages. |
| Google Sheets | Available. | Same arguments and case-sensitive matching. FINDB is the byte-based version. |

## Tips and Best Practices

- Use SEARCH when the case of the text varies.
- Combine FIND with IFERROR when a delimiter might be missing.
- Use `starting_at` to find the second or third occurrence of a delimiter.
- Use LEN to check the length of a text before calculating an end position.
- Build the start position in a helper column when the formula becomes hard to read.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FINDB](FINDB.md) | Returns the same position counted in bytes, for double-byte languages. |
| [SEARCH](SEARCH.md) | Finds text without regard to case and supports wildcards. |
| [LEFT](LEFT.md) | Extracts text before a position found by FIND. |
| [MID](MID.md) | Extracts text from the middle, using a position found by FIND. |
| [RIGHT](RIGHT.md) | Extracts text after a position found by FIND. |
| [ISNUMBER](../Information/ISNUMBER.md) | Tests whether FIND returned a position, which shows that the text was found. |

## Official Documentation

- [Microsoft Support: FIND and FINDB functions](https://support.microsoft.com/en-us/topic/c7912941-af2a-4bdf-a553-d0d89b0a0628)
- [Google Docs Editors Help: FIND](https://support.google.com/docs/answer/3094126)
