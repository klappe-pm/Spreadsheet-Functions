---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
related:
  - DEVSQ
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - spread
  - statistical
---

# DEVSQ Image Guide

Images planned for [DEVSQ](../../Functions/Statistical/DEVSQ.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: DEVSQ Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a formula bar. |
| Content | The formula `=DEVSQ(number1, [number2], ...)` with `number1` in one color, the optional `number2, ...` in a second color, and a caption that reads "up to 255 arguments". |
| Alt Text | A DEVSQ formula with its first argument and optional additional arguments labeled. |
| File Name | DEVSQ Syntax Anatomy.png |

## Image 2: Sum of Squares to Variance

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Three-step flow diagram with arrows. |
| Content | Step 1, a box with the five squared distances 0, 9, 9, 4 and 4 summed to 26. Step 2, a box that divides 26 by 4 degrees of freedom. Step 3, a result box showing 6.5 with the label "same as VAR.S". |
| Alt Text | A three-step flow from squared distances to a sum of 26, then division by 4, giving the sample variance of 6.5. |
| File Name | DEVSQ Sum of Squares to Variance.png |

## Image 3: Machine Run Time Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the run time table with a deviation column. |
| Content | The table in `A1:B7` with a squared deviation column showing 64, 16, 9, 144, 100 and 25. The total 358 is highlighted beside the formula `=DEVSQ(B2:B7)`. |
| Alt Text | A machine run time table with squared deviations that total 358. |
| File Name | DEVSQ Machine Run Time Result.png |
