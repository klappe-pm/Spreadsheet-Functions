---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Text Manipulation
use-case:
  - Byte Limit Parsing
  - Japanese Label Positions
related:
  - FIND
  - LEFTB
  - MIDB
  - RIGHTB
  - SEARCHB
level: 5
source:
  - https://support.microsoft.com/en-us/excel/text-functions-reference
  - https://support.google.com/docs/answer/3296009
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Find Bytes
  - Double Byte Find
tags:
  - byte-count
  - dbcs
  - double-byte
  - excel
  - sheets
  - text-extraction
---

# FINDB

## Description

**FINDB** returns the position of one text string inside another, the same as FIND, but it counts bytes instead of characters. A double-byte character, such as most Japanese, Chinese and Korean characters, counts as 2 bytes. A single-byte character, such as a Latin letter, digit or punctuation mark, counts as 1 byte.

Use FINDB when a position must match a byte count, for example when a legacy system or a fixed-width file expects fields at byte offsets, or when a Japanese, Chinese or Korean string must be split at a byte boundary. Pair FINDB with LEFTB, MIDB or RIGHTB to extract text using the same byte positions.

For text that uses only single-byte characters, FINDB and FIND return the same result. The difference appears only when double-byte characters come before the match. In Excel, FINDB counts double-byte characters as 2 when a double-byte language is enabled. Otherwise it counts each character as 1, so results can change with the language settings of the workbook.

The search is case-sensitive, and the function returns `#VALUE!` when the search text is not found.

## Syntax

```excel
=FINDB(search_for, text_to_search, [starting_at])
```

<!-- Image 1: FINDB Byte Positions. See Images/Text/FINDB.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `search_for` | Yes | The text to locate. It is matched literally and is case-sensitive. |
| `text_to_search` | Yes | The text to search in. A cell reference or a literal string works. |
| `starting_at` | No | The byte position where the search begins. Defaults to 1. In Excel this argument is named `start_num`. |

Note that the argument order matches FIND. Functions such as SPLIT and SUBSTITUTE use a different order, so check each one before copying a formula.

### Return Value

A whole number: the byte position of the first match, where each double-byte character counts as 2. The function returns `#VALUE!` when the search text is not found or when the arguments are reversed.

## Examples

### Example 1: Single-Byte Text

```excel
=FINDB("@", "j.lee@northwind.com")
```

**Result:** `6`

All characters are single-byte, so the byte position equals the character position, the same as FIND.

### Example 2: Position After Double-Byte Characters

```excel
=FINDB("新", "農歴新年")
```

**Result:** `5`

Each of the three characters 農, 歴 and 新 counts as 2 bytes when a double-byte setting is active. The character 新 begins at byte 5. FIND returns 3 for the same text.

### Example 3: Starting the Search at a Byte Offset

```excel
=FINDB("-", A2, 5)
```

Where A2 contains `ABCD-1234`

**Result:** `5`

The search begins at byte 5 and finds the hyphen at byte 5, because the first four letters each use one byte.

### Example 4: Handling a Missing Match

```excel
=IFERROR(FINDB("@", A3), "No Address")
```

Where A3 contains `Phone only`

**Result:** `"No Address"`

Wrap FINDB in IFERROR when the search text might be absent, so the error does not spread to other calculations.

### Example 5: Using the Position to Split Text

```excel
=LEFTB(A4, FINDB("・", A4) - 1)
```

Where A4 contains `東京・大阪`

**Result:** `"東京"`

The position of the middle dot is found in bytes, and LEFTB returns the bytes before it. With the double-byte setting active, the middle dot is at byte 5, and LEFTB returns four bytes, which is the two characters 東京.

## Story Problems

### Problem 1: Locating a Kanji in a Product Name

A Japanese retailer stores product names in A2. The label system reads fields by byte position, so the team needs the byte position of the kanji 新 in the name.

| Product Name |
| --- |
| 農歴新年 |

**Task:** Return the byte position of 新 in A2 when double-byte characters count as 2 bytes.

**Solution:**

```excel
=FINDB("新", A2)
```

**Answer:** `5`. The characters 農, 歴 and 新 occupy bytes 1 to 2, 3 to 4 and 5 to 6, so 新 starts at byte 5.

<!-- Image 2: Byte Positions in a Mixed Text String. See Images/Text/FINDB.md -->

### Problem 2: Finding the At Sign in a Mixed Record

An export contains an email address that uses only Latin characters. The team needs the byte position of the at sign to split the address.

| Contact Email |
| --- |
| j.lee@northwind.com |

**Task:** Return the byte position of the at sign in A2.

**Solution:**

```excel
=FINDB("@", A2)
```

**Answer:** `6`. Every character in the address is single-byte, so the byte position matches the character position.

## Use Cases

### Byte Limit Parsing

**Scenario:** A legacy system stores a Japanese customer name in a field limited to 12 bytes. Before import, the team needs the byte position of the family name separator.

```excel
=LEFTB(A2, FINDB(" ", A2) - 1)
```

**Why It Works:** FINDB returns the byte position of the separator space, and LEFTB returns the bytes before it. Both functions use bytes, so the split stays correct even when the name mixes single-byte and double-byte characters.

### Japanese Label Positions

**Scenario:** A label printer reads a product code and a Japanese description in fixed byte positions. The formula confirms where the description begins.

```excel
=FINDB("・", A2) + 1
```

**Why It Works:** The formula returns the byte position of the first character after the middle dot. MIDB can then extract the description from that offset.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The search text is not found. | Wrap FINDB in IFERROR, or confirm that the text exists. |
| Position differs from FIND | Double-byte characters come before the match, so byte counts are larger. | Use FINDB for byte logic and FIND for character logic. |
| Position changes between computers | The Excel language setting controls whether double-byte characters count as 2. | Set the same language on every machine, or use FIND when character positions are needed. |
| `#VALUE!` | The arguments are reversed. | Put the search text first and the text to search second. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available. | Counts double-byte characters as 2 when a double-byte language is enabled. Otherwise each character counts as 1. |
| Google Sheets | Available. | Counts each double-byte character as 2, as described on the Sheets help page. |

## Tips and Best Practices

- Use FINDB only when the byte count matters, such as a fixed-width or legacy format.
- Use FIND for ordinary character positions in Latin-only data.
- Pair FINDB with LEFTB, MIDB or RIGHTB so that the search and extraction use the same unit.
- Test the formula on a sample that contains real double-byte characters before using it in a template.
- Document the language setting that a workbook needs so that colleagues get the same positions.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FIND](FIND.md) | Returns the same position counted in characters. Use it for most work. |
| [SEARCHB](SEARCHB.md) | Finds text without regard to case, counting bytes. |
| [LEFTB](LEFTB.md) | Extracts the leftmost bytes of a string. |
| [MIDB](MIDB.md) | Extracts a byte-counted substring from a position. |
| [RIGHTB](RIGHTB.md) | Extracts the rightmost bytes of a string. |

## Official Documentation

- [Microsoft Support: Text functions reference (FIND, FINDB)](https://support.microsoft.com/en-us/excel/text-functions-reference)
- [Google Docs Editors Help: FINDB](https://support.google.com/docs/answer/3296009)
