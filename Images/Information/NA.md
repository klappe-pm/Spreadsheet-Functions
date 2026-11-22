---
domain: Spreadsheet Functions
category: Information
subcategory: Error Checks
related:
  - NA
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - information
  - images
---

# NA Image Guide

Images planned for [NA](../../Functions/Information/NA.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Syntax Anatomy

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of the formula. |
| Content | The formula `=NA()` with `NA` labeled as the function and the empty parentheses labeled as required. A callout notes that the function has no arguments and returns `#N/A`. |
| Alt Text | Diagram of the NA formula showing the function name, the required empty parentheses and the `#N/A` result. |
| File Name | NA Syntax Anatomy.png |

## Image 2: Error Spreading Through a Total

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 6. |
| Format | Screenshot of a worksheet with three value cells and two formula cells. |
| Content | Cells B2 and B4 hold 45 and 52, cell D3 holds `=IF(B3="", NA(), B3)` and shows `#N/A`, and the formula `=AVERAGE(B2, D3, B4)` shows `#N/A` in a highlighted cell. An arrow runs from D3 to the average to show the error passing through. |
| Alt Text | A worksheet where one `#N/A` in a source cell makes an average formula return `#N/A`. |
| File Name | NA Error Propagation.png |

## Image 3: Hourly Sensor Table

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Screenshot of the sensor table. |
| Content | Hour, Reading and the helper column with 21 through 24 and two `#N/A` cells in rows for hours 3 and 7. The formula `=SUMPRODUCT(ISNA(C2:C9)*1)` is shown in the formula bar with the result 2 highlighted. |
| Alt Text | A sensor table where two missing readings show as `#N/A` in a helper column and a count of 2 results from ISNA. |
| File Name | NA Hourly Sensor Table.png |
