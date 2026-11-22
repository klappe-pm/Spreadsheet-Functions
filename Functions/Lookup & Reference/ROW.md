---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
purpose:
  - Array Shaping
  - Data Retrieval
use-case:
  - Alternating Row Shading
  - Numbered Row Labels
  - Sheet Row Reporting
related:
  - ADDRESS
  - ARRAYFORMULA
  - COLUMN
  - INDEX
  - MOD
  - ROWS
level: 1
source:
  - https://support.microsoft.com/en-us/excel/functions/row-function
  - https://support.google.com/docs/answer/3093316
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Row Number
  - Row Position
tags:
  - excel
  - reference
  - row-number
  - sheets
---

# ROW

## Description

**ROW** returns the row number of a cell or range. With no argument, it returns the row of the cell that contains the formula. With a cell reference, it returns that cell's row. Row numbers start at 1 for the first row of the sheet, so `ROW(A9)` returns 9.

ROW is most useful when a formula needs to know its own position. It can number rows, build alternating row patterns, or report where a value sits on the sheet. Because it returns a number and not the cell's contents, it is usually combined with another function such as INDEX, MOD or a counter that subtracts a header row.

When the argument is a range with several rows, ROW returns the first row number in a normal formula. Microsoft 365 returns one row number per row when the range is used as an array, which spills the list down the sheet. Google Sheets needs ARRAYFORMULA to return a list for a multi-row range. ROW cannot take a reference that covers more than one area, such as a selection made with Ctrl or a comma-separated union.

## Syntax

```excel
=ROW([reference])
```

<!-- Image 1: Row Number Anatomy. See Images/Lookup & Reference/ROW.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `reference` | No | The cell or range whose row number you want. If it is omitted, ROW uses the row of the cell that contains the formula. A single area is required. |

### Return Value

A row number, a whole number from 1 upward. With a single cell, the result is one number. With a multi-row range used as an array, the result is one row number for each row in the range. ROW returns an error when the reference covers more than one area.

## Examples

### Example 1: Row of the Formula Itself

```excel
=ROW()
```

**Result:** `7`

The formula is entered in cell C7, so ROW returns 7. Copying the formula to another row returns that row's number, because the formula always reads its own position.

### Example 2: Row of a Specific Cell

```excel
=ROW(A9)
```

**Result:** `9`

The argument is one cell in row 9, so the result is 9 no matter where the formula is placed.

### Example 3: Row Numbers for a Range

```excel
=ROW(B5:B20)
```

**Result:** `5` in a normal formula. In Microsoft 365, the result spills 16 values down the sheet, from 5 to 20.

The range starts in row 5 and ends in row 20. Google Sheets returns only the first value unless the formula is wrapped in ARRAYFORMULA, as shown in the Platform Differences table.

### Example 4: Counter That Ignores the Header

```excel
=ROW()-ROW($A$1)
```

**Result:** `3` when entered in cell A4

The header is in row 1, so subtracting that row turns the formula's own row into a count. Entered in A2, the same formula returns 1. Copied down, it numbers the rows 1, 2, 3 and so on.

<!-- Image 2: Numbered Row Labels. See Images/Lookup & Reference/ROW.md -->

### Example 5: Odd and Even Rows

```excel
=MOD(ROW(), 2)
```

**Result:** `0` when entered in cell A8, and `1` when entered in cell A9

MOD returns the remainder after division by 2. Even row numbers return 0 and odd row numbers return 1. This is the basis of the alternating shading rule in the Use Cases section.

## Story Problems

### Problem 1: Reporting the Sheet Row of an Overdue Invoice

A collections clerk keeps a list of customers in `A1:B6`. Row 1 holds the headings. The clerk wants a formula that reports the sheet row of the first overdue account, so the account can be found quickly.

| Customer | Status |
| --- | --- |
| Acme | Paid |
| Birch | Open |
| Cedar | Paid |
| Dune | Overdue |
| Eden | Overdue |

**Task:** Return the sheet row number of the first cell in `B1:B6` that says Overdue, counting from the top of the sheet.

**Solution:**

```excel
=MATCH("Overdue", B1:B6, 0)+ROW(B1)-1
```

**Answer:** `5`. MATCH returns position 5 within `B1:B6`, and adding ROW(B1) minus 1 converts that position to the sheet row. Dune is in row 5.

### Problem 2: Numbering Eight Jobs

A print shop lists eight jobs in `A2:A9`, with a heading in row 1. The shop needs a job number in column B that starts at 1 for the first job and does not depend on typing numbers by hand.

**Task:** Enter one formula in `B2` that numbers each job, then copy it down to `B9`.

**Solution:**

```excel
=ROW()-ROW($A$1)
```

**Answer:** `8` in `B9`, because row 9 minus row 1 is 8. The first job in `B2` is numbered 1.

## Use Cases

### Numbered Row Labels

**Scenario:** A table of training sessions starts below a title block. Each session needs a visible number, and the numbers must stay correct if rows are added or moved above the table.

```excel
=ROW()-ROW($A$1)
```

**Why It Works:** The formula compares its own row with the row of the header cell. If rows are inserted above the table, both references move, so the difference, and therefore the number, stays the same. A typed number does not move in this way.

### Alternating Row Shading

**Scenario:** A printed price list is easier to read when every other row has a light background. The shading must apply to the whole list, including rows added later.

```excel
=MOD(ROW(), 2)=0
```

**Why It Works:** Enter this as a conditional formatting rule for the list range, such as `A2:F200`, with a light fill. ROW returns the row of each cell being checked, and MOD returns 0 for even rows, so the fill appears on every second row.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Only one number appears | A multi-row range is used in a normal formula in Google Sheets. | Wrap the formula in ARRAYFORMULA, for example `=ARRAYFORMULA(ROW(B5:B20))`. |
| Numbers are one too high or low | The counter does not subtract the header row, or it subtracts the wrong row. | Use `=ROW()-ROW($A$1)` or the row of the first data cell minus 1. |
| Error | The reference covers more than one area, such as a selection made with Ctrl. | Use a single contiguous range. |
| Wrong count after edits | A typed number was used in place of ROW, so it does not move when rows change. | Use ROW to generate the number. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | A range argument returns one row number per row when entered as a vertical array. Microsoft 365 spills these automatically. ROW does not accept multi-area references. |
| Google Sheets | Available | A multi-row range returns only the first row number unless the formula is wrapped in ARRAYFORMULA. Documents the same default behavior: with no argument, the row of the formula cell. |

## Tips and Best Practices

- Subtract the header row from ROW() to create a counter that survives row insertions.
- Use a single-row or single-column range when you need one predictable row number.
- Combine ROW with MOD to build patterns such as alternating shading, every third row or repeating schedules.
- Use ROWS when you need the count of rows in a range rather than the position of a row.
- In Google Sheets, wrap any multi-row ROW formula in ARRAYFORMULA so the result covers the whole range.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COLUMN](COLUMN.md) | The matching function that returns a column number. |
| [ROWS](ROWS.md) | Returns how many rows a range contains, not the row number of a cell. |
| [ADDRESS](ADDRESS.md) | Builds a cell address from a row and column number. |
| [INDEX](INDEX.md) | Returns a value at a row position inside a range, often a row found with ROW or MATCH. |
| [MOD](../Math%20%26%20Trig/MOD.md) | Gives the remainder that creates alternating row patterns. |
| [ARRAYFORMULA](../Google-specific/ARRAYFORMULA.md) | Lets a multi-row ROW formula return a full list in Google Sheets. |

## Official Documentation

- [Microsoft Support: ROW function](https://support.microsoft.com/en-us/excel/functions/row-function)
- [Google Docs Editors Help: ROW](https://support.google.com/docs/answer/3093316)
