---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
related:
  - WEBSERVICE
date-created: 2026-11-22
date-revised: 2026-11-22
tags:
  - web
  - images
---

# WEBSERVICE Image Guide

Images planned for [WEBSERVICE](../../Functions/Web/WEBSERVICE.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: WEBSERVICE Call Flow

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Simple flow diagram. |
| Content | Three boxes in a row: an encoded address in a cell, the WEBSERVICE call, and the raw response in the result cell. Below the call box, a note says the address must be 2,048 characters or fewer. |
| Alt Text | A flow diagram showing an encoded address passed to WEBSERVICE and the raw response returned to a cell. |
| File Name | WEBSERVICE Call Flow.png |

## Image 2: Error Results Panel

| Item | Instruction |
| --- | --- |
| Placement | Examples section, after Example 3. |
| Format | Worksheet screenshot. |
| Content | Four rows of service results. Two show response text and two show the fallback message Service unavailable, with the IFERROR formula visible in the formula bar. |
| Alt Text | A worksheet where failed service calls show the Service unavailable fallback message. |
| File Name | WEBSERVICE Error Fallback.png |

## Image 3: Length Check Table

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, after the Problem 1 answer. |
| Format | Worksheet screenshot. |
| Content | The request table with the length column, the 2105 row highlighted as over the limit, and the COUNTIF result 3 in a labeled output cell. |
| Alt Text | A request table where one address length exceeds 2,048 characters and three fit within the limit. |
| File Name | WEBSERVICE Length Check.png |
