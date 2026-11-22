---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
purpose:
  - Workbook Information
use-case:
  - Legacy Workbook Migration
  - Open Workbook Inventory
related:
  - CELL
  - GET.CELL
  - INFO
  - SHEETS
level: 5
source:
  - https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - legacy-macros
  - macro-functions
  - workbook-info
---

# GET.WORKBOOK

## Description

**GET.WORKBOOK** is a legacy Excel 4.0 macro function. It returned information about a workbook, such as its sheet names or the sheet type, and it was used in macro sheets in older Excel files. Microsoft's current alphabetical list of Excel functions does not include GET.WORKBOOK, and Google Sheets does not offer it.

Use this page when an older workbook still contains GET.WORKBOOK and you need a current replacement. For the file path, use CELL with the `"filename"` value. For the environment and open workbook count, use INFO in desktop Excel. In Google Sheets, SHEETS counts the sheets in a spreadsheet.

The argument numbers and return values of GET.WORKBOOK belong to the Excel 4.0 macro reference, which this page does not reproduce. Do not build new worksheet formulas on GET.WORKBOOK, because the current function list does not describe it for that use.

## Syntax

```excel
=GET.WORKBOOK(type_num)
```

<!-- Image 1: Legacy Function Notice. See Images/Information/GET.WORKBOOK.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `type_num` | Yes | A number that selects the workbook detail to return. The numbers come from the Excel 4.0 macro reference. |

### Return Value

The return type depends on `type_num` in the legacy macro reference. The current Microsoft function list does not document a return value for GET.WORKBOOK, so this page does not state one. Use the replacements in the examples to get the detail you need.

## Examples

The examples show the current formulas that replace common GET.WORKBOOK tasks. They are not GET.WORKBOOK formulas.

### Example 1: Full Path of the Workbook

```excel
=CELL("filename", A1)
```

**Result:** The full file path of the saved workbook as text. For an unsaved workbook, the result is empty text.

Microsoft documents that the `"filename"` value returns the full path, and it returns empty text when the file has not been saved.

### Example 2: Number of Worksheets in Open Workbooks

```excel
=INFO("numfile")
```

**Result:** `7` when three workbooks are open with 2, 1 and 4 worksheets

INFO with `"numfile"` returns the total number of worksheets in all open workbooks. INFO is available in desktop Excel only.

<!-- Image 2: Open Workbook Sheet Count. See Images/Information/GET.WORKBOOK.md -->

### Example 3: Calculation Mode

```excel
=INFO("recalc")
```

**Result:** `Automatic` or `Manual`, depending on the calculation mode the user has set

The `"recalc"` value reports the current recalculation mode.

### Example 4: Sheet Count in Google Sheets

```excel
=SHEETS()
```

**Result:** `3` in a spreadsheet with three sheet tabs

SHEETS is the Google Sheets function that counts the sheets in the spreadsheet that holds the formula.

## Story Problems

### Problem 1: Counting Sheets Across Open Files

A finance analyst has three workbooks open at the same time: Budget with 3 sheets, Sales with 5 sheets and Roster with 2 sheets.

| Workbook | Sheets |
| --- | --- |
| Budget | 3 |
| Sales | 5 |
| Roster | 2 |

**Task:** Put a formula in E1 that returns the total number of worksheets in all open workbooks.

**Solution:**

```excel
=INFO("numfile")
```

**Answer:** `10`, because 3 + 5 + 2 = 10. INFO counts every worksheet in every open workbook.

### Problem 2: Warning When Calculation Is Manual

A model sheet should tell users to refresh when calculation is set to manual.

**Task:** Put a formula in B1 that returns `Press F9 to refresh` when the calculation mode is Manual and `Up to date` otherwise. The mode is set to Manual.

**Solution:**

```excel
=IF(INFO("recalc")="Manual", "Press F9 to refresh", "Up to date")
```

**Answer:** `Press F9 to refresh`. The `"recalc"` value returns `Manual`, so the IF returns the warning.

## Use Cases

### Legacy Workbook Migration

**Scenario:** A regional team inherited a workbook whose macro sheet used GET.WORKBOOK to read the sheet type. The team wants the same information in a worksheet formula.

```excel
=CELL("filename", Summary!A1)
```

**Why It Works:** The file path comes from CELL, which works in a normal worksheet. Use the path to confirm which copy of the workbook is open before comparing results.

### Open Workbook Inventory

**Scenario:** An operations lead needs to know how many worksheets are open before running a consolidation macro.

```excel
=INFO("numfile")
```

**Why It Works:** The count covers every open workbook, so the team can confirm the expected total before it runs the consolidation.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` or no result | GET.WORKBOOK is not in Excel's current function list, so a worksheet formula may not calculate. | Replace the formula with CELL, INFO or SHEETS, as shown in the examples. |
| Empty result for the path | The workbook has not been saved. | Save the workbook, then recalculate. |
| `#N/A` from INFO | Some INFO values are removed and return `#N/A`. | Use the `"numfile"`, `"recalc"` or `"directory"` values, which remain supported. |
| Macro blocked | Legacy macro features are disabled by security settings. | Replace the legacy formula so macros are not needed. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available in the current function list | A legacy Excel 4.0 macro function. Use CELL with `"filename"`, or INFO in desktop Excel. |
| Google Sheets | Not available | Use SHEETS to count the sheets in the spreadsheet. |

## Tips and Best Practices

- Inventory every legacy macro function in a workbook before you start migrating.
- Save a copy of the workbook before you remove macro sheets.
- Compare the old and new results on a few workbooks before you retire the legacy formula.
- Avoid new GET.WORKBOOK formulas because the function is not documented for worksheet use.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CELL](CELL.md) | Returns the file path with the `"filename"` value. |
| [GET.CELL](GET.CELL.md) | The legacy macro function for cell information. |
| [INFO](INFO.md) | Returns the open worksheet count and calculation mode in desktop Excel. |
| [SHEETS](SHEETS.md) | Counts the sheets in a Google Sheets spreadsheet. |

## Official Documentation

- [Microsoft Support: Excel functions (alphabetical)](https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188)
