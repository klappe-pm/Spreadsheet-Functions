---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - FTEST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - compatibility
  - hypothesis-testing
  - images
---

# FTEST Image Guide

Images planned for [FTEST](../../Functions/Statistical/FTEST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Two Samples Layout

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | Sample A in `A2:A6` and sample B in `B2:B6` outlined in two colors and labeled array1 and array2, with the formula bar showing `=FTEST(A2:A6, B2:B6)`. |
| Alt Text | A worksheet with two sample columns and a FTEST formula that references them, each column labeled. |
| File Name | FTEST Two Samples Layout.png |

## Image 2: Spread Comparison Chart

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Box plot of two samples side by side. |
| Content | Sample A tight around 11 and sample B wide around 23, with the variances 2.5 and 22 labeled under each box. Caption reads Sample Spread Comparison. |
| Alt Text | Two box plots side by side, the second much wider than the first, with their variances labeled. |
| File Name | FTEST Spread Comparison.png |

## Image 3: Decision Result Panel

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the bottle fill table with the result cell highlighted. |
| Content | The two machine columns from Problem 1 with the blank row for Machine A visible, the formula `=FTEST(A2:A8, B2:B8)` in the formula bar, and the result cell showing 0.0148 with a note that it is below 0.05. |
| Alt Text | A bottle fill table with the FTEST result of 0.0148 highlighted and a note that it is below 0.05. |
| File Name | FTEST Bottle Fill Result.png |
