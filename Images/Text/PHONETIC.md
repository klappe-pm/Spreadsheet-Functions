---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
related:
  - PHONETIC
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - text
  - images
---

# PHONETIC Image Guide

Images planned for [PHONETIC](../../Functions/Text/PHONETIC.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: PHONETIC Reference Argument

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of one formula. |
| Content | The formula `=PHONETIC(reference)` with the argument boxed and labeled "Cell or range with furigana". Two small examples below it: one adjacent range marked "Upper-left cell is used" and one nonadjacent selection marked "Returns #N/A". |
| Alt Text | Diagram of the PHONETIC formula with its single reference argument and the adjacent and nonadjacent cases. |
| File Name | PHONETIC Reference Argument.png |

## Image 2: Phonetic Guide Stored in a Cell

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 1 result. |
| Format | Worksheet screenshot with the Phonetic Guide visible above the cell. |
| Content | Cell A2 shows a Japanese name with its furigana displayed above the kanji through the Phonetic Guide. A second cell holds `=PHONETIC(A2)`, and its result shows only the reading. A callout explains that the kanji itself is not returned. |
| Alt Text | Worksheet cell with a Japanese name and its furigana, next to a PHONETIC formula that returns only the reading. |
| File Name | PHONETIC Stored Phonetic Guide.png |
