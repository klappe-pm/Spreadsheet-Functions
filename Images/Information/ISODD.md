---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
related:
  - ISODD
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISODD Image Guide

Images planned for [ISODD](../../Functions/Information/ISODD.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=ISODD(value)` with `ISODD` labeled as the function name, `value` labeled as the number or cell reference to test, and a caption that reads "TRUE when the value is an odd integer". |
| Alt Text | A formula diagram showing ISODD with one value argument and a TRUE result for an odd integer. |
| File Name | ISODD Syntax Anatomy.png |

## Image 2: Two Crew Pattern

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Screenshot of a worksheet column with a second column of results. |
| Content | Column A holds job names in rows 2 to 7 and column B holds `=IF(ISODD(ROW(A2)),"Crew 1","Crew 2")` filled down. Crew 1 and Crew 2 alternate, with the Crew 1 rows shaded. |
| Alt Text | A worksheet with six jobs assigned alternately to Crew 1 and Crew 2. |
| File Name | ISODD Two Crew Pattern.png |

## Image 3: Odd Floor Rent Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the rent table with matching rows highlighted. |
| Content | The floor and rent table in `A1:B7`, with floors 3, 5 and 11 highlighted, the formula `=SUMPRODUCT(ISODD(A2:A7)*B2:B7)` in a labeled cell, and the result 6150 beside it. |
| Alt Text | A rent table with odd-numbered floors highlighted and a total of 6150 for those floors. |
| File Name | ISODD Odd Floor Rent Result.png |
