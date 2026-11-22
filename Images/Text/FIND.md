---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
related:
  - FIND
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - text
  - images
---

# FIND Image Guide

Images planned for [FIND](../../Functions/Text/FIND.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: FIND Arguments and Position Count

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a text string with character positions. |
| Content | The string `j.lee@northwind.com` written as individual characters, numbered 1 to 18 above them. The at sign at position 6 is highlighted. Below, the formula `=FIND("@", "j.lee@northwind.com")` with arrows labeled search_for, text_to_search and starting_at (optional, default 1). |
| Alt Text | A character-by-character diagram showing that FIND returns position 6 for the at sign in an email address. |
| File Name | FIND Arguments Position.png |

## Image 2: Locating the Second Hyphen in a SKU

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with a SKU and helper cells. |
| Content | Cell A2 holds `BLU-2025-XL`. Helper cell B2 holds `=FIND("-", A2)` showing 4, and cell C2 holds `=FIND("-", A2, B2+1)` showing 9. Both hyphens are outlined in the SKU and their positions are labeled. |
| Alt Text | A SKU with the first hyphen at position 4 and the second hyphen at position 9 outlined. |
| File Name | FIND Second Hyphen.png |
