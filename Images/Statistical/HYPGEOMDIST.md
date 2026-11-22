---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - HYPGEOMDIST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# HYPGEOMDIST Image Guide

Images planned for [HYPGEOMDIST](../../Functions/Statistical/HYPGEOMDIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of the formula. |
| Content | The formula `=HYPGEOMDIST(sample_s, number_sample, population_s, number_pop)` with callouts that sample_s and population_s count successes and number_sample and number_pop count items. A note states that this Excel version takes four arguments. |
| Alt Text | A labeled HYPGEOMDIST formula showing its four arguments. |
| File Name | HYPGEOMDIST Syntax Anatomy.png |

## Image 2: Successes in a Sample Without Replacement

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Worksheet screenshot of the committee table. |
| Content | The Problem 1 table with total staff 12, managers 4 and committee size 5 in B2 to B4, plus the formula `=HYPGEOMDIST(2, B4, B3, B2)` in the formula bar and the result 0.4242 in the output cell. |
| Alt Text | A worksheet with a committee table and a HYPGEOMDIST formula returning 0.4242. |
| File Name | HYPGEOMDIST Committee Worksheet.png |
