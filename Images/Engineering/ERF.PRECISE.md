---
domain: Spreadsheet Functions
category: Engineering
subcategory: Error Functions
related:
  - ERF.PRECISE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - images
  - probability
---

# ERF.PRECISE Image Guide

Images planned for [ERF.PRECISE](../../Functions/Engineering/ERF.PRECISE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Area From Zero to the Input Under the Error Function

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Line chart with a shaded area and a mirrored negative side. |
| Content | A bell-shaped curve centered on zero. The area from 0 to a positive x is shaded and labeled `ERF.PRECISE(x)`. The mirror image on the negative side is shaded in a second color and labeled with the negative value, which shows the function is odd. |
| Alt Text | A bell curve with the area from zero to a positive point shaded, and the mirror area on the negative side labeled as the negative result. |
| File Name | ERF PRECISE Area From Zero.png |

## Image 2: Tolerance Band Shares Table

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a worksheet with sigma bands and their shares. |
| Content | Column A holds the bands 0.5, 1.5, and 2.5. Column B shows the shares 0.3829, 0.8664, and 0.9876. The formula `=ERF.PRECISE(A2/SQRT(2))` is visible in the formula bar. |
| Alt Text | A worksheet listing three tolerance bands for bottle fills and the share of fills inside each band. |
| File Name | ERF PRECISE Tolerance Bands.png |
