---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
related:
  - ISDATE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISDATE Image Guide

Images planned for [ISDATE](../../Functions/Information/ISDATE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula in Google Sheets. |
| Content | The formula `=ISDATE(value)` with `value` labeled as the text in quotation marks or a cell reference, and two outcome boxes: TRUE for a date and FALSE for anything else. |
| Alt Text | An ISDATE formula with its value argument labeled and the TRUE and FALSE outcomes shown. |
| File Name | ISDATE Syntax Anatomy.png |

## Image 2: Date Text Check Results

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 4. |
| Format | Screenshot of a Google Sheets worksheet. |
| Content | A column of four text entries: "July 20 1969", "July", "Feb 30" and a real date cell. Next to each, an ISDATE formula shows TRUE, FALSE, FALSE and TRUE. |
| Alt Text | A Google Sheets column where ISDATE returns TRUE for a full date and a real date and FALSE for a month name and an impossible date. |
| File Name | ISDATE Date Text Check Results.png |
