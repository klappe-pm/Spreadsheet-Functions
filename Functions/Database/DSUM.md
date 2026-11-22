---
domain: Spreadsheet Functions
category: Database
subcategory: Database Aggregation
purpose:
  - Aggregation
  - Database Queries
use-case:
  - Accounts Receivable Totals
  - Regional Sales Totals
  - Unit Sales by Product
related:
  - DAVERAGE
  - DCOUNT
  - DGET
  - FILTER
  - SUMIFS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/dsum-function
  - https://support.google.com/docs/answer/3094281
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Sum
  - Sum With Criteria Range
tags:
  - database
  - excel
  - sheets
---

# DSUM

## Description

**DSUM** adds the numbers in one column (the field) of a list or table, counting only the records (rows) that match the conditions in a separate criteria range. It treats your data like a small database: the first row holds field names, every row below it is a record, and the criteria range describes which records to include.

Use DSUM when the conditions themselves should live on the sheet where people can change them. A manager can type a different region or a new minimum amount into the criteria cells and every DSUM that points at them recalculates. The criteria range also supports OR logic (several criteria rows) and AND logic (several criteria columns) without nesting functions.

For most new work, SUMIFS is simpler because the conditions sit inside the formula and no criteria block is needed. DSUM is still the better fit when you need OR conditions across rows, when non-technical users maintain the criteria, or when you inherit workbooks built around criteria ranges. In Excel, a plain text criterion such as `East` matches every value that begins with East; use `="=East"` in the criteria cell for an exact match.

## Syntax

```excel
=DSUM(database, field, criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DSUM.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:D7`. Each column needs a label in the first row. |
| `field` | Yes | The column to add: a header label in quotes (`"Sales"`), a cell that contains the label, or the column position as a number (`4` for the fourth column). |
| `criteria` | Yes | A range with at least one header label and one condition cell below it. Labels must match the database headers. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A number: the sum of the field values in matching records. It returns 0 when no record matches and `#VALUE!` when the field label does not exist in the database.

## Examples

All examples use this sales list in `A1:D7`.

| Region | Rep | Product | Sales |
| --- | --- | --- | --- |
| East | Avery | Widgets | 1200 |
| West | Blake | Gadgets | 850 |
| East | Casey | Gadgets | 640 |
| North | Drew | Widgets | 975 |
| East | Avery | Gadgets | 410 |
| West | Emery | Widgets | 1530 |

### Example 1: One Condition

Criteria in `F1:F2`: `Region` above `East`.

```excel
=DSUM(A1:D7, "Sales", F1:F2)
```

**Result:** `2250`

The three East records (1200, 640 and 410) are added.

### Example 2: Two Conditions With AND Logic

Criteria in `F1:G2`: `Region` and `Product` side by side, with `East` and `Gadgets` on the same row.

```excel
=DSUM(A1:D7, "Sales", F1:G2)
```

**Result:** `1050`

Only records that are both East and Gadgets qualify (640 and 410).

<!-- Image 2: AND Versus OR Criteria Layouts. See Images/Database/DSUM.md -->

### Example 3: Two Conditions With OR Logic

Criteria in `F1:F3`: `Region` above `East` and then `West` on the next row.

```excel
=DSUM(A1:D7, "Sales", F1:F3)
```

**Result:** `4630`

Each criteria row is a separate test, so East (2250) and West (850 + 1530) are both included.

### Example 4: A Numeric Comparison

Criteria in `F1:F2`: `Sales` above `>1000`.

```excel
=DSUM(A1:D7, "Sales", F1:F2)
```

**Result:** `2730`

Comparison operators work in criteria cells; only 1200 and 1530 are above 1000.

### Example 5: Field by Column Number

```excel
=DSUM(A1:D7, 4, F1:F2)
```

**Result:** `2250` (with the Example 1 criteria)

The number 4 points at the fourth column, Sales. A label is safer because it survives inserted columns.

## Story Problems

### Problem 1: Bagels Sold This Week

A bakery logs units sold per product per day in `A1:C7`.

| Product | Day | Units |
| --- | --- | --- |
| Bagel | Mon | 40 |
| Muffin | Mon | 25 |
| Bagel | Tue | 35 |
| Scone | Tue | 18 |
| Bagel | Wed | 42 |
| Muffin | Wed | 30 |

**Task:** Put `Product` in `E1` and `Bagel` in `E2`, then total the bagels sold.

**Solution:**

```excel
=DSUM(A1:C7, "Units", E1:E2)
```

**Answer:** `117`, because 40 + 35 + 42 = 117.

### Problem 2: Large Unpaid Invoices

A freelancer tracks invoices in `A1:C6` and wants the total of unpaid invoices of 500 or more.

| Client | Status | Amount |
| --- | --- | --- |
| Acme | Paid | 1200 |
| Birch | Unpaid | 450 |
| Cedar | Unpaid | 800 |
| Acme | Unpaid | 650 |
| Dune | Paid | 300 |

**Task:** Build a criteria range in `E1:F2` with `Status` and `Amount` as labels and `Unpaid` and `>=500` below them, then sum the matching amounts.

**Solution:**

```excel
=DSUM(A1:C6, "Amount", E1:F2)
```

**Answer:** `1450`. Cedar (800) and Acme (650) are unpaid and at least 500; Birch is unpaid but below the threshold.

## Use Cases

### Self Service Sales Dashboard

**Scenario:** Regional managers pick a region and product line from drop-downs placed in a criteria block at the top of a report.

```excel
=DSUM(SalesData, "Revenue", Criteria)
```

**Why It Works:** The named range `Criteria` holds the drop-down cells, so managers change the question without touching the formula.

### OR Conditions Without Nesting

**Scenario:** Finance needs total spend for three cost centers at once.

```excel
=DSUM(Expenses, "Amount", H1:H4)
```

**Why It Works:** `H1` holds the `CostCenter` label and `H2:H4` hold the three codes. SUMIFS would need three SUMIFS added together or an array constant.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | The field label is misspelled or not in the header row. | Match the header text exactly, or use the column number. |
| Unexpected total | A blank row in the criteria range matches every record. | Size the criteria range to the filled rows only. |
| Unexpected total | A text criterion such as `East` also matches `Eastern`. | Use `="=East"` in the criteria cell for an exact match. |
| `0` | Criteria labels do not match database headers. | Copy the header cells into the criteria range. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Criteria accept wildcards (`*`, `?`) and comparison operators. |
| Google Sheets | Available | Same arguments; criteria ranges follow the same AND by column, OR by row layout. |

## Tips and Best Practices

- Keep the criteria range away from the data (above it or on another sheet) so it is not filtered or sorted with the list.
- Format the data as a table or a named range so the database argument grows with new rows.
- Use field labels rather than column numbers so inserted columns do not break formulas.
- Prefer SUMIFS for fixed conditions written by formula builders; prefer DSUM when users edit conditions on the sheet.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Conditional sum with criteria inside the formula. |
| [DAVERAGE](DAVERAGE.md) | Averages the field for matching records. |
| [DCOUNT](DCOUNT.md) | Counts numeric field values in matching records. |
| [DGET](DGET.md) | Returns the single value that matches the criteria. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the matching rows themselves; wrap in SUM for a total. |

## Official Documentation

- [Microsoft Support: DSUM function](https://support.microsoft.com/en-us/excel/functions/dsum-function)
- [Google Docs Editors Help: DSUM](https://support.google.com/docs/answer/3094281)
