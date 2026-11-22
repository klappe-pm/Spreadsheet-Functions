---
domain: Spreadsheet Functions
category: Text
subcategory: Text Joining and Splitting
related:
  - TEXTJOIN
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - text
---

# TEXTJOIN Image Guide

Images planned for [TEXTJOIN](../../Functions/Text/TEXTJOIN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=TEXTJOIN(delimiter, ignore_empty, text1, [text2], ...)` with the delimiter, the TRUE or FALSE flag and the range argument labeled. |
| Alt Text | A formula bar showing a TEXTJOIN formula with each argument labeled. |
| File Name | TEXTJOIN Syntax Anatomy.png |

## Image 2: Ignore Empty Versus Keep Empty

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 6. |
| Format | Two side-by-side worksheet screenshots of the team roster. |
| Content | The roster in A2:A6 with one blank name. Left: the TRUE result, Ana, Ben, Cy, Dee, captioned ignore_empty TRUE. Right: the FALSE result, Ana, Ben, double comma gap, Cy, Dee, captioned ignore_empty FALSE. |
| Alt Text | Two results of the same TEXTJOIN formula, one with the blank name skipped and one with an empty item between delimiters. |
| File Name | TEXTJOIN Ignore Empty Comparison.png |

## Image 3: Filtered Names in One Line

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Worksheet screenshot of the attendance list. |
| Content | The student list with the two absent rows (Jack and Leo) highlighted, the formula in a helper cell and the joined result Jack and Leo in an output cell. |
| Alt Text | An attendance list with the two absent students highlighted and a joined result of their names. |
| File Name | TEXTJOIN Absent Students Result.png |
