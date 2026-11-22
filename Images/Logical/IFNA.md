---
domain: Spreadsheet Functions
category: Logical
subcategory: Error Handling
related:
  - IFNA
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - logical
  - images
---

# IFNA Image Guide

Images planned for [IFNA](../../Functions/Logical/IFNA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=IFNA(value, value_if_na)` with value boxed and labeled Checked for #N/A, and value_if_na boxed and labeled Returned only for #N/A. Both arguments are marked required. |
| Alt Text | A formula with IFNA, its two required arguments labeled, and a note that only #N/A is replaced. |
| File Name | IFNA Syntax Anatomy.png |

## Image 2: Replacement Versus Pass-Through

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two worksheet snippets side by side. |
| Content | Left: a VLOOKUP with a missing key showing the replacement text Not Found, labeled #N/A caught. Right: a division by zero showing #DIV/0!, labeled not caught, passed through. |
| Alt Text | Two worksheet examples. The left one replaces a missing lookup with text, and the right one shows a division error still visible. |
| File Name | IFNA Replacement Versus Pass Through.png |

## Image 3: Region Lookup Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the account table beside the region list. |
| Content | The account column with a formula column showing East, West, Unassigned, and North. The Unassigned cell is highlighted, and the region list in F1:G4 is outlined. |
| Alt Text | An account table where AC-31 shows Unassigned and the other accounts show their regions. |
| File Name | IFNA Region Lookup Results.png |
