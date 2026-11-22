---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
related:
  - COVARIANCE.P
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - covariance
  - images
  - statistical
---

# COVARIANCE.P Image Guide

Images planned for [COVARIANCE.P](../../Functions/Statistical/COVARIANCE.P.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: COVARIANCE.P Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a formula bar. |
| Content | The formula `=COVARIANCE.P(array1, array2)` with each array highlighted in a different color. A caption under the formula reads "Whole population: divide by n". |
| Alt Text | A COVARIANCE.P formula with its two array arguments highlighted and labeled. |
| File Name | COVARIANCE.P Syntax Anatomy.png |

## Image 2: Population Versus Sample Divisor

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Two-row comparison diagram. |
| Content | Top row: the five deviation products from Example 1 (20, 6, 0, 6, 20), a sum of 52, and a divisor of 5 labeled "population (n)" with the result 10.4. Bottom row: the same sum of 52 with a divisor of 4 labeled "sample (n minus 1)" and the result 13 for COVARIANCE.S. |
| Alt Text | A comparison of the population divisor of 5 and the sample divisor of 4 applied to the same sum of 52. |
| File Name | COVARIANCE.P Population Versus Sample.png |

## Image 3: Season Covariance Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the season table with a deviation product column. |
| Content | The table in `A1:C6` with a product column added. The products 92, 26, 0, 14 and 108 are shown with their sum of 240. The formula `=COVARIANCE.P(B2:B6, C2:C6)` and its result 48 appear beside the table. |
| Alt Text | A season table with deviation products that sum to 240 and a COVARIANCE.P result of 48. |
| File Name | COVARIANCE.P Season Result.png |
