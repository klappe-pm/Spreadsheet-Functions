---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
purpose:
  - Counting
  - Data Validation
use-case:
  - Attendance Sign In Sheet
  - Dynamic Range Sizing
  - Survey Response Tracking
related:
  - COUNT
  - COUNTBLANK
  - COUNTIF
  - COUNTIFS
  - LEN
  - ROWS
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/counta-function
  - https://support.google.com/docs/answer/3093991
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Count Entries
  - Count Non Empty
tags:
  - counting
  - data-validation
  - excel
  - sheets
  - text
---

# COUNTA

## Description

**COUNTA** returns how many cells in a range or list of arguments are not empty. It counts every kind of entry: text, numbers, dates, logical values, error values and formulas that return an empty string. Only cells that have never held a value, or that were cleared, are skipped.

COUNTA answers the question "how many cells have something in them?" It is the right choice for tracking form submissions, sign-in sheets and data entry progress. Use COUNT when you need only the numeric entries.

Formulas that return an empty string need care. A cell that shows nothing but contains `=IF(FALSE, "Yes", "")` holds a value as far as COUNTA is concerned, so it is counted. This surprises many people, and it is the most common cause of a count that is higher than the number of visible entries. Use COUNTIF with an exact text criterion, or a LEN test, when only visible entries should count.

## Syntax

```excel
=COUNTA(value1, [value2], ...)
```

<!-- Image 1: Filled, Empty and Formula Cells. See Images/Statistical/COUNTA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value1` | Yes | The first item, cell reference or range to check for entries. |
| `value2, ...` | No | Additional items, cell references or ranges. Excel accepts up to 255 arguments in total after `value1`. Google Sheets documents a limit of 30 and supports more in practice. |

### Return Value

A whole number: the count of cells that are not empty. COUNTA returns 0 when every cell in the range is empty, and it does not return an error for valid references, even when the range contains error values.

## Examples

### Example 1: Count Names in a List

Cells `A2:A11` hold Ruth, Omar, a blank cell, Lee, Priya, a blank cell, Sam, Yuki, Diego and Nina.

```excel
=COUNTA(A2:A11)
```

**Result:** `8`

Eight cells hold names. The two blank cells are skipped.

### Example 2: Every Type Counts

Cells `A1:A5` hold Refund, 75, TRUE, the error #N/A and the date 3/4/2026.

```excel
=COUNTA(A1:A5)
```

**Result:** `5`

Text, a number, a logical value, an error and a date all count as entries.

### Example 3: Formula Results That Look Blank

Cell `A1` holds Value, cell `A2` holds `=IF(FALSE, "Yes", "")`, and cell `A3` is empty.

```excel
=COUNTA(A1:A3)
```

**Result:** `2`

Cell `A2` looks empty but contains a formula result, so COUNTA counts it. Only `A3` is skipped.

<!-- Image 2: Empty String Results Counted. See Images/Statistical/COUNTA.md -->

### Example 4: Compare COUNTA With COUNT

Cells `A1:A5` hold Sales, 1000, Marketing, 2000 and Support.

```excel
=COUNTA(A1:A5)
```

**Result:** `5`

```excel
=COUNT(A1:A5)
```

**Result:** `2`

COUNTA counts all five entries. COUNT counts only the two numbers.

### Example 5: Zeros Are Entries

Cells `A1:A5` hold 0, 0, a blank cell, 0 and 0.

```excel
=COUNTA(A1:A5)
```

**Result:** `4`

A zero is a value, so the four zeros count. Only the blank cell is skipped. Check whether zeros mean missing data in your sheet before you rely on this count.

### Example 6: Completion Rate

Cells `B2:B101` form a list of 100 expected entries, and 75 of them are filled.

```excel
=COUNTA(B2:B101)/ROWS(B2:B101)
```

**Result:** `0.75` (display as 75 percent)

Dividing by the number of rows gives the share of expected entries that have been filled.

## Story Problems

### Problem 1: Team Waiver Sign-Off

A coach keeps a waiver status for each team member in `B2:B6`. One member has not been recorded yet and leaves the cell blank.

| Member | Waiver Status |
| --- | --- |
| Ana | Yes |
| Ben | (blank) |
| Cy | Yes |
| Dee | No |
| Eli | Yes |

**Task:** Count how many waiver entries have been recorded.

**Solution:**

```excel
=COUNTA(B2:B6)
```

**Answer:** `4`. The blank cell is skipped. The entries Yes, Yes, No and Yes count, even though one of them is No.

### Problem 2: Checklist With Formula Results

A checklist in `B2:B5` uses a formula that shows Complete when all items are done and an empty string otherwise. Rows 2 and 4 are complete. Rows 3 and 5 return an empty string.

**Task:** Count the completed checklists.

**Solution:**

```excel
=COUNTIF(B2:B5, "Complete")
```

**Answer:** `2`. COUNTA would return 4, because it counts the two empty-string results as entries. COUNTIF counts only the rows that show Complete.

## Use Cases

### Survey Response Tracking

**Scenario:** A survey administrator monitors response rates while an online form fills a sheet. The first column holds the respondent email, which is required.

```excel
=COUNTA(A2:A1000)
```

**Why It Works:** Each submission adds an email, so COUNTA on that column gives the number of responses. Comparing other question columns with this total shows which questions are being skipped.

### Attendance Sign In Sheet

**Scenario:** A class leader records attendance by typing a mark in a column for each session. The sheet holds the roll in column A.

```excel
=COUNTA(Session1) - 1
```

**Why It Works:** The header row is not an attendee, so one is subtracted. Blank cells are skipped, so the result is the number of students who were marked present.

### Dynamic Range Sizing

**Scenario:** A report needs a chart range that grows as rows are added to a list.

```excel
=OFFSET(A1, 0, 0, COUNTA(A:A), 1)
```

**Why It Works:** COUNTA sets the height of the range. The count includes the header row, so the chart range starts with the header and expands as entries are added.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Count is higher than expected | Formulas return an empty string and are counted. | Use COUNTIF with an exact criterion, or count with a LEN test. |
| Count is higher than expected | Cells hold spaces or other hidden characters. | Clean the data with `TRIM` and `CLEAN`, then count again. |
| Count includes the header | The range starts at row 1. | Start the range at row 2, or subtract 1. |
| Result is 0 unexpectedly | The range or sheet reference is wrong. | Check the references, especially those that point to another sheet. |
| Result differs from COUNT | COUNT counts only numbers, COUNTA counts every entry. | Choose the function that matches what you want to count. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions | Counts text, numbers, errors and empty-string formula results. Accepts up to 255 arguments after `value1`. |
| Google Sheets | Available | The help page documents a limit of 30 arguments but notes that Sheets supports more. It counts zero-length strings as values. |

## Tips and Best Practices

- Start ranges below the header row, such as `A2:A1000`, or subtract 1 for the header.
- Use COUNTIF for counts that depend on what a formula returns, because COUNTA counts empty-string results.
- Use LEN in an array formula when only cells with visible characters should count.
- Use COUNTA with COUNT to see how many entries in a column are not numbers: `=COUNTA(A1:A100)-COUNT(A1:A100)`.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNT](COUNT.md) | Counts numeric entries only. |
| [COUNTBLANK](COUNTBLANK.md) | Counts the empty cells, the complement of COUNTA for a range. |
| [COUNTIF](COUNTIF.md) | Counts cells that match a condition, useful when formula results must be excluded. |
| [COUNTIFS](COUNTIFS.md) | Counts cells that match several conditions at once. |
| [LEN](../Text/LEN.md) | Returns the number of characters, useful for separating visible entries from empty-string results. |
| [ROWS](../Lookup%20%26%20Reference/ROWS.md) | Returns the number of rows, the denominator for a completion rate. |

## Official Documentation

- [Microsoft Support: COUNTA function](https://support.microsoft.com/en-us/excel/functions/counta-function)
- [Google Docs Editors Help: COUNTA](https://support.google.com/docs/answer/3093991)
