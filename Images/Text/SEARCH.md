---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
related:
  - SEARCH
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - text
---

# SEARCH Image Guide

Images planned for [SEARCH](../../Functions/Text/SEARCH.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Find Text and Within Text Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula with its arguments. |
| Content | The formula `=SEARCH(find_text, within_text, [start_num])` with find_text shaded blue, within_text shaded orange and start_num outlined with a dashed line. A small example underneath shows the word `Report` inside `Quarterly Report` with the position 11 marked. |
| Alt Text | A SEARCH formula with its three arguments labeled and an example that finds a word inside a phrase. |
| File Name | SEARCH Argument Anatomy.png |

## Image 2: Position Result and Error Case

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, before the first problem heading. |
| Format | Two-row worksheet screenshot. |
| Content | Top row: the formula `=SEARCH("e", "Quarterly Report")` with the result 6 and the matched character highlighted. Bottom row: the formula `=SEARCH("z", "Quarterly Report")` with the result `#VALUE!` and a note that the text was not found. |
| Alt Text | Two SEARCH formulas, one returning the position of a letter and one returning an error because the letter is missing. |
| File Name | SEARCH Position and Error.png |

## Image 3: Email Domain Extraction Result

| Item | Instruction |
| --- | --- |
| Placement | Use Cases section, above the Email Domain Extraction example. |
| Format | Screenshot of a worksheet with the email address and extracted domain. |
| Content | Column A holds `maria.chen@northwind.com`. Column B shows the position 11 from the SEARCH formula. Column C shows the domain `northwind.com` from the MID formula. The at sign is highlighted in column A. |
| Alt Text | An email address with its at sign position found and the domain extracted in the next column. |
| File Name | SEARCH Email Domain Result.png |
