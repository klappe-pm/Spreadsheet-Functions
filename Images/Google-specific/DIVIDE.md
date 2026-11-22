---
domain: Spreadsheet Functions
category: Google-specific
subcategory: Operator Functions
related:
  - DIVIDE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - arithmetic
  - images
---

# DIVIDE Image Guide

Images planned for [DIVIDE](../../Functions/Google-specific/DIVIDE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: DIVIDE Arguments

| Item | Instruction |
| --- | --- |
| Placement | Description section, directly below the third paragraph. |
| Format | Annotated screenshot of a worksheet in Google Sheets. |
| Content | Cells B2 (dividend, 120) and C2 (divisor, 8) with the formula `=DIVIDE(B2, C2)` in D2 showing 15. Each argument has a callout label: dividend and divisor. |
| Alt Text | A DIVIDE formula with its dividend and divisor cells labeled and the quotient 15 shown. |
| File Name | DIVIDE Arguments.png |

## Image 2: DIVIDE Zero Divisor Guard

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two stacked screenshots of the same formula, one before and one after a zero divisor. |
| Content | Top: `=DIVIDE(B2, C2)` with C2 holding 0 and an error shown. Bottom: `=IFERROR(DIVIDE(B2, C2), 0)` with the cell showing 0. Captions read "Without IFERROR" and "With IFERROR". |
| Alt Text | Two versions of a DIVIDE formula with a zero divisor, one showing an error and one wrapped in IFERROR. |
| File Name | DIVIDE Zero Divisor Guard.png |
