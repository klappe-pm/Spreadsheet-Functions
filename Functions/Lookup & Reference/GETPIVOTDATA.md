---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Grouping and Pivoting
purpose:
  - Aggregation
  - Data Retrieval
use-case:
  - Membership Plan Report
  - Nursery Stock Report
related:
  - GROUPBY
  - INDEX
  - MATCH
  - PIVOTBY
  - QUERY
  - SUMIFS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/getpivotdata-function
  - https://support.google.com/docs/answer/6167538
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Pivot Lookup
tags:
  - excel
  - pivot-table
  - reference
  - sheets
---

# GETPIVOTDATA

## Description

**GETPIVOTDATA** extracts a summarized value from a PivotTable (Excel) or pivot table (Google Sheets) by naming the data field and the row and column items you want. It reads the value the pivot table shows, so the formula stays correct when the pivot is moved, resized or re-sorted. A plain cell reference such as `=F7` breaks as soon as the layout changes.

When you click a cell inside an Excel PivotTable and type an operator such as `=` and then a cell in the pivot, Excel writes a GETPIVOTDATA formula for you. You can turn that automatic behavior off in the PivotTable Options settings. Write the formula yourself when you need a value that a report summarizes in a fixed place.

GETPIVOTDATA only returns values that appear in the pivot table. A combination of items that has no data, or an item that is filtered out, produces an error. Use SUMIFS on the source data when you need a total that does not depend on the pivot layout.

## Syntax

```excel
=GETPIVOTDATA(data_field, pivot_table, [field1, item1, field2, item2], ...)
```

<!-- Image 1: Pivot Table Anchor Cell. See Images/Lookup & Reference/GETPIVOTDATA.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `data_field` | Yes | The value field to return, in quotes. Both the full name, such as `"Sum of Sales"`, and the root name, such as `"Sales"`, work in Excel. |
| `pivot_table` | Yes | A reference to any cell inside the PivotTable. The top-left corner is a common choice. |
| `field1, item1, ...` | No | Up to 126 pairs of a field name and an item. Pairs can appear in any order. Use curly braces such as `{"Mar", "Apr"}` to include several items for one field. |

<!-- Image 3: Field and Item Pairs. See Images/Lookup & Reference/GETPIVOTDATA.md -->

### Return Value

The value shown in the pivot table for the chosen data field and items. It can be a number, text, an error or blank, depending on what the pivot shows. It returns `#REF!` in Excel when the pivot reference is not a PivotTable, a field or item does not match a visible field, or the combination has no data.

## Examples

The examples use this sales list in `A1:C7`, which is summarized in a PivotTable anchored at `F3`. Regions are the rows and quarters are the columns, and the values are the sum of Sales.

| Region | Quarter | Sales |
| --- | --- | --- |
| East | Q1 | 400 |
| East | Q2 | 550 |
| West | Q1 | 300 |
| West | Q2 | 620 |
| North | Q1 | 210 |
| North | Q2 | 175 |

### Example 1: Return the Grand Total

```excel
=GETPIVOTDATA("Sales", $F$3)
```

**Result:** `2255`

With no field and item pairs, the function returns the grand total that the pivot table shows for Sales.

### Example 2: Return One Row Total

```excel
=GETPIVOTDATA("Sales", $F$3, "Region", "East")
```

**Result:** `950`

East totals 400 in Q1 and 550 in Q2. The pivot shows that row total, and the formula reads it directly.

### Example 3: Return One Cell From Two Fields

```excel
=GETPIVOTDATA("Sales", $F$3, "Region", "West", "Quarter", "Q2")
```

**Result:** `620`

This returns the single intersection of the West row and the Q2 column.

### Example 4: Use a Cell as the Item

```excel
=GETPIVOTDATA("Sales", $F$3, "Region", $H$2)
```

**Result:** `385` when `H2` contains `North`

Typing the region name in `H2` lets people choose a different region without changing the formula.

### Example 5: Handle an Item That Is Not in the Pivot

```excel
=IFERROR(GETPIVOTDATA("Sales", $F$3, "Region", "South"), "No South data")
```

**Result:** `No South data`

The pivot has no South row, so GETPIVOTDATA returns an error. IFERROR shows a message instead.

## Story Problems

### Problem 1: Herbs in April

A nursery records units sold by category and month in `A1:C7`. A PivotTable anchored at `G3` sums the units.

| Category | Month | Units |
| --- | --- | --- |
| Herbs | Mar | 40 |
| Herbs | Apr | 55 |
| Shrubs | Mar | 25 |
| Shrubs | Apr | 30 |
| Herbs | Apr | 15 |
| Shrubs | Mar | 10 |

**Task:** Return the number of herb units sold in April from the pivot table.

**Solution:**

```excel
=GETPIVOTDATA("Units", $G$3, "Category", "Herbs", "Month", "Apr")
```

**Answer:** `70`. The two April herb rows, 55 and 15, add up to 70.

### Problem 2: Standard Members in Riverside

A gym keeps membership counts by plan and city. The PivotTable is anchored at `F3`, with plans in the rows and cities in the columns.

| Plan | City | Members |
| --- | --- | --- |
| Standard | Riverside | 120 |
| Premium | Riverside | 45 |
| Standard | Hillcrest | 90 |
| Premium | Hillcrest | 60 |
| Standard | Riverside | 30 |

**Task:** Return the number of Standard members in Riverside.

**Solution:**

```excel
=GETPIVOTDATA("Members", $F$3, "Plan", "Standard", "City", "Riverside")
```

**Answer:** `150`, because 120 and 30 are the two Standard rows for Riverside.

<!-- Image 2: Story Problem Pivot Result. See Images/Lookup & Reference/GETPIVOTDATA.md -->

## Use Cases

### Nursery Stock Report

**Scenario:** A monthly report shows a headline number for each category, and the figures must stay correct when the pivot is refreshed with new sales.

```excel
=GETPIVOTDATA("Units", $G$3, "Category", $B$20, "Month", $B$21)
```

**Why It Works:** The category and month come from cells, so the same formula feeds each line of the report. The pivot does the aggregation, and the formula only picks the value.

### Membership Plan Report

**Scenario:** A regional manager wants a dashboard that pulls the member count for a chosen plan and city from a pivot that the operations team refreshes every week.

```excel
=IFERROR(GETPIVOTDATA("Members", $F$3, "Plan", $H$2, "City", $H$3), 0)
```

**Why It Works:** Plan and city are read from input cells. A combination with no members returns 0 instead of an error, so the dashboard stays clean.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#REF!` | The field or item name does not match a visible item in the pivot. | Match the spelling and case of the item, and remove any filter that hides it. |
| `#REF!` | The pivot reference points to a cell that is not in a PivotTable. | Pass a cell inside the pivot, such as the top-left corner. |
| `#REF!` | The pivot shrank after a refresh and the referenced cell is no longer in it. | Point the formula at a cell that still lies inside the pivot. |
| `#REF!` | The combination of items has no data, such as a product and salesperson pair with no sales. | Wrap the formula in IFERROR, or check that the pair exists in the pivot. |
| Error (Google Sheets) | The value is not shown in the pivot table. | Display the value in the pivot table before the formula reads it. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel versions that support PivotTables | Accepts the root field name, such as `"Sales"`, or the full name, such as `"Sum of Sales"`. Uses field and item pairs in any order. Returns `#REF!` for unmatched arguments. |
| Google Sheets | Available | Syntax is `GETPIVOTDATA(value_name, any_pivot_table_cell, [original_column, ...], [pivot_item, ...])`. The value name must match the header shown in the table, such as `"SUM of Sales"`. Column names come from the source data. |

## Tips and Best Practices

- Anchor the formula to the top-left cell of the pivot, which stays in place when the pivot is refreshed.
- Put field names and items in cells rather than in the formula when people need to change the question.
- Copy the field and item names from the pivot table headers, because Google Sheets requires the exact text shown.
- Wrap the formula in IFERROR when an item might be missing, such as a new region with no sales yet.
- Use SUMIFS on the source data when a total must stay available even after the pivot is removed.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GROUPBY](../Lookup%20%26%20Reference/GROUPBY.md) | Builds a grouped summary with a formula, without a PivotTable. |
| [INDEX](../Lookup%20%26%20Reference/INDEX.md) | Returns a value from a fixed position, which breaks when the layout changes. |
| [MATCH](../Lookup%20%26%20Reference/MATCH.md) | Finds the position of a label, often used with INDEX on pivot output. |
| [PIVOTBY](../Lookup%20%26%20Reference/PIVOTBY.md) | Builds a pivot-style summary from a formula that can be read with other formulas. |
| [QUERY](../Google-specific/QUERY.md) | Groups and aggregates source data in Google Sheets with SQL-like syntax. |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Totals source rows that match conditions, without depending on pivot layout. |

## Official Documentation

- [Microsoft Support: GETPIVOTDATA function](https://support.microsoft.com/en-us/excel/functions/getpivotdata-function)
- [Google Docs Editors Help: GETPIVOTDATA](https://support.google.com/docs/answer/6167538)
