---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
purpose:
  - Type Checking
  - Workbook Information
use-case:
  - Cell Property Audit
  - Legacy Macro Migration
related:
  - CELL
  - GET.WORKBOOK
  - INFO
  - ISREF
level: 5
source:
  - https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - cell-information
  - legacy-macros
  - macro-functions
---

# GET.CELL

## Description

**GET.CELL** is a legacy Excel 4.0 macro function. It returned information about a cell, such as its row, column, format or contents, and it was used in old macro sheets and in named formulas inside macro-enabled workbooks. Microsoft's current alphabetical list of Excel functions does not include GET.CELL, and Google Sheets does not offer it.

Use this page when you maintain an older workbook that still contains GET.CELL and need to know what to replace it with. For new work, use the CELL function. CELL covers the same cell details in a form that works in a normal worksheet formula, and the examples below show the CELL form for each common task.

The argument numbers and return values of GET.CELL belong to the Excel 4.0 macro reference, which this page does not reproduce. Do not rely on a GET.CELL formula as a worksheet formula, because Excel's current function list does not describe it for that use.

## Syntax

```excel
=GET.CELL(type_num, reference)
```

<!-- Image 1: Legacy Function Notice. See Images/Information/GET.CELL.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `type_num` | Yes | A number that selects the cell detail to return. The numbers come from the Excel 4.0 macro reference. |
| `reference` | Yes | The cell to inspect. |

### Return Value

The return type depends on `type_num` in the legacy macro reference. The current Microsoft function list does not document a return value for GET.CELL, so this page does not state one. Use the CELL replacements in the examples to confirm the result you need.

## Examples

The examples show the CELL formula that replaces each common GET.CELL task. They are not GET.CELL formulas.

### Example 1: Row Number of a Cell

```excel
=CELL("row", C4)
```

**Result:** `4`

Row 4 is the row of cell C4.

### Example 2: Column Number of a Cell

```excel
=CELL("col", C4)
```

**Result:** `3`

Column 3 is column C.

### Example 3: Address of a Cell

```excel
=CELL("address", C4)
```

**Result:** `$C$4`

The address comes back as absolute text.

### Example 4: Cell Type

With C4 empty:

```excel
=CELL("type", C4)
```

**Result:** `b`

The `"type"` value returns `"b"` for a blank cell.

<!-- Image 2: Migration Mapping. See Images/Information/GET.CELL.md -->

## Story Problems

### Problem 1: Finding a Missing Crew Hour

A crew roster stores hours worked in column B. Dana, in row 4, has no hours entered.

| Crew Member | Hours |
| --- | --- |
| Ari | 8 |
| Bo | 6 |
| Dana | |

**Task:** Put a formula in D1 that returns the row number of Dana's blank hours cell, B4, and returns nothing when the cell has a value.

**Solution:**

```excel
=IF(CELL("type", B4)="b", CELL("row", B4), "")
```

**Answer:** `4`. The cell is blank, so its type is `"b"`, and the formula returns its row.

### Problem 2: Text Code Versus Number

Column D holds a product code in D2 and a quantity in D3. The code is text and the quantity is a number.

**Task:** Put a formula in E3 that returns the type code of the quantity in D3.

**Solution:**

```excel
=CELL("type", D3)
```

**Answer:** `v`. A number is reported as `"v"`, which means any value that is not blank or text.

## Use Cases

### Cell Property Audit

**Scenario:** An analyst is reviewing an inherited workbook that used GET.CELL in a named formula to read row numbers for a checklist.

```excel
=CELL("row", Checklist!C4)
```

**Why It Works:** CELL returns the same row number as the legacy call and works in an ordinary worksheet formula. Compare the old and new results on a few rows before replacing the rest.

### Legacy Macro Migration

**Scenario:** A monthly report depends on macro sheets that use GET.CELL to read cell types. The team wants the logic to work in a normal worksheet.

```excel
=IF(CELL("type", Report!B9)="b", "Missing", "Filled")
```

**Why It Works:** The type check moves into a worksheet formula that anyone can read and copy. The macro sheet can be removed once the new formulas return the same results.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` or no result | GET.CELL is not in Excel's current function list, so a worksheet formula may not calculate. | Replace the formula with CELL. |
| Macro blocked | The workbook uses legacy macro features that are disabled by security settings. | Replace the legacy formula with CELL so macros are not needed. |
| Different result after migration | The legacy type number does not match the CELL info_type. | Compare results on sample cells and use the CELL value that matches the task. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available in the current function list | A legacy Excel 4.0 macro function. Use CELL for cell information in worksheets. |
| Google Sheets | Not available | Use CELL, which Sheets supports with a required reference argument. |

## Tips and Best Practices

- Replace GET.CELL with CELL when you update an old workbook, and compare results on sample cells first.
- Keep a list of every legacy macro function in a workbook before you start migrating, so nothing is missed.
- Avoid new GET.CELL formulas because the function is not documented for worksheet use.
- Save a copy of the old workbook before removing macro sheets.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CELL](CELL.md) | The current worksheet function that returns cell information. |
| [GET.WORKBOOK](GET.WORKBOOK.md) | The legacy macro function for sheet and workbook information. |
| [INFO](INFO.md) | Returns information about the operating environment. |
| [ISREF](ISREF.md) | Tests whether a value is a valid reference. |

## Official Documentation

- [Microsoft Support: Excel functions (alphabetical)](https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188)
