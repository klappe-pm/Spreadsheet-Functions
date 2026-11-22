---
domain: Spreadsheet Functions
category: Financial
subcategory: Loans and Annuities
related:
  - IPMT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - financial
  - images
---

# IPMT Image Guide

Images planned for [IPMT](../../Functions/Financial/IPMT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Rate, Period and Loan Amount Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | A small input block with the annual rate 7.5%, the number of periods 60, the loan amount 15,000 and the period 1. Each input is labeled with the matching IPMT argument, and an arrow from the formula bar points to each one. The rate cell shows `7.5%/12` in the formula. |
| Alt Text | A worksheet with loan inputs labeled as the rate, period, number of periods and present value arguments of IPMT. |
| File Name | IPMT Rate Period Loan Arguments.png |

## Image 2: Interest Share Falls Over the Loan Term

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 2. |
| Format | Stacked column chart with one column per payment for the first 13 months. |
| Content | Each column is the level payment of 300.57, split into an interest segment and a principal segment. The interest segment shrinks from 93.75 in month 1 to 77.69 in month 13, and the principal segment grows. The chart is labeled with both values. |
| Alt Text | A stacked column chart showing that the interest share of a level loan payment shrinks over the first 13 months. |
| File Name | IPMT Interest Share Over Term.png |

## Image 3: Interest Results for the Loan Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of a two-row results table. |
| Content | Problem 1 with the monthly inputs and the result 77.69 for payment 13. Problem 2 with the annual inputs and the result 723.10 for payment 3. Each result cell is highlighted. |
| Alt Text | A results table showing IPMT interest of 77.69 for a monthly payment and 723.10 for an annual payment. |
| File Name | IPMT Loan Problem Results.png |
