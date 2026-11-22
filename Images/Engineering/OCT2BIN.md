---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
related:
  - OCT2BIN
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - base-conversion
  - images
---

# OCT2BIN Image Guide

Images planned for [OCT2BIN](../../Functions/Engineering/OCT2BIN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula. |
| Content | The formula `=OCT2BIN(number, [places])` with `number` labeled as the octal input and `[places]` labeled as the optional output width. |
| Alt Text | Diagram of the OCT2BIN formula with its required and optional arguments labeled. |
| File Name | OCT2BIN Syntax Anatomy.png |

## Image 2: Padding a Binary Result to a Fixed Width

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 2 result. |
| Format | Screenshot of a worksheet with two rows. |
| Content | Row 2 shows `=OCT2BIN(12)` returning `1010`. Row 3 shows `=OCT2BIN(17,8)` returning `00001111`. The eight-character width is outlined and labeled as the places argument. |
| Alt Text | A worksheet comparing an unpadded binary result with a result padded to eight characters. |
| File Name | OCT2BIN Padding.png |
