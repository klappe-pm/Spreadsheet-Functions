---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Array Tools
purpose:
  - Array Shaping
use-case:
  - Combining Regional Lists
  - Single Column Export
  - Totals Across Blocks
related:
  - ARRAY_CONSTRAIN
  - ARRAYFORMULA
  - FILTER
  - TOCOL
  - TRANSPOSE
level: 3
source:
  - https://support.google.com/docs/answer/10307761
date-created: 2025-08-17
date-revised: 2026-11-22
aliases:
  - Flatten Ranges
tags:
  - array-shaping
  - arrays
  - sheets
---

# FLATTEN

## Description

**FLATTEN** takes the values from one or more ranges and returns them as a single column. The values from the first range come first, then the values from the second range, and so on, in the order the arguments are listed. Inside each range, values are read row by row, left to right, so the whole first row of a range is added before the second row begins.

Use FLATTEN when data is laid out in a grid but a later step needs a single list, such as a lookup column, a set of values to sum, or a list to filter. A single formula can gather several separate ranges into one column, and the result updates when any source cell changes.

FLATTEN does not skip empty cells. Blank values appear in the output as blank rows. To remove them, wrap the result in FILTER with a test that excludes empty values. Arguments do not have to be ranges: text and numbers typed into the formula are added in order, too. FLATTEN is available only in Google Sheets.

<!-- Image 1: FLATTEN Reading Order. See Images/Google-specific/FLATTEN.md -->

## Syntax

```excel
=FLATTEN(range1, [range2, ...])
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `range1` | Yes | The first range or value to flatten. Its values are read row by row. |
| `range2`, and more | No | Additional ranges or values to add after `range1`, in argument order. You can repeat this argument as often as needed. |

### Return Value

A single column of values. The column contains every value from every input in order, including blank values from empty cells.

## Examples

### Example 1: Flattening a Two by Two Block

```excel
=FLATTEN(A1:B2)
```

**Result:** A column of four values, `1`, `2`, `3`, `4`, when A1 holds 1, B1 holds 2, A2 holds 3 and B2 holds 4.

The first row is read first (1 then 2), and the second row follows (3 then 4).

### Example 2: Mixing Ranges and Typed Text

```excel
=FLATTEN(A1:B2, "Total", B3:B4)
```

**Result:** Seven values in order: `1`, `2`, `3`, `4`, `Total`, `5`, `6`, when B3 holds 5 and B4 holds 6.

The text is placed between the two ranges because it is listed between them in the formula.

### Example 3: Summing a Grid as One List

```excel
=SUM(FLATTEN(B2:C4))
```

**Result:** `25` for the grid used in Story Problem 2, where the blank cells add nothing to the total.

SUM adds the numbers in the flattened column, so one formula replaces a separate sum for each row.

### Example 4: Filtering the Flattened Values

```excel
=FILTER(FLATTEN(A1:B2), FLATTEN(A1:B2) > 2)
```

**Result:** `3` and `4` when A1:B2 holds the values 1, 2, 3 and 4.

FLATTEN produces the list and FILTER keeps only the values above 2.

## Story Problems

### Problem 1: Ticket Numbers From Two Teams

The East team recorded tickets in `E2:E4` and the West team in `F2:F3`.

| East | West |
| --- | --- |
| 101 | 201 |
| 102 | 202 |
| 103 | |

**Task:** Find the total of all five ticket numbers with one formula.

**Solution:**

```excel
=SUM(FLATTEN(E2:E4, F2:F3))
```

**Answer:** `709`, because 101 + 102 + 103 + 201 + 202 = 709.

### Problem 2: Removing Blank Cells From a Survey Grid

A survey grid in `B2:C4` has some empty cells. Each row is a respondent, and the columns hold scores for Question 1 and Question 2. The analyst wants a clean list of the answers that were entered.

| Respondent | Question 1 | Question 2 |
| --- | --- | --- |
| 1 | 5 | |
| 2 | 7 | 9 |
| 3 | | 4 |

**Task:** Produce a single column of the entered scores with no blank rows.

**Solution:**

```excel
=FILTER(FLATTEN(B2:C4), FLATTEN(B2:C4) <> "")
```

**Answer:** A column of four scores, `5`, `7`, `9` and `4`, in the order they appear in the grid. Their total is 25.

<!-- Image 2: FLATTEN Survey Grid Filter. See Images/Google-specific/FLATTEN.md -->

## Use Cases

### Combining Regional Lists

**Scenario:** A regional manager receives sales leads in separate blocks from each branch and needs one list for the call sheet.

```excel
=FLATTEN(Branch1!A2:C20, Branch2!A2:C20, Branch3!A2:C20)
```

**Why It Works:** The three blocks are read in order, so the call sheet begins with every lead from the first branch and then continues. Wrap the result in FILTER if blank rows appear between branches.

### Single Column Export

**Scenario:** A developer needs one column of product codes from a grid of codes laid out across several sections of a catalog.

```excel
=FLATTEN(A2:D10)
```

**Why It Works:** The formula converts a grid into one column that can be pasted into an import template or used as the lookup list for other formulas.

### Totals Across Blocks

**Scenario:** An analyst keeps monthly sales in separate blocks, one for each quarter, and needs a single annual total.

```excel
=SUM(FLATTEN(B2:D4, F2:H4))
```

**Why It Works:** SUM adds every number in the flattened list, so the two quarterly blocks are combined without a separate total for each block.

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| Blank rows in the output | FLATTEN keeps empty cells as blank values. | Wrap the result in FILTER with a test that excludes empty values. |
| Unexpected total | A text number in the source range is not added as a number. | Convert the text with VALUE or re-enter the number. |
| `#REF!` | The output would overwrite cells that already hold data. | Clear the cells below the formula, or place the formula in an empty area. |
| Wrong order | A range was given in the wrong argument order. | List the ranges in the order you want them to appear in the column. |

## Platform Differences

| Platform | Availability | Notes |
| --- | --- | --- |
| Microsoft Excel | Not available. The closest alternative is TOCOL in Microsoft 365, which turns an array into one column. | TOCOL can skip blank values with an optional argument, while FLATTEN keeps them. |
| Google Sheets | Available | Returns one column in argument order and row by row within each range. Keeps blank values. |

## Tips and Best Practices

- Wrap FLATTEN in FILTER with `<> ""` whenever the output feeds a count, a lookup or an import.
- List the ranges in the order you want the output to appear.
- Use SUM or COUNTA around FLATTEN to aggregate across blocks in one step.
- Check the output size before placing the formula, because the column spills into the cells below.

## Related Functions

| Function | Relationship |
| --- | --- |
| [ARRAYFORMULA](ARRAYFORMULA.md) | Applies a formula across a range; FLATTEN reshapes the data and ARRAYFORMULA processes it. |
| [ARRAY_CONSTRAIN](ARRAY_CONSTRAIN.md) | Trims an array to a set number of rows and columns. |
| [FILTER](../Lookup%20%26%20Reference/FILTER.md) | Removes blank or unwanted values from the flattened column. |
| [TOCOL](../Lookup%20%26%20Reference/TOCOL.md) | The closest Excel function for turning an array into one column. |
| [TRANSPOSE](../Lookup%20%26%20Reference/TRANSPOSE.md) | Swaps rows and columns, which changes the reading order before flattening. |

## Official Documentation

- [Google Docs Editors Help: FLATTEN](https://support.google.com/docs/answer/10307761)
