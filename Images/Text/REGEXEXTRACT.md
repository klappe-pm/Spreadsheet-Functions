---
domain: Spreadsheet Functions
category: Text
subcategory: Regular Expressions
related:
  - REGEXEXTRACT
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - text
  - images
---

# REGEXEXTRACT Image Guide

Images planned for [REGEXEXTRACT](../../Functions/Text/REGEXEXTRACT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: REGEXEXTRACT Arguments by Platform

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the two syntax code blocks. |
| Format | Two-column comparison diagram. |
| Content | Left column labeled Microsoft Excel shows `=REGEXEXTRACT(text, pattern, [return_mode], [case_sensitivity])` with the optional arguments in brackets. Right column labeled Google Sheets shows `=REGEXEXTRACT(text, regular_expression)`. A note under the Sheets column says case-insensitive matching uses `(?i)`. |
| Alt Text | Side by side comparison of the REGEXEXTRACT syntax in Excel and Google Sheets. |
| File Name | REGEXEXTRACT Arguments by Platform.png |

## Image 2: Return Modes Compared

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 3 result. |
| Format | Worksheet screenshot with three result columns. |
| Content | Source text `red 12, blue 7, green 30` in A2. Column B shows return mode 0 with the single result `12`. Column C shows return mode 1 with the results `12`, `7` and `30` in separate rows. A caption explains that return mode 1 returns every match. |
| Alt Text | Worksheet with a source text and three REGEXEXTRACT results showing the first match and all matches. |
| File Name | REGEXEXTRACT Return Modes.png |
