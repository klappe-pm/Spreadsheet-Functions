---
domain: Spreadsheet Functions
category: Text
subcategory: Double Byte Text
related:
  - REPLACEB
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - double-byte
---

# REPLACEB Image Guide

Images planned for [REPLACEB](../../Functions/Text/REPLACEB.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Byte Positions in a Mixed Text String

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Byte ruler diagram. |
| Content | A text string with one double-byte kanji and two single-byte letters. Above each character, a ruler shows its byte numbers: the kanji covers bytes 1 and 2, the letters cover bytes 3 and 4. A caption reads REPLACEB counts these numbers, not characters. |
| Alt Text | A mixed text string with a ruler above it showing that a double-byte character spans two byte positions. |
| File Name | REPLACEB Byte Ruler.png |

## Image 2: Byte Positions in an Invoice Reference

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a byte ruler above the reference. |
| Content | The reference `Invoice-2024` in one cell, with byte numbers 1 to 12 above the characters. Bytes 9 to 12 are highlighted as the year. |
| Alt Text | An invoice reference with byte positions shown above it and the year bytes highlighted. |
| File Name | REPLACEB Invoice Byte Positions.png |

## Image 3: Fixed Width Record Layout

| Item | Instruction |
| --- | --- |
| Placement | Use Cases section, above the Byte Limited Field Updates example. |
| Format | Table diagram of a fixed-width record. |
| Content | A record divided into labeled fields with their byte widths. The field to be replaced is shaded and labeled with its start byte and width. |
| Alt Text | A fixed-width record layout with one field shaded to show the bytes that REPLACEB replaces. |
| File Name | REPLACEB Fixed Width Layout.png |
