---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
related:
  - ADDRESS
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - lookup-reference
---

# ADDRESS Image Guide

Images planned for [ADDRESS](../../Functions/Lookup%20%26%20Reference/ADDRESS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Address Argument Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of one formula. |
| Content | The formula `=ADDRESS(4, 3, 2)` with each argument in its own colored box. Beneath each box, a caption gives its meaning: row_num is row 4, column_num is column 3, abs_num 2 is absolute row and relative column. A small table on the right lists the four abs_num values. |
| Alt Text | A labeled ADDRESS formula with row, column and reference type arguments identified. |
| File Name | ADDRESS Argument Anatomy.png |

## Image 2: Reference Style Grid

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Four-row comparison grid. |
| Content | Four rows for abs_num 1, 2, 3 and 4, each showing the same cell C4 as text (`$C$4`, `C$4`, `$C4`, `C4`). A final row shows the R1C1 output `R4C3` for the a1 argument set to FALSE. Each row has a plain-language label. |
| Alt Text | A grid comparing four absolute and relative address forms and the R1C1 form of cell C4. |
| File Name | ADDRESS Reference Style Grid.png |

## Image 3: Peak Lookup Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the formula result highlighted. |
| Content | The month and sales table in `A1:B6` with the April row highlighted. The formula bar shows the ADDRESS and MATCH formula in a cell beside the table, and that cell displays `$B$5`. |
| Alt Text | A monthly sales table with the highest value highlighted and an ADDRESS formula returning $B$5. |
| File Name | ADDRESS Peak Lookup Result.png |
