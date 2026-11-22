---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
related:
  - IMPORTTEXT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - text-file
---

# IMPORTTEXT Image Guide

Images planned for [IMPORTTEXT](../../Functions/Web/IMPORTTEXT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Delimiter and Row Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula with its arguments in order. |
| Content | The formula `=IMPORTTEXT(path, [delimiter], [skip_rows], [take_rows], [encoding], [locale])` with each argument in its own box, the delimiter box showing a pipe, and a note that an empty argument keeps its default. |
| Alt Text | A diagram of the IMPORTTEXT arguments in order with the delimiter argument highlighted. |
| File Name | IMPORTTEXT Delimiter and Row Arguments.png |

## Image 2: Pipe Delimiter Applied to Columns

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 4 and Example 5. |
| Format | Side by side comparison of the source text and the imported grid. |
| Content | Left: the four lines of `stock.txt` with the pipe characters visible. Right: the same data in three columns with the header row SKU, Qty and Bin, and the Qty column outlined. |
| Alt Text | Pipe-separated text on the left and the same data split into three columns on the right. |
| File Name | IMPORTTEXT Pipe Delimiter.png |

## Image 3: Count File Imported With a Title Row

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the imported grid with the title row marked as skipped. |
| Content | A text view of `cycle.txt` with the title line struck through and labeled skipped by skip_rows, the imported grid beside it, and the Units column with the zero value in C2 highlighted. |
| Alt Text | A cycle count file with its title line skipped and the zero-unit bin highlighted. |
| File Name | IMPORTTEXT Cycle Count Title Row.png |
