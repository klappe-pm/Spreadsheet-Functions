---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Dynamic Arrays
related:
  - FILTER
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - dynamic-array
  - images
---

# FILTER Image Guide

Images planned for [FILTER](../../Functions/Lookup%20%26%20Reference/FILTER.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: FILTER Arguments Diagram

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated worksheet screenshot. |
| Content | The inventory list in `A1:D7` with the array argument `A2:D7` outlined in blue, the include argument `D2:D7>=100` outlined in orange, and the spilled result to the right. Labels under each argument name it. |
| Alt Text | A worksheet with FILTER arguments outlined and labeled, and the spilled result of two rows. |
| File Name | FILTER Arguments Diagram.png |

## Image 2: AND and OR Logic With Include Arrays

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 5. |
| Format | Two side-by-side diagrams of the same small table. |
| Content | Left: the include arrays for `(B2:B7="Facilities")*(C2:C7="Active")` shown as a column of 1s and 0s, captioned AND, with only Whiteboard shaded. Right: the include array for `(B2:B7="Support")+(D2:D7>=150)`, captioned OR, with Office Chair, Headset and Keyboard shaded. |
| Alt Text | Two include arrays showing that multiplication returns rows meeting both conditions and addition returns rows meeting either condition. |
| File Name | FILTER And Or Logic.png |

## Image 3: Overdue Library Fines Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the fines table with matching rows highlighted. |
| Content | The table `A1:C6` with Night Harbor, Iron Garden and Quiet Hours highlighted, the formula `=SUM(FILTER(C2:C6, B2:B6>7))` in the formula bar, and the result 8.50 in a labeled output cell. |
| Alt Text | A library fines table with three books more than 7 days late highlighted and a total of 8.50. |
| File Name | FILTER Overdue Fines Result.png |
