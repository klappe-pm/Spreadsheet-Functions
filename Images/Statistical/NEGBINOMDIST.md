---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - NEGBINOMDIST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# NEGBINOMDIST Image Guide

Images planned for [NEGBINOMDIST](../../Functions/Statistical/NEGBINOMDIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Failures, Successes and Probability Inputs

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated worksheet screenshot. |
| Content | Three labeled input cells: failures in `B2` (6), successes in `B3` (4) and probability in `B4` (0.3). A formula bar shows `=NEGBINOMDIST(B2, B3, B4)` with arrows linking each cell to its argument name. A small note reads: Excel uses three arguments. |
| Alt Text | A worksheet with three input cells labeled failures, successes and probability, linked by arrows to the arguments of a NEGBINOMDIST formula. |
| File Name | NEGBINOMDIST Inputs.png |

## Image 2: Summing Exact Probabilities

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 5 and before Story Problems. |
| Format | Vertical stack of three result cells added together. |
| Content | Three rows labeled 0, 1 and 2 failures, each showing its NEGBINOMDIST value (0.0081, 0.02268 and 0.03969), with a plus sign between rows and a total of 0.07047 below a line. |
| Alt Text | Three exact probabilities for zero, one and two failures stacked and added to a total of 0.07047. |
| File Name | NEGBINOMDIST Summed Probabilities.png |
