---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Query and Filtering
related:
  - SORTN
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - sorting
---

# SORTN Image Guide

Images planned for [SORTN](../../Functions/Google-specific/SORTN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Top N Argument Layout

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of a single formula. |
| Content | The formula `=SORTN(range, [n], [display_ties_mode], [sort_column1, is_ascending1], ...)` with each argument boxed. The optional arguments are drawn in a lighter outline. A small inset explains that `n` is the number of rows kept and that the sort pairs are applied in order. |
| Alt Text | Diagram of the SORTN formula showing the range, the row count, the ties mode and the sort column and direction pairs. |
| File Name | SORTN Top N Argument Layout.png |

## Image 2: Sorted Output Examples

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a worksheet. |
| Content | The player table in `A1:C6` with the Points column highlighted. Beside it, the SORTN output from Example 2 showing three rows, Chen, Lindqvist and Rivers, with the Points column sorted from highest to lowest. The two excluded rows, Okafor and Moreno, are greyed out. |
| Alt Text | A player table with the top three rows by points returned by SORTN and the remaining rows greyed out. |
| File Name | SORTN Sorted Output.png |
