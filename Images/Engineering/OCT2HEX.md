---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
related:
  - OCT2HEX
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - base-conversion
  - images
---

# OCT2HEX Image Guide

Images planned for [OCT2HEX](../../Functions/Engineering/OCT2HEX.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula. |
| Content | The formula `=OCT2HEX(number, [places])` with `number` labeled as the octal input and `[places]` labeled as the minimum output width. |
| Alt Text | Diagram of the OCT2HEX formula with its required and optional arguments labeled. |
| File Name | OCT2HEX Syntax Anatomy.png |

## Image 2: Padding a Hexadecimal Result to a Fixed Width

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 2 result. |
| Format | Screenshot of a worksheet with two rows. |
| Content | Row 2 shows `=OCT2HEX(20,4)` returning `0010`. Row 3 shows `=OCT2HEX(377)` returning `FF`. The four-character width is outlined and labeled as the places argument. |
| Alt Text | A worksheet comparing a hexadecimal result padded to four characters with an unpadded result. |
| File Name | OCT2HEX Padding.png |
