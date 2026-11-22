---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Dynamic Arrays
purpose:
  - Array Shaping
use-case:
  - Combined Regional Lists
  - Header Plus Data Export
  - Monthly Expense Totals
related:
  - HSTACK
  - IFERROR
  - ROWS
  - TOCOL
  - WRAPROWS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/vstack-function
  - https://support.google.com/docs/answer/13191461
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Stack Arrays Vertically
  - Vertical Stack
tags:
  - array-shaping
  - dynamic-array
  - excel
  - sheets
  - stacking
---

# VSTACK

## Description

**VSTACK** joins two or more arrays or ranges one below the other and returns a single larger array. The first array appears at the top, the second array starts in the row after the first one ends, and so on. The result spills into the cells below and to the right of the formula cell, so no copying is needed.

Use VSTACK when several blocks of data share the same layout and you want to read them as one list. Typical cases include merging monthly sheets, combining regional lists, or adding a header row above a block of results. Because VSTACK returns an array, its output can feed directly into functions such as SUM, ROWS, SORT or FILTER.

The companion function [HSTACK](HSTACK.md) joins arrays side by side instead. To put the values of a range into one column, use [TOCOL](TOCOL.md). To reshape a single list into a grid with a fixed number of rows, use [WRAPROWS](WRAPROWS.md) or [WRAPCOLS](WRAPCOLS.md).

VSTACK is available in Excel for Microsoft 365, Excel for the web and Excel 2024. It is not available in Excel 2021 or earlier. Google Sheets supports it under the same name.

## Syntax

```excel
=VSTACK(array1, [array2], ...)
```

<!-- Image 1: VSTACK Syntax Anatomy. See Images/Lookup & Reference/VSTACK.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array1` | Yes | The first range, array or constant to append. It forms the top block of the result. |
| `array2` | No | The next range, array or constant to append below the previous block. |
| `...` | No | Further arrays, each appended below the last. Excel accepts many arrays in one call. |

### Return Value

A single array with as many rows as all input arrays combined and as many columns as the widest input array. If an array is narrower than the widest one, Excel fills the missing columns with `#N/A`. The result is a spilled array, so an error appears only when the output range is blocked.

## Examples

All examples use two regional lists. The North list is in `A2:C4` and the South list is in `A6:C8`, each with three rows of Store, Units and Revenue.

### Example 1: Stacking Two Ranges

```excel
=VSTACK(A2:C4, A6:C8)
```

**Result:** A spilled array of six rows and three columns

The three North rows come first, followed by the three South rows. Both ranges have the same number of columns, so no padding is needed.

### Example 2: Adding a Header Row to Results

```excel
=VSTACK({"Store","Units"}, A2:B4)
```

**Result:** A spilled array of four rows and two columns, with `Store` and `Units` at the top

The array constant supplies the header row, and the three data rows from `A2:B4` follow below it. The constant has two columns, so it matches the width of the range.

### Example 3: Handling Narrower Arrays

```excel
=IFERROR(VSTACK(A2:B3, C2:C4), "")
```

**Result:** A spilled array of five rows and two columns

`A2:B3` has two columns and `C2:C4` has one. Excel fills the missing second column for the rows from `C2:C4` with `#N/A`, and `IFERROR` replaces those cells with blank text. The first two rows keep their values.

### Example 4: Combining Three Monthly Sheets

```excel
=VSTACK(Jan!A2:B4, Feb!A2:B4, Mar!A2:B4)
```

**Result:** A spilled array with the rows of all three months, one after another

Each month sheet contributes its rows in order. If each sheet holds three data rows, the result has nine rows. Use the same layout on every sheet so the columns line up.

## Story Problems

### Problem 1: Counting Products Across Two Price Lists

A distributor keeps one price list per branch. The North list is in `A2:B5` with four products, and the South list is in `D2:E4` with three products. Both lists have a product name and a unit price in each row.

| North Product | North Price | South Product | South Price |
| --- | --- | --- | --- |
| Bolt Pack | 4.50 | Gasket | 2.25 |
| Hinge | 3.10 | Washer Set | 1.75 |
| Latch | 6.00 | Spring | 2.90 |
| Pin Kit | 5.25 | | |

**Task:** Count the total number of product rows across both lists using one formula.

**Solution:**

```excel
=ROWS(VSTACK(A2:B5, D2:E4))
```

**Answer:** `7`, because the North list contributes 4 rows and the South list contributes 3 rows.

<!-- Image 2: Stacking Ranges Into One Block. See Images/Lookup & Reference/VSTACK.md -->

### Problem 2: Total Expenses Across Three Months

A household keeps monthly expenses in column B of three sheets. January has values in `B2:B4`, February has values in `B2:B3`, and March has values in `B2:B5`.

| Month | Expenses |
| --- | --- |
| January | 120, 85, 40 |
| February | 200, 15 |
| March | 60, 75, 90, 30 |

**Task:** Add all the expenses for the three months with one formula, without copying values into a new sheet.

**Solution:**

```excel
=SUM(VSTACK(Jan!B2:B4, Feb!B2:B3, Mar!B2:B5))
```

**Answer:** `715`. January totals 245, February totals 215 and March totals 255, and those three totals add to 715.

<!-- Image 3: Monthly Totals Result. See Images/Lookup & Reference/VSTACK.md -->

## Use Cases

### Combined Regional Lists

**Scenario:** Each regional team maintains its own customer list on a separate sheet. Management wants one list for a national mailing.

```excel
=VSTACK(North!A2:C200, South!A2:C200, West!A2:C200)
```

**Why It Works:** The formula keeps the regional lists separate for entry and joins them for reporting. The ranges are extended past the current data so new rows are included without editing the formula.

### Header Plus Data Export

**Scenario:** A report must start with a header row, and the data below it comes from a ledger that can grow over time.

```excel
=VSTACK({"Date","Amount"}, FILTER(Ledger!A2:B, Ledger!B2:B<>""))
```

**Why It Works:** The array constant adds the header and FILTER removes blank ledger rows, so the export stays clean as the ledger changes.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#N/A` in the last column | One input array has fewer columns than the widest input. | Make the arrays the same width, or wrap the formula in `IFERROR`. |
| `#SPILL!` | Cells in the spill area already contain data. | Clear the cells below and to the right of the formula. |
| `#NAME?` | The workbook is opened in Excel 2021 or earlier, where VSTACK does not exist. | Open the file in Excel for Microsoft 365, Excel 2024 or Google Sheets. |
| Unexpected row count | A range includes blank rows that are part of the stack. | Limit each range to the filled rows, or filter the blanks out. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Excel for the web and Excel 2024. | Shorter arrays are padded with `#N/A`. Arguments are named `array1` and `array2`. |
| Google Sheets | Available. | Arguments are named `range1` and `range2`. The official page does not describe padding for arrays of different widths, so test that case before relying on it. |

## Tips and Best Practices

- Stack ranges of the same width so the output has no padding errors.
- Wrap the result in `IFERROR` only when you have confirmed that the `#N/A` values come from padding.
- Pass the result to `SORT`, `FILTER` or `ROWS` to build reports without helper columns.
- Use whole-column references with care, because blank rows are stacked too.

## Related Functions

| Function | Relationship |
| --- | --- |
| [HSTACK](HSTACK.md) | Joins arrays side by side instead of one below the other. |
| [IFERROR](../Logical/IFERROR.md) | Replaces the `#N/A` padding with a blank or another value. |
| [ROWS](ROWS.md) | Counts the rows of a stacked result. |
| [TOCOL](TOCOL.md) | Flattens an array into one column, which can be combined with stacking. |
| [WRAPROWS](WRAPROWS.md) | Reshapes a single list into rows of a fixed size, the opposite of stacking. |

## Official Documentation

- [Microsoft Support: VSTACK function](https://support.microsoft.com/en-us/excel/functions/vstack-function)
- [Google Docs Editors Help: VSTACK](https://support.google.com/docs/answer/13191461)
