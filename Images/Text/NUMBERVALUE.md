---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
related:
  - NUMBERVALUE
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - text
  - images
---

# NUMBERVALUE Image Guide

Images planned for [NUMBERVALUE](../../Functions/Text/NUMBERVALUE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: NUMBERVALUE Separator Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of one formula. |
| Content | The formula `=NUMBERVALUE(text, [decimal_separator], [group_separator])` with the two separator arguments in a highlighted box labeled "Pass both explicitly". An arrow points from each separator to a sample number such as `3.456,78` with its decimal comma and group period marked. |
| Alt Text | Diagram of the NUMBERVALUE formula showing the text argument and the optional decimal and group separator arguments. |
| File Name | NUMBERVALUE Separator Arguments.png |

## Image 2: Reading the Separators in a Number

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 1 result. |
| Format | Worksheet screenshot with the formula bar visible. |
| Content | Cell A2 holds `3.456,78`. The formula bar shows `=NUMBERVALUE(A2, ",", ".")`, and the result cell shows `3456.78`. The period is struck through in A2 with a note that it is ignored because it comes before the decimal comma. |
| Alt Text | Worksheet cell with a European formatted number, the NUMBERVALUE formula and the converted result. |
| File Name | NUMBERVALUE Reading Separators.png |
