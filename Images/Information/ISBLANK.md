---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
related:
  - ISBLANK
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISBLANK Image Guide

Images planned for [ISBLANK](../../Functions/Information/ISBLANK.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=ISBLANK(value)` with `value` labeled as the cell to test, and two outcome boxes: TRUE for an empty cell and FALSE for any cell with content. |
| Alt Text | An ISBLANK formula with its value argument labeled and the TRUE and FALSE outcomes shown. |
| File Name | ISBLANK Syntax Anatomy.png |

## Image 2: Blank Versus Empty Text

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a small worksheet with three cells in a column. |
| Content | Three cells: one truly empty, one with the formula `=""` that looks empty, and one with a single typed space. Each has an ISBLANK formula beside it showing TRUE, FALSE and FALSE. The first cell is outlined to show it is the only true blank. |
| Alt Text | A worksheet showing that a truly empty cell returns TRUE from ISBLANK while cells with empty text or a space return FALSE. |
| File Name | ISBLANK Blank Versus Empty Text.png |
