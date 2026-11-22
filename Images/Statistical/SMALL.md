---
domain: Spreadsheet Functions
category: Statistical
subcategory: Ranking and Percentiles
related:
  - SMALL
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - ranking
---

# SMALL Image Guide

Images planned for [SMALL](../../Functions/Statistical/SMALL.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Array and K Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=SMALL(array, k)` with `array` outlined as a range of numbers and `k` shown as a single position number pointing to the third slot of a small ranked strip of values. |
| Alt Text | A SMALL formula with the array argument outlined as a range and the k argument marked as a rank position. |
| File Name | SMALL Array K Arguments.png |

## Image 2: Sorted Positions for Tied Values

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two-column diagram: original order on the left, sorted order on the right. |
| Content | Left column: 7, 3, 9, 1, 5, 3 in their original order. Right column: 1, 3, 3, 5, 7, 9 in sorted order with positions 1 to 6 numbered. Positions 2 and 3 are both shaded to show the tie, and position 3 is labeled as the result of `=SMALL(A2:A7, 3)`. |
| Alt Text | Original and sorted lists of six numbers with the tied value 3 shaded at positions 2 and 3. |
| File Name | SMALL Sorted Positions.png |

## Image 3: Story Problem Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the supplier quote table with the result visible. |
| Content | The quotes in `B2:B6` with the Birch value 388 and the Delta value 390 highlighted, and the cell showing `390` for `=SMALL(B2:B6, 2)` in a labeled output cell. |
| Alt Text | A supplier quote table with the two lowest quotes highlighted and a SMALL result of 390. |
| File Name | SMALL Supplier Quotes Result.png |
