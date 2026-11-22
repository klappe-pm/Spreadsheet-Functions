---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Grouping and Pivoting
purpose:
  - Aggregation
  - Array Shaping
  - Sorting and Filtering
use-case:
  - Average Resolution Hours
  - Billable Hours Summary
  - Regional Revenue Matrix
related:
  - FILTER
  - GROUPBY
  - QUERY
  - SORTBY
  - SUMIFS
  - UNIQUE
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/pivotby-function
date-created: 2026-11-22
date-revised: 2026-11-22
aliases:
  - Dynamic Pivot Table
  - Pivot Summary
tags:
  - aggregation
  - dynamic-array
  - excel
  - pivot
---

# PIVOTBY

## Description

**PIVOTBY** builds a summary table from a list. It groups the rows by one or more row fields, groups the columns by one or more column fields, and calculates a summary of the values at each intersection. The result is a live formula that spills into the cells below and to the right, so it updates when the source data changes. It takes the place of a pivot table for users who want the summary to be a formula.

Each field is a column or a range of columns from the same list, and every one of them must have the same number of rows. The function argument decides how each group is summarized. SUM, AVERAGE and COUNT are common choices, and a custom lambda can calculate a result from each group. Totals, headers, sort order and an optional filter are controlled by the optional arguments, which are positional, so an empty argument is written as a comma with nothing between.

PIVOTBY is part of Microsoft 365 and is also available in Excel 2024 and Excel 2021 on Windows and Mac. Excel 2019, Excel 2016 and earlier versions do not include it. Google Sheets does not have a PIVOTBY function, and the closest alternative is listed in the Platform Differences section.

## Syntax

```excel
=PIVOTBY(row_fields, col_fields, values, function, [field_headers], [row_total_depth], [row_sort_order], [col_total_depth], [col_sort_order], [filter_array], [relative_to])
```

<!-- Image 1: PIVOTBY Argument Order. See Images/Lookup & Reference/PIVOTBY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `row_fields` | Yes | The column or columns that group the rows. Several columns create nested row groups. |
| `col_fields` | Yes | The column or columns that group the columns. Several columns create nested column groups. |
| `values` | Yes | The column or columns to summarize. Several columns create several calculated columns. |
| `function` | Yes | The function or lambda that summarizes each group, such as SUM, AVERAGE or COUNT. |
| `field_headers` | No | `0` gives no headers. `1` turns headers on but does not show them. `2` does not show headers but generates them. `3` turns headers on and shows them. When omitted, the setting is automatic. |
| `row_total_depth` | No | `0` shows no row totals, `1` shows grand totals, and `2` shows grand totals and subtotals. Use `-1` or `-2` to place totals at the top. When omitted, grand totals and subtotals are shown where possible. |
| `row_sort_order` | No | A column number counted across `row_fields` and then `values`. A negative number sorts in descending order. |
| `col_total_depth` | No | The same options as `row_total_depth`, applied to the column groups. |
| `col_sort_order` | No | A column number counted across `col_fields` and then `values`. A negative number sorts in descending order. |
| `filter_array` | No | A single column of TRUE and FALSE values, one for each row of the data. Only rows marked TRUE are summarized. Its length must match `row_fields` and `col_fields`. |
| `relative_to` | No | Used only when the function takes two arguments, such as PERCENTOF. `0` uses column totals, `1` row totals, `2` grand totals, `3` the parent column total and `4` the parent row total. |

### Return Value

A spilled summary table. It holds one row for each group in `row_fields` and one column for each group in `col_fields`, plus any totals and headers chosen by the optional arguments. Its size depends on the number of distinct groups in the data. The function returns the summary as a dynamic array, so the cells below and to the right of the formula must be empty for it to spill.

## Examples

All examples use this list of unit sales in `A1:D9`. The Region column is `A`, the Product column is `B`, the Quarter column is `C`, and the Units column is `D`.

| Region | Product | Quarter | Units |
| --- | --- | --- | --- |
| North | Pens | Q1 | 10 |
| North | Mugs | Q1 | 5 |
| North | Pens | Q2 | 8 |
| South | Pens | Q1 | 7 |
| South | Mugs | Q2 | 4 |
| South | Pens | Q2 | 6 |
| West | Mugs | Q1 | 3 |
| West | Pens | Q2 | 9 |

### Example 1: Units by Region and Quarter

```excel
=PIVOTBY(A2:A9, C2:C9, D2:D9, SUM, 3)
```

**Result:** North has 15 in Q1 and 8 in Q2, a total of 23. South has 7 in Q1 and 10 in Q2, a total of 17. West has 3 in Q1 and 9 in Q2, a total of 12. The grand totals are 25 for Q1, 27 for Q2 and 52 overall.

The `3` in the fifth argument turns on the headers, so the group names appear above and beside the figures.

### Example 2: Nested Row Groups

```excel
=PIVOTBY(A2:B9, C2:C9, D2:D9, SUM, 3)
```

**Result:** North Pens has 10 in Q1 and 8 in Q2, a total of 18. North Mugs has 5 in Q1 and no Q2 entry. South Pens has 7 in Q1 and 6 in Q2, a total of 13. South Mugs has 4 in Q2. West Pens has 9 in Q2, and West Mugs has 3 in Q1.

Two row fields, Region and Product, create a group for each region and product pair. The totals match Example 1 when the Region groups are added together.

<!-- Image 2: Nested Row Grid. See Images/Lookup & Reference/PIVOTBY.md -->

### Example 3: Average Instead of Total

```excel
=PIVOTBY(A2:A9, C2:C9, D2:D9, AVERAGE, 3)
```

**Result:** North averages 7.5 in Q1 and 8 in Q2. South averages 7 in Q1 and 5 in Q2. West averages 3 in Q1 and 9 in Q2.

Only the function changes. North's Q1 average is (10 + 5) / 2 = 7.5, because two entries fall in that cell.

### Example 4: Regions Sorted by Total Units

```excel
=PIVOTBY(A2:A9, C2:C9, D2:D9, SUM,,, -2)
```

**Result:** North first with 23 units, then South with 17, then West with 12.

The `-2` in the seventh argument sorts the rows by the second column counted from the row field, which is the Units total, in descending order. Empty arguments are written as commas so the seventh argument lines up.

### Example 5: Filtering Out One Region

```excel
=PIVOTBY(A2:A9, C2:C9, D2:D9, SUM, 3, , , , , A2:A9<>"West")
```

**Result:** North has 15 in Q1 and 8 in Q2. South has 7 in Q1 and 10 in Q2. The totals are 22 for Q1, 18 for Q2 and 40 overall.

The filter array is TRUE for every row that is not West, so West is left out of every group and every total.

## Story Problems

### Problem 1: Team Hours by Week

A project lead tracks hours for three teams across two weeks in `A1:C7`. The headings are in row 1.

| Team | Week | Hours |
| --- | --- | --- |
| Ops | W1 | 30 |
| Ops | W2 | 34 |
| Sales | W1 | 22 |
| Sales | W2 | 18 |
| Dev | W1 | 40 |
| Dev | W2 | 36 |

**Task:** Summarize the hours with teams as rows and weeks as columns, including totals.

**Solution:**

```excel
=PIVOTBY(A2:A7, B2:B7, C2:C7, SUM, 3)
```

**Answer:** The grand total is 180 hours. Dev has 76 hours, Ops has 64 and Sales has 40. Week 1 totals 92 hours and Week 2 totals 88.

<!-- Image 3: Team Hours Result. See Images/Lookup & Reference/PIVOTBY.md -->

### Problem 2: Billable Hours Only

The same hours list has a Billable column in `D2:D7`, where Yes marks billable time and No marks time that is not billed.

| Team | Week | Hours | Billable |
| --- | --- | --- | --- |
| Ops | W1 | 30 | Yes |
| Ops | W2 | 34 | No |
| Sales | W1 | 22 | Yes |
| Sales | W2 | 18 | Yes |
| Dev | W1 | 40 | No |
| Dev | W2 | 36 | Yes |

**Task:** Summarize only the billable hours with teams as rows and weeks as columns.

**Solution:**

```excel
=PIVOTBY(A2:A7, B2:B7, C2:C7, SUM, 3, , , , , D2:D7="Yes")
```

**Answer:** The billable total is 106 hours. Week 1 has 52 billable hours (30 for Ops and 22 for Sales), and Week 2 has 54 (18 for Sales and 36 for Dev).

## Use Cases

### Regional Revenue Matrix

**Scenario:** A regional manager wants a one-page summary of revenue by region and quarter, with the largest region listed first and a grand total at the bottom. The source list receives new rows each month.

```excel
=PIVOTBY(RegionList, QuarterList, RevenueList, SUM, 3, 1, -2)
```

**Why It Works:** The region names become the rows, sorted by the second column, which holds the revenue totals, in descending order. The `1` in the sixth argument adds grand totals and no subtotals. Because the summary is a formula, it recalculates whenever the named lists change, and no refresh is needed.

### Average Resolution Hours by Team

**Scenario:** A support lead needs the average hours taken to resolve tickets for each team at each priority level.

```excel
=PIVOTBY(TeamList, PriorityList, HoursList, AVERAGE, 3)
```

**Why It Works:** Each team and priority pair is a group, and AVERAGE is applied to the hours in each group. The fields must have the same number of rows, so the team, priority and hours lists should come from the same table.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#NAME?` | The workbook is open in Excel 2019 or earlier, which does not include PIVOTBY. | Open the file in Microsoft 365, Excel 2024 or Excel 2021. |
| `#SPILL!` | Cells below or to the right of the formula contain data, so the summary cannot spread. | Clear the blocking cells or move the formula to an empty area. |
| Wrong length | `filter_array` does not have the same number of rows as `row_fields` and `col_fields`. | Build the filter from the same rows as the fields. |
| Unexpected layout | Headers are showing or hiding when not wanted. | Set `field_headers` explicitly to `0`, `1`, `2` or `3`. |
| Wrong order | `row_sort_order` or `col_sort_order` points at the wrong column number. | Count the row or column fields first, then the values, and use a negative number for descending order. |
| Missing totals | `row_total_depth` or `col_total_depth` is set to `0`. | Use `1` for grand totals or leave the argument blank. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365 (Windows and Mac), Excel 2024 (Windows and Mac) and Excel 2021 (Windows and Mac) | Returns a dynamic array. Not available in Excel 2019, Excel 2016 or earlier versions. |
| Google Sheets | Not available | No PIVOTBY function. The closest alternative is QUERY with `group by` and `pivot` clauses, which is in this library. Google Sheets also offers pivot tables from the Data menu. |

## Tips and Best Practices

- Set `field_headers` to `3` in every formula so the output looks the same on every workbook.
- Use `row_total_depth` and `col_total_depth` with `0` when the summary feeds another calculation and extra totals would get in the way.
- Keep the source list in an Excel Table or a named range, so the summary follows the data as rows are added.
- Use a filter array rather than deleting rows when a summary should exclude some data but keep the source complete.
- Use SUMIFS when only one total is needed, because it is simpler than a full summary table.

## Related Functions

| Function | Relationship |
| --- | --- |
| [GROUPBY](GROUPBY.md) | Groups and summarizes rows without the column grouping that PIVOTBY adds. |
| [FILTER](FILTER.md) | Returns the rows that meet a condition, which can be used before a summary. |
| [SORTBY](SORTBY.md) | Sorts an array by another array, for use before or after a summary. |
| [UNIQUE](UNIQUE.md) | Lists the distinct values in a field, which is useful for building headings. |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Totals one cell at a time with conditions in the formula, which is simpler for a single figure. |
| [QUERY](../Google-specific/QUERY.md) | The closest Google Sheets alternative, using `group by` and `pivot` clauses. |

## Official Documentation

- [Microsoft Support: PIVOTBY function](https://support.microsoft.com/en-us/excel/functions/pivotby-function)
