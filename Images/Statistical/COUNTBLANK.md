---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
related:
  - COUNTBLANK
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# COUNTBLANK Image Guide

Images planned for [COUNTBLANK](../../Functions/Statistical/COUNTBLANK.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Blank and Filled Cells in a Range

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of one worksheet column. |
| Content | Ten cells in column A with names in some rows and blanks in others. Blank cells are outlined in orange and labeled counted. Filled cells are outlined in gray and labeled skipped. A result cell shows 4. |
| Alt Text | A worksheet column with blank cells outlined and labeled as counted by COUNTBLANK and filled cells outlined as skipped, with a result of 4. |
| File Name | COUNTBLANK Blank and Filled Cells.png |

## Image 2: Formula Blanks Counted

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a worksheet with a formula and a callout. |
| Content | Cell `A2` selected, with the formula bar showing `=IF(FALSE, "Yes", "")` and the cell displaying nothing. A callout reads "Empty string counts as blank in Excel and Sheets." Cell `A3` is truly empty, and the result cell shows 2. |
| Alt Text | A worksheet cell that returns an empty string and is counted as blank, with a callout stating that Excel and Google Sheets both count it. |
| File Name | COUNTBLANK Formula Blanks Counted.png |
