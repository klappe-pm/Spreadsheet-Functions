---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
related:
  - MID
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - text
  - images
---

# MID Image Guide

Images planned for [MID](../../Functions/Text/MID.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: MID Argument Positions

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of one formula. |
| Content | The formula `=MID(text, start_num, num_chars)` with each argument boxed and labeled. Below it, the sample text `Invoice-2025-0457` is laid out character by character with position numbers 1 to 16 above it, and the cells for positions 9 to 12 are shaded to show the result `2025`. |
| Alt Text | Diagram of the MID formula with its three arguments and a character position ruler showing the extracted year. |
| File Name | MID Argument Positions.png |

## Image 2: Finding the Start and Length From Delimiters

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 2 result. |
| Format | Worksheet screenshot with the formula bar visible. |
| Content | Cell A2 contains `SKU-98213-RED`. The two hyphens are highlighted with arrows labeled FIND, and the segment `98213` between them is outlined. The formula bar shows the full MID formula. |
| Alt Text | Worksheet cell with a SKU code, its two hyphens marked, and the middle segment extracted by a MID formula. |
| File Name | MID Delimiter Start and Length.png |

## Image 3: Fixed-Width Record Layout

| Item | Instruction |
| --- | --- |
| Placement | Use Cases section, after the Fixed-Width File Parsing scenario. |
| Format | Table diagram with a position ruler. |
| Content | One fixed-width record shown across a ruler from position 1 to 36. Three colored blocks are labeled Customer ID (positions 1 to 6), Name (positions 7 to 26) and Balance (positions 27 to 36). Each block lists the MID formula used to extract it. |
| Alt Text | Diagram of a fixed-width record with three fields marked by position and the matching MID formula for each field. |
| File Name | MID Fixed Width Record Layout.png |
