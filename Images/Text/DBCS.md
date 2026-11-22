---
category: Text
subcategory: Text Conversion
related:
  - DBCS
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - double-byte
  - images
  - japanese-text
---

# DBCS Image Guide

Images planned for [DBCS](../../Functions/Text/DBCS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Half-Width Versus Full-Width Text

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated worksheet screenshot. |
| Content | Column A with half-width codes such as TOKYO, column C with the formula `=DBCS(B2)` filled down, and the full-width results in column C. A callout points to the width difference. |
| Alt Text | A worksheet column of half-width letters converted to full-width letters by DBCS. |
| File Name | DBCS Half Width To Full Width.png |

## Image 2: Round Trip With ASC

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Three-step flow diagram. |
| Content | Step 1: the half-width word `ABC`. Step 2: DBCS converts it to full-width. Step 3: ASC converts it back, and a check mark shows the result matches the original. |
| Alt Text | A flow diagram showing a word converted to full-width and back to its original form. |
| File Name | DBCS Round Trip With ASC.png |
