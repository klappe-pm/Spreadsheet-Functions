---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
purpose:
  - Counting
use-case:
  - Auditing Report Layouts
  - Counting Union References
  - Validating Multi Area Selections
related:
  - COLUMNS
  - INDEX
  - OFFSET
  - ROWS
level: 5
source:
  - https://support.microsoft.com/en-us/excel/functions/areas-function
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Area Count
  - Reference Area Count
tags:
  - excel
  - multi-area
  - reference-count
---

# AREAS

## Description

**AREAS** counts the areas in a reference. An area is one contiguous block of cells, and a single cell counts as an area too. A reference built from several blocks, such as `A1:A3` plus `C1` plus `E1:F2`, contains as many areas as it has blocks. Use AREAS when a selection may be split and you need to know how many pieces it has before a formula expects one block.

AREAS is a specialist function. Most formulas need the size of one block, which ROWS and COLUMNS give. AREAS answers a different question: how many separate blocks the reference holds. It is most useful for checking report layouts and for validating selections made with unions.

Microsoft Excel supports unions. You join the blocks with commas and wrap the list in an extra pair of parentheses so that Excel reads the commas as part of one reference. Google Sheets does not provide AREAS.

## Syntax

```excel
=AREAS(reference)
```

<!-- Image 1: Area Count Diagram. See Images/Lookup & Reference/AREAS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `reference` | Yes | A cell or range reference. To count several blocks, wrap the list in an extra pair of parentheses, such as `((A1:A3,C1))`, so the commas join the blocks into one reference. |

### Return Value

A whole number: the count of areas in the reference. A single contiguous range returns 1.

## Examples

### Example 1: One Contiguous Block

```excel
=AREAS(B2:D4)
```

**Result:** `1`

The range is one rectangle of nine cells, so it is one area.

### Example 2: A Union of Three Blocks

```excel
=AREAS((A1:A3,C1,E1:F2))
```

**Result:** `3`

Each block is separated from the others, so the union holds three areas: the column A block, the single cell C1 and the block E1:F2.

<!-- Image 2: Union Syntax Versus Contiguous Range. See Images/Lookup & Reference/AREAS.md -->

### Example 3: Intersection Gives One Area

```excel
=AREAS(A1:D10 C5:F12)
```

**Result:** `1`

A space between two references is the intersection operator. The overlap is C5:D10, which is a single block, so the count is 1.

## Story Problems

### Problem 1: Three Blocks on a Monthly Report

A finance team keeps three blocks on a report sheet. The blocks are listed in the table below.

| Block | Range |
| --- | --- |
| Revenue | B2:E6 |
| Costs | B9:E12 |
| Notes | G2:G4 |

**Task:** Count the areas in a selection that includes all three blocks.

**Solution:**

```excel
=AREAS((B2:E6,B9:E12,G2:G4))
```

**Answer:** `3`. Each listed range is a separate block, and the union keeps them as three areas.

### Problem 2: Checking a Selection Before Copying

A bookkeeper selects two parts of a list before running a copy routine that works only on one block. The first part is `B2:B9`, and the second is `B11:B12`. Row 10 is blank between them.

| Selection | Range |
| --- | --- |
| Part A | B2:B9 |
| Part B | B11:B12 |

**Task:** In cell D2, return "Split" when the selection has more than one area and "Contiguous" when it has one.

**Solution:**

```excel
=IF(AREAS((B2:B9,B11:B12))>1, "Split", "Contiguous")
```

**Answer:** `Split`. The blank row 10 divides the selection into two areas, so AREAS returns 2.

## Use Cases

### Auditing Report Layouts

**Scenario:** A monthly report must keep each figure block in one piece. An audit cell checks that the data block has not been split by an inserted row.

```excel
=IF(AREAS(Report!$B$2:$B$40)=1, "Block intact", "Check for a split")
```

**Why It Works:** A single unbroken block returns 1. The formula reports a problem only when the reference it checks changes shape, so update the reference after rows are inserted or removed inside the block.

### Counting Union References

**Scenario:** A planner keeps four quarterly sales ranges with defined names. A total must show how many quarters are included in a selection.

```excel
=AREAS((Q1Sales,Q2Sales,Q3Sales,Q4Sales))
```

**Why It Works:** Each name refers to one block, and the union keeps the four blocks separate, so the result is 4 for all four quarters.

### Validating Multi Area Selections

**Scenario:** A control cell on a dashboard accepts a selected range from a user. The formula that follows needs exactly one block.

```excel
=IF(AREAS(Selected)=1, "OK", "Select one block")
```

**Why It Works:** The formula stops users from entering a multi-block selection before a calculation that expects one block runs.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Count does not match the blocks | The blocks are not joined with commas inside an extra pair of parentheses. | Write the union as `AREAS((A1:A3,C1))`. Without the extra parentheses, Excel reads the commas as argument separators, which does not match the single argument AREAS accepts. |
| Count of 1 for a split selection | The references are joined with a space, which is the intersection operator. | Use commas inside the extra parentheses for a union. |
| Unexpected count after editing | An inserted or deleted row changed how the blocks touch. | Recheck the references after structural edits. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024, Excel 2021, Excel 2019 and Excel 2016 | Counts areas in a reference, including unions written with commas. |
| Google Sheets | Not available | Use ROWS and COLUMNS to size a single block. |

## Tips and Best Practices

- Count areas before passing a selection to a function that expects one block.
- Use defined names for each block in a long union, so the formula stays readable.
- Remember that an area is one contiguous block, so a blank row between two blocks creates a second area.
- Use ROWS and COLUMNS when the question is how big one block is rather than how many blocks there are.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COLUMNS](COLUMNS.md) | Counts the columns in one block, the size measure AREAS does not give. |
| [INDEX](INDEX.md) | Returns a cell or area from a reference by position, including an area chosen by its number. |
| [OFFSET](OFFSET.md) | Builds a reference of a set size from a starting cell. |
| [ROWS](ROWS.md) | Counts the rows in one block. |

## Official Documentation

- [Microsoft Support: AREAS function](https://support.microsoft.com/en-us/excel/functions/areas-function)
