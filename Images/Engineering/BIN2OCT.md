---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
related:
  - BIN2OCT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - engineering
  - images
---

# BIN2OCT Image Guide

Images planned for [BIN2OCT](../../Functions/Engineering/BIN2OCT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=BIN2OCT(number, [places])` with `number` labeled as a binary value and `places` labeled as an optional width, shown in brackets. |
| Alt Text | A BIN2OCT formula with a required binary argument and an optional places argument. |
| File Name | BIN2OCT Syntax Anatomy.png |

## Image 2: Three-Bit Groups to Octal Digits

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Table with a binary and octal column. |
| Content | Rows for 000 to 111 with the matching octal digit 0 to 7, and a bracket that groups 101101 into 101 and 101 with the result 55. |
| Alt Text | A table of three-bit binary groups and their octal digits, with an example that splits 101101 into two groups of 101. |
| File Name | BIN2OCT Three Bit Groups.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet. |
| Content | The valve table in `A1:B4`, the helper column `C2:C4` holding the BIN2OCT results with three-character width, and the values 017, 012 and 006 beside the column. |
| Alt Text | A worksheet with three valve binary codes converted to three-digit octal values. |
| File Name | BIN2OCT Valve Codes Result.png |
