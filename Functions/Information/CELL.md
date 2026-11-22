---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
purpose:
  - Type Checking
  - Workbook Information
use-case:
  - Blank Input Detection
  - Cell Location Audit
related:
  - COLUMN
  - INFO
  - ISBLANK
  - ISFORMULA
  - ISREF
  - ROW
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/cell-function
  - https://support.google.com/docs/answer/3267071
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - cell-information
  - excel
  - reference-info
  - sheets
---

# CELL

## Description

**CELL** returns one piece of information about a cell. You choose the detail with an `info_type` text value: its address, its row or column number, its contents, whether it is blank, text or a number, and in desktop Excel some formatting details such as number format, alignment and lock status.

Use CELL when a formula must react to the layout or state of a cell rather than its value. Typical jobs are flagging input cells that are still empty, recording where a value sits in an audit note, and reading the current value of a cell without linking to its formula. For a simple test of whether a cell is empty, ISBLANK is easier to read. CELL is the function to use when you need the row, column, address or cell type.

The reference argument is optional in Excel, but Microsoft recommends always including it. When it is omitted, Excel uses the currently selected cell at the time of calculation, so the result can change as someone clicks around the sheet. Google Sheets requires the reference. Some `info_type` values are not supported in Excel for the web, so check the Platform Differences section before you share a workbook with people who use the browser version.

## Syntax

```excel
=CELL(info_type, [reference])
```

<!-- Image 1: Syntax Anatomy. See Images/Information/CELL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `info_type` | Yes | A text value in double quotes that names the detail to return, such as `"row"`, `"col"`, `"address"`, `"contents"` or `"type"`. |
| `reference` | Excel: No, Sheets: Yes | The cell to inspect. If an Excel formula omits it, the currently selected cell is used. Always include it. |

Valid `info_type` values are `"address"`, `"col"`, `"color"`, `"contents"`, `"filename"`, `"format"`, `"parentheses"`, `"prefix"`, `"protect"`, `"row"`, `"type"` and `"width"` in Excel. Google Sheets documents `"address"`, `"col"`, `"color"`, `"contents"`, `"prefix"`, `"row"`, `"sheet"`, `"type"` and `"width"`.

### Return Value

The return type depends on `info_type`. `"address"` returns text, `"col"` and `"row"` return numbers, `"type"` returns one letter in text, and `"width"` returns a number in Google Sheets or an array of two items in Excel.

## Examples

### Example 1: Address of a Cell

```excel
=CELL("address", C5)
```

**Result:** `$C$5`

The address comes back as absolute text, with dollar signs, regardless of how the reference is written in the formula.

### Example 2: Row and Column Numbers

```excel
=CELL("row", C5) & "-" & CELL("col", C5)
```

**Result:** `5-3`

Row 5 and column 3 (column C) are joined into one text label. Each `info_type` gets its own call, so you can pick the parts you need.

### Example 3: Detecting an Empty Cell

```excel
=CELL("type", B2)
```

**Result:** `b` when B2 is empty, `l` when B2 holds text, and `v` when B2 holds a number or other value

The `"type"` value returns `"b"` for a blank cell, `"l"` for a label (plain text) and `"v"` for anything else. A cell that contains a formula returning a number is reported as `"v"`.

<!-- Image 2: Cell Type Results. See Images/Information/CELL.md -->

### Example 4: Turning Blank Cells Into a Prompt

```excel
=IF(CELL("type", B2)="b", "Enter a value", "Recorded")
```

**Result:** `Enter a value` when B2 is blank

The formula checks the type of B2 and returns a prompt only when the cell is empty.

### Example 5: Reading the Contents of a Cell

```excel
=CELL("contents", D2)
```

**Result:** `20` when D2 contains the formula `=B2*2` and B2 holds 10

The `"contents"` value returns the value in the upper-left cell of the reference, not the formula that produced it.

## Story Problems

### Problem 1: Missing Answers in a Survey

A customer survey stores one answer per row in column B.

| Question | Answer |
| --- | --- |
| Q1 | Yes |
| Q2 | |
| Q3 | 4 |

**Task:** Put a formula in C3 that shows `Missing` when B3 is empty and `Answered` otherwise.

**Solution:**

```excel
=IF(CELL("type", B3)="b", "Missing", "Answered")
```

**Answer:** `Missing`. Cell B3 is empty, so its type is `"b"`.

### Problem 2: Finding the Row of a Delayed Order

An order list has the order number in column A and its status in column B. Order 1002 is in row 3 and has the status Delayed.

| Order | Status |
| --- | --- |
| 1001 | Shipped |
| 1002 | Delayed |
| 1003 | Shipped |

**Task:** Put a formula in D1 that returns the row number of the cell B3, which holds the delayed order.

**Solution:**

```excel
=CELL("row", B3)
```

**Answer:** `3`. Row 3 is the third row of the sheet, which is where order 1002 sits.

## Use Cases

### Cell Location Audit

**Scenario:** An auditor wants each flagged input cell listed by address in a notes column, so reviewers can jump to it quickly.

```excel
=CELL("address", Inputs!C12)
```

<!-- Image 3: Address Result in the Formula Bar. See Images/Information/CELL.md -->

**Why It Works:** The reference points at the input cell, so the address text updates when rows are inserted above it.

### Blank Input Detection

**Scenario:** A pricing sheet needs a required quantity in column B before totals are calculated.

```excel
=IF(CELL("type", B2)="b", "Required", "OK")
```

**Why It Works:** The formula returns a warning only for empty cells. Pair it with conditional formatting to highlight the rows that still need input.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Wrong address or row | The reference argument is omitted in Excel, so the selected cell is used. | Always pass the cell to inspect. |
| Unexpected error | The `info_type` text is misspelled or not in the list. | Copy the value exactly and keep it in double quotes. |
| Empty text for `"filename"` | The workbook has not been saved, so there is no file path yet. | Save the workbook, then recalculate. |
| Unsupported result in Excel for the web | `"color"`, `"format"`, `"width"` and other formatting types are not supported in Excel for the web. | Use desktop Excel for these checks or use a different test. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in desktop Excel versions | The reference is optional. Excel for the web does not support `"color"`, `"filename"`, `"format"`, `"parentheses"`, `"prefix"`, `"protect"` or `"width"`. |
| Google Sheets | Available | The reference is required. Sheets adds `"sheet"` for the sheet name, and `"width"` is measured in characters. The documented list omits `"filename"`, `"format"`, `"parentheses"` and `"protect"`. |

## Tips and Best Practices

- Always pass the reference so the result does not depend on the current selection.
- Use `"type"` with IF to flag empty input cells before totals depend on them.
- Use `"address"` in audit notes, because the text follows the cell when rows move.
- Keep the `info_type` text in a labeled cell when many formulas share the same choice.
- Test workbooks on the platform where colleagues will open them, since Excel for the web and desktop Excel differ.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COLUMN](../Lookup%20%26%20Reference/COLUMN.md) | Returns only the column number of a reference. |
| [INFO](INFO.md) | Returns details about the operating environment rather than a cell. |
| [ISBLANK](ISBLANK.md) | Tests a single cell for emptiness and returns TRUE or FALSE. |
| [ISFORMULA](ISFORMULA.md) | Tests whether a cell contains a formula. |
| [ISREF](ISREF.md) | Tests whether a value is a valid reference. |
| [ROW](../Lookup%20%26%20Reference/ROW.md) | Returns only the row number of a reference. |

## Official Documentation

- [Microsoft Support: CELL function](https://support.microsoft.com/en-us/excel/functions/cell-function)
- [Google Docs Editors Help: CELL](https://support.google.com/docs/answer/3267071)
