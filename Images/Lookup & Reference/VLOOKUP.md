---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Classic Lookup
related:
  - VLOOKUP
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - lookup
---

# VLOOKUP Image Guide

Images planned for [VLOOKUP](../../Functions/Lookup%20%26%20Reference/VLOOKUP.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: VLOOKUP Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of the formula bar. |
| Content | The formula `=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])` with each argument underlined in a different color. Under the formula, a small table range is outlined and numbered 1 to 3 across its columns to show how col_index_num counts from the key column. |
| Alt Text | A VLOOKUP formula with each argument labeled and a table range whose columns are numbered from the lookup column. |
| File Name | VLOOKUP Syntax Anatomy.png |

## Image 2: Exact Versus Approximate Match

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Side by side diagram of two sorted and unsorted key columns. |
| Content | Left: an exact match with the key 80 highlighted and the label FALSE. Right: an approximate match with the search value 85 placed between 80 and 90, and the row for 80 highlighted with the label TRUE. |
| Alt Text | Two diagrams comparing an exact match on one key with an approximate match that returns the largest key below the search value. |
| File Name | VLOOKUP Exact Versus Approximate.png |

## Image 3: Shipping Rate Lookup Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the rate table and the formula cell. |
| Content | The band table in `E1:F5` with the 10 kg row highlighted, the input 12 in `B2`, and the formula result 9.00 in a labeled output cell. |
| Alt Text | A weight band table with the 10 kg band highlighted and a VLOOKUP result of 9.00 for a 12 kg parcel. |
| File Name | VLOOKUP Shipping Rate Result.png |
