---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
related:
  - HEX2BIN
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - engineering
  - images
---

# HEX2BIN Image Guide

Images planned for [HEX2BIN](../../Functions/Engineering/HEX2BIN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=HEX2BIN(B2, 8)` in the formula bar. The argument B2 is labeled number (hex) and the argument 8 is labeled places (optional padding). |
| Alt Text | A formula bar showing HEX2BIN with a hex number and an optional places argument labeled. |
| File Name | HEX2BIN Syntax Anatomy.png |

## Image 2: Padded Status Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4 and before the Story Problems heading. |
| Format | Screenshot of a worksheet with hex codes and binary results. |
| Content | Column B lists hex codes 1F, A0 and 07. Column C shows the results 00011111, 10100000 and 00000111 from `=HEX2BIN(B2, 8)`, with the A0 row highlighted and bits 7 and 5 labeled. |
| Alt Text | A worksheet that converts three hex status codes to eight-digit binary values. |
| File Name | HEX2BIN Padded Status Worksheet.png |
