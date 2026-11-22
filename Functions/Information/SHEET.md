---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
purpose:
  - Workbook Information
use-case:
  - Multi Sheet Index Builds
  - Sheet Position Checks
  - Tab Lookup by Name
related:
  - CELL
  - INDIRECT
  - ISREF
  - SHEETS
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/sheet-function
  - https://support.google.com/docs/answer/16865249
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Sheet Number
  - Tab Number
tags:
  - excel
  - navigation
  - sheets
  - workbook-structure
---

# SHEET

## Description

**SHEET** returns the position of a sheet in the workbook's tab order. The first tab is sheet 1, the second is sheet 2, and so on. You can give it a sheet name in quotes, or a reference such as `Mar!A1` or the name of a table or range. With no argument, it returns the number of the sheet that contains the formula.

The function returns a position, not a name. If someone moves a tab, its number changes. Excel counts every sheet type, including hidden and very hidden sheets, chart sheets, macro sheets and dialog sheets, so a hidden tab still takes up a position in the count.

Use SHEET when a workbook has many tabs and you need to know where a reference lives, to build an index of tabs, or to check that the tabs are in the expected order. It is a workbook-structure function, so it does not read the contents of the sheets it points to.

## Syntax

```excel
=SHEET([value])
```

<!-- Image 1: Syntax Anatomy. See Images/Information/SHEET.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `value` | No | A sheet name in double quotes, a reference such as `Feb!A1`, or the name of a table or range. When omitted, SHEET uses the sheet that contains the formula. |

### Return Value

A whole number from 1 upward, giving the sheet's position in the tab order. An invalid reference returns `#REF!`. A sheet name that does not exist returns `#N/A`.

## Examples

All examples use this tab order: Summary (1), Jan (2), Feb (3), Mar (4), Notes (5), Archive (6).

### Example 1: The Current Sheet

Entered on the Mar tab:

```excel
=SHEET()
```

**Result:** `4`

With no argument, SHEET reports the position of the tab that holds the formula.

### Example 2: A Sheet Name in Quotes

```excel
=SHEET("Notes")
```

**Result:** `5`

Quoting the name tells Excel to look the sheet up by name, so the formula does not need a cell reference.

### Example 3: A Reference on Another Sheet

```excel
=SHEET(Feb!A1)
```

**Result:** `3`

The function reports the sheet that holds cell A1 on the Feb tab, not the sheet that contains the formula.

### Example 4: A Missing Sheet Name

```excel
=SHEET("Budget")
```

**Result:** `#N/A`

No tab named Budget exists, so SHEET returns the `#N/A` error.

### Example 5: A Default for a Missing Sheet

```excel
=IFERROR(SHEET("Budget"), 0)
```

**Result:** `0`

Wrapping the call in IFERROR gives a default that a summary can test for, instead of showing an error.

### Example 6: Tabs Between Two Sheets

```excel
=SHEET(Mar!B2)-SHEET(Jan!B2)
```

**Result:** `2`

The Mar tab is position 4 and the Jan tab is position 2, so the difference is 2. Subtracting positions shows how far apart two tabs sit.

<!-- Image 2: Tab Positions and Sheet Lookups. See Images/Information/SHEET.md -->

## Story Problems

### Problem 1: Indexing Monthly Report Tabs

A finance team keeps one tab per month in this order: Cover, Summary, Jan, Feb, Mar, Apr, May, Jun. The index on the Cover tab lists the tab number of each month so a macro can jump to the right tab.

| Tab | Position |
| --- | --- |
| Cover | 1 |
| Summary | 2 |
| Jan | 3 |
| Feb | 4 |
| Mar | 5 |
| Apr | 6 |
| May | 7 |
| Jun | 8 |

**Task:** Return the tab number of the Jun tab for the index.

**Solution:**

```excel
=SHEET("Jun")
```

**Answer:** `8`. Jun is the eighth tab in the order above.

### Problem 2: Tabs Between January and June

The same workbook needs to know how many tabs separate the January tab from the June tab, so the reviewer can confirm that no tab was inserted between them.

**Task:** Subtract the Jan position from the Jun position.

**Solution:**

```excel
=SHEET("Jun")-SHEET("Jan")
```

**Answer:** `5`. Jun is position 8 and Jan is position 3, so 8 minus 3 is 5. If the result changes, a tab was inserted or moved between them.

## Use Cases

### Multi Sheet Index Builds

**Scenario:** A contents sheet lists each report, its tab name and its position, so a reader can see where each report sits.

```excel
=SHEET(Mar!A1)
```

**Why It Works:** The formula returns the position of the Mar tab, which the index places next to the tab name. Positions change when tabs move, so the tab name stays in the index as the stable label.

### Sheet Position Checks

**Scenario:** A reporting template must keep the Summary tab first. A check cell on the Cover tab warns the team when someone moves it.

```excel
=IF(SHEET(Summary!A1)=1, "Order OK", "Summary moved")
```

**Why It Works:** SHEET returns 1 only when Summary is the first tab, so the check changes as soon as the order changes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#REF!` | The reference points to a deleted sheet or cell. | Update the formula to a valid sheet or cell. |
| `#N/A` | The sheet name in quotes does not match any tab. | Check the spelling of the sheet name. |
| `#NAME?` | A sheet name without quotes is not recognized as a name. | Put text names in double quotes. |
| A position is one higher or lower than expected | Hidden or very hidden tabs take positions in the count. | Count hidden tabs when you plan positions, or unhide them while you check the order. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available; the Microsoft page lists no version restriction | Counts visible, hidden, very hidden and other sheet types. |
| Google Sheets | Available | Numbering starts at 1 for the first sheet. Accepts a sheet name or a reference. |

## Tips and Best Practices

- Pair the position with the tab name in an index, because numbers change when tabs move and names stay stable.
- Add a check cell that compares the position to the expected number, so a moved tab shows up at once.
- Remember that hidden tabs take positions, so an index built from positions may need updating after you hide a tab.
- Use a quoted sheet name when the formula should find a tab by name rather than by a cell reference.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SHEETS](SHEETS.md) | Counts the sheets in a workbook or reference, instead of finding one sheet's position. |
| [INDIRECT](../Lookup%20%26%20Reference/INDIRECT.md) | Builds a reference from text, so a cell can name the tab to read. |
| [ISREF](ISREF.md) | Tests whether a value is a valid reference before you pass it to SHEET. |
| [CELL](CELL.md) | Returns details about a cell, including the file information that names the sheet in Excel. |

## Official Documentation

- [Microsoft Support: SHEET function](https://support.microsoft.com/en-us/excel/functions/sheet-function)
- [Google Docs Editors Help: SHEET](https://support.google.com/docs/answer/16865249)
