---
domain: Spreadsheet Functions
category: Text
subcategory: Regular Expressions
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Invoice Number Extraction
  - Refund Amount Totals
  - Support Ticket Tagging
related:
  - IFERROR
  - REGEXMATCH
  - REGEXREPLACE
  - SEARCH
  - TEXTAFTER
  - VALUE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/regexextract-function
  - https://support.google.com/docs/answer/3098244
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Extract Pattern Match
  - Regex Extract
tags:
  - excel
  - pattern-matching
  - regex
  - sheets
  - text
---

# REGEXEXTRACT

## Description

**REGEXEXTRACT** returns the part of a text string that matches a regular expression, which is a pattern written with symbols such as `\d` for a digit and `+` for one or more. Use it when the piece you need has a recognizable shape, such as an order number, a date or an amount, but its position in the text changes from row to row.

In Excel, the function accepts optional arguments. `return_mode` selects the first match (the default), all matches or the capture groups of the first match. `case_sensitivity` makes the match case-insensitive when it is set to 1. Excel uses the PCRE2 pattern syntax. Google Sheets accepts only the text and the pattern, so it returns the first match, and a capture group in the pattern returns multiple values. Sheets uses the RE2 pattern syntax, and it supports the `(?i)` inline flag for case-insensitive matching.

REGEXEXTRACT always returns text. Wrap the result in VALUE when you need a number. Neither platform's help page describes the result when nothing matches, so wrap the formula in IFERROR when some rows may not contain the pattern.

## Syntax

Microsoft Excel:

```excel
=REGEXEXTRACT(text, pattern, [return_mode], [case_sensitivity])
```

Google Sheets:

```excel
=REGEXEXTRACT(text, regular_expression)
```

<!-- Image 1: REGEXEXTRACT Arguments by Platform. See Images/Text/REGEXEXTRACT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to search, typed in quotation marks or referenced from a cell. |
| `pattern` | Yes (Excel) | The regular expression that describes the text to extract. Sheets calls this argument `regular_expression`. |
| `return_mode` | No (Excel) | `0` returns the first match (default). `1` returns all matches as a list. `2` returns the capture groups from the first match. |
| `case_sensitivity` | No (Excel) | `0` matches case-sensitively (default). `1` matches case-insensitively. In Sheets, use `(?i)` at the start of the pattern instead. |

### Return Value

Text. With the default return mode, one text value holds the first match. With return mode 1, each match is returned as a separate value. With return mode 2 or a capture group in the Sheets pattern, each captured part is returned as a separate value.

## Examples

### Example 1: Finding a Date in a Sentence

```excel
=REGEXEXTRACT("Order 4471 shipped 2025-03-02", "\d{4}-\d{2}-\d{2}")
```

**Result:** `2025-03-02`

The pattern matches four digits, a hyphen, two digits, a hyphen and two digits.

### Example 2: Converting an Extracted Amount to a Number

Cell `A2` contains `Refund $42.50 issued`.

```excel
=VALUE(REGEXEXTRACT(A2, "\d+\.\d{2}"))
```

**Result:** `42.5`

REGEXEXTRACT returns the text `42.50`, and VALUE converts it to a number, so the trailing zero does not show.

### Example 3: Returning All Matches

```excel
=REGEXEXTRACT("red 12, blue 7, green 30", "\d+", 1)
```

**Result:** `12`, `7` and `30` in three cells (Excel only)

Return mode 1 returns every match as a separate value. Each result is text.

<!-- Image 2: Return Modes Compared. See Images/Text/REGEXEXTRACT.md -->

### Example 4: Returning Capture Groups

```excel
=REGEXEXTRACT("SKU AB-1042", "([A-Z]+)-(\d+)", 2)
```

**Result:** `AB` and `1042` in two cells (Excel only)

The two parentheses in the pattern create two capture groups. Return mode 2 returns each group from the first match. Sheets returns the same groups when the pattern contains them, without the return mode argument.

### Example 5: Case-Insensitive Matching

```excel
=REGEXEXTRACT("Invoice inv-77 paid", "INV-\d+", 0, 1)
```

**Result:** `inv-77`

The match is case-insensitive, and the result shows the text exactly as it appears in the source.

In Google Sheets, the same match is written as `=REGEXEXTRACT("Invoice inv-77 paid", "(?i)INV-\d+")`.

### Example 6: Handling Rows Without a Match

```excel
=IFERROR(REGEXEXTRACT("No amount here", "\d+\.\d{2}"), "None")
```

**Result:** `None`

No decimal amount appears in the text, so the formula returns the fallback value instead of an error.

## Story Problems

### Problem 1: Totaling Refund Amounts From Support Notes

A support team keeps notes in a free-text column. Some notes mention a refund or credit with an amount, and others do not.

| Note |
| --- |
| Refund $42.50 issued |
| Credit 18.00 applied |
| No amount yet |
| Charge 130.75 pending |
| Adjustment 7.25 posted |

**Task:** Add up every amount with two decimal places in `A2:A6`. Ignore notes that have no amount.

**Solution:**

```excel
=SUMPRODUCT(IFERROR(VALUE(REGEXEXTRACT(A2:A6, "\d+\.\d{2}")), 0))
```

**Answer:** `198.5`. The amounts are 42.50, 18.00, 130.75 and 7.25, which add to 198.50. The note with no amount adds zero.

### Problem 2: Pulling Order IDs From Ticket Subjects

A help desk wants the four-digit order number from each ticket subject. Some subjects do not contain one.

| Subject |
| --- |
| Re: ORD-2231 delayed |
| Question about invoice |
| ORD-1180 damaged box |
| Pricing ORD-99 unclear |
| ORD-4402 refund |

**Task:** Return the order ID for each subject in column B, and leave the cell blank when there is no four-digit ID.

**Solution:**

```excel
=IFERROR(REGEXEXTRACT(A2, "ORD-\d{4}"), "")
```

Copy the formula down to `B6`.

**Answer:** `ORD-2231`, blank, `ORD-1180`, blank and `ORD-4402`. The pattern requires exactly four digits, so `ORD-99` does not match.

## Use Cases

### Invoice Number Extraction

**Scenario:** Supplier emails contain invoice numbers in the form `INV` followed by digits, and the numbers appear in different positions in each message.

```excel
=IFERROR(REGEXEXTRACT(A2, "INV-\d+"), "")
```

**Why It Works:** The pattern finds the invoice number wherever it appears, and IFERROR keeps the column clean for messages that have none.

### Refund Amount Totals

**Scenario:** Finance needs a monthly refund total from free-text notes, as in Problem 1.

```excel
=SUMPRODUCT(IFERROR(VALUE(REGEXEXTRACT(B2:B500, "\d+\.\d{2}")), 0))
```

**Why It Works:** The regular expression finds the amount in each note, VALUE converts it, and IFERROR gives zero to notes without an amount.

### Support Ticket Tagging

**Scenario:** A help desk wants to tag tickets that mention a product code, such as `PX` followed by three digits.

```excel
=IFERROR(REGEXEXTRACT(A2, "PX\d{3}"), "")
```

**Why It Works:** The tag is the product code itself, so filtering the sheet for a code takes one step.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Error in rows without the pattern | Neither platform's page describes the no-match result. | Wrap the formula in IFERROR. |
| Result is text, not a number | REGEXEXTRACT always returns text. | Wrap the formula in VALUE when you need a number. |
| Wrong text is returned | The pattern matches an earlier part of the text. | Make the pattern more specific, or use a capture group. |
| Multiple values appear in cells | A pattern has capture groups or Excel return mode 1 or 2 is used. | Expect several cells, or use return mode 0 for a single result. |
| Pattern does not match case | Excel is case-sensitive by default. | Set case_sensitivity to 1 in Excel, or add `(?i)` in Sheets. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Excel for the web, Microsoft 365 for Mac and Office for iPhone | Accepts return_mode and case_sensitivity. Uses the PCRE2 pattern syntax. |
| Google Sheets | Available | Accepts only text and regular_expression. Uses RE2, which does not support Unicode character class matching. Use `(?i)` for case-insensitive matching. |

## Tips and Best Practices

- Test the pattern with REGEXMATCH in Sheets, or with a few sample rows in Excel, before copying it down a column.
- Use `\d` and `{n}` for fixed-width codes, and `+` when the length varies.
- Wrap extractions in IFERROR so blank and missing values do not break totals.
- Convert with VALUE only after confirming that the extracted text is a number.
- Keep patterns in a cell or a named range when several formulas share the same rule.

## Related Functions

| Function | Relationship |
| --- | --- |
| [REGEXMATCH](REGEXMATCH.md) | Tests whether a pattern matches, returning TRUE or FALSE. |
| [REGEXREPLACE](REGEXREPLACE.md) | Replaces the matching text instead of returning it. |
| [SEARCH](SEARCH.md) | Finds a fixed string without patterns. |
| [TEXTAFTER](TEXTAFTER.md) | Returns the text after a fixed delimiter, for simpler cases. |
| [VALUE](VALUE.md) | Converts an extracted number from text to a number. |
| [IFERROR](../Logical/IFERROR.md) | Supplies a fallback when a row has no match. |

## Official Documentation

- [Microsoft Support: REGEXEXTRACT function](https://support.microsoft.com/en-us/excel/functions/regexextract-function)
- [Google Docs Editors Help: REGEXEXTRACT](https://support.google.com/docs/answer/3098244)
