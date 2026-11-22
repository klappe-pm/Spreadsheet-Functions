---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Classic Lookup
related:
  - MATCH
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - lookup
---

# MATCH Image Guide

Images planned for [MATCH](../../Functions/Lookup%20%26%20Reference/MATCH.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Match Type Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Three-row diagram with a formula strip on top. |
| Content | The formula `=MATCH(lookup_value, lookup_array, [match_type])` across the top, with each argument boxed and labeled. Below it, three short rows labeled 1, 0 and -1. Each row shows its rule in one phrase: largest value at or below, exact match, and smallest value at or above, with the required sort order beside each. |
| Alt Text | A diagram of the MATCH formula with its three arguments labeled and the three match type rules listed beneath. |
| File Name | MATCH Match Type Anatomy.png |

## Image 2: Approximate Match Tier Ladder

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 3. |
| Format | Vertical bar chart drawn as a ladder of tiers. |
| Content | Five steps labeled with the thresholds 0, 10000, 25000, 50000 and 100000. A marker sits on the 67500 level, which falls in the step labeled 50000. A label beside the marker reads position 4. |
| Alt Text | A ladder of five sales thresholds with a marker at 67500 that sits in the step at 50000, labeled position 4. |
| File Name | MATCH Approximate Tier Ladder.png |

## Image 3: Discount Tier Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, directly below the Problem 1 answer. |
| Format | Screenshot of the discount table with the result cell visible. |
| Content | The discount table in `A1:B5` with the 50 row highlighted. The quantity 75 is in `D2`. The result cell shows 10% and a small note reads position 3 from MATCH. |
| Alt Text | A discount table with the 50 unit tier highlighted, and an order quantity of 75 returning a 10 percent discount. |
| File Name | MATCH Discount Tier Result.png |
