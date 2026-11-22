---
category: Google-specific
subcategory: Parser Functions
related:
  - TO_DOLLARS
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - sheets
---

# TO_DOLLARS Image Guide

Images planned for [TO_DOLLARS](../../Functions/Google-specific/TO_DOLLARS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Number Versus Currency Display

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Side by side pair of worksheet cells. |
| Content | Left: the number `1250` in a cell with the Number format. Right: the same value after `=TO_DOLLARS(A2)`, shown as `$1,250.00`. A label under the right cell reads still a number, and a formula bar shows the unchanged value. |
| Alt Text | The number 1250 on the left and the same value shown as $1,250.00 on the right. |
| File Name | TO_DOLLARS Number Versus Currency.png |

## Image 2: Calculated Amount Display

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a short cell list. |
| Content | Three rows: the base values in column A and the formula results in column B, with the formula bar showing `=TO_DOLLARS(B2*C2)` and the result `$102.00` labeled. |
| Alt Text | A worksheet with a multiplied amount formatted as $102.00 in a result cell. |
| File Name | TO_DOLLARS Calculated Amount.png |

## Image 3: Invoice Total Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of an invoice with two line items and a total. |
| Content | Line items 1250 and 89.9 in `B2:B3`, the total cell `B5` showing `$1,339.90`, and a callout that says the SUM inside the formula produces 1339.9 before the currency display is applied. |
| Alt Text | An invoice with two line items and a total displayed as $1,339.90. |
| File Name | TO_DOLLARS Invoice Total.png |
