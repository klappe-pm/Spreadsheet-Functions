---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Array Tools
related:
  - ARRAYFORMULA
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - array-formulas
  - images
---

# ARRAYFORMULA Image Guide

Images planned for [ARRAYFORMULA](../../Functions/Google-specific/ARRAYFORMULA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: ARRAYFORMULA Spill Into Empty Cells

| Item | Instruction |
| --- | --- |
| Placement | Description section, directly below the third paragraph. |
| Format | Annotated screenshot of a Google Sheets column. |
| Content | A formula `=ARRAYFORMULA(B2:B4 * C2:C4)` in D2 with the three results spilling into D2:D4. Cells below D4 are empty and outlined as room for the output. A second column shows `#REF!` for a case where D3 already holds data, with a callout explaining the overwrite. |
| Alt Text | An ARRAYFORMULA result spilling down three cells, with a note showing the #REF! error when the output is blocked. |
| File Name | ARRAYFORMULA Spill Into Empty Cells.png |

## Image 2: ARRAYFORMULA Parts Order Column

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the parts order table with a filled total column. |
| Content | The four parts with Quantity and Unit Price in columns B and C, the single formula in D2 that produces 10, 12, 24 and 4.5 in D2:D5, and a cell with `=SUM(D2:D5)` showing 50.5 in a labeled output cell. |
| Alt Text | A parts order table with a column of line totals produced by one ARRAYFORMULA and a total of 50.5. |
| File Name | ARRAYFORMULA Parts Order Column.png |
