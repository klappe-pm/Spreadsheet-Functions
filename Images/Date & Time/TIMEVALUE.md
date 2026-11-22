---
domain: Spreadsheet Functions
category: Date & Time
subcategory: Time Values
related:
  - TIMEVALUE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - date-time
  - images
---

# TIMEVALUE Image Guide

Images planned for [TIMEVALUE](../../Functions/Date%20%26%20Time/TIMEVALUE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated worksheet screenshot. |
| Content | A cell holding the text "2:15 PM" with a visible left alignment, the formula `=TIMEVALUE("2:15 PM")` in the formula bar, and the result 0.59375 in the adjacent cell. The time_text argument is outlined and labeled. |
| Alt Text | A worksheet with the TIMEVALUE formula converting the text 2:15 PM to 0.59375. |
| File Name | TIMEVALUE Syntax Anatomy.png |

## Image 2: Accepted Time Text Formats

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Three-row table diagram. |
| Content | Columns for input text, format type and result. Rows: "2:15 PM" (12-hour), "18:45" (24-hour) and "22-Aug-2011 6:35 AM" (date ignored, time only), with the results 0.59375, 0.78125 and 0.274306. |
| Alt Text | A table of three accepted time text formats with their converted results. |
| File Name | TIMEVALUE Accepted Time Text Formats.png |
