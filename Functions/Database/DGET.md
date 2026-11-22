---
domain: Spreadsheet Functions
category: Database
subcategory: Database Retrieval
purpose:
  - Data Retrieval
  - Database Queries
use-case:
  - Employee Directory Lookup
  - Price List Lookup
  - Unique Record Retrieval
related:
  - DAVERAGE
  - DMAX
  - DMIN
  - DSUM
  - FILTER
  - INDEX
  - XLOOKUP
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/dget-function
  - https://support.google.com/docs/answer/3094148
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Get
  - Extract Single Record
tags:
  - criteria
  - database
  - excel
  - retrieval
  - sheets
---

# DGET

## Description

**DGET** returns one value from one field (column) of a list, taken from the single record that matches the conditions in a separate criteria range. The list is a range where the first row holds column labels and every row below it is a record. Unlike the other database functions, DGET does not add, count or average. It extracts.

Use DGET when the criteria should identify exactly one record, such as a unique employee ID or a product in one size, and you want that record's value in another column. DGET returns an error when no record matches and when more than one record matches, so it is a strict lookup. Use it when a second match would be a data problem that should be noticed.

When you want the first match rather than an error for duplicates, INDEX with MATCH or XLOOKUP is the usual choice. When you want every matching row, use FILTER. DGET is best when the conditions sit in a criteria block that users can edit.

## Syntax

```excel
=DGET(database, field, criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DGET.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:E8`. Each column needs a label in the first row. |
| `field` | Yes | The column that holds the value to return: a header label in quotes (`"Units"`), a cell that holds the label, or the column position as a number (`4` for the fourth column). |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

One value from the field, taken from the single record that matches the criteria. The value can be a number or text. If no record matches, DGET returns `#VALUE!`. If more than one record matches, it returns `#NUM!`.

## Examples

All examples use this shop list in `A1:E8`.

| Store | Product | Category | Units | Price |
| --- | --- | --- | --- | --- |
| Riverside | Desk | Furniture | 4 | 220 |
| Riverside | Lamp | Lighting | 12 | 35 |
| Hillside | Desk | Furniture | 2 | 240 |
| Hillside | Chair | Furniture | 9 | 85 |
| Lakeview | Lamp | Lighting | 6 | 40 |
| Lakeview | Shelf | Storage | 5 | 60 |
| Riverside | Shelf | Storage | 3 | 55 |

### Example 1: Return a Value From a Unique Match

Criteria in `G1:G2`: `Product` above `Chair`.

```excel
=DGET(A1:E8, "Units", G1:G2)
```

**Result:** `9`

Only one record is a chair, and its units value is 9.

### Example 2: Two Conditions With AND Logic

Criteria in `G1:H2`: `Store` and `Product` on the same row, with `Hillside` and `Desk` beneath them.

```excel
=DGET(A1:E8, "Price", G1:H2)
```

**Result:** `240`

Only the Hillside desk matches both conditions, so its price of 240 is returned.

<!-- Image 2: One Match Versus Several Matches. See Images/Database/DGET.md -->

### Example 3: Several Matches Return an Error

Criteria in `G1:G2`: `Product` above `Desk`.

```excel
=DGET(A1:E8, "Units", G1:G2)
```

**Result:** `#NUM!`

Two records are desks, one in Riverside and one in Hillside. DGET cannot choose between them, so it returns `#NUM!`. Add a second condition, such as the store, to make the match unique.

### Example 4: No Match Returns an Error

Criteria in `G1:G2`: `Product` above `Table`.

```excel
=DGET(A1:E8, "Price", G1:G2)
```

**Result:** `#VALUE!`

The list has no table, so no record matches and DGET returns `#VALUE!`. Wrap the formula in IFERROR to show a friendly message instead.

## Story Problems

### Problem 1: Finding an Extension

A company keeps a directory in `A1:D5` with one row for each employee.

| ID | Name | Department | Extension |
| --- | --- | --- | --- |
| E101 | Ada | Sales | 214 |
| E102 | Bo | Support | 330 |
| E103 | Cam | Sales | 215 |
| E104 | Dee | Finance | 402 |

**Task:** Put `Department` in `G1` and `Finance` in `G2`, then return the extension of the one Finance employee.

**Solution:**

```excel
=DGET(A1:D5, "Extension", G1:G2)
```

**Answer:** `402`, because Dee is the only employee in Finance.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DGET.md -->

### Problem 2: Price of One Size

A pottery shop keeps a price list in `A1:C5`. Each product appears once for each size.

| Product | Size | Price |
| --- | --- | --- |
| Mug | S | 8 |
| Mug | L | 10 |
| Bowl | S | 6 |
| Bowl | L | 9 |

**Task:** Put `Product` in `E1`, `Size` in `F1`, then `Bowl` in `E2` and `L` in `F2`. Return the price of a large bowl.

**Solution:**

```excel
=DGET(A1:C5, "Price", E1:F2)
```

**Answer:** `9`, because only one record is a large bowl.

## Use Cases

### Employee Directory Lookup

**Scenario:** A front desk enters an employee ID into a criteria cell and the extension appears in a report.

```excel
=DGET(Directory, "Extension", IDFilter)
```

**Why It Works:** The unique ID guarantees one match. If the directory ever contains a duplicate ID, the formula returns `#NUM!` and the problem is visible.

### Price List Lookup

**Scenario:** A quote sheet looks up one product in one size from a price list that the sales team updates.

```excel
=DGET(PriceList, "Price", QuoteCriteria)
```

**Why It Works:** The criteria block holds the product and size that the quote needs, so the price updates when the list changes.

### Unique Record Retrieval

**Scenario:** A data steward confirms that a record exists exactly once and reads its value in one step.

```excel
=IFERROR(DGET(Assets, "Owner", AssetTag), "Check record")
```

**Why It Works:** Wrapping DGET in IFERROR shows a message for both a missing record and a duplicate, which are the two cases that need attention.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#VALUE!` | No record matches the criteria, or the criteria label is misspelled. | Check the condition text and the header spelling in the criteria range. |
| `#NUM!` | More than one record matches. | Add a condition that identifies one record, or switch to FILTER to see all matches. |
| Unexpected result | The field label does not match a header in the first row. | Match the header text exactly in quotes, or confirm the column position. |
| Wrong value | The criteria range includes a blank row under a label, which matches every record. | Size the criteria range to the condition rows only. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel for Microsoft 365, Excel 2016 and later, and Excel for the web | Returns `#VALUE!` for no match and `#NUM!` for more than one match. |
| Google Sheets | Available | Same three arguments. The help page states that no match and multiple matches both return an error; test the exact error value before building error handling on it. |

## Tips and Best Practices

- Make the criteria unique by including a key column such as an ID, so the formula never meets two matches.
- Wrap DGET in IFERROR only when the message clearly says what went wrong.
- Use header labels rather than column numbers so inserted columns do not break the formula.
- Use FILTER or INDEX with MATCH when the list may contain duplicates and the first match is acceptable.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DAVERAGE](DAVERAGE.md) | Averages the field across all matching records instead of returning one value. |
| [DMAX](DMAX.md) | Returns the largest value across matching records. |
| [DMIN](DMIN.md) | Returns the smallest value across matching records. |
| [DSUM](DSUM.md) | Adds the field across matching records. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns every matching row, so duplicates are visible. |
| [INDEX](../Lookup%20%26%20Reference/INDEX.md) | Returns a value from a position in a range, usually paired with MATCH. |
| [XLOOKUP](../Lookup%20%26%20Reference/XLOOKUP.md) | Looks up a single key and returns the first match, with built-in not-found handling. |

## Official Documentation

- [Microsoft Support: DGET function](https://support.microsoft.com/en-us/excel/functions/dget-function)
- [Google Docs Editors Help: DGET](https://support.google.com/docs/answer/3094148)
