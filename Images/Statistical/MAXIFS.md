---
domain: Spreadsheet Functions
category: Statistical
subcategory: Conditional Extremes
related:
  - MAXIFS
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# MAXIFS Image Guide

Images planned for [MAXIFS](../../Functions/Statistical/MAXIFS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Max Range and Criteria Pairs

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Diagram of a formula with labeled arguments. |
| Content | The formula `=MAXIFS(max_range, criteria_range1, criterion1, ...)` with `max_range` outlined in one color and each criteria range and criterion pair outlined in a second color. A caption explains that every pair must match for a row to count. |
| Alt Text | Diagram of a MAXIFS formula with the max range and criteria pairs labeled and outlined. |
| File Name | MAXIFS Argument Layout.png |

## Image 2: Two Conditions Filtering Rows

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Screenshot of the sales list with rows highlighted. |
| Content | The sales list `A1:C8` with the East and Gadgets rows (640 and 1010) highlighted. The formula `=MAXIFS(C2:C8, A2:A8, "East", B2:B8, "Gadgets")` sits in a labeled output cell showing 1010. |
| Alt Text | A sales list with the two East Gadgets rows highlighted and a MAXIFS result of 1010. |
| File Name | MAXIFS Two Conditions.png |

## Image 3: Story Problem Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the ticket table with the result cell. |
| Content | The ticket table `A1:C7` with the High priority rows highlighted and T3 (67) emphasized. The formula `=MAXIFS(C2:C7, B2:B7, "High")` is in a labeled output cell showing 67. |
| Alt Text | A ticket table with the High priority rows highlighted and a MAXIFS result of 67. |
| File Name | MAXIFS High Priority Wait Result.png |
