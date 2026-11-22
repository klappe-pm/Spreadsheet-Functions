---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
related:
  - BINOM.INV
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# BINOM.INV Image Guide

Images planned for [BINOM.INV](../../Functions/Statistical/BINOM.INV.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of a formula. |
| Content | The formula `=BINOM.INV(trials, probability_s, alpha)` with each argument in its own box. Each box carries a caption with its valid range: trials of 0 or more, probability_s strictly between 0 and 1, alpha strictly between 0 and 1. |
| Alt Text | A labeled BINOM.INV formula with three required arguments and the valid range of each. |
| File Name | BINOM.INV Syntax Anatomy.png |

## Image 2: Coverage Steps

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Step chart of the cumulative binomial distribution. |
| Content | A step line for 30 trials at a 25 percent chance, from 0 to 20 successes. A dashed horizontal line marks the 0.9 target. The step at 11 is circled and labeled 11, with the cumulative value 0.9493 beside it. The step at 10 is labeled 0.8943 to show that it falls short. |
| Alt Text | A cumulative step chart crossing a 0.9 target at 11 successes. |
| File Name | BINOM.INV Coverage Steps.png |

## Image 3: Problem Two Threshold

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Annotated line chart. |
| Content | Cumulative probability for 200 tickets at a 2 percent no-show chance, for counts from 0 to 12. A dashed line marks the 0.95 confidence level. The first point at or above the line is circled and labeled 7. |
| Alt Text | A cumulative probability curve for ticket no-shows crossing a 95 percent confidence line at 7. |
| File Name | BINOM.INV Ticket No-Show Threshold.png |
