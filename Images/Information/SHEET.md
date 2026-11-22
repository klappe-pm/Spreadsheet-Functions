---
domain: Spreadsheet Functions
category: Information
subcategory: Workbook Information
related:
  - SHEET
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - information
  - images
---

# SHEET Image Guide

Images planned for [SHEET](../../Functions/Information/SHEET.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula. |
| Content | The formula `=SHEET([value])` with `SHEET` labeled as the function and `value` labeled as optional. Beneath it, three forms: no argument for the current sheet, a quoted sheet name, and a reference such as `Feb!A1`. |
| Alt Text | Diagram of the SHEET formula with its optional value argument and three forms it accepts. |
| File Name | SHEET Syntax Anatomy.png |

## Image 2: Tab Positions and Sheet Lookups

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 6. |
| Format | Screenshot of the workbook tab bar with a results panel. |
| Content | The tab bar in order: Summary, Jan, Feb, Mar, Notes, Archive, with each tab labeled by its position number 1 to 6. The Mar tab is highlighted with the formula `=SHEET(Mar!B2)-SHEET(Jan!B2)` and the result 2. |
| Alt Text | A tab bar with numbered positions and a formula that subtracts two tab positions to show a gap of 2. |
| File Name | SHEET Tab Positions.png |
