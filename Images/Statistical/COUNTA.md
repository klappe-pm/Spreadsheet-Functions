---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
related:
  - COUNTA
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# COUNTA Image Guide

Images planned for [COUNTA](../../Functions/Statistical/COUNTA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Filled, Empty and Formula Cells

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of one worksheet column. |
| Content | Five cells in column A: a name, a number, a cell that is truly empty, a cell that holds a formula returning an empty string, and a date. The filled cells are outlined in green and labeled counted. The truly empty cell is outlined in gray and labeled skipped. A result cell shows the COUNTA result. |
| Alt Text | A worksheet column with filled cells outlined as counted and one truly empty cell outlined as skipped, showing the COUNTA result. |
| File Name | COUNTA Filled Empty and Formula Cells.png |

## Image 2: Empty String Results Counted

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a worksheet with a formula bar visible. |
| Content | Cell `A2` selected, with the formula bar showing `=IF(FALSE, "Yes", "")` and the cell displaying nothing. A callout reads "Looks blank, still counted." The result cell below the range shows 2. |
| Alt Text | A worksheet cell that looks blank because its formula returns an empty string, with a callout noting that COUNTA still counts it. |
| File Name | COUNTA Empty String Results.png |
