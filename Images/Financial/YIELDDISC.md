---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
related:
  - YIELDDISC
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# YIELDDISC Image Guide

Images planned for [YIELDDISC](../../Functions/Financial/YIELDDISC.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Discount Security Layout

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | An input block in `A1:B5` with labels in column A: settlement date, maturity date, price, redemption and basis. A bar along the top shows the price below the redemption value, labeled as the gain to be annualized. |
| Alt Text | A worksheet input block for a discount security with a price bar below the redemption value. |
| File Name | YIELDDISC Discount Security Layout.png |

## Image 2: Actual Days Versus 30/360 Days

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Two calendar strips side by side. |
| Content | Left strip: February 10 to May 12, 2025 with every actual day shaded, captioned basis 2 with 91 days in the denominator. Right strip: the same dates on a 30-day month grid, captioned basis 0 with 92 days. |
| Alt Text | Two calendar strips for the same dates, one counting actual days and one counting 30-day months. |
| File Name | YIELDDISC Actual Versus 30 360 Days.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the discount note input table with the result cell. |
| Content | The Problem 2 input table in `A1:B5`, the formula `=YIELDDISC(DATE(2025,9,15), DATE(2026,1,13), 99.10, 100, 2)` in the formula bar, and the result 2.72% in a labeled output cell. |
| Alt Text | A discount note input table with a YIELDDISC formula and a result of 2.72 percent. |
| File Name | YIELDDISC Discount Note Result.png |
