---
domain: Spreadsheet Functions
category: Engineering
subcategory: Comparison and Conversion
related:
  - DELTA
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - comparison
  - images
---

# DELTA Image Guide

Images planned for [DELTA](../../Functions/Engineering/DELTA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Equal and Unequal Comparisons

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two side-by-side panels, one for a match and one for a mismatch. |
| Content | Left panel: a balance with 5 on both sides, captioned `DELTA(5,5)` returns 1. Right panel: a balance with 5 and 4, captioned `DELTA(5,4)` returns 0. A small note beneath says that omitting the second number compares with 0. |
| Alt Text | Two balance diagrams, one showing equal values and one showing unequal values, with the DELTA result for each. |
| File Name | DELTA Equal Unequal Comparison.png |

## Image 2: Batch Flags Table

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with batch counts, targets and flags. |
| Content | Columns B and C hold the filled and target counts (48 and 48, 47 and 48, 50 and 50). Column D shows the flags 1, 0, and 1, and cell D5 shows the total 2. The formula `=DELTA(B2,C2)` is visible in the formula bar. |
| Alt Text | A worksheet comparing three batch counts with their targets, with a 1 or 0 flag per row and a total. |
| File Name | DELTA Batch Flags.png |
