---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
related:
  - IMPORTJSON
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - json
  - web
---

# IMPORTJSON Image Guide

Images planned for [IMPORTJSON](../../Functions/Web/IMPORTJSON.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: The URL and the Path Argument

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a formula and a JSON response. |
| Content | The formula `=IMPORTJSON(url, query)` is shown beside a short JSON response with two records. The `url` callout points to the address, labeled "JSON response". The `query` callout, `/title`, points to the `title` field inside each record. A banner above the formula reads "Community script, not built in". |
| Alt Text | A diagram of the IMPORTJSON formula linking its address argument to a JSON response and its path argument to one field in each record. |
| File Name | IMPORTJSON URL And Path.png |

## Image 2: Imported Values Summed in a Column

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 4. |
| Format | Screenshot of a worksheet. |
| Content | A column of three imported prices, 19.50, 4.25 and 8.00, with the formula `=SUM(A2:A4)` in a cell below them that shows 31.75. The formula bar shows the SUM formula. |
| Alt Text | A worksheet column of three imported prices with a SUM formula below them that shows the total 31.75. |
| File Name | IMPORTJSON Summed Prices.png |
