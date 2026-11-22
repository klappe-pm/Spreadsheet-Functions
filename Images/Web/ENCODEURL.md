---
domain: Spreadsheet Functions
category: Web
subcategory: URL Tools
related:
  - ENCODEURL
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - url-encoding
  - web
---

# ENCODEURL Image Guide

Images planned for [ENCODEURL](../../Functions/Web/ENCODEURL.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Encoding a Value in a Cell

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated worksheet screenshot. |
| Content | Cell `A2` holds `Hello, World!`, and cell `B2` holds `=ENCODEURL(A2)` with the result `Hello%2C%20World%21`. Arrows point from the input to the output cell. |
| Alt Text | A worksheet cell with an encoded result from ENCODEURL, where the comma, space and exclamation mark are shown as percent codes. |
| File Name | ENCODEURL Encode Cell Value.png |

## Image 2: Joining an Encoded Value to a Fixed Address

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 3. |
| Format | Diagram with three labeled blocks in a row. |
| Content | Block one shows the fixed address `https://example.com/search?q=` in a blue box. Block two shows the value `red shoes` in a green box, passed through ENCODEURL. Block three shows the joined result `red%20shoes` in a gray box, with an ampersand between blocks one and two. |
| Alt Text | A diagram showing a fixed web address joined with an encoded search term, with the encoded term turned into percent codes. |
| File Name | ENCODEURL Joined Search Link.png |

## Image 3: Product Search Links in a Catalog

| Item | Instruction |
| --- | --- |
| Placement | Story Problems section, directly below the Problem 1 answer. |
| Format | Screenshot of a two-column worksheet. |
| Content | Column A lists `Oak Desk, 120 cm` and `Blue Ceramic Mug, Large`. Column B shows the encoded results `Oak%20Desk%2C%20120%20cm` and `Blue%20Ceramic%20Mug%2C%20Large`, with the formula bar showing `=ENCODEURL(A2)`. |
| Alt Text | A two-column worksheet that pairs product names with their encoded versions created by ENCODEURL. |
| File Name | ENCODEURL Product Search Links.png |
