---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
purpose:
  - Workbook Information
use-case:
  - Calculation Mode Warnings
  - Sheet Count Checks
related:
  - CELL
  - GET.WORKBOOK
  - ISREF
  - SHEETS
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/info-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases: []
tags:
  - environment-info
  - excel
  - workbook-info
---

# INFO

## Description

**INFO** returns information about the operating environment that Excel is running in. You choose the detail with a text value, such as `"recalc"` for the calculation mode, `"numfile"` for the number of worksheets in all open workbooks, or `"system"` for the operating system family.

Use INFO when a formula must change its behavior based on the environment, for example to show a warning when calculation is set to manual, or to check how many workbooks are open before a consolidation step. INFO returns details about the session, not about a cell, so use CELL for cell information and ISREF for reference checks.

Several INFO values depend on the computer and the user settings. The results can differ between a Windows and a Mac, and between two colleagues with different calculation modes. Keep INFO out of logic that must give the same answer for everyone who opens a shared workbook.

Microsoft lists INFO as unavailable in Excel for the web, while the same page's Applies To list includes Excel for the web. Check the behavior in the environment where people will open the file before you depend on it. Google Sheets has no INFO function.

## Syntax

```excel
=INFO(type_text)
```

<!-- Image 1: Syntax Anatomy. See Images/Information/INFO.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `type_text` | Yes | A text value in double quotes that names the information to return. |

Valid values are `"directory"`, `"numfile"`, `"origin"`, `"osversion"`, `"recalc"`, `"release"` and `"system"`. The values `"memavail"`, `"memused"` and `"totmem"` are no longer supported.

### Return Value

Most values return text. `"numfile"` returns a number. `"recalc"` returns `"Automatic"` or `"Manual"`. `"system"` returns `"mac"` on a Macintosh and `"pcdos"` on Windows. The removed values `"memavail"`, `"memused"` and `"totmem"` return `#N/A`.

## Examples

### Example 1: Current Calculation Mode

```excel
=INFO("recalc")
```

**Result:** `Automatic` when the workbook calculates on every change, or `Manual` when the user has set manual calculation

The value shows the mode the current Excel session is using.

### Example 2: Operating System Family

```excel
=INFO("system")
```

**Result:** `pcdos` on Windows, or `mac` on a Macintosh

The result identifies the system family, not the version. Use `"osversion"` when you need the version string.

### Example 3: Worksheets in Open Workbooks

Three workbooks are open with 2, 1 and 4 worksheets.

```excel
=INFO("numfile")
```

**Result:** `7`

The value counts every worksheet across all open workbooks, not only the active one.

<!-- Image 2: Environment Check Warning. See Images/Information/INFO.md -->

### Example 4: Warning When Calculation Is Manual

```excel
=IF(INFO("recalc")="Manual", "Press F9 to refresh", "Up to date")
```

**Result:** `Press F9 to refresh` when the calculation mode is Manual

The formula shows a reminder only in the sessions that need it.

### Example 5: A Removed Value

```excel
=INFO("memavail")
```

**Result:** `#N/A`

The memory values were removed, so INFO now returns `#N/A`. Replace any old formula that used them.

## Story Problems

### Problem 1: Counting Worksheets Before a Consolidation

A finance team has three workbooks open for the quarter: Budget with 3 worksheets, Sales with 5 and Roster with 2.

| Workbook | Worksheets |
| --- | --- |
| Budget | 3 |
| Sales | 5 |
| Roster | 2 |

**Task:** Put a formula in E1 that returns the total number of worksheets in all open workbooks.

**Solution:**

```excel
=INFO("numfile")
```

**Answer:** `10`, because 3 + 5 + 2 = 10. The consolidation step expects this total before it runs.

### Problem 2: Reminder on a Manual Model

A forecast model is shared with a colleague whose Excel session is set to manual calculation. The model should display a reminder in B1.

**Task:** Write a formula in B1 that returns `Press F9 to refresh` when the mode is Manual and `Up to date` otherwise.

**Solution:**

```excel
=IF(INFO("recalc")="Manual", "Press F9 to refresh", "Up to date")
```

**Answer:** `Press F9 to refresh` for the colleague, because the mode is Manual in that session.

## Use Cases

### Calculation Mode Warnings

**Scenario:** A large planning model takes minutes to recalculate, so users set manual calculation. Reviewers can miss updates when they forget to refresh.

```excel
=IF(INFO("recalc")="Manual", "Press F9 before reviewing", "")
```

**Why It Works:** The reminder appears only when the session uses manual calculation, so automatic-mode users see nothing extra.

### Sheet Count Checks

**Scenario:** A monthly process stops working when a user leaves too many workbooks open, because the macro expects a fixed number of worksheets.

```excel
=IF(INFO("numfile")>12, "Close unused files", "Ready")
```

**Why It Works:** The formula compares the count with a limit and shows a message that tells the user what to do before the process starts.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` | The value is one of the removed memory types or is not supported. | Remove the value and use `"osversion"`, `"system"` or `"release"` instead. |
| Different results on two computers | `"system"`, `"recalc"` and `"osversion"` depend on the session. | Do not use environment values for logic that must match across users. |
| Not available | The function does not run in Excel for the web, as Microsoft notes on the function page. | Check the environment where people open the workbook. |
| Wrong count | `"numfile"` counts all open workbooks, not only the current one. | Close unrelated workbooks or document the expected count. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in desktop Excel for Windows and Mac | Microsoft lists it as not available in Excel for the web. The same page's Applies To list includes Excel for the web, so verify in your environment. |
| Google Sheets | Not available | Use SHEETS to count sheets in a spreadsheet, or CELL for cell information. |

## Tips and Best Practices

- Use INFO for reminders and checks in your own session, not for logic that every reader must see the same way.
- Wrap INFO in IFERROR when a removed value might still be in an old formula.
- Keep the expected sheet count in a labeled input cell so the check is easy to change.
- Use CELL for cell details and ISREF for reference checks.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CELL](CELL.md) | Returns information about a cell rather than the session. |
| [GET.WORKBOOK](GET.WORKBOOK.md) | The legacy macro function for workbook details. |
| [ISREF](ISREF.md) | Tests whether a value is a valid reference. |
| [SHEETS](SHEETS.md) | Counts sheets in a Google Sheets spreadsheet. |

## Official Documentation

- [Microsoft Support: INFO function](https://support.microsoft.com/en-us/excel/functions/info-function)
