---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - FINV
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - statistical
  - images
---

# FINV Image Guide

Images planned for [FINV](../../Functions/Statistical/FINV.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Legacy Inverse Mapped to Its Replacement

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Two-column diagram. |
| Content | On the left, `=FINV(probability, deg_freedom1, deg_freedom2)` labeled "legacy name." On the right, `=F.INV.RT(probability, deg_freedom1, deg_freedom2)` labeled "current name, same result." |
| Alt Text | A diagram showing that FINV and F.INV.RT take the same arguments and return the same right-tail value. |
| File Name | FINV Legacy Mapping.png |

## Image 2: Right-Tail Cutoff on the F Curve

| Item | Instruction |
| --- | --- |
| Placement | Examples section, between Example 2 and Example 3. |
| Format | Line chart of an F curve with the right tail shaded. |
| Content | The curve for 3 and 12 degrees of freedom, with the right tail beyond the cutoff shaded to 0.10. The cutoff is labeled 2.6055, and the caption reads "the 10 percent cutoff from FINV." |
| Alt Text | An F distribution curve with the top 10 percent of the area shaded beyond a marked cutoff. |
| File Name | FINV Right Tail Cutoff.png |
