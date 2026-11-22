---
domain: Spreadsheet Functions
category: Text
subcategory: Case Conversion
related:
  - UPPER
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# UPPER Image Guide

Images planned for [UPPER](../../Functions/Text/UPPER.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Input and Output Cells

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | Column A holds mixed-case codes such as `sku-4417b`, column B holds `=UPPER(A2)` with the result `SKU-4417B`. An arrow links column A to column B. |
| Alt Text | A worksheet with a mixed-case code in one column and its uppercase version in the next column. |
| File Name | UPPER Input Output Cells.png |

## Image 2: Chained Case Functions

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly after Example 3. |
| Format | Step diagram with three boxes. |
| Content | Box 1 shows `mARCH` with LEFT taking the first letter. Box 2 shows UPPER turning `m` into `M`. Box 3 shows LOWER applied to `ARCH` and the joined result `March`. |
| Alt Text | A diagram showing how LEFT, UPPER, MID and LOWER combine to turn mARCH into March. |
| File Name | UPPER Chained Case Steps.png |
