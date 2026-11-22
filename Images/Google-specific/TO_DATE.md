---
category: Google-specific
subcategory: Parser Functions
related:
  - TO_DATE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - sheets
---

# TO_DATE Image Guide

Images planned for [TO_DATE](../../Functions/Google-specific/TO_DATE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Serial Number Versus Date Display

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Side by side pair of worksheet cells. |
| Content | Left: the number `45658` in a cell with the General format. Right: the same value after `=TO_DATE(A2)`, shown as `1/1/2025`. An arrow labeled TO_DATE joins the two cells, and a note below reads serial days since December 30, 1899. |
| Alt Text | A serial number 45658 on the left and the date 1/1/2025 on the right, joined by a TO_DATE arrow. |
| File Name | TO_DATE Serial Versus Date.png |

## Image 2: Serial Number Versus Date Display, Time Example

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two cells in a single column. |
| Content | The value `45658.4375` in the upper cell and the result `1/1/2025 10:30 AM` in the lower cell, with the fraction 0.4375 highlighted in the upper cell and labeled as the time of day. |
| Alt Text | A serial number with a decimal part and its converted date and time, 1/1/2025 at 10:30 AM. |
| File Name | TO_DATE Time Fraction.png |

## Image 3: Latest Shipment Date Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the shipment export with the result cell. |
| Content | The four order rows in `A1:B5` with ship serials, the largest value 45689 highlighted, and the result cell `D2` showing `2/1/2025` with a label. |
| Alt Text | A shipment list with the largest serial number highlighted and a converted result of 2/1/2025. |
| File Name | TO_DATE Latest Shipment.png |
