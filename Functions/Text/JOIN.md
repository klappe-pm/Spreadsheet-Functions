---
domain: Spreadsheet Functions
category: Text
subcategory: Text Joining and Splitting
purpose:
  - Text Manipulation
use-case:
  - Address Assembly
  - Code Assembly
  - Tag Lists
related:
  - ARRAYFORMULA
  - CONCAT
  - CONCATENATE
  - SPLIT
  - TEXTJOIN
level: 3
source:
  - https://support.google.com/docs/answer/3094077
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Join Values
  - Join With Delimiter
tags:
  - concatenation
  - delimiter
  - sheets
  - text-joining
---

# JOIN

## Description

**JOIN** combines the values of one or more one-dimensional ranges or arrays into a single text string, with a delimiter placed between each value. For example, `JOIN(", ", A2:A4)` returns the values in A2:A4 separated by a comma and a space.

Use JOIN when a list needs to appear on one line, such as a list of tags, a set of names in a status cell or a code built from several parts. The delimiter can be any text, including an empty string when the values should run together.

JOIN is available only in Google Sheets. Excel has no JOIN function. The closest Excel equivalent is TEXTJOIN, which takes an ignore-empty argument and can join ranges in the same way. Sheets also offers TEXTJOIN, so formulas written with TEXTJOIN can usually be moved between the two platforms.

JOIN differs from CONCAT and CONCATENATE in that the delimiter is added between every value automatically. CONCAT and CONCATENATE join values without a separator unless you type one in each argument.

## Syntax

```excel
=JOIN(delimiter, value_or_array1, [value_or_array2, ...])
```

<!-- Image 1: JOIN Arguments and Output. See Images/Text/JOIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `delimiter` | Yes | The text placed between each joined value, such as `", "`, `"-"` or `" | "`. Use an empty string (`""`) to join values with no separator. |
| `value_or_array1` | Yes | The first value or one-dimensional range to join, such as `A2:A4` or a literal in quotes. |
| `value_or_array2, ...` | No | Additional values or one-dimensional ranges to join after the first one. |

### Return Value

A single text string that contains every value in order, with the delimiter between each pair. The function returns text even when the values are numbers.

## Examples

### Example 1: Joining Literal Values

```excel
=JOIN(", ", "red", "blue", "green")
```

**Result:** `"red, blue, green"`

Each literal is placed in order, with a comma and a space between them.

### Example 2: Joining a Date From Parts

```excel
=JOIN("-", A2:A4)
```

Where A2:A4 contain `2026`, `03` and `14`

**Result:** `"2026-03-14"`

The three cells form a date string with hyphens. The values remain text, so leading zeros in `03` are kept.

### Example 3: Joining Without a Separator

```excel
=JOIN("", "A", "7", "X")
```

**Result:** `"A7X"`

An empty delimiter places nothing between the values, which is useful for building codes.

### Example 4: Joining a Column of Names

```excel
=JOIN(" | ", B2:B4)
```

Where B2:B4 contain `Ana`, `Ben` and `Cy`

**Result:** `"Ana | Ben | Cy"`

The pipe symbol separates each name. A vertical bar inside quotes is a plain character in the delimiter.

## Story Problems

### Problem 1: Listing Approved Tags

A content team keeps three approved tags for an article in A2:A4. The article form needs them on one line in a single cell.

| Tag |
| --- |
| red |
| blue |
| green |

**Task:** Join the tags in A2:A4 into one string separated by a comma and a space.

**Solution:**

```excel
=JOIN(", ", A2:A4)
```

**Answer:** `"red, blue, green"`. JOIN adds the separator between each pair of tags, in the order the cells appear.

<!-- Image 2: Tags Joined Into One Cell. See Images/Text/JOIN.md -->

### Problem 2: Building a Product Code

A warehouse builds a product code from three parts kept in B2:B4: a letter, a digit and a suffix letter. The code must have no separators.

| Part | Value |
| --- | --- |
| Prefix | A |
| Number | 7 |
| Suffix | X |

**Task:** Join the three parts in B2:B4 into one code with no separator.

**Solution:**

```excel
=JOIN("", B2:B4)
```

**Answer:** `"A7X"`. The empty delimiter places nothing between the parts.

## Use Cases

### Address Assembly

**Scenario:** A mailing list stores street, city and postal code in separate columns. The label template needs one line per address.

```excel
=JOIN(", ", A2:C2)
```

**Why It Works:** JOIN adds a comma and space between each part, so the address reads as one line. A blank part may still contribute its separator, so check records with missing parts before printing.

### Code Assembly

**Scenario:** A logistics team creates a shipment reference from the origin code, the year and the sequence number.

```excel
=JOIN("-", D2:F2)
```

**Why It Works:** One formula produces a reference such as `NYC-2026-0457`. Keep the parts as text when they have leading zeros, so the sequence number is not changed.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` in Excel | Excel has no JOIN function. | Use TEXTJOIN in Excel, with the same delimiter and range. |
| Unexpected separators | A blank cell in the range may still contribute its delimiter. | Check the source range for blanks before joining. |
| Missing spaces | The delimiter was typed without a trailing space. | Add the space inside the quotes, such as `", "`. |
| Numbers look different | The joined value uses the raw number, not the cell's display format. | Format the numbers as text first with TEXT when the display matters. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available. | The closest alternative is TEXTJOIN, available in Excel 2019 and Microsoft 365. TEXTJOIN also has an argument that skips empty cells. |
| Google Sheets | Available. | Joins one-dimensional ranges and values. The delimiter can be an empty string. |

## Tips and Best Practices

- Use a delimiter with a visible space when the joined text will be read by people.
- Use an empty string as the delimiter for codes that must not contain separators.
- Check the source range for blank cells, because blanks can leave extra separators.
- Use SPLIT to reverse a JOIN when you need the parts back in separate cells.
- Use TEXTJOIN in Excel workbooks that must join ranges.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CONCAT](CONCAT.md) | Joins values with no separator, unless you type one in each argument. |
| [CONCATENATE](CONCATENATE.md) | Joins a fixed list of values, one argument at a time. |
| [SPLIT](SPLIT.md) | Splits text by a delimiter, the reverse of JOIN. |
| [TEXTJOIN](TEXTJOIN.md) | The Excel counterpart of JOIN, with an option to skip empty values. |
| [ARRAYFORMULA](../Google-specific/ARRAYFORMULA.md) | Applies a formula to a whole range, which helps when JOIN is combined with row-by-row text. |

## Official Documentation

- [Google Docs Editors Help: JOIN](https://support.google.com/docs/answer/3094077)
