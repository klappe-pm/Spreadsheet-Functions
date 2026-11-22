---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
related:
  - YIELD
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# YIELD Image Guide

Images planned for [YIELD](../../Functions/Financial/YIELD.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Bond Inputs Layout

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | An input block in `A1:B7` with labels in column A and values in column B: settlement date, maturity date, coupon rate, price, redemption, coupons per year and day count basis. Each value cell is outlined and a matching arrow points to the argument position in the formula bar. |
| Alt Text | A worksheet input block for a bond with each value cell linked to the matching YIELD argument. |
| File Name | YIELD Bond Inputs Layout.png |

## Image 2: Day Count Basis Codes

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Reference card drawn as a two-column table. |
| Content | Five rows, one per basis code: 0 or omitted for US (NASD) 30/360, 1 for actual/actual, 2 for actual/360, 3 for actual/365, 4 for European 30/360. Each row has a small calendar icon showing how the day count is taken. |
| Alt Text | A reference card listing the five YIELD day count basis codes and their names. |
| File Name | YIELD Day Count Basis Codes.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the municipal bond input table with the result cell. |
| Content | The Problem 1 input table in `A1:B6`, the formula `=YIELD(DATE(2025,6,1), DATE(2029,11,15), 0.05, 96.20, 100, 2, 0)` in the formula bar, and the result 5.98% in a labeled output cell. |
| Alt Text | A municipal bond input table with a YIELD formula and a result of 5.98 percent. |
| File Name | YIELD Municipal Bond Result.png |
