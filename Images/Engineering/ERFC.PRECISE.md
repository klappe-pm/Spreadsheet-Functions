---
domain: Spreadsheet Functions
category: Engineering
subcategory: Error Functions
related:
  - ERFC.PRECISE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - engineering
  - images
---

# ERFC.PRECISE Image Guide

Images planned for [ERFC.PRECISE](../../Functions/Engineering/ERFC.PRECISE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=ERFC.PRECISE(A2)` in the formula bar with the argument `A2` outlined and labeled x, lower bound. A small note marks Excel as the platform. |
| Alt Text | A formula bar showing ERFC.PRECISE with one numeric argument labeled as the lower bound. |
| File Name | ERFC.PRECISE Syntax Anatomy.png |

## Image 2: Battery Retest Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4 and before the Story Problems heading. |
| Format | Screenshot of an Excel worksheet with a cell list and a probability column. |
| Content | Cells B2 and B3 hold the z-scores 0.5 and 2.0. Column C shows the formula `=0.5*ERFC.PRECISE(B2/SQRT(2))` and its result for each row, with row 3 highlighted to show the retest threshold. |
| Alt Text | An Excel worksheet that calculates the share of cells above a z-score threshold with ERFC.PRECISE. |
| File Name | ERFC.PRECISE Battery Retest Worksheet.png |
