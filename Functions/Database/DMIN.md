---
domain: Spreadsheet Functions
category: Database
subcategory: Database Aggregation
purpose:
  - Aggregation
  - Database Queries
use-case:
  - Fastest Delivery Routes
  - Lowest Temperature Records
related:
  - DGET
  - DMAX
  - MIN
  - MINIFS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/dmin-function
  - https://support.google.com/docs/answer/3094149
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Minimum
  - Minimum With Criteria
tags:
  - criteria
  - database
  - excel
  - minimum
  - sheets
---

# DMIN

## Description

**DMIN** returns the smallest value in one field (column) of a list, considering only the records that match the conditions in a separate criteria range. The list is a range where the first row holds column labels and every row below it is a record.

Use DMIN when the question is "what is the lowest value for this group," and the group is set by conditions that users can change on the sheet. Examples include the coldest reading for one city, or the shortest delivery time on one route. Because the criteria sit in cells, changing the route in one cell updates every result that depends on it.

For a minimum with conditions written inside the formula, MINIFS is simpler and needs no criteria block. DMIN is the better fit when the criteria are edited on the sheet, when OR logic across rows is needed, or when an existing workbook already uses criteria ranges. Microsoft's help page does not describe the result when no record matches, so check the criteria before relying on the output.

## Syntax

```excel
=DMIN(database, field, criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DMIN.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:E8`. Each column needs a label in the first row. |
| `field` | Yes | The column to evaluate: a header label in quotes (`"Price"`), a cell that holds the label, or the column position as a number (`5` for the fifth column). |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A number: the smallest value in the field among the records that match the criteria. Negative numbers are returned as they are stored.

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

### Example 1: Lowest Price in One Category

Criteria in `G1:G2`: `Category` above `Lighting`.

```excel
=DMIN(A1:E8, "Price", G1:G2)
```

**Result:** `35`

The lighting records have prices of 35 and 40, so the minimum is 35.

### Example 2: Fewest Units at One Store

Criteria in `G1:G2`: `Store` above `Hillside`.

```excel
=DMIN(A1:E8, "Units", G1:G2)
```

**Result:** `2`

The Hillside records have 2 and 9 units, so the minimum is 2.

<!-- Image 2: Conditions on the Same Row Versus Separate Rows. See Images/Database/DMIN.md -->

### Example 3: Two Conditions With AND Logic

Criteria in `G1:H2`: `Store` and `Category` on the same row, with `Riverside` and `Storage` beneath them.

```excel
=DMIN(A1:E8, "Price", G1:H2)
```

**Result:** `55`

Only the Riverside shelf is both in Riverside and in the Storage category, so its price of 55 is the minimum.

### Example 4: Conditions on Separate Rows (OR Logic)

Criteria in `G1:G3`: `Product` above `Desk`, then `Chair` on the next row.

```excel
=DMIN(A1:E8, "Price", G1:G3)
```

**Result:** `85`

The desk prices are 220 and 240, and the chair price is 85. The smallest of the three is 85.

## Story Problems

### Problem 1: Coldest Reading in a City

A weather station logs a daily temperature in degrees Celsius for two cities in `A1:C6`.

| City | Day | Temperature |
| --- | --- | --- |
| Oslo | Mon | 4 |
| Oslo | Tue | -2 |
| Rome | Mon | 12 |
| Rome | Tue | 9 |
| Oslo | Wed | 1 |

**Task:** Put `City` in `E1` and `Oslo` in `E2`, then find the coldest reading in Oslo.

**Solution:**

```excel
=DMIN(A1:C6, "Temperature", E1:E2)
```

**Answer:** `-2`, the Tuesday reading in Oslo. Oslo's other readings are 4 and 1.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DMIN.md -->

### Problem 2: Fastest Route Delivery

A courier records the delivery days for each route in `A1:B5`.

| Route | Days |
| --- | --- |
| Route A | 3 |
| Route B | 5 |
| Route A | 2 |
| Route C | 4 |

**Task:** Put `Route` in `D1` and `Route A` in `D2`, then find the fewest days taken on Route A.

**Solution:**

```excel
=DMIN(A1:B5, "Days", D1:D2)
```

**Answer:** `2`, because Route A took 3 days once and 2 days once.

## Use Cases

### Fastest Delivery Routes

**Scenario:** A dispatch manager compares the quickest delivery time for whichever route is chosen from a drop-down.

```excel
=DMIN(Deliveries, "Days", RouteFilter)
```

**Why It Works:** The criteria cell holds the route, so the same formula reports the best time for any route the manager selects.

### Lowest Temperature Records

**Scenario:** A climate report lists the coldest reading for each city in a summary table.

```excel
=DMIN(Readings, "Temperature", CityFilter)
```

**Why It Works:** Each city's criteria cell limits the minimum to that city's rows. Copy the formula down the table and change only the city cell.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected minimum | A blank cell under a label in the criteria range matches every record. | Size the criteria range to the condition rows only. |
| Unexpected minimum | Text criteria match more values than intended, such as `Rome` matching `Romeville`. | Use `="=Rome"` in the criteria cell for an exact match. |
| Wrong value | The field is a text column or a column number points at the wrong column. | Use the header label of a numeric column, in quotes. |
| Unexpected result | The criteria labels do not match the database headers. | Copy the header cells into the criteria range. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel for Microsoft 365, Excel 2016 and later, and Excel for the web | Criteria accept wildcards and comparison operators. |
| Google Sheets | Available | Same three arguments. The help page does not explain criteria syntax in detail, so test criteria before sharing. |

## Tips and Best Practices

- Use MIN on a plain range when no conditions are needed, since it is simpler.
- Check the criteria with DCOUNT first so the minimum is based on the records you expect.
- Keep the criteria range above or beside the list, never below it.
- Use header labels rather than column numbers so inserted columns do not break the formula.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DGET](DGET.md) | Returns the single matching value rather than the smallest one. |
| [DMAX](DMAX.md) | Returns the largest matching value. |
| [MIN](../Statistical/MIN.md) | Finds the smallest number in a plain range with no criteria. |
| [MINIFS](../Statistical/MINIFS.md) | Finds the smallest value that meets conditions written inside the formula. |

## Official Documentation

- [Microsoft Support: DMIN function](https://support.microsoft.com/en-us/excel/functions/dmin-function)
- [Google Docs Editors Help: DMIN](https://support.google.com/docs/answer/3094149)
