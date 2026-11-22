---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
related:
  - FINDB
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# FINDB Image Guide

Images planned for [FINDB](../../Functions/Text/FINDB.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: FINDB Byte Positions

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two-row diagram of a text string with byte positions. |
| Content | Top row: the characters 農, 歴, 新, 年 each drawn as a wide block labeled with bytes 1 to 2, 3 to 4, 5 to 6 and 7 to 8. Bottom row: the same text with FIND numbering 1, 2, 3, 4. A callout shows that FINDB("新") returns 5 and FIND returns 3. |
| Alt Text | A diagram comparing byte positions and character positions for the Japanese characters 農歴新年. |
| File Name | FINDB Byte Positions.png |

## Image 2: Byte Positions in a Mixed Text String

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a formula and result. |
| Content | Cell A2 holds 農歴新年. Cell B2 holds `=FINDB("新", A2)` showing 5. A note beside the cell reads "Each kanji counts as 2 bytes when the double-byte setting is active." |
| Alt Text | A worksheet showing FINDB returning byte position 5 for the kanji 新 in a Japanese product name. |
| File Name | FINDB Kanji Position.png |
