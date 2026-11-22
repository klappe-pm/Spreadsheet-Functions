---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
related:
  - IMSUM
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - complex-numbers
  - images
---

# IMSUM Image Guide

Images planned for [IMSUM](../../Functions/Engineering/IMSUM.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula. |
| Content | The formula `=IMSUM(inumber1, [inumber2], ...)` with `inumber1` labeled as required, `[inumber2]` labeled as optional, and the ellipsis labeled as more values up to 255 arguments in total. |
| Alt Text | Diagram of the IMSUM formula with required and optional arguments labeled. |
| File Name | IMSUM Syntax Anatomy.png |

## Image 2: Summing a Range of Complex Values

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 4 result. |
| Format | Screenshot of a worksheet column. |
| Content | Cells B2 to B4 holding `4+1i`, `1+3i` and `2-2i`, with the range outlined. Cell B5 holds the formula `=IMSUM(B2:B4)` and shows the result `7+2i`. |
| Alt Text | A worksheet column of three complex numbers summed by IMSUM to give 7+2i. |
| File Name | IMSUM Range Sum.png |
