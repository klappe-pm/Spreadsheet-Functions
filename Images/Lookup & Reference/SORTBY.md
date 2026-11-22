---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Dynamic Arrays
related:
  - SORTBY
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - lookup-reference
---

# SORTBY Image Guide

Images planned for [SORTBY](../../Functions/Lookup%20%26%20Reference/SORTBY.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: SORTBY Key Pairs

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=SORTBY(array, by_array1, [sort_order1], [by_array2, sort_order2], ...)`. The array is shaded, the first key and its direction share one color, and the second key and direction share another. |
| Alt Text | The SORTBY formula with the data array shaded and two key and direction pairs in different colors. |
| File Name | SORTBY Key Pairs.png |

## Image 2: Two-Key Sort Layout

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Two worksheet screenshots side by side. |
| Content | Left: the sales list in `A2:C6` with Region and Sales columns highlighted as keys. Right: the result of `=SORTBY(A2:C6, B2:B6, 1, C2:C6, -1)` with East rows first (Avery above Casey), then North, then West (Emery above Blake). |
| Alt Text | A sales list and its sorted result, grouped by region and ordered by sales within each region. |
| File Name | SORTBY Two-Key Sort Layout.png |
