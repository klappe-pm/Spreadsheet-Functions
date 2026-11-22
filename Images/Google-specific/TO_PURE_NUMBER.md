---
category: Google-specific
subcategory: Parser Functions
related:
  - TO_PURE_NUMBER
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - sheets
---

# TO_PURE_NUMBER Image Guide

Images planned for [TO_PURE_NUMBER](../../Functions/Google-specific/TO_PURE_NUMBER.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Formatted Display Versus Pure Number

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Three stacked worksheet cells. |
| Content | The value `$1,250.00` in a currency-formatted cell, the value `50%` in a percent-formatted cell, and the result of `=TO_PURE_NUMBER(A2)` showing `1250` with a label that reads formatting removed. |
| Alt Text | A currency-formatted value and the plain number 1250 that TO_PURE_NUMBER returns for it. |
| File Name | TO_PURE_NUMBER Formatted Versus Pure.png |

## Image 2: Date Cells and Their Serial Numbers

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Table of three cells with their displayed and returned values. |
| Content | Columns labeled Cell Display, Formula and Result. Rows show `1/1/2025` with `=TO_PURE_NUMBER(B2)` giving `45658`, and `12:00 PM` with `=TO_PURE_NUMBER(C2)` giving `0.5`. |
| Alt Text | A table of date and time cells and the plain numbers TO_PURE_NUMBER returns for them. |
| File Name | TO_PURE_NUMBER Date and Time Serials.png |

## Image 3: Days Between Two Formatted Dates

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the project milestone row. |
| Content | The start date `1/1/2025` in `B2`, the due date `3/15/2025` in `C2`, and the result `73` in `D2` with the formula bar showing the two TO_PURE_NUMBER calls subtracted. |
| Alt Text | A project milestone row with a start date, a due date and a day count of 73 calculated from the two plain serial numbers. |
| File Name | TO_PURE_NUMBER Days Between Dates.png |
