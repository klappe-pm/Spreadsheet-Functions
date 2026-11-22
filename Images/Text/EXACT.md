---
domain: Spreadsheet Functions
category: Text
subcategory: Text Comparison
related:
  - EXACT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# EXACT Image Guide

Images planned for [EXACT](../../Functions/Text/EXACT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: EXACT Arguments and Result

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | Two cells, A2 with `Summer2026` and B2 with `summer2026`, and a formula cell with `=EXACT(A2, B2)` showing `FALSE`. Arrows point to each argument, labeled text1 and text2. |
| Alt Text | A worksheet where EXACT compares two passwords that differ only by case and returns FALSE. |
| File Name | EXACT Arguments Result.png |

## Image 2: Case and Space Differences in Matching Rows

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of two SKU columns side by side with a result column. |
| Content | List A and List B with the five SKU rows. Row 2 (Red Hen and red hen) is outlined with a label "case differs". Row 4 (Gray Cat and Gray Cat with a trailing space) is outlined with the label "trailing space". Rows 1, 3 and 5 are marked TRUE in a helper column. The count cell shows 3. |
| Alt Text | Two SKU lists where rows 1, 3 and 5 match exactly and rows 2 and 4 differ in case or spacing. |
| File Name | EXACT SKU Matches.png |
