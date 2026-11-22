---
domain: Spreadsheet Functions
category: Information
subcategory: Type Checks
related:
  - ISOMITTED
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - information
---

# ISOMITTED Image Guide

Images planned for [ISOMITTED](../../Functions/Information/ISOMITTED.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a single formula. |
| Content | The formula `=ISOMITTED(argument)` with `ISOMITTED` labeled as the function name, `argument` labeled as a LAMBDA parameter, and a caption that reads "TRUE when the parameter was left out of the call". |
| Alt Text | A formula diagram showing ISOMITTED with one argument that names a LAMBDA parameter. |
| File Name | ISOMITTED Syntax Anatomy.png |

## Image 2: Optional Argument Pattern

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 2 answer. |
| Format | Diagram of a LAMBDA call with two branches. |
| Content | A box for the LAMBDA definition with parameters `amount` and `rate`, an IF branch labeled ISOMITTED(rate) pointing to a default path (amount times 0.9) and a supplied path (amount times 1 minus rate). A caption reads "Left blank: default path. Value given: supplied path." |
| Alt Text | A flow diagram in which an omitted rate sends the calculation down the default path and a supplied rate uses the rate value. |
| File Name | ISOMITTED Optional Argument Pattern.png |
