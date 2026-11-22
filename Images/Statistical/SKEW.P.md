---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
related:
  - SKEW.P
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# SKEW.P Image Guide

Images planned for [SKEW.P](../../Functions/Statistical/SKEW.P.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Population Skewness Syntax

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=SKEW.P(number1, [number2], ...)` with `number1` marked required and `[number2]` marked optional. A bracket under the first argument reads "complete group, not a sample". |
| Alt Text | A SKEW.P formula with the first argument marked required and the optional arguments marked. |
| File Name | SKEW.P Syntax Arguments.png |

## Image 2: Population Versus Sample Comparison

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Side by side screenshot of two result cells. |
| Content | The data `A1:A8` with two formula cells below it: `=SKEW.P(A1:A8)` showing `0.65625` and `=SKEW(A1:A8)` showing `0.8185`. Labels read Population and Sample. |
| Alt Text | Two skewness results for the same data, one labeled population and one labeled sample. |
| File Name | SKEW P Versus SKEW.png |

## Image 3: Story Problem Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the weekly order table with the result visible. |
| Content | The daily order table in `B2:B8` with the Sunday value of 31 highlighted, and the cell showing `1.6930` for `=SKEW.P(B2:B8)` in a labeled output cell. |
| Alt Text | A weekly order table with the Sunday peak highlighted and a SKEW.P result of 1.6930. |
| File Name | SKEW P Weekly Orders Result.png |
