---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
related:
  - EXPON.DIST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - distribution
  - images
  - statistical
---

# EXPON.DIST Image Guide

Images planned for [EXPON.DIST](../../Functions/Statistical/EXPON.DIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: EXPON.DIST Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a formula bar. |
| Content | The formula `=EXPON.DIST(x, lambda, cumulative)` with each argument in its own color. Captions read "time, 0 or more", "rate, above 0" and "TRUE for probability, FALSE for density". |
| Alt Text | An EXPON.DIST formula with x, lambda and cumulative arguments highlighted and labeled. |
| File Name | EXPON.DIST Syntax Anatomy.png |

## Image 2: Cumulative Probability Between Two Times

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Exponential curve with a shaded band. |
| Content | A decreasing exponential density curve for lambda 0.25 with the area between 2 and 4 minutes shaded. The labels show the cumulative values 0.3935 at 2 minutes and 0.6321 at 4 minutes, and the shaded area is labeled 0.2387. |
| Alt Text | An exponential curve for rate 0.25 with the area between 2 and 4 minutes shaded and labeled 0.2387. |
| File Name | EXPON.DIST Probability Between Two Times.png |

## Image 3: Call Arrival Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Cumulative curve with a marker. |
| Content | A cumulative curve for lambda 0.25 with a vertical marker at 3 minutes. The point on the curve is labeled 0.5276. The formula `=EXPON.DIST(3, 0.25, TRUE)` sits beside the chart. |
| Alt Text | A cumulative exponential curve with a marker at 3 minutes showing a probability of 0.5276. |
| File Name | EXPON.DIST Call Arrival Result.png |
