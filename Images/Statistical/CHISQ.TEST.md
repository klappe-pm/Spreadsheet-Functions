---
domain: Spreadsheet Functions
category: Statistical
subcategory: Hypothesis Tests
related:
  - CHISQ.TEST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# CHISQ.TEST Image Guide

Images planned for [CHISQ.TEST](../../Functions/Statistical/CHISQ.TEST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Observed and Expected Tables

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of two small worksheet tables side by side. |
| Content | The observed table in `A2:B3` outlined in one color and labeled actual_range, and the expected table in `A6:B7` outlined in a second color and labeled expected_range. Both tables have the same shape. A note states that both ranges must hold the same number of cells. |
| Alt Text | Two two-by-two worksheet tables, one observed and one expected, outlined and labeled as the two CHISQ.TEST arguments. |
| File Name | CHISQ.TEST Observed and Expected Tables.png |

## Image 2: Expected Counts From Row and Column Totals

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Screenshot of a worksheet with totals added around the observed table. |
| Content | Row totals in column C and column totals in row 4 of the observed table, the grand total in C4, and the formula `=SUM($A2:$B2)*SUM(A$2:A$3)/SUM($A$2:$B$3)` in cell A6. Arrows show that the expected value in each cell comes from its row total and column total divided by the grand total. |
| Alt Text | A worksheet showing row totals, column totals and the grand total used to build the expected counts for a chi-squared test. |
| File Name | CHISQ.TEST Expected Counts From Totals.png |
