---
category: Cube
subcategory: OLAP Members
related:
  - CUBEKPIMEMBER
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - cube
  - images
---

# CUBEKPIMEMBER Image Guide

Images planned for [CUBEKPIMEMBER](../../Functions/Cube/CUBEKPIMEMBER.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Connection, KPI Name and Property Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the function call. |
| Content | The formula `=CUBEKPIMEMBER(connection, kpi_name, kpi_property, [caption])` with each argument in its own box. Under `kpi_property`, a small table lists 1 KPIValue, 2 KPIGoal, 3 KPIStatus, 4 KPITrend, 5 KPIWeight and 6 KPICurrentTimeMember. The optional caption box is drawn with a dashed outline. |
| Alt Text | A diagram of the CUBEKPIMEMBER arguments with the six KPI property codes listed beneath the property argument. |
| File Name | CUBEKPIMEMBER Arguments.png |

## Image 2: KPI Value Inside CUBEVALUE

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly after Example 3. |
| Format | Flow diagram with three boxes and two arrows. |
| Content | A box labeled CUBEKPIMEMBER with KPIValue inside, an arrow into a box labeled CUBEVALUE, and an arrow out to a box labeled Number in cell. The diagram shows the KPI component passed as the member expression. |
| Alt Text | A flow diagram in which a KPI component from CUBEKPIMEMBER feeds CUBEVALUE and returns a number to the cell. |
| File Name | CUBEKPIMEMBER Value Flow.png |

## Image 3: Monthly Profit Against Goal Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a small worksheet. |
| Content | A two-row table with Value 84000 and Goal 90000, and one result cell showing -6000 with the formula bar displaying the subtraction of the two CUBEVALUE formulas. |
| Alt Text | A worksheet showing a KPI value of 84000 against a goal of 90000 and a result of -6000. |
| File Name | CUBEKPIMEMBER Goal Gap.png |
