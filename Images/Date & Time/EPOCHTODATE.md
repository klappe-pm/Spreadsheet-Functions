---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Construction
related:
  - EPOCHTODATE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - date-time
  - images
---

# EPOCHTODATE Image Guide

Images planned for [EPOCHTODATE](../../Functions/Date%20%26%20Time/EPOCHTODATE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Timestamp Units

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram with a number scale. |
| Content | A horizontal scale with three markers for the same moment: `1700000000` labeled seconds (unit 1, default), `1700000000000` labeled milliseconds (unit 2), and `1700000000000000` labeled microseconds (unit 3). A note under the scale reads "all three give 11/14/2023 22:13:20 UTC." |
| Alt Text | A scale showing one moment written in seconds, milliseconds and microseconds, with the matching unit numbers. |
| File Name | EPOCHTODATE Timestamp Units.png |

## Image 2: Same Moment in Three Units

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Three-row table with the formula and the result in each row. |
| Content | Rows for Example 1 (seconds), Example 2 (milliseconds) and Example 3 (microseconds). Each row shows the formula, the timestamp, and the result `11/14/2023 22:13:20`. A column labeled "Unit" is highlighted. |
| Alt Text | A table with three EPOCHTODATE formulas, each returning the same UTC date and time from a different unit. |
| File Name | EPOCHTODATE Same Moment Units.png |
