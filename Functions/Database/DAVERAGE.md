---
domain: Spreadsheet Functions
category: Database
subcategory: Database Aggregation
purpose:
  - Aggregation
  - Database Queries
use-case:
  - Branch Performance Averages
  - Carrier Delivery Times
  - Customer Ratings
related:
  - AVERAGEIFS
  - DCOUNT
  - DGET
  - DMAX
  - DSUM
  - FILTER
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/daverage-function
  - https://support.google.com/docs/answer/3094144
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Average
  - Average With Criteria Range
tags:
  - average
  - criteria
  - database
  - excel
  - sheets
---

# DAVERAGE

## Description

**DAVERAGE** returns the average of the values in one field (column) of a list, counting only the records that match the conditions in a separate criteria range. The list is a range where the first row holds column labels and every row below it is a record.

Use DAVERAGE when the conditions should live on the sheet, where a user can type a different store name or a new minimum into a cell and every DAVERAGE that points at that cell updates. The criteria range also supports OR logic (conditions on separate rows) and AND logic (conditions on the same row) without nesting functions.

For fixed conditions written inside a formula, AVERAGEIFS is simpler because it needs no criteria block. DAVERAGE is the better fit when the criteria are maintained by people who do not write formulas, when OR logic across rows is needed, or when an existing workbook already uses criteria ranges. Text matching is not case-sensitive, and typing text without an equal sign matches every value that starts with those characters.

## Syntax

```excel
=DAVERAGE(database, field, criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DAVERAGE.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:E8`. Each column needs a label in the first row. |
| `field` | Yes | The column to average: a header label in quotes (`"Price"`), a cell that holds the label, or the column position as a number (`5` for the fifth column). |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Labels must match the database headers. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A number: the average of the field values in the records that match the criteria. Microsoft's help page does not describe the result when no record matches, so check the criteria before relying on the output.

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

### Example 1: Average Price for One Store

Criteria in `G1:G2`: `Store` above `Lakeview`.

```excel
=DAVERAGE(A1:E8, "Price", G1:G2)
```

**Result:** `50`

The two Lakeview records have prices of 40 and 60, so the average is 50.

### Example 2: Two Conditions With AND Logic

Criteria in `G1:H2`: `Store` and `Category` on the same row, with `Riverside` and `Storage` beneath them.

```excel
=DAVERAGE(A1:E8, "Units", G1:H2)
```

**Result:** `3`

Only one record is both in Riverside and in the Storage category, the shelf with 3 units.

<!-- Image 2: Conditions on the Same Row Versus Separate Rows. See Images/Database/DAVERAGE.md -->

### Example 3: Conditions on Separate Rows (OR Logic)

Criteria in `G1:G3`: `Product` above `Desk`, then `Chair` on the next row.

```excel
=DAVERAGE(A1:E8, "Units", G1:G3)
```

**Result:** `5`

The two desk records have 4 and 2 units and the chair has 9. The three values add to 15, and 15 divided by 3 is 5.

### Example 4: Field by Column Number

Criteria in `G1:G2`: `Store` above `Lakeview`.

```excel
=DAVERAGE(A1:E8, 4, G1:G2)
```

**Result:** `5.5`

The number 4 points at the fourth column, `Units`. The Lakeview units are 6 and 5, which average 5.5. A header label is safer than a column number because it still works after a column is inserted.

## Story Problems

### Problem 1: Ratings by Branch

A coffee chain records a customer rating for each drink sold at its branches in `A1:C6`.

| Branch | Drink | Rating |
| --- | --- | --- |
| Harbor | Latte | 4 |
| Harbor | Mocha | 5 |
| Pier | Latte | 3 |
| Pier | Tea | 4 |
| Harbor | Tea | 2 |

**Task:** Put `Branch` in `G1` and `Harbor` in `G2`, then find the average rating for the Harbor branch.

**Solution:**

```excel
=DAVERAGE(A1:C6, "Rating", G1:G2)
```

**Answer:** `3.67`, rounded, because the three Harbor ratings are 4, 5 and 2, which total 11, and 11 divided by 3 is 3.67.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DAVERAGE.md -->

### Problem 2: Heavy Shipments by Carrier

A small distributor logs each shipment's carrier, weight in kilograms and transit days in `A1:C6`.

| Carrier | Weight | Days |
| --- | --- | --- |
| Northline | 12 | 3 |
| Northline | 4 | 2 |
| Swiftway | 15 | 5 |
| Northline | 20 | 4 |
| Swiftway | 8 | 2 |

**Task:** Use `Carrier` and `Weight` as labels in `G1:H1`, with `Northline` in `G2` and `>10` in `H2`, then find the average transit days for Northline shipments heavier than 10 kg.

**Solution:**

```excel
=DAVERAGE(A1:C6, "Days", G1:H2)
```

**Answer:** `3.5`, because the two qualifying shipments (12 kg and 20 kg) took 3 and 4 days.

## Use Cases

### Branch Performance Averages

**Scenario:** Area managers want the average rating for whichever branch they select from a drop-down list on a shared report.

```excel
=DAVERAGE(Ratings, "Rating", BranchFilter)
```

**Why It Works:** The named range `BranchFilter` holds the drop-down cell and its label, so managers change the question without editing the formula. Use a table or named range for `Ratings` so new rows are included.

### Carrier Delivery Times

**Scenario:** Operations compares average transit days for heavy parcels across carriers, using a criteria block that planners can edit.

```excel
=DAVERAGE(Shipments, "Days", ShipCriteria)
```

**Why It Works:** The criteria block holds the carrier and the weight threshold. Changing the threshold from `>10` to `>20` updates every average on the report.

### Customer Ratings for Several Products

**Scenario:** A product team needs the average rating for either of two products on the same review sheet.

```excel
=DAVERAGE(Reviews, "Stars", H1:H3)
```

**Why It Works:** The two product names sit on separate rows of the criteria range, so the function applies OR logic and averages both products together.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected average | The criteria range sits below the list, so new records land on a non-blank row. | Place the criteria range beside or above the list. |
| Unexpected average | A blank cell under a label in the criteria range matches every record. | Remove the blank cell, or keep it on purpose to average the whole column. |
| Unexpected average | Text criteria match more values than intended, such as `East` matching `Eastern`. | Use `="=East"` in the criteria cell for an exact match. |
| Wrong column averaged | The field label is misspelled or the column number points at a different column. | Use the exact header text in quotes, or confirm the column position. |
| Unexpected average | The criteria labels do not match the database headers. | Copy the header cells into the criteria range instead of typing them. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel for Microsoft 365, Excel 2016 and later, and Excel for the web | Criteria accept wildcards (`*`, `?`, `~`) and comparison operators such as `>10`. |
| Google Sheets | Available | Same three arguments. The help page does not explain criteria syntax in detail, so test criteria in Sheets before sharing a workbook. |

## Tips and Best Practices

- Keep the criteria range away from the database, above it or on another sheet, so filtering or sorting the list does not disturb the conditions.
- Convert the database to an Excel table or a named range so the `database` argument grows as rows are added.
- Use header labels rather than column numbers so inserted columns do not break the formula.
- Prefer AVERAGEIFS for fixed conditions written by formula builders, and DAVERAGE when users edit conditions on the sheet.
- Check the criteria with DCOUNT first. If the count is 0 or unexpectedly large, the average will not be meaningful either.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGEIFS](../Statistical/AVERAGEIFS.md) | Averages with conditions written inside the formula instead of a criteria range. |
| [DCOUNT](DCOUNT.md) | Counts the numeric values that match the same criteria, useful for checking the sample size. |
| [DGET](DGET.md) | Returns one matching value rather than an average. |
| [DMAX](DMAX.md) | Returns the largest matching value for the same field. |
| [DSUM](DSUM.md) | Adds the matching values instead of averaging them. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Returns the matching rows themselves, so AVERAGE can be applied to the result. |

## Official Documentation

- [Microsoft Support: DAVERAGE function](https://support.microsoft.com/en-us/excel/functions/daverage-function)
- [Google Docs Editors Help: DAVERAGE](https://support.google.com/docs/answer/3094144)
