---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
related:
  - BETA.INV
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# BETA.INV Image Guide

Images planned for [BETA.INV](../../Functions/Statistical/BETA.INV.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of the formula bar. |
| Content | The formula `=BETA.INV(probability, alpha, beta, [A], [B])` with the probability, alpha and beta arguments required, and A and B marked optional with the defaults 0 and 1 noted. |
| Alt Text | A labeled BETA.INV formula with three required arguments and two optional bounds. |
| File Name | BETA.INV Syntax Anatomy.png |

## Image 2: Probability to Value Mapping

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Cumulative curve diagram. |
| Content | An S-shaped cumulative curve for alpha 2 and beta 2 on the interval 0 to 1. A horizontal arrow at probability 0.5 meets the curve, and a vertical arrow drops to the value 0.5 on the horizontal axis, labeled median. |
| Alt Text | A cumulative beta curve with arrows showing that probability 0.5 maps to the value 0.5. |
| File Name | BETA.INV Probability to Value.png |

## Image 3: Results Panel for the Completion Problem

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Worksheet screenshot. |
| Content | The input table in `A1:B4` with probability 0.5, alpha 2 and beta 2 visible, the formula `=BETA.INV(B2, B3, B4, 0, 100)` in a labeled cell, and the result 50 highlighted. |
| Alt Text | An input table with probability 0.5 and shape parameters 2 and 2, and a BETA.INV result of 50 highlighted. |
| File Name | BETA.INV Completion Results.png |
