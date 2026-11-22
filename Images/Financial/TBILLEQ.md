---
domain: Spreadsheet Functions
category: Financial
subcategory: Treasury Bills
related:
  - TBILLEQ
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# TBILLEQ Image Guide

Images planned for [TBILLEQ](../../Functions/Financial/TBILLEQ.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=TBILLEQ(settlement, maturity, discount)` with each argument labeled. A timeline below the formula shows settlement, maturity and a bracket marked DSM, the days between them. |
| Alt Text | A TBILLEQ formula with its three arguments labeled and a timeline showing settlement, maturity and the days between them. |
| File Name | TBILLEQ Syntax Anatomy.png |

## Image 2: Story Problem Result Panel

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the bill terms and the deposit rate in a small table. |
| Content | Settlement February 15, 2026, maturity August 14, 2026 and discount 4% in labeled cells, with the deposit rate 4.10% beside them. The formula `=TBILLEQ(DATE(2026,2,15), DATE(2026,8,14), 0.04)` sits in a result cell showing 4.14%. |
| Alt Text | A worksheet comparing a 4 percent bill discount rate, converted to a 4.14 percent bond-equivalent yield, with a 4.10 percent deposit rate. |
| File Name | TBILLEQ Bill Versus Deposit Result.png |
