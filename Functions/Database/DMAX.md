---
domain: Spreadsheet Functions
category: Database
subcategory: Database Aggregation
purpose:
  - Aggregation
  - Database Queries
use-case:
  - Peak Rainfall Reports
  - Project Workload Peaks
related:
  - DGET
  - DMIN
  - MAX
  - MAXIFS
level: 3
source:
  - https://support.microsoft.com/en-us/excel/functions/dmax-function
  - https://support.google.com/docs/answer/3094227
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Maximum
  - Maximum With Criteria
tags:
  - criteria
  - database
  - excel
  - maximum
  - sheets
---

# DMAX

## Description

**DMAX** returns the largest value in one field (column) of a list, considering only the records that match the conditions in a separate criteria range. The list is a range where the first row holds column labels and every row below it is a record.

Use DMAX when the question is "what is the highest value for this group," and the group is defined by conditions that users may change on the sheet. A typical case is a peak rainfall for one station, or the longest task in one project. Because the criteria sit in cells, a manager can switch from one project to another without editing the formula.

For a maximum with conditions written inside the formula, MAXIFS is simpler and needs no criteria block. DMAX is the better fit when the conditions are edited on the sheet, when OR logic across rows is needed, or when an existing workbook already uses criteria ranges. Microsoft's help page does not describe the result when no record matches, so check the criteria before relying on the output.

## Syntax

```excel
=DMAX(database, field, criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DMAX.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:E8`. Each column needs a label in the first row. |
| `field` | Yes | The column to evaluate: a header label in quotes (`"Price"`), a cell that holds the label, or the column position as a number (`5` for the fifth column). |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A number: the largest value in the field among the records that match the criteria.

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

### Example 1: Highest Price at One Store

Criteria in `G1:G2`: `Store` above `Hillside`.

```excel
=DMAX(A1:E8, "Price", G1:G2)
```

**Result:** `240`

The Hillside records have prices of 240 and 85, and 240 is the larger.

### Example 2: Most Units in One Category

Criteria in `G1:G2`: `Category` above `Lighting`.

```excel
=DMAX(A1:E8, "Units", G1:G2)
```

**Result:** `12`

The two lighting records have 12 and 6 units, so the maximum is 12.

<!-- Image 2: Conditions on the Same Row Versus Separate Rows. See Images/Database/DMAX.md -->

### Example 3: Conditions on Separate Rows (OR Logic)

Criteria in `G1:G3`: `Store` above `Riverside`, then `Lakeview` on the next row.

```excel
=DMAX(A1:E8, "Price", G1:G3)
```

**Result:** `220`

Riverside has prices of 220, 35 and 55, and Lakeview has 40 and 60. The largest of these five values is 220.

### Example 4: Field by Column Number

Criteria in `G1:G2`: `Category` above `Storage`.

```excel
=DMAX(A1:E8, 5, G1:G2)
```

**Result:** `60`

The number 5 points at the fifth column, `Price`. The storage records have prices of 60 and 55, so the maximum is 60.

## Story Problems

### Problem 1: Peak Rainfall at a Station

A weather log records monthly rainfall in millimeters for two stations in `A1:C6`.

| Station | Month | Rainfall |
| --- | --- | --- |
| Ridge | Jan | 42 |
| Ridge | Feb | 55 |
| Delta | Jan | 30 |
| Delta | Feb | 18 |
| Ridge | Mar | 61 |

**Task:** Put `Station` in `E1` and `Ridge` in `E2`, then find the wettest month's rainfall at Ridge.

**Solution:**

```excel
=DMAX(A1:C6, "Rainfall", E1:E2)
```

**Answer:** `61`, the March value at Ridge, which is higher than the January (42) and February (55) values.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DMAX.md -->

### Problem 2: Longest Build Task

A project tracker logs hours for each task in `A1:C6`.

| Project | Task | Hours |
| --- | --- | --- |
| Atlas | Build | 40 |
| Atlas | Test | 25 |
| Orion | Build | 52 |
| Orion | Test | 18 |
| Atlas | Build | 33 |

**Task:** Put `Task` in `E1` and `Build` in `E2`, then find the largest number of hours logged on any build task.

**Solution:**

```excel
=DMAX(A1:C6, "Hours", E1:E2)
```

**Answer:** `52`, the Orion build. The Atlas builds (40 and 33) and all test tasks are lower.

## Use Cases

### Peak Rainfall Reports

**Scenario:** A utility compares the highest monthly rainfall for whichever station an analyst selects from a drop-down.

```excel
=DMAX(Rainfall, "Millimeters", StationFilter)
```

**Why It Works:** The named criteria range keeps the formula fixed while the selected station changes, and the result is the peak value for that station.

### Project Workload Peaks

**Scenario:** A planning lead finds the largest single task in each project to decide where to add staff.

```excel
=DMAX(Tasks, "Hours", ProjectFilter)
```

**Why It Works:** Each project has its own criteria cell, so the maximum reflects only that project's tasks.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Unexpected maximum | A blank cell under a label in the criteria range matches every record. | Size the criteria range to the condition rows only. |
| Unexpected maximum | Text criteria match more values than intended, such as `East` matching `Eastern`. | Use `="=East"` in the criteria cell for an exact match. |
| Wrong value | The field is a text column or a column number points at the wrong column. | Use the header label of a numeric column, in quotes. |
| Unexpected result | The criteria labels do not match the database headers. | Copy the header cells into the criteria range. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel for Microsoft 365, Excel 2016 and later, and Excel for the web | Criteria accept wildcards and comparison operators. |
| Google Sheets | Available | Same three arguments. The help page does not explain criteria syntax in detail, so test criteria before sharing. |

## Tips and Best Practices

- Use MAX on a plain range when no conditions are needed, since it is simpler.
- Confirm the criteria with DCOUNT first; a maximum over an empty set is not a meaningful result.
- Keep the criteria range above or beside the list, never below it.
- Use header labels rather than column numbers so inserted columns do not break the formula.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DGET](DGET.md) | Returns the single matching value rather than the largest one. |
| [DMIN](DMIN.md) | Returns the smallest matching value. |
| [MAX](../Statistical/MAX.md) | Finds the largest number in a plain range with no criteria. |
| [MAXIFS](../Statistical/MAXIFS.md) | Finds the largest value that meets conditions written inside the formula. |

## Official Documentation

- [Microsoft Support: DMAX function](https://support.microsoft.com/en-us/excel/functions/dmax-function)
- [Google Docs Editors Help: DMAX](https://support.google.com/docs/answer/3094227)
