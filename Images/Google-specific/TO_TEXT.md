---
category: Google-specific
subcategory: Parser Functions
related:
  - TO_TEXT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - sheets
---

# TO_TEXT Image Guide

Images planned for [TO_TEXT](../../Functions/Google-specific/TO_TEXT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Number Versus Text Result

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two worksheet cells side by side with a formula bar visible. |
| Content | Left: the currency value `1250` displayed as `$1,250.00`. Right: the result of `=TO_TEXT(A2)` displayed as `$1,250.00` and left aligned, with a label that reads text output. |
| Alt Text | A currency value beside its text result, both displayed as $1,250.00, with the text result aligned to the left. |
| File Name | TO_TEXT Number Versus Text.png |

## Image 2: Currency Text in an Export Column

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the invoice row with three columns. |
| Content | The invoice number `INV-2041` in `A2`, the amount `1250` in `B2` formatted as currency, the converted text `$1,250.00` in `C2`, and the length `9` in `D2` with the LEN formula in the formula bar. |
| Alt Text | An invoice row with the amount converted to text and a character count of 9. |
| File Name | TO_TEXT Invoice Export.png |

## Image 3: Percentage Label Beside a Dashboard Title

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a dashboard cell with a label. |
| Content | The rate `0.25` in `B2` displayed as `25%`, and the label cell `C2` showing `Growth: 25%` with the formula `="Growth: "&TO_TEXT(B2)` in the formula bar. |
| Alt Text | A dashboard label that reads Growth: 25%, built from a percentage cell with TO_TEXT. |
| File Name | TO_TEXT Growth Label.png |
