---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - TDIST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# TDIST Image Guide

Images planned for [TDIST](../../Functions/Statistical/TDIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Tails Argument Choices

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two-panel diagram of the t-distribution curve. |
| Content | Left panel: the area beyond x in one tail only, labeled tails 1. Right panel: the areas beyond x and beyond -x shaded together, labeled tails 2 and equal to twice the one-tailed area. |
| Alt Text | Two t-distribution panels showing one shaded tail for tails 1 and two shaded tails for tails 2. |
| File Name | TDIST Tails Choices.png |

## Image 2: Replacement Formulas

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 4 result. |
| Format | Side by side worksheet comparison with matching results. |
| Content | Three rows: `=TDIST(2.2, 14, 2)` with 0.045100 beside `=T.DIST.2T(2.2, 14)` with 0.045100, and `=TDIST(1.8, 20, 1)` with 0.043482 beside `=T.DIST.RT(1.8, 20)` with 0.043482. A caption notes that the results match. |
| Alt Text | A worksheet comparing TDIST formulas with their T.DIST.2T and T.DIST.RT replacements, showing matching results. |
| File Name | TDIST Replacement Formulas.png |
