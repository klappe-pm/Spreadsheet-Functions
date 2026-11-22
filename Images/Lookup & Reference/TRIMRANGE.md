---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Array Shaping
related:
  - TRIMRANGE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - lookup-reference
---

# TRIMRANGE Image Guide

Images planned for [TRIMRANGE](../../Functions/Lookup%20%26%20Reference/TRIMRANGE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: TRIMRANGE Edge Codes

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram with a small grid and a legend. |
| Content | A grid with blank rows above and below a data block. The formula `=TRIMRANGE(range, [trim_rows], [trim_cols])` sits above the grid. A legend lists the codes: 0 none, 1 leading blanks, 2 trailing blanks, 3 both (the default). |
| Alt Text | A grid with blank rows above and below a data block, beside a legend of the trim_rows codes. |
| File Name | TRIMRANGE Edge Codes.png |

## Image 2: Trim Before and After

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, before Problem 1. |
| Format | Two screenshots side by side. |
| Content | Left: the form export in `A1:B12`, with the header row and six responses shaded and rows 8 to 12 shaded grey as blank padding. Right: the result of `=ROWS(TRIMRANGE(A1:B12))-1` in a labeled cell showing 6. |
| Alt Text | A form export with blank padding rows at the bottom and a TRIMRANGE count of 6 responses. |
| File Name | TRIMRANGE Trim Before and After.png |
