---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
related:
  - IMSECH
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - complex-numbers
  - images
---

# IMSECH Image Guide

Images planned for [IMSECH](../../Functions/Engineering/IMSECH.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Complex Input for a Hyperbolic Function

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a single formula cell and its result cell. |
| Content | A cell containing `=IMSECH("1+1i")` and the result `0.4983-0.5911i`. Callouts label the input `1+1i` as the complex value and the result in `x+yi` form. |
| Alt Text | A worksheet cell showing IMSECH applied to the complex value 1+1i, with the result labeled. |
| File Name | IMSECH Complex Input.png |

## Image 2: Input From Two Cells

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Screenshot of a small worksheet. |
| Content | Cell A2 holds 2 under a column labeled Real and cell B2 holds -1 under a column labeled Imaginary. Cell C2 shows `=IMSECH(COMPLEX(A2,B2))` and its result `0.1512+0.2270i`. An arrow links each input cell to COMPLEX. |
| Alt Text | A worksheet with real and imaginary parts in two cells feeding COMPLEX and IMSECH. |
| File Name | IMSECH Input From Cells.png |
