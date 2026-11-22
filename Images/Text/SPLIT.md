---
domain: Spreadsheet Functions
category: Text
subcategory: Text Joining and Splitting
related:
  - SPLIT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - text
---

# SPLIT Image Guide

Images planned for [SPLIT](../../Functions/Text/SPLIT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Delimiter Splitting Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula with four arguments. |
| Content | The formula `=SPLIT(text, delimiter, [split_by_each], [remove_empty_text])`. Below it, the sample text `North,South,East` with the comma delimiters marked in orange. Optional arguments are outlined with dashed lines and labeled with their defaults, TRUE. |
| Alt Text | A SPLIT formula with its four arguments labeled and a sample comma-separated text with its delimiters marked. |
| File Name | SPLIT Argument Anatomy.png |

## Image 2: Split Result Across Columns

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a worksheet row. |
| Content | One row of cells showing `Oak Hill` and `Pine Ridge` in two adjacent cells, with the formula in the first cell. The formula `=SPLIT("Oak Hill; Pine Ridge", "; ", FALSE)` is shown in the formula bar. |
| Alt Text | A worksheet row where a SPLIT formula fills two adjacent cells with the parts of a phrase. |
| File Name | SPLIT Result Across Columns.png |

## Image 3: Speaker List Split Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of a worksheet with the source and the spilled result. |
| Content | Column A holds `Ruiz / Kim Lee / Osei`. The result row shows `Ruiz`, `Kim Lee` and `Osei` in three cells. The second cell is highlighted to show that the space inside the name is kept. |
| Alt Text | A speaker list split into three names, with the two-word name kept whole in the second cell. |
| File Name | SPLIT Speaker List Result.png |
