---
domain: Spreadsheet Functions
category: Database
subcategory: Database Aggregation
purpose:
  - Aggregation
  - Database Queries
use-case:
  - Compound Growth Factors
  - Multi-Stage Pass Rates
related:
  - DAVERAGE
  - DSUM
  - PRODUCT
  - SUMPRODUCT
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/dproduct-function
  - https://support.google.com/docs/answer/3094230
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Product
  - Product With Criteria
tags:
  - criteria
  - database
  - excel
  - product
  - sheets
---

# DPRODUCT

## Description

**DPRODUCT** multiplies together the values in one field (column) of a list, considering only the records that match the conditions in a separate criteria range. The list is a range where the first row holds column labels and every row below it is a record.

Use DPRODUCT when the values are factors that should be multiplied, such as yearly growth multipliers, stage pass rates or scaling factors. The criteria select which records are multiplied, so one formula can produce a cumulative factor for each fund, line or product.

For a plain range with no conditions, PRODUCT is simpler. For a product of pairs of values across two ranges, SUMPRODUCT is used with other arithmetic. DPRODUCT is the better fit when the conditions are edited on the sheet or when OR logic across rows is needed. Microsoft's help page does not state the result for an empty set of records, so check the criteria before relying on the output.

## Syntax

```excel
=DPRODUCT(database, field, criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DPRODUCT.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:E8`. Each column needs a label in the first row. |
| `field` | Yes | The column whose values are multiplied: a header label in quotes (`"Units"`), a cell that holds the label, or the column position as a number. |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A number: the product of the field values among the records that match the criteria. Format the cell as currency or percentage if the values call for it.

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

### Example 1: Multiply Units at One Store

Criteria in `G1:G2`: `Store` above `Lakeview`.

```excel
=DPRODUCT(A1:E8, "Units", G1:G2)
```

**Result:** `30`

The Lakeview records have 6 and 5 units, and 6 times 5 is 30.

### Example 2: Three Records in One Store

Criteria in `G1:G2`: `Store` above `Riverside`.

```excel
=DPRODUCT(A1:E8, "Units", G1:G2)
```

**Result:** `144`

The Riverside records have 4, 12 and 3 units. 4 times 12 times 3 is 144.

<!-- Image 2: Conditions on the Same Row Versus Separate Rows. See Images/Database/DPRODUCT.md -->

### Example 3: Conditions on Separate Rows (OR Logic)

Criteria in `G1:G3`: `Product` above `Desk`, then `Chair` on the next row.

```excel
=DPRODUCT(A1:E8, "Units", G1:G3)
```

**Result:** `72`

The two desks have 4 and 2 units and the chair has 9. 4 times 2 times 9 is 72.

### Example 4: Product of Prices in One Category

Criteria in `G1:G2`: `Category` above `Storage`.

```excel
=DPRODUCT(A1:E8, "Price", G1:G2)
```

**Result:** `3300`

The storage records cost 60 and 55, and 60 times 55 is 3300.

## Story Problems

### Problem 1: Cumulative Growth of One Fund

An analyst records a yearly growth factor for two funds in `A1:C5`. A factor of 1.05 means 5 percent growth that year.

| Fund | Year | Growth Factor |
| --- | --- | --- |
| Alpha | 2025 | 1.05 |
| Alpha | 2026 | 1.10 |
| Beta | 2025 | 0.98 |
| Alpha | 2027 | 1.02 |

**Task:** Put `Fund` in `E1` and `Alpha` in `E2`, then find the cumulative growth factor for Alpha across all its years.

**Solution:**

```excel
=DPRODUCT(A1:C5, "Growth Factor", E1:E2)
```

**Answer:** `1.1781`, because 1.05 times 1.10 times 1.02 is 1.1781. That means Alpha grew 17.81 percent over the three years.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DPRODUCT.md -->

### Problem 2: Overall Pass Rate for a Production Line

A factory tracks the pass rate at each inspection stage for two production lines in `A1:C5`. Each rate is a fraction of the units that move on to the next stage.

| Line | Stage | Pass Rate |
| --- | --- | --- |
| Line 1 | Stage 1 | 0.95 |
| Line 1 | Stage 2 | 0.90 |
| Line 2 | Stage 1 | 0.97 |
| Line 1 | Stage 3 | 0.98 |

**Task:** Put `Line` in `E1` and `Line 1` in `E2`, then find the overall pass rate for Line 1 across all three stages.

**Solution:**

```excel
=DPRODUCT(A1:C5, "Pass Rate", E1:E2)
```

**Answer:** `0.8379`, because 0.95 times 0.90 times 0.98 is 0.8379, or 83.79 percent of units pass every stage.

## Use Cases

### Compound Growth Factors

**Scenario:** A planner multiplies the yearly growth factors for one fund to find its cumulative return, with the fund name typed into a cell.

```excel
=DPRODUCT(Growth, "Factor", FundFilter)
```

**Why It Works:** Each factor compounds on the previous one, which is exactly what multiplication does. Subtract 1 from the result to get the total return.

### Multi-Stage Pass Rates

**Scenario:** An operations team estimates how many finished units pass every inspection stage on one line.

```excel
=DPRODUCT(Stages, "PassRate", LineFilter) * StartingUnits
```

**Why It Works:** Multiplying the stage rates gives the share of units that pass everything. Multiplying that share by the starting count gives the expected finished units.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected product | A blank cell under a label in the criteria range matches every record. | Size the criteria range to the condition rows only. |
| Unexpected product | Percentages are typed as text, so they are not multiplied. | Enter the rates as numbers or percentages, not as text. |
| Wrong value | The field label does not match the header, or a column number points at the wrong column. | Use the exact header text in quotes, or confirm the column position. |
| Unexpected result | The criteria labels do not match the database headers. | Copy the header cells into the criteria range. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel for Microsoft 365, Excel 2016 and later, and Excel for the web | Criteria accept wildcards and comparison operators. |
| Google Sheets | Available | Same three arguments. The help page does not explain criteria syntax in detail, so test criteria before sharing. |

## Tips and Best Practices

- Use PRODUCT on a plain range when no conditions are needed.
- Keep rates as numbers; a value stored as text is ignored or breaks the product.
- Keep the criteria range above or beside the list, never below it.
- Check the product with a helper column for a few rows before using it on a large report.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DAVERAGE](DAVERAGE.md) | Averages the field for the same matching records. |
| [DSUM](DSUM.md) | Adds the field for the same matching records instead of multiplying. |
| [PRODUCT](../Math%20%26%20Trig/PRODUCT.md) | Multiplies numbers in a plain range with no criteria. |
| [SUMPRODUCT](../Math%20%26%20Trig/SUMPRODUCT.md) | Multiplies arrays element by element and then adds the results. |

## Official Documentation

- [Microsoft Support: DPRODUCT function](https://support.microsoft.com/en-us/excel/functions/dproduct-function)
- [Google Docs Editors Help: DPRODUCT](https://support.google.com/docs/answer/3094230)
