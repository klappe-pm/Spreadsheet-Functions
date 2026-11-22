---
domain: Spreadsheet Functions
category: Financial
subcategory: Depreciation
related:
  - VDB
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# VDB Image Guide

Images planned for [VDB](../../Functions/Financial/VDB.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=VDB(cost, salvage, life, start_period, end_period, [factor], [no_switch])` with each argument labeled. Brackets around factor and no_switch are marked optional. A timeline beneath the formula marks period 0 at the start of the life and shows start and end points on it. |
| Alt Text | A VDB formula with its seven arguments labeled and a timeline showing a start and end point within the asset's life. |
| File Name | VDB Syntax Anatomy.png |

## Image 2: Story Problem Result Panel

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the lathe terms and an eight-row schedule. |
| Content | Cost 1,800, salvage 200, life 8 in labeled cells. The yearly charges 450.00, 337.50, 253.13, 189.84, 142.38, 106.79, 80.09 and 40.27 sit in a column, with years 2 to 4 highlighted. The formula `=VDB(1800, 200, 8, 1, 4)` shows the result 780.47. |
| Alt Text | A worksheet schedule of eight declining depreciation charges with years 2 to 4 highlighted and a total of 780.47. |
| File Name | VDB Lathe Schedule Result.png |
