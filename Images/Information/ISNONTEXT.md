---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
related:
  - ISNONTEXT
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISNONTEXT Image Guide

Images planned for [ISNONTEXT](../../Functions/Information/ISNONTEXT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=ISNONTEXT(value)` with `ISNONTEXT` labeled as the function name, `value` labeled as the value to test, and a caption that reads "TRUE for anything that is not text". |
| Alt Text | A formula diagram showing ISNONTEXT with one value argument and a TRUE or FALSE result. |
| File Name | ISNONTEXT Syntax Anatomy.png |

## Image 2: Product Codes Check

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the product code column with a check column beside it. |
| Content | Column A holds the codes 00417, 417, B22, 1080 and 2210. Column B holds `=IF(ISNONTEXT(A2),"Convert to text","OK")` filled down. The rows for 417 and 1080 are highlighted. |
| Alt Text | A product code column in which the two numeric codes are flagged Convert to text. |
| File Name | ISNONTEXT Product Codes Check.png |
