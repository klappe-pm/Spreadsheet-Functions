---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
related:
  - ISNUMBER
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISNUMBER Image Guide

Images planned for [ISNUMBER](../../Functions/Information/ISNUMBER.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=ISNUMBER(value)` with `ISNUMBER` labeled as the function name, `value` labeled as the value to test, and a caption that reads "TRUE for numbers, dates and times". |
| Alt Text | A formula diagram showing ISNUMBER with one value argument and a TRUE or FALSE result. |
| File Name | ISNUMBER Syntax Anatomy.png |

## Image 2: Invoice Total Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the invoice table with the total cell labeled. |
| Content | The invoice table in `A1:B7` with the amount column showing 120, pending, 85, 240, 60 and void. The two status rows are shaded grey, and the formula `=SUMPRODUCT(ISNUMBER(B2:B7)*1,B2:B7)` sits beside the table with the result 505. |
| Alt Text | An invoice table with two status words shaded and a total of 505 for the numeric amounts. |
| File Name | ISNUMBER Invoice Total Result.png |
