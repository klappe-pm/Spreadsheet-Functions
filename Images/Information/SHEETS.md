---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
related:
  - SHEETS
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - information
  - images
---

# SHEETS Image Guide

Images planned for [SHEETS](../../Functions/Information/SHEETS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula. |
| Content | The formula `=SHEETS([reference])` with `SHEETS` labeled as the function and `reference` labeled as optional. A note beneath explains that a 3D reference such as `Jan:Mar!B2` spans several tabs, and that omitting the argument counts the whole workbook. |
| Alt Text | Diagram of the SHEETS formula with its optional reference argument and a note on 3D references. |
| File Name | SHEETS Syntax Anatomy.png |

## Image 2: Sheets Counted in a 3D Reference

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 5. |
| Format | Screenshot of the tab bar with the name manager. |
| Content | The tab bar with Index, Jan, Feb, Mar, Apr, May, Jun and Notes. A bracket spans the Jan, Feb and Mar tabs, labeled Q1_Span with the name `=Jan:Mar!$B$2`. The formula `=SHEETS(Q1_Span)` shows the result 3. |
| Alt Text | A tab bar with a bracket over three tabs labeled as a named 3D reference, and a SHEETS formula that returns 3. |
| File Name | SHEETS 3D Reference Count.png |
