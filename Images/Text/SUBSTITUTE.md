---
domain: Spreadsheet Functions
category: Text
subcategory: Text Cleaning
related:
  - SUBSTITUTE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - text
---

# SUBSTITUTE Image Guide

Images planned for [SUBSTITUTE](../../Functions/Text/SUBSTITUTE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Old Text and New Text Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula with four arguments. |
| Content | The formula `=SUBSTITUTE(text, old_text, new_text, [instance_num])`. The text argument is shaded blue, old_text orange, new_text green and instance_num outlined with a dashed line. A small example reads `Q1 sales` with `Q1` marked as old_text and `Q2` as new_text. |
| Alt Text | A SUBSTITUTE formula with its four arguments labeled and a short example that swaps one word. |
| File Name | SUBSTITUTE Argument Anatomy.png |

## Image 2: Occurrence Selection Example

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, before the first problem heading. |
| Format | Two-row diagram of one text string and two results. |
| Content | The text `Q1 sales, Q1 returns` with both occurrences of Q1 outlined. Row A: no instance_num, both replaced, giving `Q2 sales, Q2 returns`. Row B: instance_num 2, only the second replaced, giving `Q1 sales, Q2 returns`. |
| Alt Text | Two results of SUBSTITUTE on the same text, one replacing every occurrence and one replacing only the second. |
| File Name | SUBSTITUTE Occurrence Selection.png |

## Image 3: Single Occurrence Replacement Result

| Item | Instruction |
| --- | --- |
| Placement | Use Cases section, above the Account Code Cleanup example. |
| Format | Screenshot of a worksheet with the source and result columns. |
| Content | Column A holds `Q1 sales, Q1 returns`. Column B holds the SUBSTITUTE formula with instance_num 2 and the result `Q1 sales, Q2 returns`. The changed letters are highlighted in column B. |
| Alt Text | A report note in one column and the note with only its second quarter label changed in the next column. |
| File Name | SUBSTITUTE Single Occurrence Result.png |
