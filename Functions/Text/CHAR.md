---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Text Manipulation
use-case:
  - Character Code Checks
  - Delimiter Building
  - Line Breaks in Cells
related:
  - CLEAN
  - CODE
  - TEXTJOIN
  - UNICHAR
  - UNICODE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/char-function
  - https://support.google.com/docs/answer/3094120
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Character From Code
tags:
  - character-codes
  - excel
  - sheets
  - text-conversion
---

# CHAR

## Description

**CHAR** returns the character that matches a code number. It is the reverse of CODE, which returns the number for a character. Most people use CHAR for characters that cannot be typed easily, such as a line break, a tab or a vertical bar, and for building text from a list of codes.

In Excel, the code must be a whole number from 1 to 255. The character comes from the ANSI character set on Windows and from the Macintosh character set on the Mac. Common codes such as 65 (A) and 124 (|) return the same character on both systems. Excel for the web supports only codes 9, 10, 13 and 32 and above.

Google Sheets reads the number against the current Unicode table and expects a decimal (base 10) value. If a table lists hexadecimal values, convert them with HEX2DEC first. Not every Unicode character displays on every device, so test any unusual character before sharing the file.

<!-- Image 1: Character Codes in a Formula. See Images/Text/CHAR.md -->

## Syntax

```excel
=CHAR(number)
```

Google Sheets uses the argument name `table_number` in the same position.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `number` | Yes | A whole number that identifies the character. Excel accepts 1 to 255. In Google Sheets this argument is `table_number`, a decimal value from the Unicode table. |

### Return Value

A text value containing one character. Numbers outside the valid range, or text that cannot be read as a number, produce an error.

## Examples

### Example 1: Returning a Capital Letter

```excel
=CHAR(65)
```

**Result:** `A`

Code 65 is the capital letter A in the standard character set.

### Example 2: Shifting From a Column Index

```excel
=CHAR(A2+64)
```

Where `A2` contains `5`.

**Result:** `E`

Adding 64 to the position of a letter in the alphabet gives its code, so position 5 returns E.

### Example 3: Line Break Inside a Cell

```excel
=A2 & CHAR(10) & B2
```

Where `A2` contains `Floor 2` and `B2` contains `Room 14`.

**Result:** `Floor 2` on one line and `Room 14` on the next, with Wrap Text turned on.

The line feed character forces the second value onto a new line. Without Wrap Text, the cell shows both values on one line.

### Example 4: Joining Values With a Vertical Bar

```excel
=A2 & CHAR(124) & B2
```

Where `A2` contains `Q1` and `B2` contains `2026`.

**Result:** `Q1|2026`

Code 124 is the vertical bar, which is useful as a visible separator in exported text.

<!-- Image 2: Character Code Chart Excerpt. See Images/Text/CHAR.md -->

## Story Problems

### Problem 1: Three-Line Address Label

A mailing list has names and address parts in `A2:C2`.

| Name | Street | City |
| --- | --- | --- |
| Ruth | 12 Elm Road | Port Alvin |

**Task:** Join the three parts into one cell, `D2`, with each part on its own line.

**Solution:**

```excel
=A2 & CHAR(10) & B2 & CHAR(10) & C2
```

**Answer:** Three lines, reading `Ruth`, `12 Elm Road` and `Port Alvin`, because CHAR(10) inserts a line feed between each part.

### Problem 2: Spelling Out Letter Codes

A list of codes sits in `A2:A4`: 71, 72 and 73.

**Task:** Convert each code to its letter in column B.

**Solution:**

```excel
=CHAR(A2)
```

Fill this formula down to `B4`.

**Answer:** `G`, `H` and `I`, because codes 71, 72 and 73 are the letters G, H and I in the standard set.

## Use Cases

### Multi-Line Cell Labels

**Scenario:** A shipping label cell must show the recipient name and address on separate lines.

```excel
=B2 & CHAR(10) & C2
```

**Why It Works:** The line feed separates the two values. Turn on Wrap Text for the cell so the second line appears, and widen the row if the text is long.

### Building Tab-Delimited Export Lines

**Scenario:** An import tool expects each record as three values separated by tabs.

```excel
=A2 & CHAR(9) & B2 & CHAR(9) & C2
```

**Why It Works:** Code 9 is a tab character, and it is one of the codes that Excel for the web also supports. Save the column as text to keep the tabs intact.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is text that is not a number, or a number outside the valid range. | Check the argument, and keep Excel codes between 1 and 255. |
| Line break does not appear | Wrap Text is turned off for the cell. | Turn on Wrap Text. |
| Blank or box symbol | The code is not available in the character set on the computer, or the font lacks the glyph. | Use a common code, or change the font. |
| Different letters on different platforms | Excel uses ANSI on Windows and the Macintosh set on Mac, while Sheets uses Unicode. | Test codes above 127 on each platform before sharing. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Codes 1 to 255. Excel for the web supports only codes 9, 10, 13 and 32 and above. |
| Google Sheets | Available | Uses the Unicode table with decimal codes. Use HEX2DEC to convert hexadecimal values. |

## Tips and Best Practices

- Use CODE to find the number of a character and CHAR to turn the number back into the character.
- Use UNICHAR in Excel for code points above 255, because CHAR accepts only 1 to 255.
- Remember that CHAR(10) needs Wrap Text to show a line break.
- Pair CHAR(10) with CLEAN when you need to remove line feeds from imported text.
- Test any character outside the basic range before you rely on it in shared files.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CLEAN](CLEAN.md) | Removes the control characters from codes 0 to 31, including tabs and line feeds. |
| [CODE](CODE.md) | Returns the code of the first character, which is the reverse of CHAR. |
| [TEXTJOIN](TEXTJOIN.md) | Joins values with a delimiter, so CHAR is often used to build the delimiter. |
| [UNICHAR](UNICHAR.md) | Returns a character from a Unicode code point, including codes above 255. |
| [UNICODE](UNICODE.md) | Returns the Unicode code point of the first character. |

## Official Documentation

- [Microsoft Support: CHAR function](https://support.microsoft.com/en-us/excel/functions/char-function)
- [Google Docs Editors Help: CHAR](https://support.google.com/docs/answer/3094120)
