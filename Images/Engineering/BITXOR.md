---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bitwise Operations
related:
  - BITXOR
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - bitwise
  - images
---

# BITXOR Image Guide

Images planned for [BITXOR](../../Functions/Engineering/BITXOR.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Bit-by-Bit Comparison of Two Values

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Three stacked rows of eight bit boxes with a column of matching and differing positions. |
| Content | Row 1: the bits of 5 (`00000101`). Row 2: the bits of 3 (`00000011`). Row 3: the result (`00000110`). Positions that differ are shaded in row 3 and labeled differ. Caption: `BITXOR(5,3) returns 6`. |
| Alt Text | Two bit patterns, 5 and 3, compared position by position with the differing positions shaded in the result row. |
| File Name | BITXOR Bit Comparison.png |

## Image 2: Sensor Masks and Changed Bits Table

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the mask pairs and the XOR result. |
| Content | Columns B and C hold the previous and current masks (22 and 19, 31 and 31, 8 and 24). Column D holds the formula `=BITXOR(B2,C2)` and the results 5, 0, and 16. The changed bits of the Line 1 row are highlighted in the result cell. |
| Alt Text | A worksheet comparing three pairs of sensor masks, with the changed bits returned in a result column. |
| File Name | BITXOR Sensor Mask Changes.png |
