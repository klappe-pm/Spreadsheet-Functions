---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Array Tools
purpose:
  - Array Shaping
use-case:
  - Line Item Totals
  - Name Length Checks
  - Pass Fail Flags
related:
  - ARRAY_CONSTRAIN
  - BYROW
  - FLATTEN
  - IF
  - LET
  - MAP
level: 3
source:
  - https://support.google.com/docs/answer/3093275
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Array Formula
  - Bulk Formula
tags:
  - array-formulas
  - arrays
  - automation
  - sheets
---

# ARRAYFORMULA

## Description

**ARRAYFORMULA** lets one formula work on a whole range instead of a single cell. The formula returns an array, and Google Sheets places each value in the cells below (and to the right, for a horizontal result) without you copying the formula down. One formula in one cell can therefore produce a column of totals, labels or checks, and it stays in one place when rows are added.

The official help page makes two points that shape how you use the function. First, many array formulas expand into neighboring cells automatically, so the explicit wrapper is often unnecessary. Second, pressing Ctrl+Shift+Enter while you edit a formula adds `ARRAYFORMULA(` to the start of it. Use the wrapper when a formula that works on one cell needs to work on a range, such as an IF test or an arithmetic expression over two columns.

The result must have room to expand. If cells below the formula already hold data, the output cannot be placed, and the formula shows `#REF!`. Array formulas also cannot be exported, according to the official page. ARRAYFORMULA is available only in Google Sheets. In Excel 365, most formulas that reference a range return an array on their own, so the wrapper is not needed.

<!-- Image 1: ARRAYFORMULA Spill Into Empty Cells. See Images/Google-specific/ARRAYFORMULA.md -->

## Syntax

```excel
=ARRAYFORMULA(array_formula)
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `array_formula` | Yes | A range, a mathematical expression that uses one or more ranges of the same size, or a function that returns more than one cell. The expression must include a range to produce several results. |

### Return Value

An array: the results of `array_formula` placed in the cells below and to the right of the formula. A formula that refers only to single cells returns one value, because there is no range to expand across.

## Examples

### Example 1: Multiplying Two Columns

```excel
=ARRAYFORMULA(B2:B4 * C2:C4)
```

**Result:** `15`, `12` and `20` in three cells, when B2:B4 holds `5`, `8` and `2` and C2:C4 holds `3`, `1.5` and `10`.

Each result is the quantity in column B multiplied by the price in column C on the same row.

### Example 2: Keeping Blank Rows Empty

```excel
=ARRAYFORMULA(IF(A2:A4="", "", B2:B4 * C2:C4))
```

**Result:** The same products as Example 1 for rows that have a name in column A, and empty cells for any row without a name.

The IF test stops the output from showing zeros in rows that have no data yet.

### Example 3: Measuring Text Length

```excel
=ARRAYFORMULA(LEN(A2:A4))
```

**Result:** `3`, `8` and `6` when A2:A4 holds `Pen`, `Notebook` and `Eraser`.

LEN works on each cell in the range, so the whole column of character counts appears from one formula.

### Example 4: Summing Only Values Above a Threshold

```excel
=ARRAYFORMULA(SUM(IF(D2:D7>100, D2:D7, 0)))
```

**Result:** `375` when D2:D7 holds `90`, `120`, `150`, `80`, `105` and `60`.

Only the values above 100 are kept (120, 150 and 105), and their total is 375.

### Example 5: Labeling Each Row

```excel
=ARRAYFORMULA(IF(B2:B6>=80, "Pass", "Review"))
```

**Result:** A label for each score in B2:B6. A score of 80 or more shows Pass, and any lower score shows Review.

The same IF test applies to every row, so changing the threshold in one formula updates the whole column.

## Story Problems

### Problem 1: Line Totals for a Parts Order

A repair shop lists four parts. The quantity is in column B and the unit price is in column C.

| Part | Quantity | Unit Price |
| --- | --- | --- |
| Washer | 4 | 2.50 |
| Bracket | 10 | 1.20 |
| Pump seal | 3 | 8.00 |
| Gasket | 6 | 0.75 |

**Task:** Put the line total for every part in column D with one formula, then find the order total.

**Solution:**

```excel
=ARRAYFORMULA(B2:B5 * C2:C5)
```

Place this in `D2`. Add the total with `=SUM(D2:D5)` in a separate cell.

**Answer:** `50.5`, because the line totals are 10, 12, 24 and 4.5, and 10 + 12 + 24 + 4.5 = 50.5.

<!-- Image 2: ARRAYFORMULA Parts Order Column. See Images/Google-specific/ARRAYFORMULA.md -->

### Problem 2: Pass or Review Flags for Test Scores

A tutor scored five quizzes and wants a flag beside each score in column C.

| Student | Score |
| --- | --- |
| Ada | 88 |
| Ben | 72 |
| Chloe | 95 |
| Dev | 61 |
| Ezra | 79 |

**Task:** Fill column C with one formula that shows Pass for scores of 80 or more and Review for anything lower.

**Solution:**

```excel
=ARRAYFORMULA(IF(B2:B6>=80, "Pass", "Review"))
```

Place this in `C2`.

**Answer:** Two Pass flags (Ada and Chloe) and three Review flags (Ben, Dev and Ezra).

## Use Cases

### Line Item Totals

**Scenario:** An invoice lists quantity and unit price for each product line, and new lines are added at the bottom.

```excel
=ARRAYFORMULA(IF(A2:A="", "", B2:B*C2:C))
```

**Why It Works:** The IF test keeps empty rows blank, and the multiplication fills every filled line automatically. Adding a product in row 20 needs no formula change.

### Name Length Checks

**Scenario:** A data entry team must keep product codes within a maximum length before an import.

```excel
=ARRAYFORMULA(IF(LEN(A2:A)>12, "Too long", "OK"))
```

**Why It Works:** LEN measures every code in the column at once. Flagged rows stand out for correction before the import runs.

### Pass Fail Flags

**Scenario:** A training coordinator marks each learner as Pass or Review based on a score.

```excel
=ARRAYFORMULA(IF(B2:B6>=80, "Pass", "Review"))
```

**Why It Works:** Each row gets a flag from the same rule. Because the threshold is written once, the coordinator can change it in one place.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `#REF!` | The output would overwrite cells that already hold data, so it cannot expand. | Clear the cells below and to the right of the formula, or move the formula. |
| `#REF!` | Ranges have mismatched sizes, such as 100 rows multiplied by 50 rows. | Use ranges with the same number of rows (or columns for a horizontal result). |
| Single value only | The expression refers to single cells, not ranges. | Change single references such as A2 to ranges such as A2:A. |
| Zeros in empty rows | Arithmetic on blank cells returns 0. | Wrap the expression in IF to return a blank for empty rows. |
| `#REF!` or circular reference | The output range overlaps the input range it reads from. | Place the formula in a column or sheet that is not one of its inputs. |
| Slow sheet | A very large open-ended range, such as A:A, is recalculated with complex formulas. | Use a bounded range such as A2:A1000 that covers the real data. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available as a function. Excel 365 spills dynamic array results without a wrapper. | Legacy Excel needed Ctrl+Shift+Enter and a pre-selected output range for array formulas. |
| Google Sheets | Available | Many array formulas expand automatically; the explicit wrapper is needed when a formula must work on a range. |

## Tips and Best Practices

- Test with a bounded range such as A2:A10 before you expand the formula to a full column.
- Wrap arithmetic in IF to keep blank rows clean, so totals and counts do not pick up zeros.
- Place the formula in an empty column with room to expand, and leave the rows below it clear.
- Use LET or MAP when a formula grows long, so each part is named and easier to read.
- Keep ranges the same size inside one expression, so the result does not fail with a size mismatch.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ARRAY_CONSTRAIN](ARRAY_CONSTRAIN.md) | Trims an array result to a set number of rows and columns. |
| [BYROW](../Logical/BYROW.md) | Applies a function to each row of a range, for row level results that need a custom rule. |
| [FLATTEN](FLATTEN.md) | Combines several ranges into one column, which can then be processed in one step. |
| [IF](../Logical/IF.md) | Supplies the test that most ARRAYFORMULA expressions use to control the output. |
| [LET](../Logical/LET.md) | Names parts of a long formula so each step is readable. |
| [MAP](../Logical/MAP.md) | Applies a LAMBDA to each value in an array, for transformations that need custom logic. |

## Official Documentation

- [Google Docs Editors Help: ARRAYFORMULA](https://support.google.com/docs/answer/3093275)
