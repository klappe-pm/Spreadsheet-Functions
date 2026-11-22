---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Construction
related:
  - DATEVALUE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - date-time
  - images
---

# DATEVALUE Image Guide

Images planned for [DATEVALUE](../../Functions/Date%20%26%20Time/DATEVALUE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Text Date Becomes a Serial Number

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two-cell before and after diagram. |
| Content | Left: a cell showing `4/18/2026` left-aligned, the typical look of text. Right: the same cell after `=DATEVALUE(A2)` is entered and the cell is formatted as a date, showing `4/18/2026` right-aligned with the serial number 46130 in a tooltip. An arrow labeled DATEVALUE connects the two. |
| Alt Text | Two cells before and after DATEVALUE: text left-aligned, then a real date right-aligned with serial 46130. |
| File Name | DATEVALUE Text To Serial.png |

## Image 2: Text Layouts Accepted by DATEVALUE

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Table with a screenshot of each result. |
| Content | Three rows: `"4/18/2026"` returns the date, `"2026/02/23"` returns the date, and `"7/4/2026 18:30"` returns the date with the time dropped. A column marked "Time ignored" is highlighted on the third row. |
| Alt Text | A table showing three text date layouts converted by DATEVALUE, with the time portion of the third entry dropped. |
| File Name | DATEVALUE Accepted Layouts.png |
