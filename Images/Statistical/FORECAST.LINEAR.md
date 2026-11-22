---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
related:
  - FORECAST.LINEAR
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - forecasting
  - images
  - linear-regression
---

# FORECAST.LINEAR Image Guide

Images planned for [FORECAST.LINEAR](../../Functions/Statistical/FORECAST.LINEAR.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Known Values Layout

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | Spend values in `A2:A6` labeled known_x's and sales values in `B2:B6` labeled known_y's, with the x value 90 in a separate cell labeled x. Arrows show each argument mapping to its range. |
| Alt Text | A worksheet with the x value and known x and y ranges of a FORECAST.LINEAR formula labeled. |
| File Name | FORECAST LINEAR Known Values Layout.png |

## Image 2: Scatter Plot With Fitted Line

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 1. |
| Format | Scatter chart with a straight trendline. |
| Content | The five spend and sales points plotted, a straight linear trendline through them, and a highlighted point at spend 90 on the line labeled 397. |
| Alt Text | A scatter chart of five spend and sales points with a fitted straight line and a highlighted forecast point at spend 90. |
| File Name | FORECAST LINEAR Scatter Fit.png |

## Image 3: Story Problem Results Panel

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the spend and sales table with the formula result highlighted. |
| Content | The five rows of Problem 1, the formula `=FORECAST.LINEAR(90, B2:B6, A2:A6)` in the formula bar, and the result cell showing 397. |
| Alt Text | A spend and sales table with the FORECAST.LINEAR result of 397 highlighted. |
| File Name | FORECAST LINEAR Sales Result.png |
