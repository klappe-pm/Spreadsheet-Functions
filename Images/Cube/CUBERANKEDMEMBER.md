---
category: Cube
subcategory: OLAP Members
related:
  - CUBERANKEDMEMBER
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - cube
  - images
---

# CUBERANKEDMEMBER Image Guide

Images planned for [CUBERANKEDMEMBER](../../Functions/Cube/CUBERANKEDMEMBER.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Connection, Set, Rank and Caption Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the function call. |
| Content | The formula `=CUBERANKEDMEMBER(connection, set_expression, rank, [caption])`. A small ranked list beside the rank argument shows position 1 at the top, position 2 below it and position 3 below that. |
| Alt Text | A diagram of the CUBERANKEDMEMBER arguments with a ranked list showing positions 1, 2 and 3. |
| File Name | CUBERANKEDMEMBER Arguments.png |

## Image 2: Top Five Ranks Filled Down a Column

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly after Example 4. |
| Format | Screenshot of a worksheet with a column of ranked names. |
| Content | Column D lists five rep names in rank order in D2 to D6. The formula bar shows the ROWS formula in D2 with the set reference in B2, and the rank values 1 to 5 appear as a faint helper column to the left. |
| Alt Text | A worksheet with five ranked rep names filled down a column from a sorted set. |
| File Name | CUBERANKEDMEMBER Top Five.png |

## Image 3: Sorted Set Ranking Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a sales table with a result cell. |
| Content | The five reps with sales 5100, 4200, 3900, 3100 and 2750 are shown sorted from highest to lowest, with the second row highlighted as Avery. The result cell shows Avery. |
| Alt Text | A sorted list of five reps with Avery highlighted in second place. |
| File Name | CUBERANKEDMEMBER Second Seller.png |
