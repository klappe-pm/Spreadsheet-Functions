---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
related:
  - COUPDAYBS
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# COUPDAYBS Image Guide

Images planned for [COUPDAYBS](../../Functions/Financial/COUPDAYBS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Coupon Period Timeline

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Horizontal timeline diagram with labeled dates. |
| Content | A line showing the last coupon date (August 15, 2026), the settlement date (February 10, 2027) and the next coupon date (February 15, 2027). Shade the span from the last coupon to settlement and label it COUPDAYBS (179 days, actual). Shade the remaining five days in a second color and label them COUPDAYSNC. |
| Alt Text | A timeline of a coupon period with the days before settlement and the days after settlement shaded in different colors. |
| File Name | COUPDAYBS Coupon Period Timeline.png |

## Image 2: Accrued Share Calculation

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Annotated worksheet screenshot. |
| Content | The formula bar showing the COUPDAYBS formula divided by COUPDAYS, with the result cell displaying 0.9728. Add small labels that name the numerator (179 days) and the denominator (184 days). |
| Alt Text | A worksheet with a formula dividing the days from the last coupon to settlement by the days in the coupon period. |
| File Name | COUPDAYBS Accrued Share Calculation.png |

## Image 3: Bond Table and Accrued Share

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the bond table with a highlighted row. |
| Content | The Bond, Settlement, Maturity, Frequency and Basis table with the Ridge row (row 3) highlighted. Show the Problem 2 formula in a cell below the table and the result 0.8667 in a labeled output cell. |
| Alt Text | A bond table with the Ridge row highlighted and a formula producing the accrued share 0.8667. |
| File Name | COUPDAYBS Bond Table and Accrued Share.png |
