---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
related:
  - RATE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# RATE Image Guide

Images planned for [RATE](../../Functions/Financial/RATE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=RATE(nper, pmt, pv, [fv], [type], [guess])` with each argument labeled. Brackets around fv, type and guess are marked optional. Arrows show that the payment and the present value carry opposite signs. |
| Alt Text | A RATE formula with its six arguments labeled and the optional ones marked. |
| File Name | RATE Syntax Anatomy.png |

## Image 3: Story Problem Result Panel

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the financing terms in a small table. |
| Content | The amount 10,000, the payment of -310 and the 36 periods in labeled cells. The formula `=RATE(36, -310, 10000)*12` sits in a result cell showing 7.27%. A note beside the cell reads monthly rate times 12. |
| Alt Text | A worksheet with 36 payments of 310 on a 10,000 financing amount, showing a nominal annual rate of 7.27 percent. |
| File Name | RATE Equipment Financing Result.png |

## Image 2: Monthly to Annual Conversion

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 1. |
| Format | Two-step flow diagram. |
| Content | Box one, labeled RATE output: 0.698% per month. Arrow labeled times 12. Box two, labeled nominal annual rate: 8.37%. |
| Alt Text | A flow diagram converting a monthly rate of about 0.698 percent into an annual nominal rate of 8.37 percent. |
| File Name | RATE Monthly To Annual.png |
