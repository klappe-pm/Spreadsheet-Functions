---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
related:
  - IMTAN
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - complex-numbers
  - images
---

# IMTAN Image Guide

Images planned for [IMTAN](../../Functions/Engineering/IMTAN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula. |
| Content | The formula `=IMTAN(inumber)` with `inumber` labeled and three accepted inputs listed beneath it: text in `x+yi` form, a COMPLEX result and a real number. |
| Alt Text | Diagram of the IMTAN formula with its argument and the three accepted input types labeled. |
| File Name | IMTAN Syntax Anatomy.png |

## Image 2: Real and Imaginary Parts in Separate Cells

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 3 result. |
| Format | Screenshot of a worksheet with three columns. |
| Content | Cells A2 holds 0.5, B2 holds 0.25 and C2 holds `=IMTAN(COMPLEX(A2,B2))` showing `0.5045007027+0.3124206925i`. The real and imaginary inputs are outlined and labeled. |
| Alt Text | A worksheet where the real and imaginary parts of a complex input sit in separate cells and feed IMTAN through COMPLEX. |
| File Name | IMTAN Separate Cells.png |
