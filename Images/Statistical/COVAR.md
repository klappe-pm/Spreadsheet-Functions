---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - COVAR
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - compatibility
  - images
  - statistical
---

# COVAR Image Guide

Images planned for [COVAR](../../Functions/Statistical/COVAR.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: COVAR Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a formula bar. |
| Content | The formula `=COVAR(array1, array2)` with `array1` and `array2` highlighted in two colors. A caption under each says "same number of data points". |
| Alt Text | A COVAR formula with its two array arguments highlighted and labeled. |
| File Name | COVAR Syntax Anatomy.png |

## Image 2: Positive and Negative Covariance

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Two scatter plots side by side, drawn from the overtime table. |
| Content | Left plot: overtime hours on the horizontal axis and units packed on the vertical axis, with points rising from lower left to upper right, captioned "Example 1: positive covariance, 136". Right plot: overtime hours against defects, with points falling from upper left to lower right, captioned "Example 3: negative covariance, -7.6". |
| Alt Text | Two scatter plots, one with a rising pattern and one with a falling pattern, labeled with their covariance results. |
| File Name | COVAR Positive and Negative.png |

## Image 3: Staffing Covariance Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the staffing table with a worked deviation column. |
| Content | The table in `A1:C6` with two added columns labeled "Staff minus mean" and "Orders minus mean". A product column follows, and its total of 1,640 sits above the formula `=COVAR(B2:B6, C2:C6)` and its result 328. |
| Alt Text | A staffing table with deviation and product columns that sum to 1,640 and a COVAR result of 328. |
| File Name | COVAR Staffing Result.png |
