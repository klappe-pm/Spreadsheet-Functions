---
domain: Spreadsheet Functions
category: Text
subcategory: Text Generation
related:
  - COPILOT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - copilot
  - images
  - retired
---

# COPILOT Image Guide

Images planned for [COPILOT](../../Functions/Text/COPILOT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Retired Formula Warning

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet cell showing the error. |
| Content | A cell containing `=COPILOT("Summarize these comments in one sentence", B2:B50)` with the error `#NAME?` displayed in the cell. A callout reads "Retired September 14, 2026". |
| Alt Text | A worksheet cell with a COPILOT formula that now shows the #NAME? error. |
| File Name | COPILOT Retired Formula Warning.png |

## Image 2: Find Retired Formulas

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 3 and Example 4. |
| Format | Screenshot of the Find and Replace dialog. |
| Content | The Find and Replace dialog with COPILOT in the Find what box and Look in set to Formulas, with the matching cells listed below. |
| Alt Text | The Find and Replace dialog set to search formulas for COPILOT. |
| File Name | COPILOT Find Retired Formulas.png |

## Image 3: Rebuilding Retired Summary Cells

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the summary sheet with error cells highlighted. |
| Content | The Report Line and Summary table, with the North and East cells showing `#NAME?` highlighted, the formula `=SUMPRODUCT(--ISERROR(B2:B5))` in a labeled cell, and the result 2 beside it. |
| Alt Text | A summary sheet with two error cells highlighted and a formula counting them. |
| File Name | COPILOT Rebuilding Summary Cells.png |
