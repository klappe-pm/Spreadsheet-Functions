---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Classic Lookup
related:
  - HLOOKUP
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - lookup
---

# HLOOKUP Image Guide

Images planned for [HLOOKUP](../../Functions/Lookup%20%26%20Reference/HLOOKUP.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: HLOOKUP Argument Layout

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated worksheet screenshot. |
| Content | The quarterly table in `A1:G4` with the first row outlined as the search row, the lookup value Mar highlighted in row 1, and the value 150 highlighted in row 2 of the same column. Labels name table_array, lookup_value and row_index_num. |
| Alt Text | A worksheet table with HLOOKUP arguments labeled, showing the search in the top row and the returned value in row 2. |
| File Name | HLOOKUP Argument Layout.png |

## Image 2: Commission Tier Lookup

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Diagram of the tier table with a marker on the sales figure. |
| Content | The tier table `B1:E2` with thresholds 0, 1000, 2000 and 3000 across the top and rates beneath. A marker sits on sales of 1240, between 1000 and 2000, and the 4% cell is shaded. |
| Alt Text | A commission tier table with sales of 1240 falling in the 1000 tier, which pays 4 percent. |
| File Name | HLOOKUP Commission Tiers.png |

## Image 3: Exact Versus Approximate Match

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Side-by-side diagram of two results from the same header row. |
| Content | Left: an exact match with FALSE, where only the exact header Mar is highlighted. Right: an approximate match with TRUE on the sorted tiers, where 750 highlights the 500 column because it is the largest value that does not exceed 750. |
| Alt Text | Two HLOOKUP results comparing an exact match on a month with an approximate match on a sorted tier row. |
| File Name | HLOOKUP Exact Versus Approximate.png |
