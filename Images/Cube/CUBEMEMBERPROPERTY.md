---
category: Cube
subcategory: OLAP Members
related:
  - CUBEMEMBERPROPERTY
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - cube
  - images
---

# CUBEMEMBERPROPERTY Image Guide

Images planned for [CUBEMEMBERPROPERTY](../../Functions/Cube/CUBEMEMBERPROPERTY.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Connection, Member and Property Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the function call. |
| Content | The formula `=CUBEMEMBERPROPERTY(connection, member_expression, property)` with each argument in its own box. The property box shows two forms: text in quotes and a cell reference. |
| Alt Text | A diagram of the CUBEMEMBERPROPERTY arguments showing that the property can be text or a cell reference. |
| File Name | CUBEMEMBERPROPERTY Arguments.png |

## Image 2: Property Lookup Filled Down a Column

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly after Example 4. |
| Format | Screenshot of a worksheet with three columns. |
| Content | Column A holds member expressions, column B holds the property name Owner, and column C shows the returned owner names. The formula bar shows the formula in C2 with cell references. A fourth row is highlighted to show the Check member result from Example 4 in column D. |
| Alt Text | A worksheet with member expressions, an Owner property column, and returned owner names filled down a column. |
| File Name | CUBEMEMBERPROPERTY Filled Down.png |

## Image 3: Owner Lookup Column

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet. |
| Content | Column A lists Gadgets, Widgets, Cables and Sensors. Column B shows Blake, Avery, Casey and Not found. The Sensors row is outlined to show the missing owner. |
| Alt Text | A worksheet listing four products with owners Blake, Avery and Casey, and Not found for Sensors. |
| File Name | CUBEMEMBERPROPERTY Owner Lookup.png |
