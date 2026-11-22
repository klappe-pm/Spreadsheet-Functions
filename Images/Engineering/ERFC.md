---
domain: Spreadsheet Functions
category: Engineering
subcategory: Error Functions
related:
  - ERFC
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - engineering
  - images
---

# ERFC Image Guide

Images planned for [ERFC](../../Functions/Engineering/ERFC.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=ERFC(A2)` in the formula bar with the argument `A2` outlined and labeled x, lower bound. A callout beside the cell shows the numeric input. |
| Alt Text | A formula bar showing ERFC with one numeric argument labeled as the lower bound. |
| File Name | ERFC Syntax Anatomy.png |

## Image 2: Tail Probability Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4 and before the Story Problems heading. |
| Format | Screenshot of a worksheet with a z-score column and a probability column. |
| Content | Column A lists z-scores 1.0, 1.5, 2.0 and 2.5. Column B shows the formula `=0.5*ERFC(A2/SQRT(2))` filled down, with results 0.15866, 0.06681, 0.02275 and 0.00621. |
| Alt Text | A worksheet that converts four z-scores to upper-tail probabilities with ERFC. |
| File Name | ERFC Tail Probability Worksheet.png |
