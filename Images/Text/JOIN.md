---
domain: Spreadsheet Functions
category: Text
subcategory: Text Joining and Splitting
related:
  - JOIN
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# JOIN Image Guide

Images planned for [JOIN](../../Functions/Text/JOIN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: JOIN Arguments and Output

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a formula and its output. |
| Content | The formula `=JOIN(", ", "red", "blue", "green")` in a formula bar. Callouts label `delimiter`, `value_or_array1` and `value_or_array2, ...`. A cell below shows the output `red, blue, green`. |
| Alt Text | A JOIN formula with the delimiter and value arguments labeled and the joined text shown in the result cell. |
| File Name | JOIN Arguments Output.png |

## Image 2: Tags Joined Into One Cell

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a vertical list and a result cell. |
| Content | Cells A2 to A4 hold red, blue and green in a column. Cell B2 holds `=JOIN(", ", A2:A4)` and displays "red, blue, green". Arrows connect the three source cells to the result cell. |
| Alt Text | A column of three tags joined into one cell with commas between them. |
| File Name | JOIN Tags Joined.png |
