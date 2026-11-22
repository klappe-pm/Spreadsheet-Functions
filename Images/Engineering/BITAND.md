---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bitwise Operations
related:
  - BITAND
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - engineering
  - images
---

# BITAND Image Guide

Images planned for [BITAND](../../Functions/Engineering/BITAND.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=BITAND(number1, number2)` with both arguments labeled as whole numbers zero or greater. |
| Alt Text | A BITAND formula with two required whole-number arguments. |
| File Name | BITAND Syntax Anatomy.png |

## Image 2: Bit Overlap Diagram

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two stacked binary rows with a result row. |
| Content | Rows for 3 (011), 6 (110) and the result (010). Columns where both rows hold a 1 are shaded and the result row shows 1 only in the shaded column. Caption: a result bit is 1 only when both inputs are 1. |
| Alt Text | Two binary rows stacked over a result row, with one shaded column where both inputs are 1. |
| File Name | BITAND Bit Overlap.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet. |
| Content | The user table in `A1:B6`, the helper column `C2:C6` holding the BITAND results against mask 4, and the COUNTIF total 4 in `C7` with a label. Rows with the Approve bit are highlighted. |
| Alt Text | A worksheet of five user masks with BITAND results in a helper column and a count of four users with the Approve bit. |
| File Name | BITAND Approval Rights Result.png |
