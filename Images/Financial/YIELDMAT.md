---
domain: Spreadsheet Functions
category: Financial
subcategory: Bonds and Securities
related:
  - YIELDMAT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# YIELDMAT Image Guide

Images planned for [YIELDMAT](../../Functions/Financial/YIELDMAT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Issue, Settlement and Maturity Inputs

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | An input block in `A1:B6` with labels in column A: settlement date, maturity date, issue date, interest rate, price and basis. The issue date cell is highlighted and labeled as the start of the note's life, since YIELDMAT needs it in addition to the other dates. |
| Alt Text | A worksheet input block for an interest at maturity note with the issue date highlighted. |
| File Name | YIELDMAT Issue Settlement Maturity Inputs.png |

## Image 2: Issue to Maturity Timeline

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Horizontal timeline diagram. |
| Content | A line from 2025-01-31 (issue) to 2026-06-30 (maturity). Markers show the settlement date at 2025-06-30 and the interval from issue to settlement labeled as the accrued portion, and from settlement to maturity labeled as the remaining portion. |
| Alt Text | A timeline from issue date to maturity with the settlement date marked between them. |
| File Name | YIELDMAT Issue to Maturity Timeline.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the certificate input table with the result cell. |
| Content | The Problem 2 input table in `A1:B6`, the formula `=YIELDMAT(DATE(2025,10,15), DATE(2026,4,15), DATE(2025,4,15), 0.06, 100.30, 0)` in the formula bar, and the result 5.23% in a labeled output cell. |
| Alt Text | A certificate input table with a YIELDMAT formula and a result of 5.23 percent. |
| File Name | YIELDMAT Certificate Result.png |
