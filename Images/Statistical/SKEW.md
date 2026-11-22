---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
related:
  - SKEW
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# SKEW Image Guide

Images planned for [SKEW](../../Functions/Statistical/SKEW.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Skewness Syntax and Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=SKEW(number1, [number2], ...)` with `number1` underlined as required and `[number2]` shaded as optional. A callout points to a range such as `A1:A8` as one valid argument. |
| Alt Text | A SKEW formula with the first argument marked required and the second marked optional. |
| File Name | SKEW Syntax Arguments.png |

## Image 2: Reading the Sign of the Result

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Simple number line diagram. |
| Content | A horizontal axis marked negative, zero and positive. Three markers: a negative value with a long left tail, zero with a symmetric curve, and a positive value with a long right tail. Caption each marker with its tail direction. |
| Alt Text | A number line showing that negative skewness has a left tail, zero is symmetric and positive skewness has a right tail. |
| File Name | SKEW Sign Reading.png |

## Image 3: Story Problem Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the score list with the formula result visible. |
| Content | The score list in `B2:B11` with the cell showing `-0.2475` for `=SKEW(B2:B11)` in a labeled output cell. Highlight the two lowest scores (62 and 71) to show the low-side tail. |
| Alt Text | A quiz score list with the two lowest scores highlighted and a SKEW result of negative 0.2475. |
| File Name | SKEW Quiz Scores Result.png |
