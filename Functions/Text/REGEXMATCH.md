---
domain: Spreadsheet Functions
category: Text
subcategory: Regular Expressions
purpose:
  - Data Validation
  - Text Manipulation
use-case:
  - Email Domain Filtering
  - Phone Number Format Checks
  - SKU Format Checks
related:
  - FILTER
  - REGEXEXTRACT
  - REGEXREPLACE
  - SEARCH
  - TEXT
level: 4
source:
  - https://support.google.com/docs/answer/3098292
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Pattern Test
  - Regex Match
tags:
  - data-validation
  - pattern-matching
  - regex
  - sheets
  - text
---

# REGEXMATCH

## Description

**REGEXMATCH** tests whether a piece of text matches a regular expression, which is a pattern written with symbols such as `^` for the start of the text, `\d` for a digit and `$` for the end. It returns `TRUE` when the text contains a match and `FALSE` when it does not.

Use REGEXMATCH when the question is yes or no: does this code follow the format, does this address belong to a domain, does this phone number have the right number of digits. Pair it with FILTER to keep only the matching rows, or with IF to flag the rest. When you need the matching text itself, use REGEXEXTRACT instead.

REGEXMATCH accepts only text. A number such as 404 must be converted with TEXT before it is tested. Google Sheets uses the RE2 pattern syntax, which supports the `(?i)` flag for case-insensitive matching. RE2 does not support matching by Unicode character classes.

This function is available in Google Sheets only. Microsoft Excel does not have REGEXMATCH.

## Syntax

```excel
=REGEXMATCH(text, regular_expression)
```

<!-- Image 1: REGEXMATCH Arguments. See Images/Text/REGEXMATCH.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to test. Enter it in quotation marks, reference a cell, or use a formula that returns text. Numbers must be converted with TEXT first. |
| `regular_expression` | Yes | The RE2 pattern to test against the text. A pattern that matches anywhere in the text returns TRUE, unless `^` and `$` anchor it to the start and end. |

### Return Value

A logical value: `TRUE` when the pattern matches somewhere in the text, and `FALSE` when it does not. An invalid pattern returns an error.

## Examples

### Example 1: Matching a Partial Pattern

```excel
=REGEXMATCH("Spreadsheets", "S.r")
```

**Result:** `TRUE`

The period matches any single character, so `S`, `p` and `r` match the text `Spr` at the start of the word.

### Example 2: Case-Insensitive Match

```excel
=REGEXMATCH("Spreadsheets", "(?i)^spread")
```

**Result:** `TRUE`

The `(?i)` flag makes the match ignore case, so the lowercase pattern matches the capitalized word.

### Example 3: Validating a Code Format

Cell `A2` contains `SK-1001`.

```excel
=REGEXMATCH(A2, "^SK-\d{4}$")
```

**Result:** `TRUE`

The code starts with `SK-`, followed by exactly four digits and the end of the text. A code such as `SK-12` returns `FALSE`.

### Example 4: Filtering Rows With a Pattern

Cells `A2:A6` contain `ana@example.com`, `bo@sample.org`, `cy@example.com`, `dee@test.net` and `eve@example.com`.

```excel
=FILTER(A2:A6, REGEXMATCH(A2:A6, "@example\.com$"))
```

**Result:** `ana@example.com`, `cy@example.com` and `eve@example.com`

REGEXMATCH returns one TRUE or FALSE for each row, and FILTER keeps the rows where the result is TRUE.

<!-- Image 2: FILTER With a Pattern Test. See Images/Text/REGEXMATCH.md -->

### Example 5: Testing a Number

Cell `A2` contains the number `404`.

```excel
=REGEXMATCH(TEXT(A2, "0"), "^\d{3}$")
```

**Result:** `TRUE`

TEXT converts the number to the text `404` before the pattern is tested. Without TEXT, REGEXMATCH returns an error because it accepts only text.

## Story Problems

### Problem 1: Counting Valid Product Codes

A stockroom uses product codes in the form `SK-` followed by exactly four digits. Staff type codes by hand, so some entries are wrong.

| Product Code |
| --- |
| SK-1001 |
| SK-12 |
| sk-1002 |
| SK-1003X |
| SK-9999 |
| SK-4400 |

**Task:** Count the codes that follow the format exactly, with capital `SK`, four digits and nothing after them.

**Solution:**

```excel
=SUMPRODUCT(--REGEXMATCH(A2:A7, "^SK-\d{4}$"))
```

**Answer:** `3`. SK-1001, SK-9999 and SK-4400 match. SK-12 has too few digits, sk-1002 uses lowercase letters, and SK-1003X has a trailing letter.

### Problem 2: Checking Phone Number Formats

A call center accepts ten-digit North American numbers with optional brackets, spaces, dots or hyphens. Numbers with a country code or too few digits must be reviewed.

| Phone Number |
| --- |
| (555) 123-4567 |
| 555.123.4567 |
| 5551234 |
| +1 555 123 4567 |
| 555-123-4567 |

**Task:** Count the numbers that use the accepted format.

**Solution:**

```excel
=SUMPRODUCT(--REGEXMATCH(A2:A6, "^\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}$"))
```

**Answer:** `3`. The first, second and last numbers match. The short number has too few digits, and the number with the country code starts with a plus sign.

## Use Cases

### SKU Format Checks

**Scenario:** A catalog team wants every new SKU to follow the same pattern before the item is published.

```excel
=IF(REGEXMATCH(A2, "^[A-Z]{2}-\d{4}$"), "OK", "Check code")
```

**Why It Works:** The pattern enforces uppercase letters, a hyphen and four digits, and the flag tells the team which rows to correct.

### Email Domain Filtering

**Scenario:** A marketing team wants only the addresses at its own domain for a partner mailing.

```excel
=FILTER(B2:B500, REGEXMATCH(B2:B500, "@example\.com$"))
```

**Why It Works:** The `$` anchor keeps the match at the end of the address, so `@example.com.au` is not included.

### Phone Number Format Checks

**Scenario:** A list of phone numbers is imported from several sources, and only numbers in one format should be sent to the dialer.

```excel
=IF(REGEXMATCH(C2, "^\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}$"), "Dial", "Review")
```

**Why It Works:** The optional separators accept the common formats, and the anchors reject numbers that carry extra digits.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error for a number | REGEXMATCH accepts only text. | Convert the number with TEXT before testing. |
| `FALSE` for a match you expected | The pattern is case-sensitive, or the anchors are too strict. | Add `(?i)` for case-insensitive matching, or remove the anchors. |
| `TRUE` for a value that should fail | The pattern is not anchored with `^` and `$`. | Add the anchors to test the whole value. |
| Error in the formula | The pattern is invalid, for example it has an unclosed bracket. | Check the brackets and escape characters in the pattern. |
| Error in a FILTER | The FILTER range and the test range have different numbers of rows. | Use the same rows in both ranges. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | The closest alternative is REGEXEXTRACT inside IFERROR, which returns a fallback value when nothing matches. |
| Google Sheets | Available | Uses RE2, which supports `(?i)` but not Unicode character class matching. Accepts text only. |

## Tips and Best Practices

- Test a pattern on a few known good and bad values before you filter a large range.
- Anchor patterns with `^` and `$` when the whole value must match.
- Use TEXT for numeric codes, and keep leading zeros by choosing the right format string.
- Keep long patterns in a helper cell or a named range so they are easy to review.
- Combine REGEXMATCH with FILTER or IF instead of nesting several SEARCH tests.

## Related Functions

| Function | Relationship |
| --- | --- |
| [REGEXEXTRACT](REGEXEXTRACT.md) | Returns the matching text, instead of TRUE or FALSE. |
| [REGEXREPLACE](REGEXREPLACE.md) | Replaces matching text, for cleaning rather than testing. |
| [SEARCH](SEARCH.md) | Tests for a plain text string without patterns. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Keeps the rows where the pattern test returns TRUE. |
| [TEXT](TEXT.md) | Converts a number to text before a pattern test. |

## Official Documentation

- [Google Docs Editors Help: REGEXMATCH](https://support.google.com/docs/answer/3098292)
