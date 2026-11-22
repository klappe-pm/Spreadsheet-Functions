---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Account Number Masking
  - Compact Date Conversion
  - Fixed-Width File Parsing
related:
  - FIND
  - LEFT
  - LEN
  - MIDB
  - RIGHT
  - SEARCH
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/mid-function
  - https://support.google.com/docs/answer/3094129
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Middle Characters
  - Mid String
  - Substring Extraction
tags:
  - excel
  - parsing
  - sheets
  - string-extraction
  - text
---

# MID

## Description

**MID** returns a set number of characters from the middle of a text string. You give it the text, the position of the first character to return, and how many characters to return. Position 1 is the first character in the string.

Use MID when the part you need sits at a known position or can be found with FIND or SEARCH. LEFT and RIGHT are simpler when the part you need is at the start or the end. MID handles the cases in between, such as a fixed-width code, a date embedded in an ID, or the segment between two delimiters.

MID needs all three arguments. If `start_num` is greater than the length of the text, MID returns an empty string rather than an error. If `start_num` plus `num_chars` passes the end of the text, MID returns the characters up to the end. Both behaviors are helpful, but they can hide a bad position, so check the output length on a sample before you copy a formula down a long column.

For double-byte languages, Microsoft Excel also offers MIDB, which counts bytes instead of characters. Google Sheets provides MIDB too. For ordinary text, MID and MIDB return the same result.

## Syntax

```excel
=MID(text, start_num, num_chars)
```

<!-- Image 1: MID Argument Positions. See Images/Text/MID.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to read from. Enter it in quotation marks, reference a cell, or use a formula that returns text. |
| `start_num` | Yes | The position of the first character to return. Position 1 is the first character. A value less than 1 returns `#VALUE!`. |
| `num_chars` | Yes | The number of characters to return. A negative value returns `#VALUE!`. Zero returns an empty string. |

### Return Value

A text string that holds up to `num_chars` characters starting at `start_num`. The result is text even when it contains only digits. MID returns an empty string when `start_num` is past the end of the text.

## Examples

### Example 1: Pulling a Year From a Code

```excel
=MID("Invoice-2025-0457", 9, 4)
```

**Result:** `2025`

The word `Invoice-` takes 8 characters, so position 9 is the first digit of the year.

### Example 2: Extracting the Middle Segment Between Hyphens

Cell `A2` contains `SKU-98213-RED`.

```excel
=MID(A2, FIND("-", A2)+1, FIND("-", A2, FIND("-", A2)+1)-FIND("-", A2)-1)
```

**Result:** `98213`

FIND locates the first and second hyphens, and the formula returns the characters between them. The same pattern works for any segment between two delimiters.

<!-- Image 2: Finding the Start and Length From Delimiters. See Images/Text/MID.md -->

### Example 3: Start Position Past the End

```excel
=MID("Shipping", 12, 4)
```

**Result:** `""` (empty text)

The word has 8 characters, so position 12 lies beyond it. MID returns empty text instead of an error.

### Example 4: Length Larger Than the Remaining Text

```excel
=MID("Shipping", 5, 100)
```

**Result:** `ping`

Position 5 starts at `p`, and the length of 100 is more than the four characters left, so MID returns everything from position 5 to the end.

### Example 5: Counting From the End of the Text

Cell `A2` contains `ProductCode123ABC`, which has 17 characters.

```excel
=MID(A2, LEN(A2)-5, 3)
```

**Result:** `123`

`LEN(A2)-5` gives position 12, the first digit of `123`. The formula takes three characters from there.

### Example 6: Negative Length Returns an Error

```excel
=MID("Shipping", 2, -1)
```

**Result:** `#VALUE!`

The number of characters cannot be negative. Check formulas that calculate the length, and wrap the calculation in MAX(0, ...) when the value can go below zero.

## Story Problems

### Problem 1: Summing Batch Codes From Part Numbers

A parts supplier encodes a four-digit batch number in positions 4 to 7 of each part number. The receiving clerk needs the total of the batch numbers received today.

| Part Number |
| --- |
| AB-7741-XZ |
| CD-2290-QA |
| EF-1058-LM |
| GH-3317-TR |
| IJ-4006-WS |

**Task:** Extract the batch number from each part number and add them together.

**Solution:**

```excel
=SUMPRODUCT(VALUE(MID(A2:A6, 4, 4)))
```

**Answer:** `18412`, because 7741 + 2290 + 1058 + 3317 + 4006 = 18412. VALUE converts each extracted text value to a number before SUMPRODUCT adds them.

### Problem 2: Counting Students by Enrollment Year

A school builds student IDs in the form `S` followed by the enrollment year, a hyphen and a four-digit serial number. The registrar needs the number of students who enrolled in 2024.

| Student ID |
| --- |
| S2024-0871 |
| S2023-1140 |
| S2024-0092 |
| S2025-0310 |
| S2024-0777 |
| S2022-0001 |

**Task:** Count the IDs whose year, at positions 2 to 5, is 2024.

**Solution:**

```excel
=SUMPRODUCT(--(MID(A2:A7, 2, 4)="2024"))
```

**Answer:** `3`. Three IDs carry the year 2024, and the double minus sign turns the TRUE and FALSE results into 1 and 0.

## Use Cases

### Fixed-Width File Parsing

**Scenario:** A legacy system exports customer records as fixed-width text. The customer ID occupies positions 1 to 6, the name positions 7 to 26, and the balance positions 27 to 36.

```excel
=TRIM(MID(A2, 7, 20))
```

**Why It Works:** Each field is pulled by its position, and TRIM removes the padding spaces. Record the position map in a reference table so future changes are easy to make.

<!-- Image 3: Fixed-Width Record Layout. See Images/Text/MID.md -->

### Compact Date Conversion

**Scenario:** A logistics system writes ship dates as eight digits, such as `20251103`, and the report needs a real date.

```excel
=DATE(VALUE(MID(A2, 1, 4)), VALUE(MID(A2, 5, 2)), VALUE(MID(A2, 7, 2)))
```

**Why It Works:** MID cuts out the year, month and day, VALUE converts each part to a number, and DATE builds a real date value that sorts and calculates correctly.

### Account Number Masking

**Scenario:** A statement shows only the last four digits of a card number.

```excel
="XXXX-XXXX-XXXX-"&MID(A2, 13, 4)
```

**Why It Works:** MID extracts the final four digits from a 16-digit number, and the text joins them to a fixed mask. The source cell still holds the full number, so restrict access to it.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `start_num` is less than 1. | Start at 1 or greater, and check the calculation that produces the position. |
| `#VALUE!` | `num_chars` is negative. | Wrap the length in MAX(0, ...) when it is calculated. |
| `#VALUE!` | A position or length is text that cannot convert to a number. | Check the source for stray text, and wrap the input in VALUE only when the text is numeric. |
| Empty result | `start_num` is past the end of the text. | Compare the position with LEN before extracting. |
| Characters are off by one | The formula assumes position 0 is the first character. | Remember that the first character is position 1. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all versions | MIDB counts bytes for double-byte languages. In workbooks set to Compatibility Version 2, a surrogate pair counts as one character. Variation selectors still count as separate characters. |
| Google Sheets | Available | MIDB is also available and counts bytes for double-byte text. Use LEN for the length when you want everything to the end of the text. |

## Tips and Best Practices

- Remember that the first character is position 1, not position 0.
- Use FIND or SEARCH to calculate a start position when the text is not fixed width.
- Use LEN to calculate a length when you want everything from a position to the end.
- Wrap the result in TRIM when the source data is padded with spaces.
- Keep fixed-width position maps in a reference table so every formula can point to the same field definitions.
- Test a formula on several sample rows, including the shortest and longest values, before copying it down a column.

## Related Functions

| Function | Relationship |
| --- | --- |
| [LEFT](LEFT.md) | Returns characters from the start of the text. |
| [RIGHT](RIGHT.md) | Returns characters from the end of the text. |
| [FIND](FIND.md) | Finds a position in the text, case-sensitive, to feed MID. |
| [SEARCH](SEARCH.md) | Finds a position in the text, case-insensitive, to feed MID. |
| [LEN](LEN.md) | Returns the length of the text, used for end-relative positions. |
| [MIDB](MIDB.md) | Extracts by bytes, for double-byte character sets. |

## Official Documentation

- [Microsoft Support: MID and MIDB functions](https://support.microsoft.com/en-us/excel/functions/mid-function)
- [Google Docs Editors Help: MID](https://support.google.com/docs/answer/3094129)
