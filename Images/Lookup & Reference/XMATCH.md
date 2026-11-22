---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Modern Lookup
related:
  - XMATCH
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - lookup
---

# XMATCH Image Guide

Images planned for [XMATCH](../../Functions/Lookup%20%26%20Reference/XMATCH.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: XMATCH Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])` with each argument underlined. Beside it, a row of five cells is numbered 1 to 5 to show that the result is a position, not a value. |
| Alt Text | An XMATCH formula with its arguments labeled and a row of numbered cells showing position. |
| File Name | XMATCH Syntax Anatomy.png |

## Image 2: Position Versus Value Returned

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 5. |
| Format | Two worksheet panels side by side. |
| Content | Left: the product list in `A2:B6` with the code P-300 highlighted and a result cell showing 3. Right: the same row in the wider table with the Filing Cabinet price 145 highlighted, showing that INDEX turns the position into a value. |
| Alt Text | A product list with the third row highlighted and the position 3 returned, next to the price from that row. |
| File Name | XMATCH Position Versus Value.png |

## Image 3: Last Match Search Direction

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Two arrows drawn over a vertical list of eight shipment statuses. |
| Content | The list of statuses in `B2:B9` with the three Late rows marked. A down arrow labeled search first to last points to shipment 2. An up arrow labeled search last to first points to shipment 7 with the result 7 in a labeled cell. |
| Alt Text | A list of eight shipment statuses with the last Late entry found by searching from the bottom. |
| File Name | XMATCH Last Match Direction.png |
