---
domain: Spreadsheet Functions
category: Logical
subcategory: Lambda Helpers
related:
  - REDUCE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - logical
  - images
---

# REDUCE Image Guide

Images planned for [REDUCE](../../Functions/Logical/REDUCE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated formula bar screenshot. |
| Content | The formula `=REDUCE([initial_value], array, LAMBDA(accumulator, value, calculation))`. The initial value is marked optional in Excel and the accumulator and value names are labeled inside the LAMBDA. |
| Alt Text | A formula bar showing REDUCE with the initial value, the array and the LAMBDA labeled. |
| File Name | REDUCE Syntax Anatomy.png |

## Image 2: Accumulator Steps for REDUCE

| Item | Instruction |
| --- | --- |
| Placement | Examples section, before Example 3. |
| Format | Horizontal step diagram. |
| Content | Start at the initial value 1, then boxes for each step: 1 times 3 gives 3, 3 times 2 gives 6, 6 times 4 gives 24. Each box feeds the next as the accumulator. |
| Alt Text | A chain of three multiplication steps leading from an initial value of 1 to a final value of 24. |
| File Name | REDUCE Accumulator Steps.png |

## Image 3: Growth Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a small worksheet. |
| Content | Month and growth factor columns with factors 1.02, 1.05 and 0.98. The starting balance 1000 and the final result 1049.58 appear in labeled cells, with the REDUCE formula shown above the result. |
| Alt Text | A table of three growth factors and a final balance of 1049.58 from a starting balance of 1000. |
| File Name | REDUCE Growth Worksheet.png |
