---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
related:
  - HEX2OCT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - engineering
  - images
---

# HEX2OCT Image Guide

Images planned for [HEX2OCT](../../Functions/Engineering/HEX2OCT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=HEX2OCT(B2, 4)` in the formula bar. The argument B2 is labeled number (hex) and the argument 4 is labeled places (optional padding). |
| Alt Text | A formula bar showing HEX2OCT with a hex number and an optional places argument labeled. |
| File Name | HEX2OCT Syntax Anatomy.png |

## Image 2: Permission Mode Table

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4 and before the Story Problems heading. |
| Format | Screenshot of a worksheet with file names, hex permissions and octal results. |
| Content | Column B lists 1ED, 1A4 and 1FF. Column C shows 0755, 0644 and 0777 from `=HEX2OCT(B2, 4)`, with the config.env row highlighted and the padding zero labeled. |
| Alt Text | A worksheet that converts three hex permission values to four-digit octal modes. |
| File Name | HEX2OCT Permission Mode Table.png |
