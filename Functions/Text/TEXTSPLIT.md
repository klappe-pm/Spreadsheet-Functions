---
domain: Spreadsheet Functions
category: Text
subcategory: Text Joining and Splitting
purpose:
  - Array Shaping
  - Text Manipulation
use-case:
  - Name Parts Into Columns
  - Pasted Table Text
  - Tag List To Rows
related:
  - SPLIT
  - TEXTAFTER
  - TEXTBEFORE
  - TEXTJOIN
  - TRIM
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/textsplit-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Split Text Into Columns
  - Split Text Into Rows
tags:
  - dynamic-array
  - excel
  - splitting
---

# TEXTSPLIT

## Description

**TEXTSPLIT** splits a text string into an array that spills into neighboring cells. A column delimiter splits the text across columns, and an optional row delimiter splits it down rows. One formula can turn a single cell of delimited text into a small table.

Use TEXTSPLIT when a cell holds delimited data, such as a pasted block of comma-separated values, a list of tags, or the parts of a name. Because the output spills, the result updates when the source cell changes, and no helper columns are needed. For a single split point that returns one piece at a time, use TEXTBEFORE or TEXTAFTER.

Matching is case-sensitive by default. Set match_mode to 1 to ignore case. When rows end up with different numbers of items, the empty positions are filled with pad_with, which defaults to `#N/A`, so supply a value to keep the table clean.

## Syntax

```excel
=TEXTSPLIT(text, col_delimiter, [row_delimiter], [ignore_empty], [match_mode], [pad_with])
```

<!-- Image 1: Syntax Anatomy. See Images/Text/TEXTSPLIT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `text` | Yes | The text to split. |
| `col_delimiter` | Yes | The character or string that marks where to split across columns. Use an array constant such as `{",",";"}` for more than one delimiter. |
| `row_delimiter` | No | The character or string that marks where to split down rows. Leave it empty to keep all items in one row. |
| `ignore_empty` | No | TRUE skips consecutive delimiters that would leave an empty item. FALSE keeps them as empty cells. The default is FALSE. |
| `match_mode` | No | 0 matches case-sensitively and is the default. 1 ignores case. |
| `pad_with` | No | The value used to fill gaps when rows have different lengths. The default is `#N/A`. |

### Return Value

An array that spills across columns, down rows, or both. The array is sized by the number of pieces, and any empty positions show `pad_with`. When the spill range is blocked by other content, the result shows `#SPILL!`.

## Examples

### Example 1: Split a List Across Columns

```excel
=TEXTSPLIT("North,South,East",",")
```

**Result:** three cells in a row: `North`, `South`, `East`

With no row delimiter, every piece goes into one row, one piece per column.

### Example 2: Split Rows and Columns

```excel
=TEXTSPLIT("red,small;blue,large",",",";")
```

**Result:** a 2 by 2 table: `red` and `small` on the first row, `blue` and `large` on the second

The semicolon starts a new row, and the comma starts a new column.

### Example 3: Split Only Down a Column

```excel
=TEXTSPLIT("alpha;beta;gamma",,";")
```

**Result:** three cells down one column: `alpha`, `beta`, `gamma`

Leaving the column delimiter empty puts each piece on its own row.

### Example 4: Skip Empty Pieces

```excel
=TEXTSPLIT("a,,b",",",,TRUE)
```

**Result:** two cells in a row: `a`, `b`

The double comma would normally create an empty middle cell. With ignore_empty set to TRUE, the empty piece is dropped. The default FALSE keeps it as a blank cell.

### Example 5: Pad Uneven Rows

```excel
=TEXTSPLIT("1,2,3;4,5",",",";",FALSE,0,0)
```

**Result:** a 2 by 3 table: `1`, `2`, `3` on the first row, and `4`, `5`, `0` on the second

The second row has only two items, so pad_with fills the last position with 0.

## Story Problems

### Problem 1: Scores From a Pasted Block

Cell `A2` holds `Ava,42;Ben,37;Cora,58`, copied from a web page. Each record is a name and a score.

**Task:** Spread the block into a table with one row per record and one column for each field.

**Solution:**

```excel
=TEXTSPLIT(A2,",",";")
```

**Answer:** a 3 by 2 table. Row 1 is Ava and 42, row 2 is Ben and 37, and row 3 is Cora and 58. The scores are text, so convert them with VALUE before adding them.

### Problem 2: Survey Answers With Uneven Rows

Cell `A2` holds the answers from two survey rows: `yes,no,yes;no,yes`. The second row is one answer short.

**Task:** Build a table with three columns, and mark the missing answer with a hyphen.

**Solution:**

```excel
=TEXTSPLIT(A2,",",";",FALSE,0,"-")
```

**Answer:** a 2 by 3 table. Row 1 is yes, no and yes. Row 2 is no, yes and a hyphen in the last column.

<!-- Image 2: Row and Column Delimiters. See Images/Text/TEXTSPLIT.md -->

## Use Cases

### Name Parts Into Columns

**Scenario:** A customer list stores full names in one column, and the mailing merge needs the first and last names in separate cells.

```excel
=TEXTSPLIT(A2," ")
```

**Why It Works:** Each space starts a new column, so a two-part name fills two cells. Names with a middle name spill into a third cell, so check the widest row before filling the report.

### Pasted Table Text

**Scenario:** Someone pastes a table as plain text in a single cell, with tabs between columns and line breaks between rows.

```excel
=TEXTSPLIT(A2,CHAR(9),CHAR(10))
```

**Why It Works:** CHAR(9) is the tab character that separates columns, and CHAR(10) is the line break that separates rows. The spilled result rebuilds the table in the sheet.

### Tag List to Rows

**Scenario:** A product record holds tags such as `red, small, cotton` in one cell, and the team wants each tag on its own row for filtering.

```excel
=TEXTSPLIT(A2,,", ",TRUE)
```

**Why It Works:** The comma and space form the row delimiter, so each tag drops onto its own row. ignore_empty removes any blank tags left by a trailing comma.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` in part of the result | Rows have different lengths, and pad_with is not set. | Supply a pad_with value, or wrap the formula in IFNA. |
| `#SPILL!` | Cells in the spill range are not empty. | Clear the blocking cells, or move the formula to an empty area. |
| Blank cells in the result | ignore_empty is FALSE and the text has consecutive delimiters. | Set ignore_empty to TRUE. |
| No split happens | The delimiter does not appear in the text, so the whole text stays in one cell. | Check the delimiter, and use match_mode 1 if the case differs. |
| Numbers fail in arithmetic | Split pieces are text. | Convert the pieces with VALUE before calculating. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web), Excel 2024 (Windows and Mac) | Spills across columns and rows. Excel 2021, Excel 2019 and Excel 2016 do not include the function. |
| Google Sheets | Not available | The closest alternative is SPLIT, which splits on one delimiter per call and returns a row of pieces. |

## Tips and Best Practices

- Set pad_with whenever the rows may differ in length, so the table stays readable.
- Use an array constant such as `{",",";"}` when one split point is not enough.
- Keep the spill area clear, and leave room below and to the right of the formula.
- Use TRIM on the source first when the text came from users or a web page.
- Use TEXTJOIN to reverse the split when you need to rebuild the delimited text.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SPLIT](../Text/SPLIT.md) | Google Sheets function that splits on one delimiter and returns a row. |
| [TEXTAFTER](../Text/TEXTAFTER.md) | Returns the text after one delimiter occurrence, for a single piece. |
| [TEXTBEFORE](../Text/TEXTBEFORE.md) | Returns the text before one delimiter occurrence, for a single piece. |
| [TEXTJOIN](../Text/TEXTJOIN.md) | Joins pieces back into one string with a delimiter. |
| [TRIM](../Text/TRIM.md) | Removes extra spaces from pieces before they are used. |

## Official Documentation

- [Microsoft Support: TEXTSPLIT function](https://support.microsoft.com/en-us/excel/functions/textsplit-function)
