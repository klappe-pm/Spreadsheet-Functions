---
domain: Spreadsheet Functions
category: Database
subcategory: Database Aggregation
related:
  - DCOUNT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - database
  - images
---

# DCOUNT Image Guide

Images planned for [DCOUNT](../../Functions/Database/DCOUNT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Database, Field and Criteria Ranges

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a worksheet. |
| Content | The shop list `A1:E8` outlined in one color and labeled database, the Units header highlighted and labeled field, and the criteria block `G1:G2` outlined in a second color and labeled criteria. |
| Alt Text | A worksheet with the database, field and criteria ranges of a DCOUNT formula outlined and labeled. |
| File Name | DCOUNT Database Field Criteria.png |

## Image 2: Numeric Versus Nonblank Counting

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Two column snapshots side by side. |
| Content | Left: the Units column with the Hillside desk cell showing `Pending`, captioned DCOUNT (numbers only), with the result 1. Right: the same column with the same cell highlighted, captioned DCOUNTA (nonblank), with the result 2. |
| Alt Text | Two counts of the same Units column showing that DCOUNT skips a text entry and DCOUNTA counts it. |
| File Name | DCOUNT Numeric Versus Nonblank.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the ticket list with matching rows highlighted. |
| Content | The ticket list with T101 and T104 highlighted, T103 marked with a note that its hours value is text, the criteria cell `E2` showing Support, and the DCOUNT result 2 in a labeled output cell. |
| Alt Text | A ticket list with two numeric Support entries highlighted and a DCOUNT result of 2. |
| File Name | DCOUNT Support Tickets Result.png |
