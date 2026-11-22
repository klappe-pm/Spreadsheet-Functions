---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
related:
  - BIN2DEC
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - engineering
  - images
---

# BIN2DEC Image Guide

Images planned for [BIN2DEC](../../Functions/Engineering/BIN2DEC.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=BIN2DEC(number)` with `number` labeled as a binary value of up to 10 characters. |
| Alt Text | A BIN2DEC formula with its single argument labeled as a binary value. |
| File Name | BIN2DEC Syntax Anatomy.png |

## Image 2: Sign Bit Layout

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Diagram of a 10-bit row of boxes. |
| Content | Ten boxes labeled with positions 9 to 0. The leftmost box is marked sign bit, the other nine are marked magnitude bits. Two example rows show 0111111111 (511) and 1000000000 (-512) with arrows to their decimal values. |
| Alt Text | A row of ten bit boxes with the leftmost box marked as the sign bit, and the two extreme values labeled 511 and -512. |
| File Name | BIN2DEC Sign Bit Layout.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet. |
| Content | The sensor and code table in `A1:B5`, the helper column `C2:C5` holding the BIN2DEC results, and the SUM total 67 in `C6` with a label. |
| Alt Text | A worksheet with four sensor codes converted to decimal in a helper column and a SUM total of 67. |
| File Name | BIN2DEC Shelf Sensor Result.png |
