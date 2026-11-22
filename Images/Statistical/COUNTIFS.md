---
domain: Spreadsheet Functions
category: Statistical
subcategory: Counting
related:
  - COUNTIFS
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - counting
  - images
  - statistical
---

# COUNTIFS Image Guide

Images planned for [COUNTIFS](../../Functions/Statistical/COUNTIFS.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: COUNTIFS Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated screenshot of a formula bar. |
| Content | The formula `=COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2], ...)` with each range and each criteria in its own color. Brackets mark the optional pair, and a caption notes that pairs repeat. |
| Alt Text | A COUNTIFS formula with its criteria ranges and criteria highlighted, and the optional pairs marked in brackets. |
| File Name | COUNTIFS Syntax Anatomy.png |

## Image 2: AND Logic in a COUNTIFS Formula

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Screenshot of the order list with a three-column check strip beside it. |
| Content | The order list in `A1:C8`. For the formula in Example 6, each row shows three check marks for East, units of at least 20 and Closed. Rows 4 and 7 have three checks and are shaded. Row 2 shows a cross on the Closed test. |
| Alt Text | An order list where rows that pass all three COUNTIFS tests are shaded and the failing row shows which test it fails. |
| File Name | COUNTIFS AND Logic Checks.png |

## Image 3: Certification Result

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the certification table with the qualifying rows highlighted. |
| Content | The table in `A1:D9`. Rows for Ruiz, Moreau and Reyes are highlighted. The formula `=COUNTIFS(B2:B9, "Support", C2:C9, "Yes", D2:D9, ">=80")` and its result 3 appear in a labeled cell below the table. |
| Alt Text | A certification table with three Support staff who passed with 80 or more highlighted and a COUNTIFS result of 3. |
| File Name | COUNTIFS Certification Result.png |
