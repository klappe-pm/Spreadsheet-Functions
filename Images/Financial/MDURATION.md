---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
related:
  - MDURATION
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# MDURATION Image Guide

Images planned for [MDURATION](../../Functions/Financial/MDURATION.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Bond Dates, Coupon and Yield Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | Cells `B2` to `B6` labeled settlement (1/15/2025), maturity (1/15/2030), coupon (6%), yield (5%) and frequency (2). An arrow from the formula bar points to each cell in `=MDURATION(B2, B3, B4, B5, B6)`. |
| Alt Text | A worksheet with bond dates, coupon, yield and frequency cells labeled as the arguments of MDURATION. |
| File Name | MDURATION Bond Arguments.png |

## Image 2: Price Change for a Yield Move

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Line chart of estimated price against yield. |
| Content | Two lines over yields from 4% to 6%: a straight tangent line from the modified duration estimate at 5% and a curved line for the bond's full price. The two lines touch at 5%, and the tangent line is labeled with the 4.30% per point slope. |
| Alt Text | A line chart showing a straight duration estimate touching a curved bond price line at a 5% yield. |
| File Name | MDURATION Price Change Estimate.png |

## Image 3: Duration Results for the Bond Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the bond inputs and two result cells. |
| Content | The Problem 1 inputs table with the result 4.30 in a labeled cell. Beside it, the Problem 2 cell showing -2.15% for a half point rise in yield. |
| Alt Text | A worksheet with a bond duration of 4.30 and an estimated price change of negative 2.15 percent. |
| File Name | MDURATION Bond Problem Results.png |
