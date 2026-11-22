---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
purpose:
  - Text Manipulation
use-case:
  - Credit Card Masking
  - Customer ID Validation
  - Product Code Parsing
related:
  - FIND
  - LEFTB
  - LEN
  - MID
  - RIGHT
  - SEARCH
  - TRIM
  - VALUE
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/left-function
  - https://support.google.com/docs/answer/3094079
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Extract Left
  - Left Characters
  - Left String
tags:
  - excel
  - extraction
  - sheets
  - substring
  - text-parsing
---

# LEFT

## Description

**LEFT** returns a set number of characters from the beginning of a text string. It is the basic tool for pulling a fixed-width prefix from text, such as the area code in a phone number, the department code at the start of a product code or the year at the start of an ISO date stored as text.

The second argument, `num_chars`, sets how many characters to return. When it is omitted, LEFT returns one character. When it is larger than the text, LEFT returns the whole text without an error. Spaces, digits and punctuation count as characters.

LEFT always returns text. A number that LEFT extracts is therefore a text value. Wrap the result in VALUE when the extracted digits must take part in arithmetic. For text whose prefix length varies, combine LEFT with FIND or SEARCH to find a delimiter first, or use TEXTBEFORE where your platform supports it.

Excel also provides LEFTB, which counts bytes instead of characters for double-byte languages. Microsoft documents LEFTB as deprecated, so use LEFT for new work unless a byte limit must be met.

## Syntax

```excel
=LEFT(text, [num_chars])
```

<!-- Image 1: LEFT Arguments and Output. See Images/Text/LEFT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to take characters from. A literal in quotes, a cell reference or a formula that returns text all work. A number is converted to its text form. In Google Sheets this argument is named `string`. |
| `num_chars` | No | The number of characters to return. Must be zero or greater. Defaults to 1 when omitted. A value larger than the text returns the whole text. Zero returns an empty string. In Google Sheets this argument is named `number_of_characters`. |

### Return Value

A text string containing up to `num_chars` characters from the start of `text`. The result is always text, even when the characters are digits. A negative `num_chars` returns an error.

## Examples

### Example 1: Fixed-Width Prefix

```excel
=LEFT("Hello World", 5)
```

**Result:** `"Hello"`

The first five characters, `H` through `o`, are returned, and the rest of the string is dropped.

### Example 2: Default Single Character

```excel
=LEFT("ABCDEF")
```

**Result:** `"A"`

When `num_chars` is omitted, LEFT returns one character. This suits codes that are classified by their first letter.

### Example 3: Area Code From a Phone Number

```excel
=LEFT("(555) 123-4567", 5)
```

**Result:** `"(555)"`

The count includes both parentheses. To keep only the digits, remove the brackets with SUBSTITUTE or start the extraction after the bracket with MID.

### Example 4: Category From a Product Code

```excel
=LEFT("ELEC-TV-55IN-4K", 4)
```

**Result:** `"ELEC"`

The first four characters identify the department. This works when every code uses the same prefix width.

### Example 5: Prefix From a Cell

```excel
=LEFT(A1, 3)
```

Where A1 contains `Customer12345`

**Result:** `"Cus"`

A cell reference works like a literal string, so the same formula can be copied down a column.

### Example 6: Year From an ISO Date Stored as Text

```excel
=LEFT("2025-08-17", 4)
```

**Result:** `"2025"`

Dates stored as text in the form YYYY-MM-DD can be split by position. The result is text, not the number 2025.

### Example 7: Empty Cell

```excel
=LEFT("", 5)
```

**Result:** `""` (an empty string)

LEFT returns an empty string for empty text, so blank cells do not cause an error.

### Example 8: Count Larger Than the Text

```excel
=LEFT("Hi", 10)
```

**Result:** `"Hi"`

The whole string is returned when it is shorter than the count.

### Example 9: Removing a Known Suffix

```excel
=LEFT(A1, LEN(A1) - 4)
```

Where A1 contains `Report2025`

**Result:** `"Report"`

LEN returns 10, and subtracting 4 leaves 6 characters from the left. This removes the last four characters when their length is known.

### Example 10: First Name From a Full Name

```excel
=LEFT(A1, FIND(" ", A1) - 1)
```

Where A1 contains `John Smith`

**Result:** `"John"`

FIND locates the space at position 5. Subtracting 1 excludes the space, and LEFT returns the characters before it.

### Example 11: Prefix Before a Hyphen, Ignoring Case

```excel
=LEFT(A1, SEARCH("-", A1) - 1)
```

Where A1 contains `ABC-12345`

**Result:** `"ABC"`

SEARCH returns the position of the hyphen. It is the same as FIND for a hyphen, but it also ignores case when the delimiter is a letter.

### Example 12: Branching on the First Character

```excel
=IF(LEFT(A1, 1) = "A", "Category A", "Other")
```

Where A1 contains `A1234`

**Result:** `"Category A"`

Testing the first character inside IF is a common way to route rows to different categories.

### Example 13: Two Characters From the End

```excel
=LEFT(RIGHT(A1, 8), 2)
```

Where A1 contains `123 Main St, Austin, TX 78701`

**Result:** `"TX"`

RIGHT returns the last eight characters, `TX 78701`, and LEFT then takes the first two.

### Example 14: Converting an Extracted Number

```excel
=VALUE(LEFT(A1, 4))
```

Where A1 contains `2025 Annual Report`

**Result:** `2025` (as a number)

VALUE turns the text prefix into a number so that the result can be used in a calculation.

## Story Problems

### Problem 1: Country Prefix in Order Codes

An export of shipping orders stores codes that begin with a two-letter country code followed by the year and a sequence number.

| Order Code |
| --- |
| US-2026-0457 |
| CA-2026-0112 |
| MX-2026-0389 |

**Task:** Extract the country code from each code in A2:A4.

**Solution:**

```excel
=LEFT(A2, 2)
```

Copy the formula down to row 4.

**Answer:** `US` for row 2, `CA` for row 3 and `MX` for row 4. Each code has a two-letter prefix, so a fixed count of 2 is enough.

<!-- Image 2: Country Prefixes From Order Codes. See Images/Text/LEFT.md -->

### Problem 2: Next Year From an ISO Date Text

A planning sheet stores the start date of a project as text in A2, in the form `2026-03-14`. The next budget year must be calculated from the year part.

| Start Date (text) |
| --- |
| 2026-03-14 |

**Task:** Extract the year, convert it to a number and add 1.

**Solution:**

```excel
=VALUE(LEFT(A2, 4)) + 1
```

**Answer:** `2027`. LEFT returns `"2026"`, VALUE converts it to 2026, and adding 1 gives 2027.

## Use Cases

### Product Code Parsing

**Scenario:** An inventory system uses product codes such as `ELEC-TV-55IN-001`, where the first four characters name the department. The team needs the department for summary reports.

```excel
=LEFT(A2, 4)
```

**Why It Works:** The department comes straight from the product code, so it cannot drift out of step with the code. If codes vary in width, use `LEFT(A2, FIND("-", A2) - 1)` to take everything before the first hyphen.

### Customer ID Validation

**Scenario:** Customer IDs must start with `CU` and have six digits after the prefix. Records that fail the check are flagged before import.

```excel
=IF(AND(LEFT(A2, 2) = "CU", LEN(A2) = 8, ISNUMBER(VALUE(MID(A2, 3, 6)))), "Valid", "Invalid")
```

**Why It Works:** LEFT checks the prefix, LEN checks the total length, and MID with VALUE checks that the remaining characters are digits. Each test catches a different kind of error.

### Credit Card Masking

**Scenario:** Customer service staff confirm a card by its first four digits and last four digits, and the middle digits are masked on screen.

```excel
=LEFT(A2, 4) & "-XXXX-XXXX-" & RIGHT(A2, 4)
```

**Why It Works:** LEFT returns the visible prefix, RIGHT returns the visible suffix, and the masked section is plain text. The full number should be kept out of the displayed sheet.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | `num_chars` is negative. | Use MAX(0, your calculation) when the count is computed. |
| Wrong characters | The text has leading spaces or invisible characters. | Wrap the text in TRIM, or in CLEAN and TRIM. |
| Total ignores the value | The result is text, and functions such as SUM skip text. | Wrap the result in VALUE before summing. |
| Prefix length varies | A fixed count works only when every value has the same width. | Use FIND or SEARCH to locate a delimiter, and extract up to it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available. | Includes LEFTB for byte-counted extraction. Microsoft documents LEFTB as deprecated. In Compatibility Version 2, surrogate pairs in Unicode text are handled as single characters. |
| Google Sheets | Available. | Uses `string` and `number_of_characters` as argument names. Also has LEFTB, which Google documents as deprecated. Works with ARRAYFORMULA for ranges. |

## Tips and Best Practices

- Check the data pattern before writing a fixed-width formula, because one unusual entry can shift the result.
- Use `LEFT(TRIM(A1), 3)` when the source may have stray spaces.
- Use FIND or SEARCH with LEFT when the prefix length varies, such as `LEFT(A1, FIND("-", A1) - 1)`.
- Wrap extracted numbers in VALUE before arithmetic, such as `VALUE(LEFT(A1, 4)) + 1`.
- Wrap the formula in IFERROR when a delimiter might be missing, such as `IFERROR(LEFT(A1, FIND("-", A1) - 1), A1)`.
- Use TEXTBEFORE where your platform supports it to extract everything before a delimiter in one step.

## Related Functions

| Function | Relationship |
| --- | --- |
| [RIGHT](RIGHT.md) | Extracts characters from the end of the text. |
| [MID](MID.md) | Extracts characters from any position in the middle of the text. |
| [FIND](FIND.md) | Locates a delimiter, which LEFT can use to set its count. |
| [SEARCH](SEARCH.md) | Locates a delimiter without regard to case. |
| [LEN](LEN.md) | Returns the length, useful for computing a count from the end. |
| [TRIM](TRIM.md) | Removes extra spaces before extraction. |
| [VALUE](VALUE.md) | Converts an extracted prefix that holds digits into a number. |
| [LEFTB](LEFTB.md) | Extracts a number of bytes, for double-byte text. |

## Official Documentation

- [Microsoft Support: LEFT and LEFTB functions](https://support.microsoft.com/en-us/excel/functions/left-function)
- [Google Docs Editors Help: LEFT](https://support.google.com/docs/answer/3094079)
