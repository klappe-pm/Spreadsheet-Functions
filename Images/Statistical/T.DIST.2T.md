---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
related:
  - T.DIST.2T
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# T.DIST.2T Image Guide

Images planned for [T.DIST.2T](../../Functions/Statistical/T.DIST.2T.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Two Tails of the Distribution

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled t-distribution curve with two shaded tails. |
| Content | A bell-shaped curve centered on zero with vertical lines at -x and +x. The area beyond +x and the area below -x are shaded in the same color and labeled as the two tails whose sum is the result. |
| Alt Text | A t-distribution curve with both tails beyond the absolute value of x shaded and labeled. |
| File Name | T.DIST.2T Two Tails.png |

## Image 2: Negative Statistic Handling

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 4 result. |
| Format | Side by side formula comparison in a worksheet. |
| Content | Left: the formula `=T.DIST.2T(-1.8, 15)` with the result `#NUM!` highlighted. Right: the formula `=T.DIST.2T(ABS(-1.8), 15)` with the result 0.092002 highlighted. A caption reads ABS makes the input non-negative. |
| Alt Text | Two formulas side by side, one returning a number error for a negative input and one returning 0.092002 after ABS is applied. |
| File Name | T.DIST.2T ABS Comparison.png |

## Image 3: Support Ticket Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of a small worksheet with the statistic and formula visible. |
| Content | Cell B2 holds -1.8, cell C2 holds 15, and the formula `=T.DIST.2T(ABS(B2), 15)` is in the output cell showing 0.092002. |
| Alt Text | A worksheet with a statistic of -1.8 and a two-tailed T.DIST.2T result of 0.092002. |
| File Name | T.DIST.2T Support Ticket Result.png |
