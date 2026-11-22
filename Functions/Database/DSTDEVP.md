---
domain: Spreadsheet Functions
category: Database
subcategory: Database Statistics
purpose:
  - Database Queries
  - Statistical Analysis
use-case:
  - Full Production Run Checks
  - Season Score Spread
related:
  - DSTDEV
  - DVARP
  - STDEV.P
  - STDEV.S
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/dstdevp-function
  - https://support.google.com/docs/answer/3094280
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Population Standard Deviation
  - Population Spread With Criteria
tags:
  - criteria
  - database
  - excel
  - sheets
  - statistics
---

# DSTDEVP

## Description

**DSTDEVP** calculates the standard deviation of a field (column) of a list, considering only the records that match the conditions in a separate criteria range. It treats the matching records as the entire population you care about, so it divides by the number of records rather than one less. The list is a range where the first row holds column labels and every row below it is a record.

Use DSTDEVP when the matching records are the complete set, such as every bolt in one production run or every test score from one season. When the records are only a sample of a larger process, use DSTDEV instead. For small groups the two results differ noticeably, so the choice should be made deliberately.

For a standard deviation of a plain range with no conditions, STDEV.P is the population equivalent. DSTDEVP is the better fit when the conditions are edited on the sheet or when OR logic across rows is needed. Microsoft's help page does not describe the result when no record matches, so check the criteria before relying on the output.

## Syntax

```excel
=DSTDEVP(database, field, criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DSTDEVP.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:B7`. Each column needs a label in the first row. |
| `field` | Yes | The column to analyze: a header label in quotes (`"Length"`), a cell that holds the label, or the column position as a number. |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A number: the population standard deviation of the field values among the records that match the criteria.

## Examples

All examples use this class list in `A1:D9`. The same records are used on the DSTDEV page, so the population and sample results can be compared.

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

### Example 1: Population Spread of One Class

Criteria in `F1:F2`: `Class` above `Algebra`.

```excel
=DSTDEVP(A1:D9, "Score", F1:F2)
```

**Result:** `6.55` (rounded)

If the three Algebra students are the whole group of interest, the population standard deviation of 82, 75 and 91 is about 6.55.

### Example 2: Two Conditions With AND Logic

Criteria in `F1:G2`: `Class` and `Hours` on the same row, with `Biology` and `>=3` beneath them.

```excel
=DSTDEVP(A1:D9, "Score", F1:G2)
```

**Result:** `4.50`

The two qualifying Biology scores are 88 and 79. Their population standard deviation is exactly 4.5.

<!-- Image 2: Conditions on the Same Row Versus Separate Rows. See Images/Database/DSTDEVP.md -->

### Example 3: Conditions on Separate Rows (OR Logic)

Criteria in `F1:F3`: `Class` above `Biology`, then `Chemistry` on the next row.

```excel
=DSTDEVP(A1:D9, "Score", F1:F3)
```

**Result:** `9.86` (rounded)

Five scores are included: 68, 88, 79, 94 and 71. Their population standard deviation is about 9.86.

### Example 4: Whole Column With a Blank Criteria Cell

Criteria in `F1:F2`: `Class` above a blank cell.

```excel
=DSTDEVP(A1:D9, "Score", F1:F2)
```

**Result:** `8.86` (rounded)

A blank cell under a label matches every record, so all eight scores are treated as the full population.

## Story Problems

### Problem 1: Full Production Run Check

A factory measures every bolt in one production run, so the run is the entire population for that check. Lengths are in millimeters and are stored in `A1:B7`.

| Run | Length |
| --- | --- |
| R7 | 50 |
| R7 | 52 |
| R7 | 54 |
| R7 | 48 |
| R8 | 61 |
| R8 | 59 |

**Task:** Put `Run` in `D1` and `R7` in `D2`, then find the population standard deviation of the run R7 lengths.

**Solution:**

```excel
=DSTDEVP(A1:B7, "Length", D1:D2)
```

**Answer:** `2.24` (rounded). The four lengths average 51 and their squared deviations add to 20. Dividing by 4 gives a population variance of 5, and its square root is 2.24.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DSTDEVP.md -->

### Problem 2: Spring Test Spread

A teacher gives three spring tests and treats them as the complete set for the term's spring unit. The scores are in `A1:B5`.

| Season | Score |
| --- | --- |
| Spring | 60 |
| Spring | 70 |
| Spring | 80 |
| Fall | 90 |

**Task:** Put `Season` in `D1` and `Spring` in `D2`, then find the population standard deviation of the spring scores.

**Solution:**

```excel
=DSTDEVP(A1:B5, "Score", D1:D2)
```

**Answer:** `8.16` (rounded). The three scores average 70 and their squared deviations add to 200. Dividing by 3 gives a population variance of 66.67, and its square root is 8.16.

## Use Cases

### Full Production Run Checks

**Scenario:** A quality team confirms the spread of every part in one completed run, with the run ID chosen from a drop-down.

```excel
=DSTDEVP(Measurements, "Length", RunFilter)
```

**Why It Works:** Because the run is fully measured, dividing by the full count is the correct choice, and the criteria cell lets the team switch runs without editing the formula.

### Season Score Spread

**Scenario:** A coach measures the spread of all scores from one season, where every score in the season is included.

```excel
=DSTDEVP(Scores, "Score", SeasonFilter)
```

**Why It Works:** The season is the whole population of interest, so the population version describes it accurately.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Spread looks slightly too small | The records are a sample, but DSTDEVP was used. | Use DSTDEV for a sample of a larger process. |
| Unexpected result | A blank cell under a label in the criteria range matches every record. | Size the criteria range to the condition rows only. |
| No meaningful spread | Too few records match the criteria to show any variation. | Check the matching count with DCOUNT and widen the criteria if needed. |
| Unexpected result | Text criteria match more values than intended, such as `Spr` matching `Spring Break`. | Use `="=Spring"` in the criteria cell for an exact match. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel for Microsoft 365, Excel 2016 and later, and Excel for the web | Uses the entire matching population. Criteria accept wildcards and comparison operators. |
| Google Sheets | Available | Same three arguments and a population-based result. The help page does not explain criteria syntax in detail, so test criteria before sharing. |

## Tips and Best Practices

- Use DSTDEVP only when the matching records are the whole population; otherwise use DSTDEV.
- Check the count of matching records with DCOUNT so the population is what you think it is.
- Pair the result with DAVERAGE to show both the center and the spread.
- Keep the criteria range above or beside the list, never below it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DSTDEV](DSTDEV.md) | Same criteria, but treats the matching records as a sample. |
| [DVARP](DVARP.md) | Population variance for the same records, the squared version of this spread. |
| [STDEV.P](../Statistical/STDEV.P.md) | Population standard deviation of a plain range with no criteria. |
| [STDEV.S](../Statistical/STDEV.S.md) | Sample standard deviation of a plain range with no criteria. |

## Official Documentation

- [Microsoft Support: DSTDEVP function](https://support.microsoft.com/en-us/excel/functions/dstdevp-function)
- [Google Docs Editors Help: DSTDEVP](https://support.google.com/docs/answer/3094280)
