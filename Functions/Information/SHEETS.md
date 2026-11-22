---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
purpose:
  - Workbook Information
use-case:
  - Quarter Span Checks
  - Tab Count Reports
  - Workbook Size Monitoring
related:
  - INDIRECT
  - ISREF
  - SHEET
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/sheets-function
  - https://support.google.com/docs/answer/16865347
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Count Tabs
  - Sheet Count
tags:
  - counting
  - excel
  - sheets
  - workbook-structure
---

# SHEETS

## Description

**SHEETS** returns the number of sheets in a reference. Given a 3D reference, such as a named range that runs from the Jan tab to the Mar tab, it returns the number of sheets that range crosses. With no argument, it counts every sheet in the workbook that contains the formula.

Excel counts every sheet type, including visible, hidden and very hidden worksheets, and chart, macro and dialog sheets. A hidden tab therefore raises the count even though nobody sees it. An invalid reference returns `#REF!`.

Use SHEETS to check the size of a workbook, to confirm that a 3D reference still covers the tabs you expect, or to count only the data tabs in a file that also has an index tab. SHEET answers a different question: it returns the position of one sheet, not the number of sheets.

## Syntax

```excel
=SHEETS([reference])
```

<!-- Image 1: Syntax Anatomy. See Images/Information/SHEETS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `reference` | No | A 3D reference or a name that refers to one, such as `Jan:Mar!B2`. When omitted, SHEETS counts all sheets in the workbook that contains the formula. |

### Return Value

A whole number: the count of sheets in the reference, or in the workbook when the argument is omitted. An invalid reference returns `#REF!`.

## Examples

All examples use a workbook with eight tabs in this order: Index, Jan, Feb, Mar, Apr, May, Jun, Notes. None of the tabs is hidden.

### Example 1: Counting Every Tab

```excel
=SHEETS()
```

**Result:** `8`

With no argument, SHEETS counts all eight tabs in the workbook.

### Example 2: Counting a 3D Reference

Assume a workbook name called `Q1_Span` refers to `=Jan:Mar!$B$2`.

```excel
=SHEETS(Q1_Span)
```

**Result:** `3`

The name covers the Jan, Feb and Mar tabs, so the result is 3. The count follows the name, not the cell.

### Example 3: Excluding the Index Tab

```excel
=SHEETS()-1
```

**Result:** `7`

Subtracting 1 removes the Index tab, which leaves seven tabs of data.

### Example 4: Building a Text Label

```excel
="Tabs in file: "&SHEETS()
```

**Result:** `Tabs in file: 8`

Joining the count to text lets a cover page show the tab total without a separate cell.

### Example 5: A Threshold Check

```excel
=IF(SHEETS()>12, "Review tabs", "Within limit")
```

**Result:** `Within limit`

With eight tabs, the file is under the limit of 12, so the check returns the message for a passing file.

<!-- Image 2: Sheets Counted in a 3D Reference. See Images/Information/SHEETS.md -->

## Story Problems

### Problem 1: Counting the Months in a Half-Year Span

A finance workbook has an Index tab, one tab for each month from January to June, and a Notes tab. A named range called `Half_Year` refers to `=Jan:Jun!$A$1`. The team needs the number of monthly tabs that the name covers.

| Tab Order | Tab |
| --- | --- |
| 1 | Index |
| 2 | Jan |
| 3 | Feb |
| 4 | Mar |
| 5 | Apr |
| 6 | May |
| 7 | Jun |
| 8 | Notes |

**Task:** Count the sheets covered by the name `Half_Year`.

**Solution:**

```excel
=SHEETS(Half_Year)
```

**Answer:** `6`. The span runs from Jan to Jun, which is six tabs.

### Problem 2: Counting Data Tabs in a Report Bundle

A report bundle has nine tabs: one Index tab, six data tabs and two hidden tabs used for lookups. The team wants the number of tabs that are not the index.

**Task:** Count every tab in the workbook, then remove the Index tab.

**Solution:**

```excel
=SHEETS()-1
```

**Answer:** `8`. SHEETS counts the hidden tabs too, so the total is 9, and removing the index leaves 8 tabs.

## Use Cases

### Tab Count Reports

**Scenario:** A governance rule limits each workbook to 12 tabs so that files stay manageable. A check cell on the Index tab flags files that go over the limit.

```excel
=IF(SHEETS()>12, "Too many tabs", "Within limit")
```

**Why It Works:** SHEETS counts hidden tabs, so the check cannot be bypassed by hiding extra tabs. The formula returns a clear message the moment the limit is passed.

### Quarter Span Checks

**Scenario:** A summary formula uses a 3D name that covers the Jan to Mar tabs. An analyst needs to know when someone inserts or removes a tab inside that span.

```excel
=SHEETS(Q1_Span)=3
```

**Why It Works:** The formula returns TRUE while the span covers three tabs. If a tab is inserted inside the span, the count changes and the check returns FALSE.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#REF!` | The reference is invalid, often after a sheet in the reference was deleted. | Redefine the name or reference so it points to valid sheets. |
| Count is higher than expected | Hidden and very hidden tabs are included in the count. | Subtract the tabs you do not want to count, or remove the hidden tabs. |
| Span count is lower than expected | The 3D reference does not reach the tab you intended. | Check the first and last tab named in the reference. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available; the Microsoft page lists no version restriction | Counts visible, hidden, very hidden and other sheet types. Supports 3D references. |
| Google Sheets | Available | Returns the total number of sheets in the referenced spreadsheet. With no argument, counts the sheets in the current spreadsheet. |

## Tips and Best Practices

- Use SHEETS with no argument to count every tab in a file, then subtract the tabs that are not data.
- Name a 3D reference when a formula must cover a fixed run of tabs, and the name keeps working when tabs are added inside the run.
- Check the count after a template change, because a hidden tab can appear in the total without anyone noticing.
- Keep the index or cover tab outside the count by subtracting it, so the number reflects the data.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SHEET](SHEET.md) | Returns the position of one sheet, not the number of sheets. |
| [INDIRECT](../Lookup%20%26%20Reference/INDIRECT.md) | Builds a reference from text, so a cell can point at a tab by name. |
| [ISREF](ISREF.md) | Tests whether a value is a valid reference before you pass it to SHEETS. |

## Official Documentation

- [Microsoft Support: SHEETS function](https://support.microsoft.com/en-us/excel/functions/sheets-function)
- [Google Docs Editors Help: SHEETS](https://support.google.com/docs/answer/16865347)
