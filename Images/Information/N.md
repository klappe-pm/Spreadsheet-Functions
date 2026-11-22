---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
related:
  - N
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - information
  - images
---

# N Image Guide

Images planned for [N](../../Functions/Information/N.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula. |
| Content | The formula `=N(value)` with `N` labeled as the function, and `value` labeled as the single argument that accepts a number, date, logical value, text or error. Beneath it, a short list of the four outputs: number returns itself, TRUE returns 1, FALSE returns 0, text returns 0. |
| Alt Text | Diagram of the N formula with its single value argument and the four kinds of result. |
| File Name | N Syntax Anatomy.png |

## Image 2: TRUE and FALSE Converted to 1 and 0

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a small worksheet. |
| Content | Cells A4 (TRUE) and A5 (FALSE) with the formula `=N(A4)+N(A5)` in a third cell showing 1. The two logical cells are outlined and the result cell is highlighted. |
| Alt Text | A worksheet where TRUE and FALSE cells are converted with N and summed to 1. |
| File Name | N True False Conversion.png |

## Image 3: Surcharge Table Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the order table. |
| Content | The table with Order, Base Fee, Express and a new Total column. The Express TRUE rows show 17 and 23, and the FALSE row shows 12. The formula `=B2+N(C2)*5` appears in the formula bar. |
| Alt Text | An order table where express orders show a 5 surcharge added through N and non-express orders keep their base fee. |
| File Name | N Shipping Surcharge Result.png |
