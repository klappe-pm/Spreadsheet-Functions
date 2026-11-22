---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
purpose:
  - Type Checking
  - Workbook Information
use-case:
  - Formula Audit Column
  - Hard Coded Total Detection
  - Named Input Check
related:
  - CELL
  - FORMULATEXT
  - ISBLANK
  - ISNUMBER
  - ISREF
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/isformula-function
  - https://support.google.com/docs/answer/6270316
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - excel
  - formula-audit
  - information
  - sheets
---

# ISFORMULA

## Description

**ISFORMULA** returns TRUE when the referenced cell contains a formula and FALSE when it holds a constant such as a number, a date or a piece of text. It lets a workbook check its own structure, for example to find a total that someone typed over with a fixed number.

A formula still counts as a formula when it returns an error. The formula `=1/0` shows `#DIV/0!`, and ISFORMULA on that cell still returns TRUE. Use ISERROR or ISERR to test the result instead.

Use ISFORMULA in audit columns, in checks that run before a report is sent, and in conditional formatting that highlights typed-over cells. For the text of a formula, use FORMULATEXT.

## Syntax

```excel
=ISFORMULA(reference)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/ISFORMULA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `reference` | Yes | A reference to the cell to test. It can be a cell reference, a name that refers to a cell, or a formula. A name that does not refer to a cell returns `#VALUE!`. |

### Return Value

TRUE when the referenced cell contains a formula, including a formula that returns an error. FALSE when the cell contains a constant or is empty. A non-reference argument that is not valid, such as a name that refers to a number instead of a cell, returns `#VALUE!`.

## Examples

### Example 1: Checking a Formula Cell

Cell A2 holds the formula `=B2*C2`.

```excel
=ISFORMULA(A2)
```

**Result:** `TRUE`

The cell contains a formula, so the function returns TRUE.

### Example 2: Checking a Typed Value

Cell A3 holds the number `500`, typed by hand.

```excel
=ISFORMULA(A3)
```

**Result:** `FALSE`

The cell contains a constant, so the function returns FALSE.

### Example 3: A Formula That Returns an Error

Cell A4 holds `=1/0`, which displays `#DIV/0!`.

```excel
=ISFORMULA(A4)
```

**Result:** `TRUE`

The error is the result of a formula, so the cell still counts as a formula.

### Example 4: Labeling Cells in an Audit Column

Cell B2 holds the number `42`, typed by hand.

```excel
=IF(ISFORMULA(B2),"Formula","Typed value")
```

**Result:** `Typed value`

The IF function turns the TRUE or FALSE result into a label that reviewers can read.

<!-- Image 2: Formula Audit Column. See Images/Information/ISFORMULA.md -->

## Story Problems

### Problem 1: Finding Typed-Over Totals

A monthly budget sheet has four totals in `B2:B5`. Two rows are formulas, and two were typed over with fixed numbers during an update. The controller wants the count of typed totals before the file is sent.

| Line | Total |
| --- | --- |
| Rent | =SUM(B6:B7) |
| Utilities | 4500 |
| Software | =B9*12 |
| Travel | 1200 |

**Task:** Place `=ISFORMULA(B2)` in `C2`, fill it down to `C5`, then count the FALSE results.

**Solution:**

```excel
=ISFORMULA(B2)
=COUNTIF(C2:C5,FALSE)
```

**Answer:** `2`. The Utilities and Travel totals hold typed numbers, so ISFORMULA returns FALSE for them.

### Problem 2: Checking a Named Input

A forecast uses a named cell called `TaxRate` that points to `Assumptions!B2`. The model should take its tax rate from a typed input, not from a calculation.

| Name | Refers To | Content |
| --- | --- | --- |
| TaxRate | Assumptions!B2 | 0.08 (typed) |

**Task:** Test whether `TaxRate` contains a formula.

**Solution:**

```excel
=ISFORMULA(TaxRate)
```

**Answer:** `FALSE`. The named cell holds the typed value 0.08, so the input is a constant.

## Use Cases

### Formula Audit Column

**Scenario:** A finance team reviews a large workbook and wants to see at a glance which cells in a calculation column are formulas.

```excel
=IF(ISFORMULA(D2),"","Check this cell")
```

**Why It Works:** The formula returns a blank string for formula cells and a warning for typed cells. Filter the column for warnings to find every cell that needs review.

### Hard Coded Total Detection

**Scenario:** A report total should always come from a SUM formula, so any typed number is a risk.

```excel
=IF(ISFORMULA(B12),"OK","Typed total")
```

**Why It Works:** Place the check beside the total. If someone types over the formula, the label changes and the reviewer sees it before the report goes out.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The argument is a name or value that does not refer to a cell. | Pass a cell reference or a name that refers to a cell. |
| `TRUE` for a cell that shows an error | A formula that returns an error still counts as a formula. | Test the result with ISERROR if the error matters. |
| `FALSE` for a formula in a range | In Google Sheets, a range argument checks only its first cell. | Test each cell separately, as in Problem 1. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft 365, Microsoft 365 for Mac, Excel for the web, Excel 2024, Excel 2021, Excel 2019 and Excel 2016. | Accepts a cell reference, a name or a formula as its argument. |
| Google Sheets | Available | Accepts a cell, a named cell or a range. For a range, only the first cell is checked. |

## Tips and Best Practices

- Pair ISFORMULA with FORMULATEXT to show the formula alongside the test result.
- Use a reference to a single cell in Google Sheets so the result is clear.
- Build audit checks on a separate sheet so the checks do not disturb the report layout.
- Add conditional formatting based on ISFORMULA to highlight typed values in calculation columns.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FORMULATEXT](../Lookup%20%26%20Reference/FORMULATEXT.md) | Returns the formula text, so reviewers can read what a cell calculates. |
| [ISREF](ISREF.md) | Tests whether a value is a reference, which ISFORMULA needs as its argument. |
| [ISBLANK](ISBLANK.md) | Tests for an empty cell rather than a formula. |
| [ISNUMBER](ISNUMBER.md) | Tests the value returned by a cell instead of whether the cell holds a formula. |
| [CELL](CELL.md) | Returns information about a cell's format, location and contents. |

## Official Documentation

- [Microsoft Support: ISFORMULA function](https://support.microsoft.com/en-us/excel/functions/isformula-function)
- [Google Docs Editors Help: ISFORMULA](https://support.google.com/docs/answer/6270316)
