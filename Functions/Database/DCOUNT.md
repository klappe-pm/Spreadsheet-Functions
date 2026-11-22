---
domain: Spreadsheet Functions
category: Database
subcategory: Database Aggregation
purpose:
  - Counting
  - Database Queries
use-case:
  - Invoice Counts Over Threshold
  - Numeric Entries Only
  - Ticket Response Counts
related:
  - COUNT
  - COUNTIFS
  - DAVERAGE
  - DCOUNTA
  - DGET
  - DSUM
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/dcount-function
  - https://support.google.com/docs/answer/3094222
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Count
  - Count Numeric Records
tags:
  - counting
  - criteria
  - database
  - excel
  - sheets
---

# DCOUNT

## Description

**DCOUNT** counts the cells that contain numbers in one field (column) of a list, considering only the records that match the conditions in a separate criteria range. The list is a range where the first row holds column labels and every row below it is a record. Text, dates stored as text and blank cells in the field are not counted.

Use DCOUNT when you need to know how many records meet a condition and that the field holds a numeric value. A common case is counting invoices over a threshold when some rows have a note typed into the amount column. DCOUNT skips the note, while DCOUNTA counts it.

The criteria range is built from one or more column labels with conditions beneath them. Conditions on the same row combine with AND, and conditions on separate rows combine with OR. For a count of rows that meet fixed conditions, COUNTIFS is simpler because it needs no criteria block. DCOUNT is the better choice when conditions are edited on the sheet or when OR logic across rows is needed.

## Syntax

```excel
=DCOUNT(database, [field], criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DCOUNT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:E8`. Each column needs a label in the first row. |
| `field` | No | The column to count: a header label in quotes (`"Price"`), a cell that holds the label, or the column position as a number. When omitted, the function counts the matching records. |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A whole number: how many cells in the field contain numbers within the records that match the criteria. A count of zero means no matching record holds a number in that field.

## Examples

All examples use this shop list in `A1:E8`. The Units value for the Hillside desk is the text `Pending`, not a number.

| Store | Product | Category | Units | Price |
| --- | --- | --- | --- | --- |
| Riverside | Desk | Furniture | 4 | 220 |
| Riverside | Lamp | Lighting | 12 | 35 |
| Hillside | Desk | Furniture | Pending | 240 |
| Hillside | Chair | Furniture | 9 | 85 |
| Lakeview | Lamp | Lighting | 6 | 40 |
| Lakeview | Shelf | Storage | 5 | 60 |
| Riverside | Shelf | Storage | 3 | 55 |

### Example 1: Count Priced Items in One Category

Criteria in `G1:G2`: `Category` above `Lighting`.

```excel
=DCOUNT(A1:E8, "Price", G1:G2)
```

**Result:** `2`

Both lighting records have a numeric price, so both are counted.

### Example 2: Text Entries Are Skipped

Criteria in `G1:G2`: `Store` above `Hillside`.

```excel
=DCOUNT(A1:E8, "Units", G1:G2)
```

**Result:** `1`

The two Hillside records match, but the desk's units value is the text `Pending`. Only the chair's 9 is a number, so the count is 1. The same criteria with DCOUNTA returns 2.

<!-- Image 2: Numeric Versus Nonblank Counting. See Images/Database/DCOUNT.md -->

### Example 3: Numeric Comparison

Criteria in `G1:G2`: `Price` above `>=50`.

```excel
=DCOUNT(A1:E8, "Price", G1:G2)
```

**Result:** `5`

The prices 220, 240, 85, 60 and 55 are at least 50. The prices 35 and 40 are below the threshold.

### Example 4: Conditions on Separate Rows (OR Logic)

Criteria in `G1:G3`: `Store` above `Lakeview`, then `Hillside` on the next row.

```excel
=DCOUNT(A1:E8, "Price", G1:G3)
```

**Result:** `4`

Lakeview has two priced records (40 and 60) and Hillside has two (240 and 85). The four records are counted once each.

## Story Problems

### Problem 1: Support Tickets With Hours Logged

A help desk tracks hours spent on each ticket in `A1:C6`. Some entries were not finished, so the hours field contains the word `Pending`.

| Ticket | Team | Hours |
| --- | --- | --- |
| T101 | Support | 3 |
| T102 | Sales | 5 |
| T103 | Support | Pending |
| T104 | Support | 6 |
| T105 | Sales | 2 |

**Task:** Put `Team` in `E1` and `Support` in `E2`, then count the Support tickets that have a numeric hours value.

**Solution:**

```excel
=DCOUNT(A1:C6, "Hours", E1:E2)
```

**Answer:** `2`, because tickets T101 (3 hours) and T104 (6 hours) are Support tickets with numbers. T103 is excluded because `Pending` is text.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DCOUNT.md -->

### Problem 2: Invoices at or Above a Threshold

A freelancer lists invoice amounts in `A1:B6`.

| Client | Amount |
| --- | --- |
| Acme | 1200 |
| Birch | 450 |
| Cedar | 1000 |
| Dune | 980 |
| Ellis | 3100 |

**Task:** Put `Amount` in `D1` and `>=1000` in `D2`, then count the invoices that qualify.

**Solution:**

```excel
=DCOUNT(A1:B6, "Amount", D1:D2)
```

**Answer:** `3`, because Acme (1200), Cedar (1000) and Ellis (3100) meet the threshold. Dune (980) falls just short.

## Use Cases

### Invoice Counts Over Threshold

**Scenario:** A finance team counts how many open invoices exceed a review limit, with the limit typed into a cell that managers can change.

```excel
=DCOUNT(Invoices, "Amount", ReviewLimit)
```

**Why It Works:** The named range `ReviewLimit` holds the label and the condition, so changing the limit updates the count. Keep the amount column numeric so text notes are not counted by mistake.

### Numeric Entries Only

**Scenario:** A survey export mixes numeric ratings with notes such as `N/A`, and the team needs only the number of rated responses for one region.

```excel
=DCOUNT(Survey, "Rating", H1:H2)
```

**Why It Works:** Because DCOUNT ignores text, the count reflects answered ratings without a helper column. Use DCOUNTA when the goal is to count every filled cell instead.

### Ticket Response Counts

**Scenario:** A support lead counts tickets handled by one team that have a recorded response time.

```excel
=DCOUNT(Tickets, "ResponseMinutes", TeamFilter)
```

**Why It Works:** Blank or text response times are excluded, so the count matches the number of tickets that actually have a measured time.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Count lower than expected | Some field values are text that looks like a number, such as `12` stored as text. | Convert the values to numbers, or use DCOUNTA to count every filled cell. |
| Count of 0 | Criteria labels do not match the database headers. | Copy the header cells into the criteria range. |
| Unexpected count | A blank cell under a label in the criteria range matches every record. | Size the criteria range to the condition rows only. |
| Unexpected count | Text criteria match more values than intended, such as `East` matching `Eastern`. | Use `="=East"` in the criteria cell for an exact match. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel for Microsoft 365, Excel 2016 and later, and Excel for the web | Counts only numeric cells in the field. Criteria accept wildcards and comparison operators. |
| Google Sheets | Available | Same arguments and the same purpose of counting numeric values. The help page does not explain criteria syntax in detail, so test criteria before sharing. |

## Tips and Best Practices

- Use DCOUNT on a numeric column and DCOUNTA on a text column, so the function matches what you want to count.
- Omit the field argument only when you want a count of records; otherwise give the label of a column that holds the values you are testing.
- Keep the criteria range above or beside the list, never below it.
- Check a count with a second method, such as COUNTIFS, when the figure feeds a payment or a report.

## Related Functions

| Function | Relationship |
| --- | --- |
| [COUNT](../Statistical/COUNT.md) | Counts numeric cells in a plain range with no criteria. |
| [COUNTIFS](../Statistical/COUNTIFS.md) | Counts rows that meet conditions written inside the formula. |
| [DAVERAGE](DAVERAGE.md) | Averages the numeric values for the same matching records. |
| [DCOUNTA](DCOUNTA.md) | Counts every nonblank cell in the field, including text. |
| [DGET](DGET.md) | Returns the single value that matches the criteria. |
| [DSUM](DSUM.md) | Adds the numeric values for the same matching records. |

## Official Documentation

- [Microsoft Support: DCOUNT function](https://support.microsoft.com/en-us/excel/functions/dcount-function)
- [Google Docs Editors Help: DCOUNT](https://support.google.com/docs/answer/3094222)
