---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
related:
  - OFFSET
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - reference
---

# OFFSET Image Guide

Images planned for [OFFSET](../../Functions/Lookup%20%26%20Reference/OFFSET.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: OFFSET Argument Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated worksheet screenshot with a formula bar callout. |
| Content | The formula `=OFFSET(B2, 3, 0)` in the formula bar. Cell B2 is marked as the starting reference. Arrows show a move three rows down to B5, which is highlighted as the result. Labels beside the formula name the rows and cols arguments and note that height and width are optional. |
| Alt Text | A worksheet with an OFFSET formula, showing a move from the starting cell B2 down three rows to the highlighted result B5. |
| File Name | OFFSET Argument Anatomy.png |

## Image 2: Rolling Window Range

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 3. |
| Format | Worksheet screenshot of the weekly sales table with a shaded result block. |
| Content | The table in `A1:B7` with B2 marked as the start. The three cells B5, B6 and B7 are shaded as the window, with the sum 180 and the average 60 shown in labeled result cells. A bracket beside the shaded cells reads height 3. |
| Alt Text | A weekly sales table with the last three weeks shaded as the window that OFFSET returns, with its average of 60 shown. |
| File Name | OFFSET Rolling Window Range.png |

## Image 3: Four Week Window Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, directly below the Problem 1 answer. |
| Format | Screenshot of the sales table with the selected weeks outlined. |
| Content | The weekly sales table in `A1:B7` with the value 4 in `D1`. The cells B4 through B7 are outlined, and the result cell shows 210. A small note reads four rows from B7 upward, starting at B4. |
| Alt Text | A weekly sales table with the four most recent weeks outlined and a total of 210 shown in the result cell. |
| File Name | OFFSET Four Week Window Result.png |
