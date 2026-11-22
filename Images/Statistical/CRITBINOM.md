---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - CRITBINOM
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - compatibility
  - images
  - statistical
---

# CRITBINOM Image Guide

Images planned for [CRITBINOM](../../Functions/Statistical/CRITBINOM.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: CRITBINOM Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a formula bar. |
| Content | The formula `=CRITBINOM(trials, probability_s, alpha)` with each argument in its own color. Captions read "number of trials", "chance of success per trial" and "target cumulative probability". |
| Alt Text | A CRITBINOM formula with its trials, probability and alpha arguments highlighted and labeled. |
| File Name | CRITBINOM Syntax Anatomy.png |

## Image 2: Cumulative Totals for CRITBINOM

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 5. |
| Format | Bar chart with a horizontal line for the target. |
| Content | Bars for the cumulative probability of 0 through 6 successes with 10 trials at 30 percent: about 0.028, 0.149, 0.383, 0.650, 0.850, 0.953 and 0.989. A dashed horizontal line marks 0.9. The bar for 5 successes is the first to cross the line, labeled "result 5". |
| Alt Text | A bar chart of cumulative binomial probabilities crossing a dashed 0.9 line at 5 successes. |
| File Name | CRITBINOM Cumulative Totals.png |

## Image 3: Survey Response Threshold

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Bar chart with a horizontal line for the target. |
| Content | Bars for the cumulative probability of 10 through 13 responses with 25 invitations at 40 percent: about 0.586, 0.732, 0.846 and 0.922. A dashed line marks 0.8. The bar for 12 responses is labeled "result 12" and is the first above the line. |
| Alt Text | A bar chart showing the cumulative probability crossing 0.8 at 12 survey responses. |
| File Name | CRITBINOM Survey Threshold.png |
