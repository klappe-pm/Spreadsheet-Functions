---
domain: Spreadsheet Functions
category: Logical
subcategory: Conditional Tests
related:
  - SWITCH
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - logical
---

# SWITCH Image Guide

Images planned for [SWITCH](../../Functions/Logical/SWITCH.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=SWITCH(expression, value1, result1, [value2, result2], ..., [default])` with each part labeled: expression, the value and result pairs, and the optional default at the end. An arrow marks the default as the last argument. |
| Alt Text | A SWITCH formula with the expression, value and result pairs, and the optional default labeled. |
| File Name | SWITCH Syntax Anatomy.png |

## Image 2: Nested IF Versus SWITCH

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 2. |
| Format | Two formulas stacked in a worksheet formula bar or code panel. |
| Content | Top: the nested IF formula with the three IF levels and their closing parentheses highlighted. Bottom: the SWITCH version with each value and result pair on its own line. Both return `Green` for the cell value `G`, shown in a result cell beside each formula. |
| Alt Text | A nested IF formula and an equivalent SWITCH formula, both returning Green. |
| File Name | SWITCH Nested IF Versus Switch.png |

## Image 3: Discount Tiers Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of a worksheet. |
| Content | The membership table in columns A to C with column D holding the discount formula. The discount values 30, 15, 4.5, 0 and 8 are visible in column D, and the total 57.5 is shown in a labeled cell below the column. |
| Alt Text | A membership worksheet where SWITCH assigns each discount by level and the discounts total 57.5. |
| File Name | SWITCH Discount Tiers Worksheet.png |
