---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
purpose:
  - Conditional Logic
  - Counting
use-case:
  - Overdue Invoice Counts
  - Regional Order Counts
  - Shift Attendance Tracking
related:
  - AVERAGEIF
  - COUNT
  - COUNTA
  - COUNTBLANK
  - COUNTIFS
  - COUNTUNIQUE
  - SUMIF
  - SUMPRODUCT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/get-started/use-the-countif-function-in-microsoft-excel
  - https://support.google.com/docs/answer/3093480
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Conditional Count
  - Count With Criteria
tags:
  - counting
  - criteria
  - excel
  - sheets
  - wildcards
---

# COUNTIF

## Description

**COUNTIF** counts the cells in a range that meet one condition. Use it to answer questions such as "How many orders came from the East region?" or "How many invoices are more than 30 days late?" The condition, called the criteria, can be an exact value, a comparison such as `">50"`, a cell reference, or a text pattern that uses wildcards.

COUNTIF accepts only one condition. When every condition must be true at the same time, use COUNTIFS. When you need the total of matching values rather than a count, use SUMIF.

Criteria are not case-sensitive in Excel or Google Sheets, so `"apples"` and `"APPLES"` match the same cells. Text criteria can include the wildcards `*` (any sequence of characters) and `?` (exactly one character). Wildcards only apply to text, so a numeric comparison such as `">10"` ignores them.

Excel and Google Sheets accept the same criteria syntax for normal use. Google's help page describes the criterion as a string when the range holds text, and as a number, numeric string, or number with an operator when the range holds numbers.

## Syntax

```excel
=COUNTIF(range, criteria)
```

<!-- Image 1: COUNTIF Syntax Anatomy. See Images/Statistical/COUNTIF.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `range` | Yes | The cells to test. Blank cells and text values are ignored when the criteria is numeric. Use a contiguous range such as `A2:A100`. |
| `criteria` | Yes | The condition a cell must meet. It can be a number, text, an expression such as `">50"`, a cell reference, or a text pattern with wildcards. |

### Return Value

A whole number: the count of cells in `range` that meet `criteria`. It returns 0 when no cell matches. It returns `#VALUE!` when the range refers to a closed workbook.

## Examples

All examples use this order list in `A1:C8`, with headers in row 1.

| Region | Units | Status |
| --- | --- | --- |
| East | 12 | Open |
| West | 45 | Closed |
| East | 30 | Closed |
| North | 8 | Open |
| West | 60 | Open |
| East | 22 | Closed |
| South | 15 | Open |

### Example 1: Exact Text Match

```excel
=COUNTIF(A2:A8, "East")
```

**Result:** `3`

Rows 2, 4 and 7 contain East. The match ignores capitalization, so `"east"` would return the same count.

### Example 2: Numeric Comparison

```excel
=COUNTIF(B2:B8, ">20")
```

**Result:** `4`

The units 45, 30, 60 and 22 are greater than 20. The operator and the number sit together inside the quotation marks.

### Example 3: Cell Reference as the Threshold

Cell `E2` holds `30`.

```excel
=COUNTIF(B2:B8, ">="&E2)
```

**Result:** `3`

The `&` operator joins the comparison symbol to the value in `E2`, so the formula reads `">=30"`. The units 45, 30 and 60 qualify. Change `E2` and the count updates.

<!-- Image 2: Wildcard Patterns in COUNTIF Criteria. See Images/Statistical/COUNTIF.md -->

### Example 4: Not Equal To

```excel
=COUNTIF(A2:A8, "<>East")
```

**Result:** `4`

The `<>` operator counts every cell that does not equal East. Here that is the rows for West (2), North (1) and South (1).

### Example 5: Wildcard That Ends With a Pattern

```excel
=COUNTIF(A2:A8, "*th")
```

**Result:** `2`

The asterisk matches any characters before `th`. North and South qualify.

### Example 6: Wildcard for an Exact Length

```excel
=COUNTIF(A2:A8, "?????")
```

**Result:** `2`

Each question mark matches exactly one character, so the pattern finds five-letter values. North and South have five letters; East and West have four.

## Story Problems

### Problem 1: Overdue Invoices

A small contractor lists invoice days past due in `A1:B9`.

| Invoice | Days Late |
| --- | --- |
| INV-101 | 0 |
| INV-102 | 45 |
| INV-103 | 12 |
| INV-104 | 31 |
| INV-105 | 90 |
| INV-106 | 5 |
| INV-107 | 60 |
| INV-108 | 30 |

**Task:** Count the invoices that are more than 30 days late.

**Solution:**

```excel
=COUNTIF(B2:B9, ">30")
```

**Answer:** `4`. Invoices 102 (45), 104 (31), 105 (90) and 107 (60) qualify. Invoice 108 is exactly 30, so it does not.

<!-- Image 3: Overdue Invoice Result. See Images/Statistical/COUNTIF.md -->

### Problem 2: Shift Absence Log

A shift supervisor records one status per employee in `A1:B9`.

| Employee | Status |
| --- | --- |
| Ruiz | Present |
| Chen | Absent (sick) |
| Okafor | Absent (vacation) |
| Patel | Present |
| Lindqvist | Late |
| Moreau | Absent (sick) |
| Nakamura | Present |
| Reyes | Absent (training) |

**Task:** Count every absence, whatever the reason.

**Solution:**

```excel
=COUNTIF(B2:B9, "Absent*")
```

**Answer:** `4`. The entries for Chen, Okafor, Moreau and Reyes start with "Absent", and the wildcard matches each reason.

## Use Cases

### Flag Repeated Sign-Ups

**Scenario:** An event team collects sign-up emails in column A and needs to find addresses that appear more than once.

```excel
=COUNTIF($A$2:$A$500, A2)>1
```

**Why It Works:** The formula compares each email with the full list and returns `TRUE` for repeats. Anchor the range with `$` signs so the reference stays fixed when you copy the formula down. Trim stray spaces first, because `"ana@example.com "` and `"ana@example.com"` do not match.

### Count Orders for a Selected Region

**Scenario:** A regional manager picks a region from a drop-down in `H2`, and the dashboard shows that region's order count.

```excel
=COUNTIF(Orders[Region], H2)
```

**Why It Works:** The criteria is a cell reference, so the result changes when the drop-down changes. Using a table column such as `Orders[Region]` keeps the range sized to the data as rows are added.

### Count Scores at or Above a Pass Mark

**Scenario:** A teacher keeps the pass mark in cell `F1` and wants the number of students who reach it.

```excel
=COUNTIF(C2:C40, ">="&F1)
```

**Why It Works:** Joining the operator to the cell keeps the threshold editable. The formula works for numbers only; the wildcard pattern rules do not apply.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Count of `0` or an unexpected total | The comparison operator is typed without quotation marks, as in `>50`. | Put the whole criteria in quotes: `">50"`. |
| Count lower than expected | Cells contain leading or trailing spaces. | Clean the data with `TRIM`, or wrap the criteria cell in `TRIM` as in `=COUNTIF(A2:A100, TRIM(E1))`. |
| Incorrect count for long text | The text in the range or the criteria is longer than 255 characters. | Shorten the text, or join it with `&` in smaller parts. |
| Wildcard seems to do nothing | The wildcard is used with a numeric comparison. | Wildcards only match text. Use operators such as `">10"` for numbers. |
| Count includes more rows than intended | `*` or `?` in the criteria matches more than expected. | Escape the literal character with a tilde: `"~*"` or `"~?"`. |
| `#VALUE!` | The range refers to a workbook that is closed. | Open the source workbook, then recalculate. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available | Text criteria are not case-sensitive and support `*` and `?`. COUNTIF cannot count by cell color; that needs a VBA user-defined function. |
| Google Sheets | Available | Same criteria syntax. Accepts a numeric string or a number with an operator when the range holds numbers. |

## Tips and Best Practices

- Put the operator and the value together inside quotation marks, and join a cell reference with `&`.
- Use COUNTIFS when a second condition must also be true, and add separate COUNTIF results when either condition may be true.
- Use `"<>"` to count non-blank cells and `""` to count blank cells, and say which one you mean in the sheet.
- Use `~` before a wildcard to match a literal asterisk or question mark.
- Keep criteria in cells rather than in the formula so people can change the question without editing it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNTIFS](COUNTIFS.md) | Counts rows that meet several conditions at once. |
| [SUMIF](../Math%20%26%20Trig/SUMIF.md) | Adds the values that meet one condition instead of counting them. |
| [AVERAGEIF](AVERAGEIF.md) | Averages the values that meet one condition. |
| [COUNT](COUNT.md) | Counts numeric values with no condition. |
| [COUNTA](COUNTA.md) | Counts non-empty cells with no condition. |
| [COUNTUNIQUE](../Math%20%26%20Trig/COUNTUNIQUE.md) | Counts distinct values in a range. |

## Official Documentation

- [Microsoft Support: Use the COUNTIF function in Microsoft Excel](https://support.microsoft.com/en-us/excel/get-started/use-the-countif-function-in-microsoft-excel)
- [Google Docs Editors Help: COUNTIF](https://support.google.com/docs/answer/3093480)
