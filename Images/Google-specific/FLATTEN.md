---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Array Tools
related:
  - FLATTEN
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - arrays
  - images
---

# FLATTEN Image Guide

Images planned for [FLATTEN](../../Functions/Google-specific/FLATTEN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: FLATTEN Reading Order

| Item | Instruction |
| --- | --- |
| Placement | Description section, directly below the third paragraph. |
| Format | Diagram with two parts: a two by two grid and a single output column. |
| Content | Left: the grid A1:B2 with values 1, 2 in the first row and 3, 4 in the second, with arrows numbered 1 to 4 showing the row by row reading order. Right: the output column with 1, 2, 3, 4 in the same order. |
| Alt Text | A two by two grid read row by row, with its values listed in order in a single output column. |
| File Name | FLATTEN Reading Order.png |

## Image 2: FLATTEN Survey Grid Filter

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the survey grid and its filtered output. |
| Content | The respondent grid in A1:C4 with blank cells outlined, and the formula `=FILTER(FLATTEN(B2:C4), FLATTEN(B2:C4) <> "")` in a cell beside it. The output shows 5, 7, 9 and 4 in a single column with no blank rows. |
| Alt Text | A survey grid with blank cells and a filtered single column of four scores. |
| File Name | FLATTEN Survey Grid Filter.png |
