---
domain: Spreadsheet Functions
category: Web
subcategory: Google Data Services
related:
  - IMPORTRANGE
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - cross-spreadsheet
  - web
---

# IMPORTRANGE Image Guide

Images planned for [IMPORTRANGE](../../Functions/Web/IMPORTRANGE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Source File, Range String and Destination

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Diagram with two spreadsheet windows and a formula. |
| Content | On the left, a source spreadsheet with a sheet tab named "Sales" and the range `A1:D10` outlined. On the right, a destination spreadsheet with the formula `=IMPORTRANGE(url, "Sales!A1:D10")` in a cell and the imported block below it. An arrow runs from the source range to the destination cell. Labels read "Source file URL" and "Sheet and range". |
| Alt Text | A diagram showing a source spreadsheet range flowing into a destination sheet through an IMPORTRANGE formula. |
| File Name | IMPORTRANGE Source And Destination.png |

## Image 2: A Filtered Import Using QUERY

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 4. |
| Format | Screenshot of a worksheet. |
| Content | The destination sheet shows a result table with two columns and a header row. The formula bar shows `=QUERY(IMPORTRANGE(...),"select Col1, Col4 where Col4 > 1000",1)`. Only rows with values above 1000 appear in the table. |
| Alt Text | A destination worksheet showing a filtered table of two columns produced by QUERY wrapped around IMPORTRANGE. |
| File Name | IMPORTRANGE Filtered Query.png |
