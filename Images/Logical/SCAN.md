---
domain: Spreadsheet Functions
category: Logical
subcategory: Lambda Helpers
related:
  - SCAN
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - logical
  - images
---

# SCAN Image Guide

Images planned for [SCAN](../../Functions/Logical/SCAN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated formula bar screenshot. |
| Content | The formula `=SCAN([initial_value], array, LAMBDA(accumulator, value, calculation))`. The initial value is labeled as the starting point and the LAMBDA parameters are labeled as the running result and the current item. |
| Alt Text | A formula bar showing SCAN with its initial value, array and LAMBDA labeled. |
| File Name | SCAN Syntax Anatomy.png |

## Image 2: Running Steps Versus Final Total

| Item | Instruction |
| --- | --- |
| Placement | Examples section, before Example 3. |
| Format | Two columns side by side. |
| Content | Left: the input values 5, 3, 8 and 2 with a running total column showing 5, 8, 16 and 18. Right: the same input with a single SUM result of 18 in a labeled cell, with a note that the last running value equals the total. |
| Alt Text | Two panels, one showing a running total column and one showing a single total with the same final value. |
| File Name | SCAN Running Steps Versus Final Total.png |

## Image 3: Running Balance Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a small worksheet. |
| Content | The transaction list in column B with the amounts 300, -450, -200 and 150, and the running balances 1500, 1050, 850 and 1000 spilled beside them. The final balance 1000 is highlighted. |
| Alt Text | A transaction list with a running balance column ending at 1000 and the final balance highlighted. |
| File Name | SCAN Running Balance Worksheet.png |
