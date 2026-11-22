---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
related:
  - GROWTH
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# GROWTH Image Guide

Images planned for [GROWTH](../../Functions/Statistical/GROWTH.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of the formula. |
| Content | The formula `=GROWTH(known_y's, [known_x's], [new_x's], [const])` with callouts: known y values must be greater than 0, the x arguments are optional, and const defaults to TRUE. |
| Alt Text | A labeled GROWTH formula showing the known y, known x, new x and const arguments. |
| File Name | GROWTH Syntax Anatomy.png |

## Image 2: Exponential Fit Versus Straight Line

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Scatter chart with two fitted lines. |
| Content | Points for x = 1 to 5 with values 6, 12, 24, 48 and 96. A curved exponential fit passes through the points, extended to x = 6 at 192. A straight dashed line from the TREND function is shown for comparison and falls well below 192 at x = 6. |
| Alt Text | A scatter chart of exponentially growing points with a curved exponential fit and a straight line, showing the exponential fit predicting 192 at x equal to 6. |
| File Name | GROWTH Exponential Fit Versus Straight Line.png |
