---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Modern Lookup
related:
  - XLOOKUP
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - lookup
---

# XLOOKUP Image Guide

Images planned for [XLOOKUP](../../Functions/Lookup%20%26%20Reference/XLOOKUP.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: XLOOKUP Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])` with the four required and optional arguments grouped by color. A note beside the formula reads that the lookup and return ranges must be the same size. |
| Alt Text | An XLOOKUP formula with its arguments grouped into required and optional parts. |
| File Name | XLOOKUP Syntax Anatomy.png |

## Image 2: Match Modes Compared

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 6. |
| Format | Four small panels in a row, one per match mode. |
| Content | Panel 1 (0): an exact match on 100. Panel 2 (-1): the nearest smaller value 62 highlighted. Panel 3 (1): the nearest larger value 145 highlighted. Panel 4 (2): a wildcard pattern `*Lamp*` matching the text Desk Lamp. Each panel is labeled with its match mode number. |
| Alt Text | Four panels showing exact, next smaller, next larger and wildcard matching modes for XLOOKUP. |
| File Name | XLOOKUP Match Modes.png |

## Image 3: Discount Tier Lookup Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the tier table and the formula cell. |
| Content | The tier table in `F2:G5` with the 50 row highlighted, the order quantity 68 in a labeled input cell, and the result 10% in the formula cell. |
| Alt Text | A volume discount table with the 50 unit tier highlighted and an XLOOKUP result of 10% for an order of 68 units. |
| File Name | XLOOKUP Discount Tier Result.png |
