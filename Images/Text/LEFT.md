---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
related:
  - LEFT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# LEFT Image Guide

Images planned for [LEFT](../../Functions/Text/LEFT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: LEFT Arguments and Output

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a text string. |
| Content | The string `Hello World` drawn as separate character boxes. A bracket over the first five boxes is labeled `num_chars = 5`, and an arrow points to the result `Hello`. A callout notes that omitting num_chars returns one character. |
| Alt Text | A diagram showing LEFT returning the first five characters of Hello World. |
| File Name | LEFT Arguments Output.png |

## Image 2: Country Prefixes From Order Codes

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a source column and a result column. |
| Content | Column A lists US-2026-0457, CA-2026-0112 and MX-2026-0389. Column B holds `=LEFT(A2, 2)` filled down and shows US, CA and MX. The formula bar shows the formula in B2. |
| Alt Text | A worksheet where LEFT extracts the two-letter country prefix from three order codes. |
| File Name | LEFT Country Prefix.png |
