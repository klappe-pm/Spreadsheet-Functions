---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
related:
  - STDEVPA
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# STDEVPA Image Guide

Images planned for [STDEVPA](../../Functions/Statistical/STDEVPA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of a formula bar. |
| Content | The formula `=STDEVPA(value1, [value2], ...)` with `value1` highlighted as required, `[value2]` shown in brackets as optional, and an ellipsis marking more arguments. |
| Alt Text | A labeled STDEVPA formula showing the required first argument and optional additional arguments. |
| File Name | STDEVPA Syntax Anatomy.png |

## Image 2: Text Versus Number Handling

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 2 result. |
| Format | Side by side worksheet screenshots. |
| Content | Left: the range `A2:A7` with 4, 8, 6, "n/a", 5 and 7 and the STDEVPA result 2.581989 beside it. Right: the same range with the STDEVP result 1.414214. The "n/a" cell is shaded and labeled counted as 0 for STDEVPA and ignored for STDEVP. |
| Alt Text | Two worksheet ranges with a text entry, showing STDEVPA counting the text as zero and STDEVP ignoring it. |
| File Name | STDEVPA Text Handling.png |

## Image 3: Bottle Fill Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the bottle volume table with the formula bar visible. |
| Content | The table `A1:B9` with the Volume column highlighted, the formula `=STDEVPA(B2:B9)` in the formula bar, and the result 2.496873 in a labeled output cell. |
| Alt Text | A bottle volume table with STDEVPA applied to the volume column and a result of 2.496873. |
| File Name | STDEVPA Bottle Fill Result.png |
