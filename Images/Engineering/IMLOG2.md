---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
related:
  - IMLOG2
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - complex-numbers
  - images
---

# IMLOG2 Image Guide

Images planned for [IMLOG2](../../Functions/Engineering/IMLOG2.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Complex Number Text Format

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a single formula cell and its result cell. |
| Content | A cell containing `=IMLOG2("1+2i")` and the result `1.1610+1.5973i`. Callouts label the real part `1`, the imaginary part `2i`, and the result in `x+yi` form. |
| Alt Text | A worksheet cell showing IMLOG2 applied to the text 1+2i, with the complex result labeled. |
| File Name | IMLOG2 Complex Text Format.png |

## Image 2: Complex Input From Two Cells

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Screenshot of a small worksheet. |
| Content | Cell A2 holds 3 under a column labeled Real and cell B2 holds 3 under a column labeled Imaginary. Cell C2 shows `=IMLOG2(COMPLEX(A2,B2))` and its result `2.0850+1.1331i`. An arrow links each input cell to COMPLEX. |
| Alt Text | A worksheet with real and imaginary inputs in two cells feeding COMPLEX and IMLOG2. |
| File Name | IMLOG2 Complex From Cells.png |
