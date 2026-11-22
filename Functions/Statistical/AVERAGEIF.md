---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
purpose:
  - Aggregation
  - Conditional Logic
use-case:
  - Department Pay Averages
  - Order Size Analysis
  - Regional Sales Averages
related:
  - AVERAGE
  - AVERAGEIFS
  - COUNTIF
  - IFERROR
  - SUMIF
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/averageif-function
  - https://support.google.com/docs/answer/3256529
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Conditional Average
tags:
  - averages
  - conditional
  - criteria
  - excel
  - sheets
---

# AVERAGEIF

## Description

**AVERAGEIF** averages the cells in a range that meet one condition. You give it the range to test, the condition, and an optional range of numbers to average. If you leave out the average range, the function averages the cells it tested. The condition can be a number, a comparison such as `">10"`, a cell reference, or text.

Use AVERAGEIF when only some rows should count, such as the average hours for one team or the average order size above a minimum. It replaces a pattern that would otherwise need a helper column or an array formula. When the test is on a different column from the numbers, pass both ranges and keep them the same size.

AVERAGEIF handles one condition. For two or more conditions, use AVERAGEIFS, which takes the average range first. AVERAGE takes no condition at all. The function works the same way in Excel and Google Sheets, but the two help pages describe the no-match result differently, so test that case in your own file.

## Syntax

```excel
=AVERAGEIF(range, criteria, [average_range])
```

<!-- Image 1: Syntax Anatomy. See Images/Statistical/AVERAGEIF.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `range` | Yes | The cells to test against the criteria. They can hold numbers, text, or references to them. In Google Sheets this argument is named `criteria_range`. |
| `criteria` | Yes | The condition that decides which cells are averaged. It can be a number, a comparison such as `">=10"`, a cell reference, or text. Use `"<>Ops"` for "not equal to". |
| `average_range` | No | The numbers to average. Cells in this range line up with the matching cells in `range`, starting at the top-left cell. If omitted, `range` itself is averaged. In Excel, a different-sized average range is resized to match `range`. |

### Return Value

A number: the arithmetic mean of the cells in `average_range` whose matching cells in `range` meet the criteria. Excel returns `#DIV/0!` when no cell meets the criteria. Empty cells in the average range are ignored, and TRUE or FALSE cells in `range` are ignored.

## Examples

All examples use this list in `A1:B7`, with the team in column A and hours worked in column B.

| Team | Hours |
| --- | --- |
| Ops | 12 |
| Sales | 8 |
| Ops | 15 |
| Support | 6 |
| Sales | 10 |
| Ops | 9 |

### Example 1: Text Criterion

```excel
=AVERAGEIF(A2:A7, "Ops", B2:B7)
```

**Result:** `12`

The Ops rows hold 12, 15 and 9. Their total is 36, and dividing by three gives 12.

### Example 2: Comparison Criterion

```excel
=AVERAGEIF(B2:B7, ">=10")
```

**Result:** `12.33`

No average range is given, so the function averages the hours themselves. The values 12, 15 and 10 total 37. Dividing by three gives 12.333, shown here rounded to two decimals.

<!-- Image 2: Criteria Matching Rows. See Images/Statistical/AVERAGEIF.md -->

### Example 3: Not Equal To

```excel
=AVERAGEIF(A2:A7, "<>Ops", B2:B7)
```

**Result:** `8`

Every row that is not Ops qualifies: Sales (8 and 10) and Support (6). The three values total 24, and 24 divided by 3 is 8.

### Example 4: Wildcard Match

```excel
=AVERAGEIF(A2:A7, "Sa*", B2:B7)
```

**Result:** `9`

The asterisk matches any text that starts with "Sa", which covers both Sales rows. Their hours are 8 and 10, and the average is 9. The wildcard `?` matches exactly one character.

### Example 5: Averaging the Tested Range

```excel
=AVERAGEIF(B2:B7, ">10")
```

**Result:** `13.5`

Only 12 and 15 are greater than 10. Their average is 13.5. Without a third argument, the same range is both tested and averaged.

## Story Problems

### Problem 1: Support Response Times for High Priority Tickets

A help desk logs each ticket's priority and the hours to first response in `A1:B6`.

| Priority | Hours |
| --- | --- |
| High | 2 |
| Low | 30 |
| High | 4 |
| Medium | 12 |
| High | 3 |

**Task:** Find the average first-response time for High priority tickets.

**Solution:**

```excel
=AVERAGEIF(A2:A6, "High", B2:B6)
```

**Answer:** `3` hours. The three High tickets take 2, 4 and 3 hours, which total 9, and 9 divided by 3 is 3.

### Problem 2: Average Size of Larger Orders

An online shop lists five order amounts in `A1:B6`. The owner wants the average of orders above 100.

| Order | Amount |
| --- | --- |
| A-101 | 80 |
| A-102 | 150 |
| A-103 | 220 |
| A-104 | 95 |
| A-105 | 310 |

**Task:** Average only the orders whose amount is greater than 100.

**Solution:**

```excel
=AVERAGEIF(B2:B6, ">100")
```

**Answer:** `226.67`. The qualifying orders are 150, 220 and 310. They total 680, and 680 divided by 3 is 226.67 when rounded to two decimals.

<!-- Image 3: Results Panel for the Order Problem. See Images/Statistical/AVERAGEIF.md -->

## Use Cases

### Department Pay Averages

**Scenario:** An HR analyst reports the average salary for one department from a staff table.

```excel
=AVERAGEIF(Staff[Department], "Finance", Staff[Salary])
```

**Why It Works:** The structured references keep the two columns aligned as new employees are added. Changing the department name in the formula gives the average for another team.

### Order Size Analysis

**Scenario:** A sales team wants the average order value for orders that reach a free shipping threshold.

```excel
=AVERAGEIF(Orders!C2:C500, ">=75", Orders!C2:C500)
```

**Why It Works:** The threshold can live in a cell, so the team changes the question by editing one value. Use a cell reference such as `">="&$F$1` to do that.

### Regional Sales Averages

**Scenario:** A regional manager compares average deal size across regions, using a cell that holds the region name.

```excel
=IFERROR(AVERAGEIF(Deals[Region], $H2, Deals[Amount]), "No deals")
```

**Why It Works:** IFERROR shows a readable message when a region has no deals yet, instead of the `#DIV/0!` error that Excel returns for an empty match.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#DIV/0!` | No cell in `range` meets the criteria. | Check the spelling of the criterion, or wrap the formula in IFERROR. |
| Unexpected result | The criterion has trailing spaces, so `"Ops "` does not match `Ops`. | Trim the source data with TRIM or correct the criterion. |
| Unexpected result | An asterisk or question mark in the criterion acts as a wildcard. | Put a tilde before the character, for example `"~*"`, to match it literally. |
| Unexpected result | The average range does not line up with the test range. | Give both ranges the same number of rows, starting in the same row. |
| Unexpected result | A text number in `average_range` is not averaged. | Convert it to a number before averaging. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | All versions, including Excel for the web | Uses wildcards, comparison operators and cell references in criteria. An empty criteria cell is treated as 0. |
| Google Sheets | Available | Accepts the same criterion patterns, with the first argument named `criteria_range`. The help page does not describe the no-match result, so check it in your file. |

## Tips and Best Practices

- Keep the test range and the average range the same shape, so each average cell lines up with its test cell.
- Put the criterion in a cell and reference it, so people can change the question without editing the formula.
- Use AVERAGEIFS when a second condition is needed.
- Wrap the formula in IFERROR when a group might have no matching rows.
- Use COUNTIF beside AVERAGEIF to show how many rows the average is based on.

## Related Functions

| Function | Relationship |
| --- | --- |
| [AVERAGE](AVERAGE.md) | Averages every numeric value with no condition. |
| [AVERAGEIFS](AVERAGEIFS.md) | Averages cells that meet two or more conditions. |
| [COUNTIF](COUNTIF.md) | Counts the cells that meet the same kind of condition. |
| [IFERROR](../Logical/IFERROR.md) | Replaces the `#DIV/0!` result when no cells match. |
| [SUMIF](../Math%20%26%20Trig/SUMIF.md) | Adds the matching values instead of averaging them. |

## Official Documentation

- [Microsoft Support: AVERAGEIF function](https://support.microsoft.com/en-us/excel/functions/averageif-function)
- [Google Docs Editors Help: AVERAGEIF](https://support.google.com/docs/answer/3256529)
