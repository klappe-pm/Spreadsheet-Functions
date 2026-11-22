---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
related:
  - STDEV.S
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - spread
---

# STDEV.S Image Guide

Images planned for [STDEV.S](../../Functions/Statistical/STDEV.S.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Number Arguments for STDEV.S

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=STDEV.S(number1, [number2], ...)` with `number1` marked required and `[number2]` marked optional. A small label under the formula reads "sample of the population". |
| Alt Text | A STDEV.S formula with the first number argument marked required and the optional arguments marked. |
| File Name | STDEV.S Syntax Arguments.png |

## Image 2: Sample Versus Population Spread

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Side by side screenshot of two result cells. |
| Content | The data `A2:A7` with two formula cells below it: `=STDEV.S(A2:A7)` showing `1.8708` and `=STDEV.P(A2:A7)` showing `1.7078`. A bracket between the two results is labeled sample versus population. |
| Alt Text | Two standard deviation results for the same six values, one labeled sample and one labeled population. |
| File Name | STDEV.S Sample Versus Population.png |

## Image 3: Story Problem Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the bottle volume table with the result visible. |
| Content | The five bottle volumes in `B2:B6` and the cell showing `2.7019` for `=STDEV.S(B2:B6)` in a labeled output cell. |
| Alt Text | A table of five bottle fill volumes with a STDEV.S result of 2.7019. |
| File Name | STDEV.S Bottle Volumes Result.png |
