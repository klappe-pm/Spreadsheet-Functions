---
domain: Spreadsheet Functions
category: Statistical
subcategory: Averages
related:
  - AVERAGEIFS
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# AVERAGEIFS Image Guide

Images planned for [AVERAGEIFS](../../Functions/Statistical/AVERAGEIFS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of the formula bar. |
| Content | The formula `=AVERAGEIFS(average_range, criteria_range1, criterion1, [criteria_range2, criterion2], ...)` with the average range labeled first, then each range and criterion pair in a different color, and a note that every range matches the size of the average range. |
| Alt Text | A labeled AVERAGEIFS formula with the average range followed by repeating range and criterion pairs. |
| File Name | AVERAGEIFS Syntax Anatomy.png |

## Image 2: Every Condition Must Hold

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Worksheet screenshot with two highlight colors. |
| Content | The department and shift table with the Billing day rows shaded in one color and the Night rows shaded in a second color. The single row that satisfies both Night and greater than 30 is outlined, with the result 35 shown. |
| Alt Text | A department and shift table where one row meets both the night shift and the greater than 30 conditions, giving an average of 35. |
| File Name | AVERAGEIFS Every Condition.png |

## Image 3: Results Panel for the Commute Problem

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Worksheet screenshot. |
| Content | The trip table in `A1:C7` with the three Line 4 peak trips highlighted, the formula `=AVERAGEIFS(C2:C7, A2:A7, "Line 4", B2:B7, "Yes")` in a labeled cell, and the result 35 shown. |
| Alt Text | A trip table with three qualifying Line 4 peak trips highlighted and an AVERAGEIFS result of 35. |
| File Name | AVERAGEIFS Commute Results.png |
