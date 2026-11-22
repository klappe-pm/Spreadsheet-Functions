---
domain: Spreadsheet Functions
category: Logical
subcategory: Conditional Tests
related:
  - IFS
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - logical
  - images
---

# IFS Image Guide

Images planned for [IFS](../../Functions/Logical/IFS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated formula bar screenshot. |
| Content | The formula `=IFS(logical_test1, value_if_true1, ...)` with each test in one color and each result in another. Labels show that the pairs repeat and that the last pair is the optional TRUE default. |
| Alt Text | A formula bar showing an IFS formula with condition and result pairs colored and labeled. |
| File Name | IFS Syntax Anatomy.png |

## Image 2: Nested IF Versus IFS Layout

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Two stacked formula boxes with a bracket count on the left. |
| Content | The nested IF formula with its closing parentheses highlighted, above the IFS formula with one pair per line. Caption: same result, fewer parentheses. |
| Alt Text | Two formulas side by side, a nested IF with many closing parentheses and an IFS formula that lists each condition and result in order. |
| File Name | IFS Nested IF Versus IFS.png |

## Image 3: Stock Status Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of a small worksheet. |
| Content | Items in column A and stock counts in column B, with the reorder point in cell E1 labeled. Rows with stock at or below 20 are highlighted. The COUNTIF result 3 appears in a labeled output cell. |
| Alt Text | A stock list with three rows at or below the reorder point highlighted and a count of 3. |
| File Name | IFS Stock Status Worksheet.png |
