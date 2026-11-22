---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
related:
  - CELL
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - information
---

# CELL Image Guide

Images planned for [CELL](../../Functions/Information/CELL.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=CELL(info_type, [reference])` on a light background. `info_type` is labeled as the text that names the detail, and `reference` is labeled as the cell to inspect, with a note that the argument is optional in Excel and required in Google Sheets. |
| Alt Text | A CELL formula with its info_type and optional reference arguments labeled. |
| File Name | CELL Syntax Anatomy.png |

## Image 2: Cell Type Results

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of a small worksheet. |
| Content | Three cells in column B: one blank, one with the text Yes, and one with the number 4. Each has a CELL("type") formula beside it showing b, l and v in turn. |
| Alt Text | A worksheet showing CELL type results of b for a blank cell, l for text and v for a number. |
| File Name | CELL Type Results.png |

## Image 3: Address Result in the Formula Bar

| Item | Instruction |
| --- | --- |
| Placement | Use Cases section, after the Cell Location Audit formula. |
| Format | Screenshot of Excel with the formula bar visible. |
| Content | Cell C12 on the Inputs sheet selected, with the formula bar showing =CELL("address", Inputs!C12) and the result cell beside it showing $C$12. |
| Alt Text | Excel formula bar showing a CELL address formula that returns the absolute address of a cell. |
| File Name | CELL Address Formula Bar.png |
