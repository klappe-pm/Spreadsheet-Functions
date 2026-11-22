---
domain: Spreadsheet Functions
category: Text
subcategory: Text Conversion
related:
  - LENB
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# LENB Image Guide

Images planned for [LENB](../../Functions/Text/LENB.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: LENB Argument Layout

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of one formula. |
| Content | The formula `=LENB(text)` on one line, with the word `text` boxed and labeled "Text or cell reference" and an arrow to an output box labeled "Number of bytes". |
| Alt Text | Diagram of the LENB formula showing one text argument and a byte count output. |
| File Name | LENB Argument Layout.png |

## Image 2: LEN and LENB on the Same Text

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after the Example 3 result. |
| Format | Worksheet screenshot with two formula columns. |
| Content | Cell A2 holds `Tokyo 東京`. Column B shows `=LEN(A2)` with the result 8, and column C shows `=LENB(A2)` with the result 10. The kanji characters in A2 are highlighted, and a note says each kanji takes two bytes. |
| Alt Text | Worksheet row comparing the character count and the byte count of a mixed Latin and kanji string. |
| File Name | LENB LEN Versus Bytes.png |
