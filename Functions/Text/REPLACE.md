---
domain: Spreadsheet Functions
category: Text
subcategory: Text Cleaning
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Customer Code Updates
  - Phone Number Masking
  - Product Code Year Updates
related:
  - LEN
  - MID
  - REGEXREPLACE
  - REPLACEB
  - SEARCH
  - SUBSTITUTE
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/replace-function
  - https://support.google.com/docs/answer/3098247
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Replace By Position
  - Replace Characters
tags:
  - excel
  - position-based
  - sheets
  - text-cleaning
---

# REPLACE

## Description

**REPLACE** swaps part of a text string for new text. You choose the position where the replacement starts and how many characters it covers. Use it when you know where the text sits, such as a fixed-width code, a year inside a product number, or the first digits of an account number.

REPLACE does not look for the old text. That is the main difference from [SUBSTITUTE](SUBSTITUTE.md), which replaces matching text wherever it appears. If the position of the target changes from row to row, combine REPLACE with [SEARCH](SEARCH.md) to find the starting position first.

The function counts characters from 1. The number of characters you replace can be zero or more, and the new text can be longer or shorter than the text it replaces. The result is always text, so wrap it in VALUE when a number is needed.

REPLACE is available in Microsoft Excel and Google Sheets with the same four arguments. Excel lists [REPLACEB](REPLACEB.md) as a deprecated byte-based version, and the Microsoft page recommends REPLACE for new work.

## Syntax

```excel
=REPLACE(old_text, start_num, num_chars, new_text)
```

<!-- Image 1: Position and Length Anatomy. See Images/Text/REPLACE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `old_text` | Yes | The text, or a cell reference that holds the text, in which characters will be replaced. |
| `start_num` | Yes | The position of the first character to replace. Counting starts at 1. |
| `num_chars` | Yes | The number of characters to replace, counted from `start_num`. |
| `new_text` | Yes | The text that takes the place of the replaced characters. It can be empty or longer than the removed text. |

### Return Value

Text. The original text with the selected characters replaced. Wrap the formula in VALUE to convert a numeric result to a number.

## Examples

### Example 1: Replace a Block of Characters

```excel
=REPLACE("ABCDEFGHIJK", 6, 5, "*")
```

**Result:** `ABCDE*K`

Counting from the sixth character, five characters (`FGHIJ`) are replaced by one asterisk. The letters before and after the block stay unchanged.

### Example 2: Update a Year Inside a Code

```excel
=REPLACE("Q3-2026-DRAFT", 4, 4, "2027")
```

**Result:** `Q3-2027-DRAFT`

The four characters starting at position 4 are the year `2026`. They are replaced with `2027`, so the rest of the code keeps its structure.

### Example 3: Mask All but the Last Four Digits

```excel
=REPLACE(A2, 1, 6, "******")
```

**Result:** `******4567` when A2 contains `5551234567`

The first six digits are replaced with asterisks, and the last four digits remain visible. This pattern suits customer-facing displays where only the end of a number should show.

### Example 4: Replace Digits in a Number Stored as Text

```excel
=VALUE(REPLACE("2009", 3, 2, "10"))
```

**Result:** `2010`

The last two digits are replaced, and VALUE converts the text result to a number so it can be used in calculations.

### Example 5: Locate the Position With SEARCH

```excel
=REPLACE(A2, SEARCH(" ", A2), 1, "_")
```

**Result:** `north_east` when A2 contains `north east`

SEARCH finds the space at position 6, and REPLACE swaps that one character for an underscore. This converts a label with a space into a value that is safe to use as a field name.

<!-- Image 2: Masked Phone Number Result. See Images/Text/REPLACE.md -->

## Story Problems

### Problem 1: Mask Customer Phone Numbers

A support team exports customer records. The company policy allows staff to see only the last four digits of each phone number, so the first six digits must be hidden before the sheet is shared.

| Phone Number |
| --- |
| 5551234567 |
| 5559870123 |

**Task:** Replace the first six digits of the first phone number with asterisks.

**Solution:**

```excel
=REPLACE(A2, 1, 6, "******")
```

**Answer:** `******4567`. The first six digits are replaced and the last four remain, so the number is readable by staff without revealing the full value.

### Problem 2: Move a Product Code to the New Year

A warehouse uses product codes that contain the catalog year in fixed positions. The code `PRD-2025-A` must move to the 2026 catalog. The year starts at position 5 and is four characters long.

| Product Code |
| --- |
| PRD-2025-A |

**Task:** Replace the year in the code with `2026`.

**Solution:**

```excel
=REPLACE(A2, 5, 4, "2026")
```

**Answer:** `PRD-2026-A`. Position 5 starts the year, four characters are replaced, and the suffix `-A` is left as it was.

<!-- Image 3: Product Code Year Update. See Images/Text/REPLACE.md -->

## Use Cases

### Customer Code Updates

**Scenario:** A billing system stores account codes such as `CUST-0001-EU`. When a region code changes, only the middle segment must be swapped.

```excel
=REPLACE(A2, 6, 4, "0002")
```

**Why It Works:** The position is fixed by the code format, so REPLACE changes exactly the four characters that hold the number. Check that every code uses the same layout before filling the formula down.

### Phone Number Masking

**Scenario:** A shared report must show only the last four digits of each number.

```excel
=REPLACE(A2, 1, LEN(A2) - 4, REPT("*", LEN(A2) - 4))
```

**Why It Works:** LEN finds the length, so the mask adapts when numbers have different lengths. REPT builds a mask that matches the number of hidden characters.

### Report Label Formatting

**Scenario:** A monthly report label holds a date in the form `2026-03`, and the month must be written as a word in the title row.

```excel
=REPLACE(A2, 6, 2, "March")
```

**Why It Works:** The month digits sit in a fixed position, so REPLACE swaps them for the month name. Use a lookup table instead when month names vary by row.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Result looks shifted | `start_num` counts from the wrong character, often because of a leading space in the data. | Remove leading spaces with TRIM, or move the position to the correct character. |
| Replaced text is too long or too short | `num_chars` does not match the length of the target text. | Count the characters to replace, or use LEN to size the value. |
| Number result is text | REPLACE always returns text. | Wrap the formula in VALUE when the result feeds a calculation. |
| Unexpected text after the change | The target position changes from row to row. | Find the position with SEARCH and use it as `start_num`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Same four arguments. The Microsoft page lists REPLACEB as deprecated and notes that REPLACE counts a surrogate pair as one character in Compatibility Version 2. |
| Google Sheets | Available | Same four arguments and order. The page documents no edge cases for out-of-range positions. |

## Tips and Best Practices

- Use SEARCH or FIND to set `start_num` when the position varies, and REPLACE only when the position is fixed.
- Check a few rows after filling the formula down, because one different row can shift the result.
- Use SUBSTITUTE when you want to replace a word or symbol rather than a range of characters.
- Keep the original column until the new values have been checked.
- Trim spaces from source data before counting positions.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SUBSTITUTE](SUBSTITUTE.md) | Replaces matching text instead of text at a position. |
| [SEARCH](SEARCH.md) | Finds the position of text so REPLACE can use it as `start_num`. |
| [LEN](LEN.md) | Returns the length of text, useful for sizing the replacement. |
| [MID](MID.md) | Extracts characters from a position without changing the original text. |
| [REGEXREPLACE](REGEXREPLACE.md) | Replaces text that matches a pattern, for more complex cases. |
| [REPLACEB](REPLACEB.md) | The byte-based version, listed as deprecated in Excel. |

## Official Documentation

- [Microsoft Support: REPLACE function](https://support.microsoft.com/en-us/excel/functions/replace-function)
- [Google Docs Editors Help: REPLACE](https://support.google.com/docs/answer/3098247)
