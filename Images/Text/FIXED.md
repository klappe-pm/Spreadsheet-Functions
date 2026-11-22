---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
related:
  - FIXED
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# FIXED Image Guide

Images planned for [FIXED](../../Functions/Text/FIXED.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: FIXED Arguments and Output

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | Cell A2 holds 1234.567 and cell B2 holds `=FIXED(A2, 1)` showing "1,234.6". Callouts label the `number`, `decimals` and `no_commas` arguments in the formula bar. A third callout notes that the result is text, aligned left. |
| Alt Text | A worksheet showing FIXED converting 1234.567 to the text 1,234.6 with arguments labeled. |
| File Name | FIXED Arguments Output.png |

## Image 2: Sales Sentence Built With FIXED

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a sentence result. |
| Content | Cell A2 holds 48213.456. Cell B2 holds the formula `="Total sales were "&FIXED(A2, 0)&" units."` and displays "Total sales were 48,213 units." The formula bar is visible above the cell. |
| Alt Text | A worksheet where FIXED rounds 48213.456 to 48,213 inside a sentence. |
| File Name | FIXED Sales Sentence.png |
