---
domain: Spreadsheet Functions
category: Engineering
subcategory: Number Base Conversion
related:
  - BIN2HEX
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - engineering
  - images
---

# BIN2HEX Image Guide

Images planned for [BIN2HEX](../../Functions/Engineering/BIN2HEX.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=BIN2HEX(number, [places])` with `number` labeled as a binary value and `places` labeled as an optional width, shown in brackets. |
| Alt Text | A BIN2HEX formula with a required binary argument and an optional places argument. |
| File Name | BIN2HEX Syntax Anatomy.png |

## Image 2: Four-Bit Groups to Hex Digits

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Table with a binary and hex column. |
| Content | Rows for 0000 to 1111 with the matching hex digit 0 to F, and a bracket that groups the 8-bit value 10110101 into 1011 and 0101 with the result B5. |
| Alt Text | A table of four-bit binary groups and their hexadecimal digits, with an example that splits 10110101 into B and 5. |
| File Name | BIN2HEX Four Bit Groups.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet. |
| Content | The header table in `A1:B4` with the binary values, the helper column `C2:C4` holding the BIN2HEX results with two-character width, and the labels 7F, 12 and 41 beside the column. |
| Alt Text | A worksheet with three binary header fields converted to two-digit hexadecimal values. |
| File Name | BIN2HEX Packet Header Result.png |
