---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - GAMMAINV
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# GAMMAINV Image Guide

Images planned for [GAMMAINV](../../Functions/Statistical/GAMMAINV.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of the formula. |
| Content | The formula `=GAMMAINV(probability, alpha, beta)` with callouts: probability is between 0 and 1, alpha is the shape, and beta is the scale. A note beside the formula says the result is a value, not a probability. |
| Alt Text | A labeled GAMMAINV formula showing the probability, alpha and beta arguments. |
| File Name | GAMMAINV Syntax Anatomy.png |

## Image 2: Probability to Value Mapping

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Cumulative curve with an arrow path. |
| Content | The cumulative gamma curve for shape 4 and scale 5. A horizontal line at 0.9 meets the curve, and a vertical arrow drops to the x axis at 33.40. Caption: the probability goes in, the value comes out. |
| Alt Text | A cumulative gamma curve with a line at probability 0.9 dropping to a value of about 33.4 on the horizontal axis. |
| File Name | GAMMAINV Probability to Value Mapping.png |
