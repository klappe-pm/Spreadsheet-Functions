---
category: Cube
subcategory: OLAP Members
related:
  - CUBEMEMBER
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - cube
  - images
---

# CUBEMEMBER Image Guide

Images planned for [CUBEMEMBER](../../Functions/Cube/CUBEMEMBER.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Connection, Member Expression and Caption Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the function call. |
| Content | The formula `=CUBEMEMBER(connection, member_expression, [caption])` with each argument labeled. Beside the member expression, a sample MDX string `[Geography].[Region].&[East]` is shown with the bracketed hierarchy parts color coded. |
| Alt Text | A diagram of the CUBEMEMBER arguments with a sample MDX member expression for the East region. |
| File Name | CUBEMEMBER Arguments.png |

## Image 2: Member Passed Into CUBEVALUE

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly after Example 4. |
| Format | Side by side diagram of two formulas. |
| Content | Left: a CUBEMEMBER cell that shows the caption East. Right: the CUBEVALUE formula with the CUBEMEMBER call inside its third argument, with an arrow from the MDX expression to the slicer. A note reads that CUBEVALUE uses the expression, not the displayed caption. |
| Alt Text | Two linked formulas showing that CUBEVALUE reads the MDX expression inside CUBEMEMBER rather than the caption. |
| File Name | CUBEMEMBER Slicer Expression.png |

## Image 3: Region Check Column

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with two columns. |
| Content | Column A lists East, West, Central and North. Column B shows East, West, Not in cube and North. The Central row is highlighted, and the formula bar shows the IFERROR and CUBEMEMBER formula. |
| Alt Text | A worksheet with four region names and a checked column in which Central shows Not in cube. |
| File Name | CUBEMEMBER Region Check.png |
