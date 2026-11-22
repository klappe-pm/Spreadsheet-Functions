---
domain: Spreadsheet Functions
category: Statistical
subcategory: Regression and Forecasting
related:
  - TREND
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - statistics
---

# TREND Image Guide

Images planned for [TREND](../../Functions/Statistical/TREND.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Known Data and New Points on a Trend Line

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated scatter chart with a straight trend line. |
| Content | Six monthly sales points from `A2:B7` as dots, the fitted straight line running through them, and the predicted points at months 7 and 8 drawn as hollow markers on the extended line. Labels show `known_y's` on the vertical axis and `known_x's` on the horizontal axis, with `new_x's` pointing to the hollow markers. |
| Alt Text | A scatter chart of monthly sales with a fitted straight trend line and two hollow predicted points beyond the last month. |
| File Name | TREND Known Data And New Points.png |

## Image 2: Forced Zero Intercept Comparison

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 3. |
| Format | Side by side scatter charts with the same six points. |
| Content | Left: the standard trend line with its intercept near 108.7 marked on the vertical axis. Right: the line forced through the origin with `const` set to FALSE, drawn from the axis origin. Each chart is captioned with its formula. |
| Alt Text | Two scatter charts comparing a trend line with an intercept against a line forced through the origin. |
| File Name | TREND Zero Intercept Comparison.png |

## Image 3: Dynamic Array Output in Microsoft 365

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of a worksheet. |
| Content | The cold drink table in `A1:B6` with the formula `=TREND(B2:B6,A2:A6,33)` in a separate cell, and the result 76.3 highlighted in the output cell with a label that reads one formula, one result. |
| Alt Text | A worksheet showing a TREND formula that returns a forecast of 76.3 for a temperature of 33 degrees. |
| File Name | TREND Cold Drink Forecast.png |
