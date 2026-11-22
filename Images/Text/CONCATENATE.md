---
category: Text
subcategory: Text Joining and Splitting
related:
  - CONCATENATE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - compatibility
  - excel
  - images
---

# CONCATENATE Image Guide

Images planned for [CONCATENATE](../../Functions/Text/CONCATENATE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Joining Cells With Explicit Separators

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated worksheet screenshot. |
| Content | Cells A2 and B2 with values, the formula `=CONCATENATE(A2, " ", B2)` in the formula bar, and the result cell. A callout points to the space argument and says the function adds no separator. |
| Alt Text | A worksheet showing a CONCATENATE formula with an explicit space argument between two cells. |
| File Name | CONCATENATE Explicit Separators.png |

## Image 2: Legacy Formula Versus Modern Replacement

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Side by side diagram. |
| Content | Left: `=CONCATENATE(A2, " ", B2, " ", C2)` labeled compatibility. Right: `=CONCAT(A2:C2)` labeled modern replacement, which accepts a range. Both show the same result for one row. |
| Alt Text | Two formulas giving the same result, one using the older function and one using CONCAT. |
| File Name | CONCATENATE Legacy Versus CONCAT.png |
