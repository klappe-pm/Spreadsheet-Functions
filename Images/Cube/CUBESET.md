---
category: Cube
subcategory: OLAP Sets
related:
  - CUBESET
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - cube
  - images
---

# CUBESET Image Guide

Images planned for [CUBESET](../../Functions/Cube/CUBESET.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Set Expression and Sort Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the function call. |
| Content | The formula `=CUBESET(connection, set_expression, [caption], [sort_order], [sort_by])`. Beside sort_order, a table lists 0 SortNone, 1 SortAscending, 2 SortDescending, 3 alphabetical ascending, 4 alphabetical descending, 5 natural ascending and 6 natural descending. An arrow links sort_by to sort_order 1 and 2 with the note required. |
| Alt Text | A diagram of the CUBESET arguments with the sort_order codes listed and sort_by linked to codes 1 and 2. |
| File Name | CUBESET Arguments.png |

## Image 2: Sorted Set Versus Cube Order

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly after Example 4. |
| Format | Two side by side lists. |
| Content | Left list: reps in cube order. Right list: the same reps sorted by Sales Amount from highest to lowest, captioned Reps by Sales. An arrow shows the sort_order 2 argument that produces the right list. |
| Alt Text | Two lists of reps, one in cube order and one sorted by sales from highest to lowest. |
| File Name | CUBESET Sorted Versus Cube Order.png |

## Image 3: Ascending Set Returning the First Member

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a store table and a result cell. |
| Content | The four stores with sales 8200, 9100, 7600 and 6400 are listed. The Valley row is highlighted at the top of a sorted helper column, and the result cell shows Valley. |
| Alt Text | A worksheet with four stores and Valley highlighted as the lowest seller. |
| File Name | CUBESET Lowest Store.png |
