---
domain: Spreadsheet Functions
category: Web
subcategory: Web Import
related:
  - IMPORTFEED
date-created: 2025-08-17
date-revised: 2026-11-22
tags:
  - images
  - rss
  - web
---

# IMPORTFEED Image Guide

Images planned for [IMPORTFEED](../../Functions/Web/IMPORTFEED.md). Each marker in the function page (`<!-- Image N -->`) shows where the image goes.

## Image 1: Feed Address and Optional Arguments

| Item | Instruction |
| --- | --- |
| Placement | Syntax section, directly below the syntax code block. |
| Format | Annotated diagram of a formula. |
| Content | The formula `=IMPORTFEED(url, [query], [headers], [num_items])` is shown with four callouts. The `url` callout points to a feed address ending in `feed.xml`, labeled "Required: RSS or Atom feed". The other three callouts are labeled "Optional: what to return", "Optional: header row" and "Optional: number of newest items". |
| Alt Text | A labeled diagram of the IMPORTFEED formula showing the required feed address and the three optional arguments. |
| File Name | IMPORTFEED Syntax Arguments.png |

## Image 2: A Single-Attribute Query

| Item | Instruction |
| --- | --- |
| Placement | Examples section, directly below Example 4. |
| Format | Screenshot of a worksheet. |
| Content | The formula `=IMPORTFEED(...,"items title",FALSE,12)` sits in the first cell of a column. The column below it shows twelve item titles, with no header row. A bracket on the right is labeled "12 items, one column". |
| Alt Text | A worksheet column showing twelve item titles returned by a single-attribute IMPORTFEED query. |
| File Name | IMPORTFEED Single Attribute Titles.png |
