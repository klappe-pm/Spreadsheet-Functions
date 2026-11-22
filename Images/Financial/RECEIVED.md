---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
related:
  - RECEIVED
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# RECEIVED Image Guide

Images planned for [RECEIVED](../../Functions/Financial/RECEIVED.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=RECEIVED(settlement, maturity, investment, discount, [basis])` with each argument labeled. Brackets around basis are marked optional. A small table beside the formula lists basis codes 0 to 4 with their names. |
| Alt Text | A RECEIVED formula with its five arguments labeled and the optional basis marked. |
| File Name | RECEIVED Syntax Anatomy.png |

## Image 2: Basis Comparison Table

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Worksheet screenshot with three result cells side by side. |
| Content | The same settlement and maturity dates, amount and rate in three rows, with the basis set to 3, 2 and omitted. The results 512,398.64, 512,575.18 and 512,295.08 sit in a results column, with the day count in a labeled column. |
| Alt Text | A worksheet comparing RECEIVED results for the same security under three day count bases. |
| File Name | RECEIVED Basis Comparison.png |

## Image 3: Story Problem Result Panel

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the note terms in a small table. |
| Content | Settlement January 5, 2026, maturity July 5, 2026, investment 250,000, discount 5% and basis 2 in labeled cells. The formula `=RECEIVED(DATE(2026,1,5), DATE(2026,7,5), 250000, 0.05, 2)` sits in a result cell showing 256,446.79. |
| Alt Text | A worksheet with the terms of a discounted note and a RECEIVED result of 256,446.79. |
| File Name | RECEIVED Discounted Note Result.png |
