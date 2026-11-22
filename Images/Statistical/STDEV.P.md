---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
related:
  - STDEV.P
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - spread
---

# STDEV.P Image Guide

Images planned for [STDEV.P](../../Functions/Statistical/STDEV.P.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Population Arguments for STDEV.P

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=STDEV.P(number1, [number2], ...)` with `number1` marked required and `[number2]` marked optional. A small label under the formula reads "whole group, not a sample". |
| Alt Text | A STDEV.P formula with the first number argument marked required and the optional arguments marked. |
| File Name | STDEV.P Syntax Arguments.png |

## Image 2: Population Variance Versus Standard Deviation

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Side by side screenshot of two result cells. |
| Content | The data `A2:A7` with `=STDEV.P(A2:A7)` showing `1.7078` and `=STDEV.P(A2:A7)^2` showing `2.9167` in labeled cells. An arrow labeled square root links the two results. |
| Alt Text | Two results for the same six values: a standard deviation of 1.7078 and a variance of 2.9167. |
| File Name | STDEV.P Variance Versus Deviation.png |

## Image 3: Story Problem Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the shift output table with the result visible. |
| Content | The six shift totals in `B2:B7` with the highest value 46 and the lowest value 38 marked, and the cell showing `2.8087` for `=STDEV.P(B2:B7)` in a labeled output cell. |
| Alt Text | A table of six shift output totals with the highest and lowest shifts marked and a STDEV.P result of 2.8087. |
| File Name | STDEV.P Shift Output Result.png |
