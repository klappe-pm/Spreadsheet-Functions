---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
related:
  - VAR.P
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - statistics
---

# VAR.P Image Guide

Images planned for [VAR.P](../../Functions/Statistical/VAR.P.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Population Divisor Compared With Sample Divisor

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two stacked formula panels with a shared sum of squares. |
| Content | The same sum of squared deviations, 17.5, shown at the top. The lower left panel divides by 6 and labels the result population variance, VAR.P, 2.9167. The lower right panel divides by 5 and labels the result sample variance, VAR.S, 3.5. A note between the panels reads the population divisor is the count of values. |
| Alt Text | Two formula panels that divide the same sum of squares of 17.5 by six for VAR.P and by five for VAR.S. |
| File Name | VAR.P Population Divisor.png |

## Image 2: Machine Output Population Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a column chart beside the data. |
| Content | The five machine outputs in `A1:B6` with the formula `=VAR.P(B2:B6)` in a labeled output cell showing 17.2. A column chart beside the table shows each machine's output with a horizontal line at the mean of 45 units per hour. |
| Alt Text | A worksheet of five machine outputs with a population variance result of 17.2 and a column chart with a mean line at 45 units per hour. |
| File Name | VAR.P Machine Output Variance.png |
