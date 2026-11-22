---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Text Manipulation
use-case:
  - Character Checks
  - Export Diagnostics
  - Sorting by Character Code
related:
  - ASC
  - CHAR
  - LEFT
  - UNICHAR
  - UNICODE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/code-function
  - https://support.google.com/docs/answer/3094122
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - First Character Code
tags:
  - character-codes
  - excel
  - sheets
  - text-conversion
---

# CODE

## Description

**CODE** returns the numeric code of the first character in a piece of text. Only that first character is evaluated, and everything after it is ignored. It is the reverse of CHAR, which turns a code back into a character.

Use CODE when you need to check what a value starts with. A code of 32 means the text begins with a space, a code of 9 means it begins with a tab, and a code between 65 and 90 means it begins with an uppercase letter in the standard set. Those checks help when imported data carries hidden leading characters.

The numbers depend on the platform. Excel returns the code from the ANSI character set on Windows and from the Macintosh character set on the Mac. Google Sheets returns the Unicode map value of the first character. Letters, digits and common punctuation match on both, but characters outside the basic range can return different numbers. Use UNICODE in Excel when you need a Unicode code point beyond the ANSI range.

<!-- Image 1: First Character Code. See Images/Text/CODE.md -->

## Syntax

```excel
=CODE(text)
```

Google Sheets uses the argument name `string` in the same position.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text, or a cell reference that contains text. Only its first character is evaluated. In Google Sheets this argument is `string`. |

### Return Value

A whole number that is the code of the first character. Empty text produces an error in Excel.

## Examples

### Example 1: Code for an Uppercase Letter

```excel
=CODE("A")
```

**Result:** `65`

Uppercase A is code 65 in the standard set.

### Example 2: Code for a Punctuation Mark

```excel
=CODE("!")
```

**Result:** `33`

The exclamation mark is code 33.

### Example 3: Code for the First Letter of a Cell

```excel
=CODE(A2)
```

Where `A2` contains `Zebra`.

**Result:** `90`

Only the Z is read, and Z is code 90.

### Example 4: Ignoring Everything After the First Character

```excel
=CODE("Hello")
```

**Result:** `72`

Only the H is evaluated. The remaining letters do not change the result.

<!-- Image 2: Code Lookup for the First Character. See Images/Text/CODE.md -->

## Story Problems

### Problem 1: Finding the First Letter Code for Each Name

A list of animal names sits in `B2:B4`.

| Ref | Name |
| --- | --- |
| 1 | Kestrel |
| 2 | Badger |
| 3 | Yak |

**Task:** Return the code of the first letter of each name in column B.

**Solution:**

```excel
=CODE(B2)
```

Fill this formula down to `B4`, and use the Name column as the source.

**Answer:** `75`, `66` and `89`, because K, B and Y are codes 75, 66 and 89 in the standard set.

### Problem 2: Comparing Uppercase and Lowercase

A test compares the letters `m` and `M`.

**Task:** Find the code of each letter, and say which one has the higher code.

**Solution:**

```excel
=CODE("m")
```

Use `=CODE("M")` for the second letter.

**Answer:** `109` for lowercase m and `77` for uppercase M, so the lowercase letter has the higher code.

## Use Cases

### Spotting Hidden Leading Characters

**Scenario:** A product code column sometimes begins with an invisible character copied from another system.

```excel
=IF(CODE(A2)<32, "Check leading character", "OK")
```

**Why It Works:** Codes below 32 are control characters such as the tab (9) and the line feed (10), so a smaller code signals hidden leading text. A code of 32 is a space, which needs TRIM rather than cleaning. Clean the value with CLEAN or TRIM once the rows are identified.

### Checking for Uppercase Starts

**Scenario:** A register requires every customer name to start with a capital letter.

```excel
=IF(AND(CODE(A2)>=65, CODE(A2)<=90), "Uppercase start", "Check name")
```

**Why It Works:** Codes 65 to 90 are the uppercase letters A to Z. The AND test passes only when the first character falls in that range.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is empty. | Check that the cell has text before calling CODE. |
| Unexpected code of 32 | The text begins with a space. | Apply TRIM before CODE. |
| Different numbers on different platforms | Excel uses ANSI or the Macintosh set, and Sheets uses the Unicode map. | Compare only letters and digits, which match, or use UNICODE in Excel. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Returns the ANSI code on Windows and the Macintosh code on Mac. |
| Google Sheets | Available | Returns the Unicode map value of the first character. Only the first character is evaluated. |

## Tips and Best Practices

- Use TRIM first when leading spaces could hide the real first character.
- Use CHAR to convert a code back into a character.
- Test non-English characters on each platform before you rely on their codes.
- Use UNICODE in Excel when a character has a code above 255.
- Combine CODE with IF or AND for quick checks on the first character of a column.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ASC](ASC.md) | Converts full-width characters to half-width, which can change the first character's code. |
| [CHAR](CHAR.md) | Turns a code number back into a character. |
| [LEFT](LEFT.md) | Extracts the first character as text, which you can test with CODE. |
| [UNICHAR](UNICHAR.md) | Returns a character from a Unicode code point. |
| [UNICODE](UNICODE.md) | Returns the Unicode code point of the first character in Excel. |

## Official Documentation

- [Microsoft Support: CODE function](https://support.microsoft.com/en-us/excel/functions/code-function)
- [Google Docs Editors Help: CODE](https://support.google.com/docs/answer/3094122)
