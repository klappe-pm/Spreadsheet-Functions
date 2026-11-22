---
domain: Spreadsheet Functions
category: Statistical
subcategory: Spread and Variance
related:
  - STDEVA
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - logical-values
---

# STDEVA Image Guide

Images planned for [STDEVA](../../Functions/Statistical/STDEVA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Value Arguments for STDEVA

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=STDEVA(value1, [value2], ...)` with `value1` marked required and `[value2]` marked optional. Callouts show that the arguments can be typed values, such as TRUE and "n/a", or ranges. |
| Alt Text | A STDEVA formula with the first value argument marked required and the optional arguments marked. |
| File Name | STDEVA Value Arguments.png |

## Image 2: Typed Entries Versus Range Entries

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two column diagram with a conversion table. |
| Content | Left column: typed entries TRUE, FALSE and "n/a" with arrows to their values 1, 0 and 0. Right column: a range holding the numbers 4, 8 and 6 plus the text n/a, with the text cell crossed out as ignored. A caption reads "typed text counts as 0; range text is ignored". |
| Alt Text | A diagram showing that typed TRUE counts as 1 and typed text counts as 0, while text inside a range is ignored. |
| File Name | STDEVA Typed Versus Range.png |

## Image 3: Story Problem Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the survey score table with the result visible. |
| Content | The scores in `B2:B6` with the `n/a` cell in row 4 shaded and marked as ignored, and the cell showing `1.7078` for `=STDEVA(B2:B6)` in a labeled output cell. |
| Alt Text | A survey score table with the text entry shaded as ignored and a STDEVA result of 1.7078. |
| File Name | STDEVA Survey Result.png |
