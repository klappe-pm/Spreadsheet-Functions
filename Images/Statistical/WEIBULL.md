---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - WEIBULL
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistics
---

# WEIBULL Image Guide

Images planned for [WEIBULL](../../Functions/Statistical/WEIBULL.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: The Weibull Parameters on a Curve

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two labeled line charts stacked vertically. |
| Content | Top chart: the cumulative Weibull curve for x from 0 to 6 with alpha 1.5 and beta 3, with the point at x = 2 marked at 0.4198. Bottom chart: the density curve for the same parameters, with the point at x = 2 marked at 0.2369. Each chart is captioned with cumulative set to TRUE or FALSE. |
| Alt Text | Two line charts of a Weibull distribution, one showing the cumulative curve and one showing the density curve, with the point at x equal to 2 marked on each. |
| File Name | WEIBULL Parameters Curves.png |

## Image 2: Failure Window on the Cumulative Curve

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a shaded cumulative chart beside it. |
| Content | The parameter table with the formula `=WEIBULL(900,1.8,1200,TRUE)-WEIBULL(600,1.8,1200,TRUE)` in a labeled output cell showing 0.1993. The chart beside it shows the cumulative curve with the area between 600 and 900 hours shaded and labeled 0.1993. |
| Alt Text | A worksheet with a Weibull formula returning 0.1993 beside a cumulative chart with the region between 600 and 900 hours shaded. |
| File Name | WEIBULL Failure Window.png |
