---
domain: Spreadsheet Functions
category: Database
subcategory: Database Statistics
purpose:
  - Database Queries
  - Statistical Analysis
use-case:
  - Bolt Length Variation
  - Quiz Score Spread
related:
  - DAVERAGE
  - DSTDEVP
  - DVAR
  - STDEV.P
  - STDEV.S
level: 4
source:
  - https://support.microsoft.com/en-us/excel/functions/dstdev-function
  - https://support.google.com/docs/answer/3094151
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Database Sample Standard Deviation
  - Standard Deviation With Criteria
tags:
  - criteria
  - database
  - excel
  - sheets
  - statistics
---

# DSTDEV

## Description

**DSTDEV** estimates the standard deviation of a field (column) of a list, considering only the records that match the conditions in a separate criteria range. It treats the matching records as a sample drawn from a larger population, which is the usual situation when the list holds only some of the items being studied. The list is a range where the first row holds column labels and every row below it is a record.

Use DSTDEV to measure how spread out the values are within a group selected by conditions, such as the variation in bolt lengths for one batch or the spread of quiz scores for one class. When the records are the complete set you care about, use DSTDEVP instead. The difference matters most for small groups, because the sample version divides by one less than the number of values.

For a standard deviation of a plain range with no conditions, STDEV.S is the equivalent function. DSTDEV is the better fit when the conditions are edited on the sheet or when OR logic across rows is needed. Google Sheets describes the same sample-based calculation on its help page.

## Syntax

```excel
=DSTDEV(database, field, criteria)
```

<!-- Image 1: Database, Field and Criteria Ranges. See Images/Database/DSTDEV.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `database` | Yes | The whole list including its header row, for example `A1:D9`. Each column needs a label in the first row. |
| `field` | Yes | The column to analyze: a header label in quotes (`"Score"`), a cell that holds the label, or the column position as a number (`3` for the third column). |
| `criteria` | Yes | A range with at least one header label and at least one condition cell below it. Conditions on the same row combine with AND; conditions on different rows combine with OR. |

### Return Value

A number: the sample standard deviation of the field values among the records that match the criteria. At least two matching numeric values are needed for a spread to exist.

## Examples

All examples use this class list in `A1:D9`.

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

### Example 1: Spread of Scores in One Class

Criteria in `F1:F2`: `Class` above `Algebra`.

```excel
=DSTDEV(A1:D9, "Score", F1:F2)
```

**Result:** `8.02` (rounded)

The three Algebra scores are 82, 75 and 91. Their sample standard deviation is about 8.02.

### Example 2: Two Conditions With AND Logic

Criteria in `F1:G2`: `Class` and `Hours` on the same row, with `Biology` and `>=3` beneath them.

```excel
=DSTDEV(A1:D9, "Score", F1:G2)
```

**Result:** `6.36` (rounded)

Two Biology students studied at least three hours: Eli (88) and Fay (79). Their sample standard deviation is about 6.36.

<!-- Image 2: Conditions on the Same Row Versus Separate Rows. See Images/Database/DSTDEV.md -->

### Example 3: Conditions on Separate Rows (OR Logic)

Criteria in `F1:F3`: `Class` above `Biology`, then `Chemistry` on the next row.

```excel
=DSTDEV(A1:D9, "Score", F1:F3)
```

**Result:** `11.02` (rounded)

Five scores are included: 68, 88, 79, 94 and 71. Their sample standard deviation is about 11.02.

### Example 4: Whole Column With a Blank Criteria Cell

Criteria in `F1:F2`: `Class` above a blank cell.

```excel
=DSTDEV(A1:D9, "Score", F1:F2)
```

**Result:** `9.47` (rounded)

A blank cell under a label matches every record, so all eight scores are used.

## Story Problems

### Problem 1: Bolt Length Variation

A machine shop measures bolt lengths in millimeters for two production batches in `A1:B7`. The team wants the spread within batch B, which is treated as a sample of the process.

| Batch | Length |
| --- | --- |
| B | 50 |
| B | 52 |
| B | 54 |
| B | 48 |
| A | 61 |
| A | 59 |

**Task:** Put `Batch` in `D1` and `B` in `D2`, then estimate the standard deviation of batch B lengths.

**Solution:**

```excel
=DSTDEV(A1:B7, "Length", D1:D2)
```

**Answer:** `2.58` (rounded). The four lengths average 51, and their squared deviations add to 20. Dividing by 3 gives a sample variance of 6.67, and its square root is 2.58.

<!-- Image 3: Results Panel for the Story Problems. See Images/Database/DSTDEV.md -->

### Problem 2: Quiz Score Spread for One Team

A coach records quiz scores for two teams in `A1:B7`.

| Team | Quiz |
| --- | --- |
| X | 6 |
| X | 8 |
| Y | 9 |
| X | 10 |
| X | 8 |
| Y | 4 |

**Task:** Put `Team` in `D1` and `X` in `D2`, then estimate how spread out Team X's quiz scores are.

**Solution:**

```excel
=DSTDEV(A1:B7, "Quiz", D1:D2)
```

**Answer:** `1.63` (rounded). Team X's scores are 6, 8, 10 and 8, with a mean of 8 and squared deviations that add to 8. The sample variance is 8 divided by 3, and its square root is 1.63.

## Use Cases

### Bolt Length Variation

**Scenario:** A quality engineer tracks how much bolt length varies within one batch, with the batch name chosen from a drop-down.

```excel
=DSTDEV(Measurements, "Length", BatchFilter)
```

**Why It Works:** The criteria cell limits the calculation to one batch, so results can be compared across batches without rewriting the formula.

### Quiz Score Spread

**Scenario:** A teacher compares how consistently students in each class scored on the same quiz.

```excel
=DSTDEV(Scores, "Score", ClassFilter)
```

**Why It Works:** A larger value means the class's results were more widely spread. Pair it with DAVERAGE to show both the center and the spread.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Spread looks too large or too small | DSTDEVP was used for a sample, or DSTDEV for a complete set. | Use DSTDEV when the records are a sample and DSTDEVP when they are the whole population. |
| Unexpected result | A blank cell under a label in the criteria range matches every record. | Size the criteria range to the condition rows only. |
| No meaningful spread | Only one record matches, and a single value has no spread. | Widen the criteria so at least two values match. |
| Unexpected result | Text criteria match more values than intended, such as `Bio` matching `Biology`. | Use `="=Bio"` in the criteria cell for an exact match. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in Excel for Microsoft 365, Excel 2016 and later, and Excel for the web | Estimates the population standard deviation from a sample. Criteria accept wildcards and comparison operators. |
| Google Sheets | Available | Same three arguments and the same sample-based calculation. The help page does not explain criteria syntax in detail, so test criteria before sharing. |

## Tips and Best Practices

- Choose DSTDEV only when the matching records are a sample; for a full population, use DSTDEVP.
- Report the mean with DAVERAGE next to the spread so readers can judge the variation fairly.
- Confirm the number of matching records with DCOUNT before trusting a spread from a small group.
- Keep the criteria range above or beside the list, never below it.

## Related Functions

| Function | Relationship |
| --- | --- |
| [DAVERAGE](DAVERAGE.md) | Gives the average for the same matching records, to pair with the spread. |
| [DSTDEVP](DSTDEVP.md) | Uses the same criteria but treats the matching records as the whole population. |
| [DVAR](DVAR.md) | Returns the variance, the squared version of this spread, for the same records. |
| [STDEV.P](../Statistical/STDEV.P.md) | Population standard deviation of a plain range with no criteria. |
| [STDEV.S](../Statistical/STDEV.S.md) | Sample standard deviation of a plain range with no criteria. |

## Official Documentation

- [Microsoft Support: DSTDEV function](https://support.microsoft.com/en-us/excel/functions/dstdev-function)
- [Google Docs Editors Help: DSTDEV](https://support.google.com/docs/answer/3094151)
