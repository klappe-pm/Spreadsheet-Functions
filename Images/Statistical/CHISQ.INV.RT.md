---
domain: Spreadsheet Functions
category: Statistical
subcategory: Hypothesis Tests
related:
  - CHISQ.INV.RT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# CHISQ.INV.RT Image Guide

Images planned for [CHISQ.INV.RT](../../Functions/Statistical/CHISQ.INV.RT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Right Tail Critical Value

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Diagram of a chi-squared curve with the right tail shaded. |
| Content | A right-skewed curve with the area to the right of a cutoff shaded and labeled with the probability argument. The cutoff on the horizontal axis is labeled with the function result. A caption reads "CHISQ.INV.RT returns the cutoff for the shaded area." Use a single accent color for the shaded area. |
| Alt Text | A chi-squared curve with the right tail shaded, showing that CHISQ.INV.RT returns the cutoff for a given right-tail probability. |
| File Name | CHISQ.INV.RT Right Tail Critical Value.png |

## Image 2: Statistic Against the Cutoff

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a small worksheet with the decision formula. |
| Content | Cells `B2` (test statistic 12.4) and `B3` (degrees of freedom 5) with the formula `=IF(B2>CHISQ.INV.RT(0.05, B3), "Reject", "Keep")` in the adjacent cell. The output cell shows Reject. A note beside the cutoff reads 11.070498. |
| Alt Text | A worksheet comparing a test statistic of 12.4 with a chi-squared cutoff of 11.070498 and returning Reject. |
| File Name | CHISQ.INV.RT Statistic Against Cutoff.png |
