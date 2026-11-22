---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Grouping and Pivoting
related:
  - GROUPBY
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - aggregation
  - images
---

# GROUPBY Image Guide

Images planned for [GROUPBY](../../Functions/Lookup%20%26%20Reference/GROUPBY.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: GROUPBY Argument Layout

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated worksheet screenshot. |
| Content | The timesheet in `A1:C7` with the Team column outlined as row_fields, the Hours column outlined as values, and the grouped output to the right with three rows (Ava, Ben and Cy). Labels under the output name the subtotal and total settings. |
| Alt Text | A timesheet and a grouped summary with the row fields and values columns outlined and labeled. |
| File Name | GROUPBY Argument Layout.png |

## Image 2: Story Problem Grouped Output

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the deal list and the grouped output side by side. |
| Content | The deal list `A1:B6` on the left with the Priya and Sam rows shaded. On the right, the output Lee 1, Priya 2 and Sam 2, with the formula shown above the output. |
| Alt Text | A deal list with rep names and a grouped output that counts two deals each for Priya and Sam and one for Lee. |
| File Name | GROUPBY Deal Counts Result.png |

## Image 3: Sorted Summary With Grand Total

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Screenshot of the output range. |
| Content | The output of `=GROUPBY(A2:A7, C2:C7, SUM, 0, 1, -2)` with Cy 20, Ava 17 and Ben 12 in rows, and a bold total row of 49 at the bottom. A callout points to the sort order argument. |
| Alt Text | A grouped summary sorted by hours from largest to smallest, with a total row of 49. |
| File Name | GROUPBY Sorted Total.png |
