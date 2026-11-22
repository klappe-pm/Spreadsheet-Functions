---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - FDIST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# FDIST Image Guide

Images planned for [FDIST](../../Functions/Statistical/FDIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Legacy Function Mapped to Its Replacement

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two-column diagram. |
| Content | On the left, the formula `=FDIST(x, deg_freedom1, deg_freedom2)` with a label "legacy name." On the right, `=F.DIST.RT(x, deg_freedom1, deg_freedom2)` with a label "current name, same result." An equals sign joins the two. |
| Alt Text | A diagram showing that FDIST and F.DIST.RT take the same arguments and return the same value. |
| File Name | FDIST Legacy Mapping.png |

## Image 2: Legacy and Replacement Results Side by Side

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Screenshot of two result columns. |
| Content | A small table with the inputs 2.2, 8 and 12, one column for FDIST and one for F.DIST.RT, both showing 0.1055, and a check mark between them. |
| Alt Text | A worksheet showing FDIST and F.DIST.RT returning the same 0.1055 for the same inputs. |
| File Name | FDIST Versus F.DIST.RT.png |
