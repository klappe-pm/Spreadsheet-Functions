---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
related:
  - ISTEXT
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISTEXT Image Guide

Images planned for [ISTEXT](../../Functions/Information/ISTEXT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=ISTEXT(value)` with `ISTEXT` labeled as the function name, `value` labeled as the value to test, and a caption that reads "TRUE for text, including numbers stored as text". |
| Alt Text | A formula diagram showing ISTEXT with one value argument and a TRUE or FALSE result. |
| File Name | ISTEXT Syntax Anatomy.png |

## Image 2: Note Flagging Results

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Screenshot of the delivery log with the label column beside the notes. |
| Content | The Notes column in `B1:B6` holds Late, 14, Paid, 0 and Hold. Column C holds `=IF(ISTEXT(B2),"Note","No note")` filled down, showing Note, No note, Note, No note, Note. |
| Alt Text | A delivery log in which the rows with text notes are labeled Note and the rows with numbers are labeled No note. |
| File Name | ISTEXT Note Flagging Results.png |
