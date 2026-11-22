---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Grouping and Pivoting
purpose:
  - Aggregation
  - Array Shaping
use-case:
  - Project Hours Summary
  - Sales Deal Counts
  - Support Ticket Minutes
related:
  - FILTER
  - GETPIVOTDATA
  - PIVOTBY
  - QUERY
  - SORT
  - UNIQUE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/groupby-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Group By
tags:
  - aggregation
  - dynamic-array
  - excel
  - grouping
---

# GROUPBY

## Description

**GROUPBY** groups rows by one or more row fields, applies a calculation to a value column for each group, and returns the result as a dynamic array. It can also sort the output, show subtotals and grand totals, and filter the source rows before grouping. Use it when you want a summary table that updates with the source data, without building a PivotTable.

Each group becomes one output row. The function takes the row labels from the row fields and the calculated values from the values argument, using a function such as SUM, AVERAGE or COUNT. Because the output is an array, you can wrap it in other functions, such as TAKE to show only the top rows or CHOOSECOLS to reorder the columns.

GROUPBY is a newer Excel function that is available in Microsoft 365. Its help page lists no earlier Excel version, so use PivotTables or SUMIFS in older workbooks. No Google Sheets help page is listed for GROUPBY, so use QUERY with a GROUP BY clause as the closest alternative in Sheets.

## Syntax

```excel
=GROUPBY(row_fields, values, function, [field_headers], [total_depth], [sort_order], [filter_array], [field_relationship])
```

<!-- Image 1: GROUPBY Argument Layout. See Images/Lookup & Reference/GROUPBY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `row_fields` | Yes | A column of values, or several columns, used to group the rows and create the row headers. |
| `values` | Yes | The column or columns to aggregate. Several columns produce several aggregations. |
| `function` | Yes | The calculation to apply, such as `SUM`, `AVERAGE` or `COUNT`. A custom LAMBDA also works. |
| `field_headers` | No | `0` for no headers, `1` for headers that are hidden, `2` to generate headers, or `3` for headers that are shown. When omitted, Excel assumes headers exist if the first value is text and the second is a number. |
| `total_depth` | No | `0` for no totals, `1` for grand totals, `2` for grand totals and subtotals, and negative values to place totals at the top. When omitted, Excel shows grand totals and subtotals where possible. |
| `sort_order` | No | A column number to sort by. Row fields come first, then value columns, and a negative number sorts in descending order. |
| `filter_array` | No | A column of TRUE and FALSE values with the same height as the row fields. Only rows marked TRUE are grouped. |
| `field_relationship` | No | `0` for a hierarchy, where later columns sort within earlier ones, or `1` for a table, where each column sorts on its own. The default is `0`. |

### Return Value

A dynamic array with one row for each group, plus any subtotal or grand total rows that the `total_depth` setting requests. The columns hold the row labels followed by the calculated values. It returns `#SPILL!` when the cells below or beside the formula are not empty.

## Examples

The examples use this timesheet in `A1:C7`, with headers in row 1.

| Team | Project | Hours |
| --- | --- | --- |
| Ava | Alpha | 12 |
| Ben | Beta | 8 |
| Ava | Beta | 5 |
| Cy | Alpha | 9 |
| Ben | Alpha | 4 |
| Cy | Beta | 11 |

### Example 1: Total Hours by Person

```excel
=GROUPBY(A2:A7, C2:C7, SUM, 0, 0, 1)
```

**Result:** Ava 17, Ben 12 and Cy 20, in three rows.

Setting `field_headers` to 0 tells GROUPBY that the values start in row 2 with no header. Setting `total_depth` to 0 removes the total row, and the sort order `1` lists the people from A to Z.

### Example 2: Sort by Hours With a Grand Total

```excel
=GROUPBY(A2:A7, C2:C7, SUM, 0, 1, -2)
```

**Result:** Cy 20, Ava 17, Ben 12 and a total row of 49.

The sort order `-2` points to the second column, which is the hours column, and the minus sign sorts it from largest to smallest. The total depth of `1` adds the grand total.

<!-- Image 3: Sorted Summary With Grand Total. See Images/Lookup & Reference/GROUPBY.md -->

### Example 3: Group Only the Alpha Rows

```excel
=GROUPBY(A2:A7, C2:C7, SUM, 0, 0, 1, B2:B7="Alpha")
```

**Result:** Ava 12, Ben 4 and Cy 9, in three rows.

The `filter_array` argument keeps only the rows where the project is Alpha before the groups are calculated.

### Example 4: Average Hours per Person

```excel
=GROUPBY(A2:A7, C2:C7, AVERAGE, 0, 0, 1)
```

**Result:** Ava 8.5, Ben 6 and Cy 10.

Replacing SUM with AVERAGE changes the calculation for each group. Ava worked 12 and 5 hours, so the average is 8.5.

## Story Problems

### Problem 1: Support Minutes by Category

A help desk logs the minutes spent on each ticket in `A1:B7`.

| Category | Minutes |
| --- | --- |
| Billing | 35 |
| Login | 12 |
| Billing | 50 |
| Shipping | 25 |
| Login | 8 |
| Billing | 15 |

**Task:** Show the total minutes for each category, the largest first, with a grand total.

**Solution:**

```excel
=GROUPBY(A2:A7, B2:B7, SUM, 0, 1, -2)
```

**Answer:** Billing 100, Shipping 25 and Login 20, followed by a total of 145. Billing has three tickets totaling 35, 50 and 15 minutes.

### Problem 2: Deals Per Sales Rep

A sales manager lists each closed deal by rep in `A1:B6`.

| Rep | Deal Value |
| --- | --- |
| Priya | 4000 |
| Sam | 2500 |
| Priya | 1200 |
| Lee | 900 |
| Sam | 3100 |

**Task:** Count the deals for each rep, sorted by rep name from A to Z.

**Solution:**

```excel
=GROUPBY(A2:A6, B2:B6, COUNT, 0, 0, 1)
```

**Answer:** Lee 1, Priya 2 and Sam 2. Each rep appears once, and COUNT returns how many deal rows that rep has.

<!-- Image 2: Story Problem Grouped Output. See Images/Lookup & Reference/GROUPBY.md -->

## Use Cases

### Project Hours Summary

**Scenario:** A project manager wants a live list of hours per team member that refreshes whenever the timesheet changes.

```excel
=GROUPBY(Timesheet!A2:A500, Timesheet!C2:C500, SUM, 0, 1, -2)
```

**Why It Works:** GROUPBY regroups the full timesheet each time it recalculates, and the sort order keeps the heaviest workloads at the top. Adding rows to the timesheet extends the summary automatically.

### Sales Deal Counts

**Scenario:** A regional director needs deal counts for each stage of the pipeline, limited to the current quarter.

```excel
=GROUPBY(Deals!B2:B400, Deals!A2:A400, COUNT, 0, 0, 1, Deals!D2:D400=$H$1)
```

**Why It Works:** The `filter_array` keeps only the rows that match the quarter in `H1`, so one formula handles each quarter without helper columns.

### Support Ticket Minutes

**Scenario:** A support lead tracks time spent on each ticket category and needs a total that matches the report sent to finance.

```excel
=GROUPBY(Tickets!C2:C300, Tickets!D2:D300, SUM, 0, 1, -2)
```

**Why It Works:** The grand total row adds the time for every category, so the total always matches the detail rows above it.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#SPILL!` | Cells below or beside the formula contain data. | Clear the spill range or move the formula to an empty area. |
| Header row treated as data | `field_headers` is omitted and the first value looks like text. | Set `field_headers` to `0` or `3` to match the range. |
| Groups in the wrong order | `sort_order` is omitted, so the order is not the one you want. | Add a sort_order value, with a minus sign for descending. |
| Totals missing or unexpected | `total_depth` is omitted, so Excel chooses totals automatically. | Set `total_depth` to `0` for no totals or `1` for grand totals. |
| Values not grouped as expected | The row field and value range have different heights. | Use the same starting and ending rows for every range. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Excel for Microsoft 365, Microsoft Office and My Office for iPhone | The help page lists no other Excel version, so use a PivotTable or SUMIFS in earlier workbooks. |
| Google Sheets | Not available | Use QUERY with a GROUP BY clause for a similar grouped summary, or build a pivot table. |

## Tips and Best Practices

- Set `field_headers` and `total_depth` explicitly so the output does not change when the data is reshaped.
- Use a negative `sort_order` for descending results, such as the largest totals first.
- Keep the row fields and value columns the same height, because mismatched ranges do not group correctly.
- Wrap the call in TAKE to show only the top rows of a long summary.
- Use `filter_array` to apply a condition before grouping, which avoids a separate FILTER step.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the matching rows, which GROUPBY can also filter in one step. |
| [GETPIVOTDATA](GETPIVOTDATA.md) | Reads a value from a PivotTable, the older way to build the same summary. |
| [PIVOTBY](../Lookup%20%26%20Reference/PIVOTBY.md) | Builds a two-way summary with row and column headers. |
| [QUERY](../Google-specific/QUERY.md) | Provides grouping and aggregation in Google Sheets. |
| [SORT](../Lookup%20%26%20Reference/SORT.md) | Sorts an array that you have already built, when GROUPBY sort options are not enough. |
| [UNIQUE](../Lookup%20%26%20Reference/UNIQUE.md) | Lists each distinct group label without calculating totals. |

## Official Documentation

- [Microsoft Support: GROUPBY function](https://support.microsoft.com/en-us/excel/functions/groupby-function)
