---
category: Text
subcategory: Text Cleaning
related:
  - CLEAN
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - data-cleaning
  - images
  - text-cleaning
---

# CLEAN Image Guide

Images planned for [CLEAN](../../Functions/Text/CLEAN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Hidden Characters in Imported Text

| Item | Instruction |
| --- | --- |
| Placement | Description section, after the third paragraph. |
| Format | Annotated worksheet screenshot. |
| Content | A cell with a visible word, the same cell with a hidden tab marked by a callout, and the cell after CLEAN with the tab gone. Callouts label the control characters. |
| Alt Text | A worksheet cell before and after CLEAN removes a hidden tab character. |
| File Name | CLEAN Hidden Characters.png |

## Image 2: Text Before and After Cleaning

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Two-column comparison table in a worksheet screenshot. |
| Content | Column A with the raw values and column B with the formula `=TRIM(CLEAN(A2))` and its results. Rows show the tab case, the line feed case and a clean value that does not change. |
| Alt Text | A two-column comparison of raw and cleaned text values. |
| File Name | CLEAN Before After.png |
