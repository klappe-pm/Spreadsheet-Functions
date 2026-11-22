---
domain: Spreadsheet Functions
category: Financial
subcategory: Treasury Bills
related:
  - TBILLYIELD
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# TBILLYIELD Image Guide

Images planned for [TBILLYIELD](../../Functions/Financial/TBILLYIELD.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=TBILLYIELD(settlement, maturity, pr)` with each argument labeled. A note beside pr says the price is quoted per 100 of face value, and a caption under the formula says Google Sheets names the third argument price. |
| Alt Text | A TBILLYIELD formula with its three arguments labeled and a note that the price is per 100 of face value. |
| File Name | TBILLYIELD Syntax Anatomy.png |

## Image 2: Story Problem Result Panel

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the quote terms in a small table. |
| Content | Settlement February 15, 2026, maturity August 14, 2026 and price 98.25 in labeled cells. The formula `=TBILLYIELD(DATE(2026,2,15), DATE(2026,8,14), 98.25)` sits in a result cell showing 3.56%. |
| Alt Text | A worksheet showing a Treasury bill quoted at 98.25 per 100 with a yield of 3.56 percent. |
| File Name | TBILLYIELD Dealer Quote Result.png |
