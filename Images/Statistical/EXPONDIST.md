---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - EXPONDIST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - compatibility
  - images
  - statistical
---

# EXPONDIST Image Guide

Images planned for [EXPONDIST](../../Functions/Statistical/EXPONDIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: EXPONDIST Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a formula bar. |
| Content | The formula `=EXPONDIST(x, lambda, cumulative)` with each argument in its own color. Captions read "time, 0 or more", "rate, above 0" and "TRUE for probability, FALSE for density". |
| Alt Text | An EXPONDIST formula with x, lambda and cumulative arguments highlighted and labeled. |
| File Name | EXPONDIST Syntax Anatomy.png |

## Image 2: Rate From an Average Lifetime

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two-step diagram. |
| Content | Left box: "Average life 800 hours". An arrow labeled "1 divided by 800" leads to a right box "Lambda 0.00125 per hour". The formula `=EXPONDIST(500, 1/800, TRUE)` sits below, with the result 0.4647. |
| Alt Text | A diagram converting an average life of 800 hours into a rate of 0.00125 per hour for the EXPONDIST formula. |
| File Name | EXPONDIST Rate From Average Life.png |

## Image 3: Light Bulb Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Cumulative curve with a marker. |
| Content | A cumulative curve for a rate of 0.00125 per hour with a vertical marker at 500 hours. The point on the curve is labeled 0.4647. The formula `=EXPONDIST(500, 1/800, TRUE)` sits beside the chart. |
| Alt Text | A cumulative exponential curve for light bulbs with a marker at 500 hours showing a probability of 0.4647. |
| File Name | EXPONDIST Light Bulb Result.png |
