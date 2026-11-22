---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
related:
  - UNICHAR
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - text
---

# UNICHAR Image Guide

Images planned for [UNICHAR](../../Functions/Text/UNICHAR.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=UNICHAR(number)` with `number` labeled as the Unicode code point. A small table beside it lists 36 as $, 8364 as euro and 10003 as a check mark. |
| Alt Text | A formula bar showing =UNICHAR(number) with a small table of code points and their symbols. |
| File Name | UNICHAR Syntax Anatomy.png |

## Image 2: Symbols in a Label

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Worksheet screenshot with three columns. |
| Content | Column A holds the code points 36, 163 and 165, column B holds the amounts, and column C shows the labels $45.00, £80.00 and ¥9,000.00. The formula UNICHAR(A2)&TEXT(B2,"#,##0.00") is shown in the formula bar. |
| Alt Text | A worksheet with code points, amounts and labels that start with a currency symbol. |
| File Name | UNICHAR Symbols In Label.png |
