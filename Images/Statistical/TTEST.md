---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - TTEST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistics
---

# TTEST Image Guide

Images planned for [TTEST](../../Functions/Statistical/TTEST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Two Samples and the Test Settings

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | Sample A in `A2:A9` and sample B in `B2:B9` side by side with headers. Each argument of the formula `=TTEST(A2:A9,B2:B9,2,2)` is labeled beneath the formula: array1, array2, tails set to 2 for two-tailed, and type set to 2 for equal variances. A callout lists the three type values: 1 paired, 2 equal variances, 3 unequal variances. |
| Alt Text | A worksheet with two sample columns and a TTEST formula whose four arguments are labeled. |
| File Name | TTEST Samples And Arguments.png |

## Image 2: Two-Sample and Paired Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Two side by side panels, each a screenshot of a worksheet. |
| Content | Left panel: the warehouse pick times in `A1:C8` with the p-value 0.0010 in a labeled output cell and the caption two independent samples. Right panel: the quiz scores in `A1:C7` with the p-value 0.0003 in a labeled output cell and the caption matched pairs. Each panel marks the threshold 0.05 on a small bar. |
| Alt Text | Two worksheet panels showing an independent two-sample TTEST result of 0.0010 and a paired TTEST result of 0.0003, both below the 0.05 threshold. |
| File Name | TTEST Two Sample And Paired Results.png |
