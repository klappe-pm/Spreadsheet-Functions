---
domain: Spreadsheet Functions
category: Text
subcategory: Double Byte Text
related:
  - RIGHTB
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - double-byte
---

# RIGHTB Image Guide

Images planned for [RIGHTB](../../Functions/Text/RIGHTB.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Byte Count From the Right

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Byte ruler diagram. |
| Content | The text `東京都` with a ruler below it showing two bytes for each kanji. A bracket covers the last four bytes and is labeled num_of_bytes = 4, which covers the kanji 京都. |
| Alt Text | Three kanji with a byte ruler, and the last four bytes bracketed as the characters RIGHTB returns. |
| File Name | RIGHTB Byte Count Ruler.png |

## Image 2: Byte Boundary in a Branch Code

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a branch code and the result. |
| Content | Column A holds `TK001東京都`. Column B holds the RIGHTB formula with num_of_bytes 4 and the result `京都`. A byte ruler sits above the value showing that the four bytes cover two kanji. |
| Alt Text | A branch code in one column and the last two kanji returned by RIGHTB with a byte ruler above. |
| File Name | RIGHTB Branch Code Result.png |

## Image 3: Fixed Width Suffix Layout

| Item | Instruction |
| --- | --- |
| Placement | Use Cases section, above the Byte Limited Field Extracts example. |
| Format | Table diagram of a fixed-width record. |
| Content | A record divided into labeled fields with their byte widths. The trailing field is shaded and labeled with the byte count that RIGHTB extracts from the right. |
| Alt Text | A fixed-width record with its last field shaded to show the bytes that RIGHTB extracts. |
| File Name | RIGHTB Fixed Width Suffix.png |
