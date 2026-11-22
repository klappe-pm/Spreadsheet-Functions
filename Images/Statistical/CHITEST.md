---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - CHITEST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# CHITEST Image Guide

Images planned for [CHITEST](../../Functions/Statistical/CHITEST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Legacy Test Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of two worksheet tables with a compatibility label. |
| Content | The observed table in `A2:B3` outlined and labeled actual_range and the expected table in `A6:B7` outlined and labeled expected_range. A small tag near the formula bar reads Compatibility function, with a note that CHISQ.TEST is the recommended name. |
| Alt Text | Two worksheet tables labeled as the arguments of CHITEST, with a note that the function is a compatibility function. |
| File Name | CHITEST Legacy Test Arguments.png |

## Image 2: Migration Check

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of one worksheet with two formulas side by side. |
| Content | A cell with `=CHISQ.TEST(A2:B3, A6:B7)` and a cell with `=CHITEST(A2:B3, A6:B7)`, both showing the same probability, and a third cell with the difference formula showing 0. |
| Alt Text | Two formulas, CHISQ.TEST and CHITEST, returning the same probability for the same ranges, with their difference equal to 0. |
| File Name | CHITEST Migration Check.png |
