---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
related:
  - VALUETOTEXT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# VALUETOTEXT Image Guide

Images planned for [VALUETOTEXT](../../Functions/Text/VALUETOTEXT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Concise and Strict Output

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | Column A holds the values TRUE, 1500, Hello and 0.25. Column B holds the formula `=VALUETOTEXT(A2,0)` filled down, with its text results. A caption labels column B as text output. |
| Alt Text | A worksheet with mixed values in one column and their text versions in the next column. |
| File Name | VALUETOTEXT Concise Output.png |

## Image 2: Concise Versus Strict Output

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly after Example 4. |
| Format | Comparison table drawn as a two-row diagram. |
| Content | Three columns: the input, the concise result with format `0`, and the strict result with format `1`. Rows show `Hello` as `Hello` and `"Hello"`, and `42` as `42` in both columns. |
| Alt Text | A comparison of concise and strict output for a text value and a number. |
| File Name | VALUETOTEXT Concise Strict Comparison.png |
