---
domain: Spreadsheet Functions
category: Statistical
subcategory: Hypothesis Tests
related:
  - T.TEST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# T.TEST Image Guide

Images planned for [T.TEST](../../Functions/Statistical/T.TEST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Two Sample Ranges and the Test Options

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of two worksheet columns. |
| Content | Column B labeled before and column C labeled after, each outlined in a different color and labeled array1 and array2. Callouts beside the formula bar point to the tails argument with the values 1 or 2 and to the type argument with the values 1, 2 and 3. |
| Alt Text | Two worksheet columns labeled as the two arrays of a T.TEST formula, with callouts for the tails and type arguments. |
| File Name | T.TEST Arguments.png |

## Image 2: Paired Versus Two-Sample Layouts

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 2 result. |
| Format | Side by side diagram of two data layouts. |
| Content | Left: paired layout with before and after values on the same row for each patient, captioned type 1 paired, same rows. Right: two independent columns of different lengths, captioned type 2 or 3, independent samples. |
| Alt Text | Two data layouts, one with paired rows for each patient and one with two independent columns. |
| File Name | T.TEST Paired Versus Two Sample.png |

## Image 3: Two Sample Result Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the two plant columns with the formula bar visible. |
| Content | Plant A in column A with six values, plant B in column B with seven values, the formula `=T.TEST(A2:A7, B2:B8, 2, 2)` in the formula bar, and the output cell showing 0.000432. |
| Alt Text | Two columns of fill times with a T.TEST formula using type 2 and a p-value of 0.000432. |
| File Name | T.TEST Two Plant Result.png |
