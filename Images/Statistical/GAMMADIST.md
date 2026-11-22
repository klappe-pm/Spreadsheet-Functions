---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - GAMMADIST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# GAMMADIST Image Guide

Images planned for [GAMMADIST](../../Functions/Statistical/GAMMADIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of the formula. |
| Content | The formula `=GAMMADIST(x, alpha, beta, cumulative)` with four callouts: x is the value being tested, alpha is the shape, beta is the scale (1 gives the standard gamma), and cumulative chooses probability (TRUE) or density (FALSE). |
| Alt Text | A labeled GAMMADIST formula showing the x, alpha, beta and cumulative arguments. |
| File Name | GAMMADIST Syntax Anatomy.png |

## Image 2: Density and Cumulative Curves

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Line chart with two panels side by side. |
| Content | Left panel: the gamma density curve for shape 2 and scale 3, with the point at x = 4 marked at height 0.117. Right panel: the cumulative curve for the same parameters, with the point at x = 4 marked at 0.385. Caption: the density is a height, the cumulative value is a probability. |
| Alt Text | Two gamma curves, one for the density and one for the cumulative distribution, with x equal to 4 marked on each. |
| File Name | GAMMADIST Density and Cumulative Curves.png |
