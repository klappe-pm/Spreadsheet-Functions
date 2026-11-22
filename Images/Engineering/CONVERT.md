---
domain: Spreadsheet Functions
category: Engineering
subcategory: Comparison and Conversion
related:
  - CONVERT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - conversion
  - images
---

# CONVERT Image Guide

Images planned for [CONVERT](../../Functions/Engineering/CONVERT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Unit Code Pattern

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of one formula. |
| Content | The formula `=CONVERT(1,"lbm","kg")` with three callouts: the number 1 labeled value, `"lbm"` labeled from unit, and `"kg"` labeled to unit. A note beneath says both codes must measure the same quantity. |
| Alt Text | A CONVERT formula with its value, starting unit code and target unit code labeled. |
| File Name | CONVERT Unit Code Pattern.png |

## Image 2: Freight Weight Conversion Table

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the pallet list and the converted column. |
| Content | Column B lists pallet weights in pounds mass (1200, 845.5, 2310). Column C shows the formula `=ROUND(CONVERT(B2,"lbm","kg"),2)` in the formula bar and the results 544.31, 383.51, and 1047.8. |
| Alt Text | A worksheet with pallet weights in pounds and their kilogram values rounded to two decimal places. |
| File Name | CONVERT Freight Weights.png |
