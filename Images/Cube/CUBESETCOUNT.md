---
category: Cube
subcategory: OLAP Sets
related:
  - CUBESETCOUNT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - cube
  - images
---

# CUBESETCOUNT Image Guide

Images planned for [CUBESETCOUNT](../../Functions/Cube/CUBESETCOUNT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Set Argument as a Cell Reference

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram with two cells. |
| Content | Cell A3 is outlined and labeled set, and it contains a CUBESET formula shown in the formula bar. A second cell with the formula CUBESETCOUNT(A3) has an arrow pointing back to A3 and a label that reads the count of items. |
| Alt Text | A diagram showing that CUBESETCOUNT refers to a cell that holds a CUBESET formula. |
| File Name | CUBESETCOUNT Set Reference.png |

## Image 2: Count Compared With an Expected Size

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly after Example 4. |
| Format | Screenshot of a worksheet with a sorted and an unsorted set. |
| Content | Two columns of reps, one in cube order and one sorted by sales. Both count cells show the same number, and a note beside them says that sorting does not change the count. |
| Alt Text | Two lists of reps with the same count, showing that sorting does not change the number of items. |
| File Name | CUBESETCOUNT Sorted Count.png |

## Image 3: Planned Count Compared With the Set

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of a small planning sheet. |
| Content | Column B lists the four West stores, cell B2 shows the count 4, and cell E2 holds the planned value 5. The result cell shows Check set in a highlighted color. |
| Alt Text | A planning sheet where the count of 4 does not match the planned 5, so the result reads Check set. |
| File Name | CUBESETCOUNT Plan Check.png |
