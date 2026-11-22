---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - STDEVP
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - compatibility
  - images
---

# STDEVP Image Guide

Images planned for [STDEVP](../../Functions/Statistical/STDEVP.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Number Arguments for STDEVP

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=STDEVP(number1, [number2], ...)` with `number1` marked required and `[number2]` marked optional. A label under the formula reads "whole group" and a small tag reads legacy. |
| Alt Text | A STDEVP formula with the first number argument marked required, the optional arguments marked and a legacy tag beside the name. |
| File Name | STDEVP Syntax Arguments.png |

## Image 2: Legacy Function Matches Its Replacement

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a worksheet with three formula cells. |
| Content | The data `A2:A5` with `=STDEVP(A2:A5)` showing `1.4790`, `=STDEV.P(A2:A5)` showing `1.4790` in an adjacent cell, and a difference cell with `=STDEVP(A2:A5)-STDEV.P(A2:A5)` showing `0`. |
| Alt Text | Two population standard deviation results for the same data that match, and a difference cell showing zero. |
| File Name | STDEVP Versus STDEV.P.png |

## Image 3: Story Problem Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the station defect table with the result visible. |
| Content | The five station counts in `B2:B6` with the highest count 15 marked, and the cell showing `2.2804` for `=STDEVP(B2:B6)` in a labeled output cell. |
| Alt Text | A table of five station defect counts with the highest count marked and a STDEVP result of 2.2804. |
| File Name | STDEVP Station Defects Result.png |
