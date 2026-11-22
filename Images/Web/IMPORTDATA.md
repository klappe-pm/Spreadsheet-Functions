---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
related:
  - IMPORTDATA
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - csv
  - web
---

# IMPORTDATA Image Guide

Images planned for [IMPORTDATA](../../Functions/Web/IMPORTDATA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: The URL Argument and the Imported Grid

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a browser window beside a worksheet. |
| Content | The browser shows a plain-text CSV file with comma-separated lines, labeled "The address must point to the file". The worksheet shows the formula `=IMPORTDATA(...)` with the address highlighted and an arrow leading to the rows it fills below and to the right. |
| Alt Text | A browser showing a plain CSV file next to a worksheet where IMPORTDATA fills rows from that file's address. |
| File Name | IMPORTDATA URL And Grid.png |

## Image 2: Imported CSV Rows in the Sheet

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 2. |
| Format | Screenshot of a worksheet. |
| Content | Rows of a sample store list imported by IMPORTDATA. The first row, labeled as the header, is shaded differently. Each comma-separated field is in its own column. The formula bar shows `=IMPORTDATA(A2)` and the cell `A2` shows the address. |
| Alt Text | A worksheet showing a store list imported from a CSV address, with the header row shaded and each field in its own column. |
| File Name | IMPORTDATA Imported Store Rows.png |

## Image 3: Daily Export Address in the Story Problem

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, directly below the Problem 1 answer. |
| Format | Screenshot of a worksheet with a small input table. |
| Content | Cell `B1` shows 12 and cell `B2` shows 2026-11-21. A result cell beside them shows the completed address `https://example.com/exports/daily.csv?store=12&day=2026-11-21`, with the formula bar showing the IMPORTDATA formula. |
| Alt Text | A worksheet with a store number and export date that combine into a daily CSV address used by IMPORTDATA. |
| File Name | IMPORTDATA Daily Export Address.png |
