---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
related:
  - WRAPCOLS
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - lookup
---

# WRAPCOLS Image Guide

Images planned for [WRAPCOLS](../../Functions/Lookup%20%26%20Reference/WRAPCOLS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: WRAPCOLS Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=WRAPCOLS(vector, wrap_count, [pad_with])` with each argument underlined. Beside it, a single column of six values is shown being cut into two stacks of three. |
| Alt Text | A WRAPCOLS formula with its arguments labeled and a column of values shown wrapped into columns. |
| File Name | WRAPCOLS Syntax Anatomy.png |

## Image 2: Source List Versus Wrapped Columns

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 5. |
| Format | Two worksheet panels side by side. |
| Content | Left: the list of six values in `A2:A7`. Right: the result of `WRAPCOLS(A2:A7, 2)` as a two-row, three-column grid, with the first column highlighted and labeled 12 and 7. |
| Alt Text | A list of six values on the left and the same values wrapped into three columns of two on the right. |
| File Name | WRAPCOLS Source Versus Wrapped.png |

## Image 3: Block Totals From Wrapped Columns

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Worksheet screenshot with the wrapped result shown in a grid. |
| Content | The eight session counts in `B2:B9`. A two-column grid to the right shows the first block of four and the second block of four, with the second column highlighted and the total 51 in a labeled result cell. |
| Alt Text | Eight session attendance counts wrapped into two columns, with the second column highlighted and totaling 51. |
| File Name | WRAPCOLS Block Totals.png |
