---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Construction
related:
  - DATE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - date-time
  - images
---

# DATE Image Guide

Images planned for [DATE](../../Functions/Date%20%26%20Time/DATE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Year, Month and Day Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Diagram with three labeled boxes feeding into one date. |
| Content | Three boxes labeled year, month and day, each holding a sample value (2026, 1, 10). An arrow runs from the boxes to a calendar cell showing 1/10/2026. Under the year box, a note reads "1900 to 9999 used as entered." |
| Alt Text | A diagram showing year, month and day values combined by DATE into one calendar date. |
| File Name | DATE Year Month Day Arguments.png |

## Image 2: Month Overflow Table

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Small annotated table. |
| Content | Three rows: DATE(2026, 13, 1) gives 1/1/2027, DATE(2026, 14, 2) gives 2/2/2027, and DATE(2026, 7, 0) gives 6/30/2026. A column of the month values is highlighted to show the overflow. |
| Alt Text | A table of DATE formulas with out-of-range month or day inputs and the dates they return. |
| File Name | DATE Month Overflow Table.png |
