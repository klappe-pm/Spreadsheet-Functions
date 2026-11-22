---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Dynamic Arrays
purpose:
  - Data Retrieval
  - Sorting and Filtering
use-case:
  - Expense Approval Queue
  - Open Ticket Lists
  - Overdue Library Fines
related:
  - CHOOSECOLS
  - QUERY
  - SORT
  - SUMIFS
  - UNIQUE
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/filter-function
  - https://support.google.com/docs/answer/3093197
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Array Filter
  - Conditional Filter
tags:
  - dynamic-array
  - excel
  - filtering
  - sheets
---

# FILTER

## Description

**FILTER** returns the rows or columns of a range that meet one or more conditions. The matching results spill into the cells below or beside the formula, so the list updates when the source data or the conditions change. Use it when you need a live list of matching records instead of rows hidden with AutoFilter.

The `include` argument is a Boolean array that has the same height or width as the source range. Build it with a comparison such as `B2:B7="Active"`. Combine several conditions with `*` for AND logic and `+` for OR logic, and wrap each condition in parentheses so the operators evaluate in the right order.

When no rows match, Excel returns `#CALC!` unless you supply the optional `if_empty` value. Google Sheets has no `if_empty` argument and returns `#N/A` instead, so wrap the formula in IFERROR when the same workbook must show a clean message on both platforms. FILTER is not available in Excel 2019 or earlier.

## Syntax

```excel
=FILTER(array, include, [if_empty])
```

<!-- Image 1: FILTER Arguments Diagram. See Images/Lookup & Reference/FILTER.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array` | Yes | The range or array to return. It can be one column, one row or several columns or rows. |
| `include` | Yes | A Boolean array with the same number of rows (or columns) as `array`. Rows where the value is TRUE are returned. |
| `if_empty` | No | The value returned when no row matches. Omitting it causes `#CALC!` in Excel when nothing matches. |

Google Sheets uses the syntax `FILTER(range, condition1, [condition2, ...])`. Each condition is a separate argument, and the conditions combine with AND. Sheets does not accept `if_empty`.

### Return Value

A dynamic array that contains the rows or columns of `array` where `include` is TRUE. It returns `#CALC!` in Excel, or `#N/A` in Sheets, when no row matches and no fallback is supplied. It returns `#VALUE!` when `include` does not match the size of `array`.

## Examples

The examples use this inventory list in `A1:D7`. Row 1 holds the headers.

| Item | Team | Status | Cost |
| --- | --- | --- | --- |
| Desk Lamp | Ops | Active | 45 |
| Office Chair | Facilities | Retired | 180 |
| Monitor Arm | Ops | Active | 95 |
| Whiteboard | Facilities | Active | 120 |
| Headset | Support | Retired | 60 |
| Keyboard | Support | Active | 75 |

### Example 1: Return One Column Where a Condition Matches

```excel
=FILTER(A2:A7, C2:C7="Active")
```

**Result:** `Desk Lamp`, `Monitor Arm`, `Whiteboard` and `Keyboard`, spilled down four cells.

The include array `C2:C7="Active"` marks four rows as TRUE. Only the matching item names are returned.

### Example 2: Return Full Rows Where a Number Matches

```excel
=FILTER(A2:D7, D2:D7>=100)
```

**Result:** Two rows, `Office Chair` (Facilities, Retired, 180) and `Whiteboard` (Facilities, Active, 120).

The first argument returns all four columns, so the spilled result is two rows by four columns.

### Example 3: Show a Message When Nothing Matches

```excel
=FILTER(A2:D7, B2:B7="Legal", "No Legal items")
```

**Result:** `No Legal items`

No row has `Legal` in column B, so the `if_empty` text appears in the cell. Use this form in any list that people read, so an empty result never shows an error.

### Example 4: Combine Conditions With AND Logic

```excel
=FILTER(A2:A7, (B2:B7="Facilities")*(C2:C7="Active"))
```

**Result:** `Whiteboard`

Both conditions must be TRUE. Multiplying the two TRUE or FALSE arrays gives 1 only when both are TRUE. In Google Sheets, the same logic is written as `=FILTER(A2:A7, B2:B7="Facilities", C2:C7="Active")`.

### Example 5: Combine Conditions With OR Logic

```excel
=FILTER(A2:A7, (B2:B7="Support")+(D2:D7>=150))
```

**Result:** `Office Chair`, `Headset` and `Keyboard`, spilled down three cells.

Adding two conditions returns a row when either one is TRUE. Office Chair qualifies on cost, and Headset and Keyboard qualify on team.

<!-- Image 2: AND and OR Logic With Include Arrays. See Images/Lookup & Reference/FILTER.md -->

### Example 6: Filter by a Value in a Cell

```excel
=FILTER(A2:A7, C2:C7=G1)
```

**Result:** When `G1` contains `Retired`, the result is `Office Chair` and `Headset`.

Point the include array at an input cell so people can change the criteria without editing the formula.

## Story Problems

### Problem 1: Bake Sale Morning Crew

A volunteer coordinator keeps the bake sale roster in `A1:B7`, with one volunteer per row.

| Volunteer | Shift |
| --- | --- |
| Amara | Morning |
| Ben | Afternoon |
| Chloe | Morning |
| Dev | Evening |
| Eli | Morning |
| Farah | Afternoon |

**Task:** List the names of every volunteer on the Morning shift, and show `No volunteers` when the shift is empty.

**Solution:**

```excel
=FILTER(A2:A7, B2:B7="Morning", "No volunteers")
```

**Answer:** `Amara`, `Chloe` and `Eli`, spilled down three cells, because those are the three rows marked Morning.

### Problem 2: Overdue Library Fines

A school library charges $0.25 for each day a book is late. The table sits in `A1:C6`.

| Book | Days Late | Fine |
| --- | --- | --- |
| Maple Street | 2 | 0.50 |
| Night Harbor | 9 | 2.25 |
| Iron Garden | 14 | 3.50 |
| Paper Moon | 7 | 1.75 |
| Quiet Hours | 11 | 2.75 |

**Task:** Total the fines for books that are more than 7 days late.

**Solution:**

```excel
=SUM(FILTER(C2:C6, B2:B6>7))
```

**Answer:** `$8.50`. Night Harbor (2.25), Iron Garden (3.50) and Quiet Hours (2.75) are more than 7 days late. Paper Moon is exactly 7 days late, so it is excluded.

<!-- Image 3: Overdue Library Fines Result. See Images/Lookup & Reference/FILTER.md -->

## Use Cases

### Expense Approval Queue

**Scenario:** A finance team wants a queue of expense claims that still need approval, and the list must update as new claims are added to the log.

```excel
=FILTER(Claims!A2:G500, (Claims!F2:F500="Pending")*(Claims!E2:E500>=$K$1), "Nothing waiting")
```

**Why It Works:** Both conditions are multiplied for AND logic, and `K1` holds the approval threshold. Changing `K1` widens or narrows the queue without touching the formula.

### Open Ticket Lists

**Scenario:** A support lead needs each agent to see only their open tickets, sorted by age.

```excel
=SORT(FILTER(Tickets!A2:E300, (Tickets!D2:D300="Open")*(Tickets!B2:B300=$H$1)), 5, 1)
```

**Why It Works:** FILTER keeps the open tickets for the agent named in `H1`, and SORT orders them by the fifth column. The result is one formula with no helper columns.

### Overdue Library Fines

**Scenario:** A librarian totals the fines owed on items that are more than a set number of days overdue.

```excel
=SUM(FILTER(Loans!C2:C400, Loans!B2:B400>$H$2))
```

**Why It Works:** FILTER returns only the fines whose days-late value passes the threshold in `H2`. SUM then totals the filtered result.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#CALC!` | No row matches and `if_empty` is omitted (Excel). | Add an `if_empty` value such as `"No results"`. |
| `#N/A` | No row matches (Google Sheets). | Wrap the formula in IFERROR with the fallback text. |
| `#VALUE!` | The `include` array has a different number of rows or columns than `array`. | Use ranges of the same height or width. |
| `#SPILL!` | Cells in the spill range already contain data. | Clear the cells below or beside the formula. |
| Wrong rows returned | Conditions are not wrapped in parentheses, so the operators run in the wrong order. | Write each condition as `(A2:A7="X")` before combining it with `*` or `+`. |
| `#NAME?` | The workbook uses Excel 2019 or earlier, which does not include FILTER. | Use INDEX and MATCH, or upgrade to Excel 2021 or Microsoft 365. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Microsoft 365, Excel 2024, Excel 2021 and Excel for the web | Not available in Excel 2019 or earlier. Empty results return `#CALC!` unless `if_empty` is supplied. Conditions combine with `*` and `+`. |
| Google Sheets | Available | Syntax is `FILTER(range, condition1, [condition2, ...])`. Conditions are separate arguments and combine with AND. No `if_empty` argument exists, and empty results return `#N/A`. |

## Tips and Best Practices

- Always supply `if_empty` in Excel, or wrap the formula in IFERROR in Sheets, so users never see an error code.
- Put parentheses around every condition in a compound filter. `(B2:B7="X")*(D2:D7>10)` works, and `B2:B7="X"*D2:D7>10` does not.
- Reference a cell for each criterion rather than typing values into the formula, so people can change the filter without editing it.
- Leave empty rows and columns below and beside the formula, because the result grows when the source grows.
- Use SORT or UNIQUE around FILTER to order or de-duplicate the output in the same formula.
- Use whole-column or table references such as `Table1[Cost]` so the source expands with new rows.

## Related Functions

| Function | Relationship |
| --- | --- |
| [CHOOSECOLS](../Lookup%20%26%20Reference/CHOOSECOLS.md) | Selects specific columns from the filtered result. |
| [QUERY](../Google-specific/QUERY.md) | Filters, sorts and groups with SQL-like syntax in Google Sheets. |
| [SORT](../Lookup%20%26%20Reference/SORT.md) | Orders the rows that FILTER returns. |
| [SUMIFS](../Math%20%26%20Trig/SUMIFS.md) | Totals a column for conditions written inside the formula, without a spill range. |
| [UNIQUE](../Lookup%20%26%20Reference/UNIQUE.md) | Removes duplicate values from the filtered result. |

## Official Documentation

- [Microsoft Support: FILTER function](https://support.microsoft.com/en-us/excel/functions/filter-function)
- [Google Docs Editors Help: FILTER](https://support.google.com/docs/answer/3093197)
