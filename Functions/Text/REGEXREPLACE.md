---
domain: Spreadsheet Functions
category: Text
subcategory: Regular Expressions
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Account Number Cleanup
  - Phone Number Normalization
  - Stripping Extra Spaces
related:
  - REGEXEXTRACT
  - REGEXMATCH
  - REPLACE
  - SUBSTITUTE
  - TRIM
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/regexreplace-function
  - https://support.google.com/docs/answer/3098245
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Pattern Replace
  - Regex Replace
tags:
  - data-cleaning
  - excel
  - pattern-matching
  - regex
  - sheets
  - text
---

# REGEXREPLACE

## Description

**REGEXREPLACE** finds every part of a text string that matches a regular expression and replaces it with new text. A pattern describes the shape of the text rather than the exact words, so one formula can remove all punctuation, collapse runs of spaces or mask every number in a sentence.

Use REGEXREPLACE for cleaning jobs that SUBSTITUTE cannot handle, because SUBSTITUTE replaces only fixed text. When the pattern is a single fixed string, SUBSTITUTE is simpler. When you want the matching text instead of the rest of the string, use REGEXEXTRACT.

Excel and Google Sheets accept different arguments. Excel adds an `occurrence` argument, which can target one match counted from the end, and a `case_sensitivity` argument. Sheets accepts only the text, the pattern and the replacement, and it replaces every match. Sheets uses the RE2 pattern syntax, so use `(?i)` for case-insensitive matching. Excel uses the PCRE2 syntax.

## Syntax

Microsoft Excel:

```excel
=REGEXREPLACE(text, pattern, replacement, [occurrence], [case_sensitivity])
```

Google Sheets:

```excel
=REGEXREPLACE(text, regular_expression, replacement)
```

<!-- Image 1: REGEXREPLACE Arguments by Platform. See Images/Text/REGEXREPLACE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to change. Enter it in quotation marks, reference a cell, or use a formula that returns text. |
| `pattern` | Yes (Excel) | The regular expression that describes the text to replace. Sheets calls this argument `regular_expression`. |
| `replacement` | Yes | The text that takes the place of each match. An empty string removes the matches. In Excel, capturing groups can be referenced with `$n`. |
| `occurrence` | No (Excel) | `0` replaces every match (default). A negative number targets one match counted from the end, so `-1` targets the last match. |
| `case_sensitivity` | No (Excel) | `0` matches case-sensitively (default). `1` matches case-insensitively. In Sheets, use `(?i)` at the start of the pattern instead. |

### Return Value

Text. The original text with each matching part replaced. If nothing matches, the text is returned unchanged.

## Examples

### Example 1: Keeping Only the Digits

```excel
=REGEXREPLACE("(555) 123-4567", "\D", "")
```

**Result:** `5551234567`

`\D` matches every character that is not a digit, and each match is replaced with nothing.

<!-- Image 2: Removing Non-Digits Before and After. See Images/Text/REGEXREPLACE.md -->

### Example 2: Replacing Every Number

```excel
=REGEXREPLACE("Order 4471 and 900", "\d+", "#")
```

**Result:** `Order # and #`

`\d+` matches each run of one or more digits, so both numbers are replaced.

### Example 3: Replacing Only the Last Match (Excel)

```excel
=REGEXREPLACE("a-b-c-d", "-", "/", -1)
```

**Result:** `a-b-c/d` (Excel only)

The negative occurrence counts from the end, so only the last hyphen is replaced.

### Example 4: Case-Insensitive Replacement (Excel)

```excel
=REGEXREPLACE("Cat cat CAT", "cat", "dog", 0, 1)
```

**Result:** `dog dog dog`

Each of the three words matches because the case_sensitivity argument is 1.

### Example 5: Case-Insensitive Replacement (Sheets)

```excel
=REGEXREPLACE("Cat cat CAT", "(?i)cat", "dog")
```

**Result:** `dog dog dog`

The `(?i)` flag makes the match ignore case, which gives the same result as Example 4 in Excel.

### Example 6: Collapsing Runs of Spaces

```excel
=REGEXREPLACE("  Blue    widget  ", "\s+", " ")
```

**Result:** ` Blue widget ` (one leading space, one trailing space)

Each run of spaces becomes one space. The leading and trailing spaces are shortened, not removed, so wrap the formula in TRIM when they must go.

## Story Problems

### Problem 1: Adding Digits From Mixed Account Codes

A bank export holds account codes with letters, hyphens, slashes and spaces mixed in. The auditor needs the total of the digits in the four codes in `A2:A5`.

| Account Code |
| --- |
| AC-100-45 |
| BK 2210 |
| CD/7-3 |
| EF 88 1 |

**Task:** Remove everything that is not a digit from each code, then add the numbers.

**Solution:**

```excel
=SUMPRODUCT(VALUE(REGEXREPLACE(A2:A5, "\D", "")))
```

**Answer:** `13209`. The digits form 10045, 2210, 73 and 881, which add to 13209.

### Problem 2: Summing Amounts Written With Currency Signs

A purchasing list holds amounts with dollar signs and thousands separators, such as `$1,250.00`, and the total needs to be a number.

| Amount |
| --- |
| $1,250.00 |
| $87.50 |
| $12,000 |

**Task:** Remove the dollar signs and commas from each amount, then add the three values.

**Solution:**

```excel
=SUMPRODUCT(VALUE(REGEXREPLACE(A2:A4, "[$,]", "")))
```

**Answer:** `13337.5`, because 1250.00 + 87.50 + 12000 = 13337.50.

## Use Cases

### Account Number Cleanup

**Scenario:** A payment file contains account numbers with spaces and hyphens, and the bank accepts only letters and digits.

```excel
=REGEXREPLACE(A2, "[^A-Za-z0-9]", "")
```

**Why It Works:** The negated class matches every character that is not a letter or digit, and each one is removed.

### Phone Number Normalization

**Scenario:** Phone numbers arrive in many formats, and the dialer needs digits only.

```excel
=REGEXREPLACE(B2, "\D", "")
```

**Why It Works:** Brackets, spaces, dots and hyphens are all non-digits, so one pattern normalizes every format.

### Stripping Extra Spaces

**Scenario:** Product names pasted from a web page contain runs of spaces between words.

```excel
=TRIM(REGEXREPLACE(C2, "\s+", " "))
```

**Why It Works:** The pattern collapses each run of whitespace into one space, and TRIM removes the leading and trailing spaces that remain.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Nothing changed | The pattern does not match, or it is case-sensitive. | Test the pattern on one value, and add `(?i)` in Sheets or set case_sensitivity to 1 in Excel. |
| Every match replaced when only one was wanted | Excel defaults to occurrence 0, which replaces all matches. | Set a negative occurrence in Excel, or narrow the pattern in Sheets. |
| `$1` appears in the output in Sheets | The Sheets help page does not describe backreferences. | Avoid capturing groups in the replacement, or use REGEXEXTRACT instead. |
| Number is text after cleaning | REGEXREPLACE returns text. | Wrap the result in VALUE when you need a number. |
| Error in the formula | The pattern is invalid, for example a bracket is not closed. | Check the brackets and escape characters. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Excel for the web, Microsoft 365 for Mac and Office for iPhone | Accepts occurrence and case_sensitivity. Capturing groups can be used in the replacement with `$n`. Uses the PCRE2 pattern syntax. |
| Google Sheets | Available | Accepts only text, regular_expression and replacement, and replaces every match. Uses RE2, which supports `(?i)`. The help page does not describe backreferences in the replacement. |

## Tips and Best Practices

- Test a pattern on a few sample values before copying the formula down a column.
- Use `\D` to keep digits and `[^A-Za-z0-9]` to keep letters and digits.
- Wrap the result in TRIM when spaces remain after the cleanup.
- Convert the result with VALUE only after confirming that it contains only digits.
- Keep the original column so you can compare the cleaned value with the source.

## Related Functions

| Function | Relationship |
| --- | --- |
| [REGEXEXTRACT](REGEXEXTRACT.md) | Returns the matching text instead of replacing it. |
| [REGEXMATCH](REGEXMATCH.md) | Tests whether a pattern matches, returning TRUE or FALSE. |
| [SUBSTITUTE](SUBSTITUTE.md) | Replaces fixed text, which is simpler when the pattern is one string. |
| [REPLACE](REPLACE.md) | Replaces characters by their position in the text. |
| [TRIM](TRIM.md) | Removes leading and trailing spaces after a cleanup. |

## Official Documentation

- [Microsoft Support: REGEXREPLACE function](https://support.microsoft.com/en-us/excel/functions/regexreplace-function)
- [Google Docs Editors Help: REGEXREPLACE](https://support.google.com/docs/answer/3098245)
