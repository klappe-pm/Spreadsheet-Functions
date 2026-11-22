---
domain: Spreadsheet Functions
category: Text
subcategory: Text Measurement
related:
  - LEN
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# LEN Image Guide

Images planned for [LEN](../../Functions/Text/LEN.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: LEN Counting Characters

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a text string as individual character boxes. |
| Content | The string `Hello World` drawn as 11 boxes, with the space box shaded and labeled "counts as 1". Below it, the formula `=LEN("Hello World")` and the result `11`. |
| Alt Text | A diagram showing that LEN counts each letter and the space in Hello World, giving 11. |
| File Name | LEN Counting Characters.png |

## Image 2: Message Length Check

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a message and a length result. |
| Content | Cell A2 holds "Your order ships Monday, thanks!". Cell B2 holds `=LEN(A2)` and displays 32. Cell C2 holds `=IF(B2 <= 160, "Fits", "Too long")` and displays "Fits". |
| Alt Text | A worksheet where LEN counts a 32 character order message and a check cell confirms it fits the 160 character limit. |
| File Name | LEN Message Length.png |
