---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
use-case:
  - Combined Quarterly Table
  - Export Column Merge
  - Side By Side Rosters
related:
  - CHOOSECOLS
  - DROP
  - EXPAND
  - TAKE
  - TRANSPOSE
  - VSTACK
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/hstack-function
  - https://support.google.com/docs/answer/13190756
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Horizontal Stack
tags:
  - array
  - dynamic-array
  - excel
  - sheets
---

# HSTACK

## Description

**HSTACK** joins two or more arrays or ranges side by side, column by column, and returns one larger array. It works like placing ranges next to each other, but the result is a formula that updates when the source ranges change. Use it to build a combined table from lists kept in separate columns, or to add a column of labels to a block of numbers.

The result has as many rows as the tallest input and as many columns as all the inputs together. When an input has fewer rows than the tallest one, Excel fills the missing rows with `#N/A`. Wrap HSTACK in IFERROR to replace those blanks with an empty string or another value.

HSTACK is a dynamic array function. It spills its result into the cells below and to the right of the formula, so those cells must be empty. The Microsoft help page lists it for Microsoft 365 and Excel 2024, not for Excel 2021 or earlier. Google Sheets also supports HSTACK, and its help page covers the basic syntax but not the behavior for ranges of different heights.

## Syntax

```excel
=HSTACK(array1, [array2], ...)
```

<!-- Image 1: Stacking Columns Side by Side. See Images/Lookup & Reference/HSTACK.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first range or array to place at the left of the result. |
| `[array2], ...` | No | Additional ranges or arrays to append to the right, in the order given. |

Google Sheets writes the same function as `HSTACK(range1, [range2, ...])`, with a comma or semicolon separator depending on the locale.

### Return Value

A dynamic array with the same number of rows as the tallest input and the combined number of columns. Cells that fall outside a shorter input show `#N/A` in Excel.

## Examples

The examples use this score list in `A1:B4`, with headers in row 1.

| Name | Score |
| --- | --- |
| Ava | 88 |
| Ben | 92 |
| Cy | 79 |

### Example 1: Join Two Columns

```excel
=HSTACK(A2:A4, B2:B4)
```

**Result:** A three-row, two-column block: Ava and 88, Ben and 92, Cy and 79.

Each input contributes one column to the result, and the rows line up because both inputs have three rows.

### Example 2: Include the Headers

```excel
=HSTACK(A1:A4, B1:B4)
```

**Result:** A four-row block with the headers `Name` and `Score` in the first row, followed by the three records.

Starting both ranges at row 1 carries the headers into the result.

### Example 3: Replace Mismatched Rows With a Blank

Cell `C2` holds `Pass` and cell `C3` holds `Fail`, so the range `C2:C3` has only two rows.

```excel
=IFERROR(HSTACK(A2:A4, C2:C3), "")
```

**Result:** Ava and Pass, Ben and Fail, and Cy with a blank second column.

Without IFERROR, the third row would show `#N/A` because `C2:C3` has no third value. The blank keeps the table clean.

### Example 4: Keep the First Two Rows

```excel
=TAKE(HSTACK(A2:A4, B2:B4), 2)
```

**Result:** Ava and 88, Ben and 92.

TAKE limits the stacked result to its first two rows, so the formula returns a short preview of the combined table.

## Story Problems

### Problem 1: Combined Quarterly Units

A shop keeps product names in `A1:A4`, Q1 unit sales in `B1:B4` and Q2 unit sales in `C1:C4`. Row 1 holds the headers.

| Product | Q1 | Q2 |
| --- | --- | --- |
| Lamp | 30 | 28 |
| Desk | 45 | 50 |
| Shelf | 12 | 15 |

**Task:** Build one table with the product name, Q1 and Q2 side by side, and find the total units sold across both quarters.

**Solution:**

```excel
=HSTACK(A2:A4, B2:C4)
```

**Answer:** A three-row, three-column table: Lamp 30 28, Desk 45 50, and Shelf 12 15. The total of all unit cells is `180`, from `=SUM(B2:C4)`.

<!-- Image 2: Combined Quarterly Table. See Images/Lookup & Reference/HSTACK.md -->

### Problem 2: Side By Side Team Rosters

Two teams keep their members in separate lists. Team A has three people in `A2:A4`, and Team B has two people in `B2:B3`.

| Team A | Team B |
| --- | --- |
| Ana | Tom |
| Raj | Lin |
| Mei | |

**Task:** Place both lists side by side in one table, with a blank cell where Team B has no third member.

**Solution:**

```excel
=IFERROR(HSTACK(A2:A4, B2:B3), "")
```

**Answer:** Three rows: Ana and Tom, Raj and Lin, Mei and a blank. The IFERROR wrapper turns the `#N/A` in the last row into an empty string.

## Use Cases

### Combined Quarterly Table

**Scenario:** A finance analyst builds a summary that places the account names beside two quarters of figures, so the table updates when either source changes.

```excel
=HSTACK(Accounts!A2:A40, Q1!B2:B40, Q2!B2:B40)
```

**Why It Works:** Each source stays on its own sheet, and HSTACK places the columns side by side without copying values. The summary keeps the same row order as the account list.

### Export Column Merge

**Scenario:** A data team receives a customer export with one column for names and another for email addresses, and needs them in one block before loading the data into a CRM.

```excel
=IFERROR(HSTACK(Export!A2:A500, Export!B2:B500, Export!C2:C500), "")
```

**Why It Works:** The three columns join into one block, and IFERROR blanks any row where a column is shorter than the others.

### Side By Side Rosters

**Scenario:** A coordinator shows two team rosters on one printed page for a meeting.

```excel
=HSTACK(TeamA!A2:A20, TeamB!A2:A20)
```

**Why It Works:** The two rosters appear next to each other, and the result updates as members join or leave the source lists.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` in some rows | An input has fewer rows than the tallest input. | Wrap the formula in IFERROR, or extend the shorter range. |
| `#SPILL!` | Cells below or to the right of the formula are not empty. | Clear the spill range. |
| `#NAME?` | The workbook uses Excel 2021 or earlier, which does not include HSTACK. | Use Power Query or INDEX-based formulas in older versions. |
| Headers missing | The first range starts at row 2 while the headers sit in row 1. | Start the ranges at row 1 when the headers should appear. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365 (Windows, Mac and web) and Excel 2024 | The help page does not list Excel 2021 or earlier. Missing rows return `#N/A`. |
| Google Sheets | Available | Appends ranges horizontally in sequence. The help page does not describe how mismatched row counts are padded, so test before relying on blank fill. |

## Tips and Best Practices

- Keep the source ranges the same height when you can, so the output needs no IFERROR wrapper.
- Use whole-table references such as `Table1[Name]` so the result grows with the source table.
- Combine HSTACK with TAKE, DROP or CHOOSECOLS to trim or reorder the stacked result in one formula.
- Use VSTACK when the blocks should join one below another instead of side by side.
- Leave enough empty cells to the right of the formula so the spill range is not blocked.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSECOLS](../Lookup%20%26%20Reference/CHOOSECOLS.md) | Selects and reorders columns from a stacked or existing array. |
| [DROP](../Lookup%20%26%20Reference/DROP.md) | Removes rows or columns from the start or end of an array. |
| [EXPAND](../Lookup%20%26%20Reference/EXPAND.md) | Pads an array to a larger size with a value you choose, which covers mismatched rows. |
| [TAKE](../Lookup%20%26%20Reference/TAKE.md) | Returns the first or last rows or columns of an array. |
| [TRANSPOSE](../Lookup%20%26%20Reference/TRANSPOSE.md) | Swaps rows and columns, which is useful before stacking lists in the other direction. |
| [VSTACK](../Lookup%20%26%20Reference/VSTACK.md) | Appends arrays one below another instead of side by side. |

## Official Documentation

- [Microsoft Support: HSTACK function](https://support.microsoft.com/en-us/excel/functions/hstack-function)
- [Google Docs Editors Help: HSTACK](https://support.google.com/docs/answer/13190756)
