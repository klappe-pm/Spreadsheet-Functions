---
category: Cube
subcategory: OLAP Values
related:
  - CUBEVALUE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - cube
  - images
---

# CUBEVALUE Image Guide

Images planned for [CUBEVALUE](../../Functions/Cube/CUBEVALUE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Connection and Slicer Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the function call. |
| Content | The formula `=CUBEVALUE(connection, [member_expression1], [member_expression2], ...)`. Each member expression is shown as a slicer, drawn as a filter panel with a region and a measure selected, and an ellipsis box indicates more slicers can follow. |
| Alt Text | A diagram of CUBEVALUE with a connection and several slicer arguments shown as filter panels. |
| File Name | CUBEVALUE Slicer Arguments.png |

## Image 2: Region Totals Filled Down a Column

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly after Example 4. |
| Format | Screenshot of a worksheet with a region column and a total column. |
| Content | Column A lists the region expressions for East, West and North, column B shows the Sales Amount totals returned by the formula, and the formula bar shows the CUBEVALUE formula with $B$1 and A2 as references. |
| Alt Text | A worksheet with region expressions in one column and the returned Sales Amount totals in the next. |
| File Name | CUBEVALUE Region Totals.png |

## Image 3: Region Total and Share Summary

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a summary table. |
| Content | Three regions with totals 14200, 9800 and 6400, a total row showing 30400, and a result cell for East showing 14200 with a note that it is about 46.7 percent of the combined total. |
| Alt Text | A summary table of three regional totals with the East total of 14200 highlighted against a combined total of 30400. |
| File Name | CUBEVALUE East Share.png |
