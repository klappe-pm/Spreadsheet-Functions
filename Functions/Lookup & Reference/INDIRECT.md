---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
purpose:
  - Data Retrieval
use-case:
  - Cascading Dropdown Lists
  - Regional Sheet Selector
  - Variable Range Totals
related:
  - ADDRESS
  - INDEX
  - ISREF
  - MATCH
  - OFFSET
  - ROW
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/indirect-function
  - https://support.google.com/docs/answer/3093377
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Dynamic Reference
  - String Reference
  - Text To Reference
tags:
  - dynamic-reference
  - excel
  - reference
  - sheets
  - volatile
---

# INDIRECT

## Description

**INDIRECT** turns a text string into a cell or range reference and returns the contents of that reference. If a cell holds the text `B4`, then `=INDIRECT(D1)` returns the value in B4. Because the reference is built at calculation time, the target can change when a user types a different address, picks a sheet name from a list or builds the address from other cells.

INDIRECT is volatile. Microsoft Excel recalculates it whenever the worksheet changes, even when the change does not affect its target, so a workbook with many INDIRECT formulas can slow down. Where a fixed reference, INDEX with MATCH, or a range built with INDEX will do the job, use that instead. An INDIRECT reference also does not update when a sheet is renamed or a row is inserted, because the address is stored as text.

The reference style is set by the optional second argument. A1 style is the default. Passing `FALSE` reads the text as R1C1 style, which numbers rows and columns instead of using letters. Microsoft accepts cell references, a defined name that refers to a range, and references to other open workbooks. The Google Sheets page shows references to other sheets in the same spreadsheet, and it does not describe references to other files.

## Syntax

```excel
=INDIRECT(ref_text, [a1])
```

<!-- Image 1: INDIRECT Argument Anatomy. See Images/Lookup & Reference/INDIRECT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `ref_text` | Yes | The reference as text, such as `"B4"`, `"Sales!A1"`, `"'North Region'!B2"` or `"B2:B10"`. It can also be a cell that holds that text, or a defined name that refers to a range. |
| `a1` | No | `TRUE` or omitted reads `ref_text` as A1 style. `FALSE` reads it as R1C1 style, such as `"R5C2"` for cell B5. |

### Return Value

The value of the referenced cell, or the values of the referenced range when a function such as SUM receives it. INDIRECT returns `#REF!` when `ref_text` is not a valid reference, when it names a sheet or cell that does not exist, when it refers to a closed workbook in Excel, or when the reference goes beyond the sheet's row or column limits.

## Examples

All examples use this list in `A1:B5`, with the header in row 1.

| Item | Units |
| --- | --- |
| Pens | 120 |
| Staplers | 35 |
| Mugs | 60 |
| Kettles | 12 |

### Example 1: Reference From Hard-Coded Text

```excel
=INDIRECT("B4")
```

**Result:** `60`

The text `"B4"` is converted to a reference to cell B4, and the formula returns the value there.

### Example 2: Reference From a Cell

```excel
=INDIRECT(D1)
```

Where `D1` contains the text `B3`

**Result:** `35`

The formula reads the address from D1. Change D1 to `B5` and the formula returns 12 without being edited.

### Example 3: R1C1 Style

```excel
=INDIRECT("R5C2", FALSE)
```

**Result:** `12`

Row 5, column 2 is cell B5. The `FALSE` argument tells INDIRECT to read the text as R1C1 style, where R stands for row and C for column.

### Example 4: Sheet Name From a Cell

```excel
=INDIRECT("'"&D2&"'!B4")
```

Where `D2` contains `North Region`

**Result:** The value in cell B4 of the sheet named in D2

The text is joined to build a reference such as `'North Region'!B4`. The single quotes are required because the sheet name has a space. Sheet names without spaces or special characters can be written without quotes, but quoting every name is safer.

### Example 5: Sum of a Range Built From a Number

```excel
=SUM(INDIRECT("B2:B"&D3))
```

Where `D3` contains `4`

**Result:** `215`

The text becomes `B2:B4`, which covers 120, 35 and 60. The sum is 215. Change D3 and the range grows or shrinks.

### Example 6: The Same Sum Without INDIRECT

```excel
=SUM(B2:INDEX(B:B, D3))
```

Where `D3` contains `4`

**Result:** `215`

INDEX returns a reference to B4 without being volatile, so the range `B2:INDEX(B:B, D3)` covers the same cells as Example 5 with better calculation performance.

## Story Problems

### Problem 1: Regional Sheet Selector

A dashboard sheet has a drop-down in `A1` that lists the regions North, South and West. Each regional sheet has its total revenue in cell B2.

| Region Sheet | Revenue in B2 |
| --- | --- |
| North | 48200 |
| South | 36750 |
| West | 51300 |

**Task:** Enter a formula in `B1` that shows the revenue for the region chosen in `A1`.

**Solution:**

```excel
=INDIRECT("'"&A1&"'!B2")
```

**Answer:** `36750` when A1 is set to South. The quotes around the sheet name keep the reference valid if a name includes a space.

<!-- Image 2: Sheet Selector Result. See Images/Lookup & Reference/INDIRECT.md -->

### Problem 2: Total of the First Days in a Week

A shop lists daily sales in `B2:B8`, with the days in `A2:A8`. A manager enters a number of days in `D1` and wants the total of the first that many days.

| Day | Sales |
| --- | --- |
| Mon | 210 |
| Tue | 185 |
| Wed | 240 |
| Thu | 198 |
| Fri | 265 |
| Sat | 310 |
| Sun | 150 |

**Task:** Put 5 in `D1` and total the first five days of sales.

**Solution:**

```excel
=SUM(INDIRECT("B2:B"&(D1+1)))
```

**Answer:** `1098`, because 210 + 185 + 240 + 198 + 265 = 1098. The formula builds `B2:B6` from D1 plus 1, because the data starts in row 2.

## Use Cases

### Regional Sheet Selector

**Scenario:** A regional sales manager keeps one sheet per region with the same layout. The dashboard should show the same key figures for whichever region is selected in a drop-down.

```excel
=INDIRECT("'"&$A$2&"'!B2")
```

**Why It Works:** Each KPI formula joins the selected sheet name to a fixed cell address. The quotes handle sheet names with spaces. Adding a new region needs a new sheet and a new drop-down entry, but no formula changes. Renaming a regional sheet breaks the reference, so update the drop-down list when a sheet is renamed.

### Cascading Dropdown Lists

**Scenario:** A purchase form has a category drop-down in `A2`. The second drop-down should list only the products in the chosen category.

```excel
=INDIRECT(A2)
```

**Why It Works:** Each category is a defined name that refers to its product list, and the name matches the text in the first drop-down exactly. Enter `=INDIRECT(A2)` as the source of the second data validation list. Choosing a different category changes the list without changing the formula. This pattern relies on the names matching the drop-down text, so keep the spelling consistent.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#REF!` | The text is not a valid reference, or a sheet name is misspelled. | Check spelling, and compare the text with the sheet tab name. |
| `#REF!` | A sheet name has a space or a special character and the quotes are missing. | Wrap the sheet name in single quotes inside the text, as in `"'North Region'!B2"`. |
| `#REF!` | The source workbook is closed in Excel. | Open the source workbook, or use a different method for data in another file. |
| Wrong value | The text is in R1C1 style, but the second argument is omitted or `TRUE`. | Pass `FALSE` as the second argument for R1C1 text. |
| Slow workbook | Many INDIRECT formulas recalculate on every change. | Replace INDIRECT with INDEX-based references where the target can be expressed that way. |
| `#REF!` | The reference goes beyond the last row or column of the sheet. | Check the calculated row or column numbers. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Accepts A1 and R1C1 text, defined names, and references to open workbooks. Closed workbooks return `#REF!`. Recalculates on every worksheet change. |
| Google Sheets | Available | Accepts A1 and R1C1 text, using `FALSE` as the second argument for R1C1. The documentation shows references to other sheets in the same spreadsheet and does not describe other files. Use IMPORTRANGE for data in another spreadsheet. |

## Tips and Best Practices

- Use INDIRECT only when the address truly comes from text, and use INDEX for ranges that can be built from positions.
- Always put sheet names in single quotes inside the text, even when they seem to need none.
- Wrap the formula in IFERROR to show a friendly message when a user picks an invalid name.
- Keep a list of sheet names on one sheet, so a rename needs one change rather than many formula edits.
- Use defined names with INDIRECT for lists and datasets, because the names are easier to read and to maintain.

## Related Functions

| Function | Relationship |
| --- | --- |
| [INDEX](INDEX.md) | Returns a reference or value by position without volatility. Often a better choice for ranges. |
| [OFFSET](OFFSET.md) | Returns a reference from a starting cell. It is also volatile. |
| [ADDRESS](ADDRESS.md) | Builds the text address from row and column numbers, which INDIRECT can then read. |
| [MATCH](MATCH.md) | Finds the position of a header or name, which can be turned into an address. |
| [ROW](ROW.md) | Returns a row number that can be combined with text to build an address. |
| [ISREF](../Information/ISREF.md) | Tests whether a value is a valid reference, which helps when the text may be wrong. |

## Official Documentation

- [Microsoft Support: INDIRECT function](https://support.microsoft.com/en-us/excel/functions/indirect-function)
- [Google Docs Editors Help: INDIRECT](https://support.google.com/docs/answer/3093377)
