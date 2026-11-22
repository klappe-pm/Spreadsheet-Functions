---
domain: Spreadsheet Functions
category: Financial
subcategory: Treasury Bills
related:
  - TBILLPRICE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# TBILLPRICE Image Guide

Images planned for [TBILLPRICE](../../Functions/Financial/TBILLPRICE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=TBILLPRICE(settlement, maturity, discount)` with each argument labeled. A small bar beside the formula marks a price of 100 at the top and the discounted price below it, with the discount labeled. |
| Alt Text | A TBILLPRICE formula with its three arguments labeled and a bar showing a price below face value of 100. |
| File Name | TBILLPRICE Syntax Anatomy.png |

## Image 2: Story Problem Result Panel

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the bill terms in a small table. |
| Content | Settlement February 15, 2026, maturity August 14, 2026, discount 4% and face value 500,000 in labeled cells. The formula `=TBILLPRICE(DATE(2026,2,15), DATE(2026,8,14), 0.04)*500000/100` sits in a result cell showing 490,000.00. A note beside the price cell reads 98.00 per 100 of face value. |
| Alt Text | A worksheet showing a Treasury bill with a face value of 500,000 priced at 98.00 per 100, for a total cost of 490,000.00. |
| File Name | TBILLPRICE Municipal Purchase Result.png |
