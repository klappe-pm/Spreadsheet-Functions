---
domain: Spreadsheet Functions
category: Add-in & Automation
subcategory: Add-in Functions
related:
  - CALL
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - add-in
  - automation
  - images
---

# CALL Image Guide

Images planned for [CALL](../../Functions/Add-in%20%26%20Automation/CALL.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Two Forms of CALL

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the second syntax code block. |
| Format | Two annotated worksheet cells side by side. |
| Content | Left: `=CALL(A5)` with `A5` labeled register_id. Right: a full `=CALL(module_text, procedure, type_text)` formula with each argument labeled and the type_text argument marked as the return type code. |
| Alt Text | Two CALL formulas, one using a register ID and one naming the DLL, procedure and type text. |
| File Name | CALL Two Forms.png |

## Image 2: Register and Call Steps

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 1 result. |
| Format | Screenshot of two cells in a worksheet. |
| Content | `A5` holding the REGISTER.ID formula and a second cell holding `=CALL(A5)`, with an arrow from `A5` to the second cell. |
| Alt Text | A register ID in one cell passed to a CALL formula in another cell. |
| File Name | CALL Register And Call.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the kiosk log with the largest value highlighted. |
| Content | The kiosk table in `A1:B4` with the 16200000 row highlighted, the formula `=MAX(B2:B4)/60000` in the formula bar, and the result 270 in a labeled output cell. |
| Alt Text | A kiosk uptime table with the longest uptime highlighted and a result of 270 minutes. |
| File Name | CALL Kiosk Uptime Result.png |
