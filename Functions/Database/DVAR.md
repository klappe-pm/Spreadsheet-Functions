---
domain: Spreadsheet Functions
category: Database
subcategory: Database Statistics
purpose:
  - Database Queries
  - Statistical Analysis
use-case:
  - Lot Height Variance
  - Tree Growth Variance
related:
  - DSTDEV
  - DVARP
  - VAR
  - VAR.S
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/dvar-function
  - https://support.google.com/docs/answer/3094236
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Sample Variance
  - Variance With Criteria
tags:
  - criteria
  - database
  - excel
  - sheets
  - statistics
---

# DVAR

## Description

**DVAR** estimates the variance of a field (column) of a list, considering only the records that match the conditions in a separate criteria range. The variance measures how far the values spread from their average, expressed in squared units. The matching records are treated as a sample of a larger population, so the calculation divides by one less than the number of records. The list is a range where the first row holds column labels and every row below it is a record.

Use DVAR when the records that match a condition are a sample of a larger process, such as the growth of trees in one plot, and you want the variance of that group. When the records are the complete set, use DVARP. DVAR is the squared form of DSTDEV, so take the square root of the result to compare it with a standard deviation.

For a variance of a plain range with no conditions, VAR.S is the equivalent function. DVAR is the better fit when the conditions are edited on the sheet or when OR logic across rows is needed. Microsoft describes DVAR as estimating the variance from a sample, and the same sample-based calculation is described on the Google Sheets help page.

## Syntax

```excel
=DVAR(database, field, criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DVAR.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:C6`. Each column needs a label in the first row. |
| `field` | Yes | The column to analyze: a header label in quotes (`"Growth"`), a cell that holds the label, or the column position as a number. |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A number: the sample variance of the field values among the records that match the criteria. At least two matching numeric values are needed for a variance to exist.

## Examples

All examples use this class list in `A1:D9`, the same records used on the DSTDEV page.

| Class | Student | Score | Hours |
| --- | --- | --- | --- |
| Algebra | Ana | 82 | 3 |
| Algebra | Ben | 75 | 2 |
| Algebra | Cy | 91 | 5 |
| Biology | Dev | 68 | 1 |
| Biology | Eli | 88 | 4 |
| Biology | Fay | 79 | 3 |
| Chemistry | Gus | 94 | 6 |
| Chemistry | Hana | 71 | 2 |

### Example 1: Score Variance in One Class

Criteria in `F1:F2`: `Class` above `Algebra`.

```excel
=DVAR(A1:D9, "Score", F1:F2)
```

**Result:** `64.33` (rounded)

The three Algebra scores have a sample variance of about 64.33. Its square root, about 8.02, is the DSTDEV result for the same records.

### Example 2: Two Conditions With AND Logic

Criteria in `F1:G2`: `Class` and `Hours` on the same row, with `Biology` and `>=3` beneath them.

```excel
=DVAR(A1:D9, "Score", F1:G2)
```

**Result:** `40.50`

Only Eli (88) and Fay (79) qualify. Their sample variance is 40.5.

<!-- Image 2: Conditions on the Same Row Versus Separate Rows. See Images/Database/DVAR.md -->

### Example 3: Conditions on Separate Rows (OR Logic)

Criteria in `F1:F3`: `Class` above `Biology`, then `Chemistry` on the next row.

```excel
=DVAR(A1:D9, "Score", F1:F3)
```

**Result:** `121.50`

Five scores are included: 68, 88, 79, 94 and 71. Their sample variance is 121.5.

### Example 4: Whole Column With a Blank Criteria Cell

Criteria in `F1:F2`: `Class` above a blank cell.

```excel
=DVAR(A1:D9, "Score", F1:F2)
```

**Result:** `89.71` (rounded)

A blank cell under a label matches every record, so all eight scores are used.

## Story Problems

### Problem 1: Plant Height Variance in One Lot

A nursery measures the height in centimeters of seedlings from two lots in `A1:B7`. The team treats the measured seedlings in lot L2 as a sample of all seedlings grown from that supplier.

| Lot | Height |
| --- | --- |
| L1 | 28 |
| L2 | 30 |
| L2 | 36 |
| L1 | 31 |
| L2 | 33 |
| L1 | 27 |

**Task:** Put `Lot` in `D1` and `L2` in `D2`, then estimate the variance of the lot L2 heights.

**Solution:**

```excel
=DVAR(A1:B7, "Height", D1:D2)
```

**Answer:** `9`. The three lot L2 heights are 30, 36 and 33, with a mean of 33. Their squared deviations are 9, 9 and 0, which add to 18. Dividing by 2 gives a sample variance of 9.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DVAR.md -->

### Problem 2: Tree Growth in One Plot

A forester records the growth in centimeters for trees in two plots in `A1:B6`. The four trees in plot P1 are a sample of the plots on the estate.

| Plot | Growth |
| --- | --- |
| P1 | 10 |
| P2 | 25 |
| P1 | 14 |
| P1 | 12 |
| P1 | 16 |

**Task:** Put `Plot` in `D1` and `P1` in `D2`, then estimate the variance of growth in plot P1.

**Solution:**

```excel
=DVAR(A1:B6, "Growth", D1:D2)
```

**Answer:** `6.67` (rounded). The four values average 13, and their squared deviations add to 20. Dividing by 3 gives a sample variance of 6.67.

## Use Cases

### Lot Height Variance

**Scenario:** A nursery compares how uniform the seedling heights are across supplier lots, choosing each lot from a drop-down.

```excel
=DVAR(Measurements, "Height", LotFilter)
```

**Why It Works:** A lower variance means more uniform heights. The criteria cell lets the team compare lots without rewriting the formula.

### Tree Growth Variance

**Scenario:** A forestry team estimates how much growth varies from tree to tree within a plot that was sampled.

```excel
=DVAR(Growth, "Centimeters", PlotFilter)
```

**Why It Works:** The sample variance reflects the uncertainty of a sampled plot, which is the right measure when the plot is not fully measured.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Variance looks too large or too small | DVARP was used for a sample, or DVAR for a complete set. | Use DVAR for a sample and DVARP for the whole population. |
| Unexpected result | A blank cell under a label in the criteria range matches every record. | Size the criteria range to the condition rows only. |
| No meaningful variance | Only one record matches, and a single value has no spread. | Widen the criteria so at least two values match. |
| Unexpected result | Text criteria match more values than intended, such as `P1` matching `P10`. | Use `="=P1"` in the criteria cell for an exact match. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft Excel, including Excel for the web | Estimates the population variance from a sample. Criteria accept wildcards and comparison operators. |
| Google Sheets | Available | Same three arguments and the same sample-based variance. The help page does not explain criteria syntax in detail, so test criteria before sharing. |

## Tips and Best Practices

- Take the square root of DVAR to compare the spread with the units of the original data.
- Use DVARP when the matching records are the full population.
- Confirm the matching count with DCOUNT before reporting a variance from a small group.
- Keep the criteria range above or beside the list, never below it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DSTDEV](DSTDEV.md) | Sample standard deviation for the same records; the square root of DVAR. |
| [DVARP](DVARP.md) | Population variance for the same records. |
| [VAR](../Statistical/VAR.md) | Sample variance of a plain range with no criteria. |
| [VAR.S](../Statistical/VAR.S.md) | Current name for the sample variance of a plain range with no criteria. |

## Official Documentation

- [Microsoft Support: DVAR function](https://support.microsoft.com/en-us/excel/functions/dvar-function)
- [Google Docs Editors Help: DVAR](https://support.google.com/docs/answer/3094236)
