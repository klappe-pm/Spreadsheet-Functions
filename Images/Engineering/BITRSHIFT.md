---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bitwise Operations
related:
  - BITRSHIFT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - bitwise
  - images
---

# BITRSHIFT Image Guide

Images planned for [BITRSHIFT](../../Functions/Engineering/BITRSHIFT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Bit Pattern Before and After a Right Shift

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two rows of eight bit boxes with a labeled arrow between them. |
| Content | Top row: the bits of 13 (`00001101`) with the two rightmost boxes outlined and labeled dropped. Bottom row: the remaining bits (`00000011`) with the two left boxes filled with zeros and labeled filled. A caption reads `BITRSHIFT(13,2) returns 3`. |
| Alt Text | Eight bit boxes for 13 shown before and after a right shift of two places, with the dropped bits outlined. |
| File Name | BITRSHIFT Bit Pattern Shift.png |

## Image 2: Badge IDs Split Into Site and Door Fields

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the badge list in column A and the formula result in column B. |
| Content | Column A lists 25857, 12290, 4611, and 65281. Column B shows 101, 48, 18, and 255. The formula `=BITRSHIFT(A2,8)` appears in the formula bar, and the upper byte of one badge ID is shaded. |
| Alt Text | A worksheet with four badge IDs in one column and their site codes in the next column, computed with BITRSHIFT by 8 places. |
| File Name | BITRSHIFT Badge Site Codes.png |
