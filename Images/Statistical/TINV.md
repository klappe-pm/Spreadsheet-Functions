---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - TINV
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# TINV Image Guide

Images planned for [TINV](../../Functions/Statistical/TINV.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Probability and Degrees of Freedom

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of a t-distribution curve with both tails shaded. |
| Content | The curve with both tails beyond the critical value shaded in one color, a bracket labeled total two-tailed probability spanning both tails, and the positive critical value marked on the right. |
| Alt Text | A t-distribution curve with both tails shaded and labeled as the total two-tailed probability used by TINV. |
| File Name | TINV Probability Anatomy.png |

## Image 2: Replacement Check

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 4 result. |
| Format | Side by side worksheet comparison. |
| Content | Column B holds `=TINV(0.05, 10)` returning 2.228139 and column C holds `=T.INV.2T(0.05, 10)` returning 2.228139. A check cell beside them shows TRUE when the two values match. |
| Alt Text | Two worksheet columns with TINV and T.INV.2T returning the same value 2.228139, and a check cell showing TRUE. |
| File Name | TINV Replacement Check.png |
