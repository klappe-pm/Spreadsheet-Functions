---
domain: Spreadsheet Functions
category: Text
subcategory: Text Joining and Splitting
purpose:
  - Array Shaping
  - Text Manipulation
use-case:
  - Attendee Name Lists
  - Date Part Splitting
  - Warehouse Aisle Codes
related:
  - JOIN
  - REGEXEXTRACT
  - TEXTJOIN
  - TEXTSPLIT
  - TRIM
level: 2
source:
  - https://support.google.com/docs/answer/3094136
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Split Text
  - Split by Delimiter
tags:
  - delimiter
  - sheets
  - spill-range
  - text-splitting
---

# SPLIT

## Description

**SPLIT** divides a text value into pieces at each occurrence of a delimiter, and places each piece in its own cell in the same row. Use it when a single cell holds several values separated by a comma, semicolon, slash or other character, such as a list of tags, a date written as `2026/03/14`, or a set of codes separated by semicolons.

SPLIT is a Google Sheets function. Microsoft Excel does not have a SPLIT function, and the closest alternative in Microsoft 365 is TEXTSPLIT.

By default, SPLIT treats each character in the delimiter as a separate delimiter. A delimiter of `; ` therefore splits at both the semicolon and the space. Set the optional `split_by_each` argument to `FALSE` to split only at the complete delimiter string. Consecutive delimiters normally produce no empty cells, because `remove_empty_text` defaults to `TRUE`.

The pieces are returned across columns from the cell where the formula is entered, so SPLIT fills a row. To split several cells, use the formula in each row or wrap the source in ARRAYFORMULA.

## Syntax

```excel
=SPLIT(text, delimiter, [split_by_each], [remove_empty_text])
```

<!-- Image 1: Delimiter Splitting Anatomy. See Images/Text/SPLIT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to divide. A cell reference or a literal string is accepted. |
| `delimiter` | Yes | The character or characters that mark the divisions. Each character is a separate delimiter unless `split_by_each` is `FALSE`. |
| `split_by_each` | No | `TRUE` (default) splits at each character in `delimiter`. `FALSE` splits only at the complete delimiter string. |
| `remove_empty_text` | No | `TRUE` (default) removes empty pieces, so consecutive delimiters act as one. `FALSE` keeps an empty cell between consecutive delimiters. |

### Return Value

The pieces of `text`, placed in consecutive cells of one row starting at the cell that holds the formula. The delimiter characters are not included in the pieces.

## Examples

### Example 1: Split a Comma-Separated List

```excel
=SPLIT("North,South,East", ",")
```

**Result:** `North` in the formula cell, `South` in the next cell, and `East` in the one after.

Each comma is a delimiter, and each part of the list fills one cell in the row.

### Example 2: Split at Each Character of a Delimiter

```excel
=SPLIT("red; green blue", "; ")
```

**Result:** `red`, `green`, `blue` in three adjacent cells

With the default `split_by_each` of `TRUE`, the semicolon and the space both act as delimiters. Empty pieces between them are removed by default.

### Example 3: Split at the Whole Delimiter

```excel
=SPLIT("Oak Hill; Pine Ridge", "; ", FALSE)
```

**Result:** `Oak Hill` and `Pine Ridge` in two adjacent cells

Setting `split_by_each` to `FALSE` means the space inside `Oak Hill` is not a delimiter. Only the complete `; ` string divides the text.

### Example 4: Keep Empty Pieces

```excel
=SPLIT("1,,2", ",", TRUE, FALSE)
```

**Result:** `1`, an empty cell, and `2` in three adjacent cells

Setting `remove_empty_text` to `FALSE` keeps the empty piece between the two commas, which preserves the position of each value in the row.

### Example 5: Split a Date

```excel
=SPLIT("2026/03/14", "/")
```

**Result:** `2026`, `03` and `14` in three adjacent cells

Each slash divides the date into year, month and day. The parts stay as text, so convert them with VALUE if they feed a calculation.

<!-- Image 2: Split Result Across Columns. See Images/Text/SPLIT.md -->

## Story Problems

### Problem 1: Split Warehouse Aisle Codes

A warehouse stores the aisle codes for each product in one cell, separated by semicolons. The picking team needs each code in its own column to build a route.

| Aisle Codes |
| --- |
| A12;B07;C33 |

**Task:** Split the codes and state the value in the second cell of the row.

**Solution:**

```excel
=SPLIT(A2, ";")
```

**Answer:** `B07` in the second cell, with `A12` in the first and `C33` in the third.

### Problem 2: Split a Speaker List

An event planner lists the speakers for a session in one cell, separated by slashes with a space on each side. The planner needs each name in its own cell, and no name should be split at the space inside it.

| Speakers |
| --- |
| Ruiz / Kim Lee / Osei |

**Task:** Split the list so that `Kim Lee` stays as one name, and state the value of the second cell.

**Solution:**

```excel
=SPLIT(A2, " / ", FALSE)
```

**Answer:** `Kim Lee`. Setting `split_by_each` to `FALSE` treats the whole ` / ` as the delimiter, so the space inside `Kim Lee` is kept.

<!-- Image 3: Speaker List Split Result. See Images/Text/SPLIT.md -->

## Use Cases

### Attendee Name Lists

**Scenario:** A registration export stores several attendee names in one cell, separated by semicolons, and the team needs one name per row for name badges.

```excel
=SPLIT(A2, ";")
```

**Why It Works:** The formula fills the names across a row. TRANSPOSE or a second step can turn the row into a column when badges are printed row by row.

### Date Part Splitting

**Scenario:** Order dates arrive as text in the form `2026/03/14`, and the analysts need the year and month separately.

```excel
=SPLIT(A2, "/")
```

**Why It Works:** Each part lands in its own cell, so the year and month can be referenced directly. Convert the parts with VALUE when they are used in calculations.

### Warehouse Aisle Codes

**Scenario:** Each product record lists several aisle codes, and the picking team needs a count of codes per product.

```excel
=COUNTA(SPLIT(A2, ";"))
```

**Why It Works:** SPLIT returns the codes in one row, and COUNTA counts the non-empty cells. The result is the number of aisles to visit for that product.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Pieces split at spaces | The delimiter has spaces, and `split_by_each` is `TRUE`. | Set `split_by_each` to `FALSE` for a whole-string delimiter. |
| Empty cells in the row | `remove_empty_text` is `FALSE`, or the delimiter is missing at the end. | Set `remove_empty_text` to `TRUE`, or trim the source. |
| Result is blocked | The cells to the right of the formula already hold values. | Clear the cells that the result must fill. |
| Only one value appears | The delimiter is not in the text. | Check the source value and the delimiter character. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | The closest alternative is TEXTSPLIT in Microsoft 365, which has a similar purpose with a different argument layout. |
| Google Sheets | Available | Four arguments, with `split_by_each` and `remove_empty_text` both defaulting to `TRUE`. The results spill across columns. |

## Tips and Best Practices

- Set `split_by_each` to `FALSE` whenever the delimiter is a word or contains a space.
- Trim the source with TRIM when data comes from forms or exports, to avoid stray spaces in the pieces.
- Leave the cells to the right of the formula empty, so the spilled result has room to fill.
- Use ARRAYFORMULA to split every value in a column at once.
- Convert date parts with VALUE before using them in date formulas.

## Related Functions

| Function | Relationship |
| --- | --- |
| [JOIN](JOIN.md) | Combines values with a delimiter, the reverse of SPLIT. |
| [TEXTJOIN](TEXTJOIN.md) | Joins text with a delimiter and can skip empty values. |
| [TEXTSPLIT](TEXTSPLIT.md) | The Microsoft 365 equivalent for splitting text into rows and columns. |
| [REGEXEXTRACT](REGEXEXTRACT.md) | Returns a pattern-matched part of the text when the pieces are not separated by a fixed delimiter. |
| [TRIM](TRIM.md) | Removes extra spaces from the pieces after splitting. |

## Official Documentation

- [Google Docs Editors Help: SPLIT](https://support.google.com/docs/answer/3094136)
