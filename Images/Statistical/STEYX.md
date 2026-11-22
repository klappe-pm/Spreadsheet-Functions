---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
related:
  - STEYX
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# STEYX Image Guide

Images planned for [STEYX](../../Functions/Statistical/STEYX.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Known Y and Known X Ranges

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a two-column worksheet. |
| Content | Column A labeled known x's with spend values and column B labeled known y's with sales values. Both ranges are outlined in different colors, and an arrow shows that each row is one pair. |
| Alt Text | A two-column worksheet with known x and known y ranges outlined and labeled for a STEYX formula. |
| File Name | STEYX Known Ranges.png |

## Image 2: Regression Line and Error Band

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 2 result. |
| Format | Scatter chart with a fitted straight line. |
| Content | Six points from the ad spend data plotted as spend on the horizontal axis and sales on the vertical axis. A straight trend line runs through them, with a shaded band one standard error above and below the line. A marker at spend 9 shows the predicted sales of about 29.79. |
| Alt Text | A scatter chart with a fitted line and a shaded band showing the standard error around the prediction. |
| File Name | STEYX Regression Band.png |

## Image 3: Delivery Data Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the delivery table with the formula bar visible. |
| Content | The table `A1:B6` with distance and minutes columns, the formula `=STEYX(B2:B6, A2:A6)` in the formula bar, and the result 1.536523 in a labeled output cell. |
| Alt Text | A delivery table with distance and minutes columns and a STEYX result of 1.536523. |
| File Name | STEYX Delivery Result.png |
