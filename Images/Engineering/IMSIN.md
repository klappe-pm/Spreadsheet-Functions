---
domain: Spreadsheet Functions
category: Engineering
subcategory: Complex Numbers
related:
  - IMSIN
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - complex-numbers
  - images
---

# IMSIN Image Guide

Images planned for [IMSIN](../../Functions/Engineering/IMSIN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Complex Angle Input

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a single formula cell and its result cell. |
| Content | A cell containing `=IMSIN("1+1i")` and the result `1.2985+0.6350i`. Callouts label the angle `1+1i` as radians and the result in `x+yi` form. |
| Alt Text | A worksheet cell showing IMSIN applied to the complex angle 1+1i, with the result labeled. |
| File Name | IMSIN Complex Angle Input.png |

## Image 2: Sum of Two Complex Samples

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of a small worksheet. |
| Content | The sample table with angles `1+1i` and `2-1i` in cells B2 and B3, the formula `=IMSUM(IMSIN(B2), IMSIN(B3))` in the solution cell, and the result `2.7016+1.1240i` in a labeled output cell. |
| Alt Text | A worksheet where IMSIN is applied to two samples and IMSUM returns their combined value 2.7016+1.1240i. |
| File Name | IMSIN Combined Sample Result.png |
