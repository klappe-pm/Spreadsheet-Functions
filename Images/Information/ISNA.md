---
domain: Spreadsheet Functions
category: Information
subcategory: Error Checks
related:
  - ISNA
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISNA Image Guide

Images planned for [ISNA](../../Functions/Information/ISNA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=ISNA(value)` with `ISNA` labeled as the function name, `value` labeled as the value to test, and a caption that reads "TRUE only for the #N/A error". |
| Alt Text | A formula diagram showing ISNA with one value argument and a TRUE or FALSE result. |
| File Name | ISNA Syntax Anatomy.png |

## Image 2: Vendor Quote Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the quote table with error cells highlighted. |
| Content | The item and price table in `A1:B5`, with the Paper and Markers rows showing `#N/A` in the price column and highlighted. The formula `=SUMPRODUCT(ISNA(B2:B5)*1)` sits beside the table with the result 2. |
| Alt Text | A vendor quote table with two #N/A prices highlighted and a count of 2 for missing quotes. |
| File Name | ISNA Vendor Quote Results.png |
