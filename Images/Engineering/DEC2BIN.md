---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
related:
  - DEC2BIN
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - binary
  - images
---

# DEC2BIN Image Guide

Images planned for [DEC2BIN](../../Functions/Engineering/DEC2BIN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Decimal, Binary and Padding

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Three-column diagram. |
| Content | Left column: the decimal value 9. Middle column: the binary digits 1001. Right column: the same value padded to four characters by the `places` argument, shown as a second example that pads 1 to `0001`. A caption reads `DEC2BIN(9,4) returns 1001`. |
| Alt Text | A diagram showing decimal 9 converted to the four-digit binary string 1001. |
| File Name | DEC2BIN Decimal To Binary.png |

## Image 2: Relay Channel Status Table

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with channel numbers and their binary strings. |
| Content | Column A holds 5, 18, and 200. Column B shows `00000101`, `00010010`, and `11001000`. The formula `=DEC2BIN(A2,8)` is visible in the formula bar. |
| Alt Text | A worksheet listing three relay channel numbers and their eight-digit binary strings. |
| File Name | DEC2BIN Relay Channels.png |
