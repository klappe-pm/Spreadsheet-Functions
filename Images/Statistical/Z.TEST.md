---
domain: Spreadsheet Functions
category: Statistical
subcategory: Hypothesis Tests
related:
  - Z.TEST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# Z.TEST Image Guide

Images planned for [Z.TEST](../../Functions/Statistical/Z.TEST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Arguments on a Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | The data range `B2:B11` outlined and labeled array, a cell with the hypothesized mean 11 labeled x, and an optional cell with the value 2 labeled sigma. The formula bar shows `=Z.TEST(B2:B11, 11, 2)`. |
| Alt Text | A worksheet with the array, x and sigma arguments of Z.TEST outlined and labeled. |
| File Name | Z TEST Syntax Arguments.png |

## Image 2: Tail Areas for One-Tailed and Two-Tailed Tests

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 1 and Example 2. |
| Format | Diagram of a bell curve with shaded tails. |
| Content | Left panel: a normal curve with the right tail shaded and captioned one-tailed value. Right panel: the same curve with both tails shaded and captioned two-tailed value, with the note that the two-tailed value is twice the smaller tail. |
| Alt Text | Two bell curves comparing a shaded right tail for a one-tailed Z.TEST result with two shaded tails for a two-tailed result. |
| File Name | Z TEST Tail Areas.png |

## Image 3: Results for the Delivery Times Story

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the delivery table with the formula result. |
| Content | The eight delivery times in `B2:B9` with the formula `=Z.TEST(B2:B9, 40, 3)` in an adjacent cell and the result 0.006664 highlighted. |
| Alt Text | A worksheet with eight delivery times and a Z.TEST result of 0.006664. |
| File Name | Z TEST Delivery Result.png |
