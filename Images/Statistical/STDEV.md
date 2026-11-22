---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - STDEV
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - compatibility
  - images
---

# STDEV Image Guide

Images planned for [STDEV](../../Functions/Statistical/STDEV.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Number Arguments for STDEV

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=STDEV(number1, [number2], ...)` with `number1` marked required and `[number2]` marked optional. A small tag labeled legacy sits beside the function name. |
| Alt Text | A STDEV formula with the first number argument marked required, the optional arguments marked and a legacy tag beside the name. |
| File Name | STDEV Syntax Arguments.png |

## Image 2: Legacy Function Matches Its Replacement

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a worksheet with two formula cells. |
| Content | The data `A2:A7` with `=STDEV(A2:A7)` showing `1.8708` and `=STDEV.S(A2:A7)` showing `1.8708` in adjacent cells. A third cell shows `=STDEV(A2:A7)-STDEV.S(A2:A7)` with the result `0`. |
| Alt Text | Two standard deviation results for the same data that match, and a difference cell showing zero. |
| File Name | STDEV Versus STDEV.S.png |

## Image 3: Story Problem Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the pump run hour table with the result visible. |
| Content | The four run hour values in `B2:B5` and the cell showing `0.6455` for `=STDEV(B2:B5)` in a labeled output cell, with a note beside it that reads use STDEV.S in future revisions. |
| Alt Text | A table of four pump run hours with a STDEV result of 0.6455. |
| File Name | STDEV Pump Hours Result.png |
