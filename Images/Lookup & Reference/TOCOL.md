---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
related:
  - TOCOL
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - lookup-reference
---

# TOCOL Image Guide

Images planned for [TOCOL](../../Functions/Lookup%20%26%20Reference/TOCOL.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: TOCOL Reading Order

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two small grids side by side with numbered arrows. |
| Content | Left: a 3 by 3 grid numbered in row order, with arrows running across each row, labeled scan_by_column FALSE (default). Right: the same grid with arrows running down each column, labeled scan_by_column TRUE. Both feed into a single column on the right of each grid. |
| Alt Text | Two 3 by 3 grids showing values read across rows in one case and down columns in the other, each flowing into a single column. |
| File Name | TOCOL Reading Order.png |

## Image 2: Ignore Options

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Screenshot of the sample block with three output columns beside it. |
| Content | The block in `A2:C4` with the blank cell in row 3, column B highlighted. Three output columns: the result of `=TOCOL(A2:C4)` showing a 0 where the blank was, the result of `=TOCOL(A2:C4, 1)` with that value removed, and the result of `=TOCOL(A2:C4, 1, TRUE)` in column order. |
| Alt Text | A 3 by 3 block with one blank cell and three resulting columns, one that shows a zero, one that omits the blank, and one read in column order. |
| File Name | TOCOL Ignore Options.png |
