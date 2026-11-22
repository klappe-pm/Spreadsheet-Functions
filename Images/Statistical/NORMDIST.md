---
domain: Spreadsheet Functions
category: Statistical
subcategory: Legacy Compatibility
related:
  - NORMDIST
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - statistical
---

# NORMDIST Image Guide

Images planned for [NORMDIST](../../Functions/Statistical/NORMDIST.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Normal Curve With Mean and Standard Deviation

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Labeled line chart of a bell curve. |
| Content | A bell curve centered on a vertical line labeled mean (80 mm). Markers at one and two standard deviations (12 mm each) on both sides, labeled standard_dev. |
| Alt Text | A bell curve centered on a mean of 80 with markers one and two standard deviations away on each side. |
| File Name | NORMDIST Normal Curve.png |

## Image 2: Equivalent Calculation Through a Z-Score

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 5 and before Story Problems. |
| Format | Two-column comparison. |
| Content | Left column: NORMDIST(95, 80, 12, TRUE) returns 0.894350. Right column: the value 95 converted to a z-score of 1.25 (95 minus 80, divided by 12), then NORMSDIST(1.25) returns 0.894350. A caption notes that the two results match. |
| Alt Text | Two columns showing that NORMDIST on the raw value and NORMSDIST on the z-score both return 0.894350. |
| File Name | NORMDIST Z Score Equivalent.png |
