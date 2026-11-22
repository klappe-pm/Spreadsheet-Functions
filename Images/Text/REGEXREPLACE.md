---
domain: Spreadsheet Functions
category: Text
subcategory: Regular Expressions
related:
  - REGEXREPLACE
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - text
  - images
---

# REGEXREPLACE Image Guide

Images planned for [REGEXREPLACE](../../Functions/Text/REGEXREPLACE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: REGEXREPLACE Arguments by Platform

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the two syntax code blocks. |
| Format | Two-column comparison diagram. |
| Content | Left column labeled Microsoft Excel shows `=REGEXREPLACE(text, pattern, replacement, [occurrence], [case_sensitivity])` with the optional arguments in brackets. Right column labeled Google Sheets shows `=REGEXREPLACE(text, regular_expression, replacement)`. A note under the Sheets column says it replaces every match and that case-insensitive matching uses `(?i)`. |
| Alt Text | Side by side comparison of the REGEXREPLACE syntax in Excel and Google Sheets. |
| File Name | REGEXREPLACE Arguments by Platform.png |

## Image 2: Removing Non-Digits Before and After

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 1 result. |
| Format | Worksheet screenshot with input and output columns. |
| Content | Column A holds `(555) 123-4567`. Column B holds the formula `=REGEXREPLACE(A2, "\D", "")` and the result `5551234567`. The brackets, space and hyphen in column A are struck through to show that they are removed. |
| Alt Text | Worksheet with a formatted phone number, the REGEXREPLACE formula and the digits-only result. |
| File Name | REGEXREPLACE Removing Non-Digits.png |
