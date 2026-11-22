---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bitwise Operations
related:
  - BITOR
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - engineering
  - images
---

# BITOR Image Guide

Images planned for [BITOR](../../Functions/Engineering/BITOR.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=BITOR(number1, number2)` with both arguments labeled as whole numbers zero or greater. |
| Alt Text | A BITOR formula with two required whole-number arguments. |
| File Name | BITOR Syntax Anatomy.png |

## Image 2: Bit Union Diagram

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two stacked binary rows with a result row. |
| Content | Rows for 6 (0110), 11 (1011) and the result (1111). Each column where either row holds a 1 is shaded, and the result row is 1 in every shaded column. Caption: a result bit is 1 when either input is 1. |
| Alt Text | Two binary rows stacked over a result row, with every column that holds a 1 in either row shaded in the result. |
| File Name | BITOR Bit Union.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet. |
| Content | The sensor table in `A1:B3` with readings 5 and 10, the combined result 15 in `C2` with a label, and a legend beside the table naming the four alarm bits. |
| Alt Text | A worksheet with two alarm sensor readings combined by BITOR into a single value of 15 with a legend of the four alarms. |
| File Name | BITOR Alarm Panel Result.png |
