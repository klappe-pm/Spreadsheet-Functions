---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
related:
  - IMSEC
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - complex-numbers
  - images
---

# IMSEC Image Guide

Images planned for [IMSEC](../../Functions/Engineering/IMSEC.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Complex Angle Input

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a single formula cell and its result cell. |
| Content | A cell containing `=IMSEC("1+1i")` and the result `0.4983+0.5911i`. Callouts label the angle `1+1i` as radians and the result in `x+yi` form. |
| Alt Text | A worksheet cell showing IMSEC applied to the complex angle 1+1i, with the result labeled. |
| File Name | IMSEC Complex Angle Input.png |

## Image 2: Complex Angle From Two Cells

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Screenshot of a small worksheet. |
| Content | Cell A2 holds 2 under a column labeled Real and cell B2 holds -1 under a column labeled Imaginary. Cell C2 shows `=IMSEC(COMPLEX(A2,B2))` and its result `-0.4131-0.6875i`. An arrow links each input cell to COMPLEX. |
| Alt Text | A worksheet with real and imaginary angle parts in two cells feeding COMPLEX and IMSEC. |
| File Name | IMSEC Angle From Cells.png |
