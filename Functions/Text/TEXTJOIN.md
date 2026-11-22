---
domain: Spreadsheet Functions
category: Text
subcategory: Text Joining and Splitting
purpose:
  - Data Cleaning
  - Text Manipulation
use-case:
  - Address Lines Without Gaps
  - Key Built From Several Fields
  - Tag Lists From Columns
related:
  - CONCAT
  - FILTER
  - JOIN
  - SPLIT
  - TEXTSPLIT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/textjoin-function
  - https://support.google.com/docs/answer/7013992
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Concatenate With Delimiter
  - Join Text With Delimiter
tags:
  - concatenation
  - delimiters
  - excel
  - sheets
---

# TEXTJOIN

## Description

**TEXTJOIN** combines several text strings, or the cells in one or more ranges, into a single string. You choose the delimiter (the separator placed between items) and decide whether empty cells are skipped. Setting ignore_empty to TRUE keeps blank cells from leaving double separators in the result, which is the main difference from CONCAT and the ampersand.

Use TEXTJOIN to build lists such as a comma-separated set of tags from a row of cells, a single address line that skips blank fields, or a key that joins several columns for matching. Combine it with FILTER to join only the rows that meet a condition.

The result is one text string, up to 32,767 characters. The function accepts up to 252 text arguments, and each argument can be a single string or a range. Numbers are treated as text. An empty delimiter joins the items with nothing between them.

## Syntax

```excel
=TEXTJOIN(delimiter, ignore_empty, text1, [text2], ...)
```

<!-- Image 1: Syntax Anatomy. See Images/Text/TEXTJOIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `delimiter` | Yes | The separator placed between each item. It can be an empty string, text in double quotes, or a cell that holds text. |
| `ignore_empty` | Yes | TRUE skips empty cells. FALSE keeps them, so each empty cell adds an extra delimiter. |
| `text1` | Yes | The first item to join. It can be a text string, a number, a cell or a range. |
| `text2`, ... | No | Additional items to join. Up to 252 text arguments in total, counting `text1`. |

### Return Value

A single text string that contains every non-skipped item separated by the delimiter. The result is `#VALUE!` when the string would exceed 32,767 characters.

## Examples

The examples use a team roster in `A2:A6` (names: Ana, Ben, a blank cell, Cy and Dee) and roles in `B2:B6` (Lead, blank, Dev, QA and Ops).

### Example 1: Skip Blank Cells

```excel
=TEXTJOIN(", ",TRUE,A2:A6)
```

**Result:** `Ana, Ben, Cy, Dee`

With ignore_empty set to TRUE, the blank cell in row 4 adds nothing to the list.

### Example 2: Keep Blank Cells

```excel
=TEXTJOIN(", ",FALSE,A2:A6)
```

**Result:** `Ana, Ben, , Cy, Dee`

With ignore_empty set to FALSE, the blank cell contributes an empty item, so the list has two delimiters side by side.

### Example 3: Join Two Cells on One Line

```excel
=TEXTJOIN(" | ",TRUE,A2,B2)
```

**Result:** `Ana | Lead`

Each argument can be a single cell. The delimiter sits between the two items.

### Example 4: Join Only Matching Rows

```excel
=TEXTJOIN(", ",TRUE,FILTER(A2:A6,B2:B6<>""))
```

**Result:** `Ana, Cy, Dee`

FILTER returns the names in rows that have a role. The row with a blank name is included by FILTER, and ignore_empty removes it from the join.

### Example 5: Join With No Delimiter

```excel
=TEXTJOIN("",TRUE,A2:A3)
```

**Result:** `AnaBen`

An empty delimiter places nothing between the items, so the names run together.

### Example 6: Mix a Label and a Range

```excel
=TEXTJOIN(" ",TRUE,"Team:",A2:A3)
```

**Result:** `Team: Ana Ben`

A literal string and a range can appear in the same call. The label is the first item and the names follow it.

<!-- Image 2: Ignore Empty Versus Keep Empty. See Images/Text/TEXTJOIN.md -->

## Story Problems

### Problem 1: Bins With Stock for a Pick List

A warehouse sheet lists one bin code per product in `B2:B5`. Products that are out of stock have no bin code.

| Product | Bin |
| --- | --- |
| Bolt kit | A-12 |
| Hinge set | (blank) |
| Latch pack | C-03 |
| Pin set | B-07 |

**Task:** Build one line that lists every bin that has stock, separated by commas.

**Solution:**

```excel
=TEXTJOIN(", ",TRUE,B2:B5)
```

**Answer:** `A-12, C-03, B-07`. The blank bin for the hinge set does not add a delimiter.

### Problem 2: Names of Absent Students

A class list has students in `A2:A6` and attendance flags in `B2:B6`, where N means absent.

| Student | Present |
| --- | --- |
| Ines | Y |
| Jack | N |
| Kim | Y |
| Leo | N |
| Mia | Y |

**Task:** Return the names of absent students as one phrase, with and between the last two names.

**Solution:**

```excel
=TEXTJOIN(" and ",TRUE,FILTER(A2:A6,B2:B6="N"))
```

**Answer:** `Jack and Leo`. FILTER returns only the absent students, and TEXTJOIN joins them.

<!-- Image 3: Filtered Names in One Line. See Images/Text/TEXTJOIN.md -->

## Use Cases

### Address Lines Without Gaps

**Scenario:** A mailing list stores street, city and postal code in separate columns, and some customers have no second address line.

```excel
=TEXTJOIN(", ",TRUE,A2:C2)
```

**Why It Works:** Blank fields disappear, so a missing postal code does not leave a stray comma at the end of the address.

### Tag Lists From Columns

**Scenario:** A product sheet has up to five tag columns per row, and the storefront needs one comma-separated tag list.

```excel
=TEXTJOIN(", ",TRUE,D2:H2)
```

**Why It Works:** One range argument covers all five columns, and blank tags are skipped.

### Key Built From Several Fields

**Scenario:** Duplicate detection needs a single key built from the customer name, the postal code and the date of birth.

```excel
=TEXTJOIN("|",FALSE,LOWER(TRIM(A2)),TRIM(B2),TEXT(C2,"yyyy-mm-dd"))
```

**Why It Works:** Keeping empty items (FALSE) preserves the field positions, so two rows with a blank field do not produce the same key by accident. Lowercasing and trimming remove spacing and case differences before the key is compared.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The version does not include TEXTJOIN, such as Excel 2016. | Upgrade to a version that includes the function, or use CONCATENATE with explicit ampersands. |
| `#VALUE!` | The result exceeds 32,767 characters. | Join smaller ranges and combine the parts, or split the output into several cells. |
| Double delimiters | ignore_empty is FALSE and the range has blank cells. | Set ignore_empty to TRUE. |
| Missing items | The range is shorter than expected, or the filter excludes the row. | Check the range address and the condition used in FILTER. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows and Mac), Excel for the web, Excel 2024, Excel 2021 and Excel 2019 | Accepts ranges and arrays, and a range can supply the delimiter. Excel 2016 does not include the function. |
| Google Sheets | Available | Same arguments and results. An empty delimiter concatenates the items. |

## Tips and Best Practices

- Set ignore_empty to TRUE by default, and use FALSE only when the blank positions matter.
- Pass a range rather than a list of single cells, so the formula still works when rows are added.
- Use FILTER inside TEXTJOIN to join only the rows that meet a condition.
- Keep the delimiter inside double quotes unless it is stored in a cell that the team can edit.
- Trim the inputs first when values come from users or imports, so spacing does not create extra items.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CONCAT](../Text/CONCAT.md) | Joins values without a delimiter and without skipping blank cells. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the rows that meet a condition, which TEXTJOIN can then join. |
| [JOIN](../Text/JOIN.md) | Joins a list with a delimiter in Google Sheets, without an ignore_empty option. |
| [SPLIT](../Text/SPLIT.md) | Splits a text string into pieces, the reverse of joining. |
| [TEXTSPLIT](../Text/TEXTSPLIT.md) | Splits text into rows and columns, the Excel reverse of TEXTJOIN. |

## Official Documentation

- [Microsoft Support: TEXTJOIN function](https://support.microsoft.com/en-us/excel/functions/textjoin-function)
- [Google Docs Editors Help: TEXTJOIN](https://support.google.com/docs/answer/7013992)
