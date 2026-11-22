---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - CONFIDENCE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# CONFIDENCE Image Guide

Images planned for [CONFIDENCE](../../Functions/Statistical/CONFIDENCE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Confidence Interval Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Diagram of a normal curve with a centered interval. |
| Content | A bell curve with the middle region shaded and labeled 1 minus alpha. Two tails are labeled alpha divided by 2. Beside the curve, three labels name the alpha, standard_dev and size arguments and show where each enters the margin. |
| Alt Text | A normal curve with the central interval shaded, showing how alpha, standard deviation and sample size set the margin of error. |
| File Name | CONFIDENCE Interval Arguments.png |

## Image 2: Interval Limits From a Sample Mean

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Screenshot of a small worksheet with the limit formulas. |
| Content | Cells `B2` (52.4), `B3` (4.2) and `B4` (36), the lower limit formula `=B2-CONFIDENCE(0.05, B3, B4)` in one cell showing 51.028025, and the upper limit formula in a second cell showing 53.771975. A bracket marks the interval between the two results. |
| Alt Text | A worksheet computing the lower and upper limits of a 95 percent interval around a sample mean of 52.4 with CONFIDENCE. |
| File Name | CONFIDENCE Interval Limits.png |
