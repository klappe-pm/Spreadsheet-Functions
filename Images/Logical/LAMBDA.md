---
domain: Spreadsheet Functions
category: Logical
subcategory: Lambda Helpers
related:
  - LAMBDA
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - logical
  - images
---

# LAMBDA Image Guide

Images planned for [LAMBDA](../../Functions/Logical/LAMBDA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated formula bar screenshot. |
| Content | The formula `=LAMBDA([parameter1, parameter2, ...,] calculation)` with the parameters in one color and the calculation, marked as the last argument, in another. |
| Alt Text | A formula bar showing a LAMBDA with its parameters and calculation labeled. |
| File Name | LAMBDA Syntax Anatomy.png |

## Image 2: Inline Versus Named LAMBDA Calls

| Item | Instruction |
| --- | --- |
| Placement | Examples section, before Example 3. |
| Format | Two panels side by side. |
| Content | Left: `LAMBDA(price,price*0.9)(B2)` with the argument in parentheses highlighted. Right: a Name Manager entry for DiscountPrice and the call `=DiscountPrice(B2,0.1)` in a cell. |
| Alt Text | Two panels, one showing an inline LAMBDA call and one showing a named function called from a cell. |
| File Name | LAMBDA Inline Versus Named.png |

## Image 3: Shipping Cost Worksheet

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of a small worksheet. |
| Content | Parcel and weight columns, the ShipCost results 11, 23 and 35 in column C, and the total 69 in a labeled cell. The P3 row shows its billed weight capped at 20 kg. |
| Alt Text | A parcel list with three shipping costs and a total of 69. |
| File Name | LAMBDA Shipping Cost Worksheet.png |
