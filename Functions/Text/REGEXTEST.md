---
domain: Spreadsheet Functions
category: Text
subcategory: Regular Expressions
purpose:
  - Data Validation
  - Text Manipulation
use-case:
  - Email Format Checks
  - Part Number Validation
  - Vendor Catalog Cleanup
related:
  - IF
  - ISNUMBER
  - REGEXEXTRACT
  - REGEXMATCH
  - REGEXREPLACE
  - SEARCH
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/regextest-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Pattern Test
  - Regex Test
tags:
  - excel
  - pattern-matching
  - regex
  - validation
---

# REGEXTEST

## Description

**REGEXTEST** checks whether a text value matches a regular expression (regex) pattern. It returns `TRUE` when any part of the text matches the pattern and `FALSE` when none of it does. Use it when a plain text search is not precise enough, for example to confirm that a part number has two letters, a hyphen and four digits, or that a code contains no stray characters.

Because REGEXTEST reports whether a match exists, it works well inside `IF`, `FILTER` and `COUNTIF` formulas. Use [REGEXEXTRACT](REGEXEXTRACT.md) when you need the matching text itself, and [REGEXREPLACE](REGEXREPLACE.md) when you need to change it.

The match is case sensitive by default. The optional third argument switches to case-insensitive matching. Anchors such as `^` (start of text) and `$` (end of text) control whether the pattern must cover the whole value or only a part of it.

REGEXTEST is available in Excel for Microsoft 365, Excel for Microsoft 365 for Mac and Excel for the web. Google Sheets has no REGEXTEST function. Use [REGEXMATCH](REGEXMATCH.md) there.

## Syntax

```excel
=REGEXTEST(text, pattern, [case_sensitivity])
```

<!-- Image 1: Pattern Argument Anatomy. See Images/Text/REGEXTEST.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text, or a cell reference that holds the text, to test. |
| `pattern` | Yes | The regular expression that describes the text to match. Patterns use the PCRE2 syntax. |
| `case_sensitivity` | No | `0` for case-sensitive matching or `1` for case-insensitive matching. The default is case sensitive. |

### Return Value

`TRUE` when any part of `text` matches `pattern`, and `FALSE` when no part matches. The result is a logical value, so it can feed `IF`, `FILTER` or `COUNTIF` directly. The Microsoft page does not describe any error conditions for this function.

## Examples

### Example 1: Test a Part Number Pattern

```excel
=REGEXTEST("AB-1234", "^[A-Z]{2}-\d{4}$")
```

**Result:** `TRUE`

The pattern asks for two uppercase letters, a hyphen, and exactly four digits, with nothing before or after. The value fits that shape, so the result is `TRUE`.

### Example 2: Match Without Regard to Case

```excel
=REGEXTEST("ab-1234", "^[A-Z]{2}-\d{4}$", 1)
```

**Result:** `TRUE`

The third argument `1` makes the comparison case insensitive, so the lowercase letters match the uppercase pattern. With the default setting, the same call returns `FALSE`.

### Example 3: Combined With IF

```excel
=IF(REGEXTEST(A2, "^\d{5}$"), "Valid ZIP", "Check ZIP")
```

**Result:** `Valid ZIP` when A2 contains `78701`

The pattern accepts exactly five digits. Any other value returns `Check ZIP`, so the formula flags short codes and codes with letters in one step.

### Example 4: Match Any Part of the Text

```excel
=REGEXTEST("Order 88 shipped", "\d{3}")
```

**Result:** `FALSE`

Without `^` or `$`, the pattern matches anywhere in the text. This value has only two consecutive digits, so no part matches three digits and the result is `FALSE`. Changing the text to `Order 880 shipped` returns `TRUE`.

### Example 5: Check the End of a Value

```excel
=REGEXTEST("Bldg 4, Austin TX 78701", "\d{5}$")
```

**Result:** `TRUE`

The `$` anchor requires the match to sit at the end of the text. The address ends with a five-digit postal code, so the test passes.

### Example 6: Count Passing Rows

```excel
=COUNTIF(B2:B6, TRUE)
```

**Result:** `2` when column B holds the REGEXTEST results for the five part numbers in the Story Problems section

COUNTIF counts the logical `TRUE` values that the REGEXTEST formulas filled down column B produced.

<!-- Image 2: Part Number Results Column. See Images/Text/REGEXTEST.md -->

## Story Problems

### Problem 1: Part Number Check Before a Vendor Import

A purchasing team receives a catalog from a supplier. Every valid part number has two uppercase letters, a hyphen and four digits. The team needs to know how many rows pass before the import runs.

| Part Number | Valid Format |
| --- | --- |
| AB-1234 | |
| ab-1234 | |
| AB-12345 | |
| XY-9081 | |
| Q-1000 | |

**Task:** Count the part numbers that match the required format.

**Solution:**

```excel
=REGEXTEST(A2, "^[A-Z]{2}-\d{4}$")
=COUNTIF(B2:B6, TRUE)
```

**Answer:** `2`. `AB-1234` and `XY-9081` pass. The lowercase `ab-1234` fails because matching is case sensitive by default, `AB-12345` has five digits, and `Q-1000` has one letter.

### Problem 2: Phone Number Formats

A call center accepts phone numbers in three styles. The team wants to accept a number only when it has a three-digit area code, a three-digit exchange, and a four-digit line number separated by a hyphen. An optional area code in parentheses or a space after it is allowed.

| Number | Accepted |
| --- | --- |
| (512) 555-0198 | |
| 512-555-0198 | |
| 5125550198 | |
| 555-01 | |

**Task:** Count the numbers the pattern accepts.

**Solution:**

```excel
=REGEXTEST(A2, "^\(?\d{3}\)?[ -]?\d{3}-\d{4}$")
```

**Answer:** `2`. The first two numbers pass. `5125550198` has no hyphen before the last four digits, and `555-01` is too short.

<!-- Image 3: Email Format Check Layout. See Images/Text/REGEXTEST.md -->

## Use Cases

### Email Format Checks

**Scenario:** A marketing team imports a list of sign-up addresses and wants to flag entries that obviously lack an `@` sign or a domain.

```excel
=REGEXTEST(A2, "^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$")
```

**Why It Works:** The pattern requires one `@`, no spaces, and a final dot followed by at least two letters. It catches obvious errors, but it does not prove that an address exists. Confirm important addresses another way.

### Part Number Validation

**Scenario:** An inventory sheet receives part numbers from several suppliers, and only codes in the `AB-1234` format can be entered into the warehouse system.

```excel
=IF(REGEXTEST(A2, "^[A-Z]{2}-\d{4}$"), "OK", "Review")
```

**Why It Works:** The `IF` wrapper turns the logical result into a readable status column. Rows marked `Review` can be sorted and corrected before they are entered.

### Vendor Catalog Cleanup

**Scenario:** A supplier catalog sometimes includes codes with leading or trailing spaces, which break lookups.

```excel
=REGEXTEST(A2, "^\s|\s$")
```

**Why It Works:** The pattern matches a space at the start or at the end of the value. Rows that return `TRUE` can be trimmed with TRIM before the lookup runs.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `FALSE` for a value that looks correct | The pattern is case sensitive by default and the value uses different letter case. | Pass `1` as the third argument, or change the pattern. |
| `TRUE` for a value that should fail | The pattern has no anchors, so it matches a part of a longer value. | Add `^` at the start and `$` at the end. |
| `FALSE` for a valid pattern | The pattern uses syntax that is not PCRE2, such as a Sheets-only construct. | Rewrite the pattern in PCRE2 syntax and test it on a few rows. |
| Wrong result after a change | The third argument was entered as text such as `"1"` in a cell that is not a number. | Enter `0` or `1` as a number, or reference a cell that holds the number. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel for Microsoft 365 for Mac, Excel for the web | Patterns use the PCRE2 flavor. The page documents no regex flags beyond `case_sensitivity`. |
| Google Sheets | Not available | The closest alternative is REGEXMATCH, which tests for a match in the same way. Check its pattern syntax on its own page before you reuse a pattern. |

## Tips and Best Practices

- Test the pattern on five or six sample values, including edge cases, before filling it down a column.
- Anchor the pattern with `^` and `$` when the whole value must match, and leave them out when a part is enough.
- Use the case-insensitive setting only when letter case in the data is not meaningful.
- Pair REGEXTEST with IF to show a readable status instead of raw `TRUE` and `FALSE` values.
- Use REGEXEXTRACT rather than REGEXTEST when you need the matched text.
- Keep a short list of tested patterns in a sheet tab so the team can reuse them.

## Related Functions

| Function | Relationship |
| --- | --- |
| [REGEXMATCH](REGEXMATCH.md) | The Google Sheets equivalent that returns `TRUE` or `FALSE` for a match. |
| [REGEXEXTRACT](REGEXEXTRACT.md) | Returns the matching text instead of a logical result. |
| [REGEXREPLACE](REGEXREPLACE.md) | Changes the text that matches the pattern. |
| [SEARCH](SEARCH.md) | Finds a plain text string and returns its position, without a pattern. |
| [IF](../Logical/IF.md) | Turns the `TRUE` or `FALSE` result into a label or status. |
| [ISNUMBER](../Information/ISNUMBER.md) | Checks whether a value is a number, which complements a pattern check on numeric codes. |

## Official Documentation

- [Microsoft Support: REGEXTEST function](https://support.microsoft.com/en-us/excel/functions/regextest-function)
