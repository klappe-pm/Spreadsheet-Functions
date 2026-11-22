---
domain: Spreadsheet Functions
category: Statistical
subcategory: Distributions
related:
  - STANDARDIZE
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - distribution
---

# STANDARDIZE Image Guide

Images planned for [STANDARDIZE](../../Functions/Statistical/STANDARDIZE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Value, Mean and Standard Deviation Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=STANDARDIZE(x, mean, standard_dev)` with each argument in a separate colored box labeled value, mean and standard deviation. A note under standard_dev reads "must be greater than zero". |
| Alt Text | A STANDARDIZE formula with the value, mean and standard deviation arguments labeled. |
| File Name | STANDARDIZE Arguments.png |

## Image 2: Positive and Negative Results

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Bell curve diagram with a vertical axis of standard deviations. |
| Content | A normal curve with marks at minus 1, 0 and 1.25 standard deviations. The mark at 1.25 is labeled with the value 85 from Example 1, and the mark at minus 1 is labeled with the value 58 from Example 2. |
| Alt Text | A bell curve with marks showing a z-score of 1.25 above the mean and a z-score of negative 1 below the mean. |
| File Name | STANDARDIZE Positive Negative Results.png |

## Image 3: Story Problem Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the bolt measurement table with the result visible. |
| Content | The table in `A1:B4` with the measured length 50.9, target mean 50.0 and standard deviation 0.4, and the cell showing `2.25` for `=STANDARDIZE(B2, B3, B4)` in a labeled output cell. |
| Alt Text | A table of bolt measurements with a STANDARDIZE result of 2.25. |
| File Name | STANDARDIZE Bolt Result.png |
