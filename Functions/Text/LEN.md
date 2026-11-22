---
domain: Spreadsheet Functions
category: Text
subcategory: Text Measurement
purpose:
  - Counting
  - Data Validation
use-case:
  - Data Entry Validation
  - Field Truncation Prevention
  - Text Comparison Debugging
related:
  - CLEAN
  - CODE
  - LEFT
  - LENB
  - RIGHT
  - SUBSTITUTE
  - TRIM
  - VALUE
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/len-function
  - https://support.google.com/docs/answer/3094081
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Character Count
  - String Length
  - Text Length
tags:
  - counting
  - excel
  - length
  - sheets
  - validation
---

# LEN

## Description

**LEN** returns the number of characters in a text string. Spaces, punctuation, digits and nonprinting characters all count as one character each. Use it to check entry lengths, to find where a delimiter sits near the end of a string, or to detect hidden characters that make two values look alike but behave differently.

LEN returns a number, not text. A number passed to LEN is converted to its text form first, so `LEN(12345)` returns 5 and `LEN(123.45)` returns 6, because the decimal point counts as a character.

The most common surprise is a higher count than expected. Trailing spaces, non-breaking spaces, line breaks and other invisible characters all add to the total. Compare `LEN(A1)` with `LEN(TRIM(CLEAN(A1)))` to see how many hidden characters are present.

Excel also provides LENB, which counts bytes for double-byte languages. Microsoft documents LENB as deprecated, so use LEN for new work unless a byte count is required.

## Syntax

```excel
=LEN(text)
```

<!-- Image 1: LEN Counting Characters. See Images/Text/LEN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text whose characters are counted. A literal in quotes, a cell reference or a formula that returns text all work. A number is converted to its text form before it is counted. |

### Return Value

A whole number: the count of characters in `text`, including spaces and invisible characters. An empty string returns 0.

## Examples

### Example 1: Counting a Word

```excel
=LEN("Hello")
```

**Result:** `5`

The letters H, e, l, l and o make five characters.

### Example 2: Counting Spaces

```excel
=LEN("Hello World")
```

**Result:** `11`

The five letters of Hello, the space, and the five letters of World make 11 characters.

### Example 3: Empty String

```excel
=LEN("")
```

**Result:** `0`

An empty string has no characters. This helps distinguish a truly empty value from a cell that only looks empty.

### Example 4: Length of a Cell

```excel
=LEN(A2)
```

Where A2 contains `Product Code`

**Result:** `12`

The word Product has 7 characters, the space adds 1, and Code adds 4.

### Example 5: Numbers Are Counted as Text

```excel
=LEN(123.45)
```

**Result:** `6`

The value is read as the text `123.45`, and the decimal point counts as a character.

### Example 6: Detecting a Trailing Space

```excel
=LEN("Hello ")
```

**Result:** `6`

The space after the word is counted. If a cell displays `Hello` but returns 6 here, it contains an invisible trailing space.

### Example 7: Finding Extra Spaces

```excel
=LEN(A3) - LEN(TRIM(A3))
```

Where A3 contains `  Hello  World  `

**Result:** `5`

LEN counts 16 characters in the original. TRIM reduces the text to `Hello World`, which has 11 characters. The difference of 5 is the number of extra spaces removed.

### Example 8: Counting Words Separated by Single Spaces

```excel
=LEN(A4) - LEN(SUBSTITUTE(A4, " ", "")) + 1
```

Where A4 contains `The quick brown fox`

**Result:** `4`

The sentence has 19 characters. Removing the spaces leaves 16. The difference of 3 is the number of spaces, and adding 1 gives the number of words. The formula assumes single spaces between words.

### Example 9: Counting a Specific Letter

```excel
=LEN(A5) - LEN(SUBSTITUTE(A5, "a", ""))
```

Where A5 contains `banana`

**Result:** `3`

Removing every lowercase a leaves 3 characters. The difference from the original length of 6 is the number of a characters. SUBSTITUTE is case-sensitive, so uppercase A is not counted here.

### Example 10: Checking a Fixed-Length Code

```excel
=IF(LEN(A6) = 10, "Valid", "Invalid Length")
```

Where A6 contains `PROD123456`

**Result:** `"Valid"`

The code has ten characters, so it passes the length check.

## Story Problems

### Problem 1: Checking a Text Message Limit

A customer service team sends short order updates by text message. The carrier limit for one message in this workflow is 160 characters.

| Message |
| --- |
| Your order ships Monday, thanks! |

**Task:** Count the characters in the message in A2 and state whether it fits the limit.

**Solution:**

```excel
=LEN(A2)
```

**Answer:** `32`. The message has 32 characters, well under the 160 character limit, so it fits.

<!-- Image 2: Message Length Check. See Images/Text/LEN.md -->

### Problem 2: Exact Length for a Password Field

A system requires passwords of exactly 10 characters. A user typed `Blue Fox 7 ` with a trailing space, which is stored in B2.

| Field | Entry |
| --- | --- |
| Password (B2) | Blue Fox 7  |

**Task:** Count the characters in B2 to decide whether the entry meets the length rule.

**Solution:**

```excel
=LEN(B2)
```

**Answer:** `11`. The visible text has 10 characters, but the trailing space makes the total 11, so the entry fails the 10 character rule.

## Use Cases

### Data Entry Validation

**Scenario:** An employee ID must be six digits. Entries that are too long, too short or contain letters are flagged before they are saved.

```excel
=IF(AND(LEN(A2) = 6, ISNUMBER(VALUE(A2))), "Valid", "Invalid")
```

**Why It Works:** LEN checks the length, and VALUE with ISNUMBER checks that the entry reads as a number. Combine both tests so that a six-letter entry is not accepted.

### Field Truncation Prevention

**Scenario:** An export sends names to a legacy system whose name field holds 50 characters. Long names must be found before the export runs, so they can be shortened by a person.

```excel
=IF(LEN(A2) > 50, "Will truncate: " & LEN(A2) & " characters", "OK")
```

**Why It Works:** The formula reports the actual length of each long name. Manual review is safer than an automatic cut, because a shortened name can lose meaning.

### Text Comparison Debugging

**Scenario:** Two codes look the same, but a lookup fails to match them. The team needs to find the hidden characters.

```excel
=LEN(A2) - LEN(TRIM(CLEAN(A2)))
```

**Why It Works:** TRIM removes extra spaces, and CLEAN removes nonprinting characters. A result above zero shows how many hidden characters are present in the cell. Use CODE on individual characters to identify the source.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Count is higher than the visible text | Trailing spaces, non-breaking spaces or line breaks are present. | Compare with `LEN(TRIM(CLEAN(A1)))` and clean the source data. |
| Count is zero for a cell that looks filled | The cell is empty, or a formula returns an empty string. | Test with `A1 = ""` and check the formula that fills the cell. |
| Count differs between platforms | Surrogate pairs in Unicode text, such as some emoji, can be counted differently. | Check the workbook compatibility setting, or test the characters in the target platform. |
| Count is wrong for double-byte text | Expected a byte count. LEN counts characters. | Use LENB only when a byte count is required. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available. | LENB is available for byte counts and is documented as deprecated. In Compatibility Version 2, surrogate pairs count as one character. |
| Google Sheets | Available. | Counts every character, including spaces and nonprinting characters, as the help page states. |

## Tips and Best Practices

- Use LEN to detect hidden characters when a value looks right but does not match.
- Compare `LEN(A1)` with `LEN(TRIM(A1))` to find extra spaces without changing the source.
- Use LEN with SUBSTITUTE to count a character or a word, and state the assumptions behind the count.
- Use LEN in data validation rules for fixed-format codes, such as `=LEN(A1) = 10`.
- Test LEN on empty cells, because an empty cell returns 0 and a formula that returns "" also returns 0.

## Related Functions

| Function | Relationship |
| --- | --- |
| [TRIM](TRIM.md) | Removes extra spaces before a length is measured. |
| [CLEAN](CLEAN.md) | Removes nonprinting characters before a length is measured. |
| [CODE](CODE.md) | Returns the code of one character, which helps identify hidden characters. |
| [LEFT](LEFT.md) | Extracts a prefix whose length can be computed with LEN. |
| [RIGHT](RIGHT.md) | Extracts a suffix whose length can be computed with LEN. |
| [SUBSTITUTE](SUBSTITUTE.md) | Removes a character so that LEN can count the difference. |
| [VALUE](VALUE.md) | Converts a text number to a value, often used with LEN in validation. |
| [LENB](LENB.md) | Counts bytes instead of characters, for double-byte text. |

## Official Documentation

- [Microsoft Support: LEN function](https://support.microsoft.com/en-us/excel/functions/len-function)
- [Google Docs Editors Help: LEN](https://support.google.com/docs/answer/3094081)
