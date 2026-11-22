---
domain: Spreadsheet Functions
category: Engineering
subcategory: Bitwise Operations
related:
  - BITLSHIFT
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - engineering
  - images
---

# BITLSHIFT Image Guide

Images planned for [BITLSHIFT](../../Functions/Engineering/BITLSHIFT.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=BITLSHIFT(number, shift_amount)` with `number` labeled as a whole number and `shift_amount` labeled as the places to move, with a note that a negative value shifts right. |
| Alt Text | A BITLSHIFT formula with a whole-number argument and a shift amount argument. |
| File Name | BITLSHIFT Syntax Anatomy.png |

## Image 2: Left Shift Bit Diagram

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Two binary rows with an arrow between them. |
| Content | The top row shows 1 (0001) and the lower row shows the result of a two-place left shift, 0100 (4), with the two new zeros on the right highlighted. A short caption reads each left shift doubles the value. |
| Alt Text | A binary row shifted two places to the left with two zeros added on the right, equal to four times the original value. |
| File Name | BITLSHIFT Left Shift Diagram.png |

## Image 3: Results Panel for the Story Problems

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet. |
| Content | The board table in `A1:C4` with raw counts and shifts, the helper column `D2:D4` holding the BITLSHIFT results 12, 40 and 14, and the SUM total 66 in `D5` with a label. |
| Alt Text | A worksheet with three board counts scaled by BITLSHIFT in a helper column and a total of 66. |
| File Name | BITLSHIFT Sensor Scaling Result.png |
