---
domain: Spreadsheet Functions
category: Statistical
subcategory: Correlation Transforms
related:
  - FISHER
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# FISHER Image Guide

Images planned for [FISHER](../../Functions/Statistical/FISHER.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Correlation Scale Compared With the Fisher Scale

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two number lines drawn one above the other. |
| Content | The top line runs from -1 to 1 and is labeled correlation. The bottom line is unbounded and is labeled Fisher scale. Arrows connect 0.6, 0.9 and -0.5 on the top line to 0.6931, 1.4722 and -0.5493 on the bottom line. The caption notes that values near 1 spread out on the Fisher scale. |
| Alt Text | Two number lines showing correlations between -1 and 1 mapped to wider Fisher values, with three example points marked. |
| File Name | FISHER Correlation and Fisher Scales.png |

## Image 2: Transformed Values in a Helper Column

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a worksheet with a helper column. |
| Content | Columns A to C holding a study label, a correlation and a Fisher value. Column C is outlined and labeled helper column, with the formula `=FISHER(B2)` shown in the formula bar and the results 0.4477, 0.6184 and 0.7089 in the rows below. |
| Alt Text | A worksheet with a helper column that holds the Fisher transformation of each correlation in the column beside it. |
| File Name | FISHER Helper Column.png |
