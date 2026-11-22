---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
related:
  - IMPORTHTML
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - html-parsing
  - web
---

# IMPORTHTML Image Guide

Images planned for [IMPORTHTML](../../Functions/Web/IMPORTHTML.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Address, Query Type and Index

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a formula. |
| Content | The formula `=IMPORTHTML(url, query, index)` is shown with three callouts. The `url` callout points to a web page address, labeled "Page address". The `query` callout is labeled "Type: table or list". The `index` callout is labeled "Position of the table or list, counted from 1 separately for each type". |
| Alt Text | A labeled diagram of the IMPORTHTML formula showing the page address, the query type and the index. |
| File Name | IMPORTHTML Syntax Arguments.png |

## Image 2: A List Imported as One Column

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 3. |
| Format | Two-panel diagram. |
| Content | The left panel shows a bulleted list in a web page, with the first list highlighted. The right panel shows a worksheet column where each bullet is in its own row, with the formula `=IMPORTHTML(...,"list",1)` in the cell above. |
| Alt Text | A web page bulleted list on the left and the same items as one column in a worksheet on the right. |
| File Name | IMPORTHTML List Column.png |
