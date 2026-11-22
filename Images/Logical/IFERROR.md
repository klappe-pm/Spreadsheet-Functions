---
domain: Spreadsheet Functions
category: Logical
subcategory: Error Handling
related:
  - IFERROR
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - logical
  - images
---

# IFERROR Image Guide

Images planned for [IFERROR](../../Functions/Logical/IFERROR.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=IFERROR(value, value_if_error)` with value boxed and labeled Formula to check, and value_if_error boxed and labeled Returned only when an error occurs. Arrows show the two possible outputs: the result itself and the fallback. |
| Alt Text | A formula with IFERROR, its two arguments labeled, and arrows showing the two possible outputs. |
| File Name | IFERROR Syntax Anatomy.png |

## Image 2: Replacement Versus Original Result

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 5. |
| Format | Side by side screenshot of two small tables. |
| Content | Left table: a lookup with a match, showing the returned value unchanged. Right table: a lookup with no match, showing the replacement text Not Found. The error cell is labeled #N/A before the replacement. |
| Alt Text | Two small worksheet examples showing a matched lookup returning its value and an unmatched lookup returning the replacement text. |
| File Name | IFERROR Replacement Result.png |

## Image 3: Order Totals Panel

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the order sheet with the price list beside it. |
| Content | The order table with the calculated column showing 50, 50, 0, and 40. Row O3 is highlighted and labeled as the missing SKU. The total of 140 is shown below the column. |
| Alt Text | An order sheet where the missing SKU row shows 0 and the total is 140. |
| File Name | IFERROR Order Totals.png |
