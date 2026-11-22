---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
related:
  - T.DIST.RT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# T.DIST.RT Image Guide

Images planned for [T.DIST.RT](../../Functions/Statistical/T.DIST.RT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Right Tail Area

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled t-distribution curve with the right tail shaded. |
| Content | A bell-shaped curve centered on zero with a vertical line at x and the area to its right shaded. The shaded area is labeled right tail, and the label notes that the area to the left of x is not included. |
| Alt Text | A t-distribution curve with the area to the right of x shaded and labeled as the right tail. |
| File Name | T.DIST.RT Right Tail.png |

## Image 2: One-Sided Decision Rule

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 4 result. |
| Format | Screenshot of a small worksheet with the decision cell highlighted. |
| Content | Cell B2 holds 1.5, cell C2 holds 24, the formula `=IF(T.DIST.RT(B2, 24) < 0.05, "Improvement Confirmed", "Not Confirmed")` is in the formula bar, and the output shows Not Confirmed with the probability 0.073328 in a neighboring cell. |
| Alt Text | A worksheet with a one-sided decision formula returning Not Confirmed because the right-tail probability is 0.073328. |
| File Name | T.DIST.RT Decision Rule.png |
