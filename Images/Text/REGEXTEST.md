---
domain: Spreadsheet Functions
category: Text
subcategory: Regular Expressions
related:
  - REGEXTEST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - regex
---

# REGEXTEST Image Guide

Images planned for [REGEXTEST](../../Functions/Text/REGEXTEST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Pattern Argument Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of one formula with three labeled arguments. |
| Content | The formula `=REGEXTEST(text, pattern, case_sensitivity)` with the text argument shaded blue, the pattern argument shaded orange and the optional case argument outlined with a dashed line. A caption under the pattern reads `^ start and $ end anchors`. |
| Alt Text | A REGEXTEST formula with its text, pattern and optional case sensitivity arguments labeled. |
| File Name | REGEXTEST Argument Anatomy.png |

## Image 2: Part Number Results Column

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with two columns. |
| Content | Column A lists `AB-1234`, `ab-1234`, `AB-12345`, `XY-9081` and `Q-1000`. Column B shows TRUE, FALSE, FALSE, TRUE and FALSE. The count formula in a cell below reads 2. |
| Alt Text | A list of part numbers with TRUE and FALSE results from a pattern test and a count of 2 below. |
| File Name | REGEXTEST Part Number Results.png |

## Image 3: Email Format Check Layout

| Item | Instruction |
| --- | --- |
| Placement | Use Cases section, above the Email Format Checks example. |
| Format | Two-column table diagram. |
| Content | Left column lists sample addresses, one with a missing at sign and one valid. Right column shows the TRUE or FALSE result for each, with a note that the pattern checks shape only. |
| Alt Text | A table of sample email addresses with a column of pattern test results beside them. |
| File Name | REGEXTEST Email Check Layout.png |
