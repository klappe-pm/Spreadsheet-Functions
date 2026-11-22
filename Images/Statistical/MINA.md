---
domain: Spreadsheet Functions
category: Statistical
subcategory: Extremes
related:
  - MINA
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# MINA Image Guide

Images planned for [MINA](../../Functions/Statistical/MINA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Logical Values in a Reference

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet column. |
| Content | Cells `B2:B4` holding 0.5, FALSE, and TRUE, with the FALSE and TRUE cells outlined. Callouts beside them read FALSE counts as 0 and TRUE counts as 1. The formula `=MINA(B2:B4)` appears in a cell below with the result 0. |
| Alt Text | A worksheet column with FALSE and TRUE callouts and a MINA result of 0. |
| File Name | MINA Logical Values Reference.png |

## Image 2: MIN Compared With MINA

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 1 and Example 2. |
| Format | Side by side comparison of two worksheet cells. |
| Content | The same range `B2:B4` shown twice. Left caption: `=MINA(B2:B4)` returns 0. Right caption: `=MIN(B2:B4)` returns 0.5. Both captions use the same column of values. |
| Alt Text | Two results for the same range, MINA returning 0 and MIN returning 0.5. |
| File Name | MINA Versus MIN.png |
