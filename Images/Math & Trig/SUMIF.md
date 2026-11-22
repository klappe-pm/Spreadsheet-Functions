---
domain: Spreadsheet Functions
category: Math & Trig
subcategory: Conditional Sums
related:
  - SUMIF
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - math-trig
---

# SUMIF Image Guide

Images planned for [SUMIF](../../Functions/Math%20%26%20Trig/SUMIF.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula. |
| Content | The formula `=SUMIF(range, criteria, [sum_range])` with range labeled "cells tested", criteria labeled "condition", and sum_range labeled "cells added when the test passes". An arrow shows that sum_range is matched by position. |
| Alt Text | Diagram of the SUMIF formula showing the tested range, the condition and the optional sum range. |
| File Name | SUMIF Syntax Anatomy.png |

## Image 2: Criteria Patterns

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of the bakery list with four result cells. |
| Content | The product and revenue list in A2:B7, with result cells showing 670 for "Croissant", 760 for ">200", 1060 for "<>Muffin" and 670 for "Crois*". Each criterion has a short label beside its result. |
| Alt Text | A bakery list with four SUMIF results using an exact match, a comparison, a not-equal test and a wildcard. |
| File Name | SUMIF Criteria Patterns.png |

## Image 3: Client Name Wildcard

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 table. |
| Format | Screenshot of the invoice list with matching rows shaded. |
| Content | The client list with Harbor Co and Pine Co shaded, the formula `=SUMIF(A2:A6, "*Co", B2:B6)` and the result 2225 in a labeled cell. |
| Alt Text | An invoice list with two clients ending in Co shaded and a SUMIF total of 2225. |
| File Name | SUMIF Client Wildcard.png |
