---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - BETADIST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# BETADIST Image Guide

Images planned for [BETADIST](../../Functions/Statistical/BETADIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled diagram of the formula bar. |
| Content | The formula `=BETADIST(x, alpha, beta, [A], [B])` with x, alpha and beta required, and A and B optional. A banner above the formula reads "Compatibility function. Use BETA.DIST in new work." |
| Alt Text | A labeled BETADIST formula with a compatibility note that points to BETA.DIST. |
| File Name | BETADIST Syntax Anatomy.png |

## Image 2: Legacy and Replacement Formulas Side by Side

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Side by side worksheet screenshots. |
| Content | Left: the legacy formula `=BETADIST(0.2, 2, 5)` with the result 0.3446. Right: the replacement formula `=BETA.DIST(0.2, 2, 5, TRUE)` with the same result 0.3446, and a caption reading "Same result". |
| Alt Text | Two formulas, BETADIST and BETA.DIST, each returning 0.3446 for the same inputs. |
| File Name | BETADIST Replacement Comparison.png |
