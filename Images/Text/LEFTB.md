---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
related:
  - LEFTB
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# LEFTB Image Guide

Images planned for [LEFTB](../../Functions/Text/LEFTB.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: LEFTB Bytes Compared With LEFT Characters

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two-row diagram. |
| Content | Top row: the text `熊本` drawn as two wide blocks, each labeled with 2 bytes, and a bracket over the first block labeled `LEFTB(…, 2)` returning 熊. Bottom row: the same text with a bracket over both blocks labeled `LEFT(…, 2)` returning 熊本. A caption reads "LEFTB counts bytes, LEFT counts characters." |
| Alt Text | A diagram comparing LEFTB, which returns one kanji for a two-byte limit, with LEFT, which returns two kanji for a two-character limit. |
| File Name | LEFTB Bytes Versus Characters.png |

## Image 2: Byte Limit Applied to a Japanese Name

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a formula and result. |
| Content | Cell A2 holds 熊本県. Cell B2 holds `=LEFTB(A2, 4)` and displays 熊本. A note beside it reads "Each kanji is 2 bytes, so 4 bytes hold two characters. 県 does not fit." |
| Alt Text | A worksheet where LEFTB returns the first two kanji of 熊本県 for a four-byte limit. |
| File Name | LEFTB Japanese Name.png |
