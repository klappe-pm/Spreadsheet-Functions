---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
purpose:
  - Array Shaping
use-case:
  - Export Column Reordering
  - Report Column Selection
  - Trimming Imported Data
related:
  - CHOOSEROWS
  - DROP
  - FILTER
  - TAKE
  - TRANSPOSE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/choosecols-function
  - https://support.google.com/docs/answer/13197914
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Column Selector
  - Pick Columns
tags:
  - array-shaping
  - dynamic-array
  - excel
  - sheets
---

# CHOOSECOLS

## Description

**CHOOSECOLS** returns a new array made of the columns you name, in the order you name them. Give it a table and the column numbers 1, 3 and 5, and it returns columns 1, 3 and 5 as one block. A column number can repeat, so the same column can appear twice in the result.

Use CHOOSECOLS when you want to keep a few columns from a wider table, such as a report that needs only three of twelve fields. Use DROP when it is easier to name the columns you do not want. CHOOSECOLS works on a range or on an array produced by another formula, so it can sit at the end of a chain of array functions.

Negative numbers count from the right edge of the array. The number -1 is the last column, -2 is the column before it, and so on. Because the count starts from the right, the same negative numbers keep pointing at the same last columns when new columns are added to the left.

## Syntax

```excel
=CHOOSECOLS(array, col_num1, [col_num2], ...)
```

<!-- Image 1: Column Selection Anatomy. See Images/Lookup & Reference/CHOOSECOLS.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array that holds the columns to return. |
| `col_num1` | Yes | The first column to return. 1 is the first column, and a negative number counts from the last column. Zero is not allowed. |
| `col_num2`, ... | No | More column numbers, returned in the order given. A column can be listed more than once. |

### Return Value

A new array that holds the requested columns in the order listed. In Excel, a column number of 0, or one whose absolute value is larger than the number of columns, returns `#VALUE!`. The array spills into the cells below and to the right of the formula in Excel 365.

## Examples

All examples use this order table in `A1:E6`, with headers in row 1.

| ID | Customer | Region | Units | Price |
| --- | --- | --- | --- | --- |
| 1001 | Harbor Cafe | North | 4 | 12 |
| 1002 | Lakeside Deli | South | 10 | 8 |
| 1003 | Pine Market | North | 6 | 15 |
| 1004 | Riverside Bakery | East | 3 | 20 |
| 1005 | Summit Grill | South | 7 | 9 |

### Example 1: Two Columns in Their Original Order

```excel
=CHOOSECOLS(A2:E6, 2, 5)
```

**Result:** the Customer and Price columns for all five orders

The numbers 2 and 5 pick columns B and E, and the result keeps that order.

### Example 2: Repeating a Column

```excel
=CHOOSECOLS(A2:E6, 1, 3, 1)
```

**Result:** three columns: ID, Region and ID again

Column 1 appears twice because it is listed twice. Repeating a column is useful when a template needs a key next to each row.

### Example 3: Columns Counted From the Right

```excel
=CHOOSECOLS(A2:E6, -1, -2)
```

**Result:** the Price column, then the Units column

Negative numbers count from the last column. -1 returns Price and -2 returns Units.

<!-- Image 2: Positive and Negative Column Numbers. See Images/Lookup & Reference/CHOOSECOLS.md -->

### Example 4: Summing One Column

```excel
=SUM(CHOOSECOLS(A2:E6, 4))
```

**Result:** `30`

Column 4 is Units, and 4 + 10 + 6 + 3 + 7 is 30.

### Example 5: Summing the Last Column

```excel
=SUM(CHOOSECOLS(A2:E6, -1))
```

**Result:** `64`

The last column is Price, and 12 + 8 + 15 + 20 + 9 is 64.

## Story Problems

### Problem 1: Minutes From a Support Export

A support team exports four fields for each ticket. The export is in `A1:D5`, and the minutes-open field is in column C.

| Ticket | Agent | Minutes Open | Priority |
| --- | --- | --- | --- |
| T-101 | Ana | 35 | High |
| T-102 | Ben | 80 | Low |
| T-103 | Ana | 55 | High |
| T-104 | Cy | 20 | Medium |

**Task:** Total the minutes-open values, using only the column that holds them.

**Solution:**

```excel
=SUM(CHOOSECOLS(A2:D5, 3))
```

**Answer:** `190`. The column holds 35, 80, 55 and 20, and those values add to 190.

### Problem 2: Latest Week of Store Sales

A chain tracks weekly sales in `A1:D4`. Store names are in column A, and the three most recent weeks are in columns B to D, with the latest week in column D.

| Store | Week 1 | Week 2 | Week 3 |
| --- | --- | --- | --- |
| Central | 500 | 620 | 580 |
| Harbor | 410 | 390 | 455 |
| Hilltop | 300 | 350 | 410 |

**Task:** Total the sales for the latest week only, without naming the column number.

**Solution:**

```excel
=SUM(CHOOSECOLS(A2:D4, -1))
```

**Answer:** `1445`. The latest week is column D, which holds 580, 455 and 410. Those values add to 1445.

## Use Cases

### Export Column Reordering

**Scenario:** A system exports customer records in a fixed order, but an upload template needs the ID, the email and the region in a different order.

```excel
=CHOOSECOLS(RawExport!A2:H500, 1, 4, 2, 8)
```

**Why It Works:** The formula returns the four fields in the template order without a manual cut and paste. If the export adds a column before these fields, the numbers shift, so check the header row after each new export.

### Report Column Selection

**Scenario:** A management summary needs the product name, the region and the most recent month from a 24-column sales table.

```excel
=CHOOSECOLS(SalesTable, 1, 3, -1)
```

**Why It Works:** The negative number -1 always returns the last column, so the report keeps the latest month even when older months are added to the left.

### Trimming Imported Data

**Scenario:** A bank export contains a long description column that the reconciliation sheet does not need. The sheet keeps the date, the reference and the amount.

```excel
=CHOOSECOLS(BankImport, 1, 2, 5)
```

**Why It Works:** The three needed columns return as one array and the unused description column is left out. Use DROP instead when the export has only one unwanted column at the end.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | A column number is 0, or its absolute value is larger than the number of columns. | Check the column count and the sign of each number. |
| Wrong columns | The export changed and the numbers now point at other fields. | Check the header row after each export, or move to a formula that finds columns by header. |
| `#SPILL!` | The cells below or to the right of the formula already hold data. | Clear the blocked cells, or move the formula to an empty area. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows, Mac and web), Excel 2024 (Windows and Mac) | Returns an array that spills in Excel 365. Negative numbers count from the last column. |
| Google Sheets | Available, in the Array category | Same arguments. The page does not describe the error behavior. |

## Tips and Best Practices

- Use CHOOSECOLS to keep a few columns and DROP to remove a few.
- Use negative numbers for the last columns of a table that is still growing on the left.
- Check the header row against the column numbers each time the source changes.
- Leave empty space below and to the right of the formula so the array can spill.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSEROWS](CHOOSEROWS.md) | Picks rows by number, the row counterpart of this function. |
| [DROP](DROP.md) | Removes rows or columns from the start or end, which suits removing a few columns. |
| [FILTER](FILTER.md) | Keeps rows that match a condition. Combine it with CHOOSECOLS to filter rows and pick columns. |
| [TAKE](TAKE.md) | Keeps the first or last rows or columns of an array. |
| [TRANSPOSE](TRANSPOSE.md) | Swaps rows and columns, which is useful when the columns need to become rows. |

## Official Documentation

- [Microsoft Support: CHOOSECOLS function](https://support.microsoft.com/en-us/excel/functions/choosecols-function)
- [Google Docs Editors Help: CHOOSECOLS](https://support.google.com/docs/answer/13197914)
