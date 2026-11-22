---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
related:
  - MIDB
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# MIDB Image Guide

Images planned for [MIDB](../../Functions/Text/MIDB.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: MIDB Byte Counting

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of one formula with a byte ruler. |
| Content | The formula `=MIDB(text, start_num, num_bytes)` with each argument labeled. Below it, the text `ABC東京` is shown with a byte ruler under it: A, B and C each marked as one byte, and each kanji marked as two bytes. |
| Alt Text | Diagram of the MIDB formula with a byte ruler showing single-byte letters and two-byte kanji. |
| File Name | MIDB Byte Counting.png |

## Image 2: Character Count Versus Byte Count

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 2 result. |
| Format | Two stacked rows of character boxes. |
| Content | The text `東京都庁舎` shown as five character boxes. The top row, labeled MID, shades four characters from position 2 to give `京都庁舎`. The bottom row, labeled MIDB, shades only the first two kanji, which together take four bytes, to give `京都`. |
| Alt Text | Two rows comparing MID, which takes four characters, with MIDB, which takes four bytes and returns two kanji. |
| File Name | MIDB Character Versus Byte Count.png |
