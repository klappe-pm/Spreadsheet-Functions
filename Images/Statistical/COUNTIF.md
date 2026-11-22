---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
related:
  - COUNTIF
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - counting
  - images
  - statistical
---

# COUNTIF Image Guide

Images planned for [COUNTIF](../../Functions/Statistical/COUNTIF.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: COUNTIF Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a formula bar. |
| Content | The formula `=COUNTIF(range, criteria)` with `range` highlighted in one color and `criteria` in a second color. Each highlighted part has a caption below it. |
| Alt Text | A COUNTIF formula with its range and criteria arguments highlighted and labeled. |
| File Name | COUNTIF Syntax Anatomy.png |

## Image 2: Wildcard Patterns in COUNTIF Criteria

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Table-style graphic with three columns: pattern, meaning, sample match. |
| Content | Rows for `"*th"`, `"?????"` and `"~*"`. Each row shows the pattern, a one-line meaning and the matching sample word from the order list. |
| Alt Text | A table of three COUNTIF wildcard patterns with their meanings and sample matches. |
| File Name | COUNTIF Wildcard Patterns.png |

## Image 3: Overdue Invoice Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the invoice list with the qualifying rows highlighted. |
| Content | The invoice table in `A1:B9` with rows INV-102, INV-104, INV-105 and INV-107 highlighted. The formula `=COUNTIF(B2:B9, ">30")` and its result 4 appear in a labeled cell beside the table. |
| Alt Text | An invoice list with four invoices more than 30 days late highlighted and a COUNTIF result of 4. |
| File Name | COUNTIF Overdue Invoices Result.png |
