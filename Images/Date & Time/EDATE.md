---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Date Arithmetic
related:
  - EDATE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - date-time
  - images
---

# EDATE Image Guide

Images planned for [EDATE](../../Functions/Date%20%26%20Time/EDATE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Start Date Plus Months

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of the formula. |
| Content | The formula `=EDATE(start_date, months)` with start_date in one box and months in another. An arrow runs from the start date to a calendar cell showing the result, with the label "same day, months later." |
| Alt Text | A diagram of EDATE with a start date and a months value producing a date with the same day number. |
| File Name | EDATE Start Date Plus Months.png |

## Image 2: Month-End Clamp

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Two-row calendar strip. |
| Content | Top row: January 2026 with January 31 circled and labeled "start." Bottom row: February 2026 with February 28 circled and labeled "EDATE result: last day of the shorter month." A small note beside the bottom row reads "DATE would give March 3 instead." |
| Alt Text | Calendar rows for January and February 2026, showing EDATE returning February 28 from January 31, with the DATE alternative noted. |
| File Name | EDATE Month End Clamp.png |
