---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
related:
  - IMLOG10
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - complex-numbers
  - images
---

# IMLOG10 Image Guide

Images planned for [IMLOG10](../../Functions/Engineering/IMLOG10.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Complex Number Text Format

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a single formula cell and its result cell. |
| Content | A cell containing `=IMLOG10("1+2i")` and the result `0.3495+0.4808i`. Callouts label the real part `1`, the imaginary part `2i`, and the result in `x+yi` form. |
| Alt Text | A worksheet cell showing IMLOG10 applied to the text 1+2i, with the complex result labeled. |
| File Name | IMLOG10 Complex Text Format.png |

## Image 2: Complex Input From Two Cells

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Screenshot of a small worksheet. |
| Content | Cell A2 holds 2 under a column labeled Real and cell B2 holds 1 under a column labeled Imaginary. Cell C2 shows `=IMLOG10(COMPLEX(A2,B2))` and its result `0.3495+0.2014i`. An arrow links each input cell to COMPLEX. |
| Alt Text | A worksheet with real and imaginary inputs in two cells feeding COMPLEX and IMLOG10. |
| File Name | IMLOG10 Complex From Cells.png |
