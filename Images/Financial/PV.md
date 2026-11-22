---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
related:
  - PV
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# PV Image Guide

Images planned for [PV](../../Functions/Financial/PV.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula bar. |
| Content | The formula `=PV(rate, nper, pmt, [fv], [type])` with each argument labeled. Brackets around fv and type are marked optional. Rate is shown as `0.05/12` and nper as `360` to suggest monthly periods. |
| Alt Text | A PV formula with its five arguments labeled, showing that fv and type are optional. |
| File Name | PV Syntax Anatomy.png |

## Image 2: Payment Timing Comparison

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two horizontal timelines of 24 months side by side. |
| Content | Top timeline, labeled type 1: a payment arrow at the start of each month. Bottom timeline, labeled type 0: a payment arrow at the end of each month. Captions show the results 6,802.70 and 6,768.86. |
| Alt Text | Two timelines comparing monthly payments at the start and end of each period. |
| File Name | PV Payment Timing.png |

## Image 3: Story Problem Result Panel

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with the payment schedule and the offer side by side. |
| Content | Ten rows of 2,400 payments in one column and the 18,000 offer in a labeled cell. The formula `=-PV(0.05, 10, 2400)` sits in a result cell showing 18,532.16. |
| Alt Text | A worksheet comparing ten annual payments of 2,400 with an 18,000 offer, with a present value of 18,532.16 shown. |
| File Name | PV Settlement Offer Result.png |
