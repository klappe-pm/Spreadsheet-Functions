---
domain: Spreadsheet Functions
category: Lookup & Reference
subcategory: Reference Building
related:
  - FORMULATEXT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - formula-audit
  - images
---

# FORMULATEXT Image Guide

Images planned for [FORMULATEXT](../../Functions/Lookup%20%26%20Reference/FORMULATEXT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Formula Bar and Text Output

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated worksheet screenshot. |
| Content | Cell `A3` selected with `=A1+A2` visible in the formula bar, and cell `B3` below it showing the text `=A1+A2`. Arrows connect the formula bar to the text result and label the referenced cell. |
| Alt Text | A worksheet where the formula bar shows a formula and an adjacent cell displays the same formula as text. |
| File Name | FORMULATEXT Formula Bar Output.png |

## Image 2: Labeled Price Column

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the price list with a label column. |
| Content | Columns A to C with the four price rows. Typed prices (45 and 60) are shaded light gray, calculated prices (90 and 65) are shaded light blue, and column C shows Typed, Formula, Typed and Formula. |
| Alt Text | A price list where each row is labeled as a typed price or a formula price, with the formula rows shaded. |
| File Name | FORMULATEXT Price Labels.png |

## Image 3: Locating Formulas With SEARCH

| Item | Instruction |
| --- | --- |
| Placement | Use Cases section, below the Formula Audit Before Handoff code block. |
| Format | Screenshot of a review column. |
| Content | A column of formulas with a neighboring column of TRUE and FALSE results from `ISNUMBER(SEARCH("INDEX", FORMULATEXT(D2)))`. Rows that return TRUE are highlighted. |
| Alt Text | A review column that flags the rows whose formulas contain the function name INDEX. |
| File Name | FORMULATEXT Search Flags.png |
