---
domain: Spreadsheet Functions
category: Information
subcategory: Error Checks
related:
  - ISERR
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISERR Image Guide

Images planned for [ISERR](../../Functions/Information/ISERR.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Error Exception Table

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two-column table with a short note. |
| Content | Left column: error values `#DIV/0!`, `#VALUE!`, `#REF!`, `#NAME?`, `#NUM!` and `#NULL!` marked TRUE. A separate row for `#N/A` marked FALSE, highlighted in a second color with the label "excluded". |
| Alt Text | A table showing that ISERR returns TRUE for every error except #N/A, which returns FALSE. |
| File Name | ISERR Error Exception Table.png |

## Image 2: ISERR Versus ISERROR Results

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 5. |
| Format | Side by side worksheet comparison. |
| Content | Two columns for the same four cells: `#DIV/0!`, `#N/A`, the number 10 and `SQRT(-1)`. The left column shows ISERR results (TRUE, FALSE, FALSE, TRUE) and the right column shows ISERROR results (TRUE, TRUE, FALSE, TRUE), with the `#N/A` row highlighted. |
| Alt Text | A comparison of ISERR and ISERROR results for four cells, where only the #N/A row differs. |
| File Name | ISERR Versus ISERROR Results.png |
