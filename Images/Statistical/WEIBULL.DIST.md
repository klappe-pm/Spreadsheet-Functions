---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
related:
  - WEIBULL.DIST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# WEIBULL.DIST Image Guide

Images planned for [WEIBULL.DIST](../../Functions/Statistical/WEIBULL.DIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Arguments on a Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | Three labeled input cells (age, shape, scale) in column E with the formula `=WEIBULL.DIST(E2, E3, E4, TRUE)` in the formula bar. Each argument in the formula is connected to its cell with a colored outline. |
| Alt Text | A worksheet with the x, alpha, beta and cumulative arguments of WEIBULL.DIST matched to labeled input cells. |
| File Name | WEIBULL DIST Syntax Arguments.png |

## Image 2: Shape Comparison Curves

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Line chart with three curves. |
| Content | Cumulative curves for shape 0.8, shape 1 and shape 2 on the same scale 4 axes, with x from 0 to 10. Each curve is labeled with its shape value. The legend explains that a shape below 1 rises fast early and a shape above 1 rises slowly at first. |
| Alt Text | A line chart comparing Weibull cumulative curves for shapes 0.8, 1 and 2 with the same scale. |
| File Name | WEIBULL DIST Shape Comparison.png |

## Image 3: Results for the Pump Seal Story

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the input block and the formula result. |
| Content | The input table in `E1:E4` with the labels Age, Shape and Scale, the formula `=WEIBULL.DIST(E2, E3, E4, TRUE)` in an adjacent cell, and the result 0.430217 highlighted. |
| Alt Text | A worksheet with three Weibull inputs and a WEIBULL.DIST result of 0.430217. |
| File Name | WEIBULL DIST Pump Seal Result.png |
