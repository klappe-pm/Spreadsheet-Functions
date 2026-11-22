---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Arithmetic
related:
  - EOMONTH
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - date-time
  - images
---

# EOMONTH Image Guide

Images planned for [EOMONTH](../../Functions/Date%20%26%20Time/EOMONTH.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Start Date and Month Offset

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of the formula. |
| Content | The formula `=EOMONTH(start_date, months)` with start_date and months in separate boxes. An arrow from the start date moves forward by the months value to a calendar cell that shows the last day of the target month, labeled "last day of month." |
| Alt Text | A diagram of EOMONTH with a start date and a months value returning the last day of the target month. |
| File Name | EOMONTH Start Date And Months.png |

## Image 2: Month-End Schedule

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Three-row table with calendar thumbnails. |
| Content | Three rows showing an input date and its month end: November 22, 2026 gives January 31, 2027 at a two-month offset; March 15, 2028 gives February 29, 2028 at a minus-one offset; and the first day of the next month, December 1, 2026, from the add-1 pattern. Leap-year row is highlighted. |
| Alt Text | A table of three EOMONTH examples with the resulting month-end dates, including the leap day February 29, 2028. |
| File Name | EOMONTH Month End Schedule.png |
