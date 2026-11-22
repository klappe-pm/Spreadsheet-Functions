---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
purpose:
  - Text Manipulation
use-case:
  - Checking Name Capitalization
  - Finding Hidden Symbols
  - Matching Currency Symbols
related:
  - CHAR
  - CODE
  - LEFT
  - UNICHAR
  - UPPER
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/unicode-function
  - https://support.google.com/docs/answer/9149523
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Character Code Point
  - Unicode Value
tags:
  - character-codes
  - excel
  - sheets
  - unicode
---

# UNICODE

## Description

**UNICODE** returns the Unicode number (code point) of the first character in a text string. It is the reverse of UNICHAR, and it answers questions such as which symbol a cell starts with, whether a value begins with an uppercase letter, or whether an imported value starts with an invisible character.

Only the first character is read. For a string such as `Alphabet`, the result is 65, the code for A, and the rest of the string is ignored. To check another position, combine UNICODE with MID to pick out that character first.

Use UNICODE for checks and diagnostics. The numbers it returns match the Unicode standard, so a value such as 160 points to a non-breaking space, and 8364 points to the euro sign. Numbers passed to UNICODE are treated as text, so UNICODE(123) reads the character "1" and returns 49.

## Syntax

```excel
=UNICODE(text)
```

<!-- Image 1: Syntax Anatomy. See Images/Text/UNICODE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text string or cell reference. Only its first character is evaluated. Numbers are treated as text. |

### Return Value

A number: the decimal Unicode value of the first character. The function returns `#VALUE!` when the text is empty, contains a partial surrogate, or contains a data type that is not valid for it.

## Examples

### Example 1: Code of an Uppercase Letter

```excel
=UNICODE("A")
```

**Result:** `65`

Code point 65 is the uppercase letter A.

### Example 2: Only the First Character Counts

```excel
=UNICODE("Alphabet")
```

**Result:** `65`

The rest of the word is ignored, so the result is the code for the first letter, A.

### Example 3: Code of a Currency Symbol in a Cell

```excel
=UNICODE(A2)
```

**Result:** `8364` when `A2` holds `€250`

The first character of the cell is the euro sign, which has code point 8364.

### Example 4: Code of a Space

```excel
=UNICODE(" ")
```

**Result:** `32`

A regular space has code point 32. A non-breaking space has code point 160, which is useful when diagnosing imported text.

### Example 5: Test for an Uppercase Letter

```excel
=AND(UNICODE(A3)>=65,UNICODE(A3)<=90)
```

**Result:** `TRUE` when `A3` holds `Quarterly`

Code points 65 to 90 are the uppercase letters A to Z, so the test is TRUE when the first character is one of them.

## Story Problems

### Problem 1: Flag Names That Start With a Capital Letter

A list of file names in `A2:A5` mixes capitalized and lowercase names: `Ledger`, `budget`, `Quarterly` and `forecast`.

| File Name |
| --- |
| Ledger |
| budget |
| Quarterly |
| forecast |

**Task:** Return TRUE in column B for each name that starts with an uppercase letter from A to Z, and FALSE for the others.

**Solution:**

```excel
=AND(UNICODE(A2)>=65,UNICODE(A2)<=90)
```

**Answer:** TRUE, FALSE, TRUE and FALSE, in the same order. L is code 76, b is code 98, Q is code 81 and f is code 102.

### Problem 2: Identify the Currency Symbol in Each Price

Column A holds two prices: `£ 80` in `A2` and `€ 250` in `A3`. The import needs the code of the symbol at the start of each price.

**Task:** Return the code point of the first character in each cell.

**Solution:**

```excel
=UNICODE(A2)
```

**Answer:** `163` for the pound sign in `A2` and `8364` for the euro sign in `A3`. Fill the formula down to read both rows.

<!-- Image 2: First Character Codes. See Images/Text/UNICODE.md -->

## Use Cases

### Checking Name Capitalization

**Scenario:** A file list should use capitalized names, and a quick check must flag any that start with a lowercase letter or a digit.

```excel
=AND(UNICODE(A2)>=65,UNICODE(A2)<=90)
```

**Why It Works:** The range 65 to 90 covers only the uppercase letters A to Z. Digits and lowercase letters fall outside it and return FALSE.

### Finding Hidden Symbols

**Scenario:** A column of product codes looks correct, but lookups fail, and the cause may be an invisible leading character.

```excel
=UNICODE(LEFT(A2,1))
```

**Why It Works:** LEFT returns the first character, and UNICODE shows its code. A result of 160 reveals a non-breaking space, which TRIM does not remove.

### Matching Currency Symbols

**Scenario:** A price import should be split by currency, and the euro prices must be separated from the others.

```excel
=UNICODE(LEFT(A2,1))=8364
```

**Why It Works:** The formula returns TRUE when the first character is the euro sign, so the rows can be filtered on the result.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The cell is empty, so there is no first character. | Wrap the formula in IF, such as `=IF(A2="","",UNICODE(A2))`. |
| `#VALUE!` or `#N/A` | The first character is a partial surrogate, which some symbols and emoji use. | Check the source value, because the text may contain a broken character. |
| Only one character checked | The formula reads the first character only. | Use MID with the position to check a later character. |
| Unexpected number | A number was passed in, so it was read as text. | Check the code of the character in the text, such as 49 for the character "1". |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Returns `#VALUE!` for empty text and for invalid data types. |
| Google Sheets | Available | Returns the decimal Unicode value of the first character. Works only when the input is not empty. Numbers are read as text. |

## Tips and Best Practices

- Use UNICODE with LEFT or MID to check a specific character in a text value.
- Compare the result with a known code, such as 160 for a non-breaking space, when cleaning imported data.
- Wrap the formula in IF when some cells may be blank.
- Use UNICHAR to build the symbol from the same code point.
- Remember that UNICODE returns a number, so use the result in a comparison or a lookup table.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHAR](../Text/CHAR.md) | Returns the character for a code number from 1 to 255 in the system code page. |
| [CODE](../Text/CODE.md) | Returns the code number of the first character in the system code page. |
| [LEFT](../Text/LEFT.md) | Returns the first characters of the text, which UNICODE can then test. |
| [UNICHAR](../Text/UNICHAR.md) | Returns the character for a Unicode number, the reverse of UNICODE. |
| [UPPER](../Text/UPPER.md) | Converts text to uppercase, which pairs with the capital letter check. |

## Official Documentation

- [Microsoft Support: UNICODE function](https://support.microsoft.com/en-us/excel/functions/unicode-function)
- [Google Docs Editors Help: UNICODE](https://support.google.com/docs/answer/9149523)
