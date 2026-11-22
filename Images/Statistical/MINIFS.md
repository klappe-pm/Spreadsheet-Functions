---
domain: Spreadsheet Functions
category: Statistical
subcategory: Conditional Extremes
related:
  - MINIFS
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# MINIFS Image Guide

Images planned for [MINIFS](../../Functions/Statistical/MINIFS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Min Range and Criteria Pairs

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Diagram of a formula with labeled arguments. |
| Content | The formula `=MINIFS(min_range, criteria_range1, criterion1, ...)` with `min_range` outlined in one color and each criteria range and criterion pair outlined in a second color. A caption explains that every pair must match for a row to count. |
| Alt Text | Diagram of a MINIFS formula with the min range and criteria pairs labeled and outlined. |
| File Name | MINIFS Argument Layout.png |

## Image 2: Two Conditions Filtering Rows

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Screenshot of the sales list with rows highlighted. |
| Content | The sales list `A1:C8` with the East and Gadgets rows (640 and 1010) highlighted and 640 emphasized. The formula `=MINIFS(C2:C8, A2:A8, "East", B2:B8, "Gadgets")` sits in a labeled output cell showing 640. |
| Alt Text | A sales list with the two East Gadgets rows highlighted and a MINIFS result of 640. |
| File Name | MINIFS Two Conditions.png |

## Image 3: Story Problem Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the shipment table with the result cell. |
| Content | The shipment table `A1:C6` with the Express rows highlighted and S1 (2 days) emphasized. The formula `=MINIFS(C2:C6, B2:B6, "Express")` is in a labeled output cell showing 2. |
| Alt Text | A shipment table with the Express rows highlighted and a MINIFS result of 2 days. |
| File Name | MINIFS Express Lead Time Result.png |
