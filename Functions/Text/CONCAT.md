---
domain: Spreadsheet Functions
category: Text
subcategory: Text Joining and Splitting
purpose:
  - Text Manipulation
use-case:
  - Address Lines
  - Building Full Names
  - Multi-Column Keys
related:
  - ARRAYTOTEXT
  - CONCATENATE
  - JOIN
  - TEXTJOIN
  - TEXTSPLIT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/concat-function
  - https://support.google.com/docs/answer/3093592
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Join Text
tags:
  - concatenation
  - excel
  - sheets
  - text-joining
---

# CONCAT

## Description

**CONCAT** joins text from several items into one string, in the order the items are given. It adds nothing between the items, so any space or punctuation must be supplied as an argument. It replaces CONCATENATE in Excel, and it improves on that function in one key way: each argument can be a range, so CONCAT(A2:A10) joins every cell in the range without listing them one by one.

Use CONCAT to assemble full names, address lines and lookup keys from several cells. When you need a separator between values, or want empty cells skipped, use TEXTJOIN instead, because CONCAT does neither.

In Excel, CONCAT returns `#VALUE!` when the combined text would be longer than 32,767 characters, which is the limit for one cell. In Google Sheets, CONCAT takes exactly two values and behaves like the `&` operator, so use the `&` operator or CONCATENATE for longer lists in Sheets.

<!-- Image 1: Range and Separator Arguments. See Images/Text/CONCAT.md -->

## Syntax

```excel
=CONCAT(text1, [text2], ...)
```

Google Sheets uses the form `=CONCAT(value1, value2)`.

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text1` | Yes | The first item to join. It can be a string, a number or a range, such as `A2:A10`. In Google Sheets this argument is `value1`. |
| `text2`, ... | No | Additional items. Excel allows up to 253 text arguments in total. In Google Sheets this argument is `value2`. |

### Return Value

A single text string made by joining every item in order. The result is `#VALUE!` when it exceeds 32,767 characters.

## Examples

### Example 1: Joining Two Cells

```excel
=CONCAT(A2, B2)
```

Where `A2` contains `Mar` and `B2` contains `ch`.

**Result:** `March`

No separator is added, so the two parts meet directly.

### Example 2: Joining a Range

```excel
=CONCAT(A2:A4)
```

Where `A2:A4` contain `red`, `green` and `blue`.

**Result:** `redgreenblue`

Every cell in the range is joined in order, with no separator.

### Example 3: Adding a Space Between Words

```excel
=CONCAT(A2, " ", B2)
```

Where `A2` contains `Ada` and `B2` contains `Lovelace`.

**Result:** `Ada Lovelace`

The space is an argument of its own, so it appears in the result.

### Example 4: Mixing a Range and a Single Cell

```excel
=CONCAT(A2:B2, C2)
```

Where `A2` contains `Room`, `B2` contains `12` and `C2` contains `B`.

**Result:** `Room12B`

The range contributes its two cells, and the single cell is appended after them.

<!-- Image 2: Range Joining Versus Separators. See Images/Text/CONCAT.md -->

## Story Problems

### Problem 1: Building Product Keys From a Row

A product table in `A1:C3` holds a category, a number and a size.

| Category | Number | Size |
| --- | --- | --- |
| Desk | 204 | M |
| Shelf | 11 | L |

**Task:** Build a key for each row in column D by joining all three cells.

**Solution:**

```excel
=CONCAT(A2:C2)
```

Fill this formula down to `D3`.

**Answer:** `Desk204M` for row 2 and `Shelf11L` for row 3, because CONCAT reads each row's three cells in order.

### Problem 2: Joining a List of Names Without Spaces

A list of first names sits in `A2:A4`: Ivan, Mia and Noor.

**Task:** Join all three names into one cell with no separators.

**Solution:**

```excel
=CONCAT(A2:A4)
```

**Answer:** `IvanMiaNoor`. To add spaces between the names, use TEXTJOIN with a delimiter instead.

## Use Cases

### Building Full Names

**Scenario:** A mailing list stores first and last names in separate columns, and the letter template needs them as one name.

```excel
=CONCAT(A2, " ", B2)
```

**Why It Works:** The space argument separates the names. If some rows have no first name, the result starts with a space, so TRIM or TEXTJOIN with `ignore_empty` gives a cleaner result.

### Multi-Column Lookup Keys

**Scenario:** A lookup must match on region and code together, and the match needs a single key.

```excel
=CONCAT(A2, "|", B2)
```

**Why It Works:** Fill this formula down in a helper column, then match the combined key against that column with MATCH. CONCAT works row by row here, so it should not be used on a whole column of separate rows.

### Address Lines

**Scenario:** A shipping export needs one line per address, such as a city, a state and a postal code.

```excel
=CONCAT(B2, ", ", C2, " ", D2)
```

**Why It Works:** The formula places a comma and a space between the city and state, and a space before the postal code, so the line reads `Glenview, IL 60025`.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The combined result is longer than 32,767 characters. | Split the text across cells, or join fewer items. |
| Words run together | No separator argument was supplied. | Add `" "` or another separator as an argument. |
| Gaps where blank cells were | Empty cells add nothing, but the separators around them remain. | Use TEXTJOIN with `ignore_empty` set to TRUE. |
| Numbers look unformatted | The number is converted to text in general format. | Wrap dates and currency values in TEXT first. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019, Excel 2016 and Microsoft Office | Accepts ranges and up to 253 text arguments. The result is limited to 32,767 characters. |
| Google Sheets | Available | Takes two values, `value1` and `value2`. It works like the `&` operator. |

## Tips and Best Practices

- Use CONCAT for a row or column of values that need no separator.
- Use TEXTJOIN when you need a delimiter or want blanks skipped.
- Use the `&` operator for two or three items when it reads more clearly.
- Format dates and numbers with TEXT before joining them.
- Wrap the result in TRIM when blank cells leave extra spaces.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ARRAYTOTEXT](ARRAYTOTEXT.md) | Converts an array to text with its own separators, which is useful for display. |
| [CONCATENATE](CONCATENATE.md) | Older function that accepts single cells only. CONCAT replaces it in Excel. |
| [JOIN](JOIN.md) | Joins an array with a delimiter in Google Sheets. |
| [TEXTJOIN](TEXTJOIN.md) | Joins values with a delimiter and can skip empty values. |
| [TEXTSPLIT](TEXTSPLIT.md) | Does the reverse: splits text into pieces. |

## Official Documentation

- [Microsoft Support: CONCAT function](https://support.microsoft.com/en-us/excel/functions/concat-function)
- [Google Docs Editors Help: CONCAT](https://support.google.com/docs/answer/3093592)
