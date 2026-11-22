---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
related:
  - IMPORTCSV
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - csv
  - images
---

# IMPORTCSV Image Guide

Images planned for [IMPORTCSV](../../Functions/Web/IMPORTCSV.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Import Formula Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=IMPORTCSV("C:\Exports\orders.csv", 1)` in the formula bar, with callouts pointing to path, skip_rows, take_rows and locale, and the optional arguments marked as optional. |
| Alt Text | The formula bar showing an IMPORTCSV formula with its arguments labeled. |
| File Name | IMPORTCSV Formula Anatomy.png |

## Image 2: Spilled Array Beside the Formula

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 4 and Example 5. |
| Format | Screenshot of a worksheet. |
| Content | The formula in cell E1 with the imported order rows spilling into E1:G5, the spill range outlined, and a note that the cells below must be empty. |
| Alt Text | A worksheet where an IMPORTCSV formula spills five rows of order data beside it. |
| File Name | IMPORTCSV Spilled Array.png |

## Image 3: Last Three Rows Highlighted

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the visits list with matching rows highlighted. |
| Content | The Day and Visits table with the Thu, Fri and Sat rows highlighted, the formula `=SUM(INDEX(IMPORTCSV("C:\Exports\visits.csv", 1, -3), 0, 2))` in a labeled cell, and the result 377 beside it. |
| Alt Text | A visits list with the last three days highlighted and a total of 377. |
| File Name | IMPORTCSV Last Three Rows.png |
