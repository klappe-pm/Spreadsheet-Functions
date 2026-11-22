---
domain: Spreadsheet Functions
category: Financial
subcategory: Investment Returns
related:
  - XIRR
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# XIRR Image Guide

Images planned for [XIRR](../../Functions/Financial/XIRR.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Cash Flow Layout

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | Two columns with a Date header in `A1` and a Cash Flow header in `B1`. Rows 2 to 5 hold dates and amounts. The first amount is negative and is labeled Outlay; the rest are positive and labeled Receipt. Arrows show the `values` and `dates` ranges feeding the formula. |
| Alt Text | A worksheet with dates in one column and cash flows in the next, with the values and dates ranges of an XIRR formula labeled. |
| File Name | XIRR Cash Flow Layout.png |

## Image 2: Sign Convention for Cash Flows

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Simple diagram on a timeline. |
| Content | A horizontal timeline from 2024-03-01 to 2025-08-20. The outlay of 5,000 is drawn as a downward arrow at the start; the three receipts are drawn as upward arrows at their dates. Labels state the sign convention: payments out negative, receipts positive. |
| Alt Text | A timeline with one downward outlay arrow at the start and three upward receipt arrows on later dates. |
| File Name | XIRR Sign Convention Timeline.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the loan repayment table with the result cell. |
| Content | The table for Problem 2 with the four cash flows in `B2:B5` and the dates in `A2:A5`. The formula `=XIRR(B2:B5, A2:A5)` is shown in the formula bar and its result 14.03% is shown in a labeled output cell. |
| Alt Text | A loan repayment table with a formula bar showing an XIRR formula and a result of 14.03 percent. |
| File Name | XIRR Loan Repayments Result.png |
