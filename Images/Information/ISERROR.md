---
domain: Spreadsheet Functions
category: Information
subcategory: Error Checks
related:
  - ISERROR
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISERROR Image Guide

Images planned for [ISERROR](../../Functions/Information/ISERROR.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=ISERROR(value)` with `value` labeled as the formula or cell to test, and two outcome boxes: TRUE for any error, including `#N/A`, and FALSE for numbers, text and blank cells. |
| Alt Text | An ISERROR formula with its value argument labeled and the TRUE and FALSE outcomes shown. |
| File Name | ISERROR Syntax Anatomy.png |

## Image 2: Lookup Fallback Result

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 5. |
| Format | Screenshot of a small worksheet with a price list and two lookup formulas. |
| Content | A price list in D2:E4 with codes 101, 102 and 103. Two formula cells beside it: one for code 105 showing "Not found" and one for code 102 showing 3.25. The "Not found" cell is highlighted. |
| Alt Text | A worksheet where a lookup for a missing code shows Not found and a lookup for an existing code shows its price. |
| File Name | ISERROR Lookup Fallback Result.png |
