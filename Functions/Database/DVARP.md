---
domain: Spreadsheet Functions
category: Database
subcategory: Database Statistics
purpose:
  - Database Queries
  - Statistical Analysis
use-case:
  - Complete Lot Variance
  - Full Season Variance
related:
  - DSTDEVP
  - DVAR
  - VAR
  - VAR.P
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/dvarp-function
  - https://support.google.com/docs/answer/3094238
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Population Variance
  - Population Variance With Criteria
tags:
  - criteria
  - database
  - excel
  - sheets
  - statistics
---

# DVARP

## Description

**DVARP** calculates the variance of a field (column) of a list, considering only the records that match the conditions in a separate criteria range. The matching records are treated as the entire population, so the calculation divides by the number of records rather than one less. The list is a range where the first row holds column labels and every row below it is a record.

Use DVARP when the matching records are the complete set you want to describe, such as every seedling in one lot that was measured or every tree in a fully counted plot. When the records are a sample of a larger process, use DVAR instead. The variance is in squared units, so take the square root of the result to compare it with the standard deviation from DSTDEVP.

For a variance of a plain range with no conditions, VAR.P is the population equivalent. DVARP is the better fit when the conditions are edited on the sheet or when OR logic across rows is needed. Microsoft's help page does not describe the result when no record matches, so check the criteria before relying on the output.

## Syntax

```excel
=DVARP(database, field, criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DVARP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:C6`. Each column needs a label in the first row. |
| `field` | Yes | The column to analyze: a header label in quotes (`"Growth"`), a cell that holds the label, or the column position as a number. |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A number: the population variance of the field values among the records that match the criteria.

## Examples

All examples use this class list in `A1:D9`, the same records used on the DSTDEV page, so the population and sample results can be compared.

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

### Example 1: Population Variance of One Class

Criteria in `F1:F2`: `Class` above `Algebra`.

```excel
=DVARP(A1:D9, "Score", F1:F2)
```

**Result:** `42.89` (rounded)

Treating the three Algebra students as the whole group, the population variance is about 42.89. Its square root, about 6.55, is the DSTDEVP result for the same records.

### Example 2: Two Conditions With AND Logic

Criteria in `F1:G2`: `Class` and `Hours` on the same row, with `Biology` and `>=3` beneath them.

```excel
=DVARP(A1:D9, "Score", F1:G2)
```

**Result:** `20.25`

Only Eli (88) and Fay (79) qualify. Their population variance is 20.25.

<!-- Image 2: Conditions on the Same Row Versus Separate Rows. See Images/Database/DVARP.md -->

### Example 3: Conditions on Separate Rows (OR Logic)

Criteria in `F1:F3`: `Class` above `Biology`, then `Chemistry` on the next row.

```excel
=DVARP(A1:D9, "Score", F1:F3)
```

**Result:** `97.20`

Five scores are included: 68, 88, 79, 94 and 71. Their population variance is 97.2.

### Example 4: Whole Column With a Blank Criteria Cell

Criteria in `F1:F2`: `Class` above a blank cell.

```excel
=DVARP(A1:D9, "Score", F1:F2)
```

**Result:** `78.50`

A blank cell under a label matches every record, so all eight scores are treated as the population.

## Story Problems

### Problem 1: Complete Lot Height Variance

A nursery measures the height in centimeters of every seedling in lot L2 and treats those seedlings as the whole population for that lot. The data is in `A1:B7`.

| Lot | Height |
| --- | --- |
| L1 | 28 |
| L2 | 30 |
| L2 | 36 |
| L1 | 31 |
| L2 | 33 |
| L1 | 27 |

**Task:** Put `Lot` in `D1` and `L2` in `D2`, then find the population variance of the lot L2 heights.

**Solution:**

```excel
=DVARP(A1:B7, "Height", D1:D2)
```

**Answer:** `6`. The three heights average 33 and their squared deviations add to 18. Dividing by 3 gives a population variance of 6.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DVARP.md -->

### Problem 2: Growth Across a Fully Counted Plot

A forester measures every tree in plot P1 and records its growth in centimeters in `A1:B6`. Plot P2 is not part of this count.

| Plot | Growth |
| --- | --- |
| P1 | 10 |
| P2 | 25 |
| P1 | 14 |
| P1 | 12 |
| P1 | 16 |

**Task:** Put `Plot` in `D1` and `P1` in `D2`, then find the population variance of growth in plot P1.

**Solution:**

```excel
=DVARP(A1:B6, "Growth", D1:D2)
```

**Answer:** `5`. The four values average 13 and their squared deviations add to 20. Dividing by 4 gives a population variance of 5.

## Use Cases

### Complete Lot Variance

**Scenario:** A nursery measures every seedling in a lot and reports how uniform that lot is, with the lot chosen from a drop-down.

```excel
=DVARP(Measurements, "Height", LotFilter)
```

**Why It Works:** When the whole lot is measured, the population variance is the accurate description, and the criteria cell lets the team switch lots without editing the formula.

### Full Season Variance

**Scenario:** A coach describes the spread of every score recorded in one season.

```excel
=DVARP(Scores, "Score", SeasonFilter)
```

**Why It Works:** The season is the complete set of interest, so the population calculation matches the question being asked.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Variance looks slightly too small | The records are a sample, but DVARP was used. | Use DVAR for a sample of a larger process. |
| Unexpected result | A blank cell under a label in the criteria range matches every record. | Size the criteria range to the condition rows only. |
| No meaningful variance | Too few records match the criteria to show any variation. | Check the matching count with DCOUNT and widen the criteria if needed. |
| Unexpected result | Text criteria match more values than intended, such as `P1` matching `P10`. | Use `="=P1"` in the criteria cell for an exact match. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Microsoft Excel, including Excel for the web | Calculates the variance of the entire matching population. Criteria accept wildcards and comparison operators. |
| Google Sheets | Available | Same three arguments and a population-based result. The help page does not explain criteria syntax in detail, so test criteria before sharing. |

## Tips and Best Practices

- Use DVARP only when the matching records are the complete population; otherwise use DVAR.
- Take the square root of DVARP to compare the spread with the units of the original data.
- Confirm the matching count with DCOUNT before reporting a variance.
- Keep the criteria range above or beside the list, never below it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DSTDEVP](DSTDEVP.md) | Population standard deviation for the same records; the square root of DVARP. |
| [DVAR](DVAR.md) | Sample variance for the same records. |
| [VAR.P](../Statistical/VAR.P.md) | Population variance of a plain range with no criteria. |
| [VAR](../Statistical/VAR.md) | Sample variance of a plain range with no criteria, the legacy form. |

## Official Documentation

- [Microsoft Support: DVARP function](https://support.microsoft.com/en-us/excel/functions/dvarp-function)
- [Google Docs Editors Help: DVARP](https://support.google.com/docs/answer/3094238)
