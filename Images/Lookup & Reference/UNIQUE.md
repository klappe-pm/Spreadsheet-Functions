---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Dynamic Arrays
related:
  - UNIQUE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - lookup-reference
---

# UNIQUE Image Guide

Images planned for [UNIQUE](../../Functions/Lookup%20%26%20Reference/UNIQUE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: UNIQUE Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a formula bar. |
| Content | The formula `=UNIQUE(array, [by_col], [exactly_once])` with each argument labeled. Beneath by_col, a note reads FALSE compares rows, TRUE compares columns. Beneath exactly_once, a note reads TRUE returns only values that occur once. |
| Alt Text | The UNIQUE formula with its array, by_col and exactly_once arguments labeled. |
| File Name | UNIQUE Arguments.png |

## Image 2: Exactly Once Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, before Problem 1. |
| Format | Two worksheet screenshots side by side. |
| Content | Left: the two code lists in `A2:A6` and `B2:B6`, with the codes that appear in both lists shaded grey. Right: the spilled result of `=UNIQUE(VSTACK(A2:A6, B2:B6), , TRUE)` showing SKU-10, SKU-13, SKU-15 and SKU-16. |
| Alt Text | Two code lists with shared codes shaded, beside the four codes that appear in only one list. |
| File Name | UNIQUE Exactly Once Result.png |
