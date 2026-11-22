---
domain: Spreadsheet Functions
category: Text
subcategory: Double Byte Text
related:
  - SEARCHB
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - double-byte
---

# SEARCHB Image Guide

Images planned for [SEARCHB](../../Functions/Text/SEARCHB.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Byte Positions Versus Character Positions

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Side by side byte ruler and character ruler. |
| Content | The text `大阪本社` shown twice. Left: a byte ruler numbering 1 to 8, with 本 starting at byte 5. Right: a character ruler numbering 1 to 4, with 本 at character 3. Captions read byte position and character position. |
| Alt Text | Two rulers for the same kanji text, one counting bytes and one counting characters, showing different positions for the same character. |
| File Name | SEARCHB Byte and Character Rulers.png |

## Image 2: Double-Byte Position Comparison

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Screenshot of a worksheet with two result columns. |
| Content | Column A holds `大阪本社`. Column B shows `=SEARCHB("本", A2)` with the result 5. Column C shows `=SEARCH("本", A2)` with the result 3. |
| Alt Text | A kanji string with SEARCHB returning 5 and SEARCH returning 3 for the same character. |
| File Name | SEARCHB Position Comparison.png |

## Image 3: Branch Name Byte Positions

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a branch name and the result. |
| Content | Column A holds `東京本部`. Column B shows the SEARCHB formula with the result 5. A byte ruler above the text marks byte 5 under the 本 character. |
| Alt Text | A branch name with the byte position of its office marker found and marked on a ruler. |
| File Name | SEARCHB Branch Name Bytes.png |
