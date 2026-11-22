---
domain: Spreadsheet Functions
category: Text
subcategory: Text Extraction
related:
  - RIGHT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - text
---

# RIGHT Image Guide

Images planned for [RIGHT](../../Functions/Text/RIGHT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Text and Character Count Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a text string and the formula. |
| Content | The string `INV-00457` with the last five characters `00457` bracketed and labeled num_chars = 5. Above the formula `=RIGHT(text, [num_chars])`, arrows point to text and num_chars with the optional bracket visible. |
| Alt Text | A text string with its last five characters bracketed and a RIGHT formula with its two arguments labeled. |
| File Name | RIGHT Text and Count Anatomy.png |

## Image 2: Invoice Suffix Extraction

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with three invoice numbers and their extracted suffixes. |
| Content | Column A lists `INV-00457`, `ACME-88213` and `PO-5`. Column B shows the RIGHT formula and its results `00457`, `88213` and `PO-5`. The third row is highlighted to show that a short value returns in full. |
| Alt Text | Three invoice numbers with the last five characters extracted, and the short one returned in full. |
| File Name | RIGHT Invoice Suffix Extraction.png |

## Image 3: File Routing Flow

| Item | Instruction |
| --- | --- |
| Placement | Use Cases section, above the File Extension Routing example. |
| Format | Flow diagram with three decision boxes. |
| Content | A file name enters the first decision, which checks whether its last four characters equal `xlsx`. Yes leads to the spreadsheet queue. No leads to a second decision checking the last three characters for `pdf`, then to the PDF queue or manual review. |
| Alt Text | A flow chart that routes files by checking the last characters of their names. |
| File Name | RIGHT File Routing Flow.png |
