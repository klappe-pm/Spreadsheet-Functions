---
domain: Spreadsheet Functions
category: Database
subcategory: Database Aggregation
related:
  - COUNTUNIQUEIFS
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - database
  - images
---

# COUNTUNIQUEIFS Image Guide

Images planned for [COUNTUNIQUEIFS](../../Functions/Database/COUNTUNIQUEIFS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: COUNTUNIQUEIFS Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a formula bar. |
| Content | The formula `=COUNTUNIQUEIFS(count_unique_range, criteria_range1, criterion1, [criteria_range2, criterion2, ...])`. The first argument is one color and labeled "counted once per person". The criteria pairs are a second color, and the optional pair is in brackets. |
| Alt Text | A COUNTUNIQUEIFS formula with its count range, criteria pairs and optional pair labeled. |
| File Name | COUNTUNIQUEIFS Syntax Anatomy.png |

## Image 2: Distinct Customers Versus Rows

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 1. |
| Format | Two columns side by side. |
| Content | Left column: the five Web rows from the purchase list with Ana and Cara appearing twice, captioned "5 rows". Right column: the three distinct names Ana, Cara and Ben, captioned "3 distinct customers". An arrow links each name on the right to its rows on the left. |
| Alt Text | Five web purchase rows reduced to three distinct customers with arrows linking repeated names to one entry. |
| File Name | COUNTUNIQUEIFS Distinct Versus Rows.png |

## Image 3: Workshop Attendee Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the session list with matching rows highlighted. |
| Content | The table in `A1:C9`. The Workshop rows rated 4 or higher are highlighted: Priya, Lena (two rows) and Tom. Omar's row is not highlighted. The formula `=COUNTUNIQUEIFS(A2:A9, B2:B9, "Workshop", C2:C9, ">=4")` and its result 3 sit in a labeled cell beside the table. |
| Alt Text | A session table with the qualifying workshop ratings highlighted and a COUNTUNIQUEIFS result of 3. |
| File Name | COUNTUNIQUEIFS Workshop Result.png |
