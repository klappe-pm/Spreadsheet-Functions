---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Query and Filtering
purpose:
  - Aggregation
  - Data Retrieval
  - Sorting and Filtering
use-case:
  - Filtered Customer Lists
  - Regional Revenue Summaries
  - Top Performer Lists
related:
  - FILTER
  - GROUPBY
  - IFERROR
  - PIVOTBY
  - SORT
  - SUMIFS
level: 4
source:
  - https://support.google.com/docs/answer/3093343
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Google Sheets Query
  - GViz Query Language
  - SQL for Spreadsheets
tags:
  - aggregation
  - filtering
  - query-language
  - sheets
  - sql-like
---

# QUERY

## Description

**QUERY** runs a query written in the Google Visualization API Query Language against a range of data. The query language resembles SQL: a SELECT clause chooses columns, a WHERE clause filters rows, GROUP BY and PIVOT summarize data, and ORDER BY, LIMIT and OFFSET sort and trim the output. The result spills into the cells below and to the right of the formula.

Use QUERY when one formula should filter, sort, summarize and reshape data together. A single QUERY can replace a chain of FILTER, SORT and SUMIFS formulas and a helper column for each step. Because the query is text, a cell reference can change the filter by joining it into the query string.

QUERY is specific to Google Sheets. Microsoft Excel has no equivalent function, and the query language has no JOIN clause and no HAVING clause. Filter grouped results with a second QUERY or with FILTER instead. The clauses must appear in this order: SELECT, WHERE, GROUP BY, PIVOT, ORDER BY, LIMIT, OFFSET, LABEL, FORMAT and OPTIONS. Every clause is optional.

## Syntax

```excel
=QUERY(data, query, [headers])
```

<!-- Image 1: Query Clause Order. See Images/Google-specific/QUERY.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `data` | Yes | The range to query, such as `A1:D7` or a named range. Each column holds one type of value. If a column mixes types, the majority type is used and the other values are treated as blank. |
| `query` | Yes | The query text in quotation marks, or a cell that holds it. Columns are named by their position in `data`: A is the first column of the range, B the second, and so on. Text values in the query use single quotes. |
| `headers` | No | The number of header rows at the top of `data`. Omitted or `-1` means Sheets guesses the count from the data. Use `0` when there is no header row, or a positive number to state the count. |

### Return Value

A table of values that spills into the cells beside the formula. When `headers` is 1 or more, the first output row contains column labels. When no rows match the query, the formula returns no data, so wrap it in IFERROR to show a message instead.

## Examples

All examples use this sales list in `A1:D7`, with headers in row 1.

| Rep | Region | Product | Revenue |
| --- | --- | --- | --- |
| Ana | North | Desk | 450 |
| Ben | South | Chair | 120 |
| Cara | North | Chair | 310 |
| Dev | West | Desk | 600 |
| Eli | South | Desk | 280 |
| Fay | North | Lamp | 90 |

### Example 1: Select Columns and Filter Rows

```excel
=QUERY(A1:D7, "select A, C, D where D > 200", 1)
```

**Result:** A header row (Rep, Product, Revenue) followed by Ana Desk 450, Cara Chair 310, Dev Desk 600 and Eli Desk 280.

Column letters in the query refer to positions in `A1:D7`. The WHERE clause keeps only rows with revenue above 200.

### Example 2: Group and Sum

```excel
=QUERY(A1:D7, "select B, sum(D) where C = 'Desk' group by B", 1)
```

**Result:** North 450, South 280 and West 600, with a header row above them.

The WHERE clause keeps only desk sales, and GROUP BY adds the revenue for each region.

<!-- Image 2: Grouped Output Example. See Images/Google-specific/QUERY.md -->

### Example 3: Top Two by Revenue

```excel
=QUERY(A1:D7, "select A, D order by D desc limit 2", 1)
```

**Result:** Dev 600 and Ana 450, with a header row above them.

ORDER BY sorts the rows from largest to smallest, and LIMIT keeps only the first two.

### Example 4: Filter With a Cell Reference

```excel
=QUERY(A1:D7, "select A, D where B = '"&F1&"'", 1)
```

**Result:** Ana 450, Cara 310 and Fay 90 when `F1` holds North.

The ampersand joins the value in F1 into the query text. Text values need single quotes around them inside the query.

### Example 5: Pivot Revenue by Product

```excel
=QUERY(A1:D7, "select B, sum(D) group by B pivot C", 1)
```

**Result:** A header row with Region, Chair, Desk and Lamp. North shows 310, 450 and 90. South shows 120 and 280 with a blank under Lamp. West shows 600 under Desk and blanks elsewhere.

PIVOT turns each product into its own column, with the summed revenue at each intersection.

### Example 6: Rename Output Columns

```excel
=QUERY(A1:D7, "select A, D where D >= 300 order by D desc label A 'Rep', D 'Revenue'", 1)
```

**Result:** Dev 600, Ana 450 and Cara 310, with the header row reading Rep and Revenue.

LABEL changes the column headings in the output without changing the source data.

## Story Problems

### Problem 1: Large Event Attendance

An events team lists its events in `A1:C6`, with the attendee count in column C.

| Event | Venue | Attendees |
| --- | --- | --- |
| Launch | Hall A | 240 |
| Workshop | Room 2 | 35 |
| Summit | Hall B | 510 |
| Training | Room 4 | 90 |
| Expo | Hall A | 180 |

**Task:** Build one formula that lists the event names and attendee counts for events with more than 100 attendees, largest first.

**Solution:**

```excel
=QUERY(A1:C6, "select A, C where C > 100 order by C desc", 1)
```

**Answer:** Summit with 510, Launch with 240 and Expo with 180. Workshop and Training are excluded because they have 100 or fewer attendees.

<!-- Image 3: Attendance Story Result. See Images/Google-specific/QUERY.md -->

### Problem 2: Spending by Category

A small firm records each expense in `A1:C6` with the category in column A and the amount in column C.

| Category | Month | Amount |
| --- | --- | --- |
| Office | Jan | 300 |
| Travel | Jan | 150 |
| Office | Feb | 220 |
| Travel | Feb | 90 |
| Office | Jan | 75 |

**Task:** Build one formula that totals the amount for each category, largest total first.

**Solution:**

```excel
=QUERY(A1:C6, "select A, sum(C) group by A order by sum(C) desc", 1)
```

**Answer:** Office with a total of 595 and Travel with a total of 240. Office is 300 plus 220 plus 75, and Travel is 150 plus 90.

## Use Cases

### Filtered Customer Lists

**Scenario:** A sales lead picks a region from a drop-down in `H1`, and the sheet lists the matching customers.

```excel
=QUERY(Customers!A1:D, "select A, B, D where C = '"&$H$1&"'", 1)
```

**Why It Works:** The query text is rebuilt from `H1` each time the drop-down changes. The formula reads the same range in every case, so the list updates without edits.

### Regional Revenue Summaries

**Scenario:** A finance team needs revenue totals by region, sorted from largest to smallest, for a monthly review.

```excel
=QUERY(Sales!A1:D, "select B, sum(D) group by B order by sum(D) desc", 1)
```

**Why It Works:** One formula groups and sorts the data. Adding rows to the source range updates the summary when the range covers them.

### Top Performer Lists

**Scenario:** A regional manager wants the ten highest sellers on a dashboard tab.

```excel
=QUERY(Reps!A1:D, "select A, D order by D desc limit 10", 1)
```

**Why It Works:** ORDER BY ranks the rows by revenue and LIMIT keeps the first ten, which avoids a separate sort step.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unable to parse query string | The query has a typo, a missing quote, or a clause out of order. | Check the keywords and quotes, and keep the clauses in the order SELECT, WHERE, GROUP BY, PIVOT, ORDER BY. |
| No data is returned | No rows match the WHERE clause. | Relax the condition or wrap the formula in IFERROR with a message. |
| Wrong column is used | The query refers to a letter beyond the last column of the range. | Use the letters that match the positions in `data`, starting with A. |
| Headers appear in the results or are missing | The `headers` argument does not match the range. | Set `headers` to the number of header rows, or 0 when there are none. |
| Values are blank in a column | The column mixes types, and the minority type is treated as blank. | Clean the column so that every value has the same type. |
| Cell reference breaks the query | The cell value was not joined with quotes around text. | Use `'"&A1&"'` for text and `"&A1&"` for numbers. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available | Use FILTER with SORT for row selection, GROUPBY or PIVOTBY for summaries, or a PivotTable. |
| Google Sheets | Available | Uses the Google Visualization API Query Language, with SELECT, WHERE, GROUP BY, PIVOT, ORDER BY, LIMIT, OFFSET, LABEL, FORMAT and OPTIONS clauses. |

## Tips and Best Practices

- Start with `select *` to confirm the range is correct, then add WHERE, GROUP BY and ORDER BY one at a time.
- Put the headers count in the third argument so the first row is never read as data.
- Use single quotes around text values in the query and no quotes around numbers.
- Use `ARRAYFORMULA` or the `Col1` form when the data comes from another function such as IMPORTRANGE, because the identifiers then refer to the array rather than to sheet columns.
- Filter grouped results with a second QUERY or with FILTER, because the query language has no HAVING clause.
- When PIVOT is used, ORDER BY cannot sort by an aggregated column, so sort the output with SORT if needed.
- Use a named range or a bounded range such as `A1:D500` instead of whole columns to keep large queries fast.

## Related Functions

| Function | Relationship |
| --- | --- |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns matching rows without grouping or sorting in one step. |
| [SORT](../Lookup%20%26%20Reference/SORT.md) | Sorts a range by one or more columns. |
| [GROUPBY](../Lookup%20%26%20Reference/GROUPBY.md) | Groups rows and summarizes them, similar to GROUP BY. |
| [PIVOTBY](../Lookup%20%26%20Reference/PIVOTBY.md) | Builds a cross-tab summary, similar to PIVOT. |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Sums values that meet several conditions, without the query language. |
| [IFERROR](../Logical/IFERROR.md) | Replaces the error or empty result with a message. |

## Official Documentation

- [Google Docs Editors Help: QUERY](https://support.google.com/docs/answer/3093343)
- [Google Visualization API Query Language Reference](https://developers.google.com/chart/interactive/docs/querylanguage)
