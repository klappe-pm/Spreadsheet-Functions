---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
related:
  - ISFORMULA
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISFORMULA Image Guide

Images planned for [ISFORMULA](../../Functions/Information/ISFORMULA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=ISFORMULA(reference)` with `ISFORMULA` labeled as the function name, `reference` labeled as a cell, name or formula to test, and a caption that reads "TRUE when the cell holds a formula". |
| Alt Text | A formula diagram showing ISFORMULA with one reference argument and a TRUE or FALSE result. |
| File Name | ISFORMULA Syntax Anatomy.png |

## Image 2: Formula Audit Column

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Screenshot of a worksheet with an audit column beside a calculation column. |
| Content | Column B holds a mix of formulas and typed numbers. Column C holds `=IF(ISFORMULA(B2),"Formula","Typed value")` filled down. Typed-value rows are highlighted in a warning color. |
| Alt Text | A worksheet audit column labeling each cell as Formula or Typed value, with typed rows highlighted. |
| File Name | ISFORMULA Formula Audit Column.png |
