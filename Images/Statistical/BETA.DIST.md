---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
related:
  - BETA.DIST
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# BETA.DIST Image Guide

Images planned for [BETA.DIST](../../Functions/Statistical/BETA.DIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of the formula bar. |
| Content | The formula `=BETA.DIST(x, alpha, beta, cumulative, [A], [B])` with the four required arguments in one color and the optional bounds A and B in a second color, with notes that cumulative TRUE gives a probability and FALSE gives a density. |
| Alt Text | A labeled BETA.DIST formula with four required arguments and two optional bound arguments. |
| File Name | BETA.DIST Syntax Anatomy.png |

## Image 2: Default and Custom Bounds

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two panel diagram with curves. |
| Content | Left panel: a beta density curve on the interval 0 to 1 with the point 0.5 marked and the cumulative area below it shaded. Right panel: the same curve on the interval 1 to 5 with the point 3 marked at the same relative position. A caption notes that both give 0.6875. |
| Alt Text | Two beta curves, one on 0 to 1 and one on 1 to 5, with the marked point at the same relative position and the same probability. |
| File Name | BETA.DIST Default and Custom Bounds.png |

## Image 3: Results Panel for the Conversion Problem

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Worksheet screenshot. |
| Content | The input table in `A1:B4` with alpha, beta and the threshold rate visible, the formula `=BETA.DIST(B4, B2, B3, TRUE)` in a labeled cell, and the result 0.3446 highlighted. |
| Alt Text | An input table with alpha 2, beta 5 and threshold 0.2, and a BETA.DIST result of 0.3446 highlighted. |
| File Name | BETA.DIST Conversion Results.png |
