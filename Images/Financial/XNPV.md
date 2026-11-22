---
domain: Spreadsheet Functions
category: Financial
subcategory: Investment Returns
related:
  - XNPV
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# XNPV Image Guide

Images planned for [XNPV](../../Functions/Financial/XNPV.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Discount Rate and Schedule Layout

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | A Date and Cash Flow table in `A1:B5` with the first row negative. A rate label in `D1` and the value 0.08 in `D2` are outlined in a second color. Arrows show `rate`, `values` and `dates` mapping to the formula arguments. |
| Alt Text | A worksheet with a dated cash flow table and a rate cell, with each XNPV argument labeled. |
| File Name | XNPV Rate and Schedule Layout.png |

## Image 2: Result at Two Discount Rates

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Bar chart with two bars. |
| Content | Two bars for the same schedule: at 8 percent the bar is negative at -284.96; at 5 percent it is positive at 65.03. A zero line runs across the chart and each bar carries its value label. |
| Alt Text | A bar chart comparing the net present value of one schedule at 8 percent, which is negative, and at 5 percent, which is positive. |
| File Name | XNPV Result at Two Rates.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the oven savings table with the result cell. |
| Content | The five-row oven table with the purchase in row 2 and the savings below it. The rate 9% in `D2` and the formula `=XNPV(D2, B2:B6, A2:A6)` are shown, with the result -1801.45 in a labeled output cell. |
| Alt Text | An oven savings table with an XNPV formula at 9 percent returning a negative value of 1801.45. |
| File Name | XNPV Oven Result.png |
