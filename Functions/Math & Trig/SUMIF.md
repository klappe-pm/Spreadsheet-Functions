---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Conditional Sums
purpose:
  - Aggregation
  - Conditional Logic
use-case:
  - Category Sales Totals
  - Client Name Totals
  - Expense Category Totals
related:
  - AVERAGEIF
  - COUNTIF
  - DSUM
  - SUMIFS
  - SUMPRODUCT
level: 2
source:
  - https://support.microsoft.com/en-us/excel/functions/sumif-function
  - https://support.google.com/docs/answer/3093583
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Conditional Sum
  - Sum If
tags:
  - conditional
  - criteria
  - excel
  - sheets
  - wildcards
---

# SUMIF

## Description

**SUMIF** adds the values in one range when the matching cells in another range meet a single condition. It checks each cell in the criteria range against the criterion. When a cell matches, SUMIF adds the value in the same position in the sum range. Use it for totals by category, region, status, or any other single test.

The argument order is the reverse of the question you ask. The criteria range comes first, the criterion second, and the sum range last. When you omit the sum range, SUMIF adds the cells in the criteria range that match, which is useful for summing numbers that pass a test such as "greater than 200".

The criterion can be a number, a text value, a cell reference, a comparison such as `">500"`, or a wildcard pattern such as `"North*"`. Wildcards work only with text. For more than one condition, use SUMIFS.

## Syntax

```excel
=SUMIF(range, criteria, [sum_range])
```

<!-- Image 1: Syntax Anatomy. See Images/Math & Trig/SUMIF.md -->

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `range` | Yes | The cells to test against the criterion, such as a column of product names or categories. Dates and numbers are allowed. |
| `criteria` | Yes | The condition that selects rows. Text and expressions with operators must be in quotes, such as `"Apples"` or `">500"`. A cell reference such as `D2` also works. |
| `sum_range` | No | The cells to add when the matching test passes. If omitted, SUMIF adds the cells in `range`. The sum range should be the same size and shape as `range`. |

### Return Value

A single number equal to the total of the sum range (or the range itself when the sum range is omitted) for the rows that match. The function returns 0 when no rows match.

## Examples

All examples use this bakery list in `A2:B7`.

| Product | Revenue |
| --- | --- |
| Croissant | 240 |
| Baguette | 180 |
| Croissant | 310 |
| Muffin | 95 |
| Croissant | 120 |
| Baguette | 210 |

### Example 1: Total for One Product

```excel
=SUMIF(A2:A7, "Croissant", B2:B7)
```

**Result:** `670`

The three Croissant rows hold 240, 310 and 120. The match ignores capital letters, so "croissant" would match as well.

### Example 2: Sum Values Above a Threshold

```excel
=SUMIF(B2:B7, ">200")
```

**Result:** `760`

No sum range is given, so SUMIF adds the revenue values that are greater than 200: 240, 310 and 210.

### Example 3: Exclude One Product

```excel
=SUMIF(A2:A7, "<>Muffin", B2:B7)
```

**Result:** `1060`

The `<>` operator means "not equal to." The total of all revenue is 1155, and removing the Muffin row of 95 gives 1060.

<!-- Image 2: Criteria Patterns. See Images/Math & Trig/SUMIF.md -->

### Example 4: Wildcard Match

```excel
=SUMIF(A2:A7, "Crois*", B2:B7)
```

**Result:** `670`

The asterisk matches any text after "Crois", so the pattern finds the same Croissant rows as Example 1.

### Example 5: Criterion From a Cell

Cell D2 contains `Baguette`.

```excel
=SUMIF(A2:A7, D2, B2:B7)
```

**Result:** `390`

Changing the text in D2 changes the total without editing the formula, which suits reports with a selection cell.

## Story Problems

### Problem 1: Total Owed by Client Name

An accountant keeps a list of unpaid invoices in `A1:B6`. The client names that end with "Co" belong to one group.

| Client | Amount |
| --- | --- |
| Harbor Co | 1250 |
| Lark LLC | 480 |
| Summit Ltd | 2100 |
| Pine Co | 975 |
| Oak Partners | 1500 |

**Task:** Total the amounts for clients whose names end with "Co".

**Solution:**

```excel
=SUMIF(A2:A6, "*Co", B2:B6)
```

**Answer:** `2225`, from Harbor Co (1250) and Pine Co (975). Lark LLC, Summit Ltd and Oak Partners do not end with "Co".

<!-- Image 3: Client Name Wildcard. See Images/Math & Trig/SUMIF.md -->

### Problem 2: Travel Spending in a Cell

A small firm records expenses in `A2:B6` and keeps the category to total in cell `D2`.

| Category | Amount |
| --- | --- |
| Travel | 340 |
| Meals | 85 |
| Travel | 120 |
| Supplies | 60 |
| Travel | 75 |

**Task:** Put `Travel` in D2 and total the Travel amounts.

**Solution:**

```excel
=SUMIF(A2:A6, D2, B2:B6)
```

**Answer:** `535`, from 340 + 120 + 75.

## Use Cases

### Category Sales Totals

**Scenario:** A store exports a transaction log and needs revenue for each product category.

```excel
=SUMIF(C2:C5000, "Electronics", E2:E5000)
```

**Why It Works:** Each category gets its own SUMIF. Put the category names in a summary column and point the formulas at them, so one change to a label updates the report.

### Client Name Totals

**Scenario:** An accounts team sorts clients into groups by a shared word in the company name.

```excel
=SUMIF(B2:B500, "*Partners*", F2:F500)
```

**Why It Works:** The asterisks match the word anywhere in the name. Check the list for spelling variants, because a name that is spelled differently will not match.

### Expense Category Totals

**Scenario:** A department compares actual spending with its budget for one expense category.

```excel
=SUMIF(Expenses[Department], "Marketing", Expenses[Amount])
```

**Why It Works:** Structured table references keep the ranges matched in size and expand as rows are added to the table.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Total is too low or too high | The sum range is a different size from the criteria range. Excel adds the cells that start at the top-left of the sum range and match the size of the criteria range. | Use ranges of the same size and shape. |
| `0` | No rows match, or the numbers in the sum range are stored as text. | Check the spelling of the criterion and convert the text values to numbers. |
| Wrong result for long text | The criterion or matching text is longer than 255 characters, or it equals `#VALUE!`. Excel can return incorrect results in these cases. | Shorten the criterion or match on a shorter key. |
| No match on numbers | A wildcard was used with a numeric criterion. | Use a comparison such as `">100"` for numbers. |
| `#NAME?` | The text criterion is not in quotes. | Put text criteria in quotes, such as `"Apples"`. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Available in all current versions, including Excel for the web | Wildcards are `*`, `?` and `~` for an escaped literal. Matches are not case sensitive. |
| Google Sheets | Available | The wildcards `*`, `?`, `~?`, `~*` and `~~` are supported. Matches are not case sensitive. Regular expressions are not supported. |

## Tips and Best Practices

- Keep the criteria range and the sum range the same size, starting on the same row.
- Store the criterion in a cell and reference it, so the formula stays the same when the question changes.
- Join a comparison operator with a cell reference by using `">"&G1`, so the threshold can come from a cell.
- Use TRIM on the criteria column when stray spaces could prevent a match.
- Switch to SUMIFS when a second condition is needed.

## Related Functions

| Function | Relationship |
| --- | --- |
| [SUMIFS](SUMIFS.md) | Totals rows that meet several conditions. |
| [COUNTIF](../Statistical/COUNTIF.md) | Counts rows that meet the same single condition. |
| [AVERAGEIF](../Statistical/AVERAGEIF.md) | Averages values that meet the same single condition. |
| [SUMPRODUCT](SUMPRODUCT.md) | Handles OR logic and conditions combined with arithmetic. |
| [DSUM](../Database/DSUM.md) | Totals records that match criteria stored in a block of cells. |

## Official Documentation

- [Microsoft Support: SUMIF function](https://support.microsoft.com/en-us/excel/functions/sumif-function)
- [Google Docs Editors Help: SUMIF](https://support.google.com/docs/answer/3093583)
